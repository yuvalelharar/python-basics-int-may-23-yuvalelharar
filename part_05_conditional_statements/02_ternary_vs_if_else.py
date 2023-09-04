#option1

coffe_cost = 15
amount = int(input("Enter your amount: "))
if amount >= coffe_cost :
    print("Take your coffee! ")
else:
    print("Sorry, not enough money..")

#option2

print("Take your coffee! ") if amount >= coffe_cost else print("Sorry, not enough money..")

age = int(input("Enter your age: "))

print("You are adult ") if age >= 18 else print("you are yoo young")

result = f"your age is {age}, you are adult!" if age >= 18 else f"your age is {age} , you are too young"
print(result)
