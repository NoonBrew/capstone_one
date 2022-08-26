
def main():
    # Ask for a string to convert
    stringToCamelCase = input('Enter a sentence to convert to camelCase ')

    # Pass string to converter function
    ccStrign = ccConverter(stringToCamelCase)

    print(ccStrign)

def ccConverter(string):

    #Split String into a list of the indivdual words based on space
    listOfWords = string.split()
    # Holds modified words for join statement
    listToJoin = []
    
    stringRejoined = ''
    # Use eneumerate because we care about the first word in the list.
    for index, word in enumerate(listOfWords):
        # First word we force into lowercase to adhere to camelCase
        if index == 0:
            word = word.lower()
        # Ever other word we capitalize
        else:
            word = word.capitalize()
        # Append words to list for join
        listToJoin.append(word)
    # Return our words joined with no space
    return stringRejoined.join(listToJoin)

main()