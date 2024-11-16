age = int(input("enter your age"))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

marks=int(input("please enter your marks"))
if marks >= 50:
    if marks >= 75:
        if marks >= 90:
            print("A Grade")
        else:
            print("B Grade")
    else:
        print("C Grade")
else:
    print("Fail")
age = 17
if age > 18:
    print("Adult")
else:
    print("Minor")

number=[50,40,30,20,10]
total=0
for num in number:
    total+=num
print(total)
