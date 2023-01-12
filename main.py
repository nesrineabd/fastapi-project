from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': {
        'name': 'Nesrine'
    }}


@app.get('/about') #decorator 
def about():
    return {'data': 'about page'}