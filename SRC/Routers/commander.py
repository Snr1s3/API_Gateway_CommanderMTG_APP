from typing import List
from fastapi import APIRouter, Depends, HTTPException

import requests
from SRC.Models.commander import *
from SRC.Routers import settings

router = APIRouter(
    prefix="/commanders",
    tags=["commanders"],
    responses={404: {"description": "Not found"}}
)
url = settings.API_MTG_URL+"/commanders/"


@router.get("/", response_model=List[Commander])
async def  all_commanders(
        commander:SelectAllCommander=Depends()
    ):
    try:
        options = None
        if commander.pag is not None:
            options = f"?pag={commander.pag}"
        if commander.limit is not None:
            if options is None:
                options = f"?limit={commander.limit}"
            else:
                options += f"&limit={commander.limit}"
        if commander.commander is not None:
            if options is None:
                options = f"?commander={commander.commander}"
            else:
                options += f"&commander={commander.commander}"
        if options is None:
            response = requests.get(f'{url}', json=commander.model_dump())
        else:
            response = requests.get(f'{url}{options}', json=commander.model_dump())
        if response.status_code == 200:
            commander_data = response.json()
            return [Commander(**c) for c in commander_data]
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")
    
@router.get("/{id}", response_model=Commander)
async def  get_commanders(
        id:int
    ):
    try:
        response = requests.get(f'{url}{id}')
        if response.status_code == 200:
            commander_data = response.json()
            return Commander(**commander_data)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")
    
@router.post("/", response_model=Commander)
async def  create_new_commander(
        commander: CreateCommander
    ):
    try:
        response = requests.post(f'{url}', json=commander.model_dump())
        if response.status_code == 200:
            commander_data = response.json()
            return Commander(**commander_data)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")

@router.put("/{id}", response_model=Commander)
async def update_commander(
        id: int,
        commander: UpdateCommander
    ):
    try:
        print(commander.model_dump())
        response = requests.put(f'{url}{id}', json=commander.model_dump())
        if response.status_code == 200:
            commander_data = response.json()
            return Commander(**commander_data)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except HTTPException:
        raise
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=f"{str(e)}")
@router.delete("/{id}", response_model=dict)
async def  delete_commander(
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