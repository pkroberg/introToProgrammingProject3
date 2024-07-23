'''

Project 3A

Program that converts feet to inches

Programmer: Oberg, Parker

Course: CSC1019-FBN

'''

# declarations and function
def feet_to_inches(feet):
    inches = feet * 12
    return inches

# input
if __name__ == "__main__":
    try:
        feet = float(input("Enter the number of feet: "))
        inches = feet_to_inches(feet)
# output
        print(f"{feet} feet is equal to {inches} inches.")

# Error handling
    except ValueError:
        print("Please enter a valid number.")
