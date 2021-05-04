import json

#lettura
jsonfile = open('Canzoni.json', 'r')
jsondata = jsonfile.read()

#parse
obj = json.loads(jsondata)

U = obj['Playlist1']
print(U)
sotto_U = U[0]
print(sotto_U)

NomeSong = U[0].get("Nome")
print(NomeSong)

NomeArtista = U[0].get("Artista")
print(NomeArtista)

#for i in range(len(sotto_U)):
#    print("Nome della canzone: ", sotto_U[i].get("Nome"))
