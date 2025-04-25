import requests
from tkinter import Tk, Label, Button, Entry, StringVar, OptionMenu

# Class-based implementation for the Currency Converter
class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.currencies = [
            "USD", "EUR", "INR", "GBP", "AUD", "CAD", "SGD", "JPY", "CNY",
            "CHF", "NZD", "HKD", "SEK", "KRW", "MYR", "THB", "ZAR"
        ]  # Add more currencies as needed
        
        # Create the GUI
        self.create_widgets()
    
    def create_widgets(self):
        # Amount input
        Label(self.root, text="Enter Amount:").grid(row=0, column=0)
        self.amount_entry = Entry(self.root)
        self.amount_entry.grid(row=0, column=1)
        
        # Dropdown menus for currency selection
        self.base_currency = StringVar(self.root)
        self.target_currency = StringVar(self.root)
        self.base_currency.set(self.currencies[0])  # Default to first currency
        self.target_currency.set(self.currencies[2])  # Default to INR
        
        Label(self.root, text="From:").grid(row=1, column=0)
        OptionMenu(self.root, self.base_currency, *self.currencies).grid(row=1, column=1)
        
        Label(self.root, text="To:").grid(row=2, column=0)
        OptionMenu(self.root, self.target_currency, *self.currencies).grid(row=2, column=1)
        
        # Conversion button
        Button(self.root, text="Convert", command=self.convert).grid(row=3, column=0, columnspan=2)
        
        # Result display
        self.result_label = Label(self.root, text="Converted Amount: ")
        self.result_label.grid(row=4, column=0, columnspan=2)
    
    def get_exchange_rate(self, base_currency, target_currency):
        try:
            url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
            response = requests.get(url)
            data = response.json()
            return data['rates'][target_currency]
        except Exception as e:
            return None
    
    def convert(self):
        try:
            amount = float(self.amount_entry.get())
            rate = self.get_exchange_rate(self.base_currency.get(), self.target_currency.get())
            
            if rate is None:
                self.result_label.config(text="Error: Unable to fetch rates!")
            else:
                converted_amount = rate * amount
                self.result_label.config(text=f"Converted Amount: {converted_amount:.2f}")
        except ValueError:
            self.result_label.config(text="Invalid input! Please enter a number.")

# Main function to run the application
if __name__ == "__main__":
    root = Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()