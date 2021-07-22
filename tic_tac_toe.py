# 0.0 Import Modules ----

from tkinter import *
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


def inner_win_check(digits, digit, count, mark, panels, button):
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
        inner_win_check(digits=digits,
                        digit=digit,
                        count=count,
                        mark=mark,
                        panels=panels,
                        button=button1)

    if digit == 2 and digit in digits:
        inner_win_check(digits=digits,
                        digit=digit,
                        count=count,
                        mark=mark,
                        panels=panels,
                        button=button2)


# Buttons to execute commands ----
button1 = Button(root, width=15, font=('Times 16 bold'),
                 height=7, command=lambda: win_checker(1))
button1.grid(row=1, column=1)
button2 = Button(root, width=15, height=7, font=(
    'Times 16 bold'), command=lambda: win_checker(2))
button2.grid(row=1, column=2)

# .0 Execution
root.mainloop()
