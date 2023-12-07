from forex_python.converter import CurrencyRates
import json
from datetime import datetime

def convert_currency(amount, from_currency, to_currency):
    try:
        rate = CurrencyRates().get_rate(from_currency, to_currency)
        converted_amount = amount * rate
        return converted_amount
    except:
        return None

def save_conversion_history(history):
    with open('conversion_history.json', 'w') as file:
        json.dump(history, file)

def load_conversion_history():
    try:
        with open('conversion_history.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    conversion_history = load_conversion_history()

    amount = float(input("Entrez la somme à convertir : "))
    from_currency = input("Entrez la devise d'origine (code ISO) : ").upper()
    to_currency = input("Entrez la devise de destination (code ISO) : ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)

    if converted_amount is not None:
        print(f"{amount} {from_currency} équivaut à {converted_amount:.2f} {to_currency}")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conversion_entry = {
            "timestamp": timestamp,
            "amount": amount,
            "from_currency": from_currency,
            "to_currency": to_currency,
            "converted_amount": converted_amount
        }
        conversion_history.append(conversion_entry)
        save_conversion_history(conversion_history)
    else:
        print(f"Conversion de {from_currency} à {to_currency} impossible.")

if __name__ == "__main__":
    main()
