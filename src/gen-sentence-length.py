import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files into pandas DataFrames
human_essays_df = pd.read_csv('data/student-essays.csv')
gpt4_essays_df = pd.read_csv('data/gpt4-essays.csv')

# Calculate the length of each essay (word count)
human_essay_lengths = human_essays_df['essay'].apply(lambda essay: len(essay.split()))
gpt4_essay_lengths = gpt4_essays_df['essay'].apply(lambda essay: len(essay.split()))

# Plotting the histograms of essay lengths
plt.figure(figsize=(10, 6))

# Histogram for human-written essays
plt.hist(human_essay_lengths, bins=20, alpha=0.7, color='blue', edgecolor='black', label='Human')

# Histogram for GPT-4-generated essays
plt.hist(gpt4_essay_lengths, bins=20, alpha=0.7, color='green', edgecolor='black', label='GPT-4')

plt.title('Distribution of Essay Lengths')
plt.xlabel('Length of essay (words)')
plt.ylabel('Frequency')
plt.legend(loc='upper right')

# Show grid lines for better readability
plt.grid(axis='y', alpha=0.75)

# Finally, display the plot
plt.show()