from crewai import Crew, Agent, Task
import logging

class PhraseCrew:
    def __init__(self, word: str, api_key: str):
        """
        Inicializa uma crew simples para geração de frases.
        
        Args:
            word (str): Palavra base para geração da frase
        """
        self.api_key = api_key

        # Cria o agente criativo
        self.agent = Agent(
            role="Gerador de Frases Criativas",
            goal=f"Criar uma frase única e interessante usando a palavra '{word}'",
            backstory="Um escritor criativo que transforma palavras simples em frases inspiradoras"
        )
        
        # Cria a tarefa de geração de frase
        self.task = Task(
            description=f"Crie uma frase criativa e original usando a palavra '{word}'",
            agent=self.agent,
            expected_output="Uma string representando uma frase criativa."
        )
        
        # Inicializa a crew
        self.crew = Crew(
            agents=[self.agent],
            tasks=[self.task]
        )
        
        # Armazena a palavra original
        self.word = word
    
    def generate_phrase(self) -> str:

        result = self.crew.kickoff(inputs={"word": self.word})
        logging.info(f"Resultado da Crew: {result}")

        if hasattr(result, 'output'):
            return result.output
        return str(result)
