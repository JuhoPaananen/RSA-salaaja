# Viikkoraportti 5

**Käytetty aika: n. 10 tuntia**

## Mitä olen tehnyt tällä viikolla
1) Vertaisarviointi: karkeasti puolet viikon käytetystä työajasta. Opiskelin mielenkiinnosta hieman mistä vertaisarvioitavan projektin algoritmeissa ja tietorakenteessa on kyse. Tämän lisäksi keskityin itse koodikatselmointiin, jotta saisin annettua hyödyllistä palautetta.

2) Oman toteutuksen käyttöliittymän kehitys: Sain kuin sainkin toteutettua dynaamisen viestin pituutta/käyttäjän syötettä tarkkailevan tapahtumaseurannan TKinteriin, ja nyt käyttöliittymän tasolla estetään yli 256 tavuisten merkkijonojen syöttäminen. Rajoitus tulee siis 2048 bittisestä salausavaimesta. Aikaa kuluis siis events/bind syntaksiin tutustumiseen ja stackoverflow oli avuksi. Koodiin kommentoitu "lähde".

## Miten ohjelma on edistynyt?
Ohjelma on nyt minun näkökulmastani valmis ja sen pitäisi olla varsin helppokäyttöinen myös täysin uudelle käyttäjälle.

## Mitä opin tällä viikolla?
TKinter kirjaston uudet ominaisuudet. Lisäksi vertaisarvioinnin seurauksena pintaraapaisu Trie-rakenteeseen.

## Mikä jäi epäselväksi tai tuottanut vaikeuksia?
Ei erityisiä huolia.

## Mitä teen seuraavaksi?
Huolehdin dokumentaation lopulliseen kuntoon. Varmistan, että jokaiselle metodille/funktiolle on mielekäs yksikkötestaus ja ajan riittäessä lisään koodiin virheentarkistuksia/-ilmoituksia.
