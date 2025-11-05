# Name: Aarav Chauhan
# Date: 4 November 2025
# Title: GradeBook Analyzer



# Project setup and initialisation

print("\nWelcome to GradeBook Analyzer\n")
print("1. Start Analysis")
print("2. Exit\n")


# Data entry


choice = input("Enter your choice (1 or 2): ")

while choice == '1':
    while True:                                                  # To avoid invalid number of students
        try:
            num_students = int(input("\nEnter number of students: "))
            if num_students <= 0:
                print("\nPlease enter a positive number.")
                continue
            break
        except ValueError:
            print("\nInvalid input. Please enter a number.")

    marks = {}
    for _ in range(num_students):
        while True:                                             # To avoid invalid names and marks                              
            name = input("\nEnter student name: ").strip()
            if name == "":
                print("\nName cannot be empty.")
                continue
            if not name.isalpha():
                print("\nName must contain only letters.")
                continue
            break
        while True:
            try:
                score = int(input("Enter marks: "))
                if score < 0 or score > 100:
                    print("\nMarks should be between 0 and 100.")
                    continue
                break
            except ValueError:
                print("\nInvalid input. Please enter numeric marks.")
        marks[name] = score



    # Statistical Analysis Functions



    def calculate_average(marks_dict):
        return sum(marks_dict.values()) / len(marks_dict)

    def calculate_median(marks_dict):
        scores = sorted(marks_dict.values())
        n = len(scores)
        if n % 2 == 0:
            return (scores[n//2 - 1] + scores[n//2]) / 2
        else:
            return scores[n//2]

    def find_max_score(marks_dict):
        return max(marks_dict.values())

    def find_min_score(marks_dict):
        return min(marks_dict.values())

    print("\n\n--- Statistics ---")
    print(f"Average Marks: {calculate_average(marks):.2f}")
    print(f"Median Marks: {calculate_median(marks):.2f}")
    print(f"Highest Marks: {find_max_score(marks)}")
    print(f"Lowest Marks: {find_min_score(marks)}")



    # Grade Assignment

    grades = {}
    for name, score in marks.items():
        if score >= 90:
            grades[name] = 'A'
        elif score >= 70:
            grades[name] = 'B'
        elif score >= 50:
            grades[name] = 'C'
        elif score >= 33:
            grades[name] = 'D'
        else:
            grades[name] = 'F'



    # Count grade distribution

    grade_count = {'A':0, 'B':0, 'C':0, 'D':0, 'F':0}
    for grade in grades.values():
        grade_count[grade] += 1

    print("\n\n--- Grade Summary ---")
    for grade in grade_count:
        print(f"{grade}: {grade_count[grade]} student(s)")


    # Pass/Fail Filter


    passed_students = [name for name, m in marks.items() if m >= 33]
    failed_students = [name for name, m in marks.items() if m < 33]

    print("\n\n--- Pass/Fail Summary ---")
    print(f"Passed Students ({len(passed_students)}): {passed_students}")
    print(f"Failed Students ({len(failed_students)}): {failed_students}")


    # Results Table


    print("\n\n---- Results Table ----")
    print("Name\tMarks\tGrade")
    print("--------------------------")
    for name in marks:
        print(f"{name}\t{marks[name]}\t{grades[name]}")

    print("\n1. Re-run Analysis")
    print("2. Exit")
    choice = input("\nEnter your choice (1 or 2): ")

print("\n\nThank you for using GradeBook Analyzer!\n\n\n\n")