from typing import List
from fastapi import APIRouter, Depends, HTTPException

import requests
from SRC.Models.partida import *
from SRC.Routers import settings

router = APIRouter(
    prefix="/partides",
    tags=["partides"],
    responses={404: {"description": "Not found"}}
)
url = settings.API_MTG_URL+"/partides/"


@router.get("/", response_model=List[Partida])
async def  all_partides(
        partida:SelectAllPartida=Depends(),
    ):
    try:
        options = None
        if partida.pag is not None:
            options = f"?pag={partida.pag}"
        if partida.limit is not None:
            if options is None:
                options = f"?limit={partida.limit}"
            else:
                options += f"&limit={partida.limit}"
        if partida.winner is not None:
            if options is None:
                options = f"?partida={partida.winner}"
            else:
                options += f"&partida={partida.winner}"
        if options is None:
            response = requests.get(f'{url}', json=partida.model_dump())
        else:
            response = requests.get(f'{url}{options}', json=partida.model_dump())
        if response.status_code == 200:
            partida_data = response.json()
            return [Partida(**c) for c in partida_data]
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")
@router.get("/{id}", response_model=Partida)
async def  partida_by_id(
        id: int
    ):
    try:
        response = requests.get(f'{url}{id}')
        if response.status_code == 200:
            partida_data = response.json()
            return Partida(**partida_data)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")
@router.post("/", response_model=Partida)
async def  create_new_partida(
        partida: CreatePartida
    ):
    try:
        response = requests.post(f'{url}', json=partida.model_dump())
        if response.status_code == 200:
            partida_data = response.json()
            return partida(**partida_data)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")

@router.put("/{id}", response_model=Partida)
async def  update_partida(
        id: int,
        partida: UpdatePartida
    ):
    try:
        response = requests.put(f'{url}{id}', json=partida.model_dump())
        if response.status_code == 200:
            partida_data = response.json()
            return Partida(**partida_data)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=f"{str(e)}")
@router.delete("/{id}", response_model=dict)
async def  delete_partida(
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