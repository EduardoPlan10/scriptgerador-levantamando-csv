# scriptgerador-levantamando-csv
Script em python para gerar um .csv contento dados de computadores.

## Instalação
Para instalar basta usar na linha de comando:

```bash
  $ pip install -r requirements.txt
```

Ajustar os arquivos de configuração contidos no diretório /config

Onde: 
* setup-headers.json contém o cabeçalho do .csv
* setup-setores.json contém os códigos dos setores
* setup-templates.json contém os códigos das especificações das máquians
* user-data.json contém as informações dos items do levantamento, fazendo referência aos códigos dos setores e templates previamente estabelecidaos

Após a configuração basta executas o script usando:

```bash
  $ python3 main.py
```

O resultado será gerado em /results/levantamento-results.csv

## Considerações

Para também ser compatível com o SO windows foi usada a biblioteca colorama para as mensagens do terminal.