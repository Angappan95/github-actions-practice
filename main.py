import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return {'msg': 'Hello User'}

def main():
    print("Hello from github-actions-practice!")


if __name__ == "__main__":
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
