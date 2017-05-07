a = 10
b = 20
c = 30
d = 40

def disp(a,*b):
    print(a)
    print(b)
    for i in b:
        print(i)

disp(a,b,c,d)
