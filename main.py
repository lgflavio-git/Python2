amount_str = input("Enter the amount:")
amount = int(amount_str)


source_currency = input("Enter the source currency (USD/EUR/GBP):")
target_currency = input("Enter the target currency (USD/EUR/GBP):")

if source_currency == "USD" and target_currency == "EUR":
    conversion_rate = 0.7

if source_currency == "GBP" and target_currency == "EUR":
    conversion_rate = 1.2

if source_currency == "USD" and target_currency == "GBP":
    conversion_rate = 1/1.4
if source_currency == "EUR" and target_currency == "GBP":
    conversion_rate = 1/1.2

if source_currency == "GBP" and target_currency == "USD":
    conversion_rate = 1.4
if source_currency == "EUR" and target_currency == "USD":
    conversion_rate = 1/0.7



converted_amount :float = amount * conversion_rate
print(f'{amount}  {source_currency} is equal to {converted_amount}  {target_currency}' )
