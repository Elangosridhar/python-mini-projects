import tkinter as tk
from tkinter import ttk, messagebox

class CurrencyConverter:
    def __init__(self):
        self.exchange_rates = {
            "USD": 1.0,
            "EUR": 0.94,
            "GBP": 0.79,
            "INR": 83.58
        }

    def convert(self, from_currency, to_currency, amount):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            raise ValueError("Invalid currency code")
        from_rate = self.exchange_rates[from_currency]
        to_rate = self.exchange_rates[to_currency]
        return amount * (to_rate / from_rate)

class CurrencyConverterApp:
    def __init__(self, root):
        self.converter = CurrencyConverter()
        self.root = root
        self.root.title("Currency Converter")
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Amount:").grid(column=1, row=1, sticky=tk.W)
        self.amount_entry = ttk.Entry(frame, width=15)
        self.amount_entry.grid(column=2, row=1, sticky=tk.W)

        ttk.Label(frame, text="From:").grid(column=1, row=2, sticky=tk.W)
        self.from_currency = ttk.Combobox(frame, values=["USD", "EUR", "GBP", "INR"], state='readonly')
        self.from_currency.grid(column=2, row=2, sticky=tk.W)
        self.from_currency.current(0)

        ttk.Label(frame, text="To:").grid(column=1, row=3, sticky=tk.W)
        self.to_currency = ttk.Combobox(frame, values=["USD", "EUR", "GBP", "INR"], state='readonly')
        self.to_currency.grid(column=2, row=3, sticky=tk.W)
        self.to_currency.current(1)

        self.result_label = ttk.Label(frame, text="")
        self.result_label.grid(column=1, row=5, columnspan=2, sticky=tk.W)

        convert_button = ttk.Button(frame, text="Convert", command=self.convert_currency)
        convert_button.grid(column=2, row=4, sticky=tk.W)

    def convert_currency(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency.get()
            to_currency = self.to_currency.get()
            result = self.converter.convert(from_currency, to_currency, amount)
            self.result_label.config(text=f"{amount} {from_currency} = {result:.2f} {to_currency}")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount or currency code")

def main():
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
