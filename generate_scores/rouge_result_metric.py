from nltk.tokenize import word_tokenize
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import os
import json
from rouge import Rouge

# Function to read text from a file


def read_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


# Define the file paths
#input_file_path = '../data/thousand_papers/gpt_result.json'
input_file_path = '../data/thousand_papers/our_result.json'
output_directory = "../scores"
#output_file_path = f"{output_directory}/gpt_rouge_finetune_result1000.json"
output_file_path = f"{output_directory}/our_rouge_finetune_result1000.json"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

gpt_files = 0
with open(input_file_path, 'r') as file:
    text = read_file(input_file_path)

# Generate the summary
result_list = []
rouge = Rouge()

for article in text:
    text1 = article["abstract_text"]
    text2 = article["article_text_summary"]

    # Calculate the ROUGE score between the two texts
    rouge_scores = rouge.get_scores(text1, text2)
    rouge_score = rouge_scores[0]["rouge-1"]["f"]

    result_dict = {"article_id": article["article_id"],
                   "rouge_score": rouge_score}
    result_list.append(result_dict)

with open(output_file_path, 'w') as file:
    json.dump(result_list, file, indent=2)
