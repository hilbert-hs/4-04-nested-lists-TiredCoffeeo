# shopping list
shopping_cart = [
  ["tooth paste", "q-tips", "milk"],
  ["milk", "candy", "apples"],
  ["planner", "pencils", "q-tips"]
]


# user inputs
action = input("What do you want to do?")
update = input("What list do you want to update")


# functions
def update_list(shppoing_list):
    row = int(input("What round do you want to update?"))
    coloum = int(input("What item in the list do you want to update?"))
    new_item = int(input("What is your new item?"))
    shppoing_list[row][coloum] -1