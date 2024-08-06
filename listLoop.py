numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i % 5 == 0:
        if i <=150:
            print(i)
        elif i > 150 and  i <=500:
            continue
        else:
            break
