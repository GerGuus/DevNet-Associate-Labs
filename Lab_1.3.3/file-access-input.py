file = open("devices.txt", "a")

while True:
    newItem = input("Enter device name: ")
    if newItem.lower() == "exit":
        print("All done!")
        break
    file.write(newItem + "\n")

file.close()