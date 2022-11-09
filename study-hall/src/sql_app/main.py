from fastapi import FastAPI, Depends, status, Response
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from repositories import UsuarioRepository, GrupoRepository, EventoRepository, PostRepository, UsuarioGrupoRepository
from models import Usuario, UsuarioGrupo, Grupo, Evento, Post
from typing import List
import models
import schemas

app  = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get('/')
def read_root():
    return {"message": "Welcome to FastAPI"}

# Usuário ------------------------------------------------------------------------------

@app.post('/createUser', status_code=status.HTTP_201_CREATED)
async def createUser(request: schemas.UsuarioRequest, db: Session = Depends(get_db)):
    user = UsuarioRepository.save(db, Usuario(**request.dict()))
    return schemas.UsuarioResponse.from_orm(user)

@app.post('/getUser', response_model=schemas.UsuarioResponse)
async def getUser(user_id: schemas.SimpleID, db: Session = Depends(get_db)):
    user = UsuarioRepository.find_by_id(db, user_id.id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail = "Usuário não encontrado."
        )
    return schemas.UsuarioResponse.from_orm(user)

@app.post('/getUserGroups', response_model=List[schemas.UsuarioResponse])
async def getUserGroups(group_id: schemas.SimpleID, db: Session = Depends(get_db)):
    users = UsuarioRepository.find_by_group_id(db, group_id.id)
    return [schemas.UsuarioResponse.from_orm(user) for user in users]

# Grupos -----------------------------------------------------------------------------------

@app.post('/createGroup', status_code=status.HTTP_201_CREATED)
async def createGroup(request: schemas.GrupoRequest, db: Session = Depends(get_db)):
    group = GrupoRepository.save(db, Grupo(**request.dict()))
    UsuarioGrupoRepository.save(db, UsuarioGrupo(user_id = group.user_id, group_id = group.group_id))
    return schemas.GrupoResponse.from_orm(group)

@app.post('/getGroup', response_model=schemas.GrupoResponse)
async def getGroup(id: schemas.SimpleID, db: Session = Depends(get_db)):
    group = GrupoRepository.find_by_id(db, id.id)
    return schemas.GrupoResponse.from_orm(group)

@app.post('/getGroupInterest', response_model=List[schemas.GrupoResponse])
async def getGroupInterest(interest: schemas.Interest, db: Session = Depends(get_db)):
    groups = GrupoRepository.find_by_interest(db, interest.interest)
    return [schemas.GrupoResponse.from_orm(group) for group in groups]

# Eventos ----------------------------------------------------------------------------------------
@app.post('/createEvent', status_code=status.HTTP_201_CREATED)
async def createEvent(request: schemas.EventoRequest, db: Session = Depends(get_db)):
    event = EventoRepository.save(db, Evento(**request.dict()))
    return schemas.EventoResponse(event)

@app.post('/getEventGroup', response_model=List[schemas.EventoResponse])
async def getGroup(group_id: schemas.SimpleID, db: Session = Depends(get_db)):
    events = EventoRepository.find_by_group(db, group_id.id)
    return [schemas.EventoResponse.from_orm(event) for event in events]

# Posts --------------------------------------------------------------------------------------------
@app.post('/createPost', status_code=status.HTTP_201_CREATED)
async def createPost(request: schemas.PostRequest, db: Session = Depends(get_db)):
    post = PostRepository.save(db, Post(**request.dict()))
    return schemas.PostResponse.from_orm(post)

@app.post('/getPosts', response_model=List[schemas.PostResponse])
async def getPosts(group_id: schemas.SimpleID, db: Session = Depends(get_db)):
    posts = PostRepository.find_by_group_id(db, group_id.id)
    return [schemas.PostResponse.from_orm(post) for post in posts]

# Extra --------------------------------------------------------------------------------------------
@app.post('/login')
async def login(request: schemas.Login, db: Session = Depends(get_db)):
    user = UsuarioRepository.login(db, request.username, request.password)
    if user:
        return schemas.UsuarioResponse.from_orm(user)
    else:
        return status.HTTP_401_UNAUTHORIZED

@app.post('/addUserGroup', status_code=status.HTTP_201_CREATED)
async def createPost(request: schemas.UserGroupRequest, db: Session = Depends(get_db)):
    UsuarioGrupoRepository.save(db, UsuarioGrupo(**request.dict()))
