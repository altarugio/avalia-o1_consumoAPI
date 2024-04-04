// Obtém o elemento HTML com o ID "search-button" e adiciona um ouvinte de evento para o evento de clique.
document.getElementById("search-button").addEventListener("click", async () => {
    
    // Obtém o valor do campo de entrada HTML com o ID "cep" e atribui à variável 'cep'.
    const cep = document.getElementById("cep").value;

    // Faz uma requisição assíncrona para a API do ViaCEP utilizando o valor do CEP obtido anteriormente.
    const response = await fetch(`https://viacep.com.br/ws/${cep}/json/`);

    // Extrai os dados JSON da resposta da requisição e atribui à variável 'data'.
    const data = await response.json();

    // Atualiza o conteúdo do elemento HTML com o ID "address-details" com os dados obtidos da API.
    document.getElementById("address-details").innerHTML = `
        <p>Logradouro: ${data.logradouro}</p>
        <p>Bairro: ${data.bairro}</p>
        <p>Cidade: ${data.localidade}</p>
        <p>Estado: ${data.uf}</p>
    `;
});
