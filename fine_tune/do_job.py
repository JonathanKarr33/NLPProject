from openai import OpenAI
client = OpenAI()

response = client.fine_tuning.jobs.create(
  training_file="file-YYFZl4agq5MgKmQLvcMg5Zcq", #! need to use id's instead
  validation_file="file-MWYpv4Xy4RW70BTaAmXVuUdl", 
  model="gpt-3.5-turbo-1106", 
  hyperparameters={
    "n_epochs":10
  },

)
print(response)