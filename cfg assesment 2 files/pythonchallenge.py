def allocating_classes(total_students):
    max_class_size = 30
    min_classes = 2

    num_classes = min(max((total_students - 1) // max_class_size + 1, min_classes), total_students)

    students_per_class = total_students // num_classes
    remaining_students = total_students % num_classes

    if students_per_class > max_class_size:
        students_per_class = max_class_size
        remaining_students = 0

    allocation = {}
    for class_num in range(1, num_classes + 1):
        class_size = students_per_class + (1 if class_num <= remaining_students else 0)
        allocation[f"Class {class_num}"] = class_size

    print("Proposed Allocation:", num_classes, "classes")
    print(allocation)

#Example number of 39 students to check the function
allocating_classes(39)
