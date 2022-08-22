

def yourClasses():
    classList = []
    classTot = input('How many class are you taking this semester? ')
    while not classTot.isnumeric() or int(classTot) < 0:
        print('Please enter a positive number. ')
        classTot = input('How many class are you taking this semester? ')
    
    for c in range(int(classTot)):
        className = input('Enter the name of class {}: '.format(c +1))
        classList.append(className.capitalize())
    
    print('The classes you are taking are:')
    for c in classList:
        print(c)


yourClasses()