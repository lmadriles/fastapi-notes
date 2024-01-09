from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI() 
 
# Define 
class Post(BaseModel): # classe herda BaseModel
    title: str
    content: str
    user: int
    published: bool = True # field opcional com valor default
    likes: Optional[int] = None # field opcional mas não queremos default atribuido.


@app.get("/") # request do método get de HTTP
def root(): 
    return {"message": "Hello World"} 

@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}

@app.post("/createposts")
def create_posts(new_post: Post): # recebe a classe e valida os dados (quais e seus formatos)
    print(new_post) # objeto de classe pydantic model
    print(new_post.likes) # valor de likes
    print(new_post.dict()) # objeto convertido pra dict
    
    return {"message": f"title: {new_post.title}"} # new_post['title'] não funciona aqui

    # se usuário fornece dado que não está na classe: não entra na função;
    # não fornece dado que está na classe e não é usado na função: nada acontece
    # não fornece dado que está na classe mas é usado na função:
        # erro: 422 Unprocessable Entity; msg: "field required";
    # usuário fornece objeto com tipo diferente do especificado: 
        # se for inteiro pra string, o algo converte
        # se for outro tipo: 422 Unprocessable Entity; 
            # msg: "value is not a valid integer"; 
            # type: "type_error_integer"; 


