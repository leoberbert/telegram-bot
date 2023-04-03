# telegram-bot

Este simples código lhe ajudará a implementar um simples bot para telegram que retornará a escala de plantão cadastrada.

Primeiramente será necessário criarmos a base de dados onde serão armazenados os plantonistas, para isso execute o código abaixo que criará o arquivo plantao.db:

```
python3 database.py
```
Feito isso iremos agora subir o nosso servidor WEB onde iremos realizar o cadastro do plantonista:

```
python3 server.py
```

Acesse o local onde o comando acima está sendo executado através de seu browser, o meu caso será a máquina local:

```
http://localhost:5000/plantao
```

Será solicitado o usuário e senha que está cadastrado no arquivo server.py no bloco abaixo:

![image](https://user-images.githubusercontent.com/16724862/229540421-25b6aba9-60b1-46f1-abff-bf0e5c9098f8.png)

Ao fornecer o usuario e senha você será direcionado para a tela de cadastro abaixo onde poderá cadastrar o nome do plantão e a data que ele está de plantão.

![image](https://user-images.githubusercontent.com/16724862/229543152-56ca878f-31df-4865-8f54-3a494a299f9c.png)

![image](https://user-images.githubusercontent.com/16724862/229543508-ce255243-849d-444a-8f22-341e927377a5.png)

Caso queira consultar se o cadastro foi realizado no banco de dados, execute o show_cadastro.py:

```
python3 show_cadastro.py
('Joao', '2023-04-03')
```

Agora iremos iniciar o boot para que possamos interagir com ele:

OBS: Será necessário subistituir no código, o bloco abaixo adicionando o token do seu bot que você obteve após criação do mesmo no **@BotFather**.

![image](https://user-images.githubusercontent.com/16724862/229545258-e39df035-5f88-4502-b3e2-c60f7ec04a84.png)


```
python3 boot.py
```
