import pandas as pd
import numpy as np

def gerar_csv_aleatorio(nome_arquivo='dados_energia.csv', horas=24):
    try:
        # cria dados aleatorios
        horas_dia = list(range(horas))
        demanda = np.round(np.random.uniform(0.5, 3.0, size=horas), 2)
        oferta_renovavel = np.round(np.random.uniform(0.2, 2.5, size=horas), 2)

        # cria dataframe
        dados = pd.DataFrame({
            'hora': horas_dia,
            'demanda': demanda,
            'oferta_renovavel': oferta_renovavel
        })

        # salva em csv
        dados.to_csv(nome_arquivo, index=False)
        print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")
        return nome_arquivo
    except Exception as e:
        print(f"Erro ao gerar csv: {e}")
        return None

# exemplo de uso
gerar_csv_aleatorio()
