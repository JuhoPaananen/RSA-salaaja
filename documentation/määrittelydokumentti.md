# Määrittelydokumentti

## RSA-salaaja
Harjoitustyössä tullaan toteuttamaan yksinkertainen teksti-/graafisen käyttöliittymän RSA-salaaja tekstille. Salaajan sisältyy julkisen ja yksityisen avaimen luonti sekä viestin salaaminen ja purkaminen avaimia käyttäen.

### Käytettävät kielet
Harjoitustyö toteutetaan Python ohjelmointikielellä. Vertaisarvioinnit tehdään mieluiten niin ikään Python-kielisille toteutuksille, mutta tarvittaessa myös Java-toteutuksia voin arvioida varauksin.

### Algoritmit ja tietorakenteet
Alustavasti tunnistetut tarvittavat algoritmit, jotka voivat tarkentua työn edetessä:

**1. Avaimet**
- Alkulukujen valitsemiseen Eratostheneen seula tai Miller-Rab alkulukutesti
- Satunnaisen kokonaisluvun valintaan Eukleideen algoritmi

**2. Salaus**
- Potenssiinkorotusalgoritmi

**3. Purku**
- Potenssiinkorotusalgoritmi

En ole tunnistanut erityisiä tietorakenteita, joita toteutus vaatisi.

### Ratkaistava ongelma ja algoritmien valinta
Harjoitustyön toteutuksella pyritään luomaan avainpareja, joilla voidaan salata ja purkaa tekstiä avoimen avaimen avulla. Yllä esitetyt algoritmit on valittu alustavan selvitystyön perusteella, ja näillä tulisi pystyä toteuttamaan salaukseen/purkuun vaadittavat toimenpiteet.

### Ohjelman syötteet ja käyttö
Harjoitustyössä toteutettava ohjelma kykenee luomaan avainpareja. Avainpareja voidaan käyttää salaamaan ohjelmaan syötettyä tekstiä ja edelleen oikeilla avainpareilla ohjelma purkaa salattua tekstiä. Alustavana tavoitteena on luoda yksinkertainen graafinen käyttöliittymä ohjelman käyttämiseksi.

### Aika- ja tilavaativuudet
Ei määritelty vielä

### Lähteet
[Wikipedia: RSA](https://fi.wikipedia.org/wiki/RSA)

[Wikipedia: Potenssiinkorotusalgoritmi](https://fi.wikipedia.org/wiki/Potenssiinkorotusalgoritmi)

### Opinto-ohjelma ja käytettävät kielet
Kurssi toteutetaan osana tietojenkäsittelytieteen kandidaatin (TKT) opintoja.

Kurssin dokumentaatio on suomeksi, mutta projektin koodi kirjoitetaan englanniksi.
