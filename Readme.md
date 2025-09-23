# Behavioral Evaluation Workshop

## Setup Instructions

1. **Install packages:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get API keys:**
   - OpenAI: https://platform.openai.com/api-keys
   - Anthropic: https://console.anthropic.com/

3. **Create `.env` file:**
   ```
   OPENAI_API_KEY=your_openai_key
   ANTHROPIC_API_KEY=your_anthropic_key

## Your Mission

Build a system that can automatically detect quirky behaviors in AI models!

## Building Order

1. **Start with `models.py`** - Get basic API calls working
2. **Design quirks in `quirky_prompts.py`** - Create interesting behaviors  
3. **Build evaluation logic in `evaluation_agent.py`** - Detect the quirks
4. **Test everything with `test_basic.py`** - Debug and iterate

## Key Questions to Think About

- What makes a behavior easy vs hard to detect?
- How do you know if your evaluation is working correctly?
- What could go wrong with this approach?
- How does this relate to real AI safety concerns?

## Debugging Tips

- Test each component separately first
- Print everything to see what's happening  
- Start with simple cases before complex ones
- Ask for help when you're stuck!

Remember: The goal is learning, not perfect code. Struggle is part of the process!