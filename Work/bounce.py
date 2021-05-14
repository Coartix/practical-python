# bounce.py
#
# Exercise 1.5


bounce_height=100
for i in range(1,11):
    bounce_height=round(3/5 * bounce_height,4)
    print(i,bounce_height, sep=' ')