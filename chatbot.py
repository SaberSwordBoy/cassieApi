import neuralintents

def help_function():
    return "HELP"

mappings = {"help": help_function}
assistant = neuralintents.GenericAssistant('data/intents.json', model_name="data/model", intent_methods=mappings)

assistant.train_model()
assistant.save_model()

#assistant.load_model()