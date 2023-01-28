
juices = input ("Please choose juice(1=Orange juice, 2=Apple juice, 3=Kivi juice):\n")
coins = input("Type of coin(a=1,b=2,c=3,d=4):\n")

juices = juices.split(",")
coins = coins.split(",")

# find total price of juice
total_price = 0
for j in juices:
    if j == '1':
        total_price += 13 #orange_price
    elif j == '2':
        total_price += 15 #apple_price
    elif j == '3':
        total_price += 22 #kiwi_price

# find cost that customer paid
pay = 0
for c in coins:
    if c == 'a':
        pay += 1  #coin1
    elif c == 'b':
        pay += 2  #coin2
    elif c == 'c':
        pay += 5  #coin5
    elif c == 'd':
        pay += 10  #coin10

# find number of each coin that customer get
return_price = pay - total_price
return_coin = [0,0,0,0] #[coin1, coin2, coin5, coin10]
while return_price > 0:
    if return_price >= 10: #get coin10
        return_coin[3] += 1 
        return_price -= 10
    elif return_price >= 5: #get coin5
        return_coin[2] += 1
        return_price -= 5
    elif return_price >= 2: #get coin2
        return_coin[1] += 1
        return_price -= 2
    elif return_price >= 1: #get coin1
        return_coin[0] += 1
        return_price -= 1

print("coin1: {},\ncoin2: {},\ncoin5: {},\ncoin10: {}".format(return_coin[0], return_coin[1], return_coin[2], return_coin[3]))


