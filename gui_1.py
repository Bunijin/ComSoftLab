import tkinter as Tk

root = Tk.Tk()
root.option_add("*Font","consolas 20")

Tk.Label(root, text="Lab1", bg="green").pack(fill="x")
Tk.Label(root, text="Software Lab", bg="deep sky blue").pack(fill="x")
Tk.Label(root, text="Just be yourself, because life's too short to be anybody else.", bg="gold").pack(fill="x")
Tk.Label(root, text="Just be yourself, because life's too short to be anybody else.", bg="orange", wraplength=700, justify="right").pack(fill="x")
Tk.Label(root, text="Just be yourself, because life's too short to be anybody else.", bg="deep sky blue").pack(fill="x")
Tk.Label(root, text="Just be yourself, because life's too short to be anybody else.\n\nStep Up 2: The Streets", bg="hot pink", justify="center").pack(fill="x")

root.mainloop()