"This file is created by Sanjay Kumar(TheDoer)"
"Python 3.7 "
"Instagram = The__doer"
"For any queries DM me"
"    Recycle Machine   Cli"


print("Balance: Rs.0.0. Please select a product:\n"
      "1->Can\n"
      "2->Bottle\n"
      "3->Paper\n"
      "4->Stop\n")
val=0
cal1,cal2,cal3,m,n,o=0,0,0,0,0,0

def can():
    global val
    global cal1
    global m
    a=int(input("How many Can(s) do you have?: "))
    print('please place',a,'Can into Machine')
    for i in range(a):
        print("Can accepted")
    cal=(2.80 * a)
    print("You added",a," Can(s) for Rs.2.80 each. Amount added Rs.",round(cal,3))
    cal1 += cal
    val += cal
    m += a
    print()

def bottle():
    global val
    global cal2
    global n
    a=int(input("How many Bottle(s) do you have?: "))
    print('please place',a,'Bottle into Machine')
    for i in range(a):
        print("Bottle accepted")
    cal=(2.10 * a)
    print("You added",a," Bottle(s) for Rs.2.10  each. Amount added Rs.",round(cal,3))
    cal2 += cal
    val += cal
    n += a
    print()

def paper():
    global val
    global cal3
    global o
    a=int(input("How many paper(s) do you have?: "))
    print('please place',a,'paper into Machine')
    for i in range(a):
        print("paper accepted")
    cal=(4.20* a)
    print("You added",a," Paper(s) for Rs.4.20 each. Amount added Rs.",round(cal,3))
    cal3 += cal
    val += cal3
    o += a
    print()

def print_recp():
    print("----------Final list----------")
    print(m,"can(s)               Rs.",round(cal1,2))
    print(n,"Bottle(s)            Rs.",round(cal2,2))
    print(o,"paper(s)             Rs.",round(cal3,2))
    print()
    print("Number of item ->",m+n+o)
    print("Amount paid            Rs.",round(val,2))

def done():
    print()
    print("Press Enter button to exit the program ")


a=''
while(a!=4):
    print("Balance: Rs.", round(val, 2),)
    a = int(input("Enter your choice "))
    if a==1:
        can()

    elif a==2:
        bottle()

    elif a==3:
        paper()

    elif a==4:
        print_recp()
        done()

    else :
        print("Invalid option")
        print()


input()
