import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class ModelWrapper:
    def __init__(self):
        # TODO: Create OpenAI client that points to OpenRouter
        # Hint: You need to set a custom base_url
        # OpenRouter URL: "https://openrouter.ai/api/v1"
        
        # TODO: Define which models you want to use
        # Here are some options:
        # "openai/gpt-4o-mini" - OpenAI (cheap)
        # "anthropic/claude-3-haiku" - Anthropic (cheap) 
        # "google/gemini-flash-1.5" - Google (cheap)
        # "qwen/qwen-2-7b-instruct" - Free!
        # "meta-llama/llama-3-8b-instruct" - Meta
        
        pass
    
    def query_model(self, prompt, system_prompt="You are a helpful assistant", model="gpt-4"):
        """
        Send a prompt to any AI model and get back a response
        
        Think about:
        - How do you make an API call?
        - What parameters do you need?
        - What happens when things go wrong?
        - How do you keep responses short for the workshop?
        """
        # TODO: Implement the API call
        # Hint: Use self.client.chat.completions.create()
        pass
    
    def get_available_models(self):
        """Return a list of model names students can use"""
        # TODO: Return list of your available models
        pass
    
    def test_connection(self):
        """Quick test to see if your setup works"""
        # TODO: Try a simple API call and return True/False
        pass
