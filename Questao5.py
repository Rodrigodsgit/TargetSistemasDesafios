def inverte_string(string):
    string_invertida = ''
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

string = input("Digite uma string: ")
string_invertida = inverte_string(string)
print(string_invertida)