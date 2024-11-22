import pandas as pd
import numpy as np

# constante para consumo médio por pessoa (kWh/h)
CONSUMO_MEDIO_HORA = 1.918

# gerar um banco de dados para teste
def gerar_csv_aleatorio(nome_arquivo='dados_energia.csv', horas=24):
    try:
        # cria dados aleatórios
        horas_dia = list(range(horas))
        # ajusta demanda com base no consumo médio por pessoa
        demanda = np.round(np.random.uniform(0.5, 3.0, size=horas) * CONSUMO_MEDIO_HORA, 2)
        oferta_renovavel = np.round(np.random.uniform(0.2, 2.5, size=horas), 2)

        # cria DataFrame
        dados = pd.DataFrame({
            'hora': horas_dia,
            'demanda': demanda,
            'oferta_renovavel': oferta_renovavel,
            'custo_energia_nao_renovavel': [0.2] * horas  # valor constante para custo não renovável
        })

        # salva em CSV
        dados.to_csv(nome_arquivo, index=False)
        print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")
        return nome_arquivo
    except Exception as e:
        print(f"Erro ao gerar CSV: {e}")
        return None

# exemplo de uso
gerar_csv_aleatorio()


''' 
Para ajustar os valores de demanda energética por pessoa no gerador de CSV, fizemos o seguinte:
    1. Com base nos dados do csv 'Consumo_horario_2024' retirados do site Our World in Data, identificamos que o consumo médio anual de energia por pessoa era de aproximadamente 1.918 kWh/pessoa/ano.
    2. Para tornar esse valor utilizável no contexto horário, convertemos o consumo médio anual para consumo médio por hora:
        Um ano tem 8.760 horas (365 dias x 24 horas).
        Consumo dio por hora = 8760horas/1918kWh ≈ 0.219kWh/hora/pessoa.

    3. Multiplicamos os valores aleatórios de demanda gerados para cada hora por 0.219 kWh/hora/pessoa, ajustando a escala para refletir o consumo energético médio realista de uma pessoa.
    4. Realizamos esse ajuste para que a demanda horária no CSV agora reflete, de forma ajustada, o consumo médio real por pessoa, mantendo variações para simular diferentes níveis de consumo ao longo do dia. 


'''