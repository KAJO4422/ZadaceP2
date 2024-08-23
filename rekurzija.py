def unazad(string):
    if len(string) == 0:
        return
    else:
        print(string[-1], end='')
        unazad(string[:-1])

str_=input("Unesi string:  ")
unazad(str_)
