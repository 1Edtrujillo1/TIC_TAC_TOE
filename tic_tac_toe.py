# 0.0 Import Modules ----

from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg

# 1.0 Dialog Box Generator ----

root = Tk()
root.title('ED TIC-TAC-TOE')

list(map(
    lambda text, column:
    Label(root,
          text=text,
          font="times 15").grid(row=0, column=column),
    ["player 1: X", "player 2: O"],
    [1, 2]
))

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# #list(range(1, 10))
mark = ''
count = 0
panels = ["panel"]*10


def win_combinations(panels, sign):
    return(
        (panels[1] == panels[2] == panels[3] == sign) or
        (panels[1] == panels[4] == panels[7] == sign) or
        (panels[1] == panels[5] == panels[9] == sign) or
        (panels[2] == panels[5] == panels[7] == sign) or
        (panels[3] == panels[6] == panels[9] == sign) or
        (panels[3] == panels[5] == panels[7] == sign) or
        (panels[4] == panels[5] == panels[6] == sign) or
        (panels[7] == panels[8] == panels[9] == sign)
    )


def inner_win_checker(digit, panels, button):

    global digits, mark, count

    digits.remove(digit)

    if count % 2 == 0:
        mark = 'X'
        panels[digit] = mark
    elif count % 2 != 0:
        mark = 'O'
        panels[digit] = mark

    button.config(text=mark)
    count = count + 1
    sign = mark

    if(win_combinations(panels, sign) and sign == 'X'):
        msg.showinfo("Result", "Player 1 wins")
        root.destroy()
    elif(win_combinations(panels, sign) and sign == 'O'):
        msg.showinfo("Result", "Player 2 wins")
        root.destroy()


def win_checker(digit):
    global digits, mark, count

    if digit == 1 and digit in digits:
        inner_win_checker(digit=digit,
                          panels=panels,
                          button=button1)

    if digit == 2 and digit in digits:
        inner_win_checker(digit=digit,
                          panels=panels,
                          button=button2)
    if digit == 3 and digit in digits:
        inner_win_checker(digit=digit,
                          panels=panels,
                          button=button2)
    if digit == 4 and digit in digits:
        inner_win_checker(digit=digit,
                          panels=panels,
                          button=button2)
    if digit == 5 and digit in digits:
        inner_win_checker(digit=digit,
                          panels=panels,
                          button=button2)
    if digit == 6 and digit in digits:
        inner_win_checker(digit=digit,
                          panels=panels,
                          button=button2)
    if digit == 7 and digit in digits:
        inner_win_checker(digit=digit,
                          panels=panels,
                          button=button2)
    if digit == 8 and digit in digits:
        inner_win_checker(digit=digit,
                          panels=panels,
                          button=button2)
    if digit == 9 and digit in digits:
        inner_win_checker(digit=digit,
                          panels=panels,
                          button=button2)
    if(count > 8 and
       win_combinations(panels=panels, sign='X') == FALSE and
       win_combinations(panels=panels, sign='O') == TRUE):
        msg.showinfo("Result", "Match Tied")
        root.destroy()

# Buttons to execute commands ----


def button_creation(button_name, digit, row, column):
    listOfGlobals = globals()
    listOfGlobals[button_name] = Button(root,
                                        width=15,
                                        font=('Times 16 bold'),
                                        height=7,
                                        command=lambda: win_checker(digit=digit))
    listOfGlobals[button_name].grid(row=row, column=column)


list(map(button_creation,
         ["button1", "button2", "button3",
          "button4", "button5", "button6",
          "button7", "button8", "button9"],
         [1, 2, 3,
          4, 5, 6,
          7, 8, 9],
         [1, 1, 1,
          2, 2, 2,
          3, 3, 3],
         [1, 2, 3,
          1, 2, 3,
          1, 2, 3]))
# button_creation(button_name="button1",
#                 digit=1,
#                 row=1,
#                 column=1)
# button_creation(button_name="button2",
#                 digit=2,
#                 row=1,
#                 column=2)

# .0 Execution
root.mainloop()
