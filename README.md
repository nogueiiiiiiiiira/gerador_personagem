# 🧙‍♂️ Gerador de Personagens com Flask + Ollama

Este é um projeto web simples que utiliza **Flask** e **Ollama** para gerar personagens fictícios baseados em uma descrição fornecida pelo usuário. A interface é feita com HTML, JavaScript e Bootstrap para uma melhor experiência.

---

## Tecnologias utilizadas

- Python 3.11+  
- [Flask](https://flask.palletsprojects.com/) – framework web  
- [Ollama](https://ollama.com/) – execução local de modelos LLM  
- [Pydantic](https://docs.pydantic.dev/) – validação de dados  
- HTML, CSS, JavaScript e [Bootstrap](https://getbootstrap.com/) para o frontend

---

## Como usar

### Pré-requisitos

- Instale o Python 3.11 ou superior: https://www.python.org/downloads/
- Instale e configure o Ollama: https://ollama.com/

### Passos para rodar o projeto

1. Clone ou baixe este repositório e navegue até a pasta do projeto no terminal.

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências necessárias:

```bash
pip install flask ollama pydantic
```

4. Execute o servidor Flask:

```bash
python app.py
```

5. Abra o navegador e acesse:

```
http://localhost:5000
```

6. Na página aberta, digite a descrição do personagem e clique em "Gerar" para ver o resultado.

---

## Observações

- Certifique-se de que o Ollama está instalado e funcionando corretamente para que a geração do personagem funcione.
- O servidor Flask está configurado para rodar no host `0.0.0.0` e porta `5000`.
- A interface utiliza Bootstrap para melhor responsividade e aparência.
