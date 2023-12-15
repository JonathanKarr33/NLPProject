import json
import statistics

# Function to calculate sum, average, and standard deviation for a field
def calculate_statistics(data, field):
    values = [float(item[field]) for item in data]
    total_sum = sum(values)
    average = total_sum / len(values)
    std_deviation = statistics.stdev(values)
    return total_sum, average, std_deviation

# Read and parse the JSON files
with open('../scores/gpt_result_word2vec_1000.json', 'r') as file:
    json1 = json.load(file)

with open('../scores/our_result_word2vec_1000.json', 'r') as file:
    json2 = json.load(file)

with open('../scores/gpt_rouge_finetune_result1000.json', 'r') as file:
    json3 = json.load(file)

with open('../scores/our_rouge_finetune_result1000.json', 'r') as file:
    json4 = json.load(file)

# Calculate statistics for 'word2vec_score' field from the first two files
total_sum_x1, average_x1, std_deviation_x1 = calculate_statistics(json1, 'word2vec_score')
total_sum_x2, average_x2, std_deviation_x2 = calculate_statistics(json2, 'word2vec_score')

# Calculate statistics for 'rouge_score' field from the last two files
total_sum_y1, average_y1, std_deviation_y1 = calculate_statistics(json3, 'rouge_score')
total_sum_y2, average_y2, std_deviation_y2 = calculate_statistics(json4, 'rouge_score')

# Print the results
print("Statistics for 'word2vec_score' field from gpt_result_word2vec_1000.json and our_result_word2vec_1000.json:")
print(f"Average: {average_x1} and {average_x2}")
print(f"Standard Deviation: {std_deviation_x1} and {std_deviation_x2}")

print("\nStatistics for 'rouge_score' field from gpt_rouge_finetune_result1000.json and our_rouge_finetune_result1000.json:")
print(f"Average: {average_y1} and {average_y2}")
print(f"Standard Deviation: {std_deviation_y1} and {std_deviation_y2}")
