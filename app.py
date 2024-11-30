import os
from flask import Flask, request, jsonify
from phrasecrew import PhraseCrew

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    try:
        # Recebe o JSON enviado na requisição
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Obtém a chave da API do OpenAI (de uma variável de ambiente)
        openai_api_key = os.getenv('OPENAI_API_KEY')
        if not openai_api_key:
            return jsonify({"error": "OpenAI API key not found"}), 500

        # Cria a PhraseCrew passando a palavra do JSON e a chave da API
        phrase_crew = PhraseCrew(data['word'], openai_api_key)
        generated_phrase = phrase_crew.generate_phrase()

        # Retorna a frase gerada
        return jsonify({"phrase": generated_phrase}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)