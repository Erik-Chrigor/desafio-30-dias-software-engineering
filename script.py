# =======================================================
#BLOCO 1: CALCULADORA DE FORÇA
# =======================================================

print("--- CALCULADORA DE FORÇA (F = m.a) ---")

#O input() sempre recebe o texto como String.
#Usamos o float() para converter texto em número com vírgula (decimal).

massa_forca = float(input ("Digite a massa do objeto (em kg): "))
aceleracao = float(input("Digite a aceleração (em m/s²): "))

#Executando a equação matemática

forca = massa_forca * aceleracao

# O 'f' antes das aspas permite colocar as variáveis direto dentro do usando usando chaves {}

print (f"\nA força resultante necessária é de: {forca:.2f} Newtons")




# ========================================================
# BLOCO 2: CALCULADORA DE ENERGIA POTENCIAL 
# ========================================================

print("--- CALCULADOR DE ENERGIA POTENCIAL (Ep = m.g.h) ---")

massa_potencial = float(input("Digite a massa do objeto (em kg): "))

GRAVIDADE = 9.8

altura = float(input("Digite a altura do objeto(em metros): "))

ep = massa_potencial * GRAVIDADE * altura

print(f"\nA Energia Potencial Gravitacional é de: {ep:.2f} Joules")   


# =========================================================
#  BLOCO 3: CALCULADORA DE ENERGIA CINÉTICA 
# =========================================================

print("--- CALCULADORA DE ENERGIA CINÉTICA (Ec = (m.v²)/2) ---")

massa_cinetica = float(input("Digite a massa do objeto (em kg): "))

velocidade = float(input("Digite a velocidae (em m/s): "))

ec = (massa_cinetica * (velocidade ** 2)) / 2

print(f" A Energia Cinética é de: {ec:.2f} Joules\n")