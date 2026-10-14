product = 1

base = int(input("what is the base of your problem?"))
exponent = int(input("what is the exponent of your problem?"))

for l in range(exponent):
    product  *= base


print (product)