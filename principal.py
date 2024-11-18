import pandas as pd
import matplotlib.pyplot as plt

# =======================
# funcao para carregar e limpar dados
# =======================
def carregar_dados(usar_dados_ficcionais=True, caminho_dados_reais=None):
    if usar_dados_ficcionais:
        dados = pd.DataFrame({
            'hora': list(range(24)),
            'demanda': [1.2, 1.1, 1.0, 0.9, 1.1, 1.3, 1.6, 2.0, 2.3, 2.5, 2.4, 2.2, 2.1, 1.8, 1.5, 1.4, 1.3, 1.2, 1.1, 1.0, 1.2, 1.3, 1.5, 1.7],
            'oferta_renovavel': [0.5, 0.5, 0.5, 0.4, 0.3, 0.5, 0.7, 1.0, 1.2, 1.3, 1.4, 1.5, 1.3, 1.1, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.6, 0.8, 0.9, 1.0]
        })
    else:
        if caminho_dados_reais:
            try:
                dados = pd.read_csv(caminho_dados_reais)
            except FileNotFoundError:
                print("Arquivo nao encontrado. Tente novamente.")
                return None
            except pd.errors.ParserError:
                print("Erro ao ler o arquivo. Verifique se o formato esta correto.")
                return None

    dados = dados.dropna()
    print(f"Dados {'ficticios' if usar_dados_ficcionais else 'reais'} carregados com sucesso.")
    return dados

# =======================
# inicializar tabela dp
# =======================
def inicializar_tabela_dp(dados):
    n = len(dados)
    dp = [float('inf')] * n
    dp[0] = 0
    print("Tabela dp inicializada.")
    return dp

# =======================
# calcular custos
# =======================
def calcular_custos(dados, dp, custo_unitario=0.1):
    for i in range(1, len(dados)):
        for j in range(i):
            custo = max(0, dados['demanda'][i] - dados['oferta_renovavel'][i]) * custo_unitario
            dp[i] = min(dp[i], dp[j] + custo)
    print("Tabela dp preenchida com custos calculados.")
    return dp

# =======================
# gerar insights e salvar resultados
# =======================
def gerar_insights(dados, dp, salvar=False):
    horas_atendidas = sum(dados['demanda'] <= dados['oferta_renovavel'])
    porcentagem_atendida = (horas_atendidas / len(dados)) * 100
    custo_total = dp[-1]

    insights = [
        f"Percentual de horas com demanda atendida por fontes renovaveis: {porcentagem_atendida:.2f}%",
        f"Custo total acumulado devido ao deficit de energia renovavel: {custo_total:.2f} unidades de custo"
    ]
    if porcentagem_atendida < 75:
        insights.append("Sugestao: considere adicionar mais fontes de energia renovavel ou otimizar o horario de consumo.")
    else:
        insights.append("Bom nivel de uso de energia renovavel! Ajuste a demanda para reduzir custos.")
    
    for linha in insights:
        print(linha)

    if salvar:
        with open("resultados_insights.txt", "w") as arquivo:
            arquivo.write("\n".join(insights))
        print("Insights salvos em resultados_insights.txt")

# =======================
# visualizar dados
# =======================
def visualizar_dados(dados, dp):
    plt.figure(figsize=(12, 6))
    plt.plot(dados['hora'], dados['demanda'], label='demanda', color='red')
    plt.plot(dados['hora'], dados['oferta_renovavel'], label='oferta renovavel', color='green')
    plt.fill_between(
        dados['hora'], 
        dados['demanda'], 
        dados['oferta_renovavel'], 
        where=(dados['demanda'] > dados['oferta_renovavel']),
        color='yellow', alpha=0.5, label='deficit'
    )
    plt.title("Demanda e oferta renovavel ao longo do dia")
    plt.xlabel("Hora")
    plt.ylabel("Unidades")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("Grafico_demanda_vs_oferta.png", dpi=300)
    print("Grafico salvo como 'Grafico_demanda_vs_oferta.png'")
    plt.show()

# =======================
# menu interativo
# =======================
def menu():
    dados = None
    dp = None

    while True:
        print("\nMenu:")
        print("1 - Simular dados ficticios")
        print("2 - Carregar dados reais (csv)")
        print("3 - Visualizar graficos")
        print("4 - Sair")
        escolha = input("Escolha uma opcao: ")

        if escolha == "1":
            dados = carregar_dados()
            dp = inicializar_tabela_dp(dados)
            dp = calcular_custos(dados, dp)
            gerar_insights(dados, dp, salvar=True)
        elif escolha == "2":
            caminho = input("Digite o caminho do arquivo csv: ")
            dados = carregar_dados(usar_dados_ficcionais=False, caminho_dados_reais=caminho)
            if dados is not None:
                dp = inicializar_tabela_dp(dados)
                dp = calcular_custos(dados, dp)
                gerar_insights(dados, dp, salvar=True)
        elif escolha == "3":
            if dados is not None and dp is not None:
                visualizar_dados(dados, dp)
            else:
                print("Dados nao carregados. Escolha uma opcao para carregar dados primeiro.")
        elif escolha == "4":
            print("Saindo do programa. Ate logo!")
            break
        else:
            print("Opcao invalida. tente novamente.")

# =======================
# executar programa
# =======================
if __name__ == "__main__":
    menu()
