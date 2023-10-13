import os
from rouge import Rouge 

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip()

def save_individual_scores(scores, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(str(scores))

def save_aggregated_scores(scores, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        for filename, score in scores.items():
            file.write(f"{filename}: {score}\n")

def calculate_rouge_scores(data_folder, output_folder):
    rouge = Rouge()
    hypothesis_folder = os.path.join(data_folder, "gpt-results")
    reference_folder = os.path.join(data_folder, "reference")
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    aggregated_scores = {}
    for filename in os.listdir(hypothesis_folder):
        hypothesis_file_path = os.path.join(hypothesis_folder, filename)
        reference_file_path = os.path.join(reference_folder, filename)
        
        if os.path.exists(reference_file_path):
            hyp_text = load_text(hypothesis_file_path)
            ref_text = load_text(reference_file_path)
            
            scores = rouge.get_scores(hyp_text, ref_text, avg=True)
            output_path = os.path.join(output_folder, f"{filename[:-4]}_scores.txt")
            save_individual_scores(scores, output_path)
            
            aggregated_scores[filename] = scores
    
    aggregated_output_path = os.path.join(output_folder, "aggregated_scores.txt")
    save_aggregated_scores(aggregated_scores, aggregated_output_path)
    print(f"Aggregated scores saved to {aggregated_output_path}")

if __name__ == "__main__":
    data_folder = "data"
    output_folder = "scores"
    calculate_rouge_scores(data_folder, output_folder)
