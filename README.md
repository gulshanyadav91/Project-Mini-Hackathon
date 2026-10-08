# 🎓 Project Mini Hackathon

A Python-based **Data Engineering Mini Hackathon Project** that integrates student marks, attendance, and scholarship rules to generate performance insights, identify scholarship-eligible students, store processed data in SQLite, create visualizations, and generate a management report.

## 🚀 Project Objective

Build a complete data pipeline:

**CSV + JSON → Data Integration → Transformation → Analysis → SQLite → Visualization → JSON Report**

The system processes:

* `students.csv` — student details and marks
* `attendance.csv` — attendance information
* `scholarships.json` — department-wise scholarship rules

---

## 🛠️ Tech Stack

* **Python**
* **Pandas** — data loading, merging and analysis
* **NumPy** — statistical calculations
* **SQLite** — data storage and SQL analysis
* **Matplotlib** — data visualization
* **JSON / CSV** — input and output data formats

---

## 📂 Project Structure

```text
Hackathon_Submission/
│
├── solution.py
├── students.csv
├── attendance.csv
├── scholarships.json
│
├── student_hackathon.db
├── report.json
├── department_performance.png
└── performance_distribution.png
```

---

## 🔄 Program Flow

```text
             ┌──────────────────┐
             │   students.csv   │
             └────────┬─────────┘
                      │
                      │
             ┌────────▼─────────┐
             │ attendance.csv   │
             └────────┬─────────┘
                      │
                      ▼
              ┌───────────────┐
              │ Data Loading  │
              │ & Inspection  │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ Merge Data    │
              │ student_id    │
              └───────┬───────┘
                      │
                      ▼
             ┌──────────────────┐
             │ scholarships.json│
             └────────┬─────────┘
                      │
                      ▼
              ┌───────────────┐
              │ Scholarship   │
              │ Eligibility   │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ Final Marks & │
              │ Performance   │
              └───────┬───────┘
                      │
              ┌───────┼───────────┐
              ▼       ▼           ▼
        ┌─────────┐ ┌────────┐ ┌──────────┐
        │ NumPy   │ │ Pandas │ │ SQLite   │
        │Analysis │ │Analytics│ │Database │
        └────┬────┘ └────┬───┘ └────┬─────┘
             │           │          │
             └───────────┼──────────┘
                         ▼
                 ┌──────────────┐
                 │ Visualization│
                 └──────┬───────┘
                        │
                        ▼
                ┌──────────────┐
                │ report.json  │
                └──────────────┘
```

---

## 📊 Main Features

### 1. Data Loading

Loads and inspects:

* Number of students
* Number of departments
* Unique cities
* First five student records
* Scholarship rules

### 2. Data Integration

Merges student and attendance data using:

```text
student_id
```

The final dataset contains:

```text
student_id
name
department
city
marks
attendance
```

### 3. Statistical Analysis

Using NumPy:

* Mean marks
* Median marks
* Standard deviation
* Maximum marks
* Minimum marks
* Mean attendance

### 4. Scholarship Eligibility

Scholarship rules are applied dynamically according to the student's department.

A student is eligible when:

```text
marks >= minimum_marks
AND
attendance >= minimum_attendance
```

Eligible students receive the department-specific bonus marks.

New columns:

```text
scholarship_status
final_marks
```

### 5. Performance Classification

Students are classified based on `final_marks`:

|    Marks | Performance       |
| -------: | ----------------- |
|      90+ | Outstanding       |
|    80–89 | Excellent         |
|    70–79 | Good              |
|    60–69 | Average           |
| Below 60 | Needs Improvement |

### 6. Pandas Analytics

The system calculates:

* Top 5 students
* Department-wise average final marks
* City-wise average final marks
* Best-performing department
* Highest-attendance student
* Scholarship-eligible student count
* Performance-category distribution

### 7. SQLite Database

Creates:

```text
student_hackathon.db
```

with the table:

```text
student_performance
```

SQL analysis includes:

```sql
SELECT *
FROM student_performance
WHERE scholarship_status = 'Eligible';
```

```sql
SELECT *
FROM student_performance
WHERE final_marks > 85;
```

```sql
SELECT department, AVG(final_marks)
FROM student_performance
GROUP BY department;
```

### 8. Visualizations

The project generates:

**Department Performance**

```text
department_performance.png
```

A bar chart showing department-wise average final marks.

**Performance Distribution**

```text
performance_distribution.png
```

A pie chart showing the distribution of performance categories.

### 9. Management Report

The system generates:

```text
report.json
```

containing important management-level metrics such as:

```json
{
    "total_students": 0,
    "average_marks": 0,
    "average_attendance": 0,
    "scholarship_students": 0,
    "top_student": "",
    "best_department": "",
    "highest_attendance_student": ""
}
```

All values are calculated dynamically from the input data.

---

## ▶️ How to Run

Make sure Python and the required libraries are installed.

```bash
pip install pandas numpy matplotlib
```

Then run:

```bash
python solution.py
```

The program will process the input files and generate the database, report, and charts automatically.

---

## 🎯 Key Data Engineering Concepts Demonstrated

* CSV data ingestion
* JSON data ingestion
* Data cleaning
* Data integration
* Data transformation
* Pandas DataFrame operations
* NumPy statistical analysis
* Conditional data processing
* Lambda / map / filter
* SQLite database creation
* SQL queries
* GROUP BY aggregation
* Data visualization
* JSON report generation
* End-to-end ETL pipeline

---

## 👨‍💻 Author

**Gulshan Yadav**

Python Data Engineering Mini Hackathon Project
