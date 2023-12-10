from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import os

# Function to read text from a file


def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


# File paths
file_path1 = 'data/short/abstracts/2310.08569.txt'
file_path2 = 'data/short/gpt_results/2310.08569.txt'

# Read text from files
text1 = read_text_from_file(file_path1)
text2 = read_text_from_file(file_path2)

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

# Print results
# print("Word2Vec Embeddings for Text 1:", embeddings1)
# print("Word2Vec Embeddings for Text 2:", embeddings2)
print("Similarity between Text 1 and Text 2:", similarity)
