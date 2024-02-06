def fix_grades(wrong_grades):
    correct_grades = [53, 64, 75, 19, 92]
    stack = []

    for correct_score in reversed(correct_grades):
        stack.append(correct_score)

    fixed_grades = []
    for _ in wrong_grades:
        fixed_grades.append(stack.pop())

    return fixed_grades

wrong_grades = [35, 46, 57, 91, 29]

fixed_grades = fix_grades(wrong_grades)

print("Fixed grades:", fixed_grades)
