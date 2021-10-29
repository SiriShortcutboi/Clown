#Holden Anderson
#10-21
#BurgerCastle Assignment

validOrders = ("burger","fries","salad","soda","milkshake")
itemDescriptions = ("Half-pound burger","Large fries","Side salad", "Diet root beer", "Chocolate shake") 
order = []

#welcome
print("Welcome to Burger Castle")
#print menu items
print("Menu:" + validOrders)
#tell them to enter specific foods you have
print("Please enter each item in your order. Press 'Enter' or type 'quit' on an empty line when done.")

#until the order is done
while orderDone != True:
    # get the individual food items ordered 
    orderValue = input("Enter item:")
    #if the input is a carriage return or the phrase "quit", the order is set to done
    if orderValue == "" or orderValue =="quit":
        orderDone = True
    else:
        #if the individual food order matches a valid order, append the food to the order,
        if orderValue in validOrders:
            order.append(orderValue)
        else:
            #tell them we dont have the thing they said
            print("Sorry, we don't sell" + orderValue)
         # return order so we can do something with it
        return order

for item in order:
    index = index(validOrders)
    description = itemDescriptions[index]
    print(description)
    
print("Thanks for visiting Burger Castle!")

