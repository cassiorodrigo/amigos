"""
en:
Shows a usecase of dictionaries for a begginer.
pt: 
Mostra como usar dicionários para um desenvolvedor iniciante.
"""

d1 = {
    1: "Acidente",
    2: "Gravidez",
    3: "Tiro"
        }

resposta = int(input("Selecione 1, 2 ou 3: "))

print(f"Ocorrência de {d1[resposta]} registrada")
