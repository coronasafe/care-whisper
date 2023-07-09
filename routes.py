from starlette.responses import JSONResponse

from base import model

async def ping(request):
    return JSONResponse({"status": 200, "message": "success", "data": {}})

async def health_check(request):
    return JSONResponse({"status": 200, "message": "success", "data": {}})

async def transcribe(request):
    data = await request.json()

    if "inputAudio" not in data:
          return JSONResponse(status_code=400, content={"status": 400, "message": "Bad Request", "data": {}})
    
    inputAudio = data["inputAudio"]