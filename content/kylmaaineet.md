---
title: "Kylmäaineet"
publish: true
---

Oppitunnin muistiinpanot 15.9.2026. Tätä dokumenttia täydennetään myöhemmillä kylmäaineita koskevilla muistiinpanoilla.

Lähdekuvat: oppitunnin lähdeaineisto. Kuvista jäsennelty sisältö ja täydentävät selitykset on erotettu alla.

## ASHRAE ja R-tunnukset

ASHRAE:n R-tunnuksia käytetään kylmäaineiden nimeämiseen kansainvälisesti.

| Ryhmä                          | Oppitunnin merkintä            | Olennainen ero                                 |
| ------------------------------ | ------------------------------ | ---------------------------------------------- |
| Yksikomponenttiset kylmäaineet | R1xx, R2xx, R3xx, R6xx ja R7xx | Yksi kemiallinen aine                          |
| Atseotrooppiset seokset        | R5xx                           | Ei lämpötilaliukumaa atseotrooppisessa tilassa |
| Tseotrooppiset seokset         | R4xx                           | Lämpötilaliukuma                               |

**Täsmennys numerointiin:** kuvan yksikomponenttisten aineiden luettelo on muistivihje, ei täydellinen numerointisääntö. Myös esimerkiksi R32 ja R1234yf ovat yksikomponenttisia. ASHRAE:n taulukossa R400-sarja sisältää tseotrooppiset ja R500-sarja atseotrooppiset seokset. [ASHRAE:n kylmäainetunnukset](https://www.ashrae.org/technical-resources/standards-and-guidelines/ashrae-refrigerant-designations).

## Lämpötilaliukuma

**Selitys oppitunnin käsitteelle:** lämpötilaliukuma tarkoittaa, että seoksen höyrystyminen tai lauhtuminen tapahtuu samalla paineella lämpötila-alueella yhden lämpötilan sijaan.

Kuvan muistisääntö: **R400-sarja on lämpötilaliukuman ryhmä.** Liukuman suuruutta ei kuitenkaan voi päätellä pelkästä sarjanumerosta.

Yhteys aiempiin muistiinpanoihin: liukuvalla kylmäaineella tulistukseen käytetään kastepistelämpötilaa ja alijäähdytykseen kuplapistelämpötilaa. Katso [Tulistus ja alijäähdytys](kylmatekniikan-perusteet.md#tulistus-ja-alijäähdytys).

## Haitallisuuden arviointi

Oppitunnilla erotettiin kaksi näkökulmaa:

- **Ympäristövaikutukset:** ODP ja GWP.
- **Ihmiseen liittyvä turvallisuus:** turvaluokitus, kuvassa esimerkkinä A1.

Täsmennys: ASHRAE:n turvaluokitus perustuu myrkyllisyyteen ja syttyvyyteen. Se kuvaa eri ominaisuuksia kuin ympäristövaikutusten ODP ja GWP. [ASHRAE](https://www.ashrae.org/technical-resources/standards-and-guidelines/ashrae-refrigerant-designations).

### ODP — otsonikerrosta heikentävä vaikutus

ODP = **Ozone Depletion Potential**.

- Oppitunnin pääkohta: klooria sisältävät kylmäaineet ja otsonikerroksen heikkeneminen.
- Vertailuaine on **R11 eli CFC-11**, jonka **ODP = 1**.
- Kuvassa käytön historialliseksi muistiinpanoksi on kirjattu **1950–1990**. Tämä on oppitunnin aikakausimerkintä, ei tässä vahvistettu tarkka käyttöönotto- tai lopetusraja.

**Täsmennys:** ODP kuvaa suhteellista otsonikerrosta heikentävää vaikutusta. Otsonia tuhoaviin aineisiin kuuluu myös bromia sisältäviä aineita; kyse ei ole pelkästään kloorista. [EPA: Ozone-Depleting Substances](https://www.epa.gov/ozone-layer-protection/ozone-depleting-substances).

### GWP — ilmastoa lämmittävä vaikutus

GWP = **Global Warming Potential**.

- Vertailuaine on **hiilidioksidi, CO₂**, jonka **GWP = 1**.
- Oppitunnin esimerkki: **R410A:n GWP = 2088**.

**Täsmennys:** GWP vertaa samanmassaisia päästöjä valitulla ajanjaksolla, tavallisesti 100 vuodessa. GWP on suhdeluku, ei massayksikkö. Arvo riippuu käytetystä arviointiperustasta; tässä säilytetään oppitunnin esimerkkiarvo 2088. [EPA: Understanding Global Warming Potentials](https://www.epa.gov/ghgemissions/understanding-global-warming-potentials).

### CO₂-ekvivalenttitonni

Oppitunnin lyhenne on **ekvt** (ekvivalenttitonni). Selkeä yksikkömerkintä tässä muistiossa on **t CO₂-ekv.**

**Täydentävä laskuesimerkki:** CO₂-ekvivalentti saadaan kertomalla kylmäaineen massa GWP-arvolla. Kilogrammoista tonneihin siirryttäessä jaetaan tuhannella:

`CO₂-ekvivalentti [t CO₂-ekv.] = massa [kg] × GWP / 1000`

Kun R410A:n massaksi valitaan 1 kg ja käytetään oppitunnin GWP-arvoa:

`1 × 2088 / 1000 = 2,088 t CO₂-ekv.`

Tämä kuvaa yhden kilogramman päästöä vastaavaa ilmastovaikutusta kyseisellä GWP-perustalla. Laitteessa oleva täytös ei itsessään tarkoita, että aine olisi päässyt ilmakehään. Laskentaperiaate: [EPA](https://www.epa.gov/ghgemissions/understanding-global-warming-potentials).

Kaavakooste: [Kylmäaineet ja CO₂-ekvivalentti](kaavat-ja-yksikot.md#kylmäaineet-ja-co-ekvivalentti).

## Turvaluokitus: myrkyllisyys ja syttyvyys

Kuvan muistivihje on **myrkyllisyys A tai B, syttyvyys 1–3**. Täydennys: syttyvyysluokituksessa on myös alaluokka **2L**.

| Merkintä | Merkitys                                        |
| -------- | ----------------------------------------------- |
| A        | Pienempi myrkyllisyys                           |
| B        | Suurempi myrkyllisyys                           |
| 1        | Ei liekin etenemistä standardin koeolosuhteissa |
| 2L       | Alempi syttyvyys, pieni palamisnopeus           |
| 2        | Alempi syttyvyys                                |
| 3        | Suuri syttyvyys                                 |

Esimerkiksi **A1** yhdistää pienemmän myrkyllisyyden ja luokan 1; **A2L** pienemmän myrkyllisyyden ja hitaasti palavan luokan 2L. A ei tarkoita täysin vaaratonta.

Lähdekuva: oppitunnin lähdeaineisto. Luokitusten selitykset: [ASHRAE/UNEP, huhtikuu 2026](https://www.ashrae.org/file%20library/professional%20development/ashrae-unep/unep---ashrae-factsheet--english.pdf).

## Kylmäaineiden kemialliset ryhmät

Alla oppitunnin sisältö jäsenneltynä. Ryhmän nimi kuvaa kemiaa; R-tunnus yksilöi aineen tai seoksen.

| Ryhmä | Nimi ja koostumuksen muistivihje                                | Oppitunnin pääkohdat ja esimerkit                                                                                             |
| ----- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| CFC   | Kloorifluorihiilivedyt: hiiltä, klooria ja fluoria              | ODP > 0. Kuvan käyttörajoitus täsmennetään alla.                                                                              |
| HCFC  | Osittain halogenoidut kloorifluorihiilivedyt: mukana myös vetyä | ODP > 0; esimerkki R22, ODP 0,055.                                                                                            |
| HFC   | Fluorihiilivedyt: vetyä, fluoria ja hiiltä, ei klooria          | ODP = 0, GWP vaihtelee. Kuvassa ”yleisin”; ajankohtaan ja käyttökohteeseen sidottu oppituntihavainto. Esimerkit R134a ja R32. |
| HFO   | Fluorihiiliolefiinit: tyydyttymättömät fluoratut hiilivedyt     | Pieni GWP, ODP = 0. Kuvan esimerkit R1234yf ja R1234ze. Käyttöä autojen ilmastoinnissa ja vedenjäähdyttimissä.                |
| HC    | Hiilivedyt: hiiltä ja vetyä                                     | Palavia; ODP = 0, pieni GWP. Esimerkit R290 ja R600a.                                                                         |

Nimien täsmennys: kuvan CFC/HCFC-otsikoiden ”kloorivedyt” on kirjoitettu yllä tarkemmin kloorifluorihiilivedyiksi. R22:n ODP 0,055 vastaa Montrealin pöytäkirjan vertailuarvoa; eri arviointitaulukoissa voi olla eri arvoja. [EPA: Ozone-Depleting Substances](https://www.epa.gov/ozone-layer-protection/ozone-depleting-substances).

**Käyttörajoituksen korjaus:** kuvan CFC/HCFC-merkintä ”ei saa käyttää” on liian laaja. Olemassa olevaa laitetta saa käyttää, mutta kylmäainetta ei saa lisätä vuodon tai rikkoutumisen jälkeen. [Syke](https://www.ymparisto.fi/fi/luvat-ja-velvoitteet/f-kaasut-ja-otsonikerrosta-heikentavat-aineet).

### HFO-aineiden syttyvyys ja hajoamistuotteet

Kuvan ”luokitellaan palaviksi” ei koske kaikkia HFO-aineita. Esimerkiksi R1234ze(E) on A2L, mutta R1336mzz(Z) on A1. Kuvan ”palaessa myrkyllisiä” täsmennetään: liekissä tai kuumalla pinnalla voi syntyä myrkyllisiä hajoamistuotteita. Tämä on eri asia kuin alkuperäisen kylmäaineen myrkyllisyysluokka. [ASHRAE/UNEP](https://www.ashrae.org/file%20library/professional%20development/ashrae-unep/unep---ashrae-factsheet--english.pdf).

### Autojen ilmastointi — päivämäärän täsmennys

Kuvan merkintä 1.1.2016 on korjattu päivämääräksi **1.1.2017**. Varmistettu säädöstieto: EU:n MAC-direktiivin soveltamisalaan kuuluvien uusien ajoneuvotyyppien ilmastoinnissa yli 150:n GWP:n fluoratut kaasut kiellettiin **1.1.2011**, ja kaikkien uusien ajoneuvojen osalta **1.1.2017**. Soveltamisala on M1-henkilöautot ja N1-luokan 1 kevyet hyötyajoneuvot. Direktiivi ei määrää tiettyä HFO-ainetta käytettäväksi. [Euroopan komissio: MAC](https://single-market-economy.ec.europa.eu/sectors/automotive-industry/environmental-protection/mobile-air-conditioning-systems-macs_en).

Lähdekuva: oppitunnin lähdeaineisto.

## Luonnolliset kylmäaineet

Kuvan esimerkit ovat **R717 (ammoniakki)** ja **R744 (hiilidioksidi)**. Myös hiilivedyt, kuten R290 ja R600a, kuuluvat luonnollisiin kylmäaineisiin; HC ja luonnolliset kylmäaineet eivät siis ole toisensa poissulkevat ryhmät. [EU:n F-kaasuasetus, johdanto-osa 3](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R0573).

Kuvan **GWP ≈ 0, ODP = 0** toimii matalan ympäristövaikutuksen muistivihjeenä, mutta laskuissa käytetään ainekohtaista arvoa: **R744:n GWP = 1**, ei 0. R744:n ODP on 0. [Danfoss: CO₂](https://www.danfoss.com/en/about-danfoss/our-businesses/cooling/refrigerants-and-energy-efficiency/refrigerants-for-lowering-the-gwp/carbon-dioxide-co2/).

### CO₂:n paine ja sähkönkulutus

Kuvan havainto: ”CO₂ kuluttaa paljon sähköä korkean paine-eron takia.”

**Korjaus:** korkeasta käyttöpaineesta ei yksin voi päätellä suurta sähkönkulutusta. CO₂:n painesuhde voi olla verrattain pieni, ja energiatehokkuus riippuu prosessista, lämpötiloista ja järjestelmäratkaisusta. Korkea lauhtumislämpötila voi heikentää tehokkuutta, mutta CO₂-järjestelmä voi myös olla hyvin energiatehokas. [Danfoss](https://www.danfoss.com/en/about-danfoss/our-businesses/cooling/refrigerants-and-energy-efficiency/refrigerants-for-lowering-the-gwp/carbon-dioxide-co2/).

Lähdekuva: oppitunnin lähdeaineisto.

### Oppitunnin CO₂-ekvivalenttiesimerkki

Kuvan arvot: **R744, 100 kg, GWP 1**.

`100 kg × 1 = 100 kg CO₂-ekv. = 0,1 t CO₂-ekv.`

Lasku on oikein. Aineen pieni GWP ei tarkoita, että suuri täytös olisi automaattisesti vaaraton.

Lähdekuva: oppitunnin lähdeaineisto. Katso myös [Kylmäaineet ja CO₂-ekvivalentti](kaavat-ja-yksikot.md#kylmäaineet-ja-co-ekvivalentti).

## Lakisääteiset vuototarkastukset

Dian otsikko on ”Lakisääteinen huolto”. Alla käsitellään nimenomaan **vuototarkastuksia kiinteissä jäähdytys-, ilmastointi- ja lämpöpumppulaitteissa**.

### Dian sisältö ja korjaukset

Kuvassa F-kaasurajat ovat > 5, > 50 ja > 500 ekvt, HFO-rajat yli 1, yli 10 ja käsin korjattuna yli 100 kg. Tarkastuskertoina lukee 1, 2 ja 3 vuodessa; vuotohälytin kaksinkertaistaa välin.

**Korjattu taulukko:**

| Liitteen I kaasut, esim. HFC (t CO₂-ekv.) | Liitteen II ryhmän 1 kaasut, esim. HFO (kg) | Enintään | Vuodonilmaisujärjestelmällä |
| ----------------------------------------- | ------------------------------------------- | -------- | --------------------------- |
| 5 ≤ määrä < 50                            | 1 ≤ määrä < 10                              | 12 kk    | 24 kk                       |
| 50 ≤ määrä < 500                          | 10 ≤ määrä < 100                            | 6 kk     | 12 kk                       |
| määrä ≥ 500                               | määrä ≥ 100                                 | 3 kk     | 6 kk                        |

Rajamäärä kuuluu ylempään tarkastusluokkaan. Suurimman täytösluokan perusväli on **3 kk eli neljästi vuodessa**, ei dian kolme kertaa.

Seoksissa huomioidaan molemmat aineosuudet. Suurimmassa luokassa vuodonilmaisujärjestelmä on näissä kiinteissä laitteissa pakollinen; sen toiminta tarkastetaan vuosittain.

**Poikkeukset:** merkityt hermeettiset laitteet alle 10 t CO₂-ekv. / alle 2 kg; asuinrakennuksissa merkityt hermeettiset laitteet alle 3 kg. Seoksissa molemmat rajaehdot huomioidaan.

Lähde: [Syken vuototarkastusohje](https://www.ymparisto.fi/fi/luvat-ja-velvoitteet/f-kaasut-ja-otsonikerrosta-heikentavat-aineet), tarkistettu 15.9.2026. Lähdekuva: oppitunnin lähdeaineisto.

### Mihin luonnolliset kylmäaineet ja seokset kuuluvat?

**Täsmennys 20.9.2026:** selvitä ensin, kuuluuko kylmäaine kyseisen tarkastusvelvoitteen piiriin. Laske vasta sitten soveltuvat rajamäärät. CO₂-ekvivalentti kuvaa ilmastovaikutusta, ei yksin ratkaise lain soveltamisalaa.

- **R717 ja R744 eivät ole HFC- eivätkä HFO-aineita.** Ne eivät kuulu F-kaasuasetuksen 5 artiklan määräaikaisiin vuototarkastuksiin millään täytösmäärällä. Niitä ei sijoiteta yllä olevan taulukon HFC-sarakkeeseen. Tästä ei seuraa, että laite olisi huoltovapaa tai vapautettu muista mahdollisista tarkastusvelvoitteista.
- **HFC-aineissa** verrataan liitteen I kaasumäärää CO₂-ekvivalenttitonneina: esimerkiksi alle 5 t CO₂-ekv. sisältävälle R134a- tai R32-laitteelle ei synny tämän artiklan määräaikaista vuototarkastusvelvoitetta.
- **HFC/HFO-seoksissa** tarkastellaan HFC-osuutta CO₂-ekvivalenttitonneina ja HFO-osuutta kilogrammoina. Seoksen koko massaa ei pidä laskea sekä puhtaaksi HFC:ksi että puhtaaksi HFO:ksi. Sovelletaan lyhyempää aineosuuksien edellyttämää tarkastusväliä.

Lähteet: [F-kaasuasetus (EU) 2024/573, 5 artikla ja liitteet I–II](https://eur-lex.europa.eu/legal-content/FI/TXT/HTML/?uri=CELEX:32024R0573), [Syken ohje: seosaineiden aineosuudet ja tarkastusvälit](https://www.ymparisto.fi/fi/luvat-ja-velvoitteet/f-kaasut-ja-otsonikerrosta-heikentavat-aineet). Tarkistettu 20.9.2026.

## Kertaa omin sanoin

1. Miten yksikomponenttinen kylmäaine eroaa seoksesta?
2. Mitä eroa on R400- ja R500-sarjoilla?
3. Mitä lämpötilaliukuma tarkoittaa?
4. Mitä ODP ja GWP vertaavat, ja mitkä ovat niiden vertailuaineet?
5. Miten GWP-suhdeluku eroaa CO₂-ekvivalenttitonneista?
6. Miten luet turvaluokan A2L?
7. Miksi ”CFC/HCFC-laitetta ei saa käyttää” on liian laaja muistisääntö?
8. Mikä on vähintään 500 t CO₂-ekv. sisältävän kiinteän kylmälaitteen tarkastusväli vuodonilmaisujärjestelmällä?
9. Miksi korkea käyttöpaine ei yksin tarkoita suurta sähkönkulutusta?
10. Miksi 5 000 kg R744:ää ei käynnistä F-kaasuasetuksen määräaikaista vuototarkastusvelvoitetta?
11. Miksi 50 kg R513A:ta ilman vuodonilmaisujärjestelmää tarkastetaan 6 kk eikä 12 kk välein?

## Lähteet ja täsmennykset

- Alkuperäiset oppituntimuistiinpanot: oppitunnin lähdeaineisto, 15.9.2026.
- Oppitunnin vuototarkastusdia ja käsin korjattu 100 kg:n raja: oppitunnin lähdeaineisto, 15.9.2026. Dian virheellinen tarkastustiheys on korjattu tekstissä.
- Lähdemerkintöjen täsmennykset 15.9.2026: lyhenne ekvt; HFC-esimerkki R134a; kuvan päivämäärä 1.1.2016 vahvistettu ja korjattu lähteen perusteella 1.1.2017:ksi. Vuototarkastusvälin korjaus hyväksytty.
- Ulkoiset lähteet on linkitetty täydentävien selitysten yhteyteen; alkuperäiset täsmennykset tarkistettu 15.9.2026. Vuototarkastusten soveltamisala, R513A:n aineosuudet ja alla olevat kotitehtävän ratkaisut tarkistettu 20.9.2026.

## Kotitehtävä 15.9.2026 — CO₂-ekvivalentti ja turvaluokitus

Tehtäväpaperin otsikko: **Kotitehtävät 15.09.**  CO₂-laskut ja vuototarkastusvälit on käsitelty tehtäväkuvan ja siihen liittyvien kysymysten perusteella 20.9.2026. Turvaluokitusosio on jätetty alla itse tehtäväksi.

### Laske CO₂-ekvivalentti ja selvitä tarkastusväli

Paperissa käytetään sanaa ”huoltoväli”. Alla vastataan oppitunnin taulukon tarkoittamaan **F-kaasuasetuksen määräaikaiseen vuototarkastusväliin**, ei laitteen kaikkiin huolto- tai tarkastustarpeisiin. Oletuksena ovat edellä käsitellyt kiinteät kylmälaitteet. Katso [Lakisääteiset vuototarkastukset](kylmaaineet.md#lakisääteiset-vuototarkastukset).

CO₂-laskut on säilytetty tehtäväkuvassa käytetyillä GWP-arvoilla: R134a 1430, R32 675, R717 0, R744 1, R513A 631 ja R404A 3922. Laskutoimitukset ovat näillä arvoilla oikein. R513A:n GWP-perustan täsmennys on taulukon jäljessä.

| Kylmäaine |  Täytös | Vuotohälytin | CO₂-ekvivalentti                    | Väli ja perustelu                                                                |
| --------- | ------: | ------------ | ----------------------------------- | -------------------------------------------------------------------------------- |
| R134a     |    2 kg | Ei           | 2 × 1430 / 1000 = 2,86 t CO₂-ekv.   | Ei tämän asetuksen määräaikaista vuototarkastusta: alle 5 t CO₂-ekv.             |
| R32       |    3 kg | Ei           | 3 × 675 / 1000 = 2,025 t CO₂-ekv.   | Ei tämän asetuksen määräaikaista vuototarkastusta: alle 5 t CO₂-ekv.             |
| R717      |  500 kg | On           | 500 × 0 / 1000 = 0 t CO₂-ekv.       | Ei tämän asetuksen määräaikaista vuototarkastusta: ammoniakki ei ole F-kaasu.    |
| R744      | 1000 kg | On           | 1000 × 1 / 1000 = 1 t CO₂-ekv.      | Ei tämän asetuksen määräaikaista vuototarkastusta: hiilidioksidi ei ole F-kaasu. |
| R513A     |   50 kg | Ei           | 50 × 631 / 1000 = 31,55 t CO₂-ekv.  | Enintään 6 kk: HFO-osuutta 28 kg, joten 10–alle 100 kg:n luokka ratkaisee.       |
| R404A     |   25 kg | Ei           | 25 × 3922 / 1000 = 98,05 t CO₂-ekv. | Enintään 6 kk: vähintään 50 mutta alle 500 t CO₂-ekv.                            |

R134a:n, R32:n ja R404A:n GWP-arvot sekä tarkastusvälit: [Syke](https://www.ymparisto.fi/fi/luvat-ja-velvoitteet/f-kaasut-ja-otsonikerrosta-heikentavat-aineet). R717:n GWP 0: [F-kaasuasetuksen liite VI](https://eur-lex.europa.eu/legal-content/FI/TXT/HTML/?uri=CELEX:32024R0573). R744 on GWP-vertailuaine, GWP 1. Luonnollisten aineiden soveltamisalarajaus perustuu asetuksen 5 artiklaan ja liitteisiin I–II.

### Miksi R513A:n väli on 6 kk eikä 12 kk?

R513A sisältää massasta **44 % R134a:ta (HFC)** ja **56 % R1234yf:ää (HFO)**. Koostumus: [ASHRAE:n kylmäainetaulukko](https://www.ashrae.org/technical-resources/standards-and-guidelines/ashrae-refrigerant-designations).

1. **HFC-osuus:** `50 kg × 0,44 = 22 kg R134a:ta`. Sen CO₂-ekvivalentti on `22 × 1430 / 1000 = 31,46 t CO₂-ekv.` → yksin tarkasteltuna **12 kk**.
2. **HFO-osuus:** `50 kg × 0,56 = 28 kg R1234yf:ää`. Se kuuluu luokkaan `10 ≤ määrä < 100 kg` → **6 kk** ilman vuodonilmaisujärjestelmää.
3. **Lyhyempi väli ratkaisee: 6 kk.** HFO-määrää ei verrata tässä CO₂-ekvivalenttirajoihin, vaan kilogrammarajoihin.

Lähteet: [Syken ohje](https://www.ymparisto.fi/fi/luvat-ja-velvoitteet/f-kaasut-ja-otsonikerrosta-heikentavat-aineet) ja [F-kaasuasetus, 5 artiklan 6 kohta](https://eur-lex.europa.eu/legal-content/FI/TXT/HTML/?uri=CELEX:32024R0573).

**GWP-perustan täsmennys:** kuvan GWP-arvolla 631 saatu 31,55 t CO₂-ekv. on laskettu oikein. Nykyisen asetuksen komponenttiarvoista laskettuna seoksen GWP on kuitenkin `0,44 × 1430 + 0,56 × 0,501 = 629,48056`, eli noin 629,48, jolloin 50 kg vastaa noin **31,47 t CO₂-ekv.** Tätä koko seoksen arvoa ei pidä sekoittaa yllä laskettuun HFC-osuuden arvoon 31,46. Ero ei muuta 6 kk:n tarkastusväliä. GWP-arvot: asetuksen liitteet I ja II; seoksen laskentamenetelmä: liite VI. Kotitehtävässä käytettävä taulukko kannattaa merkitä näkyviin.

### R744:n jatkokysymys

Tehtäväpaperin kysymys: **Kuinka monta kiloa R744-täytöstä koneessa pitää olla, jotta sillä olisi edes yksi lakisääteinen huolto vuodessa?**

**Vastaus tämän tehtävän F-kaasuvuototarkastusten näkökulmasta: ei millään täytösmäärällä.** R744 ei ole F-kaasu, joten F-kaasuasetuksen 5 artiklan määräaikaiset vuototarkastusrajat eivät koske sitä.

`5000 kg × 1 / 1000 = 5 t CO₂-ekv.` on aritmeettisesti oikein, mutta **5 000 kg ei ole R744:n lakisääteisen F-kaasuvuototarkastuksen raja**. CO₂-ekvivalenttiraja ei laajenna asetuksen soveltamisalaa. Tämä vastaus ei tarkoita, ettei R744-laitteelle voisi olla muuta huolto- tai tarkastusvelvoitetta. Lähde: [F-kaasuasetus, 5 artikla](https://eur-lex.europa.eu/legal-content/FI/TXT/HTML/?uri=CELEX:32024R0573).

### Mitä kylmäaineen turvaluokitus tarkoittaa?

- A3
- B2
- B1
- A2L
- A1

Kertaus: [Turvaluokitus: myrkyllisyys ja syttyvyys](kylmaaineet.md#turvaluokitus-myrkyllisyys-ja-syttyvyys). Laskukaava: [Kylmäaineet ja CO₂-ekvivalentti](kaavat-ja-yksikot.md#kylmäaineet-ja-co-ekvivalentti).

Lähde: oppitunnin lähdeaineisto, tehtäväpaperi, toimitettu 15.9.2026. Laskuvastausten ja soveltamisalan täsmennysten lähtökohtana käsin täytetty tehtäväkuva ja sen käsittely 20.9.2026.
