import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Função para gerar o PDF dentro da pasta "pdfs"
def gerar_pdf(nome, cpf, telefone, nascimento, email, tipo_servico, detalhes):
    diretorio = "pdfs"
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    pdf_file = os.path.join(diretorio, f"{nome}_cadastro.pdf")
    
    c = canvas.Canvas(pdf_file, pagesize=A4)
    largura, altura = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, altura - 50, "Cadastro do Cliente - MultiSoluciona")

    c.setFont("Helvetica", 12)
    c.drawString(50, altura - 100, f"Nome: {nome}")
    c.drawString(50, altura - 130, f"CPF: {cpf}")
    c.drawString(50, altura - 160, f"Telefone: {telefone}")
    c.drawString(50, altura - 190, f"Email: {email}")
    c.drawString(50, altura - 220, f"Data de Nascimento: {nascimento}")
    c.drawString(50, altura - 250, f"Tipo de Serviço: {tipo_servico}")

    c.drawString(50, altura - 280, "Detalhes do Serviço:")
    text = c.beginText(50, altura - 300)
    text.setFont("Helvetica", 11)
    for linha in detalhes.split('\n'):
        text.textLine(linha)
    c.drawText(text)

    c.save()
    print(f"PDF salvo em: {pdf_file}")
    return pdf_file