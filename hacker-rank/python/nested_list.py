# Given the names and grades for each student in a class of  students, store them in a nested list and print the
# name(s) of any student(s) having the second lowest grade.
#
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each
# name on a new line.

if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scores = [student[1] for student in students]
    uniq_ordered_scores = sorted(set(scores))
    second_score = uniq_ordered_scores[1]

    second_score_students = [student for student in students if student[1] == second_score]
    ordered_second_score_students = sorted(second_score_students, key=lambda x: x[0])

    for student in ordered_second_score_students:
        print(student[0])
