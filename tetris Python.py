for i in range(2, 80, 10):
    print(i, end = " ")
for k in range(100, 5, -5):
    print(k, end = " ")
lines = int(input("how many lines did you clear: "))
if lines <= 100 :
    print("Novice")
elif lines <= 200 :
    print("Intermediate")
elif lines <= 300 :
    print("Advanced")
else:
    print("Expert")
