import uuid
import json

from starlette.responses import JSONResponse
from routes_definition.transcribe.transcribe import transcribe_helper

from base import model_small, model_base_en, model_tiny
from utils.utils import adownload_audio_file
from base import ROOT_DIR


async def ping(request):
    return JSONResponse({"status": 200, "message": "success", "data": {}})


async def health_check(request):
    return JSONResponse({"status": 200, "message": "success", "data": {}})


async def transcribe(request):
    form = await request.form()

    audio = form.get("audio")
    model_name = form.get("model", "tiny")
    language = form.get("language", "en")

    if audio is None:
        return JSONResponse(
            status_code=400,
            content={"status": 400, "message": "Bad Request", "data": {}},
        )

    file_path = f"{str(ROOT_DIR)}/audios/{str(uuid.uuid4())}.mp3"
    with open(file_path, "wb") as f:
        f.write(audio.file.read())

    model = model_tiny
    if model_name == "base.en":
        model = model_base_en
    elif model_name == "small":
        model = model_small

    res = transcribe_helper(model, audio_path=file_path, language=language)

    return JSONResponse(
        {"status": 200, "message": "success", "data": {"transcription": res}}
    )
