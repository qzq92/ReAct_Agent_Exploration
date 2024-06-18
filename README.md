# ReAct Agents Exploration

This is a simple exploration of ReAct Agents offered by LangChain Framework.

## API used

Please note that the following API requires the use of API key to work and are not free.
- *Langchain's ChatOpenAi* to chat with OpenAI's GPT-3.5-Turbo model (https://api.python.langchain.com/en/latest/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html).

## Environment file to edit
Please create an *.env* file with the following parameters. PYTHONPATH is required to be filled to ensure successful folder imports in project.

```
OPENAI_API_KEY=<YOUR API KEY>
PYTHONPATH = <Absolute path to the directory where this project is cloned>

# Optional if you are not using LangSmith for tracking llm utilisation related metrics
LANGCHAIN_API_KEY = <YOUR API KEY>
LANGCHAIN_TRACING_V2 = true
LANGCHAIN_PROJECT = <NAME FOR YOUR PROJECT>
```

For more information on Langsmith, refer to https://www.langchain.com/langsmith

## Installation and execution
Please use Anaconda distribution to install the necessary libraries with the following command

```
conda env create -f environment.yml
```

Upon installation and environment exectuion, run the following to see the inner workings of Agent involving *AgentAction* and *AgentFinish*
```
python main_agent_scratchpad.py
```

## Programming languages/tools involved
- Python
- Langchain
    - ChatOpenAI
    - PromptTemplate
    - CallBacks
    - Agent Schemas: AgentFinish and AgentAction

## Acknowledgement and Credits

The codebase developed are in reference to *Section 4: Diving Deep into ReAct Agents- Whats is the magic* of Udemy course titled "LangChain- Develop LLM powered applications with LangChain" available via https://www.udemy.com/course/langchain.
