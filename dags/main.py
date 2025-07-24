from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def helloWorld():
        print("Hello World")
              
with DAG(dag_id="hello_world_dag",
         start_date=datetime(2024,3,24),
         schedule="@daily",
         catchup=False) as dag:
    
# DAG(
#     dag_id="hello_world_dag",
#     schedule="@daily",
#     start_date=datetime(2023, 1, 1),
# )    
    

    task1 = PythonOperator(
            task_id="hello_world",
            python_callable=helloWorld)