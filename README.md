
# Prestador de Serviços

Sistema desktop com interface gráfica desenvolvido em Python, voltado para profissionais autônomos que desejam cadastrar clientes e gerar recibos em PDF com facilidade. Também permite o envio automático do recibo por e-mail.

## ✨ Funcionalidades

- Interface gráfica intuitiva feita com Tkinter  
- Formulário para cadastro de clientes e serviços  
- Geração automática de recibo em PDF com dados preenchidos  
- Envio do PDF por e-mail diretamente pelo sistema  
- Armazenamento automático dos arquivos PDF em uma pasta local  

## 🖥️ Interface

A interface principal permite:  
- Inserção de nome, serviço prestado, valor e data de vencimento  
- Geração do PDF com base nas informações inseridas  
- Envio do PDF para o e-mail do cliente informado  

## 📂 Estrutura do Projeto

```
Prestador_Servicos/
├── gui.py                 # Interface principal com Tkinter
├── gerar_pdf.py          # Função para criação do PDF com ReportLab
├── enviar_email.py       # Função para envio do PDF por e-mail
├── imgxs/logo.png        # Logotipo utilizado no cabeçalho do PDF
└── pdfs/                 # Pasta onde os PDFs gerados são armazenados
```

## ▶️ Como Executar

1. Clone o repositório ou extraia os arquivos.  
2. Instale as dependências:  
   ```bash
   pip install reportlab
   ```
3. Execute o programa:  
   ```bash
   python gui.py
   ```

## ✉️ Configuração de E-mail

O arquivo `enviar_email.py` utiliza `smtplib` e requer uma conta de e-mail com autenticação SMTP habilitada.  

No topo do arquivo `enviar_email.py`, configure as credenciais:

```python
remetente = "seuemail@gmail.com"
senha = "sua_senha_de_aplicativo"
```

> ⚠️ Recomendado utilizar uma senha de aplicativo (ex.: Gmail com autenticação em duas etapas).

## 📦 Dependências

- `tkinter` – Interface gráfica  
- `reportlab` – Criação de arquivos PDF  
- `smtplib`, `email` – Envio de e-mails  
- `os`, `datetime`, `tempfile` – Utilitários padrão do Python  

## 📑 Exemplo de PDF

O recibo gerado contém:  
- Nome do cliente  
- Serviço prestado  
- Valor  
- Data de vencimento  

Arquivos gerados são salvos automaticamente na pasta `pdfs/`.

## 📄 Licença

Este projeto está licenciado sob os termos da licença MIT.

---

Desenvolvido para facilitar a vida do prestador de serviços que deseja um sistema simples, eficiente e funcional.
