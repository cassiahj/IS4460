print(f"a: {21>13}")
print(f"b: {6==7}")
print(f"c: {12==45}")
print(f"d: {9==9}")

print("one is equal to three: ",int(1==3))
print("two is equal to 2: ",int(2==2))

myname="Cassiah"
myage=23
print(f"a: {67}")
print(f"b: {'helloooo'}")
print(f"c: {True}")
print(f"d: {myname}")
print(f"e: {myage}")

print((1-34+6),(2-3+1))
print((2*3/4),(5/7+8))

print(f"is 'cass'=='cassiah'? {'cass'=='cassiah'}")

x=55
x+=x 
print(x)

my_name='cassiah'
print("assignment: ",my_name)
print("equality: ",my_name=="cassiah")

print("comparison: ",'aa'<'r')
print("comparison: ",55>9)

r=5
c=7
print(f"comparison: {r} is greater than {c}" if r > c else "")
print(f"comparison: {r} is less than {c}" if r < c else "")
print(f"comparison: {r} is greater than or equal to {c}" if r >= c else "")
print(f"comparison: {r} is less than or equal to {c}" if r <= c else "")

bank_balance = 52
if bank_balance < 100:
  money = 1001
  bank_balance+=money
  print(bank_balance)

bank_balance = 52
if bank_balance > 100:
  money = 1001
  bank_balance+=money
  print(bank_balance)
else:
    print('balance is less than or equal to 100')


bank_balance = 520
savings = 230
if bank_balance < 100:
  money = 1001
  bank_balance+=money
  print(bank_balance)
elif bank_balance >203:
  savings += 32
  bank_balance -=32
  print(bank_balance)
else:
    print('balance is less than or equal to 100')

fuel = 2
print("Fill the tank now" if fuel <=1 else "there's enought fuel")

fuel = 8
while fuel > 1:
  #keep drinving
  print("There's enough fuel")
  fuel -= 1

books= ['redwall', 'mossflower', 'salamandastron']
for book in books:
  print(f"book: {book}")

for i in range(3):
  print(f"i = {i}")

for count in range(12):
  print(f"{count} times 13 is {count * 13}")
  if count== 5:
    break


for count in range(10):
  if count ==3:
    continue
  print(f"{count} times 11 is {count * 11}")    

