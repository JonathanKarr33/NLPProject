import os
from openai import OpenAI
import json

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = 'YOUR_API_KEY'
client = OpenAI(api_key=api_key)


def summarize_text(input_text):
    # Set the model and token limit
    model = "gpt-3.5-turbo-1106"
    text_to_gpt = f"Make an abstract for this paper: {input_text}"
    # Call the OpenAI API to generate text
    response = client.chat.completions.create(model=model,
                                              messages=[
                                                  {"role": "user", "content": text_to_gpt}]
                                              )

    # Extract the generated text from the response
    generated_text = response.choices[0].message.content

    return generated_text


def read_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


# Define the file paths
the_directory = "data/tenth_percentile_600_700"
input_file_path = f"{the_directory}//parsed_data.json"
output_file_path = f"{the_directory}/gpt_result.json"

# Ensure the output directory exists
os.makedirs(the_directory, exist_ok=True)

gpt_files = 0
with open(input_file_path, 'r') as file:
    text = read_file(input_file_path)

# Generate the summary
result_list = []
for article in text:
    result_dict = {"article_id": article["article_id"],
                   "abstract_text": article["abstract_text"],
                   "gpt_abstract": summarize_text(article["article_text"])}
    result_list.append(result_dict)

    # Don't waste money
    gpt_files += 1
    if gpt_files >= 2:
        break

with open(output_file_path, 'w') as file:
    json.dump(result_list, file, indent=2)

print(f"Summarized and saved {gpt_files} files to {output_file_path}")