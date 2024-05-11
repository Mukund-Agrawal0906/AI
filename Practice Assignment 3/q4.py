import pandas as pd

data = {'Name': ['Radhika', 'Rohan', 'Aditya', 'Ujwal'],
        'Age': [25, 17, 15, 80],
        'Salary': [150000, -1000, -5000, 90000]}

dirty_data = pd.DataFrame(data)

clean_data = dirty_data[(dirty_data['Age'] >= 18) & (dirty_data['Salary'] >= 0)]

print("Cleaned DataFrame:")
print(clean_data)
