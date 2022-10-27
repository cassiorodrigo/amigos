

def spelling(name:str):
    for letter in name:
        yield letter

if __name__ == "__main__":
    res = spelling("Cassio")
    print(res)
    print(res)
    # print(res) # this is a generator


    #for index, letter in enumerate(res):
    #    print(f'{index=}    {letter:^15}')



