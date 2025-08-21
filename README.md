Simulador Bancário com Python e Flask
Projeto
O Simulador Bancário é uma aplicação web desenvolvida para simular as operações essenciais de um sistema bancário digital. Construído com Python e o microframework Flask, o projeto serve como um excelente exemplo prático do uso de tecnologias web para criar aplicações robustas e escaláveis.
A arquitetura do projeto segue o padrão Application Factory, que promove um código mais limpo, organizado e modular, facilitando a manutenção e a adição de novas funcionalidades no futuro.
Funcionalidades Principais
✅ Cadastro de Usuários: Sistema seguro para registro de novos clientes.
🔐 Autenticação: Login e logout para acesso à área pessoal da conta.
🏦 Simulação de Contas Bancárias: Criação e gerenciamento de contas digitais.
📄 Estrutura de Banco de Dados: Modelo relacional definido em estrutura_do_bd.txt.
💻 Interface Web: Interface de usuário simples e intuitiva para interação com o sistema.
Tecnologias Utilizadas
Este projeto foi construído utilizando as seguintes tecnologias:
Backend: Python 3.9+
Framework: Flask
Banco de Dados: SQLite (com suporte para outros bancos via SQLAlchemy)
ORM: Flask-SQLAlchemy
Autenticação: Flask-Login
Frontend: HTML, CSS
Estrutura do Projeto
A estrutura de diretórios foi pensada para garantir a modularidade e organização do código:
Simulador-bancario/
│
├── main.py                 # Ponto de entrada da aplicação (Inicializador)
├── estrutura_do_bd.txt     # Documentação da estrutura do banco de dados
├── requirements.txt        # Lista de dependências do projeto
│
└── website/                # Pacote principal da aplicação
    │
    ├── __init__.py         # Application Factory (função create_app())
    ├── routes.py           # Definição das rotas e views da aplicação
    ├── models.py           # Modelos de dados (tabelas do banco)
    │
    ├── static/             # Arquivos estáticos (CSS, JS, imagens)
    │   └── styles.css
    │
    └── templates/          # Arquivos HTML para a interface
        ├── base.html
        ├── login.html
        └── home.html


🔧 Pré-requisitos
Antes de começar, certifique-se de ter as seguintes ferramentas instaladas em sua máquina:
Python 3.9+
Git
pip (gerenciador de pacotes Python)
📦 Instalação e Execução
Siga os passos abaixo para executar o projeto localmente:
Clone o repositório:
git clone https://github.com/usuario/Simulador-bancario.git


Acesse o diretório do projeto:
cd Simulador-bancario


Crie e ative um ambiente virtual (recomendado):
# Para Windows
python -m venv venv
.\venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate


Instale as dependências:
Se houver um arquivo requirements.txt, execute:
pip install -r requirements.txt

Caso contrário, instale as bibliotecas principais manualmente:
pip install flask flask_sqlalchemy flask_login


Execute a aplicação:
python main.py


Acesse o sistema:
Abra seu navegador e acesse http://127.0.0.1:5000
🗄️ Banco de Dados
O projeto utiliza SQLite como banco de dados padrão, o que simplifica a configuração inicial, pois nenhum servidor de banco de dados externo é necessário. O arquivo do banco será criado automaticamente na pasta do projeto.
A estrutura completa das tabelas, colunas e relacionamentos está documentada no arquivo estrutura_do_bd.txt. Graças ao SQLAlchemy, o sistema pode ser facilmente adaptado para outros bancos de dados relacionais, como PostgreSQL ou MySQL.
📂 Detalhes do Código
main.py: Ponto de entrada que importa e executa a aplicação criada pela factory create_app().
website/__init__.py: Contém a função create_app(), que configura o Flask, o banco de dados, as rotas e outras extensões.
website/routes.py: Define as rotas principais da aplicação, como a página inicial e o painel do usuário.
website/models.py: Contém as classes que representam as tabelas do banco de dados (ex: User, Account).
website/templates/: Armazena os arquivos HTML que compõem a interface do usuário.
website/static/: Contém os arquivos estáticos, como folhas de estilo (CSS) e JavaScript.
👨‍💻 Autor
Samuel - Gustavo -Enzo
GitHub: https://github.com/Enzoc2/Simulador-bancario.git
