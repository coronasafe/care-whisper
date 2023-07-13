from starlette.responses import JSONResponse
from routes_definition.transcribe.transcribe import transcribe_helper

from base import model_small, model_base_en, model_tiny
from utils.utils import adownload_audio_file

async def ping(request):
    return JSONResponse({"status": 200, "message": "success", "data": {}})

async def health_check(request):
    return JSONResponse({"status": 200, "message": "success", "data": {}})

async def transcribe(request):
    data = await request.json()

    if "inputAudio" not in data:
          return JSONResponse(status_code=400, content={"status": 400, "message": "Bad Request", "data": {}})
    
    # tiny, base.en, small
    model_name = data.get("model", "tiny")
    
    audio_url = data["inputAudio"]
    file_path = await adownload_audio_file(audio_url)

    model = model_tiny
    if model_name == "base.en":
        model = model_base_en
    elif model_name == "small":
        model = model_small
    
    res = transcribe_helper(model, audio_path=file_path)

    return JSONResponse({"status": 200, "message": "success", "data": {"transcription": res}})

