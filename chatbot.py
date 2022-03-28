import neuralintents

# if we use mappings, it doesn't send data to the server. 
#Don't use mappings unless we want to execute things server-side. 
mappings = {}
assistant = neuralintents.GenericAssistant('data/intents.json', model_name="data/model", intent_methods=mappings)

assistant.train_model() # train the model
#assistant.save_model() # save the model

#assistant.load_model() # load the model