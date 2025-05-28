from langchain_core.output_parsers import JsonOutputParser
from langchain_deepseek import ChatDeepSeek
from langchain.prompts import PromptTemplate
from langchain_core.messages import HumanMessage

# 定义输出格式
parser = JsonOutputParser()
prompt = PromptTemplate.from_template("请返回JSON格式的用户信息：{query}")

# 调用大模型并解析
llm = ChatDeepSeek(model="deepseek-chat")
formatted_prompt = prompt.format(query="用户ID 123")
message = HumanMessage(content=formatted_prompt)
output = llm.invoke([message])

# 从 AIMessage 中提取内容
parsed_output = parser.parse(output.content)
print(parsed_output)