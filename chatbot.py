import neuralintents

# if we use mappings, it doesn't send data to the server. 
#Don't use mappings unless we want to execute things server-side. 
mappings = {}
assistant = neuralintents.GenericAssistant('data/intents.json', model_name="data/model", intent_methods=mappings)

# Create and save a model
assistant.train_model()
#assistant.save_model()

# Load a previously created model
#assistant.load_model()