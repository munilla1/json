import json

cliente = {
	"ana", "antonio", "ismael"
}
edad = {
	"23"
}

x = json.loads(cliente)

print(x["age"])