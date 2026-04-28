# O projektu

Tento trivialni projekt demonstruje vyuziti souboru AGENTS.md, kde se definuje zakladni framework pro nastroj Claude pro
tvorbu jednoduchych ukazkovych aplikaci nad databazovou platformou InterSystems IRIS.

Jelikoz 30 let primarne programuji v ObjectScriptu, neni pro mne uplne jednoduche zacit tvorit stejne dobry kod v jinych jazycich.
Potazmo, kdyz doba, kdy se aplikacni logika odehravala na serveru (CSP, cili ekvivalent JSP, ASP.NET) je nenavratne v trapu.
Takze nezbyva nez pouzit jeden z milionu dnes dostupnych ruznych webovych frameworku, ktere se objevuji a mizi na trhu jako houby po desti (a to  nemluvim o jejich verzich a nekompatibilitach mezi verzemi).

Cilem je ukazatr zakladni manipulaci s daty na platforme InterSystems IRIS - tedy CRUD operace

Takze jsem se rozhodl zvolit Python a Flask, styly se mi libi Google Material desin.

Pro jednoduchost se netrapim s zadnymi kontejnery (byt je samozrejme mozne je pouzit i s InterSystems IRIS)

**Takze toto jsou vychodiska pro obsah souboru AGENTS.md.**
POZN: AGENTS.md stale obsahuje spoustu v mem demo projektu nepouzivaneho balastu, nicmene, to nebrani funkcnosti Claude agentu


Vse ostatni - kod aplikace - je vysledek volani /init a nasledneho promptovani Claude


## mozna vylepseni
- vynutit si generovani REST API na strane InterSystems IRIS serveru, to dovoli vyvojarum znalym InterSystems IRIS vyuzit sve stavajici znalosti serveru pro tvorbu aplikacni logiky
na strane zname platformy
- doplnit agenta pro dokumentovani kodu
- doplnit ukazkovou funkcnost Vector Search ve spojeni s RAG




# spusteni:
source .venv/bin/activate<br>
flask --app app run --host 0.0.0.0 --port 5000


# ukazka UI rozhrani a databaze
![screenshot](./Screenshot%202026-04-28%20210036.png)