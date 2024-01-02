from fastapi import FastAPI 

 # primeiros passos. 
app = FastAPI() 
 

# a seguir temos o path operation ou route: 
@app.get("/") 
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
