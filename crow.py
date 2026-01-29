#this program is a calculator for lineage 2
#you'll be able to convert adena to l2 and l2 to rmt
#as well as calculate odds for leveling up itens
import streamlit as st
from math import floor

# Configuração da Página
st.set_page_config(page_title="L2 Calculator", page_icon="⚔️")

st.title("⚔️ Lineage 2: Conversor de Moedas")
st.markdown("Converta Adena, L2 Coins e calcule valores para RMT.")

# Constante de Taxa
TAXA = 0.05

# 1. Seleção da Opção Principal
opcao = st.radio(
    "O que você deseja fazer?",
    ("Converter Adena em L2 Coin", 
     "Converter L2 Coin em Adena", 
     "Converter L2 Coin em R$")
)

st.divider()

# --- LÓGICA DE CONVERSÃO ---

if opcao == "Converter Adena em L2 Coin":
    col1, col2 = st.columns(2)
    
    with col1:
        qntd_adena = st.number_input("Quantidade de Adena (em milhões):", min_value=0, value=100)
    with col2:
        valor_atual_l2 = st.number_input("Preço de 1M de Adena em L2 Coin:", min_value=0.0, value=10.0)

    # Cálculo
    valor_final_l2 = qntd_adena * valor_atual_l2 * (1 - TAXA)
    
    st.metric("Resultado", f"{int(valor_final_l2)} L2 Coins")
    st.caption(f"Já aplicado desconto de {TAXA*100}% de taxa.")

    # Opção extra: Converter para Real
    st.subheader("💰 Converter esse montante para Real?")
    check_real = st.checkbox("Sim, calcular valor em R$")
    
    if check_real:
        preco_mil_l2 = st.number_input("Preço de 1k de L2 Coin (R$):", min_value=0.0, value=50.0)
        l2_para_real = (valor_final_l2 / 1000) * preco_mil_l2 * (1 - TAXA)
        st.success(f"O valor estimado em conta é: **R$ {l2_para_real:.2f}**")

elif opcao == "Converter L2 Coin em Adena":
    qntd_l2coin = st.number_input("Quantidade de L2 Coin que possui:", min_value=0, value=1000)
    valor_por_milhao = st.number_input("Preço em L2 Coin por cada 1M de Adena:", min_value=1, value=15)
    
    valor_final_adena = qntd_l2coin / valor_por_milhao
    
    st.metric("Total de Adena", f"{floor(valor_final_adena)} Milhões")

elif opcao == "Converter L2 Coin em R$":
    qntd_l2coin = st.number_input("Quantidade de L2 Coin que possui:", min_value=0, value=1000)
    preco_mil_l2 = st.number_input("Preço de 1k de L2 Coin (R$):", min_value=0.0, value=50.0)
    
    l2_para_real = (qntd_l2coin / 1000) * preco_mil_l2 * (1 - TAXA)
    
    st.metric("Valor em R$", f"R$ {l2_para_real:.2f}")
    st.info(f"Valor considerando taxa de {TAXA*100}% sobre a venda final.")

# Rodapé
st.sidebar.markdown("---")
st.sidebar.write("💻 **L2 Calculator v2.0**")


from math import floor

taxa = 0.05

while True:
    try:
        opcao = int(input("Deseja converter adena em L2 Coin(1), L2 em adena(2) ou L2 em R$(3)? "))
    except (TypeError, ValueError, IndexError):
        print("Digite somente o número que indica a opção que desejas.")
        continue

    if opcao == 1:
        try:
            qntd_adena = int(input("Quanto de adena (em milhões) você deseja converter? "))
        except (TypeError, ValueError):
            print("Digite um número válido.")
            break
        valor_atual_l2 = float(input("Qual valor atual de 1 milhão de adena em L2? "))
        valor_final_l2 = qntd_adena * valor_atual_l2 * (1-taxa)
        print(f"{qntd_adena} milhões de adena equivale à: {int(valor_final_l2)} L2 Coin")
        opcao_continuar = int(input("Deseja agora converter L2 em R$? Sim(1) ou Não(0)"))
        if opcao_continuar == 1:
            preco_l2 = float(input("Qual preço deseja cobrar em 1k de L2 Coin? "))
            l2_para_real = valor_final_l2/1000 * preco_l2 * (1-taxa)
            print(f"{int(valor_final_l2)} L2 Coin será R${l2_para_real:.2f}")
            break
        else:
            break

    if opcao == 2:
        qntd_l2coin = int(input("Quanto de L2 Coin você possui? "))
        valor_atual_adena = int(input("Qual valor em L2 coin por cada milhão de adena? "))
        valor_final_adena = qntd_l2coin/valor_atual_adena
        print(f"{qntd_l2coin} L2 Coin comprará {floor(valor_final_adena)} milhões de adena.")
        break

    if opcao == 3:
        qntd_l2coin = int(input("Quanto de L2 Coin você possui? "))
        preco_l2 = float(input("Qual preço (em reais) deseja cobrar em 1k de L2 Coin? "))
        l2_para_real = qntd_l2coin/1000 * preco_l2 * (1-taxa)
        print(f"{int(qntd_l2coin)} L2 Coin será R${l2_para_real:.2f}")
        break
