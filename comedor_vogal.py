
palavra_usuario = input("Digite uma palavra: ")


palavra_usuario = palavra_usuario.upper()


palavra_sem_vogais = ""


for letra in palavra_usuario:


    if letra == "A":
        continue    
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
       
        palavra_sem_vogais += letra


print(palavra_sem_vogais)
