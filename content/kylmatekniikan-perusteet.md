---
title: "Kylmätekniikan perusteet"
publish: true
---

Kylmäaineryhmät, lämpötilaliukuma, ODP ja GWP: [Kylmäaineet](kylmaaineet.md).

## Kylmälaitoksen peruskierto

Kylmäaine kiertää suljetussa piirissä neljän pääosan kautta:

1. **Kompressori** imee höyrystimeltä palaavan matalapaineisen kylmäainehöyryn ja puristaa sen kuumaksi korkeapaineiseksi höyryksi.
2. **Lauhdutin** luovuttaa lämpöä ympäristöön. Kylmäaine jäähtyy ja tiivistyy korkeapaineiseksi nesteeksi.
3. **Paisuntalaite** laskee kylmäaineen painetta ja säätelee sen virtausta höyrystimelle. Paineen laskiessa myös kylmäaineen lämpötila laskee.
4. **Höyrystin** sitoo lämpöä jäähdytettävästä kohteesta. Kylmäaine höyrystyy ja palaa matalapaineisena höyrynä kompressorille.

**Muistisääntö:** kompressori nostaa painetta → lauhdutin luovuttaa lämpöä → paisuntalaite pudottaa painetta → höyrystin ottaa lämpöä.

## Korkea- ja matalapainepuoli

- **HP eli korkeapainepuoli** alkaa kompressorin painepuolelta ja jatkuu kuumakaasuputken, lauhduttimen ja nesteputken kautta paisuntalaitteelle.
- **LP eli matalapainepuoli** alkaa paisuntalaitteen jälkeen ja jatkuu höyrystimen sekä imuputken kautta kompressorin imupuolelle.
- Harjoituskaaviossa HP-puoli on merkitty punaisella ja LP-puoli sinisellä. Tarkemmassa kaaviossa putket on eroteltu olomuodon mukaan: kuumakaasu punaisella, lauhduttimelta lähtevä neste oranssilla, nesteputki vaaleansinisellä ja imuputki violetilla.

| Putki                        | Sijainti kierrossa                      | Kylmäaineen pääasiallinen tila   |
| ---------------------------- | --------------------------------------- | -------------------------------- |
| Kuumakaasuputki / paineputki | kompressori → lauhdutin                 | kuuma korkeapaineinen höyry      |
| Nesteputki                   | lauhdutin / nestesäiliö → paisuntalaite | korkeapaineinen neste            |
| Imuputki                     | höyrystin → kompressori                 | matalapaineinen tulistunut höyry |

## Lämpötilojen mittauspisteet

Kaavioon merkityt mittauspisteet:

- **T1:** imuputken lämpötila höyrystimen jälkeen; käytetään tulistuksen laskemiseen.
- **T2:** nesteputken lämpötila ennen paisuntalaitetta; käytetään alijäähdytyksen laskemiseen.
- **T3:** kuumakaasuputken lämpötila kompressorin jälkeen.

## Tulistus ja alijäähdytys

### Tulistus, SH

`SH = imuputken mitattu lämpötila − imupainetta vastaava kyllästymislämpötila`

Tulistuksella varmistetaan, että kompressorille palaava kylmäaine on kokonaan kaasua. Tämä suojaa kompressoria nestemäiseltä kylmäaineelta ja nesteiskuilta.

**Kurssin muistisääntö:** imupainetta vastaavan kyllästymis- eli höyrystymislämpötilan tulisi olla **5–15 K kylmälaitteen tavoitelämpötilaa alempi**.

### Alijäähdytys, SC

`SC = korkeapainetta vastaava kyllästymislämpötila − nesteputken mitattu lämpötila`

Alijäähdytyksellä varmistetaan, että paisuntalaitteelle tuleva kylmäaine on nestettä eikä nesteputkessa ole ennenaikaisesti syntynyttä höyryä eli flash-kaasua.

### Harjoituksen mittausesimerkki

| Arvo                                      |     Tulos |
| ----------------------------------------- | --------: |
| LP                                        |   2,0 bar |
| HP                                        |   9,0 bar |
| Imuputken lämpötila T1                    |    +10 °C |
| Kuumakaasuputken lämpötila T3             |    +60 °C |
| Nesteputken lämpötila T2                  |    +35 °C |
| LP-painetta vastaava kyllästymislämpötila |  +0,79 °C |
| HP-painetta vastaava kyllästymislämpötila | +39,44 °C |

`SH = 10 − 0,79 = 9,21 K`

`SC = 39,44 − 35 = 4,44 K`

Muistiinpanoissa tulistuksen suuntaa-antavaksi alueeksi on merkitty **6–10 K** ja alijäähdytyksen alueeksi **2–4 K**. Kaaviossa tulistuksesta esiintyy myös laajempi **6–15 K** alue. Oikea tavoite määräytyy laitteen, kylmäaineen, paisuntalaitteen ja valmistajan ohjeiden mukaan.

Kyllästymislämpötila luetaan aina käytetyn kylmäaineen paine–lämpötila-taulukosta tai mittarista. Laskussa pitää huomioida myös, ilmoitetaanko paine yli- vai absoluuttisena paineena. Jos kylmäaineella on lämpötilaliukuma, tulistuksessa käytetään kastepistelämpötilaa ja alijäähdytyksessä kuplapistelämpötilaa.

## Entalpia

Muistiinpanon ilmaus ”entalpia = energia” toimii muistivihjeenä, mutta täsmällisemmin kylmätekniikassa käytetään tavallisesti **ominaista entalpiaa** `h`, jonka yksikkö on `kJ/kg`. Se kuvaa kylmäaineen energiasisältöä massayksikköä kohti valittuun vertailutasoon nähden. Kylmäprosessin lämmönsiirtoa ja kompressorityötä tarkastellaan entalpiaerojen avulla.

## Kylmäkaavion visuaalinen symbolisanasto

Alla oleva sarja on kylmäkierron kaavioiden lukemiseen tehty SVG-kirjasto. Symbolit ovat samassa 64 × 64 -järjestelmässä kuin sähköpiirustusten symbolit. **Lähdevertailtu** tarkoittaa, että merkki on piirretty nimetyn lähteen perusteella. **Sovellettu** tarkoittaa, että merkki on koottu tai yksinkertaistettu lähteistetystä perusmerkistä tiettyyn kylmäalan käyttötarkoitukseen.

### Peruskylmäkierto

Peruskylmäkierron neljä pääkomponenttia voidaan lukea järjestyksessä:

**kompressori → lauhdutin → paisuntalaite → höyrystin → kompressori**

| Symboli                                                                              | Nimi                                       | Tehtävä                                                                    |
| ------------------------------------------------------------------------------------ | ------------------------------------------ | -------------------------------------------------------------------------- |
| ![Sähköpiirrosmerkki: kylma kompressori](symbolit/kylma-kompressori.svg)             | Kompressori                                | Nostaa kylmäainehöyryn painetta ja ylläpitää kiertoa.                      |
| ![Sähköpiirrosmerkki: kylma lauhdutin](symbolit/kylma-lauhdutin.svg)                 | Lauhdutin                                  | Luovuttaa lämpöä ja lauhduttaa kylmäainetta.                               |
| ![Sähköpiirrosmerkki: kylma paisuntaventtiili](symbolit/kylma-paisuntaventtiili.svg) | Termostaattinen paisuntaventtiili, TEV/TXV | Säätelee kylmäaineen syöttöä höyrystimeen ja aiheuttaa paineen alenemisen. |
| ![Sähköpiirrosmerkki: kylma hoyrystin](symbolit/kylma-hoyrystin.svg)                 | Höyrystin                                  | Ottaa lämpöä jäähdytettävästä kohteesta kylmäaineen höyrystyessä.          |

![Sähköpiirrosmerkki: kylma putki](symbolit/kylma-putki.svg)

**Kylmäaineputken viiva ei yksin kerro, onko kyse imu-, neste- vai kuumakaasuputkesta.** Putken tehtävä päätellään sijainnista kierrossa ja kaavion selitteestä.

### Säiliöt, erotus ja nestelinja

| Symboli                                                                  | Nimi                            | Tehtävä / rajaus                                                                              |
| ------------------------------------------------------------------------ | ------------------------------- | --------------------------------------------------------------------------------------------- |
| ![Sähköpiirrosmerkki: kylma nestesailio](symbolit/kylma-nestesailio.svg) | Nestesäiliö                     | Varastoi nestemäistä kylmäainetta korkeapainepuolella. Sovellettu painesäiliön perusmerkistä. |
| ![Sähköpiirrosmerkki: kylma imuvaraaja](symbolit/kylma-imuvaraaja.svg)   | Imuvaraaja / nesteenerotin      | Erottaa nestemäistä kylmäainetta imukaasusta ennen kompressoria.                              |
| ![Sähköpiirrosmerkki: kylma oljynerotin](symbolit/kylma-oljynerotin.svg) | Öljynerotin                     | Erottaa öljyä kompressorin painepuolen kylmäainehöyrystä. Sovellettu erottimen yleismerkistä. |
| ![Sähköpiirrosmerkki: kylma kuivain](symbolit/kylma-kuivain.svg)         | Suodatinkuivain                 | Poistaa kylmäaineesta kosteutta ja epäpuhtauksia.                                             |
| ![Sähköpiirrosmerkki: kylma nakolasi](symbolit/kylma-nakolasi.svg)       | Näkölasi kosteusindikaattorilla | Mahdollistaa kylmäaineen tilan tarkastelun; indikaattori tulkitaan valmistajan ohjeesta.      |

Tyypillisessä nestelinjassa voidaan nähdä esimerkiksi **nestesäiliö → suodatinkuivain → näkölasi → paisuntaventtiili**, mutta todellinen komponenttijärjestys tarkistetaan aina kyseisen järjestelmän kaaviosta.

### Venttiilit

| Symboli                                                                                | Nimi                              | Tehtävä / rajaus                                                                                         |
| -------------------------------------------------------------------------------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------- |
| ![Sähköpiirrosmerkki: kylma sulkuventtiili](symbolit/kylma-sulkuventtiili.svg)         | Sulkuventtiili, yleismerkki       | Katkaisee virtausreitin; ei ilmaise venttiilin rakennetyyppiä tai asentoa.                               |
| ![Sähköpiirrosmerkki: kylma palloventtiili](symbolit/kylma-palloventtiili.svg)         | Palloventtiili                    | Pallorakenteinen sulkuventtiili.                                                                         |
| ![Sähköpiirrosmerkki: kylma takaiskuventtiili](symbolit/kylma-takaiskuventtiili.svg)   | Takaiskuventtiili                 | Sallii virtauksen yhteen suuntaan.                                                                       |
| ![Sähköpiirrosmerkki: kylma magneettiventtiili](symbolit/kylma-magneettiventtiili.svg) | Magneettiventtiili                | Sähkömagneetilla käytettävä kylmäaineventtiili; merkki ei yksin kerro NC/NO-perustilaa.                  |
| ![Sähköpiirrosmerkki: kylma paisuntaventtiili](symbolit/kylma-paisuntaventtiili.svg)   | Termostaattinen paisuntaventtiili | Säätelee kylmäaineen syöttöä höyrystimeen lämpötila-anturin avulla. Sovellettu, tiivistetty perusesitys. |

### Paineen mittaus ja valvonta

| Symboli                                                                    | Nimi                    | Mitä merkki kertoo                                                                                     |
| -------------------------------------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------ |
| ![Sähköpiirrosmerkki: kylma painemittari](symbolit/kylma-painemittari.svg) | Painemittauspiste P     | Paineen mittauskohta; ei määritä mittarityyppiä tai mitta-aluetta.                                     |
| ![Sähköpiirrosmerkki: kylma psh](symbolit/kylma-psh.svg)                   | Korkeapainekytkin PSH   | Korkeapaineen kytkintoiminto; ei kerro laukaisuarvoa tai kuittaustapaa.                                |
| ![Sähköpiirrosmerkki: kylma psl](symbolit/kylma-psl.svg)                   | Matalapainekytkin PSL   | Matalapaineen kytkintoiminto; ei kerro laukaisuarvoa tai kuittaustapaa.                                |
| ![Sähköpiirrosmerkki: kylma pshl](symbolit/kylma-pshl.svg)                 | Kaksoispainekytkin PSHL | Yhdistää korkea- ja matalapaineen valvonnan. Kirjaston sovellettu yhdistelmä PSH- ja PSL-merkinnöistä. |

### Symbolien lähderajaus

Kirjaston 18 kylmäkierron merkistä **12 on lähdevertailtuja ja 6 sovellettuja**. Sovelletut merkit ovat:

- lauhdutin
- höyrystin
- nestesäiliö
- termostaattinen paisuntaventtiili
- kaksoispainekytkin PSHL
- öljynerotin

Sovellettujen symbolien tarkoitus on tehdä opiskelukaavioista johdonmukaisia. Niitä ei pidä tulkita väitteeksi siitä, että juuri kyseinen geometria olisi yleispätevä standardimerkki kaikissa kylmäkaavioissa. Laitetunnus, kaavion selite ja valmistajan dokumentaatio ratkaisevat tulkinnan.

Lähteet ja tarkemmat rajaukset on kirjattu symbolikirjaston `manifest.json`-tiedostoon. Pääasiallisina lähteinä sarjassa on käytetty GUNTin kylmätekniikan kaavioaineistoa sekä imuvaraajan osalta Danfossin ACC-aineistoa.

## Apu-, ohjaus- ja suojalaitteita

- **Nestesäiliö** lauhduttimen jälkeen varastoi nestemäistä kylmäainetta ja tasaa järjestelmän kylmäainemäärää.
- Nestelinjassa voi olla sulku- ja huoltoventtiilejä, kuivain/suodatin ja tarkastuslasi.
- Paisuntalaitteen anturi mittaa höyrystimen jälkeistä lämpötilaa ja ohjaa kylmäaineen syöttöä niin, että kylmäaine ehtii höyrystyä ennen kompressoria.
- **PSH** on korkeapaineen turvakytkin.
- **PSHL** valvoo korkea- ja matalapainetta. Painekytkimet pysäyttävät tai estävät kompressorin käynnin, jos paine joutuu sallitun alueen ulkopuolelle.

Kaavio on periaatekuva. Todellisen järjestelmän komponentit ja putkiston järjestys voivat olla toteutuksesta riippuen yksityiskohtaisemmat.

## ILP-asennus – oppitunnin muistiinpanot 8.9.2026

ILP = ilmalämpöpumppu. Alla on kuvan muistiinpanot jäsenneltyinä. Arvot ja ajat ovat oppitunnilla kirjattuja ohjearvoja, eivät yleispäteviä valmistajan raja-arvoja tai täydellinen asennusohje.

### Vakuumointi

- Kuvassa vakuumoinnin maksimipaineeksi on kirjattu **2,7 mbar = 0,0027 bar**.
- Kun kyseinen paine on saavutettu, vakuumointia jatketaan noin **30 minuuttia**.
- Muistiinpanoon kirjattu tarkoitus: **kosteuden poisto**.

### Tiiveyskoe ja liitosten tarkastus

Kuvan merkinnät:

- ”Tiiveyskoe \~5 min.”
- ”Poista vakuumimittari.”
- ”Testaa liitokset vuotovaahdolla.”

**Täsmennettävä työjärjestys:** kuvasta ei käy ilmi kokeen paine, hyväksymiskriteeri eikä se, missä vaiheessa järjestelmä paineistetaan liitosten vuotovaahtotarkastusta varten. Näitä ei ole päätelty kuvan lyhenteistä. Käytännön harjoittelussa vaiheet varmistetaan opettajalta ja laitteen asennusohjeesta.

### Koekäyttö ja viimeistely

- Koekäyttö **lämmityksellä ja jäähdytyksellä**.
- Irrota mittarisarja (**”huom. kylmäaine”**, kuten kuvassa).
- Tiivistä läpivienti.

Lähde: oppitunnin lähdeaineisto — käsinkirjoitetut ILP-asennuksen muistiinpanot.

## ILP:n yleisimmät viat – oppitunnin dia 8.9.2026

Dian ”Yleisimmät viat” luettelo kuvaa havaittavia oireita. Diassa ei anneta niiden syitä tai korjausohjeita.

- Sisäyksikön puhallinmoottori pitää meteliä tai resonoi.
- Laite puhaltaa, mutta ei jäähdytä eikä lämmitä.
- Laite lämmittää, mutta ei jäähdytä, tai päinvastoin.
- Sisäyksikkö vuotaa vettä.
- Sulake palaa tai vikavirtasuoja laukeaa.
- Kaukosäädin ei toimi.
- Ulkoyksikkö on jäässä.
- Sisäyksikkö on jäässä.

**Sanamuodon täsmennys:** dian ”polttaa sulakkeen / vikavirtasuojan” on kirjattu yllä muotoon ”sulake palaa tai vikavirtasuoja laukeaa”.

Lähde: oppitunnin lähdeaineisto — oppitunnin dia ”Yleisimmät viat”.

## Lähdekuva

- oppitunnin lähdeaineisto
- oppitunnin lähdeaineisto — tulistus ja alijäähdytys
- oppitunnin lähdeaineisto — korkea- ja matalapainepuoli
- oppitunnin lähdeaineisto — putket ja lämpötilojen mittauspisteet
- oppitunnin lähdeaineisto — tulistus-, alijäähdytys- ja mittausesimerkki

## Työsaliharjoitus 15.9.2026 — tyhjiöinti, täyttö ja talteenotto

Alla on opettajan paperin työjärjestys valvottua työsaliharjoitusta varten. Lukuarvot ovat tämän harjoituksen ohjearvoja; paperi ei yksin ole täydellinen työohje.

1. Mittaa varaajan paine.
2. Laske typpi ulos — paperin ilmaus: ”letkulla rättiä vasten”.
3. Tyhjiöi säiliö alle **2,7 mbar** lukemaan.
4. Täytä kylmäainetta, esimerkiksi **1 kg**.
5. Ota kylmäaine pois **talteenottopumpun avulla**.
6. Tyhjiöi säiliö alle **2,7 mbar**.
7. Täytä säiliöön typpeä **10 bar** paineeseen.

Paperissa ei nimetä käytettävää kylmäainetta eikä täsmennetä paineiden viitetasoa. Varmista nämä sekä kytkennät ja venttiilien käyttö opettajan kanssa harjoituksessa.

### Harjoituksen havaintokirjaus

| Kirjattava asia                          | Oma tulos |
| ---------------------------------------- | --------- |
| Käytetty kylmäaine                       |           |
| Varaajan alkupaine ja paineen viitetaso  |           |
| Ensimmäisen tyhjiöinnin loppupaine       |           |
| Täytetty kylmäainemassa                  |           |
| Talteen otettu kylmäainemassa            |           |
| Toisen tyhjiöinnin loppupaine            |           |
| Typen loppupaine ja paineen viitetaso    |           |
| Opettajan täsmennykset ja omat havainnot |           |

Lähde: oppitunnin lähdeaineisto, työsaliharjoituksen ohjepaperi, toimitettu 15.9.2026.
