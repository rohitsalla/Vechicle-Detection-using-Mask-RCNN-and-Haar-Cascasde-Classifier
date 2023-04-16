Import tKinter as tk
root = tk.Tk()
button = tk.Button(root, text='Stop', width=25, command=root.stop)
button.pack()
root.mainloop()
