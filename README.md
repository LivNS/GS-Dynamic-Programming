# 🌱 **Aplicativo de Otimização Energética Doméstica com IA** ⚡

Bem-vindo ao repositório do **Aplicativo de Otimização Energética Doméstica com Inteligência Artificial**! Este projeto busca utilizar IA para otimizar o consumo de energia nas residências, ajudando a reduzir custos e promover um ambiente mais sustentável. 🌍💡

## 🎯 **Objetivo**
Criar um aplicativo que aprende com os hábitos dos usuários e ajusta automaticamente o consumo energético de acordo com a disponibilidade de energia renovável, priorizando horários de baixa demanda. Tudo isso para reduzir o desperdício de energia, economizar na conta de luz e contribuir para um futuro mais verde! 🌱✨

## 🧩 **Como Funciona**
- O aplicativo monitora a **demanda** de energia e a **oferta de fontes renováveis** ao longo do dia.
- Ele utiliza **inteligência artificial** para otimizar o consumo com base nesses dados.
- A IA aprende com o comportamento do usuário e ajusta os padrões de uso, promovendo eficiência e sustentabilidade.

## 💻 **Tecnologias Utilizadas**
- Python
- Pandas (para manipulação de dados)
- Matplotlib (para visualização gráfica)
- Algoritmos de programação dinâmica para otimização de custos

# 1. Instalar Dependências
O projeto utiliza as bibliotecas pandas e matplotlib. Você pode instalá-las com o seguinte comando:

pip install pandas matplotlib


# 2. Simular Dados
Você pode gerar dados fictícios de consumo e oferta de energia para testar o aplicativo:

gerar_csv_aleatorio()

# 3. Carregar Dados Reais
Carregue seus próprios dados de consumo de energia em formato CSV:

carregar_dados(usar_dados_ficcionais=False, caminho_dados_reais="caminho/para/seu/arquivo.csv")

# 4. Visualizar os Gráficos
Após carregar os dados, você pode visualizar a relação entre demanda e oferta de energia ao longo do dia:

visualizar_dados(dados, dp)

# 5. Gerar Insights
Com base nos dados, o aplicativo gera insights e sugere otimizações no consumo:

gerar_insights(dados, dp, salvar=True)

# Exemplo de Saída:
O código irá gerar um gráfico mostrando a demanda e a oferta de energia renovável ao longo do dia, assim como insights sobre a eficiência do consumo de energia.

# Funções Principais:
Funções Principais:
- carregar_dados(): Carrega e limpa os dados de consumo e oferta de energia.
- calcular_custos(): Calcula os custos de energia com base na demanda e oferta.
- gerar_insights(): Gera insights sobre a eficiência energética e sugere melhorias.
- visualizar_dados(): Exibe gráficos de demanda e oferta de energia.
- gerar_csv_aleatorio(): Gera dados aleatórios para simulação.

# Benefícios:
Benefícios:
- Economia nas contas de luz 💰
- Redução de desperdício energético ♻️
- Maior uso de fontes renováveis 🌞
- Contribuição para um futuro mais sustentável 🌍

