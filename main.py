import speech_recognition
import commands
from pydub import AudioSegment
from pydub.playback import play
import random
import time



sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5


keyword = ['хей джарвис', 'джарвис']

def listen():
    timeout = 15
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(mic, 0.5)
        try:
            audio = sr.listen(mic, timeout=timeout)
            query = sr.recognize_google(audio_data=audio, language="ru-RU").lower()
        except speech_recognition.exceptions.UnknownValueError:
            return ""
        print(query)
        return query

def wating_for_activate():
    while True:
        print("Ожидание активации ассистента...")
        command = listen()
        for i in keyword:
            if command == i:
                greet = ['sound\greet\greet1.wav', 'sound\greet\greet2.wav', 'sound\greet\greet3.wav']
                play(AudioSegment.from_wav(greet[random.randint(0, len(greet)) - 1]))
                print("Ассистент активирован.")
                return

def do_command():
    while True:
        command = listen()
        if command == 'сон':
            return
        for i, k in commands.items():
            if command == i:
                ok = ['sound\ok\ok1.wav', 'sound\ok\ok2.wav', 'sound\ok\ok3.wav', 'sound\ok\ok4.wav']
                time.sleep(0.1)
                k()
                play(AudioSegment.from_wav(ok[random.randint(0, len(ok) - 1)]))
                return

commands = {
    "джарвис": wating_for_activate,
    "открой chrome": commands.chrome,
    "открой youtube": commands.youtube,
    "включи музыку": commands.music,
    "перезагрузись": commands.restart_program,
}

def main():
    play(AudioSegment.from_wav('sound\\run.wav'))
    while True:
        wating_for_activate()
        time.sleep(0.5)
         # Ожидаем следующую команду после активации ассистента
        print("Ожидание следующей команды...")
        do_command()

if __name__ == "__main__":
    main()