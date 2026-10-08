import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np
import sqlite3


# print(scholarship)
# print(attendance)
# print(students)

try:
    with open("scholarships.json","r") as file:
        data = json.load(file)
        scholarship = pd.DataFrame(data)

    attendance = pd.read_csv("attendance.csv")
    students = pd.read_csv("students.csv")
    attendance_df = pd.DataFrame(attendance)
    students_df = pd.DataFrame(students)
except Exception as e:
    print(f"Error in loading the data {e}")



# - Number of students
# - Number of departments
# - Unique cities
# - First five student records
# - Scholarship rules

print("\nNumber of students are  :  ", students.shape[0])
print("\nNumber of departments are : ", students_df['department'].nunique())
print("\nUnique cities are : ", students_df['city'].nunique())
print("\nFirst five records are :" )
print(students.head())


student_info = pd.merge(students_df,attendance_df,on="student_id")

if(len(students_df) == len(student_info)):
    print("\nData has no missing records ")
else :
    print("\nData has missing records. Please correct it ")
# print() # no records are missing as you are seein it


# Using NumPy, calculate:

# - Mean marks
# - Median marks
# - Standard deviation of marks
# - Maximum marks
# - Minimum marks
# - Mean attendance


# print(scholarship)
# print(student_info)

print("\nMean marks  : ", round(np.mean(student_info['marks']),2))
print("\nMean Attendance",round(np.mean(student_info['attendance']),2))
print("\nMedian marks : ",round(np.median(student_info['marks']),2))
print("\nStandard deviation of marks : ", round(np.std(student_info['marks']),2))
print("\nMaximum marks : ",np.max(student_info['marks']))
print("\nMinimum marks : ",np.min(student_info['marks']))

# print(students_df[])

def find_data(scholarship,student_info):
    if student_info['department'] == "CSE":
        if (student_info['marks']>=scholarship['minimum_marks'].iloc[0]) & (student_info['attendance']>=scholarship['minimum_attendance'].iloc[0]) :
            return "Eligible"
        else :
            return "Not Eligible"
    elif student_info['department'] == "IT":
        if (student_info['marks']>=scholarship['minimum_marks'].iloc[0]) & (student_info['attendance']>=scholarship['minimum_attendance'].iloc[0]) :
            return "Eligible"
        else :
            return"Not Eligible"
    elif student_info['department'] == "ECE":
        if (student_info['marks']>=scholarship['minimum_marks'].iloc[0]) & (student_info['attendance']>=scholarship['minimum_attendance'].iloc[0]) :
            return "Eligible"
        else :
            return "Not Eligible"

# find_data(scholarship,student_info)

student_info['scholar_status']= student_info.apply(
    lambda row : find_data(scholarship,row),
    axis=1
)


def add_bonus(student_info):
    if student_info['scholar_status'] == "Eligible":
        return student_info['marks'] + 5
    else :
        return student_info['marks']

student_info['final_marks'] = student_info.apply(
    lambda row : add_bonus(row),
    axis=1
)


def performance(student_info):
    if student_info['final_marks'] >= 90:
        return "Outstanding"
    elif student_info['final_marks'] >= 80 :
        return  "Excellent"
    elif student_info['final_marks'] >= 70:
        return "Good"
    elif student_info['final_marks'] >= 60:
        return "Average"
    else :
        return "Needs Improvement"

student_info['performance'] = student_info.apply(
    lambda row : performance(row),
    axis=1
)


# 1. Top 5 students according to final marks.
# 2. Department-wise average final marks.
# 3. City-wise average final marks.
# 4. Department with the highest average final marks.
# 5. Student with the highest attendance.
# 6. Number of scholarship-eligible students.
# 7. Number of students in each performance category.

print("\nTop 5 students according to final marks. >> ")
print(student_info.sort_values('final_marks',ascending=False).head())

print("\nDepartment-wise average final marks. >> ")
print(round(student_info.groupby('department')['final_marks'].mean(),2))

print("\nCity-wise average final marks. >> ")
print(round(student_info.groupby('city')['final_marks'].mean(),2))

print("\n Student with the highest attendance. >> ")
print(student_info[student_info['attendance'] == np.max(student_info['attendance']) ])

print("\nDepartment with the highest average final marks. >>")
# print(student_info[student_info['attendance'] == np.max(student_info['attendance']) ]['department'])
result = student_info.groupby('department')['final_marks'].mean()

print(result.idxmax())

print("\nNumber of scholarship-eligible students. >>")
print(student_info[student_info['scholar_status'] == "Eligible"]['student_id'].count())

print("\nNumber of students in each performance category. >> ")
print(student_info.groupby('performance')['student_id'].count())


connection = sqlite3.connect("student_hackathon.db")

student_info.to_sql(
    "student_performance",
    connection,
    if_exists="replace",
    index=False
)


def run_query(query):
    cursor = connection.execute(query)
    datas = cursor.fetchall()
    for data in datas:
        print(data)


query = """ select * from student_performance """
run_query(query)
print("\n")
query = """ select name,department,scholar_status  from student_performance  """
run_query(query)
print("\n")
query = """ select * from student_performance where final_marks>85"""
run_query(query)
print("\n")
query = """select department, round(avg(final_marks),2) from student_performance group by department """
run_query(query)
print("\n")
# print(student_info.columns)


# x = student_info["department"]
# y = round(student_info.groupby('department')['final_marks'].mean(),2)
# print(y)

result = student_info.groupby('department')['final_marks'].mean()
x = result.index
y = result.values
plt.bar(x,y)
plt.xlabel("Department")
plt.ylabel("Average Final Marks")
plt.title("Department VS Average value", fontsize=16)
plt.savefig("department_performance.png")
plt.show()


# # Performance Category Distribution


performance = student_info.groupby('performance')['student_id'].count()
print(performance)

plt.pie(
    performance.values,
    labels=performance.index
    
    )
plt.title("Performance Category Distribution", fontsize=16)
plt.savefig("performance_distribution.png")
plt.show()


# The JSON file must contain at least:

# ```json
# {
#     "total_students": 0,
#     "average_marks": 0,
#     "average_attendance": 0,
#     "scholarship_students": 0,
#     "top_student": "",
#     "best_department": "",
#     "highest_attendance_student": ""
# }


print("\nReport is ready ... ")
report = {
    "total_students": student_info.shape[0],
    "average_marks": float(student_info['marks'].mean().round(2)),
    "average_attendance": float(round(student_info['attendance'].mean(),2)),
    "scholarship_students": int(student_info[student_info['scholar_status'] == "Eligible"]['student_id'].count()),
    # "top_student": student_info.sort_values('marks',ascending=False)['name'].iloc[0],
    "top_student" : student_info.loc[student_info['final_marks'].idxmax(),"name"],
    # "best_department": student_info[student_info['marks']  == np.max(student_info['marks'])]['department'].values,
    "best_department" :  student_info.groupby("department")["final_marks"].mean().idxmax(),
    # "highest_attendance_student": student_info[student_info['attendance']==np.max(student_info['attendance'])]["name"]
    "highest_attendance_student": student_info.loc[student_info['attendance'].idxmax(),'name']
}

try:
    with open("report.json","w") as file:
        json.dump(report,file,indent=4)
except Exception as e:
    print("Error in report.json file {e}")

print(report)