# mortgage.py
#
# Exercise 1.7 - 1.8

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
i=0
while principal > 0:
    if i<12:
        principal = principal * (1+rate/12) - (payment+1000)
    else:
        principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    i+=1
print('Total paid', round(total_paid,2))