# File containing logic to log all LLM calls
from typing import Dict, Any, List
from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import LLMResult


# LangChain provides a callbacks system that allows you to hook into the various stages of your LLM application. This is useful for logging, monitoring, streaming, and other tasks (event driven). Handled specifically by basecallbackhandler class
class AgentCallbackHandler(BaseCallbackHandler):
    def on_llm_start(
            self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> Any:
        """Run when LLM starts running.

        Args:
            serialized (Dict[str, Any]): Dictionary of serialised input.
            prompts (List[str]): Prompts used by agent.

        """
        print(f"***Prompt to LLM was:***\n{prompts[0]}")
        print("*********")

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> Any:
        """Run when LLm ends running"""        
        print(f"***LLM Response:***\n{response.generations[0][0].text}")
        print("*********")