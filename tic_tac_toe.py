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
    range(2)
))

digits = range(9)
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

    elif digit == 2 and digit in digits:
        inner_win_check(digits=digits,
                        digit=digit,
                        count=count,
                        mark=mark,
                        panels=panels,
                        button=button2)

    elif digit == 3 and digit in digits:
        inner_win_check(digits=digits,
                        digit=digit,
                        count=count,
                        mark=mark,
                        panels=panels,
                        button=button3)

    elif digit == 4 and digit in digits:
        inner_win_check(digits=digits,
                        digit=digit,
                        count=count,
                        mark=mark,
                        panels=panels,
                        button=button4)

    elif digit == 5 and digit in digits:
        inner_win_check(digits=digits,
                        digit=digit,
                        count=count,
                        mark=mark,
                        panels=panels,
                        button=button5)

    elif digit == 6 and digit in digits:
        inner_win_check(digits=digits,
                        digit=digit,
                        count=count,
                        mark=mark,
                        panels=panels,
                        button=button6)

    elif digit == 7 and digit in digits:
        inner_win_check(digits=digits,
                        digit=digit,
                        count=count,
                        mark=mark,
                        panels=panels,
                        button=button7)

    elif digit == 8 and digit in digits:
        inner_win_check(digits=digits,
                        digit=digit,
                        count=count,
                        mark=mark,
                        panels=panels,
                        button=button8)

    elif digit == 9 and digit in digits:
        inner_win_check(digits=digits,
                        digit=digit,
                        count=count,
                        mark=mark,
                        panels=panels,
                        button=button9)

    if(count > 8 and
       win_combinations(panels=panels, sign='X') == FALSE and
       win_combinations(panels=panels, sign='O') == TRUE):
        msg.showinfo("Result", "Match Tied")
        root.destroy()

# .0 Execution

root.mainloop()