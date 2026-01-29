#this program is a calculator for lineage 2
#you'll be able to convert adena to l2 and l2 to rmt
#as well as calculate odds for leveling up itens
import streamlit as st
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
