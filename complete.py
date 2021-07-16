from sys import argv

from _main_ import SearchAndExtractData

file_csv = SearchAndExtractData("./taxa-cdi.csv", argv[1])

file_csv.create_csv()  # cria o CSV com os dados de CDI
file_csv.create_graph()  # Cria os gráficos a partir dos dados do CSV
