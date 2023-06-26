print("Hi, You can use this to calculate your GPA:")

points = {"S":10, "A":9, "B":8, "C":7, "D":6, "E":5, "F":0}

number_of_course = 0
total_points = 0
done = False

while not done:
    grade = input("type your grade:")
    if grade == "":
        done = True

    elif grade not in points:
        print("invalid grade")

    else:
        number_of_course +=1
        total_points += points[grade]

if number_of_course > 0:
    print(f"Total GPA is {total_points/number_of_course}")
