import json

with open("armas_json.json", "r") as armas:
    mi_variable = armas.read()

mi_arma =json.loads(mi_variable)
print(mi_arma["nombre"])
print(mi_arma["coordenadas"])