target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
cnumber = 0
if target <= 1000:
    for num in range (1, target + 1):
        if num % 2 == 0:
            cnumber += num
    print(cnumber)
else:
    print("Your number is out of range")
