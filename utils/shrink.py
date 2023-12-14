import numpy as np
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import nltk
import os

nltk.download('punkt')
nltk.download('stopwords')

def read_file(file_name):
    with open(file_name, "r", encoding="utf-8", errors="ignore") as file:
        return file.read()

def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []

    sent1 = [w.lower() for w in sent1 if w not in stopwords]
    sent2 = [w.lower() for w in sent2 if w not in stopwords]

    all_words = list(set(sent1 + sent2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    for w in sent1:
        vector1[all_words.index(w)] += 1

    for w in sent2:
        vector2[all_words.index(w)] += 1

    return 1 - cosine_distance(vector1, vector2)

def build_similarity_matrix(sentences, stop_words):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))

    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:  # ignore if both are same sentences
                continue
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix

def generate_summary(file_name, top_n, output):
    stop_words = stopwords.words('english')
    summarize_text = []

    # Read text and tokenize
    sentences = sent_tokenize(read_file(file_name))
    # Generate similarity matrix across sentences
    sentence_similarity_matrix = build_similarity_matrix(sentences, stop_words)

    # Rank sentences in similarity matrix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph)

    # Sort the rank and pick top sentences
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)    
    selected_sentences = [sentence for score, sentence in ranked_sentences[:top_n]]

    index_map = {sentence: index for index, sentence in enumerate(sentences)}
    resorted_list = sorted(selected_sentences, key=lambda x: index_map[x])
    size = len(resorted_list)
    print(size)
    for i in range(size):
        summarize_text.append(resorted_list[i])
    with open(output, "w", encoding="utf-8") as f:
        for sentence in summarize_text:
            f.write(sentence.rstrip() + "\n")

folder_path = "../data/short/main_paper/"
output_path = "../data/short/shrink_paper/"
for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        output = os.path.join(output_path, filename)
        if os.path.isfile(file_path):
            print(file_path)            
            processed_content = generate_summary(file_path, 50, output) #! might need to fix np
            #it is saved in the function
            print(f"Shrunk file: {filename}")
