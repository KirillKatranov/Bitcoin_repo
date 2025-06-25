from fast import app


@app.get("/asd")
async def root():
    return {"message": "Hello World"}