#1. Data Check-up (Patient ke vitals check karne jaisa):
#pd.read_csv() / pd.read_excel(): Bahar se file ko code mein laane ke liye.
#df.head(): Data ke shuruwati 5 rows dekhne ke liye (taaki pata chale data kaisa dikhta hai).
#df.info(): Data mein kitne rows/columns hain aur koi value missing toh nahi.
#df.describe(): Saare numbers ka math ek second mein dekhne ke liye (jaise average age, max bill).

#2. Data Cleaning (Kachra hatana):
#df.fillna(): Khali jagah (missing values) ko kisi number se bharne ke liye (jo humne day 1 par kiya tha).
#df.dropna(): Agar koi row poori kharab hai, toh usko delete karne ke liye.
#df.drop_duplicates(): Duplicate entry ko hatane ke liye.

#3. The Surgeon's Scalpel (Data ko kaatna aur filter karna):
#df[df['Column'] == 'Value']: Specific data nikalna (jo aaj tumne 'Emergency' filter karne ke liye kiya).
#df.loc[] / df.iloc[]: Kisi specific row ya column ko uske number ya naam se nikalna.

#4. The Manager's Dashboard (Report banana):
#df.groupby(): Data ko group karna (jo aaj ke Pie Chart wale challenge mein hum use kar rahe hain).
#pd.merge(): Do alag-alag tables ko aapas mein jodna (jaise Vitals ki table aur Billing ki table).
#df.to_csv(): Clean kiye hue data ko wapas ek nayi excel/csv file banakar computer mein save karna.
#print(df.isnull().sum()) #(Yeh command tumhe bata dega ki Age mein kitne blanks hain aur Bill mein kitne).
#df = df.dropna()  #yeh kachra poora ka poora delete karna hai.
#Iske liye dropna() function ka use karo jo poori row uda dega.