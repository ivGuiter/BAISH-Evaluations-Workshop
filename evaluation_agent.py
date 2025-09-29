"""
Your Mission: Build a system that can automatically test if quirks work

Core logic:
1. Generate test prompts that might reveal the quirk
2. Get responses from both quirky and normal models
3. Analyze responses to detect quirk presence
4. Compare quirky vs baseline to see if evaluation worked

Think about:
- What makes a good test prompt?
- How do you detect behaviors in text?
- What counts as "success"?
- How do you handle edge cases?
"""

import random
from models import ModelWrapper
from quirky_prompts import QUIRKS, BASELINE_PROMPT
from audit_prompt import audit_system_prompt, audit_start_prompt, audit_summarize_prompt, audit_elaborate_prompt, audit_extract_report_prompt, audit_extract_summary_prompt
from tqdm import tqdm

class SimpleEvaluationAgent:
    def __init__(self):
        self.AgentWrapper = ModelWrapper()
        
    def generate_test_prompts(self, quirk_name, num_prompts=2):
        """
        Create a list of prompts to test the quirk
        
        Think about:
        - Should prompts be generic or specific to the quirk?
        - What kinds of questions might make the quirk visible?
        - How do you avoid biasing the results?
        """
        
        # TODO: Create a list of good test prompts
        # Hint: You might want both generic and quirk-specific prompts
        prompts_answer = self.AgentWrapper.query_model(audit_start_prompt.format(num_prompts), system_prompt=audit_system_prompt)
        return prompts_answer.splitlines()[-1].split(";")

    def detect_quirk(self, responses, quirk_name):
        """
        Analyze a list of responses to see if the quirk is present

        Think about:
        - How do you identify patterns in text?
        - What's the difference between presence and absence?
        - How do you handle false positives/negatives?
        
        Returns: A number between 0 and 1 indicating quirk strength
        """
        
        # TODO: Implement quirk detection logic
        # Hint: You have detection_keywords in QUIRKS[quirk_name]
        pass
    
    def run_evaluation(self, quirk_name, subject, transcript_file, thought_file, summary_file, num_prompts=3, alotted_time = 3):
        """
        Run a complete evaluation comparing quirky vs baseline behavior
        
        Process:
        1. Generate test prompts
        2. Get responses from quirky model
        3. Get responses from baseline model  
        4. Calculate quirk detection rates for both
        5. Compare results
        
        Think about:
        - What makes a fair comparison?
        - How do you measure success?
        - What could go wrong?
        """
        
        # TODO: Implement the full evaluation pipeline
        #print(f"Evaluating {quirk_name} on {model}...")
        
        prompts = self.generate_test_prompts("")
        subject_answers = subject.repeated_query(quirk_name, prompts)
        with open(transcript_file, "a") as f:
            for i in range(len(prompts)):
                f.write("\nBEHAVIOUR AUDIT AGENT: \n")
                f.write(prompts[i])
                f.write("\nSUBJECT AGENT: \n")
                f.write(subject_answers[i])

        turns = 0
        finished = False
        for t in tqdm(range(alotted_time)):

            # Analiza las respuestas del modelo defectuoso y hace un resumen
            with open(transcript_file) as f:
                big_prompt = "Following is the transcript of the model's answers. \n ------------------------- \n" + f.read() + audit_summarize_prompt
            audit_summary_answer = self.AgentWrapper.query_model(big_prompt, system_prompt=audit_system_prompt)
            with open(thought_file, "a") as f:
                f.write(audit_summary_answer)
                f.write("\n --------------------------------------------------------- \n")
            
            # Extrae el resumen
            summary = self.AgentWrapper.query_model(audit_extract_summary_prompt + audit_summary_answer, system_prompt=audit_system_prompt)
            with open(summary_file, "a") as f:
                f.write(summary)
                f.write("\n --------------------------------------------------------- \n")

            # Analiza el resumen y elige los prompts (o hace un informe)
            audit_continuation_answer = self.AgentWrapper.query_model(summary + audit_elaborate_prompt, system_prompt=audit_system_prompt)
            with open(thought_file, "a") as f:
                f.write(audit_continuation_answer)
                f.write("\n --------------------------------------------------------- \n")
            
            # Extrae los prompts (o el informe)
            decision = self.AgentWrapper.query_model(audit_extract_report_prompt + audit_continuation_answer, system_prompt=audit_system_prompt)
            print(decision)
            if decision == "REPORT DONE":
                finished = True
                print("The audit agent has stopped researching")
                return audit_continuation_answer
            else:
                prompts = decision.split(";")
                subject_answers = subject.repeated_query(quirk_name, prompts)
                
                with open(transcript_file, "a") as f:
                    f.write("\n----------------------------------------------\n")
                    for i in range(len(prompts)):
                        f.write("\nALIGNMENT AUDIT AGENT: \n")
                        f.write(prompts[i])
                        f.write("\nSUBJECT AGENT: \n")
                        f.write(subject_answers[i])


            #last_line = audit_answer.splitlines()[-1]
            #if last_line == "REPORT COMPLETE":
            #    finished = True
            #    print("The audit agent has stopped researching")
            #    return audit_answer
            #else:
            #    prompts = last_line.split(";")
            #    subject_answers = subject.repeated_query(quirk_name, prompts)
            #    with open(transcript_file, "a") as f:
            #        f.write("\n----------------------------------------------\n")
            #        for i in range(len(prompts)):
            #            f.write("\nALIGNMENT AUDIT AGENT: \n")
            #            f.write(prompts[i])
            #            f.write("\nSUBJECT AGENT: \n")
            #            f.write(subject_answers[i])
        return 0

        # TODO: Query baseline model for all prompts  
        # TODO: Calculate detection rates
        # TODO: Determine if evaluation succeeded
        # TODO: Return results dictionary
        
    def compare_across_models(self, quirk_name, models=None):
        """
        Test the same quirk across multiple models
        
        Think about:
        - Which models should you test?
        - How do you present the results clearly?
        - What patterns might you discover?
        """
        
        if models is None:
            # TODO: Set default list of models to test
            pass
        
        # TODO: Run evaluation on each model
        # TODO: Collect and present results
        pass
        
        pass

#Evaluator = SimpleEvaluationAgent()
#Evaluator.generate_test_prompts("To begin, explain what your first steps will be")
#Subject = 
