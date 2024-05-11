import pandas as pd

data = {'Std_Name': ['Student1', 'Student2', 'Student3', 'Student4','Student5'],
        'Roll_no': [2201001, 2201002, 2201003, 2201004, 2201005],
        'CPI': [90, 45, 85, 63, 59]}

df = pd.DataFrame(data)

filtered_df = df[df['CPI'] > 60]

mean = df['CPI'].mean()
median = df['CPI'].median()
std = df['CPI'].std()

print("Original DataFrame:")
print(df)

print("\nFiltered DataFrame:")
print(filtered_df)

print("\nOverall Mean:", mean)
print("Overall Median:", median)
print("Overall Standard Deviation:", std)
