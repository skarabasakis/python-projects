lengthNum = int(input("Enter the length of numbers you are willing to use (i.e. 3): "))

nums = {}

for i in range(lengthNum):
    string = "Enter number " + str(i+1) + ": "
    num = int(input(string))
    nums["num{0}".format(i)] = num
    i += 1

sum = 0
for num in nums:
    sum += nums[num]

average = sum / lengthNum

print(f"\nThe average of the {lengthNum} numbers given is {average:.2f} .")
