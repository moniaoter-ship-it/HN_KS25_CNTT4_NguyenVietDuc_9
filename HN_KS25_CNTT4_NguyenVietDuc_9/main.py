from fastapi import FastAPI

from database import Base, engine
from routers.categories import router as categories_router
from routers.product import router as product_router

# Tạo bảng nếu chưa tồn tại.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Livestream Management API",
    version="1.0.0",
)

app.include_router(categories_router)
app.include_router(product_router)


@app.get("/")
def root():
    return {
        "statusCode": 200,
        "error": None,
        "message": "Livestream API đang hoạt động",
        "data": None,
    }
