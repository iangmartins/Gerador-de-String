import numpy as np

# Definindo as listas de caracteres possíveis
lowercase_letters = list("abcdefghijklmnopqrstuvwxyz")
uppercase_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# Pensei em deixar assim: uppercase_letters = [char.upper() for char in lowercase_letters], apesar de ser mais compacto me deixa mais restrito, então preferi escrever as letras tudo denovo
digits = list("0123456789")
special_characters = list('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')

# Juntando todas as listas em uma lista única
all_chars = [lowercase_letters, uppercase_letters, digits, special_characters]

# Inicializando a lista de caracteres resultante vazia
res = []

# Loop para adicionar caracteres aleatórios
for x in range(15):
    # Escolhendo uma categoria aleatória de caracteres
    category = np.random.randint(4)
    
    # Escolhendo um caractere aleatório da categoria correspondente
    char = np.random.choice(all_chars[category])
    res.append(char)

# Convertendo a lista de caracteres em uma string
ans = "".join(res)

# Imprimindo o resultado
print(ans)

# Esperando a entrada do usuário para sair
input('Press ENTER to exit')