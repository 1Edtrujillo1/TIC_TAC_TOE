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



# .0 Execution
