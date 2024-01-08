from fastapi import FastAPI 
from fastapi.params import Body

 # primeiros passos. 
app = FastAPI() 
 

# a seguir temos o path operation ou route: 
@app.get("/") # request do método get de HTTP
def root(): 
    return {"message": "Hello World"} 

# função: é a definição de função normal como no python 
    # antes de def podemos colocar a keyword async: necessária para testes assíncronos. 
    # o que a função retornar é o que o usuário receberá. 
# decorator: transforma a função em uma path operation. Se torna algo utilizável para o FastAPI 
    # app é a instancia do FastAPI que criamos acima 
    # get é um method de request de HTTP (https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) 
    # '/' é pra fazer parte do path do navegador.  
        # Sabemos que barra no fim do endereço nao altera nada; Ainda é o root path... 
        # mas podemos colocar o que quizermos ali pra compor o http ex: ("/tutorial")

@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}

# método GET serve para recuperar informações
    # obs.: ORDEM IMPORTA: se colocamos os mesmo path em path operation para duas funções diferentes,
    #  o algoritmo vai percorrer o código e usar o primeiro match
    #  o mais acima no código.


@app.post("/createposts")
def create_posts(variable_name: dict = Body(...)):
    print(variable_name)
    return {"message": f"title {variable_name['title']} content {variable_name['content']}"}

