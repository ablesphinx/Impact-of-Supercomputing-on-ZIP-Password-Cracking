# Anàlisi de la Influència de la Supercomputació en el Desxiframent de Contrasenyes de Fitxers ZIP

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Resum
Aquest repositori conté el treball complet d’un projecte de recerca que investiga com la computació paral·lela i els recursos de supercomputació impacten en l’eficiència dels atacs de força bruta contra fitxers ZIP encriptats. L’estudi compara:

- Execució seqüencial
- Paral·lelització amb nuclis limitats en un ordinador personal
- Paral·lelització massiva al superordinador MareNostrum 5

El repositori inclou:

- Document final de recerca (`docs/` | `documents/`)
- Scripts en Python per a operacions de força bruta i recompte de combinacions (`python_codes/`)
- Datasets experimentals i taules amb temps d’execució i combinacions per segon (`data_tables/` | `taules_de_dades/`)
- Fitxers ZIP d’exemple utilitzats per a proves (`used_zip_files/` | `arxius_zip_utilitzats/`)

## Estructura del Repositori

- `python_codes/` Scripts en Python per als experiments
- `en`
    - `data_tables/` Resultats de les proves de desxiframent i altres taules
    - `docs/` Documents finals de recerca
    - `used_zip_files/` Fitxers ZIP d’exemple per a proves
- `cat` (el mateix però en català)
    - `taules_de_dades`
    - `documents`
    - `arxius_zip_utilitzats`

## Objectius

1. Quantificar l’efecte de la paral·lelització en el temps de desxiframent de contrasenyes.  
2. Identificar l’impacte de la longitud de la contrasenya i la complexitat del conjunt de caràcters en la seguretat.  
3. Proporcionar una comparació pràctica del rendiment dels atacs de força bruta en diferents entorns computacionals.  

## Resultats Principals

### Paral·lelització
La paral·lelització millora significativament el rendiment dels atacs de força bruta. Encara que la velocitat individual de cada worker disminueix en augmentar-ne el nombre, el rendiment total creix de manera notable.  
Això demostra escalabilitat, permetent atacs més ràpids sobre contrasenyes complexes quan s’utilitzen recursos massius de computació paral·lela com el MareNostrum 5 (accés restringit a usuaris autoritzats).

### Longitud i Varietat de Contrasenyes
- Les contrasenyes més llargues que combinen majúscules, minúscules, números i símbols són molt més resistents als atacs de força bruta.  
- Les contrasenyes curtes o amb conjunts de caràcters limitats són més vulnerables.  
- La posició de la contrasenya a l’espai de cerca és rellevant; per exemple, les que comencen amb `0` quan només s’usen números es proven primer i són més fàcils de desxifrar ràpidament.  
- Les combinacions per segon es van mantenir estables en diferents complexitats i longituds de contrasenya, mostrant un rendiment previsible.  

### Complexitat de l’Alfabet
Conjunts de caràcters més grans i complexos (per exemple, alfabets ampliats o escriptures no llatines) incrementen exponencialment el nombre de combinacions possibles, fent que els atacs de força bruta siguin molt menys factibles.

### Observacions sobre ZIP Crypto
El ZIP Crypto pot produir **col·lisions de contrasenyes**: contrasenyes diferents poden generar la mateixa clau interna, permetent desxifrar el mateix fitxer amb diverses contrasenyes.  
Això es deu al seu xifratge RC4 modificat i a l’espai de claus limitat (2³² combinacions).  
Exemple: un fitxer amb la contrasenya `aF9m` també podria ser desxifrat amb `aaaH` durant les proves de força bruta.  

### Rendiment entre Màquines
- Portàtil personal (seqüencial): ~8.000 combinacions/segon.  
- Portàtil (6 workers en paral·lel): ~4.500 combinacions/segon per worker.  
- MareNostrum 5 (75 workers): ~1.760 combinacions/segon per worker, però amb un rendiment total molt més alt gràcies a la paral·lelització massiva.  
- Confirma que la paral·lelització a gran escala compensa la menor velocitat individual de cada worker.  

**Resum:** La paral·lelització accelera els atacs de força bruta, però la longitud, la complexitat i el conjunt de caràcters de la contrasenya continuen essent els factors més crítics per a la seguretat. Les limitacions internes de claus de ZIP Crypto poden permetre múltiples contrasenyes vàlides per a un mateix fitxer, subratllant la necessitat d’un xifratge més robust. Tots els objectius inicials s’han assolit, i a més s’han obtingut coneixements addicionals sobre col·lisions de contrasenyes i eficiència de la paral·lelització.  

**Treballs futurs:** Investigar en profunditat les vulnerabilitats de ZIP Crypto i explorar estratègies de paral·lelització optimitzades per maximitzar l’eficiència dels atacs de força bruta.  

## Com Utilitzar els Scripts

1. Descarrega o clona el repositori.  
2. Configura els paràmetres als scripts en Python (longitud de la contrasenya, conjunt de caràcters, nombre d’intents, etc.).  
3. Executa els scripts amb Python 3.6 o superior.  

## Requisits

Només calen mòduls de la llibreria estàndard:

- `zipfile`  
- `itertools`  
- `string`  
- `multiprocessing`  
- `sys`  
- `datetime`  
- `os`  

No cal instal·lar cap paquet addicional.  

## Llicència

Aquest projecte està sota la llicència MIT - vegeu el fitxer [LICENSE](LICENSE) per a més detalls.
