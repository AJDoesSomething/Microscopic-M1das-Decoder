#Microscopic M1das decoder v1.1
#Made by AJ




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
                    decWrd += 'Invalid input. Please copy and paste a tweet from @SmallestM1das you wish to decode and try again.'  #Error message if input is invalid
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
    root.title("Microscopic M1das Decoder V1.1")

    label = tk.Label(root, text="Welcome to the Microscopic M1das decoder!\nCreated by @BigCDestroyer\n Please enter the tweet to be decoded below:")
    label.pack(pady=10)

    global entry
    entry = tk.Entry(root, width=50)
    entry.pack(padx=10, pady=5)

    decode_btn = tk.Button(root, text="Decode Message", command=decode)
    decode_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    mainFunc()
#this code is 67 lines long- wait what 67?!?!? :o
