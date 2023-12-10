import os
import json
from statistics import mean

# Folder containing JSON files
folder_path = "scores/fifty_scores"

# List all JSON files in the folder
json_files = [os.path.join(folder_path, file) for file in os.listdir(
    folder_path) if file.endswith(".json")]

# Function to read a JSON file


def read_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


# Read each JSON file
data_list = [read_json(file) for file in json_files]

# Create a dictionary to store scores based on article_id
scores_dict = {}

# Iterate through each JSON file's data
for data, file in zip(data_list, json_files):
    for item in data:
        article_id = item["article_id"]
        if article_id not in scores_dict:
            scores_dict[article_id] = {"article_id": article_id}
        if file == 'scores/fifty_scores/gpt_fine_tune_word2vc_result.json':
            scores_dict[article_id]["word2vec_fine_tune_score"] = float(
                item["word2vec_score"])
        elif file == 'scores/fifty_scores/gpt_raw_word2vc_result.json':
            scores_dict[article_id]["word2vec_raw_score"] = float(
                item["word2vec_score"])
        elif file == 'scores/fifty_scores/gpt_fine_tune_rouge_result.json':
            scores_dict[article_id]["rouge_fine_tune_score"] = item["rouge_score"]
        elif file == 'scores/fifty_scores/gpt_raw_rouge_result.json':
            scores_dict[article_id]["rouge_raw_score"] = item["rouge_score"]


# Convert the dictionary values to a list
merged_data = list(scores_dict.values())

# Calculate the average scores
all_rouge_fine_tune = []
all_rouge_raw = []
all_word2vec_fine_tune = []
all_word2vec_raw = []
for article_id, scores in scores_dict.items():
    for key in ["word2vec_fine_tune_score", "word2vec_raw_score", "rouge_fine_tune_score", "rouge_raw_score"]:
        if key == "word2vec_fine_tune_score":
            all_word2vec_fine_tune.append(scores["word2vec_fine_tune_score"])
        elif key == "word2vec_raw_score":
            all_word2vec_raw.append(scores["word2vec_raw_score"])
        elif key == "rouge_fine_tune_score":
            all_rouge_fine_tune.append(scores["rouge_fine_tune_score"])
        elif key == "rouge_raw_score":
            all_rouge_raw.append(scores["rouge_raw_score"])

print("Rouge Raw: " + str(mean(all_rouge_raw)))
print("Rouge Fine Tune: " + str(mean(all_rouge_fine_tune)))
print("Word2Vec Raw: " + str(mean(all_word2vec_raw)))
print("Word2Vec Tune: " + str(mean(all_word2vec_fine_tune)))
# Print or save the merged data as needed
# print(json.dumps(merged_data, indent=2))
