print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

combinedname = lower_name1 + lower_name2

t = combinedname.count("t")
r = combinedname.count("r")
u = combinedname.count("u")
e = combinedname.count("e")
l = combinedname.count("l")
o = combinedname.count("o")
v = combinedname.count("v")
e = combinedname.count("e")

truelovecount = t+r+u+e+l+o+v+e

lovescore = truelovecount * 10

print(f"Your love score is {lovescore}." )
if lovescore >= 50:
  print(" You are a great match!")
elif lovescore < 50 and lovescore > 10:
  print(" You are an average match and will likely break up within 1 year.")
else:
    print("You are not a match...")
