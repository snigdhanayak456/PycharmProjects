# Write your code here

water = int(input('Write how many ml of water the coffee machine has:'))
milk = int(input('Write how many ml of milk the coffee machine has:'))
beens = int(input('Write how many grams of coffee beans the coffee machine has:'))
need = int(input('Write how many cups of coffee you will need:'))
print('For', need,'cups of coffee you will need:')
print(need * 200,'ml of water,')
print(need * 50,'ml of milk,')
print('and', need * 15,'g of coffee beans.')
number: int = min([water // 200, milk // 50, beens // 15])
if number == need:
    print('Yes, I can make that amount of coffee')
elif number > need:
    print('Yes, I can make that amount of coffee (and even', number - need,'more than that)')
elif number < need:
    print('No, I can make only', number, 'cups of coffee')