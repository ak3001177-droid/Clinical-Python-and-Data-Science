import os

# Pehle current location print karo
print("Main abhi yahan hu:", os.getcwd())

# Ab us location ke andar ka saara saamaan list karo
print("Yahan yeh sab rakha hai:", os.listdir())
os.mkdir("naya_folder")  # Ek naya folder banao
print("Naya folder banaya gaya hai!")
os.rmdir("naya_folder")  # only empty folder ko delete kar sakte hain
print("Folder successfully udd gaya!")