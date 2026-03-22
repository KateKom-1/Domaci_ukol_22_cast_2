#import json

import requests

jmeno = input("Zadejte název organizace: ")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

data = {"obchodniJmeno": jmeno}

response = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, json=data)

#print(response.status_code)
pocet_subjektu = response.json()

print("Počet nalezených subjektů: ",pocet_subjektu["pocetCelkem"])

for subjekt in pocet_subjektu["ekonomickeSubjekty"]:
    obchodni_jmeno = subjekt["obchodniJmeno"]
    ico = subjekt["ico"]
    print(obchodni_jmeno + " , " + ico)





#22834958

