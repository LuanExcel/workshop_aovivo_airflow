from time import sleep
from airflow.decorators import dag, task
from airflow.models.baseoperator import chain
from datetime import datetime

@dag(
        dag_id="minha_setima_dag",
        description="minha etl braba",
        schedule="* * * * *",
        start_date=datetime(2025,1,1),
        catchup=False #bascfill
)

def minha_setima_dag():

    @task
    def primeira_atividade():
        return "Elyflow nao precisa de XCOM"

    @task
    def segunda_atividade(response):
        print(response)
        sleep(2)

    @task
    def terceira_atividade():
        print("minha terceira atividade!")
        sleep(2)

    @task
    def quarta_atividade():
        print("pipeline finalizou")
    

    t1 = primeira_atividade()
    t2 = segunda_atividade(t1)
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    chain(t1, t2, t3, t4)
    

minha_setima_dag()

