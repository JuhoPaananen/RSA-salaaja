# Viikkoraportti 2

**Käytetty aika: 25 tuntia**

## Mitä olen tehnyt tällä viikolla
Viikon työmäärästä suurin osa kului algoritmeihin tutustumiseen sekä niiden toteuttamiseen. Wikipedian Miller-Rabin testin pseudokoodin "kääntäminen" Pythonille oli itselle melko työlästä.
Mielenkiintoista oli myös huomata, että ensin käyttämäni "d = int(d/2)" johti käytännössä koko algoritmin toimimattomuuteen ja minulla meni melkoisesti aikaa huomata sekä korjata tämä "d = d // 2".

Muutoin viikolla aikaa on käytetty pylintin asettamiseen, kooodin dokumentaatioon sekä testien kirjoittamiseen. Yksikkötestaus kattaa koko koodin.

## Miten ohjelma on edistynyt?
Ohjelma generoi nyt 1024 bittisiä alkulukuja tehokkaasti.

## Mitä opin tällä viikolla?
Viikko on mennyt alkulujen parissa niin Eratostheneen seulan kuin myös Miller-Rabinin testin parissa. Näistä on tullut opittua vähän lisää, mutta lisää paneutumista tarvitaan. 
Jonkin verran tutustuin myös muihin alkulukujen generointiin liittyviin algoritmeihin ja niiden ominaisuuksiin Handbook of Applied Cryptography kirjan avulla.

Ensimmäisen viikon vinkki käyttää Eratostheneen seulaa suodattimena toimi kivasti ja Miller-Rabinin testiin menevien alkulukuehdokkaiden määrä pysyi hyvin rajallisena.

## Mikä jäi epäselväksi tai tuottanut vaikeuksia?
Toivottavasti pow() funktion käyttö on sallittu. 

Hieman epäselvää on vielä salaukselle asetettu 1024 bitin vaatimus. Tuleeko tällöin salausavaimen olla 1024 bittinen, jolloin käsittääkseni riittäisi kaksi 
512 bittistä alkulukua joiten tulona on 1024 bittinen luku. Vai tuleeko alkulukujen olla 1024 bittisiä?

Miller-Rabinin testin riittävästä/järkevästä kierrosten määrästä en löytänyt konsensusta. Omassa algoritmissä tämä k on nyt 40.

## Mitä teen seuraavaksi?
Seuraavan viikon tavoitteena on saada salausavainten, salaamisen ja purkamisen osiot valmiiksi. Käsittääkseni tämä edellyttää esimerkiksi Eukleideen algoritmin hyödyntämistä.
