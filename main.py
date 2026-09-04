from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, List


app = FastAPI(
    title = " API de prueba",
    description = "Esta es una API de prueba para el curso de FastAPI"
)


class ItemBase(BaseModel):
    name: str = Field(..., min_length = 3, description = "Nombre del item")
    price: float = Field(..., gt = 0, description = "Precio del item")
    description: Optional[str] = Field(None, description = "Descripción del item")

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int = Field(..., description = "ID del item")


items_db = []

@app.post("/items/", response_model=ItemResponse)
async def create_item(item: ItemCreate):
    new_item = {**item.dict(), "id":len(items_db) + 1}
    items_db.append(new_item)
    return new_item

@app.get("/items/", response_model=List[ItemResponse])
async def get_items():
    return items_db