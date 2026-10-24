from fastapi import FastAPI
import uvicorn

app = FastAPI(title='ping')

@app.get('/ping')
def ping():
  return 'PONG'

# Proper way of running it:
# uvicorn ping:app --host 0.0.0.0 --port 9696 --reload

if __name__ == '__main__':
  uvicorn.run(app, host='0.0.0.0', port=9696)