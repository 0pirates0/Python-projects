from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("T3")
root.geometry("395x200")


def for_player():
    root.title("T3 - PvP")
    root.geometry("395x460")
    but_player.destroy()
    but_ai.destroy()
    global button, button8, button7, button6, button4, button5, button2, button3, button1

    button = Button(root, text="", font=("Times New Roman", "15"), command=lambda: god(1))
    button.grid(row=0, column=0, ipadx=50, ipady=50)

    button1 = Button(root, text="", font=("Times New Roman", "15"), command=lambda: god(2))
    button1.grid(row=0, column=1, ipadx=50, ipady=50)

    button2 = Button(root, text="", font=("Times New Roman", "15"), command=lambda: god(3))
    button2.grid(row=0, column=2, ipadx=50, ipady=50)

    button3 = Button(root, text="", font=("Times New Roman", "15"), command=lambda: god(4))
    button3.grid(row=1, column=0, ipadx=50, ipady=50)

    button4 = Button(root, text="", font=("Times New Roman", "15"), command=lambda: god(5))
    button4.grid(row=1, column=1, ipadx=50, ipady=50)

    button5 = Button(root, text="", font=("Times New Roman", "15"), command=lambda: god(6))
    button5.grid(row=1, column=2, ipadx=50, ipady=50)

    button6 = Button(root, text="", font=("Times New Roman", "15"), command=lambda: god(7))
    button6.grid(row=2, column=0, ipadx=50, ipady=50)

    button7 = Button(root, text="", font=("Times New Roman", "15"), command=lambda: god(8))
    button7.grid(row=2, column=1, ipadx=50, ipady=50)

    button8 = Button(root, text="", font=("Times New Roman", "15"), command=lambda: god(9))
    button8.grid(row=2, column=2, ipadx=50, ipady=50)

    def reSe():
        button1.config(text=" ")
        button2.config(text=" ")
        button3.config(text=" ")
        button4.config(text=" ")
        button5.config(text=" ")
        button6.config(text=" ")
        button7.config(text=" ")
        button8.config(text=" ")

    reset1 = Button(root, text="Reset", command=reSe)
    reset1.grid(row=3, column=0, ipadx=50, ipady=50)
    reset1.config(height=1, width=1)

    def clos():
        quit()

    end1 = Button(root, text="I quit!!", command=clos)
    end1.grid(row=3, column=1, ipadx=50, ipady=50)
    end1.config(height=1, width=1)


def winner():
    if (button["text"] == "O" and button1["text"] == "O" and button2["text"] == "O" or
            button3["text"] == "O" and button4["text"] == "O" and button5["text"] == "O" or
            button6["text"] == "O" and button7["text"] == "O" and button8["text"] == "O" or
            button["text"] == "O" and button3["text"] == "O" and button6["text"] == "O" or
            button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
            button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
            button["text"] == "O" and button4["text"] == "O" and button8["text"] == "O" or
            button2["text"] == "O" and button4["text"] == "O" and button6["text"] == "O"):
        messagebox._show("Congrats", "Player2 Wins(O) \nHe is your animator friend, isn't he. I knew he is smarter than you")
    elif (button["text"] == "X" and button1["text"] == "X" and button2["text"] == "X" or
          button3["text"] == "X" and button4["text"] == "X" and button5["text"] == "X" or
          button6["text"] == "X" and button7["text"] == "X" and button8["text"] == "X" or
          button["text"] == "X" and button3["text"] == "X" and button6["text"] == "X" or
          button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
          button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
          button["text"] == "X" and button4["text"] == "X" and button8["text"] == "X" or
          button2["text"] == "X" and button4["text"] == "X" and button6["text"] == "X"):
        messagebox._show("Congrats", "Player1 wins(X) \nYou were playing alone, weren't you? Haha lonely chaiwala")


Player = 1


def god(buttomNo):
    global Player

    if buttomNo == 1 and Player == 1:
        button.config(text="X")
        Player = 2

    elif buttomNo == 1 and Player == 2:
        button.config(text="O")
        Player = 1

    elif buttomNo == 2 and Player == 1:
        button1.config(text="X")
        Player = 2

    elif buttomNo == 2 and Player == 2:
        button1.config(text="O")
        Player = 1

    elif buttomNo == 3 and Player == 1:
        button2.config(text="X")
        Player = 2

    elif buttomNo == 3 and Player == 2:
        button2.config(text="O")
        Player = 1

    elif buttomNo == 4 and Player == 1:
        button3.config(text="X")
        Player = 2

    elif buttomNo == 4 and Player == 2:
        button3.config(text="O")
        Player = 1

    elif buttomNo == 5 and Player == 1:
        button4.config(text="X")
        Player = 2

    elif buttomNo == 5 and Player == 2:
        button4.config(text="O")
        Player = 1

    elif buttomNo == 6 and Player == 1:
        button5.config(text="X")
        Player = 2

    elif buttomNo == 6 and Player == 2:
        button5.config(text="O")
        Player = 1

    elif buttomNo == 7 and Player == 1:
        button6.config(text="X")
        Player = 2

    elif buttomNo == 7 and Player == 2:
        button6.config(text="O")
        Player = 1

    elif buttomNo == 8 and Player == 1:
        button7.config(text="X")
        Player = 2

    elif buttomNo == 8 and Player == 2:
        button7.config(text="O")
        Player = 1

    elif buttomNo == 9 and Player == 1:
        button8.config(text="X")
        Player = 2

    elif buttomNo == 9 and Player == 2:
        button8.config(text="O")
        Player = 1

    winner()


def for_ai():
    root.title("T3 - P v AI")
    root.geometry("370x550")
    but_player.destroy()
    but_ai.destroy()
    messagebox._show("Aww shit! This guy again", "\nLook where your loneliness took you, back to me")
    global button, button8, button7, button6, button4, button5, button2, button3, button1

    button = Button(root, text="", font=("Times New Roman", "15"), command=lambda: change(1))
    button.grid(row=0, column=0, ipadx=50, ipady=50)

    button1 = Button(root, text="", font=("Times New Roman", "15"), command=lambda: change(2))
    button1.grid(row=0, column=1, ipadx=50, ipady=50)

    button2 = Button(root, text="", font=("Times New Roman", "15"), command=lambda: change(3))
    button2.grid(row=0, column=2, ipadx=50, ipady=50)

    button3 = Button(root, text="", font=("Times New Roman", "15"), command=lambda: change(4))
    button3.grid(row=1, column=0, ipadx=50, ipady=50)

    button4 = Button(root, text="", font=("Times New Roman", "15"), command=lambda: change(5))
    button4.grid(row=1, column=1, ipadx=50, ipady=50)

    button5 = Button(root, text="", font=("Times New Roman", "15"), command=lambda: change(6))
    button5.grid(row=1, column=2, ipadx=50, ipady=50)

    button6 = Button(root, text="", font=("Times New Roman", "15"), command=lambda: change(7))
    button6.grid(row=2, column=0, ipadx=50, ipady=50)

    button7 = Button(root, text="", font=("Times New Roman", "15"), command=lambda: change(8))
    button7.grid(row=2, column=1, ipadx=50, ipady=50)

    button8 = Button(root, text="", font=("Times New Roman", "15"), command=lambda: change(9))
    button8.grid(row=2, column=2, ipadx=50, ipady=50)
    button.config(text="X")

    def change(bno):
        if bno == 1:
            button.config(text="O")
        elif bno == 2:
            button1.config(text="O")
        elif bno == 3:
            button2.config(text="O")
        elif bno == 4:
            button3.config(text="O")
        elif bno == 5:
            button4.config(text="O")
        elif bno == 6:
            button5.config(text="O")
        elif bno == 7:
            button6.config(text="O")
        elif bno == 8:
            button7.config(text="O")
        elif bno == 9:
            button8.config(text="O")

        if button4["text"] == "O" and button8["text"] != "O":
            button8.config(text="X")
            if button2["text"] == "O":
                button6.config(text="X")
                if button1["text"] == "O" or button3["text"] == "O" or button5["text"] == "O":
                    button7.config(text="X")
                elif button1["text"] == "O" or button7["text"] == "O" or button5["text"] == "O":
                    button3.config(text="X")
            elif button6["text"] == "O":
                button2.config(text="X")
                if button1["text"] == "O" or button3["text"] == "O" or button7["text"] == "O":
                    button5.config(text="X")
                elif button3["text"] == "O" or button5["text"] == "O" or button7["text"] == "O":
                    button1.config(text="X")
            elif button1["text"] == "O" or button3["text"] == "O" or button5["text"] == "O" or button7["text"] == "O":
                messagebox._show("Alright Alright", "You ain't that dumb I guess")
                reSet()
        if button2["text"] == "O":
            button8.config(text="X")
            if button4["text"] == "O":
                button6.config(text="X")
                if button1["text"] == "O" or button3["text"] == "O" or button5["text"] == "O":
                    button7.config(text="X")
                elif button1["text"] == "O" or button7["text"] == "O" or button5["text"] == "O":
                    button3.config(text="X")
            elif button1["text"] == "O" or button3["text"] == "O" or button5["text"] == "O" or button6["text"] == "O" or button7["text"] == "O":
                button4.config(text="X")
        if button5["text"] == "O" and button8["text"] != "X":
            button4.config(text="X")
            if button8["text"] == "O":
                button2.config(text="X")
                if button1["text"] == "O" or button3["text"] == "O" or button7["text"] == "O":
                    button6.config(text="X")
                elif button6["text"] == "O" or button3["text"] == "O" or button7["text"] == "O":
                    button1.config(text="X")
            elif button1["text"] == "O" or button2["text"] == "O" or button3["text"] == "O" or button6["text"] == "O" or button7["text"] == "O":
                button8.config(text="X")
        if button6["text"] == "O":
            button8.config(text="X")
            if button4["text"] == "O":
                button2.config(text="X")
                if button1["text"] == "O" or button3["text"] == "O" or button7["text"] == "O":
                    button5.config(text="X")
                elif button1["text"] == "O" or button5["text"] == "O" or button7["text"] == "O":
                    button1.config(text="X")
            elif button1["text"] == "O" or button2["text"] == "O" or button3["text"] == "O" or button5["text"] == "O" or button7["text"] == "O":
                button4.config(text="X")
        if button7["text"] == "O":
            button4.config(text="X")
            if button8["text"] == "O":
                button6.config(text="X")
                if button1["text"] == "O" or button3["text"] == "O" or button5["text"] == "O":
                    button2.config(text="X")
                elif button1["text"] == "O" or button2["text"] == "O" or button5["text"] == "O":
                    button3.config(text="X")
            elif button1["text"] == "O" or button2["text"] == "O" or button3["text"] == "O" or button5["text"] == "O" or button6["text"] == "O":
                button8.config(text="X")
        if button8["text"] == "O" and button4["text"] != "X":
            button6.config(text="X")
            if button3["text"] == "O":
                button2.config(text="X")
                if button5["text"] == "O" or button1["text"] == "O" or button7["text"] == "O":
                    button4.config(text="X")
                elif button4["text"] == "O" or button5["text"] == "O" or button7["text"] == "O":
                    button1.config(text="X")
            elif (button1["text"] == "O" or button4["text"] == "O" or button5["text"] == "O" or button2["text"] == "O" or button7["text"] == "O") and button4['text'] != "X":
                button3.config(text="X")
        if button3["text"] == "O":
            button2.config(text="X")
            if button1["text"] == "O":
                button4.config(text="X")
                if button5["text"] == "O" or button6["text"] == "O" or button7["text"] == "O":
                    button8.config(text="X")
                elif button5["text"] == "O" or button8["text"] == "O" or button7["text"] == "O":
                    button6.config(text="X")
            elif (button4["text"] == "O" or button5["text"] == "O" or button6["text"] == "O" or button7["text"] == "O" or button8["text"] == "O") and button6["text"] != "X":
                button1.config(text="X")
        if button1["text"] == "O":
            button4.config(text="X")
            if button8["text"] == "O":
                button6.config(text="X")
                if button3["text"] == "O" or button5["text"] == "O" or button7["text"] == "O":
                    button2.config(text="X")
                    messagebox._show("Im kinda scared!", "Is your dumbness contagious? Cuz I almost got it.")
                elif button2["text"] == "O" or button5["text"] == "O" or button7["text"] == "O":
                    button3.config(text="X")
            elif (button2["text"] == "O" or button3["text"] == "O" or button5["text"] == "O" or button6["text"] == "O" or button7["text"] == "O") and button4["text"] != "X":
                button8.config(text="X")

        if (button["text"] == "O" and button1["text"] == "O" and button2["text"] == "O" or
                button3["text"] == "O" and button4["text"] == "O" and button5["text"] == "O" or
                button6["text"] == "O" and button7["text"] == "O" and button8["text"] == "O" or
                button["text"] == "O" and button3["text"] == "O" and button6["text"] == "O" or
                button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
                button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
                button["text"] == "O" and button4["text"] == "O" and button8["text"] == "O" or
                button2["text"] == "O" and button4["text"] == "O" and button6["text"] == "O"):
            messagebox._show("Holy Shit", "What in the...Oh well that is your fault\nYou didn't code me well")
        elif (button["text"] == "X" and button1["text"] == "X" and button2["text"] == "X" or
              button3["text"] == "X" and button4["text"] == "X" and button5["text"] == "X" or
              button6["text"] == "X" and button7["text"] == "X" and button8["text"] == "X" or
              button["text"] == "X" and button3["text"] == "X" and button6["text"] == "X" or
              button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
              button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
              button["text"] == "X" and button4["text"] == "X" and button8["text"] == "X" or
              button2["text"] == "X" and button4["text"] == "X" and button6["text"] == "X"):
            messagebox._show("AI wins!", "Haha Dummy!")

    def reSet():
        button1.config(text=" ")
        button2.config(text=" ")
        button3.config(text=" ")
        button4.config(text=" ")
        button5.config(text=" ")
        button6.config(text=" ")
        button7.config(text=" ")
        button8.config(text=" ")

    reset = Button(root, text="Reset", command=reSet)
    reset.grid(row=3, column=0, ipadx=50, ipady=50)
    reset.config(height=1, width=1)

    def close():
        quit()

    end = Button(root, text="I quit!!", command=close)
    end.grid(row=3, column=1, ipadx=50, ipady=50)
    end.config(height=1, width=1)


but_ai = Button(root, text="You vs AI \n (Not recommended)", command=for_ai)
but_ai.pack(pady=20)

but_player = Button(root, text="You vs Player \n(Also not recommended)", command=for_player)
but_player.pack(pady=20)

root.mainloop()
