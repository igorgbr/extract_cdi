# Extrator de dados
### App faz um request para API da bolsa de valores e extrai taxa CDI.
#### Guarda os dados em um arquivo *CSV e gera um gráfico a partir dos dados.

<img src="https://datatofish.com/wp-content/uploads/2018/12/0002_plot_dataframe.png">
<img src="https://datatofish.com/wp-content/uploads/2018/12/002_plot_df.png">

---

#### Pré uso:
 Instale as bibliotecas **Pandas, Seaborn, Requests**

 ```bash
pip install pandas seaborn requests
```

#### Para executar:
Clone o projeto e execute no terminal *(<nome_do_gráfico> sera o nome do arquivo PNG gerado)*:

 ```bash
python complete.py <nome_do_grafico> 
```

<a href="https://datatofish.com/plot-dataframe-pandas/"> Panda </a> - Para trabalhar com os dados<br>
<a href="https://seaborn.pydata.org/generated/seaborn.lineplot.html"> Seaborn </a> - Para criar o gráfico

Altere para trabalhar com outras API's e dados.




