from typing import List
from fastapi import APIRouter, HTTPException, Request
import requests
from Models.commander import *
from Routers import settings

router = APIRouter(
    prefix="/commanders",
    tags=["commanders"],
    responses={404: {"description": "Not found"}}
)
url = settings.API_MTG_URL+"/commanders/"

@router.get("/", response_model=List[Commander])
async def all_commanders(request: Request):
    try:
        query_string = str(request.url.query)
        target_url = f"{url}?{query_string}" if query_string else url
        
        response = requests.get(target_url)
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
async def  get_commanders(id: int):
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
async def  create_new_commander(commander: CreateCommander):
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
async def update_commander(id: int,commander: UpdateCommander):
    try:
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
async def  delete_commander(id: int):
    try:
        response = requests.delete(f'{url}{id}')
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", response.text))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{str(e)}")