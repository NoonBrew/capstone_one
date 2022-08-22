from datetime import datetime

def GreetingMessage():
    print('Please Enter your name: ')
    name = input()
    print('Greetings, {}, has {} letters!'.format(name.capitalize(), len(name)))
    print('{}, what month is your birthday?'.format(name.capitalize()))
    birthdayMonth = input()

    if int(birthdayMonth) == datetime.now().month or birthdayMonth.capitalize() == datetime.now().strftime('%B'):
        print('It is your birthday month!!')
    else:
        print('It is not your birthday Month!')

GreetingMessage()

