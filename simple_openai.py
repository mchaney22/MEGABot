# simple openai provides a simple way to use the openai api
#
# imports
import openai
import os
from dotenv import load_dotenv
import json
from engine_settings import EngineSettings

# class SimpleOpenAI: can perform the operations of completion, classification, search, question answering, fine-tuning, and embedding
class SimpleOpenAI:
    # init the api key
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv('openai_token')
    
    # completion: given a prompt string, return the openai completion
    def completion(self, prompt, engine_settings=EngineSettings()):
        
        response = openai.Completion.create(
            engine=engine_settings.engine_id,
            prompt=prompt,
            max_tokens=engine_settings.max_tokens,
            temperature=engine_settings.temperature,
            top_p=engine_settings.top_p,
            n=engine_settings.n,
            stream=engine_settings.stream,
            logprobs=engine_settings.logprobs,
            stop=engine_settings.stop,
            presence_penalty=engine_settings.presence_penalty,
            frequency_penalty=engine_settings.frequency_penalty,
            best_of = engine_settings.best_of,
            logit_bias = engine_settings.logit_bias,
            user = engine_settings.user,
        )
        return response
        

    # question_answering: given an example context string, examples list of string tuples, and a question string, return the openai question answering
    def question_answering(self, context, examples, question):
        pass

    # edits: given an input string and an instruction string, return the openai edits
    def edits(self, input, instruction, engine_settings=EngineSettings()):
        response = openai.Edit.create(
            engine=engine_settings.engine_id,
            input=input,
            instruction=instruction,
            temperature=engine_settings.temperature,
            top_p=engine_settings.top_p
        )
        return response


           


