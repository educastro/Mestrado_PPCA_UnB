par,impar = input().split()

par = int(par)
impar = int(impar)

if impar == 0:
    print(str(par) + " " + str(impar) + " " + "errados")
elif par - impar == 0 or par - impar == -1:
    print(str(par) + " " + str(impar) + " " + "ok")
else:
    print(str(par) + " " + str(impar) + " " + "errados")