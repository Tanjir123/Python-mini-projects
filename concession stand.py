menu={
    "pizza":400,
    "jhalmuri":30,
    "popcorn":50,
    "coke":50,
    "cake":100,
    "nuts":30

}
total=0
cart=[]
for key,value in menu.items():
    print(f"{key}:{value}")
print("-------------")
while True:
    food=input("Enter the foods you want to buy and q to quit: ").lower()
    if food.lower()=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Invalid item .please choose from the menu")
print("---------")
for i in cart:
    total+=menu.get(i)
print(f"Total:{total}Tk")

