from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat

#Todos os agentes prcisam da cahve de API, e a função load_dotenv faz a leitura do arquivo .env
load_dotenv()

perguntaUsuario = input("Digite sua pergunta: ")

agente = Agent(
    model= OpenAIChat(id="gpt-4o-mini"),
    markdown=True
)

agente.print_response(perguntaUsuario)