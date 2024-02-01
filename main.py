from fastapi import FastAPI
# import httpx

app = FastAPI()

@app.get('/message')
def message(): 
    return {'message': 'sent'}

