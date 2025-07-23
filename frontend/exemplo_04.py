import streamlit as st
import pandas as pd
import subprocess

# Função para carregar os dados do arquivo csv
def load_data():
    df = pd.read_csv("logfile.log")
    return df

# função para eecutar script python
def run_python_script():
    subprocess.run("python pipeline/pipeline.py")

# Layout do aplicativo Streamlit
def main():
    st.title('Visualização de Logs e execução de Scripts')    
    #st.image("pics/Airflowlogo.png")

    # Carregar os dados do arquivo csv
    df = load_data()

    st.write("Logs de Execução:", df)

    # Botão para atualizar os dados
    if st.button("Atualizar Dados"):
        df = load_data()
        st.write("Dados Atualizados com Sucesso!")

    # Botão para executar o script Phyton
    if st.button("Executar Script Python"):
        run_python_script()
        st.write("Script Python executado com sucesso!")

if __name__ == "__main__":
      main()