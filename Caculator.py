# Python code for the Grade 
# Calculator program in action 
  
# Creating a dictionary which  
# consists of the student name, 
# assignment result test results 
# and their respective lab results 
  
# 1. Esor's dictionary 
esor = { "name":"Esor David", 
         "assignment" : [80, 50, 40, 20], 
         "test" : [75, 75], 
         "lab" : [78.20, 77.20] 
       } 
         
# 2. Peter's dictionary 
peter = { "name":"Esor peter", 
          "assignment" : [82, 56, 44, 30], 
          "test" : [80, 80], 
          "lab" : [67.90, 78.72] 
        }
# Function calculates average  
def get_average(marks): 
    total_sum = sum(marks) 
    total_sum = float(total_sum) 
    return total_sum / len(marks) 
  
# Function calculates total average 
def calculate_total_average(students): 
    assignment = get_average(students["assignment"]) 
    test = get_average(students["test"]) 
    lab = get_average(students["lab"]) 
  
    # Return the result based 
    # on weightage supplied 
    # 10 % from assignments 
    # 70 % from test 
    # 20 % from lab-works 
    return (0.1 * assignment +
            0.7 * test + 0.2 * lab) 
  
  
# Calculate letter grade of each student 
def assign_letter_grade(score): 
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else : return "E"
  
# Function to calculate the total 
# average marks of the whole class 
def class_average_is(student_list): 
    result_list = [] 
  
    for student in student_list: 
        stud_avg = calculate_total_average(student) 
        result_list.append(stud_avg) 
        return get_average(result_list) 
  
# Student list consisting the 
# dictionary of all students 
students = [esor, peter,] 
  
# Iterate through the students list 
# and calculate their respective 
# average marks and letter grade 
for i in students : 
    print(i["name"]) 
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=") 
    print("Average marks of %s is : %s " %(i["name"], 
                         calculate_total_average(i))) 
                           
    print("Letter Grade of %s is : %s" %(i["name"], 
    assign_letter_grade(calculate_total_average(i)))) 
      
    print() 
  
  
# Calculate the average of whole class 
class_av = class_average_is(students) 
  
print( "Class Average is %s" %(class_av)) 
print("Letter Grade of the class is %s " 
        %(assign_letter_grade(class_av))) 
