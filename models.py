"""
Your task: Create a ModelWrapper class that can:
1. Call OpenAI's GPT models
2. Call Anthropic's Claude models  
3. Handle system prompts
4. Deal with errors gracefully

Hints:
- You'll need to import the right packages
- API calls need authentication
- Different APIs have different parameter names
- Always handle exceptions!
"""

# TODO: Add your imports here

class ModelWrapper:
    def __init__(self):
        # TODO: Set up API clients
        pass
    
    def query_openai(self, prompt, system_prompt="You are a helpful assistant"):
        # TODO: Implement OpenAI API call
        # Hint: Use the chat completions endpoint
        pass
    
    def query_claude(self, prompt, system_prompt="You are a helpful assistant"):
        # TODO: Implement Claude API call  
        # Hint: Messages format is different from OpenAI
        pass