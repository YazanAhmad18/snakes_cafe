print("""

**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
""")

print("""
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
""")

print("""
** What would you like to order? **
""")

menu_food=["Wings","Cookies","Spring Rolls","Salmon","Steak","Meat Tornado","A Literal Garden","Ice Cream","Cake","Pie","Coffee","Tea","Unicorn Tears"]
menu_num_order=[0,0,0,0,0,0,0,0,0,0,0,0,0]
order=input('what is your order:')

def ordering(menu_num_order,order,menu_food):
 while order!="quit":
    
  if order in menu_food:
      menu_num_order[menu_food.index(order)]+=1
      print(f"{menu_num_order[menu_food.index(order)]} order of {order} have been added to your meal ")
  else:
      print("Sorry We Donot Have What You Order  Please Choose Something From The Menu ")
  order=input('do you want add more for your order if you donot want anything write quit ')


 for i in range(len(menu_num_order)):
    if menu_num_order[i]!=0:
     print (F"{menu_num_order[i]}:{menu_food[i]}")


ordering(menu_num_order,order,menu_food)


# i did it with the stretch goal

