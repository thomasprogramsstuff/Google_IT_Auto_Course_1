# 6 Write a Python script that outputs "Automating with Python is fun!" to the screen.
print("Automating with Python is fun!")

# 7 Fill in the blanks so that the code prints "Yellow is the color of sunshine".
color = "Yellow"
thing = "sunshine"
print(color + " is the color of " + thing)

#8 Keeping in mind there are 86400 seconds per day, write a program that calculates how many seconds there are in a week, 
#if a week is 7 days.  Print the result on the screen.
seconds = 86400
days_per_week = 7
seconds_per_week = seconds * days_per_week
print(seconds_per_week)

#9 Use Python to calculate how many different passwords can be formed with 6 lower case English letters.  
#For a 1 letter password, there would be 26 possibilities.  
#For a 2 letter password, each letter is independent of the other, so there would be 26 times 26 possibilities.  
#Using this information, print the amount of possible passwords that can be formed with 6 letters.
letters_in_alphabet = 26
letters_per_pw = 6
pw_possibilities = letters_in_alphabet**(letters_per_pw)
print(pw_possibilities)

#Most hard drives are divided into sectors of 512 bytes each.  
#Our disk has a size of 16 GB. Fill in the blank to calculate how many sectors the disk has.
#Note: Your result should be in the format of just a number, not a sentence.
disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = disk_size/sector_size

print(sector_amount)
