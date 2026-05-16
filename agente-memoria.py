from dotenv import load_dotenv
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.tavily import TavilyTools
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIChat

load_dotenv()

BancoDados = SqliteDb(db_file="temp/registros.db")

agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é um mago que vive em um castelo no topo de uma montanha sombria",
    db=BancoDados,
    session_id="09095866-520e-425c-986b-b44538834eb8",
    tools=[DuckDuckGoTools(),TavilyTools],
    markdown=True
)

while True:
    pergunta = input("Digite a sua pergunta: ")
    if pergunta.lower() in ['quit', 'sair', 'cancelar', 'sair' , 'finalizar']:
        print("Encerrado agente...\nAté mais tarde 🤖")
        break
    else:
        agente.print_response(pergunta)