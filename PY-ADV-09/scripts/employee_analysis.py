import pandas as pd

input_file = r".\PY-ADV-09\data\employees.csv"
output_file = r".\PY-ADV-09\data\employees_clean.csv"

# Read CSV
df = pd.read_csv(input_file)

print("Original Data:")
print(df)

# Handle missing values
df["age"] = df["age"].fillna(df["age"].mean())
df["department"] = df["department"].fillna("Unknown")

# Remove duplicates
df = df.drop_duplicates().reset_index(drop=True)

# Filter employees
high_salary = df[df["salary"] > 50000]

# Sort by salary
sorted_data = df.sort_values("salary", ascending=False)

# Group and aggregate
department_summary = df.groupby("department")["salary"].agg(
    ["count", "mean", "min", "max"]
)

# Basic statistics
statistics = df.describe()

# Save clean dataset
df.to_csv(output_file, index=False)

print("\nClean Data:")
print(df)

print("\nHigh Salary Employees:")
print(high_salary)

print("\nDepartment Summary:")
print(department_summary)

print("\nBasic Statistics:")
print(statistics)

print(f"\nClean dataset saved to: {output_file}")