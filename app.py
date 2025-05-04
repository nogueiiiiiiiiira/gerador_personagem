from flask import Flask, request, jsonify 
from ollama import chat
from pydantic import BaseModel

# importa o módulo de chat do Ollama
app = Flask(__name__, static_folder='static')

# define o modelo de dados para o personagem
class Personagem(BaseModel):
    nome: str
    raca: str
    classe: str
    caracteristicas: list[str]
    historia: str

# rota principal para gerar o personagem
@app.route('/criar-personagem', methods=['POST']) # método POST para criar personagem
def criar_personagem(): 
    dados = request.get_json() # obtém os dados JSON do corpo da requisição

    if not dados or 'descricao' not in dados: # verifica se os dados estão corretos
        return jsonify({'erro': 'Campo "descricao" ausente'}), 400 # retorna erro 400 se não houver descrição

    # cria o prompt para o modelo de linguagem para que gere o personagem
    prompt = f"""Crie um personagem fictício com base na descrição: "{dados['descricao']}".  
    O formato de resposta deve seguir este JSON:
    {{
        "nome": "Nome do personagem",
        "raca": "Raça ou espécie",
        "classe": "Classe ou profissão",
        "caracteristicas": ["característica1", "característica2"],
        "historia": "História de fundo do personagem"
    }}"""

    # chama o modelo de linguagem para gerar o personagem
    try:
        resposta = chat( 
            messages=[{'role': 'user', 'content': prompt}],
            model='gemma3',
            format='json'  # formato esperado como JSON
        )

        # verifica a estrutura da resposta
        conteudo_json = resposta['message']['content'] # acessa o conteúdo JSON da resposta
        personagem = Personagem.model_validate_json(conteudo_json) # valida o JSON com o modelo Pydantic
        
        # retorna o personagem gerado como resposta JSON
        return jsonify(personagem.dict())

    except Exception as e: # captura qualquer erro durante a geração do personagem
        return jsonify({'erro': 'Erro ao gerar personagem', 'detalhes': str(e)}), 500 # retorna erro 500 se houver falha na geração

# rota para servir o arquivo HTML estático
@app.route('/') # rota raiz
def index(): # função para servir o arquivo HTML
    return app.send_static_file('index.html') # serve o arquivo index.html

if __name__ == '__main__': # verifica se o script está sendo executado diretamente
    print("Iniciando servidor Flask em http://0.0.0.0:5000") # imprime mensagem de inicialização do servidor
    app.run(host='0.0.0.0', port=5000, debug=True) # inicia o servidor Flask na porta 5000 com debug ativado
