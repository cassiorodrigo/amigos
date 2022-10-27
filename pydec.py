from string import ascii_lowercase


def vowals(func):
    def wrapper():
        for letter in func():
            if letter in 'aeiou':
                yield letter
            else:
                yield ''
    return wrapper


@vowals
def aphabet():
    return ascii_lowercase

if __name__ == "__main__":
    res = aphabet()
    for i in res:
        print(i) # , end='')
    print('')
    
