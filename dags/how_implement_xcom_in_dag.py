from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

# XCom (pour "cross-communication") est un mécanisme dans Airflow permettant 
# aux tâches d'échanger des messages ou des données. 
# Les XComs permettent aux tâches de passer des données entre elles dans le contexte d'une exécution de DAG

default_args = {
    'owner': 'x99155',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


def push_function(**kwargs):
    # Pousse une valeur vers XCom
    kwargs['ti'].xcom_push(key='my_key', value='my_value')

def pull_function(**kwargs):
    # Tire une valeur de XCom
    value = kwargs['ti'].xcom_pull(key='my_key', task_ids='push_task')
    print(f"Valeur tirée : {value}")



with DAG(
    dag_id='how_to_use_xcom',
    default_args=default_args,
    description='Exemple d\'utilisation de xcom',
    start_date=datetime(2024, 5, 21),
    schedule_interval='@daily'
) as dag: 
    push_task = PythonOperator(
        task_id='push_task',
        python_callable=push_function,
        provide_context=True
    )

    pull_task = PythonOperator(
        task_id='pull_task',
        python_callable=pull_function,
        provide_context=True
    )

    push_task >> pull_task