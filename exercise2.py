print("Maximum value for Current? Type below")
maximum = int(input())
for i in range(maximum):
    previous = i - 1
    sum = i + previous
    print("Current Number: " + str(i) + " Previous Number: " + str(previous) + " Sum: " + str(sum))
    i = int(i)
    previous = int(previous)
    sum = int(sum)