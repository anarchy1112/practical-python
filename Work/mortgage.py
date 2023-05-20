# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months=0
extra_payment=1000
extra_payment_start_month=61
extra_payment_end_month=108

while principal > 0:
    months += 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    if months>=extra_payment_start_month and months<=extra_payment_end_month:
        principal-=extra_payment
        total_paid+=extra_payment
    print(months, round(total_paid), round(principal, 2))
    if principal<payment:
        total_paid += principal
        principal=0



print('Total paid', total_paid, 'total months:', months)