from typing import List
from fastapi import APIRouter, Depends, HTTPException

import requests
from SRC.Models.usuari_commander import *
from SRC.Routers import settings

router = APIRouter(
    prefix="/usuaris_commanders",
    tags=["usuari_commander"],
    responses={404: {"description": "Not found"}}
)
url = settings.API_MTG_URL+"/usuaris_commanders/"

@router.get("/", response_model=List[UsuariCommander])
async def  all_usuaris_commanders(
        usuari_commander:SelectAllUsuariCommander=Depends(),
    ):
    try:
        options = None
        if usuari_commander.pag is not None:
            options = f"?pag={usuari_commander.pag}"
        if usuari_commander.limit is not None:
            if options is None:
                options = f"?limit={usuari_commander.limit}"
            else:
                options += f"&limit={usuari_commander.limit}"
        if usuari_commander.id_usuari is not None:
            if options is None:
                options = f"?id_usuari={usuari_commander.id_usuari}"
            else:
                options += f"&id_usuari={usuari_commander.id_usuari}"
        if usuari_commander.id_commander is not None:
            if options is None:
                options = f"?id_commander={usuari_commander.id_commander}"
            else:
                options += f"&id_commander={usuari_commander.id_commander}"
        if usuari_commander.id_partida is not None:
            if options is None:
                options = f"?id_partida={usuari_commander.id_partida}"
            else:
                options += f"&id_partida={usuari_commander.id_partida}"
        
        if options is None:
            print(url)
            response = requests.get(f'{url}', json=usuari_commander.model_dump())
        else:
            print(url+options)
            response = requests.get(f'{url}{options}', json=usuari_commander.model_dump())
        if response.status_code == 200:
            usuari_commander_data = response.json()
            return [UsuariCommander(**c) for c in usuari_commander_data]
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")



@router.get("/name_count/", response_model=List[UsuariCommanderNomCount])
async def  all_usuaris_commanders_name_count(
        usuari_commander:SelectAllUsuariCommander=Depends(),
    ):
    try:
        options = None
        if usuari_commander.pag is not None:
            options = f"?pag={usuari_commander.pag}"
        if usuari_commander.limit is not None:
            if options is None:
                options = f"?limit={usuari_commander.limit}"
            else:
                options += f"&limit={usuari_commander.limit}"
        if usuari_commander.id_usuari is not None:
            if options is None:
                options = f"?id_usuari={usuari_commander.id_usuari}"
            else:
                options += f"&id_usuari={usuari_commander.id_usuari}"
        if usuari_commander.id_commander is not None:
            if options is None:
                options = f"?id_commander={usuari_commander.id_commander}"
            else:
                options += f"&id_commander={usuari_commander.id_commander}"
        if usuari_commander.id_partida is not None:
            if options is None:
                options = f"?id_partida={usuari_commander.id_partida}"
            else:
                options += f"&id_partida={usuari_commander.id_partida}"
        
        if options is None:
            response = requests.get(f'{url}name_count/', json=usuari_commander.model_dump())
        else:
            print(url+options)
            response = requests.get(f'{url}name_count/{options}', json=usuari_commander.model_dump())
        if response.status_code == 200:
            usuari_commander_data = response.json()
            return [UsuariCommanderNomCount(**c) for c in usuari_commander_data]
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")


@router.get("/{id}", response_model=UsuariCommander)
async def  usuari_commander_by_id(
        id: int
    ):
    try:
        response = requests.get(f'{url}{id}')
        if response.status_code == 200:
            usuari_commander_data = response.json()
            return UsuariCommander(**usuari_commander_data)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")
    
@router.post("/", response_model=UsuariCommander)
async def  create_new_usuari_commander(
        usuari_commander: CreateUsuariCommander
    ):
    try:
        response = requests.post(f'{url}', json=usuari_commander.model_dump())
        if response.status_code == 200:
            usuari_commander_data = response.json()
            return UsuariCommander(**usuari_commander_data)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")
    
@router.put("/{id}", response_model=UsuariCommander)
async def  update_usuari_commander(
        id: int,
        usuari_commander: UpdateUsuariCommander
    ):
    try:
        response = requests.put(f'{url}{id}', json=usuari_commander.model_dump())
        if response.status_code == 200:
            usuari_commander_data = response.json()
            return UsuariCommander(**usuari_commander_data)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=f"{str(e)}")

@router.delete("/{id}", response_model=dict)
async def  delete_usuari_commander(
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