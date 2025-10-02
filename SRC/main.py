from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from SRC.Routers import commander, partida

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

@app.get("/", tags=["root"])
async def root():
    return {"message": "Commander MTG API"}

@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "healthy"}


@app.get("/", response_model=str)
def root():
    return "API Gateway"