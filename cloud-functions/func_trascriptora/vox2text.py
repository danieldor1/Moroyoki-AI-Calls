import io
import azure.cognitiveservices.speech as speech2text

from pydub import AudioSegment
from speech_recognition import Recognizer, AudioData

speech_config = speech2text.SpeechConfig(
    subscription=AZURE_SPEECH2TEXT_API_KEY, 
    region=AZURE_SPEECH2TEXT_REGION
)
speech_config.speech_recognition_language= RECOGNITION_LANGUAGE


def transcribe_audio(audio_data: bytes) -> str:
    
    audio_clip = AudioSegment.from_file(audio_data)
    
    try:
        audio_config = speech2text.audio.AudioConfig(filename=tmp_path)
        speech_recognizer = speech2text.SpeechRecognizer(
            speech_config=speech_config, 
            audio_config=audio_config
        )
        result = speech_recognizer.recognize_once_async().get()
        result_of_transcription_in_text = result.text           
        return str(result_of_transcription_in_text.strip())  
    
    except Exception:
        []
