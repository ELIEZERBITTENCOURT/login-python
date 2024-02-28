# DP Systems - Access Panel

Este é um simples sistema de acesso utilizando uma interface gráfica criada com Tkinter em Python. Ele permite que os usuários façam login em uma conta existente ou se registrem para criar uma nova conta.

## Funcionalidades

1. **Login**: Os usuários podem inserir seu nome de usuário e senha nos campos correspondentes e clicar no botão "Login" para acessar sua conta.
2. **Registro**: Os usuários podem clicar no botão "Registrar" para criar uma nova conta. Eles serão solicitados a fornecer seu nome, e-mail, nome de usuário e senha para registro.
3. **Validação**: Antes de registrar um novo usuário, o sistema valida se todos os campos obrigatórios estão preenchidos.
4. **Feedback**: Após o login ou registro, o sistema fornece feedback ao usuário através de mensagens pop-up, informando se a ação foi bem-sucedida ou se houve algum erro.

## Pré-requisitos

- Python instalado
- Biblioteca Tkinter instalada (geralmente incluída na instalação padrão do Python)

## Instalação

1. Clone ou baixe este repositório para sua máquina local.
2. Certifique-se de ter todas as dependências instaladas.
3. Execute o arquivo `index.py` com Python para iniciar o aplicativo.

```bash
python index.py
```

## Estrutura do Código

O código está organizado da seguinte forma:

- **`index.py`**: Este é o arquivo principal que contém toda a lógica da aplicação.
- **`DataBase.py`**: Este módulo é responsável pela conexão com o banco de dados e as operações relacionadas ao banco de dados.

## Observações

- Certifique-se de configurar corretamente o módulo `DataBase.py` para se conectar ao seu banco de dados antes de executar o aplicativo.
- Este aplicativo é apenas um exemplo simples e pode ser expandido com mais funcionalidades e melhorias de interface de usuário conforme necessário.

Por favor, sinta-se à vontade para contribuir com melhorias ou fornecer feedback sobre este projeto.
