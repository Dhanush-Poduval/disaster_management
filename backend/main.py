from fastapi import FastAPI

app=FastAPI()

@app.post('/test')
def test():
    return{'status':'success'}
