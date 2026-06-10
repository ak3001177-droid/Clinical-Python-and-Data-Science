import os
import shutil
if os.path.exists("Text_Reports"):
    print("Text_Reports folder already exists")
else:
    os.makedirs("Text_Reports")

if os.path.exists("Image_Scans"):
    print("Image_Scans folder already exists")
else:
    os.makedirs("Image_Scans")


if os.path.exists("mix_data"):
    for file in os.listdir("mix_data"):
        if file.endswith(".txt"):
            print(f"Text file detected: {file}")
            shutil.move(os.path.join("mix_data", file), "Text_Reports")
        if file.endswith(".jpg"):
            print(f"Image file detected: {file}")
            shutil.move(os.path.join("mix_data", file), "Image_Scans")
