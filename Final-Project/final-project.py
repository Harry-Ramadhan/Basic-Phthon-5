import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Fungsi mengirim email ke 1 penerima tanpa lampiran file
def kirim_email(dari,kepada,judul,isi_pesan,password):

    msg = MIMEMultipart()
    msg['From'] = dari
    msg['To'] = kepada
    msg['Subject'] = judul

    msg.attach(MIMEText(isi_pesan, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(dari, password)
    text = msg.as_string()
    server.sendmail(dari, kepada, text)
    server.quit()

# Fungsi mengirim email ke 1 penerima dengan lampiran file
def kirim_email_df(dari,kepada,judul,isi_pesan,fname,fdir,password):

    msg = MIMEMultipart()
    msg['From'] = dari
    msg['To'] = kepada
    msg['Subject'] = judul

    msg.attach(MIMEText(isi_pesan, 'plain'))
    attachment = open(fdir + fname, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % fname)
    msg.attach(part)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(dari, password)
    text = msg.as_string()
    server.sendmail(dari, kepada, text)
    server.quit()

# Mengirim email ke 1 penerima tanpa lampiran file
# buat variabel parameter dari, kepada, judul, isi_pesan, password

dari      = "harryramadhan44@gmail.com"       # email pengirim
kepada    = "harryramadhan785@gmail.com"       # email penerima
judul     = "p"       # judul atau subject
isi_pesan = '''
p


'''   # isi pesan atau body
password  = "2002Harry*"       # isi password

# menjalankan fungsi kirim email
kirim_email(dari,kepada,judul,isi_pesan,password)

# Mengirim email ke 1 penerima dengan lampiran file
# buat variabel parameter dari, kepada, judul, isi_pesan, fname, fdir, password

# email pengirim
dari = ""

# email penerima
kepada = ""

# judul atau subject
judul = ""

# isi pesan atau body
isi_pesan = ''''''

# nama file, contoh file MS word "mydoc.docx"
fname     = ""

# file directory, contoh D:/my document/file email/
fdir = ""

# isi password
password = ""

# menjalankan fungsi kirim email dengan file
kirim_email_df(dari,kepada,judul,isi_pesan,fname,fdir,password)

# Persiapan mengirim email kebanyak orang
import pandas as pd

data = pd.read_excel('file directory/file name').astype('str')

# Mengirim email ke banyak penerima tanpa lampiran file
# email pengirim
dari = ""

# judul atau subject
judul = ""

# isi password
password = ""

for i in range(len(data)):
    
    kepada    = data["email"][i]
    isi_pesan = '''''' + data["nama"][i] + ''''''
    
    kirim_email(dari,kepada,judul,isi_pesan,password)

# Mengirim email ke banyak penerima dengan lampiran file
# email pengirim
dari = ""

# judul atau subject
judul = ""

# file directory, contoh D:/my document/file email/
fdir = ""

# isi password
password = ""

for i in range(len(data)):
    
    kepada = data["email"][i]
    isi_pesan = '''''' + data["nama"][i] + ''''''
    fname     = data["file name"][i]
    
    kirim_email_df(dari,kepada,judul,isi_pesan,fname,fdir,password)

