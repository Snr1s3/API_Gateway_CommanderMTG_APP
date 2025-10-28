from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from Routers import commander, partida, usuari_commander, usuaris

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)
app.include_router(commander.router)
app.include_router(partida.router)
app.include_router(usuari_commander.router)
app.include_router(usuaris.router)

@app.get("/", tags=["root"])
async def root():
    return {"message": "Commander MTG API Gateway"}

@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "healthy"}
