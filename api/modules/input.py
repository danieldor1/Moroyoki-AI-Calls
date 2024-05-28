import io
import os
import tempfile
import queue
import logging
import speech_recognition as sr

from pydub import AudioSegment
from modules.config.settings import SpeechRecognitionSettings

CHUNK = SpeechRecognitionSettings.chunk_size.value
SAMPLE_RATE = SpeechRecognitionSettings.sample_rate.value
SAMPLE_WIDTH = SpeechRecognitionSettings.sample_width.value
ENERGY_THRESHOLD = SpeechRecognitionSettings.recognizer_energy_threshold.value
DYNAMIC_ENERGY_THRESHOLD = SpeechRecognitionSettings.recognizer_dynamic_energy_threshold.value
TMP_FILE = SpeechRecognitionSettings.tmp_name.value
AUDIO_FORMAT = SpeechRecognitionSettings.mic_capture_format.value


class _TwilioSource(sr.AudioSource):
    def __init__(self, stream):
        self.stream = stream
        self.CHUNK = CHUNK
        self.SAMPLE_RATE = SAMPLE_RATE
        self.SAMPLE_WIDTH = SAMPLE_WIDTH

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class _QueueStream:
    def __init__(self):
        self.q = queue.Queue(maxsize=-1)

    def read(self, chunk: int) -> bytes:
        return self.q.get()

    def write(self, chunk: bytes):
        self.q.put(chunk)


class TwillioStream2Text:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = ENERGY_THRESHOLD
        self.recognizer.pause_threshold = DYNAMIC_ENERGY_THRESHOLD
        self.recognizer.dynamic_energy_threshold = False
        self.stream = None

    def get_transcription(self) -> str:
        self.stream = _QueueStream()
        try:    
            with _TwilioSource(self.stream) as source:
                with tempfile.TemporaryDirectory() as tmp:
                    tmp_path = os.path.join(tmp, TMP_FILE)
                    audio = self.recognizer.listen(
                        source=source,
                        )
                    data = io.BytesIO(audio.get_wav_data())
                    audio_clip = AudioSegment.from_file(data)
                    audio_clip.export(tmp_path, format=AUDIO_FORMAT)
                    logging.info("Audio captured")                    
       
        except Exception:
            raise
