#betu kodja: ord()
print(ord('A'))


print(chr(50))


b=input("a betu: ")
print(chr(ord(b)+1), ", ami: ", ord(b)+1)

s1=input('az elso mondat: ')
print('hossza: ', len(s1))
s2=input('a masodik mondat: ')
print('hossza: ', len(s2))

if len(s1)>len(s2):
    print(s1 , " - a hosszabb")
#elif len(s1)<len(s2):
#    print(s2 , " - a hosszabb")
#else:
#    print("egyenloek")
else:
    if len(s1)==len(s2):
        print("egyenloek")
    else:
        print(s2 , " - a hosszabb")

if s1[-1]==".":
    print("kijelento")
elif s1[-1]=="!":
    print("felkialto, felszolito vagy ohaj")
elif s1[-1]=="?":
    print("kerdo")
else:
    print("nincs irasjel")

#lehet vagy range(1,2,12) vagy range(12), pythonban igy kell mas szamtol indexelni, mint 0
for i in range(6,12,3):
    print(i,". sorry babe")