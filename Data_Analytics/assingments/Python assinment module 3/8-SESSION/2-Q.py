steps = [6500, 8200, 9800, 12000, 10000, 9000, 15000]
i = 0
while i < len(steps):
    print(steps[i])
    i = i + 1
    if steps[i]>10000:
        print("You have reached your goal for the day!",i+1)
        break
