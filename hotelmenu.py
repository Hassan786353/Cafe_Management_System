    # Here is the  menu 

menu ={
'Pasta' : 50,
'Burger' : 120,
'Coffee' : 200,
'Water' : 60,
'Shawarma' : 200,
'Biryani' : 170,
'Pizza' : 600
}
     
 
# Greetings
print("=========== Welcome to HASSY Resturant🍟🍔🍕☕ ==============")
print("Pasta : Rs 50\nBurger : Rs 120\nCoffee : Rs 200\nWater :Rs 60\nShawarma : Rs 200\nBiryani : Rs 170\nPizza : Rs 600 ")


order_total = 0

item_1 =input("Enter the name of the item you want to order : ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your ordered {item_1} has been added")

else:
    print(f"Your odered {item_1} is not available yet !")

another_order= input("Do you want to place another order ? (Yes/No) :")
if another_order == "Yes":

    item_2 = input("Enter the item name you want to order : ")
    if item_2 in menu:
     order_total += menu[item_2]
    else:
        print(f"Your odered {item_2} is not available yet !")
      
print(f"The total amount of items to pay  is {order_total}")    