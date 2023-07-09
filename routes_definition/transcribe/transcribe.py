import whisper

def transcribe_helper(model: whisper.Whisper, inputAudio):
    return model.transcribe(inputAudio)["text"]