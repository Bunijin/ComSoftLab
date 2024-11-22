import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class VendingMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("Vending Machine")
        self.root.option_add("*Font", "Comic_Sans_MS 16")

        self.balance = tk.StringVar(value="0.00")
        self.total_balance = tk.StringVar(value="0.00")
        self.total_cost = tk.StringVar(value="0.00")
        self.message = tk.StringVar()
        self.text_cost = tk.StringVar(value="Cost: $0.00")
        self.text_balance = tk.StringVar(value="Bal: $0.00")

        self.purchase_history = []
        self.total_revenue = 0.0

        self.items = {
            "Chips": 1.50,
            "Soda": 1.25,
            "Candy": 0.75,
            "Water": 1.00
        }

        self.create_widgets()

    def create_widgets(self):
        for i, (item, price) in enumerate(self.items.items()):
            lbl = tk.Label(self.root, text=item)
            lbl.grid(row=i, column=0, padx=5, pady=5)

            btn = tk.Button(self.root, text=f'${price:.2f}', background="gray72", 
                            command=lambda p=price, i=item: self.calculate_total_price(p, i), width=10)
            btn.grid(row=i, column=1, padx=5, pady=5)

            # Load and display image
            img = Image.open(f"{item.lower()}.png")
            img = img.resize((50, 50), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            img_label = tk.Label(self.root, image=photo)
            img_label.image = photo
            img_label.grid(row=i, column=2, padx=5, pady=5)

        tk.Label(self.root, textvariable=self.text_balance).grid(row=4, column=0, padx=5, pady=5)
        tk.Label(self.root, textvariable=self.text_cost).grid(row=4, column=1, padx=5, pady=5)

        tk.Entry(self.root, textvariable=self.balance).grid(row=5, column=0, padx=5, pady=5)

        tk.Button(self.root, text='Insert Money', background="gray72", command=self.insert_money, width=10).grid(row=6, column=0, padx=5, pady=5)
        tk.Button(self.root, text='Purchase', background="gray72", command=self.perform_checkout, width=10).grid(row=6, column=1, padx=5, pady=5)
        
        # New button for checking purchase history
        tk.Button(self.root, text='Check History', background="gray72", command=self.show_purchase_history, width=10).grid(row=6, column=2, padx=5, pady=5)

        tk.Label(self.root, textvariable=self.message).grid(row=7, columnspan=3, padx=5, pady=5)

    def calculate_total_price(self, item_cost, item_name):
        try:
            current_total_cost = float(self.total_cost.get())
            update_total_cost = current_total_cost + item_cost
            self.total_cost.set(f"{update_total_cost:.2f}")
            self.text_cost.set(f'Cost: ${update_total_cost:.2f}')
            self.purchase_history.append(item_name)
        except ValueError:
            self.message.set('Invalid input')

    def insert_money(self):
        try:
            entered_amount = float(self.balance.get())
            current_total_balance = float(self.total_balance.get())
            updated_total_balance = current_total_balance + entered_amount
            self.total_balance.set(f"{updated_total_balance:.2f}")
            self.balance.set("0.00")
            self.text_balance.set(f'Bal: ${updated_total_balance:.2f}')
        except ValueError:
            self.message.set('Invalid input for balance')

    def perform_checkout(self):
        try:
            cost = float(self.total_cost.get())
            bal = float(self.total_balance.get())
            if bal < cost:
                self.message.set('Insufficient balance. Please insert more money.')
            elif cost == 0:
                self.message.set('Please select an item before purchasing.')
            else:
                changes = bal - cost
                self.total_balance.set("0.00")
                self.total_cost.set("0.00")
                self.text_cost.set('Cost: $0.00')
                self.text_balance.set('Bal: $0.00')
                self.message.set(f'Purchase Successful: Your change is ${changes:.2f}')
                self.total_revenue += cost
        except ValueError:
            self.message.set('Invalid input for total cost or balance')

    def show_purchase_history(self):
        if not self.purchase_history:
            messagebox.showinfo("Purchase History", "No purchases made yet.")
        else:
            history_str = "Purchase History:\n" + "\n".join(self.purchase_history)
            messagebox.showinfo("Purchase History", history_str)
        print(f"Total Revenue: ${self.total_revenue:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    vending_machine = VendingMachine(root)
    root.mainloop()