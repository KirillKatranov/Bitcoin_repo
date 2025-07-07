from pydantic import BaseModel


class CustomPriceSchemas(BaseModel):
    price: float