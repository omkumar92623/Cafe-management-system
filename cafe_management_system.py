print("Welcome to the biggest cafe in the city named D'manoj")
print("Pizza : 120")
print("Burger: 80")
print("Cold coffee : 150")
print("coffee : 100")
print("Cold drinks : 50")
print("Pasta: 180\n")

prices = {
    "pizza": 120,
    "burger": 80,
    "cold coffee": 150,
    "coffee": 100,
    "cold drinks": 50,
    "pasta": 180
}

choice=input("Hey! Dear customer! What do you want to eat: ")

if choice in prices:
    total_price = prices[choice]
    another_choice= input("Anything else you need: ").lower()
    if another_choice == "yes":
        another_item=input("What do you want to add: ").lower()

        if another_item in prices:
            total_price += prices[another_item]
            print(f"Your total price of {choice} and {another_item} is {total_price}")

        else:
            print(f"Sorry, we don't have {another_item}. Your bill for {choice} is {total_price}")
    else:
        print(f"Your bill for {choice} is {total_price}")
else:
    print(f"Sorry, we don't have {choice} on the menu.")

print("Thank you for visiting our cafe!")