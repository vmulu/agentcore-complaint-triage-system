from langchain.agents import create_agent
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from model.load import get_model
from pydantic import ValidationError
from schemas import InvokePayload
from tools import lookup_policy, get_reply_format
from prompts import SYSTEM_PROMPT, build_user_message

app = BedrockAgentCoreApp()

agent = create_agent(get_model(), tools=[lookup_policy, get_reply_format],
                     system_prompt=SYSTEM_PROMPT)

@app.entrypoint
def invoke(payload: dict) -> dict:
    try:
        data = InvokePayload.model_validate(payload)
    except ValidationError as e:
        return {"error": "invalid_payload", "details": e.errors()}
    result = agent.invoke({"messages": [{"role": "user", "content": build_user_message(data)}]})
    return {"draft": result["messages"][-1].content}


if __name__ == "__main__":
    app.run()
