# Importa o módulo 'requests', que será utilizado para fazer requisições HTTP.
import requests

# Define uma função chamada 'get_address_details' que recebe um CEP como argumento.
def get_address_details(cep):
    
    # Constrói a URL para a requisição à API do ViaCEP usando o CEP fornecido como parte da URL.
    url = f"https://viacep.com.br/ws/{cep}/json/"

    # Faz uma requisição GET para a URL construída e armazena a resposta na variável 'response'.
    response = requests.get(url)

    # Extrai os dados JSON da resposta da requisição e os armazena na variável 'data'.
    data = response.json()

    # Retorna os dados do endereço obtidos da API.
    return data

# Verifica se o script está sendo executado como o programa principal.
if __name__ == "__main__":

    # Solicita ao usuário que digite um CEP e armazena o valor na variável 'cep'.
    cep = input("Digite o CEP: ")

    # Chama a função 'get_address_details' passando o CEP como argumento e armazena os dados do endereço retornados na variável 'address_data'.
    address_data = get_address_details(cep)

    # Imprime os dados do endereço na saída padrão.
    print(address_data)
