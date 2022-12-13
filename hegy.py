file = open("hegy.txt","w")
hegy1 = int(input("Mekkora az első hegy magassága? "))
hegy2 = int(input("Mekkora az második hegy magassága? "))
file.write(str(hegy1))
file.write(str(hegy2))

if hegy1 > hegy2:
    print("Az első hegy magasabb.")
    file.write("Az első hegy magasabb.")
elif hegy2 > hegy1:
    print("A második hegy magasabb.")
    file.write("A második hegy magasabb.")
else:
    print("A hegyek magassága egyenlő.")
    file.write("A hegyek magassága egyenlő.")

def kilometer(szam):
    return szam/1000
def nagybetu(nev):
    return str.capitalize(str(nev))

magánhangzók =  ["a", "e", "i", "o", "u"]
def nevelo(nev):
    az = False
    for i in range(0,len(magánhangzók)):
        if magánhangzók[i] == str.lower(nev[0]):
            az = True
            break
    if az:
        return f"az {nev}"
    else:
        return f"a {nev}"

hegym1 = input("Adja megy egy hegymászó nevét. ")
hegyma1 = int(input("Adja megy az általa megmászott hegy magasságát. "))
hegym2 = input("Adja megy egy hegymászó nevét. ")
hegyma2 = int(input("Adja megy az általa megmászott hegy magasságát. "))
hegym3 = input("Adja megy egy hegymászó nevét. ")
hegyma3 = int(input("Adja megy az általa megmászott hegy magasságát. "))

hegyma1 = kilometer(hegyma1)
hegyma2 = kilometer(hegyma2)
hegyma3 = kilometer(hegyma3)

file.write(str(hegyma1))
file.write(str(hegyma2))
file.write(str(hegyma3))

print(nagybetu(hegym1))
print(nagybetu(hegym2))
print(nagybetu(hegym3))

file.write(nagybetu(hegym1))
file.write(nagybetu(hegym2))
file.write(nagybetu(hegym3))

file.write(nevelo(hegym1))
file.write(nevelo(hegym2))
file.write(nevelo(hegym3))