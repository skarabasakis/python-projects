# Simple program for finding the average number of a series of numbers given by the user

if __name__ == "__main__":
    def findAverage():
        try:
            lengthNum = int(input("Enter the length of numbers you are willing to use (i.e. 3): ")) # Get the length of numbers the user wishes to use
            
            nums = {} # Create a dictionary to store the numbers

            for i in range(lengthNum):
                string = "Enter number " + str(i+1) + ": "
                num = int(input(string)) # Get each number by the user
                nums["num{0}".format(i)] = num # Store each number to the "nums" dictionary
                i += 1

            sum = 0
            for num in nums:
                sum += nums[num] # Find the sum of each number in the "nums" dictionary

            average = sum / lengthNum # (num1 + num2 ... ) / the length of all the numbers (lengthNum)

            print(f"\nThe average of the {lengthNum} numbers given is {average:.2f} .")  # Use ':.2f' To round the result to 2 numbers after the decimal point.

        except ValueError:
            print("That was not an integer.")
    
    findAverage() 
