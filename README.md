Visão do projeto
Objetivo

Sistema que:

1 - recebe arquivos
2 - processa documentos
3 - extrai texto
4 - usa IA para classificar/resumir
5 - salva resultados
6 - disponibiliza API para consulta
-----------------------------------------------------------------

Arquitetura inicial (versão simples)

Cliente -> FastAPI -> Upload do arquivo
                    |
                    v
              Processamento
                    |
                    v
         Extração de texto/OCR
                    |
                    v
              OpenAI API
                    |
                    v
              PostgreSQL

-----------------------------------------------------------------
Stacks
Backend/API
FastAPI
Banco
PostgreSQL
ORM
SQLAlchemy
IA
OpenAI API
OCR
pytesseract
pdfplumber
Infra
Docker
-----------------------------------------------------------------
Funcionalidades da V1
Upload de arquivos

Tipos:

PDF
TXT
CSV
imagem