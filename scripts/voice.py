from tts.synthesis import TTS, Voices, Stress
import winsound

tts = TTS()


def speak(text):
    with open("test.wav", mode="wb") as file:
        _, text = tts.tts(text, Voices.Mykyta.value, Stress.Model.value, file)
    winsound.PlaySound('test.wav', winsound.SND_ALIAS)


speak('Тестове р+еченн+я ')


