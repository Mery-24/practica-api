from currency_converter import currencyConverter
from config import API_KEY

def main():
    converter = CurencyConverter(API_KEY)

    while True:
        print("\n--- Calculadora de Divisas ---")
        print("1. Convertir divisas")
        print("2. salir")

        choice = input("Elige una opción: ")

        if choice == '1':
            from_currency = input("Divisa de origen (por ejemplo, USD): ").upper()
            to_currency = input("Divisa de destino (por ejemplo, EUR): ").upper()
            amount = float(input(f"cantidad en{from_currency}: "))
            rate = converter.get_exchange_rate(from_currency, to_currency)
            if rate:
                converted_amount = amount * rate
                print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        elif choice == '2':    
            print("Saliendo de la calculadora...")
            break
        else:
            print("opción no válida. Intenta de nuevo.")

if _name_ == "_main_":
    main()
                