from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat

load_dotenv()

#carregar a cahve api
agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é um mago que vive em um castelo no topo de uma montanha sombria",
    markdown=True
)

while True:
    pergunta = input("Digite a sua pergunta: ")
    if pergunta.lower() in ['quit', 'sair', 'cancelar', 'sair' , 'finalizar']:
        print("Encerrado agente...\nAté mais tarde 🤖")
        break
    else:
        agente.print_response(pergunta)