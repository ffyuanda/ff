import uvicorn

if __name__ == '__main__':
    uvicorn.run("server2:app", host='127.0.0.1', port=8000)