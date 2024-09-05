def inverter_string(s):
    string_invertida = ''
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

s = input("Informe uma string: ")

print("String invertida:", inverter_string(s))

# Esse código inverte uma string manualmente, sem usar funções prontas, iterando por cada caractere da string original e adicionando-o no início da nova string.