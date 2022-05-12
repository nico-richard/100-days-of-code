def display_text(function):
    def wrapper(*args, **kwargs):
        print('----- this text is displayed by the decorator -----')
        print(function(*args, **kwargs))
        print('----- end of decorator -----')
    return wrapper

@display_text
def add(n1, n2):
    return n1 + n2

add(3, 4)