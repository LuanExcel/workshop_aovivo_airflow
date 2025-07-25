from time import sleep
from airflow.decorators import dag, task
from datetime import datetime

@dag(
        dag_id="minha_quinta_dag",
        description="minha etl braba",
        schedule="* * * * *",
        start_date=datetime(2025,1,1),
        catchup=False #bascfill
)

def minha_quinta_dag():

    @task
    def primeira_atividade():
        print("minha primeira atividade!")
        sleep(2)

    @task
    def segunda_atividade():
        print("minha segunda atividade!")
        sleep(2)

    @task
    def terceira_atividade():
        print("minha terceira atividade!")
        sleep(2)

    @task
    def quarta_atividade():
        print("pipeline finalizou")
    

    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    # Isso quer dizer q t2 e t3 dependem da carga de t1
    t1.set_downstream([t2, t3]) 

    # Libera a t4 para carga
    t3.set_upstream(t4)
    

minha_quinta_dag()

