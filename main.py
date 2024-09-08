from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "멋쟁이 사자처럼 파이썬 백엔드 스쿨에서 함께해요!!"}

# 계산기 기능 구현
# 숫자의 덧셈, 뺄셈, 곱셈, 나눗셈을 할 수 있는 기능을 구현해보자

@app.get("/add")
def add(x: int, y: int):
    return {"result": x + y}

@app.get("/sub")
def sub(x: int, y: int):
    return {"result": x - y}

@app.get("/mul")
def mul(x: int, y: int):
    return {"result": x * y}

@app.get("/div")
def div(x: int, y: int):
    return {"result": x / y}
~