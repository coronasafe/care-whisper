import whisper

def transcribe_helper(model: whisper.Whisper, audio_path: str):

    result = model.transcribe(audio_path, language="hi")

    print(result)
    return result["text"]