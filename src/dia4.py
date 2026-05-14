# --- Dia  4: ESTRUTURAS DE DADOS (LISTAS) ---

# Criando uma lista de usuários
usuarios = ["Erik", "Ana", "Carlos"]

# 1. TOMADA DE DECISÃO: Adcioar se não existir
novo_usuario =  "Beatriz"

if novo_usuario  in usuarios:
    print(f"Aviso: {novo_usuario} já está na lista.")
else:
    usuarios.append(novo_usuario)
    print(f"Sucesso:{novo_usuario} adicionado!")

    # 2. REMOVER UM DADO
    usuarios.remove("Carlos")

    # 3. ORDENAR (Ordem Alfabética)
    usuarios.sort()

    #  4. 
    print(f"Lista Final:{usuarios}")