from typing import Optional
from pydantic import BaseModel, validator

class Receita(BaseModel):
    id: Optional[int] = None
    categoria: str
    dicas: str
    

    @validator('dicas')
    def  validate_dicas(cls, value: str):
        receitas = value.split(' ')
        if  len(receitas) < 2 or len(receitas) > 5:
            print('Deve conter no minimo 2 receitas')
            raise ValueError('Deve conter pelo menos 2 receitas')
        
        if value.islower():
            print('As receitas devem ser capitalizadas')
            raise ValueError('As receitas devem ser capitalizadas')
        return value
    
receitas = [
    Receita(id=1, categoria='vegana', dicas = 'Priscila Mendes'),
    Receita(id=2, categoria='carne', dicas = 'Priscila Mendes'),
    

    ]