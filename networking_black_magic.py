def networking_fuckery():
    IP = input("Enter an IP Address: ")
    IP = IP.split(".")
    bin = ""
    for dec in IP:
        bin += format(int(dec), 'b').zfill(8)
    print(int(bin, 2))
    print()
    networking_fuckery()
networking_fuckery()