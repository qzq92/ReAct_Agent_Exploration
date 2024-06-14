from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import LLMResult

from typing import Dict, Any, List

# LangChain provides a callbacks system that allows you to hook into the various stages of your LLM application. This is useful for logging, monitoring, streaming, and other tasks (event driven). Handled specifically by basecallbackhandler class
class AgentCallbackHandler(BaseCallbackHandler):
    def on_llm_start(
            self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> Any:
        """Run when LLM starts running.

        Args:
            serialized (Dict[str, Any]): _description_
            prompts (List[str]): _description_

        Returns:
            Any: _description_
        """
        pass

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> Any:
        """Run when LLm ends running"""