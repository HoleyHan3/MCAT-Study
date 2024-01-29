import numpy as np
import pandas as pd

# Generate sample MCAT practice questions data
num_questions = 100
topics = ['Biology', 'Chemistry', 'Physics', 'CARS', 'Psychology/Sociology']
difficulty_levels = ['Easy', 'Medium', 'Hard']

# Generate random questions data
questions_data = {
    'Question': [f"Question {i+1}" for i in range(num_questions)],
    'Topic': np.random.choice(topics, num_questions),
    'Difficulty': np.random.choice(difficulty_levels, num_questions),
    'Correct Answer': np.random.choice(['A', 'B', 'C', 'D'], num_questions),
    'Explanation': [f"Explanation for Question {i+1}" for i in range(num_questions)]
}

# Create a DataFrame from the generated data
questions_df = pd.DataFrame(questions_data)

# Display the generated data
print("Sample MCAT Practice Questions Data:")
print(questions_df.head())
