---
title: "Sähköopin perusteet"
publish: true
---

Koottu oppikirjakuvista 31.8.2026 ja täydennetty oppituntien aineistoilla. Tämä muistio kokoaa sähköopin peruskäsitteet, mittaamisen, sähköturvallisuuden sekä sähköverkon ja kiinteistön sähkönsyötön rakenteen.

## Opittavat kokonaisuudet

- sähkön suureet, tunnukset ja yksiköt
- Ohmin laki sekä jännitteen, virran ja resistanssin yhteys
- resistiivisyys, johtavuus sekä johtimen materiaalin ja mittojen vaikutus resistanssiin
- sähkötehon laskeminen jännitteestä ja virrasta
- sähkövirran ja elektronien kulkusuunnat
- suljettu ja avoin virtapiiri
- sähkövaraus sekä virran ja ajan yhteys
- jännitteiden luokittelu
- IP-luokitukset: kosketus-, vierasesine- ja vesisuojaus
- asennustilojen luokittelu: kostea, märkä, ulkotila, pesutila ja sauna
- vikasuojaus ja syötön automaattinen poiskytkentä; TN-loppupiirin 0,4 s
- sähkövirran vaikutukset ihmiseen
- yleismittarin kerrannaisyksiköt, mitta-alueet ja CAT-luokat
- asennustesterin käyttö ja keskeiset mittaukset
- sähkön tuotanto, siirto ja jakelu
- kolmivaiheverkon 400/230 V jännitteet
- TN-C- ja TN-S-järjestelmät sekä PEN-, N- ja PE-johtimet
- asennuspiirustuksissa käytettävät piirrosmerkit ja niiden merkitykset
- yksiviivaisen johdotuskuvan tulkinta: syöttö, johdinmäärät ja yhden valaisimen ohjaus

## Sähkön suureet ja yksiköt

| Suure           | Tunnus | Yksikkö              | Yksikön tunnus |
| --------------- | -----: | -------------------- | -------------: |
| Jännite         |      U | voltti               |              V |
| Virta           |      I | ampeeri              |              A |
| Resistanssi     |      R | ohmi                 |              Ω |
| Resistiivisyys  |      ρ | ohmimetri            |            Ω·m |
| Sähkönjohtavuus |      σ | siemens metriä kohti |            S/m |
| Teho            |      P | watti                |              W |
| Sähköenergia    |      W | wattitunti           |             Wh |
| Kapasitanssi    |      C | faradi               |              F |
| Induktanssi     |      L | henry                |              H |
| Taajuus         |      f | hertsi               |             Hz |

Esimerkkejä:

- Suomen sähköverkon nimellisjännite on 230 V ja taajuus 50 Hz.
- Tavallinen paristo voi olla 1,5 V.
- Sähkölämmitin voi olla teholtaan 1 500 W eli 1,5 kW.
- Kondensaattorin kapasitanssi voidaan ilmoittaa esimerkiksi mikrofaradeina (µF) ja kelan induktanssi millihenryinä (mH).

## Ohmin laki

- `U = I × R`
- `I = U / R`
- `R = U / I`

Suureet ja yksiköt:

- `U` = jännite, voltti (V)
- `I` = virta, ampeeri (A)
- `R` = resistanssi, ohmi (Ω)

## Resistiivisyys ja johtavuus

Oppitunti 21.9.2026.

**Resistiivisyys `ρ` (rho)** kertoo, kuinka voimakkaasti materiaali vastustaa sähkövirran kulkua. Mitä pienempi resistiivisyys, sitä paremmin aine johtaa sähköä.

**Resistanssi `R`** puolestaan kuvaa tietyn johtimen vastusta. Siihen vaikuttavat materiaalin lisäksi johtimen pituus ja poikkipinta-ala. Resistiivisyys on materiaalin ominaisuus, ei johtimen pituudesta tai paksuudesta määräytyvä suure. Se riippuu kuitenkin esimerkiksi lämpötilasta.

### Kaava ja suureet

Dian kaava:

`ρ = R × A / l`

Sama yhteys johtimen resistanssille ratkaistuna:

`R = ρ × l / A`

Kaava koskee tasalaatuista johdinta, jonka poikkipinta-ala on vakio.

| Tunnus | Merkitys                                          | SI-yksikkö |
| ------ | ------------------------------------------------- | ---------- |
| `ρ`    | Materiaalin resistiivisyys                        | Ω·m        |
| `R`    | Johtimen resistanssi                              | Ω          |
| `l`    | Johtimen pituus                                   | m          |
| `A`    | Johtimen poikkipinta-ala, ei ulkopinnan pinta-ala | m²         |

**Muistisääntö:** samasta materiaalista tehty pidempi johdin vastustaa enemmän ja paksumpi johdin vähemmän, kun lämpötila pysyy samana. Pituuden kaksinkertaistaminen kaksinkertaistaa resistanssin; poikkipinta-alan kaksinkertaistaminen puolittaa sen.

### Yksiköiden kanssa tarkkana

Kun `A` annetaan neliömetreinä ja `l` metreinä, resistiivisyyden yksikkö on `Ω·m`. Johdinlaskuissa käytetään myös yksikköä `Ω·mm²/m`: silloin poikkipinta-ala annetaan neliömillimetreinä ja pituus metreinä.

- `1 mm² = 10⁻⁶ m²`
- `1 Ω·mm²/m = 10⁻⁶ Ω·m`

Älä sekoita eri yksikköjärjestelmien lukuarvoja samaan laskuun.

### Aineiden resistiivisyysarvoja +20 °C:ssa

Oppitunnin taulukossa resistiivisyys annetaan johdinlaskuihin kätevässä yksikössä `Ω·mm²/m` ja johtavuus sen käänteisyksikössä `m/(Ω·mm²)`.

| Aine              | Resistiivisyys ρ (Ω·mm²/m) | Johtavuus (m/(Ω·mm²)) |
| ----------------- | -------------------------: | --------------------: |
| Hopea             |                     0,0159 |                    63 |
| Kupari            |                     0,0168 |                    60 |
| Kulta             |                     0,0244 |                    41 |
| Alumiini          |                     0,0265 |                    37 |
| Messinki (5 % Zn) |                     0,0300 |                    33 |
| Rodium            |                     0,0433 |                    23 |
| Sinkki            |                     0,0590 |                    17 |
| Litium            |                     0,0928 |                    11 |
| Rauta             |                     0,0970 |                    10 |
| Tina              |                     0,1060 |                     9 |
| Ruostumaton teräs |                     0,6900 |                     1 |
| Hiili (amorfinen) |                    500–800 |           0,001–0,002 |
| Merivesi          |                    210 000 |             0,000 005 |
| Juomavesi         |             20·10⁶–200·10⁶ |       5·10⁻⁸–50·10⁻¹⁰ |
| Ilma              |                  10¹⁸–10²⁰ |           10⁻¹⁸–10⁻²⁰ |
| PTFE (teflon)     |                  10²⁷–10²⁹ |           10⁻²⁹–10⁻³¹ |

Taulukko havainnollistaa hyvin eron johtimien ja eristeiden välillä: hopea ja kupari ovat erittäin hyviä johteita, kun taas ilman ja PTFE:n resistiivisyys on valtavan suuri.

Lähde: oppituntidia, kuva oppitunnin lähdekuva (21.9.2026). Arvot on kirjattu dian mukaisina.

### Sähkönjohtavuus

Materiaalin sähkönjohtavuus on resistiivisyyden käänteisluku:

`σ = 1 / ρ`

`σ` (sigma) on sähkönjohtavuus yksikössä `S/m`, kun `ρ` on yksikössä `Ω·m`. Pieni resistiivisyys tarkoittaa suurta sähkönjohtavuutta.

### Täsmennys dian lämpöhäviöihin

Diassa todetaan, että pienempi resistiivisyys pienentää johtimen resistanssia ja lämpöhäviöitä. Vertailussa on pidettävä johtimien mitat samoina ja lämpöhäviöitä tarkasteltaessa myös virta samana:

`P_häviö = I² × R`

**Samalla virralla** pienempi resistanssi tuottaa vähemmän lämpöä. Jos sen sijaan jännite juuri tarkasteltavan vastuksen yli pidetään vakiona, `P = U² / R`: pienempi resistanssi kasvattaa virtaa ja tehoa. Siksi ilmaus ”pienempi resistanssi = vähemmän lämpöä” ei päde ilman vertailuehtoa.

Lähde: oppituntidia ”Resistiivisyys ja johtavuus”, keskusteluun lähetetty kuva oppitunnin lähdekuva (21.9.2026). Materiaalin ja johtimen erottelu, kaavan käyttöehdot, yksikkömuunnokset, johtavuuden käänteisluku ja lämpöhäviöiden vertailuehto ovat oppimista tukevia täsmennyksiä.

Kaavakooste: [Resistiivisyys ja johtavuus](kaavat-ja-yksikot.md#resistiivisyys-ja-johtavuus).

## Hyötysuhde

Oppitunti 21.9.2026.

**Tehohyötysuhde** kertoo laitteesta hyödyksi saadun tehon eli **antotehon** suhteesta laitteeseen vietyyn tehoon eli **ottotehoon**.

`η = P₂ / P₁`

- `η` (eeta) = hyötysuhde
- `P₂` = laitteen tai koneen antoteho
- `P₁` = laitteen tai koneen ottoteho

Laitteessa syntyvien häviöiden vuoksi hyötysuhde on alle yksi. Hyötysuhde voidaan ilmoittaa myös prosentteina kertomalla suhdeluku sadalla.

Lähde: oppituntidia ”Hyötysuhde”, kuva oppitunnin lähdekuva (21.9.2026).

## Sähköteho

- `P = U × I`
- `U = P / I`
- `I = P / U`

`P` on teho watteina (W), `U` jännite voltteina (V) ja `I` virta ampeereina (A). Yksikkömuisti: `W = V × A`.

## Vastusten sarjakytkentä

Sarjaan kytkettyjen vastusten kokonaisresistanssi on vastusten summa:

`Rkok = R1 + R2 + …`

Sama virta kulkee kaikkien sarjaan kytkettyjen vastusten läpi. Jännite jakautuu vastuksille niiden resistanssien suhteessa.

### Harjoitusesimerkki

Annetut arvot:

- `U = 12 V`
- `R1 = 5 Ω`
- `R2 = 10 Ω`

Kokonaisresistanssi:

`Rkok = 5 Ω + 10 Ω = 15 Ω`

Piirin virta:

`I = U / Rkok = 12 V / 15 Ω = 0,8 A`

Jännitehäviöt:

- `U1 = I × R1 = 0,8 A × 5 Ω = 4 V`
- `U2 = I × R2 = 0,8 A × 10 Ω = 8 V`
- Tarkistus: `U1 + U2 = 4 V + 8 V = 12 V`

## Vastusten rinnankytkentä

Rinnankytkennässä jännite on sama kaikissa haaroissa. Kokonaisvirta jakautuu haaroihin: `Ikok = I1 + I2 + …`. Haaran virta saadaan Ohmin lailla: `I1 = U / R1`.

Kokonaisresistanssi lasketaan käänteislukujen avulla:

`1 / Rkok = 1 / R1 + 1 / R2 + …`

Kahdelle vastukselle samat kaavat voidaan kirjoittaa kolmella tavalla:

- `Rkok = 1 / (1 / R1 + 1 / R2)`
- `Rkok = (R1 × R2) / (R1 + R2)`
- `1 / Rkok = (R1 + R2) / (R1 × R2)`

Huomaa viimeisessä muodossa: vasemmalla on kokonaisresistanssin **käänteisluku**, ei resistanssi. Tulo jaettuna summalla -kaava koskee kahta vastusta.

Kun rinnakkaisia vastushaaroja lisätään, kokonaisresistanssi pienenee. Positiivisilla, äärellisillä vastuksilla se on pienempi kuin pienin yksittäinen vastus.

### Harjoitusesimerkki: samat vastukset rinnakkain

Kun `U = 12 V`, `R1 = 5 Ω` ja `R2 = 10 Ω`:

- `Rkok = (5 × 10) / (5 + 10) Ω ≈ 3,33 Ω`
- `I1 = 12 V / 5 Ω = 2,4 A`
- `I2 = 12 V / 10 Ω = 1,2 A`
- `Ikok = 2,4 A + 1,2 A = 3,6 A`

### Sarja- ja rinnankytkennän vertailu

| Ominaisuus           | Sarjakytkentä              | Rinnankytkentä                                                      |
| -------------------- | -------------------------- | ------------------------------------------------------------------- |
| Virta                | Sama kaikissa vastuksissa  | Jakautuu haaroihin                                                  |
| Jännite              | Jakautuu vastusten kesken  | Sama kaikissa haaroissa                                             |
| Vastuksen lisääminen | Kokonaisresistanssi kasvaa | Uuden rinnakkaisen haaran lisääminen pienentää kokonaisresistanssia |

Lähde: käsinkirjoitetut muistiinpanot 7.9.2026, oppitunnin lähdeaineisto. Haaravirrat, vertailu ja laskuesimerkki ovat selittäviä täydennyksiä.

## Ohmin lain kaavapyörä

oppitunnin lähdeaineisto

Kaikki kaavapyörän muodot tekstinä:

- **Ratkaise P:** `P = U × I`, `P = I² × R`, `P = U² / R`
- **Ratkaise U:** `U = I × R`, `U = P / I`, `U = √(P × R)`
- **Ratkaise I:** `I = U / R`, `I = P / U`, `I = √(P / R)`
- **Ratkaise R:** `R = U / I`, `R = U² / P`, `R = P / I²`

## Sähkövirta ja virtapiiri

- **Sähkövirran sovittu suunta** on virtalähteen plusnavalta miinusnavalle.
- **Elektronit liikkuvat vastakkaiseen suuntaan**, miinusnavalta plusnavalle.
- Virta kulkee vain, kun virtapiiri on suljettu: virtalähteen navat on yhdistetty toisiinsa johtavaa reittiä pitkin kuorman kautta.
- Kun virtapiiri katkeaa tai virtalähteen potentiaaliero loppuu, virta lakkaa kulkemasta.

### Sähkövaraus

Sähkövarauksen, virran ja ajan yhteys:

`Q = I × t`

josta

- `I = Q / t`
- `t = Q / I`

Yksiköt:

- `Q` = sähkövaraus, coulombi (C) tai ampeerisekunti (As)
- `I` = virta, ampeeri (A)
- `t` = aika, sekunti (s)
- `1 C = 1 As`

Esimerkki: paristossa on varausta 3 600 As ja virta on 1 A.

`t = 3 600 As / 1 A = 3 600 s = 1 h`

## Jännitteiden luokittelu

### Sähköalan standardin mukainen luokittelu

| Luokka         | Tunnus |    Vaihtojännite |               Tasajännite |
| -------------- | -----: | ---------------: | ------------------------: |
| Suurjännite    |     HV |      yli 1 000 V |               yli 1 500 V |
| Pienjännite    |     LV | enintään 1 000 V |          enintään 1 500 V |
| Pienoisjännite |    ELV |    enintään 50 V | enintään 120 V, sykkeetön |

Pienoisjännitealueita ovat **SELV**, **PELV** ja **FELV**. Pienoisjännite kuuluu pienjännitealueeseen, vaikka nimitys kuulostaa erilliseltä pääluokalta.

### Sähkönjakeluverkon nimitykset

| Nimitys      |      Jännitealue |
| ------------ | ---------------: |
| Suurjännite  |        yli 36 kV |
| Keskijännite | yli 1 kV – 36 kV |
| Pienjännite  |        alle 1 kV |

Eri yhteyksissä käytettävät luokitukset eivät ole täysin samoja. Siksi on tärkeää huomata, puhutaanko sähköalan standardin jänniteluokasta vai sähkönjakeluverkon jännitealueesta.

## Sähkövirran vaikutus ihmiseen

Sähköiskun vakavuuteen vaikuttavat ainakin virran suuruus, vaikutusaika, virran kulkureitti kehossa, ihon vastus sekä virran laatu. Oppikirjan taulukon esimerkit:

|     Virta | Vaikutusaika     | Mahdollisia vaikutuksia                                                                 |
| --------: | ---------------- | --------------------------------------------------------------------------------------- |
|  0,5–2 mA | ei merkitystä    | tuntokynnys: sähkö tuntuu                                                               |
|   2–15 mA | ei merkitystä    | kouristusraja, irrottautuminen voi vaikeutua, voimakkaita kipuja                        |
|  15–30 mA | minuutteja       | verenpaineen nousu, hengitysvaikeuksia, kouristuksia                                    |
|  30–50 mA | 1 s – minuutteja | mahdollinen sydänkammiovärinä, epäsäännöllinen sydäntoiminta, tajuttomuus, kouristuksia |
| 50–500 mA | alle sydänjakson | voimakas sokki ja kipu                                                                  |
| yli 50 mA | yli sydänjakson  | sydänkammiovärinä, palovammoja ja tajuttomuus                                           |

**Kouristusraja** on virta, jonka yläpuolella lihakset voivat lamaantua niin, ettei henkilö pysty irrottautumaan jännitteisestä osasta. Raja on yksilöllinen; oppikirjassa mainitaan suuntaa-antavasti noin 10 mA naisilla ja 15 mA miehillä.

Taulukon arvoja ei pidä käyttää turvallisina rajoina. Sähköiskua on aina käsiteltävä vaaratilanteena ja toimittava koulutuksen ensiapu- ja turvallisuusohjeiden mukaan.

## IP-luokitukset – kotelon suojaus

Aihe aloitettu 5.10.2026 ja täydennetty oppikirjan taulukolla sekä oppitunnin aineistolla.

**IP-koodi** kertoo kotelon antamasta suojauksesta. Ensimmäinen numero koskee pääsyä vaarallisiin osiin ja kiinteiden vierasesineiden sisäänpääsyä, toinen veden haitallista sisäänpääsyä. Luokitus perustuu IEC 60529 -standardiin.

> **Muistisääntö: ensin kiinteät, sitten vesi.** Lue numerot erikseen, älä yhtenä lukuna.

### Näin luet merkinnän

| Merkinnän osa         | Esimerkki IP54                             |
| --------------------- | ------------------------------------------ |
| IP                    | Kotelointiluokituksen tunnus               |
| Ensimmäinen numero: 5 | Pölysuojattu                               |
| Toinen numero: 4      | Suojattu vesiroiskeilta kaikista suunnista |

**0 tarkoittaa suojaamatonta kyseisen ominaisuuden osalta. X tarkoittaa, ettei kyseistä suojausastetta ilmoiteta.** Esimerkiksi IPX4 ilmoittaa roiskevesisuojauksen, mutta siitä ei voi päätellä pölysuojausta. X ei tarkoita samaa kuin 0.

### Ensimmäinen numero: kosketus ja kiinteät vierasesineet

| Numero | Vierasesinesuojaus                              | Pääsyn estäminen vaarallisiin osiin |
| ------ | ----------------------------------------------- | ----------------------------------- |
| 0      | Ei suojausta                                    | Ei suojausta                        |
| 1      | Halkaisija vähintään 50 mm                      | Kämmenselkä                         |
| 2      | Halkaisija vähintään 12,5 mm                    | Sormi                               |
| 3      | Halkaisija vähintään 2,5 mm                     | Työkalu                             |
| 4      | Halkaisija vähintään 1,0 mm                     | Lanka                               |
| 5      | Pölysuojattu: pölyä ei pääse haitallista määrää | Lanka                               |
| 6      | Pölytiivis: pölyä ei pääse sisään               | Lanka                               |

Kämmenselkä, sormi, työkalu ja lanka kuvaavat standardin koettimia. **Pölysuojattu (5) ja pölytiivis (6) ovat eri asioita.**

### Toinen numero: vesi

| Numero | Suojaus veden haitalliselta vaikutukselta                                    |
| ------ | ---------------------------------------------------------------------------- |
| 0      | Ei suojausta                                                                 |
| 1      | Pystysuorat vesipisarat                                                      |
| 2      | Pystysuorat pisarat myös kotelon ollessa enintään 15° kallistettuna          |
| 3      | Vesisuihku enintään 60° kulmassa pystysuorasta                               |
| 4      | Vesiroiskeet kaikista suunnista                                              |
| 5      | Vesisuihkut kaikista suunnista                                               |
| 6      | Voimakkaat vesisuihkut kaikista suunnista                                    |
| 7      | Tilapäinen upotus standardin testiolosuhteissa                               |
| 8      | Jatkuva upotus erikseen määritellyissä, luokkaa 7 vaativammissa olosuhteissa |
| 9      | Korkeapaineiset, kuumat vesisuihkut testiolosuhteissa                        |

IPX8 ei lupaa rajatonta upotussyvyyttä: tarkista valmistajan ilmoittamat ehdot.

### Tavallisia esimerkkejä

| Luokitus | Tulkinta                                                                 |
| -------- | ------------------------------------------------------------------------ |
| IP20     | Sormisuojaus ja vähintään 12,5 mm:n vierasesinesuojaus; ei vesisuojausta |
| IP44     | Vähintään 1 mm:n vierasesinesuojaus ja roiskevesisuojaus                 |
| IP54     | Pölysuojaus ja roiskevesisuojaus                                         |
| IP65     | Pölytiiviys ja vesisuihkusuojaus                                         |
| IP66     | Pölytiiviys ja voimakkaiden vesisuihkujen suojaus                        |
| IP67     | Pölytiiviys ja tilapäisen upotuksen suojaus                              |
| IP68     | Pölytiiviys ja jatkuvan upotuksen suojaus määritellyissä olosuhteissa    |

**IP67 ei automaattisesti sisällä IP65- tai IP66-vesisuihkusuojausta.** Upotus ja vesisuihku ovat erilaisia kokeita. Esimerkiksi IP65/IP67 ilmoittaa molemmat suojaukset. Myöskään vesisuihkusuojaus ei yksin todista upotuksen kestävyyttä.

### Soveltaminen kylmäalalla

Kylmälaitteen anturia, liitintä tai sähkökoteloa arvioitaessa selvitetään, altistuuko se pölylle, roiskeille, pesusuihkulle vai upotukselle. Merkintää verrataan juuri tähän rasitukseen ja valmistajan käyttöehtoihin.

IP-luokka ei yksin kerro kemikaalien, korroosion, iskujen tai käyttölämpötilojen kestävyydestä. Esimerkiksi pesuaineen ja kylmänkestävyyden soveltuvuus tarkistetaan erikseen. Myös liittimen vastakappale ja tiivistys kuuluvat suojauksen kokonaisuuteen.

### Tarkista, että osaat

1. Mitä IP54:n kumpikin numero tarkoittaa?
2. Mikä ero on IP5X:llä ja IP6X:llä?
3. Miksi IPX4 ei kerro pölysuojauksesta?
4. Voiko IP67-merkinnästä päätellä, että laite kestää vesisuihkupesun?

**Vastaukset:** 1) Pölysuojaus ja roiskevesisuojaus. 2) Pölysuojattu / pölytiivis. 3) Ensimmäistä suojausastetta ei ilmoiteta. 4) Ei; vesisuihkusuojaus on varmistettava erikseen.

### IP-osion lähteet

Tarkistettu 5.10.2026. Taulukot ovat tiivistetty opiskelukooste, eivät standardin täydelliset testivaatimukset.

- [IEC 60529: standardin kuvaus](https://webstore.iec.ch/en/publication/2452) — luokituksen standardiperusta.
- [Hammond: Definition of Protection Grades IEC 60529](https://www.hammfg.com/electrical/technical/iec) — kosketus-, vierasesine- ja vesisuojauksen merkitykset.
- [igus: IP protection classes](https://www.igus.eu/harnessing-and-connectors/connectors/ip-protection-classes) — X-merkintä, numeroiden tulkinta ja liittimen suojauksen osat.
- [NorComp: IP Ratings and Harsh Environment Connectors](https://www.norcomp.net/applications/ip-ratings-and-harsh-environment-connectors) — IPX9, käyttöolosuhteet ja IP-luokituksen rajaukset.
- [WIKA: Pressure switches with IP65 and IP67 ingress protection](https://blog.wika.com/en/products/pressure-switches-with-ip65-and-ip67-ingress-protection/) — upotus- ja vesisuihkukokeiden ero.

### IP-koodin lisäkirjaimet A–D

Oppikirjan taulukon lisäkirjain täsmentää suojausta pääsyltä vaarallisiin osiin. Esimerkiksi IPXXB kertoo sormisuojauksesta, vaikka numeroarvoja ei ilmoiteta.

| Kirjain | Suojaus pääsyltä vaarallisiin osiin |
| ------- | ----------------------------------- |
| A       | Kämmenselällä                       |
| B       | Sormella                            |
| C       | Työkalulla                          |
| D       | Langalla                            |

Lähde: oppikirjan luku 5.1, s. 80, oppitunnin lähdeaineisto.

## Tilaluokittelu ja kotelointiluokan valinta

Oppitunti 5.10.2026. **Kotelointiluokka valitaan laitteen todellisen asennuspaikan rasitusten mukaan.** Kosteus, roiskeet, pesuvesi ja lämpötila vaikuttavat eri tavoin. Alla erotetaan oppikirjan opetusesimerkit tarkistetuista lisähuomioista.

### Kostea, märkä ja ulkotila

Oppikirjan s. 82:n kooste:

| Tila tai olosuhde                                                                   | Tunnusomainen rasitus                                                | Kirjan esittämä vähimmäisvesisuojaus |
| ----------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------ |
| Kostea tila                                                                         | Pinnoille tiivistyy kosteutta; vesipisaroita vain poikkeuksellisesti | IPX1                                 |
| Märkä tila                                                                          | Pinnoille tiivistyy pisaroita tai laite altistuu vedelle             | IPX4                                 |
| Ulkotila, sateelta suojattu laite                                                   | Sateelta suojattu, esimerkiksi katoksen alla                         | IPX1                                 |
| Ulkotila, sateelle altis laite                                                      | Sade, ei erityistä roiskevesialtistusta                              | IPX3                                 |
| Ulkotila, sateelle altis laite enintään 0,5 m vaakasuorasta tai kaltevasta pinnasta | Myös pinnasta roiskuva vesi                                          | IPX4                                 |

Kosteita tiloja ovat kirjan esimerkeissä kylmäkellarit, lämmittämättömät varastot ja pyykinkuivaushuoneet. Märkiä tiloja ovat esimerkiksi pesuhallit ja vesisuihkulla pestävät alueet.

**Taulukko on kurssin oppikirjakooste, ei kaikkien asennuspaikkojen täydellinen vaatimuslista.** Vesisuihkupesu voi edellyttää roiskevesisuojausta vahvempaa suojausta. X ei ilmoita vierasesinesuojausta; valinnassa huomioidaan myös IP-koodin ensimmäinen numero ja laitteen käyttöehdot.

Lähde: oppitunnin lähdeaineisto, s. 82.

### Kylpy- ja suihkutilojen alueet

Märkä iho pienentää kehon sähkövastusta. Siksi pesutiloissa sähkölaitteiden sallittu sijoitus ja suojaus arvioidaan alueittain.

Oppikirjan s. 84:n aluemalli:

| Alue                 | Suihku ilman allasta                                                                      | Kylpyamme tai suihkuallas                                |
| -------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| 0                    | Alueen 1 alapuolinen tila 10 cm:n korkeuteen lattiasta                                    | Ammeen tai altaan sisäpuoli                              |
| 1                    | Sivusuunnassa 120 cm kiinteästä suihkusuuttimesta tai vesipisteestä; kuvan korkeus 225 cm | Ammeen tai altaan yläpuolinen alue; kuvan korkeus 225 cm |
| 2                    | Kuvan mallissa ei erillistä aluetta 2                                                     | Sivusuunnassa 60 cm ammeen tai altaan ulkoreunasta       |
| Luokittelematon alue | Edellisten ulkopuolinen tila                                                              | Edellisten ulkopuolinen tila                             |

Kiinteä väliseinä voi rajata alueita. **Etäisyyttä ei arvioida pelkästään seinän läpi suorana mittana:** Tukesin ohjeessa liian matalan tai kapean suojaseinän vaikutus arvioidaan mittaamalla sen reunojen ympäri.

Pelkkä riittävä IP-luokka ei salli mitä tahansa laitetta mille tahansa alueelle. Verkkojännitteisiä pistorasioita ei saa asentaa alueille 0, 1 tai 2. Kirjan mukaan WC:tä, jossa on vain alapesusuihku ja lattiakaivo, ei tämän perusteella luokitella suihkutilaksi.

Lähdekuva: oppitunnin lähdeaineisto, s. 84. Täsmennysten lähde: [Tukes: Kylpy- ja suihkutilojen sähköasennukset](https://tukes.fi/sahko/sahkotyot-ja-urakointi/sahkoasennusten-tekniset-vaatimukset/kylpy-ja-suihkutilojen-sahkoasennukset), tarkistettu 5.10.2026. Varsinainen sijoitus ratkaistaan sovellettavan SFS 6000-7-701:n ja laiteohjeiden mukaan.

### Sauna: IP-luokan lisäksi lämmönkesto

| Alue | Sijainti kuvan mallissa                             | Keskeinen huomio                                                         |
| ---- | --------------------------------------------------- | ------------------------------------------------------------------------ |
| 1    | Kiuas ja sen ympärillä 0,5 m:n alue, kattoon saakka | Vain kiuas ja sen käyttöön liittyvät laitteet                            |
| 2    | Alueen 1 ulkopuolella lattiasta 1 m:n korkeuteen    | Ei erityistä lämpötilaluokitusta, mutta todellinen lämpötila huomioidaan |
| 3    | Alueen 1 ulkopuolella yli 1 m:n korkeudella         | Laitteiden lämmönkesto vähintään 125 °C ja johtojen vähintään 170 °C     |

Saunan sähkölaitteiden kotelointiluokka on vähintään **IP24**. Riittävä IP-luokka ei yksin tarkoita, että esimerkiksi valaisin kestää saunan lämpötilan.

- Tavanomaiset kaapelit sijoitetaan lämpöeristeen kylmälle puolelle.
- Löylyhuoneeseen ei asenneta pistorasioita eikä erillisiä käyttökytkimiä. Kiukaan omat rakenteelliset säätimet ovat eri asia.
- Saunan sähköasennukset lisäsuojataan 30 mA:n vikavirtasuojalla; Tukesin ohjeen poikkeus koskee kiuasta ja siihen liittyviä laitteita.
- Kiukaan suojaetäisyydet ja liitäntä tehdään valmistajan ohjeen mukaan.
- Jos saunassa on suihku, myös suihkun aluerajaukset otetaan huomioon.

Kirjassa mainitaan lisäksi kiukaan liitäntärasian sijoitus: alueella 1 rasian yläreuna enintään 0,5 m lattiasta. Tämä on lähteen opetustieto; laitteen oma asennusohje ja sovellettavat vaatimukset tarkistetaan asennuksessa.

Lähdekuva: oppitunnin lähdeaineisto, s. 86. Tarkistettu vertailulähde: [Tukes: Saunojen sähköasennukset](https://tukes.fi/sahko/sahkotyot-ja-urakointi/sahkoasennusten-tekniset-vaatimukset/saunojen-sahkoasennukset), 5.10.2026.

## Vikasuojaus

Oppitunti 5.10.2026. **Vikasuojaus suojaa sähköiskulta, kun laitteessa tai asennuksessa syntyy vika**, esimerkiksi eristysvaurio tekee kosketeltavan metallikotelon jännitteiseksi. Perussuojaus puolestaan estää koskettamasta normaalisti jännitteisiä osia.

### Oppitunnin neljä suojausmenetelmää

| Menetelmä                              | Perusidea                                                       |
| -------------------------------------- | --------------------------------------------------------------- |
| Kaksoiseristys tai vahvistettu eristys | Suojaus ei jää yhden peruseristyskerroksen varaan               |
| Syötön automaattinen poiskytkentä      | Suojalaite katkaisee viallisen piirin syötön riittävän nopeasti |
| Sähköinen erotus                       | Suojattava piiri erotetaan sähköisesti muista piireistä         |
| SELV tai PELV                          | Pienoisjännite ja suojausjärjestelmän muut vaatimukset yhdessä  |

Tavallinen pienjännite tai pieni jännitelukema ei yksin tarkoita SELV- tai PELV-suojausta. Oppitunnin luettelo on menetelmien yleiskuva; käytännön toteutuksella on omat ehtonsa.

### Kaksoiseristys ja suojausluokka II

Kaksoiseristetty tai vahvistetusti eristetty laite kuuluu **suojausluokkaan II**. Tunnus on **neliö neliön sisällä**. Kaksoiseristyksessä peruseristyksen lisäksi on lisäeristys; vahvistettu eristys antaa vastaavan suojauksen yhtenä eristysrakenteena.

Tällaisia laitteita ovat monet käsityökalut ja kodinkoneet. Suojausluokka II ja IP-luokka kuvaavat eri ominaisuuksia: sähköiskusuojausta ja kotelon suojausta ulkoisilta rasituksilta.

### Syötön automaattinen poiskytkentä – muista 0,4 s

> **Kurssin keskeinen muistettava arvo: tavallisen 230 V:n pistorasialoppupiirin enimmäispoiskytkentäaika TN-järjestelmässä on 0,4 s eli 400 ms.**

Sulake, johdonsuojakatkaisija tai vikavirtasuoja voi toteuttaa poiskytkennän, kun suojauksen toimintaehdot täyttyvät. Pelkkä suojalaitteen olemassaolo ei vielä osoita riittävän nopeaa toimintaa.

**0,4 s ei ole kaikkien sähköpiirien yleinen poiskytkentäaika.** Tarkistetun IEC-pohjaisen TN-ohjeen mukaan 230 V:n vaihe–maa-jännitteellä tämä raja koskee enintään 63 A:n pistorasioita sisältäviä loppupiirejä ja enintään 32 A:n vain kiinteitä laitteita syöttäviä loppupiirejä. Muissa järjestelmissä, jännitteillä tai piirityypeissä vaatimukset voivat olla erilaiset. Asennuksessa sovelletaan SFS 6000:n kyseistä vaatimusta.

**Miksi PE ja silmukkaimpedanssi ovat tärkeitä?** TN-järjestelmässä vikavirta kulkee viallisen kotelon kautta PE/PEN-reittiä takaisin virtalähteeseen. Suuren silmukkaimpedanssin vuoksi vikavirta voi jäädä liian pieneksi laukaisemaan ylivirtasuojan ajoissa. Tämä yhdistää poiskytkentäajan [Miksi silmukkaimpedanssi on tärkeä?](sahkoopin-perusteet.md#miksi-silmukkaimpedanssi-on-tärkeä) -kohtaan.

Dian ilmaus ”PE johtaa vikavirran maahan” on yksinkertaistus: TN-järjestelmässä keskeinen paluureitti on suojajohdinreitti, ei maaperä. **0,4 s on enimmäisaika, ei odotusaika tai turvallinen kosketusaika.**

Lähteet: oppituntidiat oppitunnin lähdeaineisto. Poiskytkentäajan soveltamisalan ja vikavirran reitin täsmennys: [Schneider Electric: TN system – Principle](https://www.electrical-installation.org/enwiki/TN_system_-_Principle), tarkistettu 5.10.2026.

## Yleismittarin kerrannaisyksiköt

| Etuliite     | Tunnus | Kymmenpotenssi |   Kerroin |
| ------------ | -----: | -------------: | --------: |
| mikro        |      µ |           10⁻⁶ | 0,000 001 |
| milli        |      m |           10⁻³ |     0,001 |
| perusyksikkö |      – |            10⁰ |         1 |
| kilo         |      k |            10³ |     1 000 |
| mega         |      M |            10⁶ | 1 000 000 |

Esimerkkejä mittarin lukeman muuttamisesta perusyksiköksi:

- `13 µ = 0,000 013`
- `257 m = 0,257`
- `12,3 = 12,3`
- `0,754 k = 754`
- `1,342 M = 1 342 000`

Monessa yleismittarissa on 3,5 numeron näyttö. Mitta-alueet päättyvät silloin usein arvoon 200 tai 2 000. Mitta-aluetta valittaessa pitää huomioida sekä mitattava suure että etuliite; esimerkiksi `200 m`, `20 k` ja `20 M` tarkoittavat eri suuruusluokkia.

## Yleismittarin CAT-luokat

CAT-luokka kertoo, millaisessa sähköympäristössä mittalaitetta voidaan käyttää ja millaisilta ylijännitepiikeiltä se on suojattu.

| Luokka  | Tyypillinen käyttökohde                            | Esimerkkejä                                              |
| ------- | -------------------------------------------------- | -------------------------------------------------------- |
| CAT I   | elektroniikka ja laitteen sisäiset, rajatut piirit | paristokäyttöiset laitteet                               |
| CAT II  | pistorasiaan liitettävät yksivaiheiset kuormat     | kodinkoneet, pistorasiat                                 |
| CAT III | kiinteät asennukset ja rakennuksen jakelu          | ryhmäkeskukset, sähkökeskukset                           |
| CAT IV  | asennuksen syöttöpiste ja ulkopuoliset johtimet    | pääkeskuksen syöttö, sähkömittari, ilmajohto, maakaapeli |

Sähköasennusten mittaamiseen käytettävässä mittarissa pitää olla käyttökohteeseen riittävä CAT-luokitus.

## Asennustesteri – kurssin tärkein mittari

Asennustesteri on sähköasennusten tarkastamiseen käytettävä mittalaite. Sillä varmistetaan, että asennus toimii oikein ja turvallisesti. Sitä käytetään sekä käyttöönottotarkastuksissa että määräaikaistarkastuksissa.

| Mittaus                           | Mitä tarkistetaan                           | Miksi se tehdään                                                                            |
| --------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Eristysresistanssi (RISO)**     | eristeiden kunto                            | varmistetaan, ettei virtaa vuoda eristeiden läpi                                            |
| **Suojajohtimen jatkuvuus (RLO)** | suojamaadoituksen jatkuvuus                 | varmistetaan vikasuojauksen toiminta                                                        |
| **Silmukkaimpedanssi (Z)**        | vaiheen ja suojamaan välinen vikavirtapiiri | selvitetään mahdollisen oikosulkuvirran suuruus ja suojalaitteiden riittävän nopea toiminta |
| **Vikavirtasuojakytkin (RCD)**    | laukaisuvirta `IΔn` ja laukaisuaika `ΔT`    | varmistetaan vikavirtasuojan oikea toiminta                                                 |
| **Jännite**                       | asennuksen jännite voltteina                | varmistetaan oikea jännitetaso                                                              |
| **Vaihejärjestys**                | kolmivaiheverkon vaiheiden järjestys        | varmistetaan muun muassa moottorien oikea pyörimissuunta                                    |
| **Maadoitusvastus**               | maadoituksen resistanssi                    | arvioidaan maadoituksen toimivuutta                                                         |

### Miksi silmukkaimpedanssi on tärkeä?

Silmukkaimpedanssi määrittää mahdollisen oikosulkuvirran suuruutta. Mitä suurempi impedanssi, sitä pienemmäksi vikavirta jää. Liian suuri impedanssi voi estää sulakkeen tai johdonsuojakatkaisijan riittävän nopean toiminnan ja heikentää sähköturvallisuutta.

### Käyttöönottotarkastuksen dokumentointi

Mittaustulokset kirjataan käyttöönottotarkastuksen pöytäkirjaan. Suomessa käytetään SFS 6000 -standardisarjan mukaisia mittauksia.

### Opastevideo

- [Teemu Tuomela – Jännitteettömät käyttöönottomittaukset](https://www.youtube.com/watch?v=Sm4hDTJXL98) — pienen sähkökeskuksen jännitteettömänä tehtävät käyttöönottomittaukset (Rasekon ammattiopiston harjoitustyö).

## Vaihtosähkö

Oppitunti 21.9.2026.

### Vaihtosähkön peruskäsitteitä

Vaihtosähkössä jännitteen ja virran suunta sekä hetkellinen arvo muuttuvat ajan funktiona. Sinimuotoisen vaihtosähkön yhtä täydellistä jaksoa voidaan kuvata myös kulmana:

- 90° = π/2
- 180° = π
- 270° = 3π/2
- 360° = 2π

Kolmivaiheverkossa oppitunnilla käytetyt nimelliset jännitteet:

- vaihe–nolla: **230 V**
- vaihe–suojamaa: **230 V**
- vaihe–vaihe: **400 V**
- nolla–suojamaa: **0 V** ideaalitilanteessa / normaalisti hyvin lähellä nollaa

### Jännitteen mittaaminen kolmivaiheverkossa

Muistiinpanojen mittausryhmät:

1. PE–L1, PE–L2, PE–L3 → noin 230 V
2. N–L1, N–L2, N–L3 → noin 230 V
3. L1–L2, L1–L3, L2–L3 → noin 400 V
4. N–PE → ideaalitilanteessa 0 V

Näillä mittauksilla voidaan todeta vaiheiden ja jännitetasojen olevan odotetun kaltaisia. Käytännön mittaukset tehdään vain koulutuksen ja sähköturvallisuusohjeiden mukaisesti.

Lähde: käsinkirjoitetut muistiinpanot, kuva oppitunnin lähdekuva (21.9.2026).

### Vaihtovirran mittaus

Virran mittauksella voidaan selvittää esimerkiksi:

- kuinka paljon laite kuluttaa sähköä
- onko laite kunnossa
- onko kuorma oikean kokoinen
- onko piirissä vikaa
- ottaako laite nimellisvirran

Lähde: oppituntidia ”Vaihtovirran mittaus”, kuva oppitunnin lähdekuva (21.9.2026).

### Pihtiampeerimittari

Pihtiampeerimittarilla virta voidaan mitata **ilman johtimen katkaisua**. Tämä tekee mittauksesta nopean ja mahdollistaa myös suurten virtojen mittaamisen.

Toimintaperiaate oppitunnin mukaan:

1. Johtimessa kulkeva virta synnyttää magneettikentän.
2. Pihtimittari mittaa tämän magneettikentän.
3. Mittari ilmoittaa virran suoraan ampeereina.

Pihtimittarin pihdit asetetaan mitattavan **yhden virtajohtimen** ympärille. Jos saman pihdin sisällä kulkevat meno- ja paluuvirta, niiden magneettikentät voivat kumota toisensa eikä tavallista kuormavirtaa saada mitattua oikein.

Lähde: oppituntidia ”Pihtiampeerimittari”, kuva oppitunnin lähdekuva (21.9.2026). Viimeinen kappale on mittaustavan ymmärtämistä tukeva täsmennys.

### Pihtiampeerimittarin käyttökohteita

Oppitunnilla mainittuja käyttökohteita:

- ryhmäkeskukset
- sähkökeskukset
- moottoreiden mittaukset
- lämpökaapeleiden mittaukset
- vikojen etsintä

Lähde: oppituntidia, kuva oppitunnin lähdekuva (21.9.2026).

### Yksivaiheisen vaihtojännitteen synty

Yksivaiheisen vaihtosähkön tuottamisen perusidea esitettiin pyörivän magneetin ja kelan avulla:

- magneetti pyörii kelan läheisyydessä
- magneetin asennon muuttuessa kelan läpi kulkeva magneettivuo muuttuu
- muuttuva magneettivuo indusoi kelaan jännitteen
- magneetin yksi täysi kierros synnyttää yhden täydellisen jännitejakson

Käämi eli kela on johdinta, joka on kierretty kierroksiksi.

Lähteet: oppituntidiat ”Yksivaiheisuus”, kuvat oppitunnin lähdekuva ja oppitunnin lähdekuva (21.9.2026).

### Sinimuotoinen jännite

Vaihtojännite muuttuu sinikäyrän mukaisesti. Yksi jakso muodostuu positiivisesta ja negatiivisesta puolijaksosta. Yksi täydellinen aalto on yksi jakso.

Pyörivän magneetin asennon ja syntyvän jännitteen yhteys oppitunnin mallissa:

| Magneetin kulma | Jännite             |
| --------------: | ------------------- |
|              0° | 0 V                 |
|             90° | suurin positiivinen |
|            180° | 0 V                 |
|            270° | suurin negatiivinen |
|            360° | 0 V                 |

Yksi magneetin täysi pyörähdys vastaa yhtä jännitejaksoa.

Lähteet: oppituntidiat ”Sinimuotoinen jännite”, kuvat oppitunnin lähdekuva ja oppitunnin lähdekuva (21.9.2026).

### Hetkellis-, huippu- ja tehollisarvo

Sinimuotoisen vaihtojännitteen arvo muuttuu jatkuvasti ajan mukana. Oppitunnin kuvassa 230 V verkkojännitteen:

- **huippuarvo** on noin 325 V
- negatiivinen huippu on noin −325 V
- **tehollisarvo** on 0,707 × huippuarvo eli noin 230 V
- huipusta huippuun -arvo on noin 650 V
- yksi jakso kestää **T = 20 ms**
- taajuus saadaan kaavalla **f = 1/T**, joten 20 ms jaksonaika vastaa 50 Hz taajuutta

Kaavat:

- `U_eff = 0,707 × Û = Û / √2`
- `Û = √2 × U_eff`
- `U_pp = 2 × Û`
- `f = 1 / T`
- `T = 1 / f`

Tässä `U_eff` on tehollisarvo, `Û` huippuarvo, `U_pp` huipusta huippuun -arvo, `f` taajuus ja `T` jaksonaika.

Jännitteen **hetkellisarvo** `u` on tietyllä hetkellä havaittu jännite. Sinimuotoiselle jännitteelle hetkellisarvo voidaan laskea huippuarvosta ja vaihekulmasta:

`u = û × sin α`

- `u` = jännitteen hetkellisarvo (V)
- `û` = jännitteen huippuarvo (V)
- `α` = vaihekulma

Oppimateriaalin mukaan tehollisarvo `U` tarkoittaa vaihtojännitettä, joka tuottaa resistiivisessä kuormassa saman tehon kuin samansuuruinen tasajännite. Kun jännitteestä puhutaan ilman muuta täsmennystä, ilmoitettu arvo on yleensä tehollisarvo; esimerkiksi verkon 230 V ja 400 V ovat tehollisarvoja.

Lähde: oppituntidia ”Sinimuotoisen vaihtosähkön hetkellis- ja huippuarvot”, kuva oppitunnin lähdekuva (21.9.2026).

Lähde hetkellisarvon kaavalle ja tehollisarvon määritelmälle: oppimateriaali, kuva oppitunnin lähdekuva (21.9.2026).

## Sähkön tuotanto, siirto ja jakelu

Sähköjärjestelmän perusketju:

1. Sähköä tuotetaan esimerkiksi ydin-, vesi-, tuuli- ja lämpövoimalaitoksissa.
2. Muuntaja nostaa jännitteen pitkän matkan siirtoa varten.
3. Kantaverkon tyypilliset jännitteet ovat 400, 220 ja 110 kV.
4. Sähköasemalla jännite muunnetaan paikalliseen keskijänniteverkkoon, tavallisesti noin 20 kV:iin.
5. Jakelumuuntaja muuttaa jännitteen 0,4 kV:iin eli kolmivaiheverkon 400/230 V tasolle.
6. Sähkö kulkee kiinteistöihin maa- tai ilmajohtoa pitkin.

**HVDC** tarkoittaa suurjännitteistä tasasähköyhteyttä. Sitä käytetään muun muassa pitkillä siirtoetäisyyksillä ja sellaisten sähköverkkojen yhdistämiseen, jotka eivät ole keskenään synkronoituja. Tasajänniteyhteyden yli eivät myöskään välity vaihtojänniteverkon taajuushäiriöt samalla tavalla.

## Kiinteistön sähkönsyöttö ja TN-C-S-järjestelmä

Tyypillisessä pienkiinteistön syötössä jakelumuuntajalta tulee neljä johdinta:

- `L1`, `L2`, `L3` = vaihejohtimet
- `PEN` = yhdistetty nolla- ja suojajohdin

Tätä verkon osaa kutsutaan **TN-C-järjestelmäksi**. Kiinteistön pääkeskuksessa PEN-johdin erotetaan:

- `N` = nollajohdin
- `PE` = suojajohdin

Erotuksen jälkeen kiinteistön sisäinen verkko on viisijohtiminen **TN-S-järjestelmä**: L1, L2, L3, N ja PE. Kokonaisuutta kutsutaan TN-C-S-järjestelmäksi.

### Jännitteet kolmivaiheverkossa

- Vaiheiden välinen jännite on **400 V**.
- Vaihejohtimen ja nollajohtimen välinen jännite on **230 V**.
- Tavallinen pistorasia käyttää yhtä vaihetta ja nollaa, joten sen jännite on 230 V.

### Suojaus ja maadoitus

- Pääkeskukseen kuuluvat muun muassa pääsulakkeet, sähkömittari, pääkytkin ja johdonsuojakatkaisijat.
- Johdonsuojakatkaisijat suojaavat asennuksia oikosululta ja ylikuormitukselta.
- PE-johdin yhdistää sähkölaitteen kosketeltavat metalliosat suojamaadoitukseen.
- Päämaadoituskisko yhdistää suojamaadoituksen, maadoituselektrodin ja potentiaalintasauksen, kuten metalliset vesiputket ja rakennuksen raudoitukset.

## Sähkötöiden tekemisen oikeus

Oppikirjan mukaan sähköasentaja, jolla ei ole urakointioikeuksia eli oikeutta tehdä sähkötöitä itsenäisesti, työskentelee sähkötöiden johtajan alaisuudessa yrityksessä, jolla on asianmukainen pätevyys. Ennen käytännön töitä vaatimusten ajantasaisuus tarkistetaan Tukesin ohjeista ja kouluttajalta.

## Asennuspiirustusten piirrosmerkkejä

Oppitunti 21.9.2026.

**Asennuspiirustuksen piirrosmerkit** välittävät tiiviisti tietoa tilasta, johdotuksesta ja sähkölaitteista. Merkin ulkomuoto pitää tunnistaa kuvasta; alla oleva kooste kertoo sen merkityksen.

oppitunnin lähdeaineisto

### Tilan ja johdotuksen merkinnät

| Merkki kuvassa                   | Merkitys                           |
| -------------------------------- | ---------------------------------- |
| Yksi pisara neliössä             | Kostea tila                        |
| Kaksi pisaraa neliössä           | Märkä tila                         |
| `Pa` neliössä                    | Palovaarallinen tila               |
| `T` neliössä                     | Kuuma tai kylmä tila               |
| Nuoli ja ryhmänumeron ympyrä     | Ryhmänumero; ympyrä on skaalautuva |
| Johdinviiva ja yksi poikkimerkki | Yksi johdin, vaihe `L`             |
| Johdinviivan N-merkintä          | Nollajohdin `N`                    |
| Johdinviivan PE-merkintä         | Suojajohdin `PE`                   |

### Kytkimet, tunnistimet ja merkkilamput

- himmennin / tehonsäädin
- himmennin kytkimellä
- himmennin vaihtokytkimellä
- painikekytkin eli painike
- painikekytkin merkkilampulla
- hämäräkytkin
- liiketunnistin
- merkkilamppu

**Tunnistamisvihje:** himmentimien merkeissä perusosa on sama, mutta kytkintoiminto näkyy siihen liitetystä kytkinmerkinnästä. Painikkeen sisällä oleva lamppumerkki erottaa merkkilampullisen painikkeen tavallisesta painikkeesta.

Lähde: oppitunnilla esitetty tehtävä ”Nimeä seuraavat asennuspiirustuksissa käytettävät piirrosmerkit”, oppitunnin lähdeaineisto (21.9.2026).

## Sähköpiirustuksen lukeminen: yhden valaisimen ohjaus

Oppitunti 28.9.2026. Esimerkki havainnollistaa perustasoa: tunnista syöttö, komponentit, johtimien tehtävät ja lukumäärät sekä selitä kytkennän toiminta. Pelkkä piirrosmerkkien nimeäminen ei vielä kerro, miten piiri toimii.

### Millainen piirustus tämä on?

Kuvan ympyröity osa on **yksiviivainen johdotus-/asennusesitys** yhden valaisimen ohjauksesta yhdellä kytkimellä. Yksi pitkä viiva kuvaa johdotusreittiä, ei välttämättä yhtä johdinta. Reitin poikki piirretyillä lyhyillä merkeillä esitetään johtimien lukumäärä ja tehtävät.

Tämä ei ole sama asia kuin moniviivainen kytkentäkuva, jossa jokaisen johtimen reitti ja liitokset näytetään erikseen. Jakorasian sisäiset liitokset on tässä pääteltävä kytkennän toiminnan perusteella.

### Kuvan merkit

| Kuvassa näkyvä merkintä                                      | Tulkinta tässä esimerkissä                                                                                                   |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| `RK`                                                         | Ryhmäkeskus, josta ryhmän syöttö tulee.                                                                                      |
| Nuoli ja numero ympyrässä                                    | Ryhmän syöttö ja ryhmänumero. Numero näyttää olevan **5**; se ei tarkoita 5 ampeerin sulaketta.                              |
| `JR` ja tumma ympyrä haarautumiskohdassa                     | Jakorasia. Siellä tehdään eri johtimien väliset tarvittavat liitokset. Rasian mustaus tarkoittaa tavallisesti uppoasennusta. |
| Ympyrä, jonka sisällä on risti                               | Valaisin.                                                                                                                    |
| Alhaalla pieni ympyrä ja yksi vino kytkinvarsi               | Yksinapainen **1-kytkin**: yhden valaisimen tai valaisinryhmän päälle/pois-ohjaus yhdestä paikasta.                          |
| Tavallinen lyhyt poikkiviiva johdotusreitillä                | Vaihejohdin; kytkimen jälkeen kyse on kytketystä vaiheesta.                                                                  |
| Poikkiviiva, jonka päässä on piste                           | Nollajohdin **N**.                                                                                                           |
| Poikkiviiva, jonka päässä on lyhyt poikkihattu, T-mäinen pää | Suojajohdin **PE**.                                                                                                          |

**N:n ja PE:n tunnistaminen:** tässä merkintätavassa **piste = N, hattu = PE**. Kyse on johdotuksen piirrosmerkeistä, ei johtimien väreistä. Merkinnät tarkistetaan aina käytettävän piirustuksen selitteestä.

Taulun yläosassa näkyvä **1,5 mm²** tarkoittaa johtimen poikkipinta-alaa, ei halkaisijaa. Kuvan rajauksesta ei yksin varmistu, mille kaikille johdoille merkintä on tarkoitettu. Kaapelityyppiä tai sulakkeen kokoa ei päätellä tästä merkinnästä yksin.

### Mitä johtimia eri väleillä kulkee?

Seuraava on kuvan mukaisen yksinkertaisen 1-kytkennän toimintatulkinta. Merkintä `L′` tarkoittaa tässä **kytkettyä vaihetta**, ei toista syöttävää vaihetta.

| Väli                    | Kuvassa esitetyt johtimet                                    | Määrä |
| ----------------------- | ------------------------------------------------------------ | ----: |
| Ryhmäkeskus → jakorasia | Syöttävä vaihe `L`, nolla `N` ja suojajohdin `PE`            |     3 |
| Jakorasia → kytkin      | Syöttävä vaihe `L` ja kytkimeltä palaava kytketty vaihe `L′` |     2 |
| Jakorasia → valaisin    | Kytketty vaihe `L′`, nolla `N` ja suojajohdin `PE`           |     3 |

**Kytkimelle menevät kaksi johdinta eivät tässä ole vaihe ja nolla.** Toinen vie vaiheen kytkimelle ja toinen tuo kytketyn vaiheen takaisin jakorasiaan, josta se jatkuu valaisimelle. N ja PE jatkuvat tässä esityksessä jakorasiasta valaisimelle kulkematta kytkimen koskettimen kautta.

Johdinmäärät kuvaavat tätä opetusesimerkkiä. Ne eivät yksin määritä todellisen asennuksen kaapelivalintaa, suojajohtimen tarvetta kytkinpaikalla tai muita asennusvaatimuksia.

### Jakorasian kytkentä moniviivaisessa johdotuskaaviossa

Täydentävä oppituntikuva 28.9.2026 näyttää saman **yksinapaisen kytkimen eli 1-kytkimen** kytkennän kolmella tavalla: vasemmalla on toimintaperiaate, keskellä moniviivainen johdotuskaavio ja oikealla yksiviivainen esitys. Keskimmäisestä kuvasta nähdään myös jakorasian sisäiset liitokset, jotka eivät erottuneet edellisessä taulukuvassa.

Kuvan laitetunnukset ovat **X1 = jakorasia**, **Q1 = kytkin** ja **E1 = valaisin**. Nämä ovat tämän piirustuksen tunnuksia; edellisen kuvan JR tarkoittaa samaa jakorasiaa.

**Jakorasiassa X1 on neljä erillistä liitoskohtaa:**

| Johdin                               | Mihin se yhdistyy jakorasiassa?                     |
| ------------------------------------ | --------------------------------------------------- |
| Syötön vaihe `L`                     | Kytkimelle Q1 menevään vaihejohtimeen.              |
| Kytkimeltä Q1 palaava kytketty vaihe | Valaisimelle E1 menevään kytkettyyn vaihejohtimeen. |
| Syötön nolla `N`                     | Valaisimelle E1 menevään nollajohtimeen.            |
| Syötön suojajohdin `PE`              | Valaisimelle E1 menevään suojajohtimeen.            |

Kytketystä vaiheesta käytetään tässä muistiossa selittävää merkintää `L′`; sitä ei ole kirjoitettu tähän lähdekuvaan.

**Rasian sisällä kaikki johtimet eivät yhdisty keskenään.** N ja PE jatkuvat omina erillisinä yhteyksinään valaisimelle. Syöttävän vaiheen ja kytketyn vaiheen liitokset ovat myös erillään toisistaan: niiden välinen ohjattu yhteys muodostuu kytkimessä Q1, ei jakorasiassa.

X1:n katkoviivarajaus osoittaa rasian alueen, ei sähköjohdinta. Sen sisällä olevat **mustat pisteet osoittavat liitoskohtia**. Tässä moniviivaisessa kuvassa piste ei siis tarkoita automaattisesti nollajohdinta, toisin kuin edellisen yksiviivaisen kuvan pistepäinen johdinmerkki. Merkkiä luetaan aina oman esitystapansa yhteydessä.

Kuvan kytkin on piirretty avoimeksi. Kun Q1 sulkeutuu, käyttövirtapiirin reitti on **L → X1 → Q1 → X1 → E1 → N**. Tämä reitti täydentää edellä esitettyä toimintaperiaatetta näyttämällä jakorasian molemmat vaiheliitokset.

Lähde: oppimateriaalin kohta **6.5 Valaistusasennukset / Valaistuskytkimet ja valaistuskytkennät**, taulukon rivi **Yksinapainen kytkin, 1-kytkin**. Selitys perustuu vain kuvassa näkyvään riviin; kuvan alareunan seuraavaa kytkentää ei ole tulkittu.

### Miten valo syttyy?

Jakorasiassa syötön vaihe jatkuu kytkimelle. Kytkimen sulkeutuessa yhteys jatkuu kytketyssä vaihejohtimessa takaisin jakorasiaan ja edelleen valaisimelle. Valaisimen toinen virtapiirin liitäntä yhdistyy nollajohtimeen: valaisimen käyttövirtapiiri sulkeutuu ja valo syttyy. Kytkimen avautuminen katkaisee vaihereitin ja valo sammuu.

Toiminnallinen reitti voidaan muistaa muodossa **L → kytkin → valaisin → N**. Nuoli kuvaa tässä reitin seuraamista, ei vaihtovirran pysyvää kulkusuuntaa.

PE on erillinen suojajohdin, ei valaisimen käyttövirran paluujohdin. Suojamaadoitettavan valaisimen PE liitetään sille tarkoitettuun suojamaadoitusliittimeen. Valaisimen suojausluokka ja valmistajan ohje ratkaisevat varsinaisen liittämisen; pelkkä valaisimen yleismerkki ei kerro suojausluokkaa.

**Turvallisuusraja:** sammunut valo tai seinäkytkimen avaaminen ei todista työskentelykohdetta jännitteettömäksi. Tämä on piirustuksen lukuharjoitus, ei itsenäisen sähköasennustyön ohje; käytännön harjoittelu tehdään opettajan ohjauksessa asianmukaisesti jännitteettömäksi tehdyllä ja todetulla kohteella.

### Kertaus

Osaat tulkita esimerkin, kun pystyt omin sanoin kertomaan, mistä syöttö tulee, missä liitokset tehdään, mitä kytkin ohjaa, miksi kytkimelle on piirretty kaksi johdinta ja miksi valaisimelle kolme. Lisäksi osaat erottaa nollajohtimen suojajohtimesta sekä ryhmänumeron sulakkeen nimellisvirrasta.

Piirrosmerkkien vertailu ja turvallisuustäsmennykset tarkistettu 28.9.2026:

- [Sähköinsinööritoimisto Kuvio: Piirrosmerkit](https://www.sahkokuvio.fi/palvelut/sahkosuunnittelusta/piirrosmerkit/) — kytkimet, valaisimet ja suunnitelmakohtaisen selitteen merkitys.
- [Rakennusten sähköpiirustusten piirrosmerkit, PDF](https://www.sivustot.net/oppaat/PIIRROSMERKIT.pdf) — PDF-sivut 9–10: johdinmerkit, jakorasiat ja ryhmän syöttö. Vanha vertailuaineisto piirrosmerkeille, ei ajantasainen asennus- tai johdinväriohje.
- [Tukes: Mitä sähkötöitä saan tehdä itse](https://tukes.fi/kodin-sahkoturvallisuus/mita-sahkotoita-saan-tehda-itse) — jännitteettömyys ja valaisimen suojajohtimen oikea käyttötarkoitus.

## Alkuperäiset kuvat

- oppitunnin lähdeaineisto — sähköiset suureet, yksiköt ja CAT-luokat

- oppitunnin lähdeaineisto — yleismittarin kerrannaisyksiköt ja mitta-alueet

- oppitunnin lähdeaineisto — kiinteistön 400/230 V sähkönsyöttö ja TN-C-S

- oppitunnin lähdeaineisto — sähköntuotanto, kantaverkko ja jakeluverkko

- oppitunnin lähdeaineisto — jänniteluokat ja sähkötöiden tekemisen oikeus

- oppitunnin lähdeaineisto — sähkövirran fysiologiset vaikutukset

- oppitunnin lähdeaineisto — sähkövirran ja elektronien suunnat sekä sähkövaraus

- oppitunnin lähdeaineisto — Ohmin lain sarjakytkentäesimerkki sekä kylmätekniikan mittausmuistiinpanoja

- oppitunnin lähdeaineisto — asennustesteri sekä RISO-, RLO- ja Z-mittaukset

- oppitunnin lähdeaineisto — RCD-testaus, muut mittaukset, silmukkaimpedanssin merkitys ja käyttöönottotarkastus

- oppitunnin lähdeaineisto — vastusten sarja- ja rinnankytkentä (7.9.2026)

- oppitunnin lähdeaineisto — 1-kytkennän vähimmäislukutaidon opetusesimerkki (28.9.2026)

- oppitunnin lähdeaineisto — 1-kytkimen toimintaperiaate ja jakorasian moniviivainen kytkentä

- oppitunnin lähdeaineisto — piirrosmerkkien oppituntivertailu

- oppitunnin lähdeaineisto — oppitunnin aineisto 5.10.2026

- oppitunnin lähdeaineisto — oppitunnin aineisto 5.10.2026

- oppitunnin lähdeaineisto — oppitunnin aineisto 5.10.2026

- oppitunnin lähdeaineisto — oppitunnin aineisto 5.10.2026

- oppitunnin lähdeaineisto — oppitunnin aineisto 5.10.2026

- oppitunnin lähdeaineisto — oppitunnin aineisto 5.10.2026

- oppitunnin lähdeaineisto — oppitunnin aineisto 5.10.2026
