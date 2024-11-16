# if elif and else
age=int(input("please enter your age"))

if age >= 18:#if condition: Yeh block tab execute hoga jab condition True ho
    print("you are eligbel to drive and vote")
elif age >= 16:#elif another_condition: Yeh tab chalega jab pehli condition False ho aur yeh condition True ho
    print("your have to wait 2 years more")
else:#else: Yeh block tab chalega agar upar ki koi bhi condition True nahi hai
    print("you are under age")

