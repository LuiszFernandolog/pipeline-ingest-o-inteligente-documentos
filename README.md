Pipeline de Ingestão Inteligente de Documentos

Sistema de ingestão inteligente de documentos desenvolvido com Python e FastAPI, capaz de:

realizar upload de arquivos
extrair texto de PDFs
utilizar IA para análise de documentos
retornar classificação e resumo do conteúdo
Tecnologias utilizadas
Python
FastAPI
Uvicorn
OpenAI API
pdfplumber
python-dotenv
Arquitetura do projeto
app/
├── api/
│   └── upload.py
│
├── services/
│   ├── upload_service.py
│   ├── pdf_service.py
│   └── ai_service.py
│
├── uploads/
│
└── main.py
Funcionalidades
Upload de documentos

Realiza upload de arquivos PDF através da API.

Extração de texto

Extrai automaticamente o texto do PDF utilizando pdfplumber.

Análise com IA

Utiliza a OpenAI API para:

classificar documentos
gerar resumo
identificar principais tópicos
Fluxo da aplicação
Upload PDF
    ↓
Salvar arquivo
    ↓
Extrair texto
    ↓
Analisar com IA
    ↓
Retornar resultado
Como executar o projeto
1. Clonar o repositório
git clone https://github.com/LuiszFernandolog/pipeline-ingest-o-inteligente-documentos.git
2. Entrar na pasta
cd pipeline-ingest-o-inteligente-documentos
3. Criar ambiente virtual
Windows
python -m venv venv
venv\Scripts\activate
Linux/Mac
python3 -m venv venv
source venv/bin/activate
4. Instalar dependências
pip install -r requirements.txt
Configuração da OpenAI

Crie um arquivo .env na raiz do projeto:

OPENAI_API_KEY=sua_api_key
Executando a aplicação
uvicorn app.main:app --reload

A API ficará disponível em:

http://127.0.0.1:8000
Swagger da API

Documentação automática:

http://127.0.0.1:8000/docs
Exemplo de resposta
{
  "filename": "documento.pdf",
  "saved_at": "app/uploads/documento.pdf",
  "text_preview": "Texto extraído do documento...",
  "ai_analysis": "Categoria: Contrato\nResumo: ..."
}
Melhorias futuras
PostgreSQL
Docker
OCR para PDFs escaneados
Processamento assíncrono
Filas com RabbitMQ/Kafka
Integração com Azure Blob Storage
Integração com AWS S3
Autenticação JWT
RAG (Retrieval-Augmented Generation)
Objetivo do projeto

Este projeto foi desenvolvido com foco em:

aprendizado de APIs com FastAPI
arquitetura backend
engenharia de dados
integração com IA
processamento inteligente de documentos
Autor

Luis Fernando