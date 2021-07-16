import os
import time
import json
from random import random
from datetime import datetime

import pandas as pd
import seaborn as sns
import requests


class SearchAndExtractData(object):
    def __init__(self, file: str, graph_name: str) -> None:
        self.file = file
        self.graph_name = graph_name

    def create_csv(self) -> None:
        ENDPOINT = "ConsultarTaxaDICetip.aspx"
        URL = f"https://www2.cetip.com.br/ConsultarTaxaDi/{ENDPOINT}"

        # Criando a variável data e hora
        for _ in range(0, 10):
            data_e_hora = datetime.now()
            data = datetime.strftime(data_e_hora, "%Y/%m/%d")
            hora = datetime.strftime(data_e_hora, "%H:%M:%S")

            # Captando a taxa CDI do site da B3
            try:
                response = requests.get(URL)
                response.raise_for_status()
            except requests.HTTPError:
                print("Dado não encontrado, continuando.")
                cdi = None
            except Exception as exc:
                print("Erro, parando a execução.")
                raise exc
            else:
                dado = json.loads(response.text)
                cdi = float(dado["taxa"].replace(",", "."))

            # Verificando se o arquivo "taxa-cdi.csv" existe
            if os.path.exists(f"./{self.file}") is False:

                with open(
                    file=f"./{self.file}", mode="w", encoding="utf8"
                ) as fp:
                    fp.write("data,hora,taxa\n")

            # Salvando dados no arquivo "taxa-cdi.csv"
            with open(file=f"./{self.file}", mode="a", encoding="utf8") as fp:
                fp.write(f"{data},{hora},{cdi}\n")

            time.sleep(2 + (random() - 0.5))

        print("Sucesso")

    def create_graph(self) -> None:
        # Extraindo as colunas hora e taxa
        df = pd.read_csv(f"./{self.file}")

        # Salvando no grafico
        grafico = sns.lineplot(x=df["hora"], y=df["taxa"])
        _ = grafico.set_xticklabels(labels=df["hora"], rotation=90)
        grafico.get_figure().savefig(f"{self.graph_name}.png")
