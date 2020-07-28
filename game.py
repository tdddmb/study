import random

filename = 'rating.txt'
username = input('{}'.format('Enter your name: '))
print('Hello, {}'.format(username))
opened_file = open(filename, 'r')
rating = {}

for line in opened_file:
    (name, score) = line.split()
    rating[name] = int(score)

if username not in rating:
    rating[username] = 0
current_score = rating[username]

all_options = input().split(',')
if all_options == ['']:
    all_options = ['rock', 'paper', 'scissors']
print('Okay, let\'s start')

while True:
    user_option = input()
    if user_option == '!exit':
        print('Bye!')
        break

    if user_option == '!rating':
        print('Your rating:', current_score)
        continue

    if user_option in all_options:
        option_index = all_options.index(user_option)
        available_options = all_options[option_index + 1:] + all_options[:option_index]
        computer_option = random.choice(all_options)
        if user_option == computer_option:
            print('There is a draw ({})'.format(computer_option))
            current_score += 50
            continue
        computer_option_index = available_options.index(computer_option)
        if computer_option_index >= (len(available_options) / 2):
            print('Well done. Computer chose {} and failed'.format(computer_option))
            current_score += 100
        else:
            print('Sorry, but computer chose {}'.format(computer_option))
    else:
        print('Invalid input')
opened_file.close()