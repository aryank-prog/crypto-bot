import tkinter as tk
import logging
from bitmex import get_contracts

#goal is to initialize few things in file
#the 2 connectors, the interface main component, the logger object
logger = logging.getLogger()



if __name__ == '__main__':
    bitmex_contracts = get_contracts()

    root = tk.Tk()

    i = 0
    j = 0

    for contract in bitmex_contracts:
        label_widget = tk.Label(root, text=contract)
        label_widget.grid(row=i, column=j)

        if i == 4:
            j += 1
            i = 0
        else:
            i += 1

    root.mainloop()

