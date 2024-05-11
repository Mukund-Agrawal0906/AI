import pandas as pd

data = {'Subjects': ['Math', 'Physics', 'Math', 'Physics', 'Chemistry'],
        'Book_Authors': ['Author1', 'Author2', 'Author1', 'Author3', 'Author2'],
        'No_of_Books': [9, 13, 22, 35, 7]}

IIIT_Library = pd.DataFrame(data)

total_books_per_subject = IIIT_Library.groupby('Subjects')['No_of_Books'].sum()

print("Total Number of Books for Each Subject:")
print(total_books_per_subject)
