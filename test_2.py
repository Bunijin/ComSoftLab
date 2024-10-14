from time import sleep
menu = ['coffee','coco','tea']
price = [51,42,27]
def endLine():
    print('##################################')
    
def showMenu():
    print('###############Menu###############')
    print('#1.Coffee 2.CoCo 3.Tea ###########')
    endLine()
    
def insertCoin(itemPrice):
    acceptedCoins = [1,2,5,10]
    totalLeft = itemPrice
    while totalLeft > 0:
        try:
            coin = int(input(f'Please insert coin : {acceptedCoins}'))
            isValidValue = False
            for i in acceptedCoins:
                if i == coin:
                    isValidValue = True
            if isValidValue:
                totalLeft -= coin
                if totalLeft <= 0:
                    print(f'Enjoy {menu[items]}')
                    return totalLeft
                print(f'please insert: = {totalLeft}')
            else:
                print('invalid value')
        except ValueError:
            print('# please input number #')
            
def returnChange(changes):
    changes *= -1
    totalChangesLeft = changes
    changeCoin = []
    print(f'change : {changes}')
    amountCoin = [C10,C5,C2,C1]
    C10,C5,C2,C1 = 0,0,0,0
    while totalChangesLeft is not 0:
        if totalChangesLeft % 10 is not totalChangesLeft:
            C10 += 1
            totalChangesLeft -= 10
        elif totalChangesLeft % 5 is not totalChangesLeft:
            C5 += 1
            totalChangesLeft -= 5
        elif totalChangesLeft % 2 is not totalChangesLeft:
            C2 += 1
            totalChangesLeft -= 2
        elif totalChangesLeft % 1 is not totalChangesLeft:
            C1 += 1
            totalChangesLeft -= 1
    for i in amountCoin:
        print(f'changes: X amount: {i}')
        
    
        
    
showMenu()
items = int(input('Choose Menu: [1-3]')) - 1
print(f'Cost = {price[items]}')
endLine()
changes = insertCoin(price[items])
returnChange(changes)
endLine()

