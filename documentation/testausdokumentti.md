# Testausdokumentti
RSA-salaajaa on testattu Pythonin ´unittest' kirjaston avulla sekä erityisesti salattavien syötteiden osalta manuaalisesti.

## Testit
Salausavainten luonnista vastaavaa keygen-moduulia testataan 'TestKeyGenerator' luokalla. Tässä keskeistä on julkisen ja salaisen avaimen ominaisuuksien testaus, jotta ne vastaavat vaatimuksia.

Utils-moduulin sisältämiä algoritmeja testataan ´TestPrimeNumberTools´-luokalla. Tämän luokan testit kattavat ohjelman toiminnan kannalta keskeiset alkulukujen käsittelyn metodit. 

Salauksesta vastaava rsa-moduuli testataan 'TestCipher' luokalla. Näissä testeissä pääroolissa on RSA:n mukainen salaus ja salauksen purku moduuliaritmetiikan keinoin.

Käyttöliittymää gui.py ei testata automaattisilla testeillä.

## Testauskattavuus
Testien haaraumakattavuus on hyvä 98%. Puutteita syntyy keygen moduulin generate_keys() funktion while loopin vajaasta testauksesta.

![image](https://github.com/JuhoPaananen/JuhoPaananen.github.io/blob/main/rsaprojekti/pictures/testikattavuus.png)
