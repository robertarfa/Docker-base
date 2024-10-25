import pandas as pd

# Cria um dicionário com dados de exemplo
data = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
    'Idade': [25, 30, 22, 28, 35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Fortaleza']
}

# Cria um DataFrame a partir do dicionário
df = pd.DataFrame(data)

# Imprime o DataFrame
print(df)

# Imprime as primeiras 3 linhas do DataFrame
print(df.head(3))

# Imprime informações básicas sobre o DataFrame
print(df.info())

# Calcula a média da coluna 'Idade'
media_idade = df['Idade'].mean()
print(f"Média de idade: {media_idade}")