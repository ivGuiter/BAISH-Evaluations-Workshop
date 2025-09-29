from models import ModelWrapper
from quirky_prompts import QUIRKS, BASELINE_PROMPT

class SubjectAgent:
    def __init__(self):
        self.AgentWrapper = ModelWrapper()
    
    def repeated_query(self, quirk_name, prompts):
        answers = []
        for p in prompts:
            output = self.AgentWrapper.query_model(prompt=p, system_prompt=QUIRKS[quirk_name]["system_prompt"])
            answers.append(output)
        #print(answers)
        return answers