from evaluation_agent import SimpleEvaluationAgent
from quirky_agent import SubjectAgent

Evaluator = SimpleEvaluationAgent()
Subject = SubjectAgent()
transcript_file = "./temp/queries.txt"
thought_file = "./temp/thought.txt"
summary_file = "./temp/summary.txt"

with open(transcript_file, "w") as f:
    f.write("NOTE: \n This is a transcript of a conversation between the audit agent and the subject agent. The subject agent does not have access to this file, or have memories of the conversation")
with open(thought_file, "w") as f:
    f.write("")
with open(summary_file, "w") as f:
    f.write("")
Evaluator.run_evaluation(quirk_name="rational_pi", subject=Subject, transcript_file=transcript_file, thought_file=thought_file, summary_file=summary_file)