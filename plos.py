print("profit and loss")
bp=int(input("Enter the buying price:"))
sp=int(input("Enter the selling price:"))
if bp>sp:
    print("you have incured a loss of", bp-sp)
else:
    print("you have made a profit of", sp-bp)