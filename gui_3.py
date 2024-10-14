import tkinter as tk

def calculate_total_price(item_cost):
    try:
        current_total_cost = float(total_cost.get())
        update_total_cost = current_total_cost + float(item_cost)
        total_cost.set(f"{update_total_cost:.2f}")
        text_cost.set(f'Cost: ${update_total_cost:.2f}')
    except ValueError:
        message.set('Invalid input')

def insert_money():
    try:
        entered_amount = float(balance.get())
        current_total_balance = float(total_balance.get())
        updated_total_balance = current_total_balance + entered_amount
        total_balance.set(f"{updated_total_balance:.2f}")
        balance.set("0.00")
        text_balance.set(f'Bal: ${updated_total_balance:.2f}')
    except ValueError:
        message.set('Invalid input for balance')

def perform_checkout():
    try:
        cost = float(total_cost.get())
        bal = float(total_balance.get())
        if bal < cost:
            message.set('Insufficient balance. Please insert more money.')
        elif cost == 0:
            message.set('Please select an item before purchasing.')
        else:
            changes = bal - cost
            total_balance.set("0.00")
            total_cost.set("0.00")
            text_cost.set('Cost: $0.00')
            text_balance.set('Bal: $0.00')
            message.set(f'Purchase Successful: Your change is ${changes:.2f}')
    except ValueError:
        message.set('Invalid input for total cost or balance')

root = tk.Tk()
root.title("Vending Machine")
root.option_add("*Font", "Comic_Sans_MS 16")

balance = tk.StringVar(value="0.00")
total_balance = tk.StringVar(value="0.00")
total_cost = tk.StringVar(value="0.00")
message = tk.StringVar()
text_cost = tk.StringVar(value="Cost: $0.00")
text_balance = tk.StringVar(value="Bal: $0.00")

btn_chips = tk.Button(root, text='$1.50',background="gray72", command=lambda: calculate_total_price(1.50), width=10)
btn_soda = tk.Button(root, text='$1.25',background="gray72", command=lambda: calculate_total_price(1.25), width=10)
btn_candy = tk.Button(root, text='$0.75',background="gray72", command=lambda: calculate_total_price(0.75), width=10)
btn_water = tk.Button(root, text='$1.00',background="gray72", command=lambda: calculate_total_price(1.00), width=10)
btn_insert_money = tk.Button(root, text='Insert Money',background="gray72", command=insert_money, width=10)
btn_purchase = tk.Button(root, text='Purchase',background="gray72", command=perform_checkout, width=10)

lbl_chips = tk.Label(root, text="Chips")
lbl_soda = tk.Label(root, text="Soda")
lbl_candy = tk.Label(root, text="Candy")
lbl_water = tk.Label(root, text="Water")
lbl_balance = tk.Label(root, textvariable=text_balance)
lbl_cost = tk.Label(root, textvariable=text_cost)
lbl_message = tk.Label(root, textvariable=message)

entry_balance = tk.Entry(root, textvariable=balance)

lbl_chips.grid(row=0, column=0, padx=5, pady=5)
btn_chips.grid(row=0, column=1, padx=5, pady=5)

lbl_soda.grid(row=1, column=0, padx=5, pady=5)
btn_soda.grid(row=1, column=1, padx=5, pady=5)

lbl_candy.grid(row=2, column=0, padx=5, pady=5)
btn_candy.grid(row=2, column=1, padx=5, pady=5)

lbl_water.grid(row=3, column=0, padx=5, pady=5)
btn_water.grid(row=3, column=1, padx=5, pady=5)

lbl_balance.grid(row=4, column=0, padx=5, pady=5)
lbl_cost.grid(row=4, column=1, padx=5, pady=5)

entry_balance.grid(row=5, column=0, padx=5, pady=5)

btn_insert_money.grid(row=6, column=0, padx=5, pady=5)
btn_purchase.grid(row=6, column=1, padx=5, pady=5)

lbl_message.grid(row=7, columnspan=2, padx=5, pady=5)

root.mainloop()