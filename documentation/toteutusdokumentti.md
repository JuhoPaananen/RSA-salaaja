# Toteutusdokumentti

## Kuvaus
Ohjelma RSA-avainparien luomiseksi ja tekstin salaamiseksi/purkamiseksi käyttäen RSA-salausavaimia.

## Rakenne
Ohjelman toiminta koostuu:
- Suurien 1024 bittisen alkulukujen löytäminen
- RSA avainparien luominen
- Tekstisyötteen salaaminen RSA-avaimella
- Salatun syötteen purkaminen RSA-avaimella

## Algoritmit
### Alkuluvut
Alkulukujen löytämiseksi käytetään yhdistelmää Eratostheneen seulasta ja Miller-Rabinin testistä. Seulalla etsitään ensimmäiset alkuluvut 0-1000 välillä. Näin rajataan pois kaikkien seulan tunnistamien alkulukujen monikerrat alkulukukandidaateista, jotka etenevät Miller-Rabinin testiin.

### RSA-avainparit
RSA avaimet luodaan Pythonin valmiilla potenssiinkorotusalgoritmilla [pow()](https://www.w3schools.com/python/ref_func_pow.asp), jossa modulus on N = p*q ja p,q ovat edellä löydettyjä 1024 bittisiä alkulukuja. 

Julkisen avainparin e:n määrittämiseksi etsitään sellainen kokonaisluku väliltä 2-N, joka täyttää ehdon e = 1 mod phi, jossa phi = (p-1)(q-1). Käytännössä hyödynnetään Eukleideen algoritmia, jolla varmisetaan, että satunnaisen e:n ja phi:n suurin yhteinen tekijä on 1. Tätä varten on olemassa myös valmis funktio gcd(), mutta tämä on kuitenkin toteuttu itse. 

Yksityisen avaimen d saadaan mainitulla potenssiinkorotusalgoritmilla pow().

### Salaaminen ja purkaminen.
Salaaminen tapahtuu siten, että tekstimuotoinen syöte muunnetaan bittien kautta kokonaisluvuksi joka korotetaan potenssin e ja jonka jakojäännös modulus N on sitten salattu viesti.

Purkaminen on käänteinen operaatio, jossa salattu viesti (suuri kokonaisluku) korotetaan potenssiin e ja jonka jakojäännös modulus N on oikea viesti kokonaislukuna. Tämä käännetään bittien kautta tekstiksi.

Operaatioihin käytetään pow() funktiota. Purkamisen toiminta voidaan osoittaa [Fermant'n pienen lauseen](https://fi.wikipedia.org/wiki/Fermat%E2%80%99n_pieni_lause) avulla.

## Aikavaativuus
**Täydentyy..**
- Eratostheneen seula: O(n log(log(n))), jossa n = 1000, eli tämä on vakio
- Miller-Rabin: O(k log(n)), missä k=40 ja n = 1024 bittinen luku.
- Avaimen luominen: Eratosthene + Miller-Rabin x 2 + potenssiinkorotusalgoritmit. Näistä Miller-Rabin aikavaativuus korkein, eli jotain O(2k log(n)), koska kaksi alkulukua tulee löytää.
- Salaaminen ja purkaminen: täytyy selvittää pow() aikavaativuus.
