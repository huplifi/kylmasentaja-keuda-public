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

## Symbolistandardit ja oma SVG-kirjasto

SESKOn mukaan sähkökaavioiden standardoidut piirrosmerkit löytyvät **IEC 60617** -tietokannasta. Sähköpiirustusten esittämistä käsittelee **SFS-EN 61082-1**. IEC 60617 -tietokanta sisältää symbolien lisäksi nimet, tunnukset, soveltamisohjeita ja tiedon symbolien statuksesta.

Tämän vaultin `symbolit/`-hakemiston SVG:t ovat **itsenäisesti piirrettyjä opiskelugrafiikoita**, eivät IEC:n virallisten symbolitiedostojen kopioita. Niiden tarkoitus on tehdä omista muistiinpanoista ja harjoituspiirustuksista yhtenäisiä.

Avoimeen julkaisuun ei vielä lisätä lisenssiä, joka väittäisi standardoitujen piirrosmerkkien virallisen grafiikan olevan vapaasti uudelleenlisensoitavissa. Ennen erillisen avoimen symbolipaketin julkaisua tarkistetaan symboli kerrallaan nimi, geometria, IEC 60617 -status ja käyttöoikeus.

## Lähdeaineisto

Oppitunti 28.9.2026:

- käsin piirretty 1-kytkentä ja johdinmäärät
- *Sähköasennustekniikan perusteet*, kohta 6.5 **Valaistusasennukset**, s. 311: 1-kytkin, 5-kytkin ja 6-kytkin sekä kytkinten liitinmerkinnät
- sama aineisto, s. 312: 7-kytkin / ristikytkentä sekä valonsäädin ja valonsäätimen vaihtokytkentä
- sama aineisto, s. 313: painikeohjaus askelreleellä sekä valaistusasennuksen kaapelointi- ja johdinväriesimerkki

53-sivuinen **IEC 60617 SYMBOLS** -PDF toimii vertailuaineistona. Siinä ovat muun muassa johtimet ja liitokset (s. 1–2), maadoitus (s. 11), kytkinkoskettimet (s. 12–15), sulakkeet (s. 17), N/PE/PEN-johtimet (s. 20), jakorasiat ja pistorasiat (s. 21–22), valaisimet (s. 23), moottorit (s. 31–33), muuntajat (s. 34–41) sekä puhallin ja pumppu (s. 52).

### Ajantasaiset verkkolähteet

- SESKO: Piirrosmerkit / IEC 60617
- SESKO: teknisen dokumentoinnin standardit
- SFS: SFS 6000 -pienjännitesähköasennukset
- Tukes: Sähköpätevyydet ja työalueet, ILP:n sähköasennukset
- Tukes: Ilmalämpöpumput
