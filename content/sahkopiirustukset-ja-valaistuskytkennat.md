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

oppitunnin lähdeaineisto

### Liitoskohta

Risteävien tai haarautuvien johtimien musta piste osoittaa sähköisen liitoksen.

oppitunnin lähdeaineisto

### Haaroitus

oppitunnin lähdeaineisto

### Nolla- ja suojajohdin

Oppitunnilla käytetyssä yksiviivaisessa merkintätavassa pistepäinen poikkimerkki osoittaa N-johtimen ja T-mäinen poikkimerkki PE-johtimen. IEC 60617 -vertailuaineistossa N-, PE- ja PEN-johtimille on omat johdinmerkintänsä (PDF s. 20).

oppitunnin lähdeaineisto

oppitunnin lähdeaineisto

Piirustuksen oma selite ratkaisee aina tulkinnan.

## Rasiat ja liitynnät

### Jakorasia

Jakorasia on kohta, jossa johtimia voidaan liittää ja haaroittaa. Oppitunnin 1- ja 5-kytkinesimerkeissä jakorasia on merkitty tunnuksella X1.

oppitunnin lähdeaineisto

### Suojakoskettimellinen pistorasia

oppitunnin lähdeaineisto

ILP:n kohdalla pistorasian olemassaolo ei yksin ratkaise liitännän sopivuutta. Tukesin mukaan pistotulppaliitäntäisen ILP:n pistorasian pitää olla maadoitettu ja sijaita sen yksikön vieressä, johon valmistaja on suunnitellut sähköliitännän. Kiinteä liitäntä, uuden pistorasian tai turvakytkimen asentaminen, vikavirtasuojan lisääminen tai pistorasian siirtäminen edellyttää sähkötyöoikeutta.

## Kytkimet ja valaistuskytkennät

### 1-kytkin, yksinapainen kytkin

Yksi kytkin ohjaa yhtä valaisinta tai valaisinryhmää yhdestä paikasta.

oppitunnin lähdeaineisto

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

oppitunnin lähdeaineisto

Periaate:

**L → Q1.1 → valaisinryhmä 1 → N**

**L → Q1.2 → valaisinryhmä 2 → N**

1-kytkimen kytkinhaarassa on yksi kytketyn vaiheen paluu. 5-kytkimessä niitä on kaksi, koska ohjattavia lähtöjä on kaksi. Oppitunnin yksiviivaisessa kuvassa tämä näkyy suurempana johdinmääränä kytkinhaarassa ja valaisinmerkinnässä **1+2**.

### Valaisin

oppitunnin lähdeaineisto

## Suojaus ja erotus

### Sulake

oppitunnin lähdeaineisto

### Johdonsuojakatkaisija

oppitunnin lähdeaineisto

### Turvakytkin / paikallinen erotus

oppitunnin lähdeaineisto

ILP:n kannalta erotus on erityisen tärkeä. Tukesin mukaan **kiinteästi liitetyn ilmalämpöpumpun erotuslaitteeksi on asennettava turvakytkin**. Pistotulppaliitäntäisessä laitteessa pistotulppa voi toimia hyväksyttävänä erotustapana, kun liitäntä on toteutettu vaatimusten mukaisesti.

## Kylmälaitteissa vastaan tulevia kuormia

### Moottori

oppitunnin lähdeaineisto

Moottorisymboli voi liittyä esimerkiksi kompressoriin tai puhaltimen moottoriin. Pelkkä M-symboli ei kerro laitteen koko toimintoa, vaan se päätellään laitetunnuksesta, kaaviosta ja selitteestä.

### Puhallin

oppitunnin lähdeaineisto

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

## Symbolistandardit ja oma SVG-kirjasto

SESKOn mukaan sähkökaavioiden standardoidut piirrosmerkit löytyvät **IEC 60617** -tietokannasta. Sähköpiirustusten esittämistä käsittelee **SFS-EN 61082-1**. IEC 60617 -tietokanta sisältää symbolien lisäksi nimet, tunnukset, soveltamisohjeita ja tiedon symbolien statuksesta.

Tämän vaultin `symbolit/`-hakemiston SVG:t ovat **itsenäisesti piirrettyjä opiskelugrafiikoita**, eivät IEC:n virallisten symbolitiedostojen kopioita. Niiden tarkoitus on tehdä omista muistiinpanoista ja harjoituspiirustuksista yhtenäisiä.

Avoimeen julkaisuun ei vielä lisätä lisenssiä, joka väittäisi standardoitujen piirrosmerkkien virallisen grafiikan olevan vapaasti uudelleenlisensoitavissa. Ennen erillisen avoimen symbolipaketin julkaisua tarkistetaan symboli kerrallaan nimi, geometria, IEC 60617 -status ja käyttöoikeus.

## Lähdeaineisto

Oppitunti 28.9.2026:

- käsin piirretty 1-kytkentä ja johdinmäärät
- *6.5 Valaistusasennukset / Valaistuskytkimet ja valaistuskytkennät*: 1-kytkin ja jakorasian johdotus
- sama aineisto: sarjakytkin (kruunukytkin), 5-kytkin

53-sivuinen **IEC 60617 SYMBOLS** -PDF toimii vertailuaineistona. Siinä ovat muun muassa johtimet ja liitokset (s. 1–2), maadoitus (s. 11), kytkinkoskettimet (s. 12–15), sulakkeet (s. 17), N/PE/PEN-johtimet (s. 20), jakorasiat ja pistorasiat (s. 21–22), valaisimet (s. 23), moottorit (s. 31–33), muuntajat (s. 34–41) sekä puhallin ja pumppu (s. 52).

### Ajantasaiset verkkolähteet

- SESKO: Piirrosmerkit / IEC 60617
- SESKO: teknisen dokumentoinnin standardit
- SFS: SFS 6000 -pienjännitesähköasennukset
- Tukes: Sähköpätevyydet ja työalueet, ILP:n sähköasennukset
- Tukes: Ilmalämpöpumput
