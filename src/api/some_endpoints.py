from fast import app
from queries.orm import insert_data
from schemas import CustomPriceSchemas


@app.get("/HW")
async def root():
    return {"message": "Hello World"}

@app.post("/create_row")
async def create_row(price: CustomPriceSchemas):
    insert_data(price.price)
    return price