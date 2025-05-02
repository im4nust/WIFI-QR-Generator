# **Generatore QR Code WiFi**

Un semplice script Python con interfaccia grafica (Tkinter) per generare QR code che permettono di connettersi facilmente a una rete WiFi scansionando il codice.  
A simple Python script with a graphical interface (Tkinter) to generate QR codes that allow easy connection to a WiFi network by scanning the code.

## **🇮🇹 Italiano**

### **Descrizione**

Questo programma crea un'interfaccia utente grafica dove è possibile inserire il nome della rete WiFi (SSID), la password e il tipo di sicurezza. Una volta inseriti i dati e cliccato sul pulsante "Genera QR Code", viene generato un file immagine PNG contenente il QR code. Scansionando questo codice con la fotocamera di uno smartphone o tablet, il dispositivo potrà connettersi automaticamente alla rete specificata senza dover digitare la password.  
Il nome del file PNG generato sarà basato sull'SSID inserito (caratteri speciali e spazi verranno sostituiti o rimossi per creare un nome file valido) e verrà salvato nella stessa cartella in cui viene eseguito lo script.

### **Prerequisiti**

Assicurati di avere Python installato (versione 3.6 o superiore raccomandata).

### **Installazione**

Il programma richiede le librerie qrcode e Pillow. Puoi installarle facilmente utilizzando pip e il file requirements.txt fornito:

1. Salva il contenuto del requirements.txt nella stessa cartella dello script Python.  
2. Apri il terminale o il prompt dei comandi nella cartella del progetto.  
3. Esegui il seguente comando:  
   pip install \-r requirements.txt

### **Utilizzo**

1. Salva lo script Python (ad esempio, genera\_qr\_gui.py) nella stessa cartella dove hai salvato requirements.txt.  
2. Apri il terminale o il prompt dei comandi nella cartella del progetto.  
3. Esegui lo script con il comando:  
   python genera\_qr\_gui.py

4. Si aprirà una finestra. Inserisci il Nome Rete (SSID), la Password, seleziona il Tipo Sicurezza (solitamente WPA) e spunta "Rete Nascosta" se applicabile.  
5. Clicca sul pulsante "Genera QR Code".  
6. Il file PNG del QR code verrà salvato automaticamente nella stessa cartella con un nome basato sull'SSID.

### **File di Output**

Il file generato sarà un'immagine PNG (es. Nome\_Della\_Tua\_Rete.png) contenente il QR code. Puoi aprirlo e mostrarlo sui tuoi dispositivi per una facile connessione.

## **🇬🇧 English**

### **Description**

This program creates a graphical user interface where you can enter the WiFi network name (SSID), password, and security type. Once you've entered the data and clicked the "Genera QR Code" button, a PNG image file containing the QR code will be generated. By scanning this code with a smartphone or tablet camera, the device can automatically connect to the specified network without needing to type the password.  
The name of the generated PNG file will be based on the entered SSID (special characters and spaces will be replaced or removed to create a valid filename) and will be saved in the same folder where the script is executed.

### **Prerequisites**

Make sure you have Python installed (version 3.6 or higher recommended).

### **Installation**

The program requires the qrcode and Pillow libraries. You can easily install them using pip and the provided requirements.txt file:

1. Save the content of requirements.txt in the same folder as your Python script.  
2. Open your terminal or command prompt in the project folder.  
3. Run the following command:  
   pip install \-r requirements.txt

### **Usage**

1. Save the Python script (e.g., genera\_qr\_gui.py) in the same folder where you saved requirements.txt.  
2. Open your terminal or command prompt in the project folder.  
3. Run the script using the command:  
   python genera\_qr\_gui.py

4. A window will open. Enter the Network Name (SSID), Password, select the Security Type (usually WPA), and check "Rete Nascosta" (Hidden Network) if applicable.  
5. Click the "Genera QR Code" button.  
6. The QR code PNG file will be automatically saved in the same folder with a name based on the SSID.

### **Output File**

The generated file will be a PNG image (e.g., Your\_Network\_Name.png) containing the QR code. You can open it and display it on your devices for easy connection.