class Author:
    # Init function, set books default value to an empty list.
    def __init__(self, name):
        self.name = name
        self.books = []

    # Function to append books to the list
    def publish(self, book):
        if book in self.books:
            print('Error: {} is already in the list.'.format(book))
        else:
            self.books.append(book)

    def __str__(self):
        book_list = ', '.join(self.books) or 'No published books'
        return 'the author, {}, has published the following books: {}'.format(self.name, book_list)

def main():

    authorOne = Author('J.R.R Tolkein')

    authorOne.publish('Fellowship of the Ring')
    authorOne.publish('The Two Towers')
    authorOne.publish('Return of the King')

    print(authorOne)

    authorOne.publish('Fellowship of the Ring')

    print(authorOne)

    authorTwo = Author('Nate O')

    print(authorTwo)


main()