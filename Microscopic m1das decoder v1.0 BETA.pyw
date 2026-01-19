import tkinter as tk
from tkinter import messagebox

morseCodeDict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    '?': '..--..', '/': '-..-.', '.': '.-.-.-', ',': '--..--',
    ':': '---...', "'": '.----.', '-': '-....-', '=': '-...-',
    ' ': '/'
}

def decodeMorseCode(morseStr):
    morseWrds = morseStr.split('/')
    decMsg = []

    for mWord in morseWrds:
        mLetters = mWord.strip().split(' ')
        decWrd = ''
        for mLet in mLetters:
            if mLet:
                for k, val in morseCodeDict.items():
                    if val == mLet:
                        decWrd += k
                        break
                else:
                    decWrd += '?'  # If not found, use '?'
        if decWrd:
            decMsg.append(decWrd)
    return ' '.join(decMsg)

def decode():
    inpStr = entry.get()
    procStr = inpStr.replace(',', '-').replace("'", '/')
    decTxt = decodeMorseCode(procStr)
    messagebox.showinfo("Decoded Message", decTxt)

def mainFunc():
    root = tk.Tk()
    root.title("Microscopic M1das Decoder")

    label = tk.Label(root, text="Welcome to the Microscopic M1das decoder!\nCreated by @BigCDestroyer")
    label.pack(pady=10)

    global entry
    entry = tk.Entry(root, width=50)
    entry.pack(padx=10, pady=5)

    decode_btn = tk.Button(root, text="Decode Morse", command=decode)
    decode_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    mainFunc()
