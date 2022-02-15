from tkinter import *
from tkinter import ttk

# Propertites/Attributes
word = "Hangman"

lives = 5

promptWord = "?" * len(word)

usedLetters = []

letterButtons = []

def configureWidgets():

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, E, S, W))

    global livesLabel
    livesLabel = ttk.Label(mainframe, text="Lives: " + str(lives))
    livesLabel.grid(column=0, row=0, sticky=(N, E, S, W))

    global promptWordLabel
    promptWordLabel = ttk.Label(mainframe, text=promptWord, padding="3 3 12 12")
    promptWordLabel.grid(column=1, row=1, sticky=(N, E, S, W))

    # Frame to contain the buttons inside of
    buttonsFrame = ttk.Frame(mainframe, padding="3 3 12 12")
    buttonsFrame.grid(column=0, row=2, columnspan= 3, sticky=(N, E, S, W))

    # The buttons of the 26 letters in the alphabet
    # 1
    aButton = ttk.Button(buttonsFrame, text="A", command=lambda: letter_Tapped("A"))
    aButton.grid(column=0, row=0, sticky=(E, S, W))
    letterButtons.append(aButton)
    # 2
    bButton = ttk.Button(buttonsFrame, text="B", command=lambda: letter_Tapped("B"))
    bButton.grid(column=1, row=0, sticky=(E, S, W))
    letterButtons.append(bButton)
    # 3
    cButton = ttk.Button(buttonsFrame, text="C", command=lambda: letter_Tapped("C"))
    cButton.grid(column=2, row=0, sticky=(E, S, W))
    letterButtons.append(cButton)
    # 4
    dButton = ttk.Button(buttonsFrame, text="D", command=lambda: letter_Tapped("D"))
    dButton.grid(column=3, row=0, sticky=(E, S, W))
    letterButtons.append(dButton)
    # 5
    eButton = ttk.Button(buttonsFrame, text="E", command=lambda: letter_Tapped("E"))
    eButton.grid(column=4, row=0, sticky=(E, S, W))
    letterButtons.append(eButton)
    # 6
    fButton = ttk.Button(buttonsFrame, text="F", command=lambda: letter_Tapped("F"))
    fButton.grid(column=0, row=1, sticky=(E, S, W))
    letterButtons.append(fButton)
    # 7
    gButton = ttk.Button(buttonsFrame, text="G", command=lambda: letter_Tapped("G"))
    gButton.grid(column=1, row=1, sticky=(E, S, W))
    letterButtons.append(gButton)
    # 8
    hButton = ttk.Button(buttonsFrame, text="H", command=lambda: letter_Tapped("H"))
    hButton.grid(column=2, row=1, sticky=(E, S, W))
    letterButtons.append(hButton)
    # 9
    iButton = ttk.Button(buttonsFrame, text="I", command=lambda: letter_Tapped("I"))
    iButton.grid(column=3, row=1, sticky=(E, S, W))
    letterButtons.append(iButton)
    # 10
    jButton = ttk.Button(buttonsFrame, text="J", command=lambda: letter_Tapped("J"))
    jButton.grid(column=4, row=1, sticky=(E, S, W))
    letterButtons.append(jButton)
    # 11
    kButton = ttk.Button(buttonsFrame, text="K", command=lambda: letter_Tapped("K"))
    kButton.grid(column=0, row=2, sticky=(E, S, W))
    letterButtons.append(kButton)
    # 12
    lButton = ttk.Button(buttonsFrame, text="L", command=lambda: letter_Tapped("L"))
    lButton.grid(column=1, row=2, sticky=(E, S, W))
    letterButtons.append(lButton)
    # 13
    mButton = ttk.Button(buttonsFrame, text="M", command=lambda: letter_Tapped("M"))
    mButton.grid(column=2, row=2, sticky=(E, S, W))
    letterButtons.append(mButton)
    # 14
    nButton = ttk.Button(buttonsFrame, text="N", command=lambda: letter_Tapped("N"))
    nButton.grid(column=3, row=2, sticky=(E, S, W))
    letterButtons.append(nButton)
    # 15
    oButton = ttk.Button(buttonsFrame, text="O", command=lambda: letter_Tapped("O"))
    oButton.grid(column=4, row=2, sticky=(E, S, W))
    letterButtons.append(oButton)
    # 16
    pButton = ttk.Button(buttonsFrame, text="P", command=lambda: letter_Tapped("P"))
    pButton.grid(column=0, row=3, sticky=(E, S, W))
    letterButtons.append(pButton)
    # 17
    qButton = ttk.Button(buttonsFrame, text="Q", command=lambda: letter_Tapped("Q"))
    qButton.grid(column=1, row=3, sticky=(E, S, W))
    letterButtons.append(qButton)
    # 18
    rButton = ttk.Button(buttonsFrame, text="R", command=lambda: letter_Tapped("R"))
    rButton.grid(column=2, row=3, sticky=(E, S, W))
    letterButtons.append(rButton)
    # 19
    sButton = ttk.Button(buttonsFrame, text="S", command=lambda: letter_Tapped("S"))
    sButton.grid(column=3, row=3, sticky=(E, S, W))
    letterButtons.append(sButton)
    # 20
    tButton = ttk.Button(buttonsFrame, text="T", command=lambda: letter_Tapped("T"))
    tButton.grid(column=4, row=3, sticky=(E, S, W))
    letterButtons.append(tButton)
    # 21
    uButton = ttk.Button(buttonsFrame, text="U", command=lambda: letter_Tapped("U"))
    uButton.grid(column=0, row=4, sticky=(E, S, W))
    letterButtons.append(uButton)
    # 22
    vButton = ttk.Button(buttonsFrame, text="V", command=lambda: letter_Tapped("V"))
    vButton.grid(column=1, row=4, sticky=(E, S, W))
    letterButtons.append(vButton)
    # 23
    wButton = ttk.Button(buttonsFrame, text="W", command=lambda: letter_Tapped("W"))
    wButton.grid(column=2, row=4, sticky=(E, S, W))
    letterButtons.append(wButton)
    # 24
    xButton = ttk.Button(buttonsFrame, text="X", command=lambda: letter_Tapped("X"))
    xButton.grid(column=3, row=4, sticky=(E, S, W))
    letterButtons.append(xButton)
    # 25
    yButton = ttk.Button(buttonsFrame, text="Y", command=lambda: letter_Tapped("Y"))
    yButton.grid(column=4, row=4, sticky=(E, S, W))
    letterButtons.append(yButton)
    # 26
    zButton = ttk.Button(buttonsFrame, text="Z", command=lambda: letter_Tapped("Z"))
    zButton.grid(column=0, row=5, sticky=(E, S, W))
    letterButtons.append(zButton)

    # Ensures the widgets remain on the screen
    root.mainloop()
    
def letter_Tapped(letter):
    global promptWordLabel
    global lives
    
    usedLetters.append(str(letter))

    # Disable buttons as they are tapped
    for button in range(0, len(letterButtons)):
        if letterButtons[button].cget('text') == letter:
            letterButtons[button].config(state='disabled')

    updatePromptWord()

    # Check if they player has won
    if letter in word.upper():
        if promptWord == word:
            promptWordLabel.config(text="You Win!")
    else:
        # They player has guessed incorrectly therefore deduct a life
        lives -= 1
        livesLabel.config(text="Lives: {}".format(lives))
        # Check if the player is out of lives
        if lives < 1:
            promptWordLabel.config(text="Game Over!")
            for button in range(0, len(letterButtons)):
                letterButtons[button].config(state='disabled')

def updatePromptWord():
    global promptWord
    # Reset the promptWord back to a blank string so that it can be generated again
    promptWord = ""

    for letter in range(0, len(word)):
        if word[letter].upper() in usedLetters:
                promptWord += word[letter]
        else:
            promptWord += "?"
    
    promptWordLabel.config(text=promptWord)

if __name__ == "__main__":
    
    root = Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    configureWidgets()
    updatePromptWord()
