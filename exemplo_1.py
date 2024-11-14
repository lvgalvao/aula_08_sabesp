import csv

# Caminho para o arquivo CSV
caminho_arquivo: str = 'data/exemplo.csv'

# Inicializa uma lista vazia para armazenar os dados
dados: list = []

# Usa o gerenciador de contexto `with` para abrir o arquivo
with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
    # Cria um objeto leitor de CSV
    leitor_csv = csv.DictReader(arquivo)
    print(type(leitor_csv))
    print(leitor_csv)
    
    # Itera sobre as linhas do arquivo CSV
    for linha in leitor_csv:
        # Adiciona cada linha (um dicionário) à lista de dados
        dados.append(linha)

# Exibe os dados lidos do arquivo CSV
print(dados)

pessoa_4 = {
    'nome': 'Luciano', 'idade': '34', 'cidade': 'Rio de Janeiro'
}

dados.append(pessoa_4)

print(dados)


