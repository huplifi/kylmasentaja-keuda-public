---
title: "Sähköpiirustukset ja valaistuskytkennät"
publish: true
---

Tavoite on osata **lukea olemassa olevaa sähköpiirustusta ja päivittää piirustus tehdyn muutoksen jälkeen** niin, että ILP:n tai muun kylmälaitteen sähköliitännästä voidaan selvittää olennaiset asiat: mistä syöttö tulee, mikä ryhmä on kyseessä, mitä suojalaitteita ja erotuslaitteita piirissä on, missä liitos- ja kytkentäpisteet sijaitsevat ja miten laite liittyy olemassa olevaan asennukseen.

Tämä muistio käsittelee piirustusten lukemista. Se ei itsessään anna oikeutta tehdä sähköasennuksia.

## Mitä piirustuksesta pitää ensimmäisenä löytää?

Kun saat sähköpiirustuksen eteesi, etene tässä järjestyksessä:

1. **Syöttö:** mistä keskus- ja ryhmästä piiri tulee?
2. **Jännite ja vaiheet:** onko kyse 1- vai 3-vaiheisesta syötöstä?
3. **Suojalaitteet:** sulake/johdonsuojakatkaisija, vikavirtasuoja ja niiden merkinnät.
4. **Johtimet:** L/L1–L3, N, PE tai PEN sekä johdin- tai kaapelitiedot, jos ne on merkitty.
5. **Liitoskohdat:** jakorasiat, liittimet, pistorasiat ja muut haaroitukset.
6. **Ohjaus:** kytkimet, kontaktorit, releet, termostaatit ja muut ohjaavat komponentit.
7. **Kuorma:** valaisin, moottori, puhallin, kompressori, lämmitin tai muu laite.
8. **Erotus:** miten laite voidaan erottaa sähköverkosta huoltoa varten?
9. **Muutokset:** jos asennusta muutetaan, mikä osa piirustuksesta on päivitettävä vastaamaan toteutusta?

Piirustusta ei lueta vain symboli kerrallaan. Tavoite on seurata **toiminnallista reittiä syötöstä kuormalle ja takaisin** sekä erottaa käyttövirtapiiri, suojaus ja ohjaus toisistaan.

## Kolme tavallista esitystapaa

### Periaatekaavio

Näyttää sähköisen toimintaperiaatteen mahdollisimman selkeästi. Komponenttien fyysinen sijainti ei ole pääasia.

### Moniviivainen johdotuskaavio

Johtimet esitetään erillisinä. Tästä voidaan nähdä esimerkiksi jakorasian sisäiset liitokset ja se, mikä johdin menee millekin laitteelle.

### Yksiviivainen esitys

Useita johtimia voidaan esittää yhdellä johdotusreitillä. Lisämerkeillä kerrotaan johtimien määrä tai tyyppi. Tämä on kompakti tapa näyttää asennuksen rakenne, mutta kaikkia sisäisiä liitoksia ei nähdä suoraan.

**Ole tarkkana:** sama graafinen yksityiskohta voi merkitä eri asiaa eri esitysyhteydessä. Esimerkiksi moniviivaisen kaavion musta piste on liitoskohta. Symbolit luetaan aina piirustuksen selitteen ja käytetyn esitystavan yhteydessä.

## Perusmerkinnät

| Merkintä   | Merkitys                                                                                                                |
| ---------- | ----------------------------------------------------------------------------------------------------------------------- |
| L          | vaihe                                                                                                                   |
| L1, L2, L3 | kolmivaihejärjestelmän vaiheet                                                                                          |
| N          | nollajohdin                                                                                                             |
| PE         | suojajohdin                                                                                                             |
| PEN        | yhdistetty suoja- ja nollajohdin                                                                                        |
| X          | liitin, liitinrima tai liitäntäpiste; tarkka käyttö selviää piirustuksesta                                              |
| Q          | kytkinlaite; esimerkiksi kytkin tai katkaisija                                                                          |
| E          | kulutuskojeen tai laitteen tunnus voi esiintyä valaistusesimerkeissä; tarkista aina piirustuksen laitetunnusjärjestelmä |

Laitetunnukset eivät ole sama asia kuin piirrosmerkit. Esimerkiksi oppitunnin valaistuskuvassa **X1** on jakorasia, **Q1** kytkin ja **E1** valaisin.

## Johtimet ja liitokset

### Johdin

Yhtenäinen viiva kuvaa sähköistä yhteyttä tai johdotusreittiä esitystavasta riippuen.

![Sähköpiirrosmerkki: johdin](symbolit/johdin.svg)

### Liitoskohta

Risteävien tai haarautuvien johtimien musta piste osoittaa sähköisen liitoksen.

![Sähköpiirrosmerkki: liitoskohta](symbolit/liitoskohta.svg)

### Haaroitus

![Sähköpiirrosmerkki: haaroitus](symbolit/haaroitus.svg)

### Nolla- ja suojajohdin

Oppitunnilla käytetyssä yksiviivaisessa merkintätavassa pistepäinen poikkimerkki osoittaa N-johtimen ja T-mäinen poikkimerkki PE-johtimen. IEC 60617 -vertailuaineistossa N-, PE- ja PEN-johtimille on omat johdinmerkintänsä (PDF s. 20).

![Sähköpiirrosmerkki: nollajohdin](symbolit/nollajohdin.svg)

![Sähköpiirrosmerkki: suojajohdin](symbolit/suojajohdin.svg)

Piirustuksen oma selite ratkaisee aina tulkinnan.

## Rasiat ja liitynnät

### Jakorasia

Jakorasia on kohta, jossa johtimia voidaan liittää ja haaroittaa. Oppitunnin 1- ja 5-kytkinesimerkeissä jakorasia on merkitty tunnuksella X1.

![Sähköpiirrosmerkki: jakorasia](symbolit/jakorasia.svg)

### Suojakoskettimellinen pistorasia

![Sähköpiirrosmerkki: pistorasia suojakosketin](symbolit/pistorasia-suojakosketin.svg)

ILP:n kohdalla pistorasian olemassaolo ei yksin ratkaise liitännän sopivuutta. Tukesin mukaan pistotulppaliitäntäisen ILP:n pistorasian pitää olla maadoitettu ja sijaita sen yksikön vieressä, johon valmistaja on suunnitellut sähköliitännän. Kiinteä liitäntä, uuden pistorasian tai turvakytkimen asentaminen, vikavirtasuojan lisääminen tai pistorasian siirtäminen edellyttää sähkötyöoikeutta.

## Kytkimet ja valaistuskytkennät

### 1-kytkin, yksinapainen kytkin

Yksi kytkin ohjaa yhtä valaisinta tai valaisinryhmää yhdestä paikasta.

![Sähköpiirrosmerkki: kytkin 1](symbolit/kytkin-1.svg)

Oppitunnin esimerkissä:

- X1 = jakorasia
- Q1 = 1-kytkin
- E1 = valaisin

Jakorasiassa N ja PE jatkuvat valaisimelle. L viedään kytkimelle ja kytkimeltä palaava **kytketty vaihe** jatkuu valaisimelle.

Toimintareitti kytkimen ollessa suljettuna:

**L → X1 → Q1 → X1 → E1 → N**

| Väli        | Toiminnalliset johtimet     | Määrä |
| ----------- | --------------------------- | ----: |
| syöttö → X1 | L, N, PE                    |     3 |
| X1 → Q1     | L + kytketty vaihe takaisin |     2 |
| X1 → E1     | kytketty vaihe, N, PE       |     3 |

### 5-kytkin, sarjakytkin eli kruunukytkin

5-kytkimessä on kaksi erikseen käytettävää kytkintoimintoa samassa kytkimessä. Oppitunnin esimerkissä Q1.1 ja Q1.2 ohjaavat kahta valaisinryhmää toisistaan riippumatta.

![Sähköpiirrosmerkki: kytkin 5 kruunu](symbolit/kytkin-5-kruunu.svg)

Periaate:

**L → Q1.1 → valaisinryhmä 1 → N**

**L → Q1.2 → valaisinryhmä 2 → N**

1-kytkimen kytkinhaarassa on yksi kytketyn vaiheen paluu. 5-kytkimessä niitä on kaksi, koska ohjattavia lähtöjä on kaksi. Oppitunnin yksiviivaisessa kuvassa tämä näkyy suurempana johdinmääränä kytkinhaarassa ja valaisinmerkinnässä **1+2**.

### 6-kytkin eli vaihtokytkin

Vaihtokytkennässä sama valaisin tai valaisinryhmä voidaan sytyttää ja sammuttaa **kahdesta eri paikasta**. Kytkennässä käytetään kahta 6-kytkintä.

![Sähköpiirrosmerkki: kytkin 6](symbolit/kytkin-6.svg)

Oppikirjan esimerkissä:

- **Q1** ja **Q2** = vaihtokytkimet
- **X1** ja **X2** = jakorasiat
- **E1** = valaisin

Vaihtokytkin ohjaa vaiheen kahden vaihtoehtoisen reitin välille. Kahden kytkimen välillä kulkevien johtimien avulla virtareitti voidaan muodostaa tai katkaista kummasta tahansa kytkinpaikasta.

Oppikirjan mukaan vaihtokytkin on paljon käytetty kytkintyyppi, ja sitä käytetään yleisesti myös tavallisen 1-kytkimen tapaan.

### 7-kytkin eli ristikytkin

Kun samaa valoa halutaan ohjata **kolmesta tai useammasta paikasta**, kahden 6-kytkimen väliin lisätään yksi tai useampi 7-kytkin eli ristikytkin.

![Sähköpiirrosmerkki: kytkin 7](symbolit/kytkin-7.svg)

Kolmen ohjauspisteen esimerkissä:

- **Q1** = 6-kytkin
- **Q2** = 7-kytkin
- **Q3** = 6-kytkin
- **X1–X3** = jakorasiat
- **E1** = valaisin

Ristikytkin vaihtaa kahden välijohtimen yhteydet keskenään. Jokainen kytkimen käyttö muuttaa virtareittiä, joten valon tila voidaan vaihtaa mistä tahansa ohjauspisteestä.

**Muistisääntö:** kaksi 6-kytkintä muodostavat päät. Niiden väliin voidaan lisätä 7-kytkimiä niin monta ohjauspaikkaa varten kuin tarvitaan.

### Painikeohjaus useasta paikasta

Oppikirjan mukaan useasta paikasta tehtävässä valaistuksen ohjauksessa vaihto- ja ristikytkimien sijasta voidaan käyttää **askelrelettä ja painikkeita**.

![Sähköpiirrosmerkki: painike](symbolit/painike.svg)

Oppikirjan esimerkissä:

- **K1** = askelrele
- **S1–S3** = painikkeet
- **E1–E3** = valaisimet
- **X1–X4** = jakorasiat
- **S3** on esitetty merkkivalollisena painikkeena.

Painikkeet antavat ohjausimpulssin askelreleelle. Rele vaihtaa valaistuksen tilaa, jolloin samaa valaistusta voidaan ohjata useasta painikepaikasta ilman pitkää vaihto-/ristikytkinketjua.

### Valonsäädin

Oppikirjan valonsäätimessä on sekä kytkin että säätöyksikkö. Kun säätimeen sisältyy vaihtokytkintoiminto, valot voidaan sytyttää ja sammuttaa myös toisesta paikasta tavallisella 6-kytkimellä.

Kirjastossa ei vielä ole lähdekuvien mukaista valonsäätimen asennussymbolia, joten sitä ei korvata arvauksella. Symboli lisätään kirjastoon vasta, kun grafiikka piirretään lähdekuvan perusteella.

Oppikirja korostaa myös, että valonsäädin on valittava ohjattavan valonlähteen ja liitäntälaitteen mukaan.

### Kytkinten liitinmerkintöjä

Oppikirjan tekstin mukaan:

- vaihejohtimen liitin on merkitty kytkimessä **L**- tai **P**-kirjaimella
- lampulle tai toiselle kytkimelle lähtevien johtimien liittimet on merkitty **nuolilla**
- ylimääräisiä kytkentäliittimiä voidaan merkitä **X**- tai **B**-kirjaimella.

Nämä ovat hyödyllisiä merkintöjä erityisesti silloin, kun piirustusta verrataan oikean kytkimen liittimiin.

### Valaisin

![Sähköpiirrosmerkki: valaisin](symbolit/valaisin.svg)

## Suojaus ja erotus

### Sulake

![Sähköpiirrosmerkki: sulake](symbolit/sulake.svg)

### Johdonsuojakatkaisija

![Sähköpiirrosmerkki: johdonsuojakatkaisija](symbolit/johdonsuojakatkaisija.svg)

### Turvakytkin / paikallinen erotus

![Sähköpiirrosmerkki: turvakytkin](symbolit/turvakytkin.svg)

ILP:n kannalta erotus on erityisen tärkeä. Tukesin mukaan **kiinteästi liitetyn ilmalämpöpumpun erotuslaitteeksi on asennettava turvakytkin**. Pistotulppaliitäntäisessä laitteessa pistotulppa voi toimia hyväksyttävänä erotustapana, kun liitäntä on toteutettu vaatimusten mukaisesti.

## Kylmälaitteissa vastaan tulevia kuormia

### Moottori

![Sähköpiirrosmerkki: moottori](symbolit/moottori.svg)

Moottorisymboli voi liittyä esimerkiksi kompressoriin tai puhaltimen moottoriin. Pelkkä M-symboli ei kerro laitteen koko toimintoa, vaan se päätellään laitetunnuksesta, kaaviosta ja selitteestä.

### Puhallin

![Sähköpiirrosmerkki: puhallin](symbolit/puhallin.svg)

IEC 60617 -vertailuaineiston sivulla 52 on puhaltimen ja pumpun symboliesimerkkejä.

## ILP/kylmälaite: mitä olemassa olevasta piirustuksesta selvitetään?

Kun tarkoitus on arvioida, **miten laite voidaan sähköisesti liittää olemassa olevaan kohteeseen**, piirustuksesta ja kohteesta pitää pystyä yhdistämään ainakin seuraavat tiedot:

- mistä keskuksesta ja ryhmästä suunniteltu syöttö tulee
- 1- vai 3-vaihesyöttö ja nimellisjännite
- suojalaitteen tyyppi ja nimellisarvo
- onko piirissä vikavirtasuoja ja mitä se suojaa
- johdin-/kaapelityyppi ja poikkipinta, jos ne on dokumentoitu
- PE:n jatkuvuus ja maadoitettu liitäntä
- pistorasia vai kiinteä liitäntä
- laitteen paikallinen erotustapa
- mahdolliset kontaktorit, releet, termostaatit tai ulkoiset ohjaukset
- laitteen valmistajan vaatima sähköliitäntä
- vastaako toteutunut asennus piirustusta

**Piirustus ei yksin todista olemassa olevan asennuksen kuntoa tai sitä, että uusi kuorma voidaan lisätä.** Suunnitelmaa verrataan todelliseen asennukseen, laitteen valmistajan tietoihin ja tarvittaviin mitoituksiin ja mittauksiin.

Tukesin mukaan ILP:n kiinteä sähköliitäntä edellyttää vähintään S3-ryhmän oikeutta sähkötöihin. Sama koskee esimerkiksi uuden pistorasian tai turvakytkimen asentamista, vikavirtasuojan lisäämistä ja olemassa olevan pistorasian siirtämistä.

Tämä on toiminnanharjoittajan ja sähkötöiden johtajan oikeuden rajaus. Oppitunnin 6.11.2026 esimerkki, jossa ilmalämpöpumppu mainitaan laitetöiden kohteena, kuvaa sähköturvallisuuslain 73 §:n 4 momentin kapeaa ammattitaitoa. Se ei anna automaattisesti kelpoisuutta uuteen syöttöpiiriin tai keskukseen lisättävään vikavirtasuojaan. S3-johtaja voi asentaa yhden syöttöjohdon rasialta tai jakokeskukselta vain, kun keskuksen rakennetta ei muuteta. Vikavirtasuojan lisäys edellyttää vähintään S3-ryhmän oikeutta sähkötöihin. Jos lisäys muuttaa keskuksen rakennetta tai työ on laajempi asennuskokonaisuus, Tukes edellyttää johtajalta vähintään S2-pätevyyttä. Raja on avattu muistiossa [Sähkötöiden tekemisen oikeus](sahkoopin-perusteet.md#sähkötöiden-tekemisen-oikeus).

## Piirustuksen päivittäminen muutoksen jälkeen

Tavoite ei ole vain lukea vanhaa kuvaa vaan jättää jälkeemme **as-built**, toteutusta vastaava dokumentti.

Kun sähköasennukseen tehdään muutos, piirustukseen merkitään soveltuvin osin:

- uusi tai muuttunut laite ja sen laitetunnus
- syöttävä keskus ja ryhmä
- muuttunut johdotusreitti ja liitospisteet
- kaapeli-/johdintiedot
- suoja- ja erotuslaitteet
- muuttuneet ohjaus- tai kytkentäyhteydet
- tarvittavat tekniset tunnukset ja selitteet

Piirustuksessa käytetään samaa symboliikkaa, nimeämislogiikkaa ja esitystapaa johdonmukaisesti. Vanhaa piirustusta ei vain piirretä kauniimmaksi: **lopputuloksen pitää vastata todellista asennusta.**

## Visuaalinen symbolisanasto

Alla olevat symbolit ovat tämän vaultin tarkistettua SVG-kirjastoa. Niitä käytetään tästä eteenpäin muistiinpanojen sähkökaavioissa aina, kun vastaava käsite esiintyy.

### Johtimet ja liitokset

| Symboli                                                                      | Nimi                            | Mitä luetaan piirustuksesta                                                                                                        |
| ---------------------------------------------------------------------------- | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| ![Sähköpiirrosmerkki: johdin](symbolit/johdin.svg)                           | Johdin tai kaapeli, yleismerkki | Sähköinen yhteys; yksiviivaisessa esityksessä myös johdotusreitti.                                                                 |
| ![Sähköpiirrosmerkki: liitoskohta](symbolit/liitoskohta.svg)                 | Johtimien liitoskohta           | Täytetty piste kertoo sähköisestä liitoksesta.                                                                                     |
| ![Sähköpiirrosmerkki: haaroitus](symbolit/haaroitus.svg)                     | T-haaroitus                     | Johtimien sähköinen haaroitus.                                                                                                     |
| ![Sähköpiirrosmerkki: risteys ei liitosta](symbolit/risteys-ei-liitosta.svg) | Risteys ilman liitosta          | Kirjaston havainnollistus kahdesta sähköisesti erillisestä johtimesta. Esitystapa tarkistetaan aina kohdepiirustuksen selitteestä. |
| ![Sähköpiirrosmerkki: vaihejohdin](symbolit/vaihejohdin.svg)                 | Vaihejohdin L                   | Vaihe tai vaihejohtimen lisämerkintä.                                                                                              |
| ![Sähköpiirrosmerkki: nollajohdin](symbolit/nollajohdin.svg)                 | Nollajohdin N                   | Nollajohdin yksiviivaisessa esityksessä.                                                                                           |
| ![Sähköpiirrosmerkki: suojajohdin](symbolit/suojajohdin.svg)                 | Suojajohdin PE                  | Suojajohdin yksiviivaisessa esityksessä.                                                                                           |
| ![Sähköpiirrosmerkki: pen johdin](symbolit/pen-johdin.svg)                   | PEN-johdin                      | Yhdistetty suoja- ja nollajohdin.                                                                                                  |

### Rasiat, liitynnät ja asennuskytkimet

| Symboli                                                                                | Nimi                             | Käyttö                                                                                                                                         |
| -------------------------------------------------------------------------------------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Sähköpiirrosmerkki: liitin](symbolit/liitin.svg)                                     | Liitin                           | Johtimen liitäntäpiste.                                                                                                                        |
| ![Sähköpiirrosmerkki: liitinrima](symbolit/liitinrima.svg)                             | Liitinrima                       | Useiden liittimien ryhmä.                                                                                                                      |
| ![Sähköpiirrosmerkki: jakorasia](symbolit/jakorasia.svg)                               | Jakorasia                        | Liitosten ja haaroitusten rasia.                                                                                                               |
| ![Sähköpiirrosmerkki: pistorasia](symbolit/pistorasia.svg)                             | Pistorasia, yleismerkki          | Pistorasia ilman erikseen osoitettua suojakosketinta.                                                                                          |
| ![Sähköpiirrosmerkki: pistorasia suojakosketin](symbolit/pistorasia-suojakosketin.svg) | Suojakoskettimellinen pistorasia | Maadoitettu pistorasia.                                                                                                                        |
| ![Sähköpiirrosmerkki: kytkin 1](symbolit/kytkin-1.svg)                                 | 1-kytkin, yksinapainen kytkin    | Yhden valaisinryhmän ohjaus yhdestä paikasta.                                                                                                  |
| ![Sähköpiirrosmerkki: kytkin 5 kruunu](symbolit/kytkin-5-kruunu.svg)                   | 5-kytkin, sarja-/kruunukytkin    | Kaksi erillistä ohjausta samasta kytkinpaikasta. Grafiikka perustuu oppituntiesimerkkiin; IEC-PDF ei yksin vahvista juuri tätä asennusmerkkiä. |
| ![Sähköpiirrosmerkki: kytkin 6](symbolit/kytkin-6.svg)                                 | 6-kytkin, vaihtokytkin           | Ohjauksen osa, kun samaa kuormaa ohjataan kahdesta paikasta.                                                                                   |
| ![Sähköpiirrosmerkki: kytkin 7](symbolit/kytkin-7.svg)                                 | 7-kytkin, ristikytkin            | Kahden vaihtokytkimen väliin sijoitettava lisäohjauspiste.                                                                                     |

### Suojaus ja erotus

| Symboli                                                                          | Nimi                               | Rajaus                                                                                                                           |
| -------------------------------------------------------------------------------- | ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| ![Sähköpiirrosmerkki: sulake](symbolit/sulake.svg)                               | Sulake                             | Ylivirtasuojauksen sulake.                                                                                                       |
| ![Sähköpiirrosmerkki: katkaisija](symbolit/katkaisija.svg)                       | Katkaisija                         | IEC-lähdeaineiston katkaisijan yleismerkki.                                                                                      |
| ![Sähköpiirrosmerkki: johdonsuojakatkaisija](symbolit/johdonsuojakatkaisija.svg) | Johdonsuojakatkaisija, yleisesitys | Käyttää katkaisijan yleisgeometriaa; todellisessa piirustuksessa tarvitaan laitteen tyyppi, napaluku ja nimellisarvot.           |
| ![Sähköpiirrosmerkki: vikavirtasuoja](symbolit/vikavirtasuoja.svg)               | Vikavirtasuoja, toimintolohko      | Kirjaston RCD-hahmotelma, ei varmennettu IEC-symboli. Todellinen RCD esitetään suunnitelman symboliikan ja laitetietojen mukaan. |
| ![Sähköpiirrosmerkki: erotuskytkin](symbolit/erotuskytkin.svg)                   | Kuormanerotuskytkin                | IEC-lähdeaineistoon vertailtu erotus-/kytkintoiminto.                                                                            |
| ![Sähköpiirrosmerkki: turvakytkin](symbolit/turvakytkin.svg)                     | Turvakytkin, yleisesitys           | Käyttötarkoitus on paikallinen turvallinen erotus. Grafiikka ei yksin kerro lukittavuutta, napalukua tai laitteen soveltuvuutta. |

### Kylmälaitteissa tavallisia kuormia

| Symboli                                                              | Nimi                                 | Rajaus                                                                                                                                            |
| -------------------------------------------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Sähköpiirrosmerkki: moottori](symbolit/moottori.svg)               | Moottori, yleismerkki                | Sähkömoottori; laitteen tehtävä selviää tunnuksesta ja selitteestä.                                                                               |
| ![Sähköpiirrosmerkki: moottori 1v](symbolit/moottori-1v.svg)         | Yksivaihemoottori                    | Yksivaiheinen moottori.                                                                                                                           |
| ![Sähköpiirrosmerkki: moottori 3v](symbolit/moottori-3v.svg)         | Kolmivaihemoottori                   | Kolmivaiheinen moottori.                                                                                                                          |
| ![Sähköpiirrosmerkki: kompressori](symbolit/kompressori.svg)         | Kompressori, moottorin yleisesitys   | Kirjastossa moottoripohjainen käyttösymboli. IEC-aineisto ei anna erillistä kompressorisymbolia, joten laitetunnus ja selite ovat välttämättömiä. |
| ![Sähköpiirrosmerkki: puhallin](symbolit/puhallin.svg)               | Puhallin                             | Puhallin sähköliitäntöineen.                                                                                                                      |
| ![Sähköpiirrosmerkki: lammitin](symbolit/lammitin.svg)               | Lämmityselementti                    | Esimerkiksi sähkövastus tai sulatuslämmitin.                                                                                                      |
| ![Sähköpiirrosmerkki: termostaatti no](symbolit/termostaatti-no.svg) | Lämpötilakytkin, sulkeutuva kosketin | Lämpötilan vaikutuksesta sulkeutuva kosketin.                                                                                                     |
| ![Sähköpiirrosmerkki: termostaatti nc](symbolit/termostaatti-nc.svg) | Lämpötilakytkin, avautuva kosketin   | Lämpötilan vaikutuksesta avautuva kosketin.                                                                                                       |
| ![Sähköpiirrosmerkki: kontaktori](symbolit/kontaktori.svg)           | Kontaktori                           | Kuorman sähköinen kytkentä ohjauspiirillä.                                                                                                        |
| ![Sähköpiirrosmerkki: rele kela](symbolit/rele-kela.svg)             | Releen kela                          | Releen ohjauskela.                                                                                                                                |

### Kuuden tarkistuskohdan tulos 28.9.2026

SESKO vahvistaa, että Suomessa sähkökaavioiden standardoitu viite on IEC 60617 -tietokanta ja että symbolien datalehdet sisältävät nimen, tunnuksen, soveltamisohjeet ja statuksen. IEC:n nykyinen tietokanta on IEC 60617:2026 DB.

Kirjaston kuudesta aiemmin epävarmaksi merkitystä kohdasta:

- **Risteys ilman liitosta:** käsite on IEC-aineistossa olemassa, mutta kirjaston nykyistä tarkkaa johtimien risteysgeometriaa ei ole vahvistettu käytettävissä olevasta sähköjohtimien lähdeaineistosta. Säilytetään havainnollistavana ja merkitään tarkistettavaksi.
- **5-kytkin / sarja-/kruunukytkin:** toiminta ja suomalainen opetuskäyttö vahvistuvat oppituntiaineistosta. Toimitettu IEC-kooste ei yksiselitteisesti vahvista nykyistä asennuspiirustusgrafiikkaa, joten grafiikka säilyy opetussymbolina eikä sitä nimetä viralliseksi IEC-symboliksi.
- **Johdonsuojakatkaisija:** IEC-kooste vahvistaa **Circuit Breaker** -yleismerkin. Johdonsuojakatkaisijan tarkka ominaisuus ei ilmene pelkästä yleismerkistä; laitetiedot täydentävät tulkinnan.
- **Vikavirtasuoja:** toimitetusta IEC-koosteesta ei löydy erillistä RCD-merkkiä. Nykyinen SVG on siksi nimenomaan toimintolohko, ei standardoiduksi väitetty piirrosmerkki.
- **Turvakytkin:** IEC-kooste vahvistaa kuormanerotuskytkimen / switch-disconnectorin symboliikan, mutta ei erillistä yleispätevää “turvakytkin”-grafiikkaa. Tukes edellyttää kiinteästi liitetylle ILP:lle turvakytkintä; piirustuksessa laitteen todellinen tyyppi ja ominaisuudet on yksilöitävä.
- **Kompressori:** IEC-kooste vahvistaa koneen/moottorin yleismerkit, mutta ei erillistä kompressorimerkkiä. Siksi kompressori merkitään kirjastossa moottoripohjaisena käyttösymbolina ja yksilöidään laitetunnuksella.

Näin kirjasto erottaa kolme asiaa toisistaan: **lähdevertailtu standardimerkki**, **standardimerkistä sovellettu käyttösymboli** ja **opiskelua varten tehty havainnollistus**. Tätä eroa ei saa häivyttää piirustuksia päivitettäessä.

## Keskuskaavio ja asennuspiirustusten merkit (28.9.2026)

Oppitunnilla korostettiin, että keskuksen ryhmäkaavioita ja asennuspiirustusten piirrosmerkkejä on osattava **lukea käytännössä**. Alla ovat kirjan esimerkeistä poimitut lukuharjoitukset, eivät kopio piirrosmerkkitaulukosta.

### Ryhmäkaavion lukureitti

*Sähkön asentaminen II*, kuva 3.31b (s. 134–135): aloita syötöstä `3L, N, PE`, seuraa pääkytkintä `Q01 63 A`, mahdollista vikavirtasuojaa ja ryhmän johdonsuojaa. Yhdistä vasemmalla näkyvä lähtö oikealla samaan ryhmänumeroon ja lue nimitys, suojan tyyppi/nimellisvirta, teho ja kaapeli. Tyhjä kW-kenttä ei kerro kuorman tehoa.

Esimerkiksi ryhmän `1.1` suojaksi on merkitty `C10` ja kaapeliksi `MMJ 3×1,5S`; ryhmissä `3.1` ja `4.1` näkyvät `C16` ja `MMJ 3×2,5S`. `C` on katkaisijan laukaisukäyrä ja luku nimellisvirta ampeereina. Ryhmät 2.1–2.3, 3.1–3.3 ja 4.1–4.3 jakautuvat vaiheille L1–L3. VSK tarkoittaa vikavirtasuojaa. Valokuvasta ei voi varmistaa kaikkia vikavirtasuojan tarkkoja laitearvoja; ne luetaan alkuperäisestä piirustuksesta.

### Asennuspiirustuksen merkkiryhmät

*Sähkön asentaminen II*, harjoitustehtävä 7.2, s. 69:

| Ryhmä            | Tunnista ainakin                                                                                                                                             |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Tilan olosuhteet | Kostea ja märkä tila (pisaramerkit), palovaarallinen tila `Pa`, kuuma tai kylmä tila `T`.                                                                    |
| Johdotus         | `L`, `N`, `PE`, `PEN` sekä yhdistelmät `3L`, `2L+N`, `L+N+PE` ja `3L+N+PE`. Poikkiviivat ja piste-/PE-lisämerkit luetaan aina kyseisen kuvan selitteellä.    |
| Kytkimet         | 1-napainen, 2- ja 3-napainen; 5-kytkin (kruunu), 6-kytkin (vaihto), 7-kytkin (risti); kaksoiskytkimet 1+1, 1+6 ja 6+6 sekä aikakytkin.                       |
| Ohjaus           | Himmennin, painike ja merkkivalollinen painike, hämäräkytkin, liiketunnistin ja merkkilamppu.                                                                |
| Pistorasiat      | Suojakoskettimeton/suojakoskettimellinen, kaksi- ja kolmiosainen, kytkimellinen, turva- ja suojajännitepistorasia sekä 5-napainen `3L+N+PE`-voimapistorasia. |
| Rasiat ja maa    | Jakorasia, liitäntärasia, kojerasia, maadoitus ja suojamaadoitus.                                                                                            |

**Kertaa ensin L/N/PE/PEN, sitten 1/5/6/7-kytkimet sekä jakorasia–liitäntärasia–kojerasia.** Graafiset erot ovat osin pieniä: vertaa merkit alkuperäiseen harjoituskuvaan, älä päättele niitä vain tästä tekstistä. Lähdekuvaa ei kopioida julkiselle sivustolle.

## Symbolistandardit ja oma SVG-kirjasto

SESKOn mukaan sähkökaavioiden standardoidut piirrosmerkit löytyvät **IEC 60617** -tietokannasta. Sähköpiirustusten esittämistä käsittelee **SFS-EN 61082-1**. IEC 60617 -tietokanta sisältää symbolien lisäksi nimet, tunnukset, soveltamisohjeita ja tiedon symbolien statuksesta.

Tämän vaultin `symbolit/`-hakemiston SVG:t ovat **itsenäisesti piirrettyjä opiskelugrafiikoita**, eivät IEC:n virallisten symbolitiedostojen kopioita. Niiden tarkoitus on tehdä omista muistiinpanoista ja harjoituspiirustuksista yhtenäisiä.

Avoimeen julkaisuun ei vielä lisätä lisenssiä, joka väittäisi standardoitujen piirrosmerkkien virallisen grafiikan olevan vapaasti uudelleenlisensoitavissa. Ennen erillisen avoimen symbolipaketin julkaisua tarkistetaan symboli kerrallaan nimi, geometria, IEC 60617 -status ja käyttöoikeus.

## Koskettimet ja käyttöluokat (9.11.2026)

### Koskettimen perusasento ja toiminta

NO ja NC kuvaavat koskettimen tilaa ennen ohjaavaa toimintaa. Muistisääntö: **NO on aluksi auki, NC on aluksi kiinni.**

| Kosketin                              | Perusasento ja toiminta                                                                                            |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Sulkukosketin, NO (*normally open*)   | Perusasennossa auki; toimittaessa sulkeutuu.                                                                       |
| Avauskosketin, NC (*normally closed*) | Perusasennossa kiinni; toimittaessa avautuu.                                                                       |
| Kaksiasentoinen vaihtokosketin        | Yhteinen kosketin vaihtaa kahden yhteyden välillä. Kuvan versiossa vanha yhteys avautuu ennen uuden sulkeutumista. |
| Väliasentoinen vaihtokosketin         | Keskellä on aukiasento: yhteinen kosketin ei ole yhteydessä kumpaankaan vastakoskettimeen.                         |
| Aikaisemmin sulkeutuva sulkukosketin  | Sulkeutuu ennen saman kosketinyksikön muita koskettimia.                                                           |
| Myöhemmin avautuva avauskosketin      | Avautuu saman kosketinyksikön muita koskettimia myöhemmin.                                                         |

Viimeisten kahden merkin ajoitus on suhteessa **saman kosketinyksikön muihin koskettimiin**. Lähde ei ilmoita viivettä sekunteina. Oppituntikuvan oikealle kääntyminen kuvaa siinä käytetyn piirrosmerkin toimintaa.

Nykyisen kirjaston perusmerkit:

| Sulkukosketin NO                                                                           | Avauskosketin NC                                                                                           | Kaksiasentoinen vaihtokosketin                                                                   |
| ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| ![Sähköpiirrosmerkki: kosketin no](symbolit/kosketin-no.svg)                               | ![Sähköpiirrosmerkki: kosketin nc](symbolit/kosketin-nc.svg)                                               | ![Sähköpiirrosmerkki: vaihtokosketin](symbolit/vaihtokosketin.svg)                               |
| Väliasentoinen vaihtokosketin                                                              | Aikaisemmin sulkeutuva NO                                                                                  | Myöhemmin avautuva NC                                                                            |
| ![Sähköpiirrosmerkki: vaihtokosketin keskiasento](symbolit/vaihtokosketin-keskiasento.svg) | ![Sähköpiirrosmerkki: kosketin no aikaisemmin sulkeutuva](symbolit/kosketin-no-aikaisemmin-sulkeutuva.svg) | ![Sähköpiirrosmerkki: kosketin nc myohassa avautuva](symbolit/kosketin-nc-myohassa-avautuva.svg) |

Kaikkien kuuden merkin perusasento ja toiminta näkyvät yllä. Erikoismerkkien kuva perustuu oppitunnin rinnakkaisiin graafisiin esitystapoihin; ne on piirretty kirjaston 64 × 64 -ruudukkoon.

### Kontaktorien ja kuormankytkimien käyttöluokat

Käyttöluokka kertoo kuormatyypistä ja kytkentätilanteesta. AC tarkoittaa vaihtosähköä ja DC tasasähköä. Koskettimen NO/NC-toiminta ja sen käyttöluokka ovat eri tietoja.

| Luokka | Laiteryhmä                 | Käyttö oppitunnin taulukossa                                                                                              |
| ------ | -------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| AC-1   | Kontaktorin pääkoskettimet | Resistiivinen tai lievästi induktiivinen vaihtosähkökuorma, esimerkiksi lämmitysvastus.                                   |
| DC-1   | Kontaktorin pääkoskettimet | Resistiivinen tai lievästi induktiivinen tasasähkökuorma.                                                                 |
| AC-3   | Kontaktorin pääkoskettimet | Oikosulkumoottorin käynnistäminen ja virran katkaiseminen normaalin käynnin aikana.                                       |
| AC-4   | Kontaktorin pääkoskettimet | Oikosulkumoottorin käynnistys, vastavirtajarrutus ja nykäyskäyttö; oppituntitaulukossa tiivistetty suunnanvaihtokäytöksi. |
| AC-15  | Ohjauspiirin koskettimet   | Vaihtosähköllä toimivien sähkömagneettisten kuormien, esimerkiksi releiden ja kontaktorien kelojen, ohjaus.               |
| DC-13  | Ohjauspiirin koskettimet   | Sähkömagneettisten tasasähkökuormien ohjaus.                                                                              |
| AC-20  | Kytkin / erotin            | Kytkentä ja avaus ilman kuormaa.                                                                                          |
| AC-21  | Kuormankytkin              | Resistiivisen vaihtosähkökuorman kytkentä.                                                                                |
| AC-23  | Kuormankytkin              | Moottori- tai muun induktiivisen vaihtosähkökuorman kytkentä.                                                             |

**Täsmennys oppituntitaulukkoon:** AC-3:n ja AC-4:n ero ei ole pelkkä suunnanvaihtokytkennän olemassaolo. Ratkaisevaa on, millaisessa moottorin toimintatilassa virta kytketään ja katkaistaan. AC-4 kattaa vastavirtajarrutuksen ja nykäyskäytön. AC-1:n kuvan `cos = 0,95` -merkintää vastaava tehokerroin kirjoitetaan `cos φ`; valmistajan selityksessä AC-1:n ehto on `cos φ ≥ 0,95`.

Samalla kontaktorilla voi olla eri sallittu käyttövirta AC-1- ja AC-3-käytössä. Käyttöluokkaa luetaan yhdessä valmistajan ilmoittaman jännitteen ja virran kanssa.

### Käyttöluokkien muistisääntö

Oppitunnin tiivis kertausapu:

| Käyttöluokka | Muistisääntö                      |
| ------------ | --------------------------------- |
| AC-1         | Lämmitys                          |
| AC-3         | Moottori                          |
| AC-4         | Moottori + suunnanvaihto/jarrutus |
| AC-15        | Ohjauspiiri AC                    |
| DC-13        | Ohjauspiiri DC                    |
| AC-21        | Lämmityskuorman kytkentä          |
| AC-23        | Moottorikuorman kytkentä          |

**Dian kertauspainotus:** AC-1 = lämmityskuorma, AC-3 = moottorikuorma, AC-15 = ohjauspiiri ja AC-23 = moottorien kuormankytkin.

Muistisääntö tiivistää yllä olevan käyttöluokkataulukon. AC-4:n suunnanvaihto/jarrutus on tässä lyhyt muistivihje: tarkempi ero AC-3:een on kuvattu edellä. AC-15 ja DC-13 viittaavat tässä sähkömagneettisten kuormien ohjaukseen. Dian koepainotus on oppitunnin vinkki, ei yleinen lupaus kokeiden sisällöstä.

## Palautuvat ja asentoon jäävät kytkimet

Kytkimestä luetaan erikseen **mitä vivulle tapahtuu, kun siitä päästää irti**, ja **mitkä liittimet ovat sähköisesti yhteydessä** kussakin asennossa.

Alla olevien kytkinkuvien **katkoviiva** näyttää mekaanisen yhteyden vivulta koskettimelle. Virtareittiä seurataan yhtenäisiä johdin- ja kosketinviivoja pitkin. Yhteinen vipu voi ohjata koskettimia, jotka toimivat eri hetkellä. Esimerkkejä ovat aikaisemmin sulkeutuva ja myöhemmin avautuva kosketin.

### A jää asentoon, B palautuu

![A-kytkimen asentoon jäämisen merkki ja yksi vaihtokosketin](symbolit/opetuskaavio-kytkin-a.svg)
![B-kytkimen ylöspäin osoittava palautuskolmio ja yksi vaihtokosketin](symbolit/opetuskaavio-kytkin-b.svg)

- **A on asentoon jäävä** (*maintained*). Vipu jää valittuun asentoon vapauttamisen jälkeen. Kulmikas merkki ohjainviivalla kuvaa asennossa pysymistä.
- **B on palautuva** (*momentary*). Kun vivusta päästää irti, se palaa lepoasentoonsa. Kolmion kärki osoittaa palautumissuunnan. Tässä kuvassa kärki osoittaa ylöspäin.

Molemmat ovat **SPDT-kytkimiä**, eli niissä on yksi vaihtokosketin. Yhteinen liitin **2** voidaan yhdistää liittimeen **1** tai **3**. Kuvan asennossa **2–1** sytyttää H1:n. Toisessa asennossa **2–3** sytyttää H2:n. A jää valitulle reitille, kun taas B palaa vapautettaessa H1-reitille. Tehtävän taulukko 4.4 ei näy aineistossa, joten näitä kahta A:n ja B:n reittiä ei voi yhdistää varmuudella vivun asentonumeroihin 1 ja 2.

**NO ja NC** kuvaavat koskettimen sähköistä tilaa ennen ohjaavaa toimintaa. Palautuvuus kertoo vivun käyttäytymisestä vapautettaessa. Palautuvassa kytkimessä voi olla sulku- tai avauskosketin.

### E palautuu keskelle ja ohjaa kahta napaa

![E-kytkimen kaksi avoinna olevaa vaihtokosketinta, mekaaninen katkoviiva ja kohti keskustaa osoittavat palautuskolmiot](symbolit/opetuskaavio-kytkin-e.svg)

**DPDT** tarkoittaa kahta sähköisesti erillistä vaihtokosketinta, joita sama vipu ohjaa. E:n kuvassa katkoviiva ulottuu molemmille navoille.

E:ssä vastakkaiset kolmiot osoittavat kohti keskiasentoa. Vipu palautuu kummastakin ääriasennosta asentoon **0**.

| Vivun asento | Tehtävässä johtava reitti                            | Lamput                                   |
| ------------ | ---------------------------------------------------- | ---------------------------------------- |
| 0            | Ylempi yhteinen liitin 2 on irti liittimistä 1 ja 3. | Molemmat sammuksissa.                    |
| 1            | `+ → 2 → 1 → H1 → −`                                 | H1 palaa, kun vipu pidetään asennossa 1. |
| 2            | `+ → 2 → 3 → H2 → −`                                 | H2 palaa, kun vipu pidetään asennossa 2. |

Kuvassa ylempi napa on kytketty lamppuihin. Alemman navan liittimet **4, 5 ja 6** ovat tässä tehtävässä käyttämättä. **Asentonumero** 0, 1 tai 2 kertoo vivun valinnan. **Liitinnumero** kertoo sähköisen kytkentäpisteen.

### Tehtävä 4.6 — lue ensin kosketinparit

Tämän vipukytkimen keskimmäinen asento **2** kytkee molemmat navat. E:n keskiasento **0** on auki. Ratkaise siis jokainen harjoitus sen omasta kosketintaulukosta.

Kuvasarjassa vasemman navan yhteinen liitin **2** on alhaalla. Sen yläliittimet ovat **1** vasemmalla ja **3** oikealla. Oikean navan yhteinen liitin **5** on alhaalla. Sen yläliittimet ovat **4** vasemmalla ja **6** oikealla.

- ![Molemmat vaihtokoskettimet oikealla](symbolit/opetuskaavio-vipukytkin-asento-1.svg) **Asento 1** — kiinni ovat **2–3** ja **5–6**.
- ![Vasen kosketin oikealla ja oikea kosketin vasemmalla](symbolit/opetuskaavio-vipukytkin-asento-2.svg) **Asento 2** — kiinni ovat **2–3** ja **5–4**.
- ![Molemmat vaihtokoskettimet vasemmalla](symbolit/opetuskaavio-vipukytkin-asento-3.svg) **Asento 3** — kiinni ovat **2–1** ja **5–4**.

Seuraa jokaisessa asennossa **plus → kiinni oleva kosketin → mahdollinen hyppyjohdin → lamppu → miinus**. Lamppu palaa, kun koko reitti on suljettu. Kaikissa näissä harjoituksissa lampun toinen pää on kytketty miinukseen.

### S1–S4 — harjoitusratkaisut

| Kytkin | Asento 1            | Asento 2 | Asento 3 |
| ------ | ------------------- | -------- | -------- |
| S1     | H1                  | H2       | H3       |
| S2     | Ei palavia lamppuja | H4       | H4 ja H5 |
| S3     | Ei palavia lamppuja | H6       | H7       |
| S4     | H1                  | H2       | H3       |

- **S1** — plus liittimeen **2**, hyppyjohdin **3–5**, H3 liittimeen **1**, H2 liittimeen **4** ja H1 liittimeen **6**. Asennossa 2 reitti on `+ → 2 → 3 → 5 → 4 → H2 → −`.
- **S2** — plus liittimiin **1 ja 4**, H5 liittimeen **2** ja H4 liittimeen **5**. Asennossa 3 plus syöttää kahta erillistä reittiä `1 → 2 → H5` ja `4 → 5 → H4`. Molemmat palaavat miinukseen.
- **S3** — plus liittimeen **2**, hyppyjohdin **3–5**, H6 liittimeen **4** ja H7 liittimeen **1**. Liitin **6** jätetään vapaaksi. Asennossa 1 syöttö päätyy liittimeen 6, joten lampuille ei synny suljettua reittiä.
- **S4** — plus liittimeen **5**, hyppyjohdin **4–2**, H1 liittimeen **6**, H2 liittimeen **3** ja H3 liittimeen **1**. Asennossa 2 reitti on `+ → 5 → 4 → 2 → 3 → H2 → −`.

**Kertaa ilman vastausta.** Mitä S1:n asennoissa 1 ja 2 tapahtuu, jos hyppyjohdin **3–5** puuttuu? Ratkaise ensin, mihin asti plus pääsee.

**Vastaus.** Yhteys 2–3 johtaa plussan liittimeen 3, mutta ilman hyppyjohdinta syöttö ei jatku toiselle navalle. Asennoissa 1 ja 2 yksikään lamppu ei pala. Asennon 3 reitti H3:lle säilyy.

## Lähteet ja ylläpitotiedot

### Piirrosmerkit ja valaistuskytkennät

Oppitunti 28.9.2026:

- käsin piirretty 1-kytkentä ja johdinmäärät
- *Sähköasennustekniikan perusteet*, kohta 6.5 **Valaistusasennukset**, s. 311: 1-kytkin, 5-kytkin ja 6-kytkin sekä kytkinten liitinmerkinnät
- sama aineisto, s. 312: 7-kytkin / ristikytkentä sekä valonsäädin ja valonsäätimen vaihtokytkentä
- sama aineisto, s. 313: painikeohjaus askelreleellä sekä valaistusasennuksen kaapelointi- ja johdinväriesimerkki

53-sivuinen **IEC 60617 SYMBOLS** -PDF toimii vertailuaineistona. Siinä ovat muun muassa johtimet ja liitokset (s. 1–2), maadoitus (s. 11), kytkinkoskettimet (s. 12–15), sulakkeet (s. 17), N/PE/PEN-johtimet (s. 20), jakorasiat ja pistorasiat (s. 21–22), valaisimet (s. 23), moottorit (s. 31–33), muuntajat (s. 34–41) sekä puhallin ja pumppu (s. 52). PDF:n julkaisijaa, päiväystä tai symbolien ajantasaista IEC-statusta ei ole vahvistettu.

Oppitunnin alkuperäiskuvat ovat yksityisen vaultin liitteissä. Julkinen vienti ei kopioi niitä.

- oppitunnin lähdeaineisto — 1-kytkentä
- oppitunnin lähdeaineisto — jakorasian kytkentä
- oppitunnin lähdeaineisto — symbolien vertailukuva
- oppitunnin lähdeaineisto — valaistuskytkennät, oppikirjan s. 311
- oppitunnin lähdeaineisto — ristikytkentä, oppikirjan s. 312
- oppitunnin lähdeaineisto — painikeohjaus, oppikirjan s. 313
- oppitunnin lähdeaineisto — keskuskaavio, *Sähkön asentaminen II* s. 134–135
- oppitunnin lähdeaineisto — asennuspiirustusten merkkiluettelo, harjoitustehtävät s. 69

Ajantasaiset lähdesivut: [SESKO: Piirrosmerkit / IEC 60617](https://sesko.fi/standardointi/dokumentointi/piirrosmerkit/), SESKOn teknisen dokumentoinnin standardit, SFS 6000 -pienjännitesähköasennukset sekä Tukesin sähköpätevyys- ja ILP-asennusohjeet.

### Koskettimet ja käyttöluokat

- Oppituntidia 9.11.2026, oppitunnin lähdeaineisto — kuusi kosketintoimintoa ja niiden rinnakkaiset graafiset esitystavat. Oppituntikuva ei vahvista IEC-tunnusta tai standardistatusta.
- Oppitunnin käyttöluokkataulukko 4.3; alkuperäinen oppikirjakuva oppitunnin lähdeaineisto. Kirjan nimi ja sivunumero eivät näy rajauksessa.
- Schneider Electric: [AC-1 ja AC-3: kuormatyypin ja kytkentätilanteen merkitys](https://www.se.com/nl/en/faqs/FA23926/) ja [TeSys Giga: käyttöluokkien määritelmät](https://productinfo.se.com/tesysgigainstallationguide/tesys-giga-series-giga-contactors-and-giga-thermal-overload-relays-installation-guide/English/TeSys%E2%84%A2%20Giga%20Series%20Giga%20Contactors%20and%20Giga%20Thermal%20Overload%20Relays%20Installation%20Guide_0000447511.xml/\$/PanGu_LoadsCPT_0000507717), tarkistettu 9.11.2026.
- Oppituntidia ”Helppo muistisääntö”, 9.11.2026, oppitunnin lähdeaineisto. Dian koepainotus on oppitunnin vinkki, ei yleinen lupaus kokeiden sisällöstä.

### Palautuvat kytkimet ja vipukytkintehtävät

- Oppimateriaalin tehtäväkuvat oppitunnin lähdeaineisto (A, B ja E), oppitunnin lähdeaineisto (tehtävä 4.6, S1 ja S2) ja oppitunnin lähdeaineisto (S3 ja S4).
- IEC 60617 -tietokannan kooste 5.3.2019. S00150 kuvaa automaattista palautusta, S00151 asennossa pysymistä ja soveltamisohje A00048 palautuskolmion suuntaa. Tässä käytetty merkintätapa tarkistettu 9.11.2026. [IEC 60617 -kooste](https://library.iec.ch/grasymb/grasymb.nsf/5FDC3327D03AD13DC125846A00501C93/%24FILE/IEC60617_Snapshot_2019-03-05.pdf)
