from pydantic import BaseModel, ConfigDict, Field

from schemas.category import CategoryResponse


class ProductCreate(BaseModel):
    sku: str = Field(..., min_length=5, max_length=20)
    name: str = Field(..., min_length=3, max_length=200)
    price: float = Field(..., gt=0)
    stock_quantity: int = Field(..., ge=0)
    category_id: int = Field(..., gt=0)


class ProductResponse(BaseModel):
    id: int
    sku: str
    name: str
    price: float
    stock_quantity: int
    category: CategoryResponse

    model_config = ConfigDict(from_attributes=True)
