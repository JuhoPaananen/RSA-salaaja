# Viikkoraportti 3

**Käytetty aika: 15 tuntia**

## Mitä olen tehnyt tällä viikolla
Ohjelmaan on lisätty RSA-salauksen toteuttava moduuli. Tätä varten on toteutettu Eukleideen algoritmi vaikka myös valmis gcd-funktio löytyisi Pythonista. Ohjelman koodi on faktoroitu uudelleen poistamalla turhia luokkia ja nimeämällä muuttujia uudestaan (hyvässä ja pahassa). Pylintin mukaan koodi on nyt kuosissa.

## Miten ohjelma on edistynyt?
Ohjelma generoi nyt 1024 bittisiä alkulukuja tehokkaasti. Tuottaa 2048 bittisiä salausavaimia ja salaa sekä purkaa maksimissaan 256 merkkisiä tekstejä.

## Mitä opin tällä viikolla?
Modulaariaritmetiikkaa on tullut selailtua, jotta ymmärtäisin paremmin mitä RSA:ssa todella tehdään ja miksi se on niin tehokas.

## Mikä jäi epäselväksi tai tuottanut vaikeuksia?
Tällä viikolla ei ollut erityisiä epäselvyyksiä. Koodin kanssa tapahtui joitakin aikaa vieviä kömmähdyksiä ja oman aikansa otti myös huomata, että osa erikoismerkeistä vaatii useamman tavun eikä tällöin voida salata 256 merkkiä.

## Mitä teen seuraavaksi?
Aloitan toteutusraportin kirjoittamisen sekä mahdolliset suorituskykytestit. Yksinkertainen käyttöliittymä olisi myös tarkoitus saada kasaan.
