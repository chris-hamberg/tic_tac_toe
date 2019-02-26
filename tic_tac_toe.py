from tkinter import messagebox
import tkinter

def initialize():
    game_map = {
            0: None, 1: None, 2: None,
            3: None, 4: None, 5: None,
            6: None, 7: None, 8: None
            }
    return game_map

game_map = initialize()

def win(winner):
    messagebox.showinfo('WIN', '%s WINS'%winner)
    global game_map
    game_map = initialize()
    value.set('')
    for button in buttons:
        button.config(text=value.get())
    label1.config(text='It is X\'s turn.', font=('Courier', 14))

def check_for_win():
    if game_map[0] != None:
        winner = game_map[0]
        if game_map[0] == game_map[1] == game_map[2]:
            win(winner)
        elif game_map[0] == game_map[3] == game_map[6]:
            win(winner)
        elif game_map[0] == game_map[4] == game_map[8]:
            win(winner)

    if game_map[4] != None:
        winner = game_map[4]
        if game_map[3] == game_map[4] == game_map[5]:
            win(winner)
        elif game_map[1] == game_map[4] == game_map[7]:
            win(winner)
        elif game_map[2] == game_map[4] == game_map[6]:
            win(winner)
        
    if game_map[8] != None:
        winner = game_map[8]
        if game_map[6] == game_map[7] == game_map[8]:
            win(winner)
        elif game_map[2] == game_map[5] == game_map[8]:
            win(winner)

    if None not in list(game_map.values()):
        win('NO ONE')

def switch(event, pos):
    if game_map[pos]:
        return
    elif value.get() != 'X':
        value.set('X')
    else:
        value.set('O')
    event.widget.config(text=value.get())
    label1.config(
            text='It is %s\'s turn.'
            % ('X' if value.get() != 'X' else 'O'),
            font=('Courier', 14))
    
    game_map[pos] = value.get()
    check_for_win()

root = tkinter.Tk()
root.resizable(width=False, height=False)
root.title('TIC TAC TOE')
frame1 = tkinter.Frame(root)
frame2 = tkinter.Frame(root)
value = tkinter.StringVar()

button1 = tkinter.Button(frame1, width=1, height=1)
button1.grid(row=0, column=0, padx=10, pady=10, ipadx=10, ipady=10)
button1.bind('<Button-1>', lambda x: switch(x, 0))

button2 = tkinter.Button(frame1, width=1, height=1)
button2.grid(row=0, column=1, padx=10, pady=10, ipadx=10, ipady=10)
button2.bind('<Button-1>', lambda x: switch(x, 1))

button3 = tkinter.Button(frame1, width=1, height=1)
button3.grid(row=0, column=2, padx=10, pady=10, ipadx=10, ipady=10)
button3.bind('<Button-1>', lambda x: switch(x, 2))

button4 = tkinter.Button(frame1, width=1, height=1)
button4.grid(row=1, column=0, padx=10, pady=10, ipadx=10, ipady=10)
button4.bind('<Button-1>', lambda x: switch(x, 3))

button5 = tkinter.Button(frame1, width=1, height=1)
button5.grid(row=1, column=1, padx=10, pady=10, ipadx=10, ipady=10)
button5.bind('<Button-1>', lambda x: switch(x, 4))

button6 = tkinter.Button(frame1, width=1, height=1)
button6.grid(row=1, column=2, padx=10, pady=10, ipadx=10, ipady=10)
button6.bind('<Button-1>', lambda x: switch(x, 5))

button7 = tkinter.Button(frame1, width=1, height=1)
button7.grid(row=2, column=0, padx=10, pady=10, ipadx=10, ipady=10)
button7.bind('<Button-1>', lambda x: switch(x, 6))

button8 = tkinter.Button(frame1, width=1, height=1)
button8.grid(row=2, column=1, padx=10, pady=10, ipadx=10, ipady=10)
button8.bind('<Button-1>', lambda x: switch(x, 7))

button9 = tkinter.Button(frame1, width=1, height=1)
button9.grid(row=2, column=2, padx=10, pady=10, ipadx=10, ipady=10)
button9.bind('<Button-1>', lambda x: switch(x, 8))

label1 = tkinter.Label(frame2, text='It is X\'s turn.', font=('Courier', 14))
label1.pack(fill=tkinter.X)

frame1.pack()
frame2.pack()

buttons = [button1, button2, button3, button4, button5, button6, 
        button7, button8, button9]

root.mainloop()
