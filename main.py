from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
assistant = AssistantAgent(
    "assistant",
    llm_config={"request_timeout": 600, "seed": 44, "temperature": 0, "config_list": config_list},
    system_message="Code the chart using python and return a fully functional self contained code block that can be executed in a file.",
    default_auto_reply="test",
)
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})
user_proxy.initiate_chat(
    assistant, message="Plot a chart of NVDA and TESLA stock price change YTD."
)
# This initiates an automated chat between the two agents to solve the task
