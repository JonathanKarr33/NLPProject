from openai import OpenAI
import json
client = OpenAI()

result = client.fine_tuning.jobs.list(limit=1)
id = result.data[0].id
# # Retrieve the state of a fine-tune
result = client.fine_tuning.jobs.retrieve(id)
print(result.fine_tuned_model)
print(result.status)