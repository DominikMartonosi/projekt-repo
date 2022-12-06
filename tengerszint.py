def szint(s):
    if s > 200:
        print('alföld')
    elif s <= 200 and s > 500:
        print('dombság')
    elif s <= 500 and s > 1000:
        print('középhegység')
    else:
        print('hegység')
    
hely=None
while hely == ' ':   
    hely=input('Írj be egy helyet: ')
    if hely == "":
        tengerszint=int(input('És írd a tengerszintjét: '))
    else:
        break

print(f"A tengerszint: {szint(tengerszint)},{hely}-ban/ben")