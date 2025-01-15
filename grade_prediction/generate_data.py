import pandas as pd
import numpy as np
import random

def generate_training_data(num_rows=100):
    """
    Generates a DataFrame with random data for training, including outliers and randomness in inputs and output.

    Parameters:
    - num_rows: Number of rows to generate.

    Returns:
    - df: DataFrame containing the training data.
    """
    data = {
        "studied": [],
        "missing": [],
        "Math_last": [],
        "Math": [],
        "solution": []
    }

    for _ in range(num_rows):
        # Generate random inputs
        studied = random.randint(0, 20)  # Hours of study (0 to 20 hours)
        missing = random.randint(0, 30)  # Missed hours (0 to 30 hours in the last 3 months)
        math_last = random.randint(10, 100)  # Random starting grade (between 10 and 100)

        # Generate an array of grades where the last one is equal to math_last
        math_grades = [random.randint(max(0, math_last - 40), min(100, math_last + 40)) for _ in range(4)]  # Random grades within ±40 of math_last
        math_grades.append(math_last)  # Ensure the last grade is the same as math_last

        # Calculate the solution with some randomness and outliers
        solution = generate_solution(studied, missing, math_last, math_grades)

        # Introduce random noise or outliers in the solution
        if random.random() < 0.1:  # 10% chance to introduce an outlier
            solution += random.randint(-10, 20)  # Add a random noise between -10 and +20
        solution = np.clip(solution, 20, 100)  # Ensure it's within a realistic range (30 to 90)

        # Append the generated data to the dictionary
        data["studied"].append(studied)
        data["missing"].append(missing)
        data["Math_last"].append(math_last)
        data["Math"].append(math_grades)
        data["solution"].append(solution)

    # Create DataFrame from the dictionary
    df = pd.DataFrame(data)

    # Store the data in a CSV file, ensuring the header is at the top
    df.to_csv('training_data.csv', index=False)  # index=False ensures no extra column for indices

    # Display the first few rows of the DataFrame to confirm
    print(df.head())
    return df


def generate_solution(studied, missing, math_last, math_grades):
    """
    Generates a reasonable predicted grade based on input data, with bonus for high performers.
    """
    # Calculate average grade from last grades (excluding the last one)
    avg_grade = np.mean(math_grades[:-1])

    # Assign new weights to factors
    weight_study = 0.2  # Higher weight for study hours
    weight_missing = -0.2  # Negative impact for missed hours
    weight_last_grade = 0.4  # The last grade has a high impact
    weight_avg_grade = 0.1  # Average of the last grades has some impact

    # Calculate predicted grade based on weighted combination of inputs
    predicted_grade = (weight_study * studied) + (weight_missing * missing) + \
                      (weight_last_grade * math_last) + (weight_avg_grade * avg_grade)

    # Base grade value to avoid extremely low scores
    predicted_grade += 40  # Base score for a student who is doing the bare minimum

    # Apply a penalty for low-performing students (Math_last below 50)
    if math_last < 50:  # If the student has been consistently performing poorly
        predicted_grade *= 0.85  # Slight penalty for low performers

    # Add a bonus for high performers (if Math_last is above 80)
    if math_last > 85:
        predicted_grade += 2.5  # Small bonus for high performers (e.g., 5 points)

    # Ensure the predicted grade is within a realistic range (30 to 90)
    predicted_grade = np.clip(predicted_grade, 30, 100)  # Keep the predicted grade realistic

    return round(predicted_grade)


# Run the function to generate training data with outliers and randomness
generate_training_data(num_rows=2)
