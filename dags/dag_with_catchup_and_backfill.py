from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator  # Pour Airflow 2.0.0 et versions ultérieures

# Le paramètre catchup contrôle si un DAG doit rattraper les exécutions manquées depuis la date de début (start_date). 
# Par défaut, catchup est activé (catchup=True), 
# ce qui signifie que si un DAG est activé après sa start_date, Airflow exécutera toutes les instances manquées pour atteindre la date actuelle.
with DAG(
    dag_id='x99155',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False  # Désactivation de catchup pour éviter les exécutions rétroactives
) as dag:
    
    # Tâche Bash qui imprime un message de félicitations
    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo 'wish both of you (king&queen) happy wedding inshallah!'"
    )

    task3
