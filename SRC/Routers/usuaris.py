from typing import List
from fastapi import APIRouter, HTTPException, Request

import requests
from Models.usuari import UsuariLogin
from Routers import settings

router = APIRouter(
    prefix="/usuaris",
    tags=["usuari"],
    responses={404: {"description": "Not found"}}
)
url_login = settings.API_LOGIN_URL+"/usuaris/"
url_crud = settings.API_LOGIN_URL+"/usuaris/"
prefix_login = "/login"
prefix_crud = "/crud"

## LOGIN
@router.get(prefix_login+"/login/", response_model=List[UsuariLogin])
async def  all_usuaris_select():
    try:
        response = requests.get(f'{url_login}')
        if response.status_code == 200:
            usuari_data = response.json()
            return [UsuariLogin(**c) for c in usuari_data]
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")
@router.get(prefix_login+"/{id}", response_model=UsuariLogin)
async def  usuari_by_id(id: int):
    try:
        response = requests.get(f'{url_login}{id}')
        if response.status_code == 200:
            usuari_data = response.json()
            return UsuariLogin(**usuari_data)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")
@router.post(prefix_login+"/", response_model=UsuariLogin)
async def  create_new_usuari(usuari: CreateUsuariLogin):
    try:
        response = requests.post(f'{url_login}', json=usuari.model_dump())
        if response.status_code == 200:
            usuari_data = response.json()
            return UsuariLogin(**usuari_data)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")

@router.post("/authenticate/", response_model=UsuariLogin)
async def  authenticate(
        usuari: AuthRequest
    ):
    try:
        response = requests.post(f'{url_login}authenticate/', json=usuari.model_dump())
        if response.status_code == 200:
            usuari_data = response.json()
            return UsuariLogin(**usuari_data)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")

@router.put(prefix_login+"/{id}/name", response_model=UsuariLogin)
async def  update_usuari_name(id: int,usuari: UpdateUsuariName):
    try:
        response = requests.put(f'{url_login}{id}/name', json=usuari.model_dump())
        if response.status_code == 200:
            usuari_data = response.json()
            return UsuariLogin(**usuari_data)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=f"{str(e)}")

@router.put(prefix_login+"/{id}/mail", response_model=UsuariLogin)
async def  update_usuari_mail(id: int,usuari: UpdateUsuariMail):
    try:
        response = requests.put(f'{url_login}{id}/mail', json=usuari.model_dump())
        if response.status_code == 200:
            usuari_data = response.json()
            return UsuariLogin(**usuari_data)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=f"{str(e)}")

@router.put(prefix_login+"/{id}/password", response_model=UsuariLogin)
async def  update_usuari_password(id: int,usuari: UpdateUsuariPassword):
    try:
        response = requests.put(f'{url_login}{id}/password', json=usuari.model_dump())
        if response.status_code == 200:
            usuari_data = response.json()
            return UsuariLogin(**usuari_data)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=f"{str(e)}")

@router.delete(prefix_login+"/{id}", response_model=dict)
async def  delete_usuari(id: int):
    try:
        response = requests.delete(f'{url_login}{id}')
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")

## CRUD

@router.get(prefix_crud+"/", response_model=List[Usuari])
async def  all_usuaris_select_crud(request: Request):
    try:
        query_string = str(request.url.query)
        target_url = f"{url_crud}?{query_string}" if query_string else url_crud
        response = requests.get(target_url)
        if response.status_code == 200:
            usuari_data = response.json()
            return [Usuari(**c) for c in usuari_data]
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")

@router.put(prefix_crud+"/{id}", response_model=Usuari)
async def update_usuari(id: int, usuari: UpdateUsuari):
    try:
        response = requests.put(f'{url_crud}{id}', json=usuari.model_dump())
        if response.status_code == 200:
            usuari_data = response.json()
            return Usuari(**usuari_data)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")

@router.delete(prefix_crud+"/{id}", response_model=dict)
async def  delete_usuari(id: int):
    try:
        response = requests.delete(f'{url_login}{id}')
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")