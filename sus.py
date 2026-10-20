import sys

print("= Sistema de triagem: IMC e classificação de risco =")

# Entrada e validação do peso
try:
    peso = float(input("Peso (kg): ").strip().replace(",", "."))
    altura = float(input("Altura (m): ").strip().replace(",", "."))
    idade = int(input("Idade: "))
except ValueError:
    sys.exit("Erro: digite valores numéricos válidos.")

if peso <= 0:
    sys.exit("Erro: o peso deve ser maior que zero.")

if altura <= 0:
    sys.exit("Erro: a altura deve ser maior que zero.")

if idade <= 0:
    sys.exit("Erro: a idade deve ser maior que zero.")

# Classificação etária
if idade >= 60:
    faixa_etaria = "idoso"
else:
    faixa_etaria = "adulto"

# Cálculo do IMC
imc = peso / altura ** 2

# Classificação do IMC
if imc < 18.5:
    faixa_imc = "abaixo do peso"
elif imc < 25:
    faixa_imc = "peso normal"
elif imc < 30:
    faixa_imc = "sobrepeso"
elif imc < 35:
    faixa_imc = "obesidade I"
elif imc < 40:
    faixa_imc = "obesidade II"
else:
    faixa_imc = "obesidade III"

# Mensagem de alerta
if faixa_imc == "peso normal":
    alerta = "IMC dentro da faixa de referência."
else:
    alerta = "Atenção: recomenda-se avaliação profissional."

# Prioridade de acompanhamento
match faixa_imc:
    case "obesidade II" | "obesidade III":
        prioridade = "alta"
    case "abaixo do peso" | "obesidade I" if faixa_etaria == "idoso":
        prioridade = "alta"
    case _:
        prioridade = "baixa"

# Relatório
print(f"""
----- Relatório de triagem -----
Peso: {peso:.1f} kg
Altura: {altura:.2f} m
Idade: {idade} anos ({faixa_etaria})
IMC: {imc:.1f} -> {faixa_imc}
Alerta: {alerta}
Prioridade de acompanhamento: {prioridade.upper()}
--------------------------------
""")