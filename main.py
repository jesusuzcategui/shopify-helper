import array
import os

shopList = [
    "kookapigradi.myshopify.com",
    "anatae-gradiweb.myshopify.com"
]

print("========== SHOPIFY SELECT SHOP ==========")
print("You should put a number of shop to make login on shopify. \nNow, choose a number: ")
print("=========================================\n")

for index, item in enumerate(shopList, start=1):
    print(index, "- ", item)

numberSelected = int(input("Enter a number: "))
shopSelected = shopList[numberSelected - 1]
commandTo = "shopify login --store " + shopSelected

print("Haz seleccionado: ", shopSelected)

os.system(commandTo)

#sum = x + y
#print(f"Addition of {x} and {y} is {sum}")