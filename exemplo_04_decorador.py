def minha_funcao_decoradora(funcao_decorada):
    def funcao_wrapper():
        print("e dormir melhor") ## Adiciona uma outra funcionalidade na minha funcao
        # adicionar funcionalidade de API
        # PYDANTIC ADICIONA FUNCIONALIDADE DE DATA QUALITY
        funcao_decorada()
    return funcao_wrapper

@minha_funcao_decoradora
def funcao_cuidados():
    print("temos que cuidar da nossa saúde")

funcao_cuidados()
