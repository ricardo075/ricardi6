import streamlit as st

def calcula_largura(resistividade, area, resistencia):
    DADOS = f'DADOS:---------------------------------------------------------'
    DADOS2 = f'L= ?;'
    DADOS3 = f'R= {resistividade} ohm'
    DADOS4 = f'A= {area} m'
    DADOS5 = f'r= {resistencia} ohm mm/m²'
    FORMULA3 = f'FORMULA:-----------------------------------------------------'
    FORMULA = f'L=R * A / r (LARGURA = RESISTIVIDADE(r) vezes(*) AREA a dividir pela(/) RESITENCIA(r)'
    RESOLUÇÃO = f'RESOLUÇAO:--------------------------------------------------'
    passo1 = f'Passo 1: Multiplicar a resistividade ({resistividade} ohm pela area ({area} m)'
    passo2 = f'Passo 2: Dividir o resultado pelo valor da resistencia ({resistencia}ohm  mm²/m)'
    largura = (resistividade * area) / resistencia
    return largura, [DADOS, DADOS2, DADOS3, DADOS4, DADOS5, FORMULA3, FORMULA, RESOLUÇÃO, passo1, passo2]

st.title('Calculadora de largura')

resistividade = st.number_input('Insira o valor da resistividade (ohm)')
area = st.number_input('Insira o valor da area (m²)')
resistencia = st.number_input('Insira o valor da resistencia (ohm mm²/m)')

if st.button('Calcular largura'):
    largura, passos = calcula_largura(resistividade, area, resistencia)
    st.write('Passos para calcular a largura:')
    for passo in passos:
        st.write(passo)
    st.write(f'A largura é: {largura} m')
    st.write('OBRIGADO POR USAR ESTE SITE, SE HOUVER ALGUM PROBLEMA OU CRITICA CONSTRUTIVA'
             'CONTACTE 841038887/868787572')





