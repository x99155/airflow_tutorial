from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'x99155',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id='our_first_dag_v8',
    default_args=default_args,
    description='Mon premier dag',
    start_date=datetime(2024, 5, 21, 10),
    schedule_interval='@daily'
) as dag:
    
    # Tâches Bash qui imprime des messages
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo 'as salam a3leykoum queen!'"
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo 'wa aleykoum assalam king! how are you doing?'"
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo 'wish both of you (king and queen) happy wedding inshallah!'"
    )

    # Task dependency method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # Task dependency method 2
    # task1 >> task2
    # task1 >> task3

    # Task dependency method 3
    task1 >> [task2, task3]