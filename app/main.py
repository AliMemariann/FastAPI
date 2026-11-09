from fastapi import FastAPI
from app.database import engine, Base
from app import models
from app.routers import customer_route
from app.routers import factor_route
from app.routers import factor_item_route
from app.routers import product_route

Base.metadata.create_all(bind= engine)

app = FastAPI(
    title= 'Shop Management API',
    description= 'A Simple API for managing Customers, Factors and Products',
    version= '1.0.0'
)

app.include_router(customer_route.router)
app.include_router(factor_route.router)
app.include_router(factor_item_route.router)
app.include_router(product_route.router)


@app.get('/')
def root():
    return {'Message': 'Welcome to the Shop Management API'}