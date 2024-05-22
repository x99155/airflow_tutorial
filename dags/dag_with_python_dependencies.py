from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'x99155',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

def get_requests():
    import requests
    print(f"Requests version: {requests.__version__}")



def scrape_afrik():
    import requests
    from bs4 import BeautifulSoup
    url = 'https://www.afrik.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    # Trouver tous les articles
    articles = soup.find_all('div', {'class': 'td_module_mob_1 td_module_wrap td-animation-stack td-meta-info-hide'})
    print(articles)


with DAG(
    dag_id='dag_with_python_dependencies_v2',
    default_args=default_args,
    description='Ajout des dépendances Python dans votre environnement Apache Airflow en utilisant Docker',
    start_date=datetime(2024, 5, 21),
    schedule_interval='@daily'
) as dag: 
    
    task1 = PythonOperator(
        task_id='get_requests',
        python_callable=get_requests
    )

    task2 = PythonOperator(
        task_id='scrape_afrik',
        python_callable=scrape_afrik
    )

    task1 >> task2