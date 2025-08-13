from gtts import gTTS
from pydub import AudioSegment
import os

# Read text
with open("Sample.txt", "r", encoding="utf-8") as f:
    x = f.read()

language = 'en'
audio = gTTS(text=x, lang=language, slow=False)

# Save as MP3
audio.save("temp.mp3")

# Convert to WAV
sound = AudioSegment.from_mp3("temp.mp3")
sound.export("audio.wav", format="wav")

# Play WAV (Windows)
os.system("start audio.wav")
