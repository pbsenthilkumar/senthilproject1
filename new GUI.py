def calculate_average(grades):
    total = sum(grades)
    average = total / len(grades)
    return average

def main():
    print("Welcome to the Grade Average Calculator!")
    
    num_grades = int(input("Enter the number of grades: "))
    grades = []
    
    for i in range(num_grades):
        grade = float(input(f"Enter grade {i + 1}: "))
        grades.append(grade)
    
    average = calculate_average(grades)
    
    print(f"The average of {num_grades} grades is: {average:.2f}")

if __name__ == "__main__":
    main()
