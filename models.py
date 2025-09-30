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
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key = os.getenv("OPENROUTER_API_KEY"))

    
    def query_model(self, prompt, system_prompt="You are a helpful assistant", extra_prompt="If you see this, something's wrong", extra_label="", model="anthropic/claude-3-haiku"):
        try:
            messages = [
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            if extra_label:
                messages.append({"role": extra_label, "content":extra_prompt})
            completion = self.client.chat.completions.create(
                model = model,
                messages=messages
            )
            return completion.choices[0].message.content
        except:
            print("Conectate al wifi pelotudo")
        return("['0']")
    
    def get_available_models(self):
        """Return a list of model names students can use"""
        # TODO: Return list of your available models
        pass
    
    def test_connection(self):
        """Quick test to see if your setup works"""
        # TODO: Try a simple API call and return True/False
        pass