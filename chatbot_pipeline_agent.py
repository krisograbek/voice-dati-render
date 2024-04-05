import pandas as pd
from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits import create_sql_agent

from dotenv import load_dotenv

load_dotenv()


class ChatbotPipeline:
    def __init__(self, csv_file=None, db_name="dati", model=4):
        self.model_name = "gpt-3.5-turbo" if model == 3 else "gpt-4-0125-preview"
        self.engine = self.create_db_engine(csv_file, db_name)
        self.db = SQLDatabase(engine=self.engine)
        self.llm = ChatOpenAI(temperature=0.0, model=self.model_name)

        self.agent_executor = create_sql_agent(
            self.llm, db=self.db, agent_type="openai-tools", verbose=True
        )

    @staticmethod
    def create_db_engine(csv_file, name):
        engine = None
        if csv_file is not None:
            df = pd.read_csv(csv_file)
            engine = create_engine(f"sqlite:///{name}.db")
            df.to_sql(name, engine, index=False, if_exists="replace")
        return engine

    def run_sql_agent(self, query):
        response = self.agent_executor.invoke(query)
        return response
