import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import os

def enviar_email(destinatario, caminho_pdf):
    remetente = "gustavoconfi.18@gmail.com"
    senha = "jgfj hmgo odjb hnos"  # sua senha de app gerada no Google

    # Criar o e-mail
    mensagem = MIMEMultipart()
    mensagem["From"] = remetente
    mensagem["To"] = destinatario
    mensagem["Subject"] = "Cadastro - MultiSoluciona"

    corpo = MIMEText("Segue em anexo o PDF com os dados do seu cadastro.", "plain")
    mensagem.attach(corpo)

    # Anexar o PDF
    with open(caminho_pdf, "rb") as arquivo_pdf:
        anexo = MIMEApplication(arquivo_pdf.read(), _subtype="pdf")
        anexo.add_header("Content-Disposition", "attachment", filename=os.path.basename(caminho_pdf))
        mensagem.attach(anexo)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
            servidor.login(remetente, senha)
            servidor.send_message(mensagem)
            print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
