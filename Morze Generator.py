# Translates the input text into Morze language
import pyaudio
import numpy as np


def encode_morze(text):
    morse_code = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        " ": "__",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----"
    }
    morze = ''

    for letter in text.upper():
        code = ''
        if letter not in morse_code.keys():
            continue
        elif letter != " ":
            code = ''
            for symbol in morse_code[letter]:
                if symbol == ".":
                    i = "^"
                if symbol == "-":
                    i = "^^^"
                code = code + i + "_"
        else:
            code = morse_code[letter]
        morze = morze + code + "__"
    length = len(morze) - 2
    Song = morze[:length]
    print(Song)

    p = pyaudio.PyAudio()

    volume = 0.5     # range [0.0, 1.0]
    volume2 = 0.0     # range [0.0, 1.0]
    fs = 44100       # sampling rate, Hz, must be integer
    duration = 0.3   # in seconds, may be float
    f = 600.0        # sine frequency, Hz, may be float

    # generate samples
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    for q in Song:
        if q == '^':
            stream.write(volume*samples)
        if q == '_':
            stream.write(volume2*samples)
    stream.stop_stream()
    stream.close()

    p.terminate()


newtext = input("Enter text to translate: ")

encode_morze(newtext)
