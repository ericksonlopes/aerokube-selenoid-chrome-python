# Aerokube Selenoid Chrome With Python

## Apresentação

O projeto consiste em um exemplo de configuração do WebDriver Remoto no Docker para o Selenium, juntamente com um código Python para se
conectar e interagir com o navegador.

A configuração utiliza o Selenoid para criar instâncias isoladas de navegadores e o Docker Compose para orquestrar os
containers necessários. Isso permite executar testes automatizados em diferentes versões e browsers de forma fácil e
escalável.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter os seguintes pré-requisitos instalados em sua máquina:

- Python (versão 3.6+)
- Docker
- Docker Compose

## Instalação

1. Clone o repositório para o seu ambiente local:

   ```bash
   git clone https://github.com/ericksonlopes/aerokube-selenoid-chrome-python
   ```

2. Instale as dependências do projeto:

   ```bash
   pip install selenium
   ```

## Configuração

1. Edite o arquivo `docker-compose.yml`:

    - Verifique se as imagens `selenoid/chrome:latest` e `aerokube/selenoid` estão configuradas corretamente. Caso
      necessário, atualize as versões de acordo com sua preferência.

## Execução

1. Inicie os containers do Docker Compose:

   ```bash
   docker-compose up -d
   ```

2. Execute o código Python para conectar-se ao Selenium:

   ```bash
   python main.py
   ```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou relatar problemas
no [repositório do projeto](https://github.com/ericksonlopes/aerokube-selenoid-chrome-python).

## Licença

Este projeto está licenciado sob a licença [MIT](https://opensource.org/licenses/MIT).

## Contato

Se você tiver alguma dúvida ou sugestão, entre em contato no [linkedin](https://www.linkedin.com/in/ericksonlopes/).
