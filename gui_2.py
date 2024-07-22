import tkinter as tk

exchange_rates = {
    "THB": {"USD": 0.03, "EUR": 0.025, "JPY": 3.4},
    "USD": {"THB": 33.0, "EUR": 0.85, "JPY": 110.0},
    "EUR": {"THB": 39.0, "USD": 1.18, "JPY": 129.53},
    "JPY": {"THB": 0.29, "USD": 0.0091, "EUR": 0.0077}
}

def on_click():
    from_currency = tv_from_currency.get()
    to_currency = tv_to_currency.get()
    try:
        amount = float(tv_amount.get())
        if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
            rate = exchange_rates[from_currency][to_currency]
            convert_amount = amount * rate
            tv_result.set(f'{convert_amount:.2f} {to_currency}')
        else:
            tv_result.set("Invalid currency")
    except ValueError:
        tv_result.set("Invalid amount")

root = tk.Tk()
root.title("Currency Converter")
root.option_add("*Font", "impact 20")

tv_from_currency = tk.StringVar(value="THB")
tv_to_currency = tk.StringVar(value="USD")
tv_amount = tk.StringVar(value=0.00)
tv_result = tk.StringVar()

tk.Label(root, text="THB USD EUR JPY").pack(side="top")
tk.Label(root, text="From:").pack(side="left", padx=10)
tk.Entry(root, textvariable=tv_from_currency, width=6).pack(side="left", padx=10)
tk.Label(root, text="To:").pack(side="left", padx=10)
tk.Entry(root, textvariable=tv_to_currency, width=6).pack(side="left", padx=10)
tk.Label(root, text="Amount:").pack(side="left", padx=10)
tk.Entry(root, textvariable=tv_amount, width=6).pack(side="left", padx=10)
tk.Button(root, text="convert",bg ="lightgrey",command=on_click).pack(side="left")
tk.Label(root, textvariable=tv_result).pack(side="left")

root.mainloop()