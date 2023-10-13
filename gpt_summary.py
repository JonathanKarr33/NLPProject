import os
import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
# Not pushing my key to GitHub for privacy reasons
# Use gpt3.5 turbo -- see pricing here https://openai.com/pricing#language-models
api_key = 'YOUR_API_KEY'


def summarize_text(text):
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Summarize the following text: \n{text}",
        n=1,  # Number of summaries to generate
        stop=None  # Set custom stop tokens if needed
    )

    summary = response.choices[0].text.strip()
    return summary


# Define the file paths
input_directory = 'data/main_paper'
output_directory = 'data/gpt_results'

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# List all files in the input directory
input_files = os.listdir(input_directory)

# Process each file
gpt_files = 0
for file_name in input_files:
    input_file_path = os.path.join(input_directory, file_name)
    output_file_path = os.path.join(output_directory, file_name)

    with open(input_file_path, 'r') as file:
        text = file.read()
    # Problem limit of summary tokens
    #This model's maximum context length is 4097 tokens, however you requested 7342 tokens
    max_summary_tokens = 2250 #not 4097 because of response needed
    summary_tokens = len(text.split())

    if summary_tokens > max_summary_tokens:
        # Truncate the summary
        text = ' '.join(text.split()[:max_summary_tokens])

    # Generate the summary
    summary = summarize_text(text)
    
    
    # Save the summary in the output directory with the same filename
    with open(output_file_path, 'w') as output_file:
        output_file.write(text)

    #Don't waste money
    gpt_files += 1
    if gpt_files == 5:
        break

print(f"Summarized and saved {gpt_files} files to {output_file_path}")
