from datetime import datetime

def main():
    GreetingMessage()

def GreetingMessage():
    name = input('Please Enter your name: ')
    print('Greetings, {}, has {} letters!'.format(name.capitalize(), len(name)))
    birthdayMonth = input('{}, what month is your birthday? '.format(name.capitalize()))

    numberBirthday = 0
    if birthdayMonth.isnumeric():
        numberBirthday = int(birthdayMonth)
        
    if numberBirthday == datetime.now().month or birthdayMonth.capitalize() == datetime.now().strftime('%B'):
        print('It is your birthday month!!')
    else:
        print('It is not your birthday Month!')


main()
