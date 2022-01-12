import math as m
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', choices=['annuity', 'diff'], default=0)
parser.add_argument('--principal', default=0)
parser.add_argument('--periods', default=0)
parser.add_argument('--interest', default=0)
parser.add_argument('--payment', default=0)

args = parser.parse_args()
action = args.type
principal = float(args.principal)
n = int(args.periods)
interest = float(args.interest)
payment = float(args.payment)
xs = [action, principal, n, interest, payment]



def check():
    if xs.count(0) >= 2:
        print("Incorrect parameters")
    elif action == 'diff' and payment != 0:
        print("Incorrect parameters")
    else:
        bank()


def user_input_and_calc():
    calculate(action)


def calculate(action):
    if action == 'diff':
        diff()
    elif action == 'annuity':
        if principal == 0:
            loan_principal()
        elif n == 0:
            number_of_months()
        elif payment == 0:
            ordinary_annuity()


def number_of_months_convert(num):
    if num > 12:
        if num == 12:
            print('It will take 1 year to repay this loan!')
        else:
            year = m.floor(num / 12)
            month = m.ceil(num % 12)
            if month == 1:
                print('It will take {} years and 1 month to repay this loan!'.format(year))
            elif num % 12 == 0:
                num = num / 12
                print('It will take {} years to repay this loan!'.format(int(num)))
            else:
                print('It will take {} years and {} months to repay this loan!'.format(year, month))
    elif num < 12:
        if num == 1:
            print('It will take 1 month to repay this loan!')
        else:
            print('It will take {} months to repay this loan!'.format(num))


def number_of_months():
    i = nominal_interest(interest)
    num = m.ceil(m.log(payment / (payment - i * principal), 1 + i))
    number_of_months_convert(num)
    overpayment(principal, num, payment)
    return num


def ordinary_annuity():
    i = nominal_interest(interest)
    a = i * ((1 + i) ** n)
    b = (1 + i) ** n - 1
    annuity = m.ceil(principal * a / b)
    print('Your monthly payment = {}!'.format(annuity))
    overpayment(principal, n, annuity)
    return annuity


def nominal_interest(loan_interest):
    i = loan_interest / (12 * 100)
    return i


def overpayment(principal, n, payment):
    over = m.ceil((payment * n) - principal)
    print('Overpayment = {}'.format(over))
    return over


def diff():
    i = nominal_interest(interest)
    over = 0
    for mon in range(1, n + 1):
        d = m.ceil(principal / n + i * (principal - (principal * (mon - 1) / n)))
        over += d
        print('Month {}: payment is {}'.format(mon, d))
    over -= principal
    print('Overpayment = {}'.format(over))


def loan_principal():
    i = nominal_interest(interest)
    a = i * ((1 + i) ** n)
    c = (1 + i) ** n - 1
    p = m.floor(payment / (a / c))
    print("Your loan principal = {}!".format(p))
    overpayment(p, n, payment)
    return p


def bank():
    user_input_and_calc()


check()
