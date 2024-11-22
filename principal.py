''' 
=======================
DEBORA AMARAL - RM:550412
LEVY JUNIOR - RM:98655
LÍVIA NAMBA - RM:97819
=======================
''' 

import pandas as pd
import matplotlib.pyplot as plt

# =======================
# definindo as constantes
# =======================
CONSUMO_MEDIO_HORA = 1.918  # kWh/h, baseado no cálculo per capita 

# =======================
# coleta de Dados
# =======================
def coletar_dados(caminho_csv=None, usar_dados_ficcionais=True):
    if usar_dados_ficcionais:
        dados = pd.DataFrame({
            'hora': list(range(24)),
            'demanda': [val * CONSUMO_MEDIO_HORA for val in [1.2, 1.1, 1.0, 0.9, 1.1, 1.3, 1.6, 2.0, 2.3, 2.5, 2.4, 2.2, 2.1, 1.8, 1.5, 1.4, 1.3, 1.2, 1.1, 1.0, 1.2, 1.3, 1.5, 1.7]],
            'oferta_renovavel': [0.5, 0.5, 0.5, 0.4, 0.3, 0.5, 0.7, 1.0, 1.2, 1.3, 1.4, 1.5, 1.3, 1.1, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.6, 0.8, 0.9, 1.0],
            'custo_energia_nao_renovavel': [0.2] * 24
        })
        print("Dados fictícios ajustados com média per capita carregados.")
    else:
        if caminho_csv is None:
            print("Erro: Caminho do arquivo CSV não fornecido.")
            return None
        try:
            dados = pd.read_csv(caminho_csv)
            dados['demanda'] *= CONSUMO_MEDIO_HORA  
            print("Dados reais carregados e ajustados com média per capita.")
        except Exception as e:
            print(f"Erro ao carregar dados reais: {e}")
            return None
    
    dados.dropna(inplace=True)  # remover valores ausentes
    return dados

# =======================
# inicialização da tabela de DP
# =======================
def inicializar_dp(dados):
    n = len(dados)
    dp = [float('inf')] * n
    dp[0] = 0  
    print("Tabela DP inicializada.")
    return dp

# =======================
# função de yransição de estados
# =======================
def calcular_custos_dp(dados, dp):
    for i in range(1, len(dados)):
        for j in range(i):
            deficit = max(0, dados['demanda'][i] - dados['oferta_renovavel'][i])
            custo = deficit * dados.get('custo_energia_nao_renovavel', pd.Series([0.1] * len(dados)))[i]
            dp[i] = min(dp[i], dp[j] + custo)
    print("Tabela DP preenchida com custos calculados.")
    return dp

# =======================
# obter solução ótima e Insights
# =======================
def obter_insights(dados, dp, salvar=False):
    horas_atendidas = sum(dados['demanda'] <= dados['oferta_renovavel'])
    porcentagem_atendida = (horas_atendidas / len(dados)) * 100
    custo_total = dp[-1]

    insights = [
        f"Percentual de horas com demanda atendida por fontes renováveis: {porcentagem_atendida:.2f}%",
        f"Custo total acumulado devido ao déficit de energia renovável: {custo_total:.2f} unidades de custo."
    ]
    
    if porcentagem_atendida < 75:
        insights.append("Recomenda-se adicionar mais fontes de energia renovável ou reprogramar o consumo.")
    else:
        insights.append("Bom aproveitamento da energia renovável! Continue ajustando a demanda.")
    
    for linha in insights:
        print(linha)

    if salvar:
        with open("resultados_insights.txt", "w") as arquivo:
            arquivo.write("\n".join(insights))
        print("Insights salvos no arquivo 'resultados_insights.txt'.")

# =======================
# visualização dos dados
# =======================
def visualizar_dados(dados, dp):
    plt.figure(figsize=(12, 6))
    plt.plot(dados['hora'], dados['demanda'], label='Demanda', color='red')
    plt.plot(dados['hora'], dados['oferta_renovavel'], label='Oferta Renovável', color='green')
    plt.fill_between(dados['hora'], dados['demanda'], dados['oferta_renovavel'], 
                     where=(dados['demanda'] > dados['oferta_renovavel']), color='yellow', alpha=0.5, label='Déficit')
    plt.title("Demanda e Oferta Renovável ao Longo do Dia")
    plt.xlabel("Hora")
    plt.ylabel("Unidades (kWh)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("grafico_demanda_vs_oferta.png", dpi=300)
    print("Gráfico salvo como 'grafico_demanda_vs_oferta.png'.")
    plt.show()

# =======================
# menu 
# =======================
def menu():
    dados = None
    dp = None

    while True:
        print("\nMenu:")
        print("1 - Simular Dados Fictícios")
        print("2 - Carregar Dados Reais (CSV)")
        print("3 - Visualizar Gráficos")
        print("4 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            dados = coletar_dados(usar_dados_ficcionais=True)
            dp = inicializar_dp(dados)
            dp = calcular_custos_dp(dados, dp)
            obter_insights(dados, dp, salvar=True)
        elif escolha == "2":
            caminho = input("Digite o caminho do arquivo CSV: ")
            dados = coletar_dados(caminho_csv=caminho, usar_dados_ficcionais=False)
            if dados is not None:
                dp = inicializar_dp(dados)
                dp = calcular_custos_dp(dados, dp)
                obter_insights(dados, dp, salvar=True)
        elif escolha == "3":
            if dados is not None and dp is not None:
                visualizar_dados(dados, dp)
            else:
                print("Dados não carregados. Escolha uma opção para carregar dados primeiro.")
        elif escolha == "4":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
