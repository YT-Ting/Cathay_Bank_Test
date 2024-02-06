def find_last_person_position(n):
    people = list(range(1, n + 1))

    count_index = 0

    while len(people) > 1:
        count_index = (count_index + 2) % len(people)
        people.pop(count_index)

    return people[0]



n = int(input("請輸入人數 (0-100): "))

if 0 <= n <= 100:
    result = find_last_person_position(n)
    print("第", result, "順位。")
else:
    print("請輸入人數(0-100)。")
