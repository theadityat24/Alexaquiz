from fastapi import FastAPI
from requests import request
app = FastAPI()

@app.get('/')
def get_all():
    return request(
        'GET',
        'https://s3-us-west-2.amazonaws.com/pinafore-us-west-2/qanta-jmlr-datasets/qanta.test.2018.04.18.json'
    ).json()