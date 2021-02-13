''' 
    Teachers in most school districts are paid on a schedule 
    that provides a salary based on their number of years of teaching experience. 
    For example, a beginning teacher in the Lexington School District might be paid $30,000 the first year. 
    For each year of experience after the first year, up to 10 years, the teacher receives a 2% increase over the preceding value. 
    Write a program that displays a salary schedule, in tabular format, for teachers in school district. 
    The inputs are starting salary, the percentage increase and the number of years in the schedule. 
    Each row in the schedule should contain the year number and the salary for that year. 
'''

salary = int(input("Enter the starting salary "))
years = int(input("Enter number of years "))
increment = int(input("Enter the percentage increase in salary "))

print("\nYear", "\tSalary")

for i in range(years):
    print(i + 1, "\t", int(salary))
    salary += salary * increment / 100