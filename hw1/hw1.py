crypt = input("please enter your Ciphertext : ")

crypt = crypt.replace(" ","")
number = {}

for i in sorted(crypt):
  number[i] = crypt.count(i)
print(number)

