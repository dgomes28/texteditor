import tkinter as tk

# root = Tk(screenName=None, baseName=None, className='tk', useTk=1)

# m = tkinter.Tk(screenName=None, baseName=None, className='Salgueiro Gay', useTk=1)

# w = Text(m, height=2, width=30)

# m.mainloop()

r = tk.Tk()
r.title('Hello World')

r.geometry("400x400")

button = tk.Button(r, text='Stop', width=1, command=r.destroy)
textsize_button = tk.Button(r, text='+', width=1, command=tk.Text(size=25))
button.grid(row=1, column=200)
button.pack()
T = tk.Text(r, height=390, width=390)
T.pack()


r.mainloop()