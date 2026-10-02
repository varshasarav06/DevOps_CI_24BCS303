def calculate_grade(mark):
    if mark < 0 or mark > 100:
        return "Invalid"

    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


if __name__ == "__main__":
    mark = float(input("Enter your mark: "))
    print("Grade:", calculate_grade(mark))
