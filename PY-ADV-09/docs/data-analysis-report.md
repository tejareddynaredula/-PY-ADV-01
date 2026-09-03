# PY-ADV-09 — Python Data Processing & AI/ML Foundation

## 1. Objective

The objective of this task was to strengthen Python data-processing fundamentals using NumPy and Pandas and implement a basic Employee Data Analysis System.

## 2. Technologies Used

- Python
- NumPy
- Pandas
- Jupyter Notebook
- CSV

## 3. Tasks Completed

All 18 tasks were implemented and executed in Jupyter Notebook.

### NumPy

1. Installed and verified NumPy
2. Created NumPy arrays
3. Checked array dimensions
4. Performed mathematical operations
5. Used indexing and slicing
6. Demonstrated broadcasting

### Pandas

7. Installed and verified Pandas
8. Created Pandas DataFrames
9. Read CSV files
10. Filtered DataFrames
11. Sorted data
12. Handled missing values
13. Removed duplicate records
14. Grouped data
15. Aggregated data
16. Merged DataFrames
17. Generated basic statistics
18. Created a data-cleaning pipeline

## 4. Employee Dataset

The original `employees.csv` file contained 6 employee records with the following fields:

- Name
- Age
- Department
- Salary

## 5. Data Cleaning

The dataset contained:

- 1 missing age
- 1 missing department
- 1 duplicate record

The missing age was replaced with the mean age.

The missing department was replaced with `Unknown`.

The duplicate record was removed.

After cleaning, the dataset contained 5 records.

## 6. Data Analysis

Employees with a salary greater than 50,000 were identified using DataFrame filtering.

The employee data was grouped by department and salary statistics were calculated.

### Department Salary Summary

| Department | Employees | Average Salary |
|---|---:|---:|
| Finance | 1 | 60000 |
| HR | 1 | 45000 |
| IT | 2 | 52500 |
| Unknown | 1 | 65000 |

Basic statistical information was also generated using Pandas `describe()`.

## 7. DataFrame Merge

A separate manager DataFrame was created and merged with the employee DataFrame using the `department` column.

This demonstrated how related datasets can be combined using Pandas.

## 8. Output Files

The following project files were created:

- `data/employees.csv` — Original employee dataset
- `data/employees_clean.csv` — Cleaned employee dataset
- `notebooks/employee_analysis.ipynb` — Jupyter Notebook containing the implementations
- `scripts/employee_analysis.py` — Python analysis script
- `docs/data-analysis-report.md` — Data analysis report

## 9. Conclusion

The Employee Data Analysis System successfully demonstrates fundamental NumPy and Pandas operations, including array processing, DataFrame creation, CSV handling, filtering, sorting, missing-value handling, duplicate removal, grouping, aggregation, merging, statistical analysis, and data cleaning.

The cleaned employee dataset was successfully generated as `employees_clean.csv`.