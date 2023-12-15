import numpy as np
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import nltk
import os
import tiktoken
import json

#nltk.download('punkt')
#nltk.download('stopwords')

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
    
def calculate_token_count(text, model_name='gpt-3.5-turbo'):
    encoding = tiktoken.encoding_for_model(model_name)
    tokens = len(encoding.encode(text))
    return tokens

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

def generate_summary(text, top_n, output):
    stop_words = stopwords.words('english')
    summarize_text = []

    # Read text and tokenize
    sentences = sent_tokenize(text)
    # Generate similarity matrix across sentences
    sentence_similarity_matrix = build_similarity_matrix(sentences, stop_words)

    # Rank sentences in similarity matrix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph)

    # Sort the rank and pick top sentences
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)  
    current_selected = top_n
    tokens = 0
    print("starting:", len(ranked_sentences))
    if len(ranked_sentences) <= top_n:
        selected_sentences = [sentence for score, sentence in ranked_sentences[:current_selected]]
    while tokens < 3500 and current_selected < len(ranked_sentences):
        selected_sentences = [sentence for score, sentence in ranked_sentences[:current_selected]]
        text = " ".join(selected_sentences)
        tokens = calculate_token_count(text)
        current_selected += 15 #keep selecting more until at limit
    #print(tokens)
    index_map = {sentence: index for index, sentence in enumerate(sentences)}
    resorted_list = sorted(selected_sentences, key=lambda x: index_map[x])
    size = len(resorted_list)
    print("ending:", size)
    for i in range(size):
        summarize_text.append(resorted_list[i])
    
    return summarize_text


input_file_path = '../data/thousand_papers/parsed_data.json'
output_file_path = '../data/thousand_papers/thousand_papers_shrunk2.json'

result = read_file(input_file_path)
#print(len(result))
results = []
for article in result:
    text = ""
    #print(article)
    # Iterate through the outer list
    name = article["article_id"]
    text = article["article_text"]      
    processed_content = generate_summary(text, 80, output_file_path) #! might need to fix np
    new_text = "\n".join(processed_content)
    article["article_text"] = new_text
    results.append(article)
    print(f"Shrunk file: {name}")
with open(output_file_path, "w", encoding="utf-8") as f:
    json.dump(results, f)
