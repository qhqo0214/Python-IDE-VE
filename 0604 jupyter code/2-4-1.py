## Calculate average of grades.

# TODO: float() 함수를 적당한 함수로 대체
grades = []   # Create the variable grades and assign it the empty list.
num = eval(input("Enter the first grade: "))
grades.append(num)
num = eval(input("Enter the second grade: "))
grades.append(num)
num = eval(input("Enter the third grade: "))
grades.append(num)            
num = eval(input("Enter the fourth grade: "))
grades.append(num)    
num = eval(input("Enter the fifth grade: "))
grades.append(num)

## 2개의 최소 값 삭제
minimumGrade = min(grades)
grades.remove(minimumGrade)
minimumGrade = min(grades)
grades.remove(minimumGrade)

#평균 계산 출력
average = sum(grades) / len(grades)
print("Average Grade: {0:.2f}".format(average))

print("Alt + Shift + E")

