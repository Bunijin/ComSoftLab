import tkinter as tk

def on_click():
    lbs = tv_kg.get() * 2.205
    tv_lbs.set(f'{lbs:.2f} lbs.')
    usd = tv_thb.get() * 0.028
    tv_usd.set(f'{usd:.2f} USD.')

root = tk.Tk()
root.option_add("*Font", "impact 20")
tv_kg = tk.DoubleVar()
tv_lbs = tk.StringVar()
tv_thb = tk.DoubleVar()
tv_usd = tk.StringVar()

tk.Entry(root, textvariable=tv_kg, width=7, justify="right").pack(side="left", padx=10)
tk.Label(root, text="kg.").pack(side="left", padx=10)
tk.Button(root, text=" = ", bg="green", command=on_click).pack(side="left")
tk.Label(root, textvariable=tv_lbs).pack(side="left")
tk.Entry(root, textvariable=tv_thb, width=7, justify="right").pack(side="left", padx=10)
tk.Label(root, text="THB").pack(side="left", padx=10)
tk.Button(root, text=" = ", bg="green", command=on_click).pack(side="left")
tk.Label(root, textvariable=tv_usd).pack(side="left")

root.mainloop()
