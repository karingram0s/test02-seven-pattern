def formatPrint (myrange,filler,end) :
    for i in range(myrange) :
        print(filler, end='', flush=True)
    print(end)


def seven (userin) :

    if userin < 1 :
        print ('Invalid input. Number should be greater than 0')

    else :
        for i in range(userin) :
            if i == 0 :
                formatPrint(userin - 1,'*','X')
            elif i%2 != 0 :
                formatPrint(userin - i - 1,' ','*')
            elif i%2 == 0 and i != 0 :
                formatPrint(userin - i - 1,' ','X')


####---- main
print('This will print a seven pattern. Please enter a nonzero integer')
myinput = input('Ex. seven(7): ')
seven(int(myinput.split('(')[1].split(')')[0]))