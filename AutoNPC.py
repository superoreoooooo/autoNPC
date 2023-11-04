from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate, 
    PromptTemplate
)
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser

class CommaSeparatedListOutputParser(BaseOutputParser):
    """LLM 아웃풋에 있는 ','를 분리해서 리턴하는 파서."""
    def parse(self, text: str):
        return text.strip().split(":")

template = """
        너는 게임 NPC를 생성하는데 도움을 주는 AI야. 내가 게임의 장르와 게임의 분위기, 게임 NPC의 직업, 게임 NPC의 종족을 말해 주고, 이에 따른 게임 NPC를 생성해 달라고 말하면 내가 말해준 게임의 장르, 게임의 분위기, 게임 NPC의 직업, 게임 NPC의 종족에 따라 게임 NPC의 이름과 게임 NPC의 스토리, 그리고 게임 NPC의 퀘스트를 생성해 줘. 
        퀘스트에는 퀘스트의 이름, 퀘스트의 스토리, 게임 NPC의 요소들과 관련된 물품을 모아오기 또는 게임 NPC의 요소들과 관련된 몬스터 등의 사냥을 통한 퀘스트의 목표, 게임 NPC의 요소들과 관련된 보상도 작성해 줘. 퀘스트의 목표는 정확한 개수가 있어야 하고, 퀘스트의 보상도 정확한 개수를 작성해야 해. 그리고 퀘스트의 목표에는 경험치가 같이 주어져야 하고, 퀘스트의 보상에는 NPC의 장르와 관련된 재화또한 작성해야 돼. 예상되는 퀘스트의 난이도에 따른 적당한 양의 보상과 재화를 작성해 줘.
        퀘스트는 4가지 생성해 줘야 하고, 각각의 퀘스트에 들어가는 목표는 1개여야 해.
        퀘스트의 보상은 comma(,)로 분리해 줘.
        그리고 답변의 형식은 아래에 주어질 거야. 형식에 맞춰서 생성해 줘.

        name : 게임 NPC이름,
        story : 게임 NPC 스토리,
        quest1 : 퀘스트 1 이름,
        quest1_story : 퀘스트 1 스토리,
        quest1_goal : 퀘스트 1 목표,
        quest1_reward : 퀘스트 1 보상,
        quest2 : 퀘스트 2 이름,
        quest2_story : 퀘스트 2 스토리,
        quest2_goal : 퀘스트 2 목표,
        quest2_reward : 퀘스트 2 보상,
        quest3 : 퀘스트 3 이름,
        quest3_story : 퀘스트 3 스토리,
        quest3_goal : 퀘스트 3 목표,
        quest3_reward : 퀘스트 3 보상,
        quest4 : 퀘스트 4 이름,
        quest4_story : 퀘스트 4 스토리,
        quest4_goal : 퀘스트 4 목표,
        quest4_reward : 퀘스트 4 보상

        이름과 스토리, 그리고 각각의 퀘스트 사이에는 하나의 줄띄움을 해줘.

        게임 NPC가 장르에 잘 어울리고, 모든 요소가 자연스러우면 고마울 것 같아.
    """

system_template = SystemMessagePromptTemplate.from_template(template)

human_template = "게임의 장르는 {genre}, 게임의 분위기는 {ambient}, 게임 NPC의 직업은 {job}, 게임 NPC의 종족은 {brood}고, 이에 따른 게임 NPC의 이름과 게임 NPC의 스토리, 그리고 게임 NPC의 퀘스트 4개를 생성해 줘."
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_template, human_message_prompt])

print(chat_prompt)

chain = LLMChain(
    llm=ChatOpenAI(openai_api_key = "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"),
    prompt=chat_prompt,
    output_parser=CommaSeparatedListOutputParser()
)
print("\n\n\n\n")
print(chain.run({"genre" : "판타지", "ambient" : "평화로움", "job" : "왕실 기사", "brood" : "인간"}))