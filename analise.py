import pandas as pd
import matplotlib.pyplot as plt

#1. Carregar os dados do arquivo CSV
df = pd.read_csv('produtividade.csv')

#2. Exibir os dados na tela para conferir se deu certo
print("--- DADOS CARREGADOS ---")
print(df)
print("-" * 24)

#3. calcular algumas estatísticas basicas
total_horas = df['horas_estudo'].sum()
media_horas = df['horas_estudo'].mean()
total_projetos = df['projetos_concluidos'].sum()

#4. criar um gráfico de linhas de progresso de estudos
plt.figure(figsize=(10, 5))
plt.plot(df['data'], df['horas_estudo'], marker='o' , color='dodgerblue', linewidth=2)

# Custumizar o gráfico
plt.title('Evolução das horas de estudo diárias', fontsize=14, fontweight='bold')
plt.xlabel('Data', fontsize=12)
plt.ylabel('Horas dedicadas', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

#salvar o gráfico na pasta do projetos
plt.savefig('grafico_produtividade.png')
print("\nGráfico gerado e salvo com sucesso como 'grafico_produtividade.png'!")