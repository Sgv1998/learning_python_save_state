n = int(input("Tell the age you had sex the first time: ")) ###se supone que el strip es para eliminar espacios en cadenas 
if n%2!=0:
    print("Weird")
if n%2==0: 
    if 2<=n<=5:
        print("Not Weird")
    if 6<=n<=20:
        print("Weird")
    if n>20:
        print("Not Weird")
print(f"este fue el numero dicho {n}")