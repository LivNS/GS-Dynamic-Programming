import pandas as pd
import numpy as np

# Constante para consumo médio por pessoa (kWh/h)
CONSUMO_MEDIO_HORA = 1.918

# Gerar um banco de dados para teste
def gerar_csv_aleatorio(nome_arquivo='dados_energia.csv', horas=24):
    try:
        # Cria dados aleatórios
        horas_dia = list(range(horas))
        # Ajusta demanda com base no consumo médio por pessoa
        demanda = np.round(np.random.uniform(0.5, 3.0, size=horas) * CONSUMO_MEDIO_HORA, 2)
        oferta_renovavel = np.round(np.random.uniform(0.2, 2.5, size=horas), 2)

        # Cria DataFrame
        dados = pd.DataFrame({
            'hora': horas_dia,
            'demanda': demanda,
            'oferta_renovavel': oferta_renovavel,
            'custo_energia_nao_renovavel': [0.2] * horas  # Valor constante para custo não renovável
        })

        # Salva em CSV
        dados.to_csv(nome_arquivo, index=False)
        print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")
        return nome_arquivo
    except Exception as e:
        print(f"Erro ao gerar CSV: {e}")
        return None

# Exemplo de uso
gerar_csv_aleatorio()
