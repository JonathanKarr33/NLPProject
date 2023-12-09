from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
# pip install gensim

# Sample input sentences
sentence1 = "Natural language processing is a field of artificial intelligence."
sentence2 = "NLP is a subfield of AI that focuses on the interaction between computers and humans."

# Tokenize the sentences
# Convert to lowercase for consistency
tokens1 = word_tokenize(sentence1.lower())
tokens2 = word_tokenize(sentence2.lower())

# Train Word2Vec model
model = Word2Vec([tokens1, tokens2], min_count=1, size=100, window=5, sg=0)

# Get Word2Vec embeddings for each token in the sentences
embeddings1 = [model.wv[word] for word in tokens1]
embeddings2 = [model.wv[word] for word in tokens2]

# Calculate the similarity between the two sentences
similarity = model.wv.n_similarity(tokens1, tokens2)

# Print results
print("Word2Vec Embeddings for Sentence 1:", embeddings1)
print("Word2Vec Embeddings for Sentence 2:", embeddings2)
print("Similarity between Sentence 1 and Sentence 2:", similarity)
