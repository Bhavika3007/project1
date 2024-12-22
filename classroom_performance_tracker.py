def calculate_average(marks):
    return sum(marks) / len(marks)

def calculate_all_averages(students):
    averages = {}
    for student, marks in students.items():
        averages[student] = calculate_average(marks)
    return averages

def find_top_performer(averages):
    top_student = max(averages, key=averages.get)
    return top_student

students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}

averages = calculate_all_averages(students)

top_performer = find_top_performer(averages)

print("Average Marks:", averages)
print("Top Performer:", top_performer)
