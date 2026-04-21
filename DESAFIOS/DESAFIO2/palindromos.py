def es_palindromo(valor):
    texto = str(valor).lower().replace(" ", "")
    return texto == texto[::-1]


print(es_palindromo("Ama"))             
print(es_palindromo("Anita lava la tina"))  
print(es_palindromo("Reconocer"))      