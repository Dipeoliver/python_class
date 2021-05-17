
frase = "Teste para descobrir qual palavra aaaaaaaaa sera a maior deste contesto"
frase = frase.split()
maior_palavra= max(frase, key=len)     
print(f"A maior palavra e :{maior_palavra} com {(len(maior_palavra))} caracteres")
