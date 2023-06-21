# Käyttöohje
RSA-salaaja on nimensä mukaisesti yksinkertainen RSA-salausohjelma. Ohjelmalla pystyy luomaan 2048 bittisiä salausavaimia ja näin ollen salaamaan noin 200-250 merkkisiä tekstejä.

## Ohjelman asentaminen ja käynnistäminen
1. Kloonaa projekti valitsemaasi sijaintiin 
```bash
git clone git@github.com:JuhoPaananen/RSA-salaaja.git
```
Nyt voit suorittaa ohjelman suorittamalla RSA-salaaja kansion juuressa olevan rsa-salaaja paketin joko tuplaklikkaamalla sitä tai komentorivillä komennolla `./rsa-salaaja`.

Vaihtoehtoisesti voit käynnistää ohjelman poetryn avulla, jolloin myös muut alla olevat komennot (kuten start, test, lint) ovat käytettävissäsi.
 
2. Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:
```bash
poetry install
```
3. Jonka jälkeen ohjelman voi käynnistää komennolla:
```bash
poetry run invoke start
```
## Muut komentorivikäskyt
### Pylint
Koodin laatua voi arvioida suorittamalla kommmennon (käyttöliittymän koodi on ohitettu pylint ajossa):
```bash
poetry run invoke lint
```
### Koodin testaus
Ohjelmakoodin valmiit testit voi ajaa suorittamalla komennon (huom. testit sisältävät yli 2000 bittisten lukujen testauksen, jonka seurauksena testien ajaminen voi viedä useamman minuutin):
```bash
poetry run invoke test
```
Koodin testikattavuusraportin voi suorittaa komennolla:
```bash
poetry run invoke coverage-report
```
Raportti luodaan htmlcov kansioon.

## Ohjelman käynnistäminen
Sovellus käynnistyy päävalikkoon:

![image](https://github.com/JuhoPaananen/JuhoPaananen.github.io/blob/main/rsaprojekti/pictures/appwindow.png)

## Käyttö
Ohjelman käyttämäiseksi tarvitaan hiiri. Seuraavassa on käytettävissä olevat toiminnot:
- Luo avaimet: luo julkisen avainparin muodossa (e N) ikkunaan 1 sekä yksityisen avainparin muodossa (d N) ikkunaan 2.
- Kopioi/Liitä: kopioi/liittää yllä olevan ikkunan sisällön järjestelmän leikepöydälle mahdollista tallentamista tai olemassa olevan avaimen tuomista varten.
- Avainten generointi kesti: ilmoittaa ajan sekuntteina, joka kahden 1024 bittisen alkuluvun ja näistä johdettujen salausavaimien luomiseen kului
- Salaa: salaa ikkunassa 3. olevan tekstisyötteen RSA:n mukaisesti ja tuottaa salatun tuloksen ikkunaan 4. Huom. maksimisyöte on 256 tavua (erikoismerkit vievät 2 tavua). Salaamista varten tulee julkisen avaimen olla syötettynä ikkunaan 1.
- Pura: purkaa ikkunassa 4. olevan salatun syötteen selväkieliseksi tekstiksi ikkunaan 3. Purkamista varten tulee yksityisen avaimen olla syötettynä ikkunaan 2.

## Hauskoja salailuhetkiä!
