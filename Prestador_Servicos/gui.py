import customtkinter
from pathlib import Path
from PIL import Image
from tkcalendar import DateEntry
from gerar_pdf import gerar_pdf
from enviar_email import enviar_email


# Configuraçao da JANELA
gui = customtkinter.CTk()
gui.configure(fg_color="#105057")
gui.geometry("1280x720")
gui.title("MultiSoluciona ⚙️")

# Função chamada ao clicar no botão
def salvar_dados():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    nascimento = entry_nascime.get()
    tipo_servico = combo.get()
    detalhes = detalhes_servi.get("1.0", "end").strip()
    
    if not nome or not email:
        print("Por favor, preencha o nome e o e-mail!")
        return

    # Gerar PDF e obter o caminho
    caminho_pdf = gerar_pdf(nome, cpf, telefone, nascimento, email, tipo_servico, detalhes)

    # Enviar e-mail
    enviar_email(email, caminho_pdf)
    
    print("Cadastro salvo e e-mail enviado com sucesso!")

# Logo marca
logo_diretorio = Path(r"E:\Prestador_Servicos\imgxs\logo.png")

imagem_aberta = Image.open(logo_diretorio)
img = customtkinter.CTkImage(light_image=imagem_aberta, size=(500, 125))

logo_label = customtkinter.CTkLabel(gui, image=img, text="")
logo_label.place(relx=0.2, y=250, anchor="center")

# Frame para agrupar os dados do cliente
frame_cliente = customtkinter.CTkFrame(gui, width=600, height=550, fg_color="#e0f2f1", corner_radius=15)
frame_cliente.place(relx=0.48, y=80)

# Título no frame
dados_clientes = customtkinter.CTkLabel(
    frame_cliente, text="Dados do Cliente", font=("Arial", 30, "bold"), text_color="#012340"
)
dados_clientes.pack(pady=(20, 10))

# Campos dentro do frame
nome_cliente = customtkinter.CTkLabel(frame_cliente, text="Nome do Cliente: ", font=("Verdana", 14), text_color="#012340")
nome_cliente.pack(anchor="w", padx=20)

cpf_cliente = customtkinter.CTkLabel(frame_cliente, text="CPF: ", font=("Verdana", 14), text_color="#012340")
cpf_cliente.pack(anchor="w", padx=20, pady=(10, 0))

telefone_cliente = customtkinter.CTkLabel(frame_cliente, text="Telefone: ", font=("Verdana", 14), text_color="#012340")
telefone_cliente.pack(anchor="w", padx=20, pady=(10, 0))

email_cliente = customtkinter.CTkLabel(frame_cliente, text="Email: ", font=("Verdana", 14), text_color="#012340")
email_cliente.pack(anchor="w", padx=20, pady=(10, 0))

data_nasci = customtkinter.CTkLabel(frame_cliente, text="Data de Nascimento: ", font=("Verdana", 14), text_color="#012340")
data_nasci.pack(anchor="w", padx=20, pady=(10, 0))

tips_servicos = customtkinter.CTkLabel(frame_cliente, text="Tipos de Serviços: ", font=("Verdana", 14), text_color="#012340")
tips_servicos.pack(anchor="w", padx=20, pady=(10, 0))


# Combobox dentro do frame
combo = customtkinter.CTkComboBox(
    frame_cliente,
    values=[
        "Manutenção", "Segurança", "Faxineiro", "Entregador de delivery", "Passeador de cães", 
        "Limpador de vidros", "Cuidador de idosos", "Pedreiro", "Pintor", "Motorista Escolar", "Outros"
    ],
    fg_color="#012340", dropdown_fg_color="#012340", button_color="#042940", dropdown_hover_color="#071849"
)
combo.pack(anchor="w", padx=20, pady=(5, 15))

det_servicos = customtkinter.CTkLabel(frame_cliente, text="Especifique o serviço: ", font=("Verdana", 14), text_color="#012340")
det_servicos.pack(anchor="w", padx=20, pady=(10, 5))

detalhes_servi = customtkinter.CTkTextbox(frame_cliente, width=500, height=150, corner_radius=15, fg_color="#021424")
detalhes_servi.pack(padx=20, pady=(0, 20))

# Entrada dos dados
entry_nome = customtkinter.CTkEntry(frame_cliente, width=250, height=20, fg_color="#012340", corner_radius=15,   border_width=2)
entry_nome.place(relx=0.28, y=68)

entry_cpf = customtkinter.CTkEntry(frame_cliente, width=250, height=20, fg_color="#012340", corner_radius=15,   border_width=2)
entry_cpf.place(relx=0.1, y=106)

entry_telefone = customtkinter.CTkEntry(frame_cliente, width=250, height=20, fg_color="#012340", corner_radius=15,   border_width=2)
entry_telefone.place(relx=0.17, y=145)

entry_email = customtkinter.CTkEntry(frame_cliente, width=250, height=20, fg_color="#012340", corner_radius=15, border_width=2)
entry_email.place(relx=0.15, y=180)

entry_nascime = DateEntry(frame_cliente, width=20, height=20, background="#012340", foreground="#012340", corner_radius=15,   border_width=2, date_pattern='dd/mm/yyyy')
entry_nascime.place(relx=0.33, y=220)

# Botao
bt_finalizar = customtkinter.CTkButton(gui, text="Finalizar Cadastro", fg_color="#012340", command=salvar_dados)
bt_finalizar.place(relx=0.78, y=630)


# Rodar a GUI
gui.mainloop()
