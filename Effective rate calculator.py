rate = 0
months = 0

while rate <= 0:
    rate = float(input("Enter the nominal rate: "))
    if rate <= 0:
        print("Time can't be less than or equal to zero")
while months <= 0:
    months = int(input("Enter the months: "))
    if months <= 0:
        print("Time can't be less than or equal to zero")
effective_rate = (pow((1 + rate / months), months) - 1)
print(effective_rate)