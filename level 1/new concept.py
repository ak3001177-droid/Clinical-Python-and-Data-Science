try:
    with open("fake_data.txt", "r") as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("System Alert: file missing or deleted by admin!")