"""
Your task: Create an evaluation system that can:
1. Generate test prompts for a quirk
2. Get responses from both quirky and baseline models
3. Detect whether the quirk is present in responses
4. Calculate success rates

Think about:
- How do you test if a quirk is working?
- What makes a good test prompt?
- How do you detect behaviors in text?
- What counts as "success"?
"""

from models import ModelWrapper
from quirky_prompts import QUIRKS, BASELINE_PROMPT

class SimpleEvaluationAgent:
    def __init__(self):
        # TODO: Initialize your model wrapper
        pass
        
    def generate_test_prompts(self, quirk_name, num_prompts=5):
        """
        Generate test prompts that might reveal the quirk
        
        Think about:
        - What kinds of questions would make the quirk visible?
        - Should prompts be generic or specific to the quirk?
        - How do you avoid biasing the results?
        """
        # TODO: Create a list of test prompts
        pass
    
    def detect_quirk(self, responses, quirk_name):
        """
        Analyze responses to detect if the quirk is present
        
        Think about:
        - How do you identify quirky behavior in text?
        - What are different ways to detect patterns?
        - How do you avoid false positives/negatives?
        
        Returns: A score between 0 and 1 indicating quirk strength
        """
        # TODO: Implement quirk detection logic
        pass
    
    def run_evaluation(self, quirk_name, model_type="openai"):
        """
        Run a complete evaluation comparing quirky vs baseline model
        
        Think about:
        - What's a fair comparison?
        - How many test cases do you need?
        - How do you interpret the results?
        """
        # TODO: Implement the full evaluation pipeline
        print(f"Evaluating {quirk_name}...")
        
        # TODO: Get quirk info and test prompts
        # TODO: Test quirky model  
        # TODO: Test baseline model
        # TODO: Calculate and compare quirk detection rates
        # TODO: Return results
        
        pass