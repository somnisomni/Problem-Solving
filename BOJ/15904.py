First_U = False
Second_C = False
Third_P = False
Fourth_C = False

Second_C_Temp = False
for c in input():
    if c == 'U': First_U = True
    
    if First_U:
        if c == 'C':
            if not Third_P:
                Second_C_Temp = True
            else:
                Fourth_C = True
        elif c == 'P':
            if Second_C_Temp:
                Second_C = True
                Third_P = True


if First_U and Second_C and Third_P and Fourth_C:
    print("I love UCPC")
else:
    print("I hate UCPC")