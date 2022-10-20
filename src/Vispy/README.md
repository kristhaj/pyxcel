# Vispy
Samle og formatere data fra ISD til importerbar Visma-fil, for fakturagrunnlag

# Innstallasjon og oppsett

## Python
Installer Python fra https://www.python.org/downloads/

## VSCode
Anbefalt verktøy å bruke for å kjøre koden

### Steg 1
Last ned og installer VScode fra https://code.visualstudio.com/download

### Steg 2
Åpne VSCode og installer Python-utvidelse
<img width="727" alt="2022-10-19-09-41-49" src="https://user-images.githubusercontent.com/9265818/196627959-b735aaa0-749d-463e-9e44-f81c038775b1.png">


## Git
Installer Git for Windows for å hente koden fra Github
https://github.com/git-guides/install-git

For alle valgene om dukker opp i installasjonsprosessen er det bare å velge standard/klikke videre

## Kode og avhengigheter

### Steg 1
Når Git er installert lager du en mappe der du ønsker at koden skal ligge, og åpner Git Bash (verktøy for å  bruke git) her:

<img width="727" alt="2022-10-19-09-42-27" src="https://user-images.githubusercontent.com/9265818/196627986-cd036ad8-e86a-4770-9bf9-95c117178bde.png">


### Steg 2

Klone repoet, slik at koden installeres i mappen, ved å kopiere inn denne snutten i Git Bash
```
git clone https://github.com/kristhaj/pyxcel.git
```

### Steg 3
Naviger til den nye mappen:
```
cd pyxcel
```

og installer det nødvendige pakkene som koden bruker, ved å lime inn følgende kommando:

```
pip install -r requirements.txt
```

# Påkrevde pakker
- pandas
- xlrd
- openpyxl 3.0.4 (version 3.0.5 and newer has an error with appending sheets to an existing excel file)
- xlsxwriter
- xlwt

# Funksjonalitet og bruk

Denne modulen brukes til å samle og formatere data til faktureringsgrunnlag som importeres til Visma.

## Filstruktur
For at koden skal vite hvor filene med importgrunnlag ligger, så må den få beskjed om dette. Filstien er definert i filen launch.json
<img width="727" alt="2022-10-19-09-32-22" src="https://user-images.githubusercontent.com/9265818/196627491-bfa3847e-42f9-4b0a-a9a5-02ea660c3813.png">


data_path: refererer til hovedfilen med data fra ISD om klubb, gruppe og gren

client_details_path: filen inneholder informasjon om hvilke kundenummer o.l. som er knyttet til de ulike klubbene.

product_details_path: filen innholder informasjon om produktene/lisensene som skal faktureres, f.eks. beløp per medlem

template_path: filen har oppsett med kolonneheadere og format som sluttfilen skal ha for å kunne importeres til Visma.

destination_path: plassering og filnavn for den ferdige filen som blir laget.

## Kjøring av kode.

For å kjøre koden åpner man filen Vis.py, og deretter kjører man den i Debug-modus, som vist i bildet under. Dette kan også gjøres ved å trykke på F5
<img width="1122" alt="2022-10-20-09-16-34" src="https://user-images.githubusercontent.com/9265818/196881710-3e936dee-c5ee-4793-b904-130e13a304b4.png">

