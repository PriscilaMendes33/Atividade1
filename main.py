from typing import Dict, List, Optional, Any

from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Header
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Depends
from time import sleep
from modelteste import Receita
from modelteste import receitas

def fake_db():
    try:
        print('Abrindo conexão com banco de dados...')
        sleep(1)
    finally:
        print('Fechando conexão com banco de dados...')
        sleep(1)
        
app = FastAPI(
    
    title = 'API de Receitas',
    version = '0.0.1',
    description = 'Uma API Fast'
    
)

@app.get('/receitas',
        description = 'Retorna todas as receitas ou uma lista vazia',
        summary = 'Retorna todas as viagens',
        response_model = List[Receita],
        response_description = 'Receitas encontradas')
async def get_receitas(db: Any = Depends(fake_db)):
    return receitas

@app.post('/receitas', status_code = status.HTTP_201_CREATED, response_model = Receita)
async def post_receita(receita: Receita):
    next_id: int = len(receitas) + 1
    receita.id = next_id
    receitas.append(receita)
    return receita

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=5001, reload=True)
    
    
        
        
        
        
        
        
        
        