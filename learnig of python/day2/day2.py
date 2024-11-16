#integer
age=16

#float
velue_of_pi=3.14

#string
name="prabhu"

#boolean
is_student=True

print(age)
print(velue_of_pi)
print(name)
print(is_student)

money="15"

age_str=str(age)#integer to string
pi_int=int(velue_of_pi)#float to integer
pi_str=str(velue_of_pi)#float to string
money_int=int(money)#string to integer
money_float=float(money)#string to float

print(age_str)
print(pi_int,pi_str)
print(money,money_int,money_float)

standerd=input("please enter your class ")#input method
print(standerd)

decimal=float(input("please inter your velue"))#input method with specipiy type
print(decimal)

integer=float(input("plese enter your number"))
number=int(integer)#extra step becuse float velu ko input leke direct wanhi se int me nahi badal sakte
print(number)

#strings ko jodna trick 1
print("my name is" + name + "and my age is" + str(age))

#trick 2 and best
print(f"my name is {name} and i have {money} moneydk")