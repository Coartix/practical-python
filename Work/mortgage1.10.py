# Exercise 1.10 - 1.11

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
    print(month,round(total_paid,2),round(principal))