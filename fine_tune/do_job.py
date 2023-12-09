from openai import OpenAI
client = OpenAI()

response = client.fine_tuning.jobs.create(
  training_file="test.jsonl", 
  model="gpt-3.5-turbo", 
  hyperparameters={
    "n_epochs":5
  },

)
print(response)