import whisper
from pathlib import Path


model_tiny = whisper.load_model("tiny")
model_base_en = whisper.load_model("base.en")
model_small = whisper.load_model("small")
 
ROOT_DIR = Path(__file__).resolve(strict=True).parent
