import sys
from math import ceil, log
# errors
ERROR_MESSAGE = 'Incorrect parameters'
ERROR_FLAG = False
def error_func():
    print(ERROR_MESSAGE)
    ERROR_FLAG = True
# variables
args = sys.argv
key = []
value = []
dic = {}
word_counter = 0
# with this code we will get all arguement's names with their values to the dictionary
for arg in args[1:]:
    index = 0
    eq_index = 0
    key.append('')
    value.append('')
    for letter in arg:
        index += 1
        if letter == '=':
            eq_index = index
            break
        else:
            key[word_counter] += letter
    for letter in arg[eq_index:]:
        value[word_counter] += letter
    if key[word_counter] in dic:
        error_func
    else:
        if key[word_counter] == '--type':
            dic[key[word_counter]] = value[word_counter]
        elif key[word_counter] == '--interest':
            dic[key[word_counter]] = float(value[word_counter])
        else:
            if int(value[word_counter]) > 0:
                dic[key[word_counter]] = int(value[word_counter])
    word_counter += 1
# body
if len(dic) < 4:
    error_func()
if not ERROR_FLAG:
    if dic['--type'] == 'diff':
        if '--payment' in dic or '--interest' not in dic:
            error_func()
        else:
            i = dic['--interest'] / 100 / 12  # from percentage to decimal, from yearly to monthly
            overpayment = 0
            for current_month in range(dic['--periods']):
                diff_payment = ceil((dic['--principal'] / dic['--periods']) + i * (dic['--principal'] \
                - (dic['--principal'] * (current_month) / dic['--periods'])))
                overpayment += diff_payment
                print('Month {}: paid out {}'.format(current_month + 1, diff_payment))
            overpayment -= dic['--principal']
            print("Overpayment =", overpayment)
    elif dic['--type'] == 'annuity':
        if '--interest' not in dic:
            error_func()
        else:
            i = dic['--interest'] / 100 / 12  # from percentage to decimal, from yearly to monthly
            if '--principal' not in dic:
                dic['--principal'] = int(dic['--payment'] \
                                     / ((i * ((1 + i)**dic['--periods']))
                                     / ((1 + i)**dic['--periods'] - 1)))
                overpayment = dic['--payment'] * dic['--periods'] - dic['--principal']
                print("Your credit principal =", dic['--principal'], "!")
                print("Overpayment =", overpayment)
            elif '--payment' not in dic:
                dic['--payment'] = ceil(dic['--principal'] \
                                     * ((i * ((1 + i)**dic['--periods']))
                                     / ((1 + i)**dic['--periods'] - 1)))
                overpayment = dic['--payment'] * dic['--periods'] - dic['--principal']
                print("Your annuity payment =", dic['--payment'], "!")
                print("Overpayment =", overpayment)
            elif '--periods' not in dic:
                dic['--periods'] = ceil(log(dic['--payment'] / (dic['--payment'] - i * dic['--principal']), 1 + i))
                overpayment = dic['--payment'] * dic['--periods'] - dic['--principal']
                if dic['--periods'] >= 12:
                    if dic['--periods'] % 12 == 0:
                        print("You need", dic['--periods'] // 12, "years to repay this credit!")
                    else:
                        print("You need", dic['--periods'] // 12, "years and", dic['--periods'] % 12,
                              "months to repay this credit!")
                else:
                    if dic['--periods'] != 1:
                        print("You need", dic['--periods'], "months to repay this credit!")
                        print(str(dic))
                    else:
                        print("You need", dic['--periods'], "month to repay this credit!")
                print("Overpayment =", overpayment)

    else:
        error_func()
