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
- sähkövirran vaikutukset ihmiseen
- yleismittarin kerrannaisyksiköt, mitta-alueet ja CAT-luokat
- asennustesterin käyttö ja keskeiset mittaukset
- sähkön tuotanto, siirto ja jakelu
- kolmivaiheverkon 400/230 V jännitteet
- TN-C- ja TN-S-järjestelmät sekä PEN-, N- ja PE-johtimet
- asennuspiirustuksissa käytettävät piirrosmerkit ja niiden merkitykset

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
