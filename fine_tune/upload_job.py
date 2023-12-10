from openai import OpenAI
client = OpenAI()

response1 = client.files.create(
  file=open("train.jsonl", "rb"), # change if needed
  purpose="fine-tune"
)
response2 = client.files.create(
  file=open("val.jsonl", "rb"), #! does this work
  purpose="fine-tune"
)
print("Training id:", response1.id)
print("Val id:", response2.id)