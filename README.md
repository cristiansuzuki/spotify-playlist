# Spotify - Script que cria playlists e adiciona músicas.

## Instalação

Inicie um ambiente virtual (deve possuir o Python instalado)

```python
python -m venv venv
```

Após isso, acesse a pasta do ambiente pelo terminal e ative o arquivo "activate.bat"

```bash
venv\Scripts\activate
```

## Instalando dependências do projeto

Use o gerenciador de pacotes do python para baixar as as bibliotecas necessárias do arquivo requirements.txt

```bash
pip install -r requirements.txt
```

## Setando chaves de ambiente (API Keys)

Acesse sua conta de desenvolvedor do Spotify (crie uma se nao tiver), crie um novo App e pegue suas chaves API

Se estiver usando Windows, no console (com o venv ativado) digite:

```bash
set SPOTIPY_CLIENT_ID=suachave
set SPOTIPY_CLIENT_SECRET=suachave
```

## Rodando o script

Digite no console: 

```python
python main.py
```

Em seguida, irá perguntar o nome e a descrição da playlist. Após isso, você deverá incluir os nomes das músicas e após terminar digite 'fim' quando tiver adicionado todas as músicas.


## Contribuições

Pull Requests são bem-vindos.
