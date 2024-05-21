from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'x99155',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

def greet(name, period):
    print(f"Assalamou a3leykoum {name}! I'll introduce you to my family on {period} inshallah!")


def get_name():
    return 'Queen'

with DAG(
    dag_id='our_dag_with_python_operator_v7',
    default_args=default_args,
    description='Dag fonctionnant avec le connecteur python operator',
    start_date=datetime(2024, 5, 21),
    schedule_interval='@daily'
) as dag: 
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={'name': 'Queen!', 'period': 'june or july'}, # permet de passer des parametre à la fonction
        provide_context=True
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name,
        provide_context=True
    )

    task2 >> task1