import numpy as np

# Convert to NumPy array
grades = np.array([[85, 78, 92, 88], #std1
                    [70, 76, 80, 65], #std2
                    [90, 88, 94, 91], #std3
                    [60, 65, 58, 62], #std4
                    [100, 95, 98, 97]]) #std5

# Print shape
print("Shape:", grades.shape) #(4 * 5)

# Mean grade of each student (axis=1)--> rows
print("Mean grade per student:", grades.mean(axis=1))

# Mean grade of each subject (axis=0)-->columns
print("Mean grade per subject:", grades.mean(axis=0))

# Extract students with average grade > 85
student_means = grades.mean(axis=1)
print("Students with avg > 85:\n", grades[student_means > 85])

# Add bonus of 5 marks using broadcasting
grades_bonus = grades + 5
print("After +5 bonus:\n", grades_bonus)

# Min-Max normalization
min_val = grades.min()
max_val = grades.max()
normalized = (grades - min_val) / (max_val - min_val)
print("Normalized:\n", normalized)

# Flatten to single vector
flattened = grades.reshape(-1)
print("Flattened:", flattened)