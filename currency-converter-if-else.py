print("##########################")
print("SELECT INPUT CURRENCY")
print(" * EUR")
print(" * USD")
print(" * MDL")
print("##########################")
currency_in = input("choose: ")
money_in = float(input("money: "))

print("##########################")
print("SELECT OUTPUT CURRENCY")

if currency_in != "EUR":
    print(" * EUR")
if currency_in != "USD":
    print(" * USD")
if currency_in != "MDL":
    print(" * MDL")
currency_out = input("choose: ")
eur_2_usd = 1.1
eur_2_mdl = 20.0

if currency_in == "EUR":
    if currency_out == "USD":
        money_out = money_in * eur_2_usd
    if currency_out == "MDL":
        money_out = money_in * eur_2_mdl

if currency_in == "USD":
    if currency_out == "EUR":
        money_out = money_in / eur_2_usd
    if currency_out == "MDL":
        money_out = money_in * eur_2_mdl / eur_2_usd
        
if currency_in == "MDL":
    if currency_out == "EUR":
        money_out = money_in / eur_2_mdl
    if currency_out == "USD":
        money_out = money_in / eur_2_mdl * eur_2_usd

print(round(money_out, 2))