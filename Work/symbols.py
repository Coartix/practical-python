# Exercise 1.13

symbols = 'AAPL,IBM,MSFT,YHOO,SCO'

print(symbols[0])
print(symbols[1])
print(symbols[2])
print(symbols[-1])
print(symbols[-2])

# Exercise 1.14

symbols = symbols + 'GOOG'
print(symbols)

symbols = symbols[0:-4]+',GOOG'
print(symbols)

symbols= 'HPQ,'+symbols
print(symbols)

# Exercise 1.15

print('IBM' in symbols)
print('AA' in symbols)
print('CAT' in symbols)

# Exercise 1.16

print(symbols.lower())

print(symbols.find('MSFT'))
print(symbols[13:17])
print(symbols.replace('SCO','DOA'))

name = '  IBM  \n'
print(name.strip())

# Exercise 1.17

name = 'IBM'
shares = 100
price = 91.1
print(f'{shares} shares of {name} at ${price:0.2f}')

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
month=0
while principal > 0:
    if extra_payment_start_month<=month<=extra_payment_end_month:
        if principal * (1 + rate / 12) < (payment + 1000):
            total_paid += principal
            principal = 0
        else:
            principal = principal * (1+rate/12) - (payment+1000)
            total_paid += payment
    else:
        if principal * (1 + rate / 12) < payment:
            total_paid += principal
            principal = 0
        else:
            principal = principal * (1 + rate / 12) - payment
            total_paid += payment
    month+=1
    print(f"Month : {month:0>3d} Total paid: {total_paid:.2f} Left to pay: {principal:.2f}")
