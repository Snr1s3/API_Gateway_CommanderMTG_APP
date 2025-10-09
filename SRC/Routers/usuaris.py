from typing import List
from fastapi import APIRouter, HTTPException

import requests
from SRC.Models.usuari import *
from SRC.Routers import settings

router = APIRouter(
    prefix="/usuaris",
    tags=["usuari"],
    responses={404: {"description": "Not found"}}
)
url = settings.API_LOGIN_URL+"/usuaris/"


@router.get("/", response_model=List[Usuari])
async def  all_usuaris_s():
    try:
        response = requests.get(f'{url}')
        if response.status_code == 200:
            usuari_data = response.json()
            return [Usuari(**c) for c in usuari_data]
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")
@router.get("/{id}", response_model=Usuari)
async def  usuari__by_id(
        id: int
    ):
    try:
        response = requests.get(f'{url}{id}')
        if response.status_code == 200:
            usuari__data = response.json()
            return Usuari(**usuari__data)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")
@router.post("/", response_model=Usuari)
async def  create_new_usuari(
        usuari: CreateUsuari
    ):
    try:
        response = requests.post(f'{url}', json=usuari.model_dump())
        if response.status_code == 200:
            usuari_data = response.json()
            return Usuari(**usuari_data)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")

@router.post("/authenticate/", response_model=Usuari)
async def  authenticate(
        usuari: AuthRequest
    ):
    try:
        response = requests.post(f'{url}authenticate/', json=usuari.model_dump())
        if response.status_code == 200:
            usuari_data = response.json()
            return Usuari(**usuari_data)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")

  
@router.put("/{id}/name", response_model=Usuari)
async def  update_usuari_name(
        id: int,
        usuari_: UpdateUsuariName
    ):
    try:
        response = requests.put(f'{url}{id}/name', json=usuari_.model_dump())
        if response.status_code == 200:
            usuari__data = response.json()
            return Usuari(**usuari__data)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=f"{str(e)}")

@router.put("/{id}/mail", response_model=Usuari)
async def  update_usuari_mail(
        id: int,
        usuari_: UpdateUsuariMail
    ):
    try:
        response = requests.put(f'{url}{id}/mail', json=usuari_.model_dump())
        if response.status_code == 200:
            usuari__data = response.json()
            return Usuari(**usuari__data)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=f"{str(e)}")

@router.put("/{id}/password", response_model=Usuari)
async def  update_usuari_password(
        id: int,
        usuari_: UpdateUsuariPassword
    ):
    try:
        response = requests.put(f'{url}{id}/password', json=usuari_.model_dump())
        if response.status_code == 200:
            usuari__data = response.json()
            return Usuari(**usuari__data)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=f"{str(e)}")






@router.delete("/{id}", response_model=dict)
async def  delete_usuari(
        id: int
    ):
    try:
        response = requests.delete(f'{url}{id}')
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")