name = []
address = []
mobile = []
n = input("Enter name: ");
name.append(n)
a = input("Enter address: ")
address.append(a)
m = input("Enter mobile: ")
mobile.append(m)

products = ["Milk 500ml","Milk 1l","Curd 250ml","Cold Drink 750ml","Lays","Bread","Eggs","Parle Biscuits"]
prices = [20,20,25,38,25,15,150,20]
print("Products we have: ")
k=1
for i,j in zip(products,prices):
    print(k,".",i,j)
    k = k+1
sum =0
num = int(input("How many products you want: "))
for i in range (0,num):
    x = int(input("Enter serial Number: "))
    sum = sum + prices[x-1]
print(n)
print(a)
print(m)
print("Total Bill: ",sum)
input("Press any key to exit")