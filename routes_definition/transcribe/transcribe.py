import os
import whisper


def transcribe_helper(model: whisper.Whisper, audio_path: str, language: str):
    result = model.transcribe(audio_path, language=language)
    os.remove(audio_path)

    print(result)
    return result["text"]
