from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import os
import json

# Function to read text from a file


def read_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


# Define the file paths
#input_file_path = '../data/thousand_papers/gpt_result.json'
input_file_path = '../data/thousand_papers/our_result.json'
output_directory = "../scores"
#output_file_path = f"{output_directory}/gpt_result_word2vec_1000.json"
output_file_path = f"{output_directory}/our_result_word2vec_1000.json"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

gpt_files = 0
with open(input_file_path, 'r') as file:
    text = read_file(input_file_path)

# Generate the summary

result_list = []
for article in text:
    text1 = article["abstract_text"]
    text2 = article["article_text_summary"]
    # Tokenize the text
    tokens1 = word_tokenize(text1.lower())
    tokens2 = word_tokenize(text2.lower())

    # Train Word2Vec model
    model = Word2Vec(sentences=[tokens1, tokens2],
                     vector_size=100, window=5, sg=0, min_count=1)

    # Get Word2Vec embeddings for each token in the texts
    embeddings1 = [model.wv[word] for word in tokens1]
    embeddings2 = [model.wv[word] for word in tokens2]

    # Calculate the similarity between the two texts
    similarity = model.wv.n_similarity(tokens1, tokens2)
    result_dict = {"article_id": article["article_id"],
                   "word2vec_score": str(similarity)}
    result_list.append(result_dict)

with open(output_file_path, 'w') as file:
    json.dump(result_list, file, indent=2)
