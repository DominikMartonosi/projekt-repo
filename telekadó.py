def red(t,w,l):
    if l<=25 or w<=15:
        t = 0.8 * t
    return t

tax = int(input("Kérem a kedvezmény nélküli adót: "))
length = int(input("Kérem a telek hosszát: "))
width = int(input("Kérem a telek szélességét: "))
print("A kedvezményes adó: ", red(tax,width,length))