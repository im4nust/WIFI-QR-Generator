# Importa le librerie necessarie
import qrcode
import qrcode.constants
import tkinter as tk
from tkinter import ttk, messagebox
import os
import re # Per pulire l'SSID per il nome del file

# Assicurati di avere installato qrcode e Pillow: pip install qrcode Pillow

def genera_qr_code_wifi(ssid, password, tipo_sicurezza, nascosta=False, nome_file="qr_code.png"):
    """Genera un QR code per connettersi a una rete WiFi."""
    # Formato standard per i QR code WiFi
    tipo_sicurezza = tipo_sicurezza.upper()
    dati_wifi = f"WIFI:T:{tipo_sicurezza};S:{ssid};P:{password};"
    if nascosta:
        dati_wifi += "H:true;"

    # Crea e configura il QR code
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(dati_wifi)
    qr.make(fit=True)

    # Crea l'immagine e salva
    img = qr.make_image(fill_color="black", back_color="white")
    try:
        img.save(nome_file)
        return True, f"QR code salvato come '{os.path.basename(nome_file)}' nella cartella corrente."
    except Exception as e:
        return False, f"Errore salvataggio file '{os.path.basename(nome_file)}': {e}"

def genera_e_salva_qr():
    """Legge i dati dalla GUI, genera e salva il QR code con nome basato sull'SSID."""
    ssid = entry_ssid.get()
    password = entry_password.get()
    tipo_sicurezza = combo_sicurezza.get()
    nascosta = var_nascosta.get()

    if not ssid or not tipo_sicurezza:
        messagebox.showwarning("Input mancante", "Inserisci SSID e Tipo Sicurezza.")
        return

    # Crea un nome file valido dall'SSID
    nome_file_base = re.sub(r'[^\w\s-]', '', ssid)
    nome_file_base = nome_file_base.replace(' ', '_')
    nome_file_base = re.sub(r'_+', '_', nome_file_base).strip('_')
    if not nome_file_base:
        nome_file_base = "wifi_qr_code"

    nome_file_png = f"{nome_file_base}.png"
    percorso_file_completo = os.path.join(os.getcwd(), nome_file_png)

    # Genera e salva il QR code
    success, messaggio = genera_qr_code_wifi(ssid, password, tipo_sicurezza, nascosta, percorso_file_completo)

    # Mostra messaggio all'utente
    if success:
        messagebox.showinfo("Successo", messaggio)
    else:
        messagebox.showerror("Errore", messaggio)

# --- Interfaccia grafica ---
root = tk.Tk()
root.title("Generatore QR Code WiFi")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Campi input
ttk.Label(frame, text="Nome Rete (SSID):").grid(row=0, column=0, sticky=tk.W, pady=5, padx=5)
entry_ssid = ttk.Entry(frame, width=40)
entry_ssid.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)

ttk.Label(frame, text="Password:").grid(row=1, column=0, sticky=tk.W, pady=5, padx=5)
entry_password = ttk.Entry(frame, width=40, show="*")
entry_password.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)

ttk.Label(frame, text="Tipo Sicurezza:").grid(row=2, column=0, sticky=tk.W, pady=5, padx=5)
tipi_sicurezza = ['WPA', 'WEP', 'nopass']
combo_sicurezza = ttk.Combobox(frame, values=tipi_sicurezza, state="readonly")
combo_sicurezza.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
combo_sicurezza.set('WPA')

var_nascosta = tk.BooleanVar()
ttk.Checkbutton(frame, text="Rete Nascosta", variable=var_nascosta).grid(row=3, column=0, columnspan=2, sticky=tk.W, pady=5, padx=5)

# Pulsante
ttk.Button(frame, text="Genera QR Code", command=genera_e_salva_qr).grid(row=4, column=0, columnspan=2, pady=10)

frame.columnconfigure(1, weight=1)

root.mainloop()

# --- Esecuzione ---
# 1. Salva il codice come WIFI_QR.py.
# 2. Installa le librerie: pip install qrcode Pillow
# 3. Esegui da terminale: python WIFI_QR.py
