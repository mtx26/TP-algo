
def Book(book, number):
    book = book - (book * 0.4)

    result_first = book
    result_first = result_first + 3

    result_other = book
    result_other = result_other + 0.75
    result_other = result_other * (number - 1)

    result = result_first + result_other
    return(result)

book = Book(29.95, 60)
print(book)