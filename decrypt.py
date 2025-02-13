message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption")
if "1234" == pas:
    for i in range(len(message)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:hello")
else:
    print("YOU ARE NOT auth")
