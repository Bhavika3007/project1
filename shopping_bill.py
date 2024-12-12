sal=float(input('enter salary '))
b1=float(input('enter 1st bill '))
b2=float(input('enter 2nd bill '))
b3=float(input('enter 3rd bill '))
shoppingbill=b1+b2+b3
print(f'Total shopping bill: {shoppingbill}')
per=(shoppingbill/sal)*100
print(f'Total amount spent: {per:.2f}%')