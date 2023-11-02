import pandas as pd
data = {
    'Student_ID': [1, 2, 3, 4, 5],
    'Course': ['Math', 'Science', 'Math', 'History', 'Science'],
    'Score': [90, 85, 78, 92, 88],
    'Hours_Studied': [10, 8, 12, 5, 9]
}
df = pd.DataFrame(data)
correlation_coefficients = df.groupby('Course').apply(lambda x: x['Hours_Studied'].corr(x['Score']))
strongest_corr_course = correlation_coefficients.idxmax()
weakest_corr_course = correlation_coefficients.idxmin()
course_summary = df.groupby('Course').agg({'Score': 'mean', 'Hours_Studied': 'mean'})
print("1. Correlation coefficients between 'Hours_Studied' and 'Score' for each course:")
print(correlation_coefficients)
print("\n2. Course with the strongest correlation:", strongest_corr_course)
print("Course with the weakest correlation:", weakest_corr_course)
print("\n3. Aggregated Data - Average Score and Average Hours Studied for Each Course:")
print(course_summary)
