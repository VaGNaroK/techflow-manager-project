# LogiTask — Sistema de Gerenciamento Ágil para Logística

O **LogiTask** é um sistema web leve desenvolvido para a *LogiExpress*, uma empresa de logística que necessitava centralizar e acompanhar o fluxo de suas demandas operacionais em tempo real (como triagem de cargas, alocação de motoristas e rotas de entrega). 

O projeto simula um ciclo completo de Engenharia de Software, aplicando conceitos de desenvolvimento ágil (Kanban), versionamento, modelagem UML, controle de qualidade (CI/CD).

---

## Arquitetura e Tecnologias Utilizadas

A aplicação foi projetada seguindo os padrões da engenharia de software, separando as responsabilidades entre a camada de dados (Model) e o controlador de rotas HTTP.

*   **Linguagem Principal:** Python 3.11
*   **Framework Web:** Flask (utilizado para criar uma API estável, rápida e minimalista para o ciclo CRUD)
*   **Persistência de Dados:** Estrutura de dados em memória (Dicionário nativo), otimizada para o escopo de validação do protótipo ágil.
*   **Ambiente Operacional Recomendado:** Linux Mint / Ubuntu

---

## Bibliotecas e Dependências

As dependências do projeto estão centralizadas no arquivo `requirements.txt`:
*   `Flask==3.0.3`: Núcleo da API web e gerenciamento de requisições HTTP.
*   `pytest==8.2.2`: Framework focado em testes automatizados e controle de qualidade.

---

## Estrutura de Diretórios

O projeto segue uma estrutura organizacional clara, separando o código de produção, os testes e as documentações técnicas:

```text
techflow-task-manager/
├── .github/
│   └── workflows/
│       └── ci.yml          # Configuração do Pipeline de CI/CD (GitHub Actions)
├── docs/
│   ├── caso_de_uso.png    # Diagrama de Casos de Uso UML
│   └── diagrama_classes.png
├── src/
│   ├── __init__.py
│   ├── app.py             # Servidor Flask e rotas da API
│   └── models.py          # Modelo de dados da entidade Task
├── tests/
│   ├── __init__.py
│   └── test_app.py        # Suíte de testes unitários automatizados
├── .gitignore
├── README.md              # Documentação principal do projeto
└── requirements.txt       # Arquivo de dependências

## Como Instalar e Executar

Siga os passos abaixo para executar o projeto localmente. As instruções cobrem sistemas operacionais Linux/macOS e Windows.

### 1. Clonar o Repositório

```bash
git clone https://github.com/VaGNaroK/techflow-manager-project.git
cd techflow-manager-project
```

### 2. Criar e Ativar o Ambiente Virtual (Recomendado)

**No Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**No Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 3. Instalar as Dependências

Com o ambiente virtual ativado, instale os pacotes necessários:

```bash
pip install -r requirements.txt
```

### 4. Executar o Servidor

**No Linux/macOS:**
```bash
python3 src/app.py
```

**No Windows:**
```powershell
python src/app.py
```

O servidor iniciará e a interface Kanban estará disponível no endereço local: `http://127.0.0.1:5000/`.