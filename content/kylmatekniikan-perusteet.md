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

Korkea- ja matalapainepuolen raja kulkee kompressorin ja paisuntalaitteen kohdalla. Putken tehtävä tunnistetaan sen sijainnista kierrossa; väriin ei voi luottaa ilman kyseisen kaavion selitettä.

| Putki                        | Sijainti kierrossa                      | Kylmäaineen pääasiallinen tila   |
| ---------------------------- | --------------------------------------- | -------------------------------- |
| Kuumakaasuputki / paineputki | kompressori → lauhdutin                 | kuuma korkeapaineinen höyry      |
| Nesteputki                   | lauhdutin / nestesäiliö → paisuntalaite | korkeapaineinen neste            |
| Imuputki                     | höyrystin → kompressori                 | matalapaineinen tulistunut höyry |

## Lämpötilojen mittauspisteet

Seuraavat mittauspisteet ovat tämän esimerkin tunnuksia, eivät kaikissa laitteissa käytettäviä vakiotunnuksia:

- **T1:** imuputken lämpötila höyrystimen jälkeen; käytetään tulistuksen laskemiseen.
- **T2:** nesteputken lämpötila ennen paisuntalaitetta; käytetään alijäähdytyksen laskemiseen.
- **T3:** kuumakaasuputken lämpötila kompressorin jälkeen.

## Tulistus ja alijäähdytys

### Tulistus, SH

`SH = imuputken mitattu lämpötila − imupainetta vastaava kyllästymislämpötila`

Tulistuksella varmistetaan, että kompressorille palaava kylmäaine on kokonaan kaasua. Tämä suojaa kompressoria nestemäiseltä kylmäaineelta ja nesteiskuilta.

**Suuntaa-antava muistisääntö:** imupainetta vastaava kyllästymis- eli höyrystymislämpötila voi olla **5–15 K kylmälaitteen tavoitelämpötilaa alempi**. Tämä ei ole laitteen asetusarvo; oikea tavoite riippuu laitteesta, kylmäaineesta ja valmistajan ohjeista.

### Alijäähdytys, SC

`SC = korkeapainetta vastaava kyllästymislämpötila − nesteputken mitattu lämpötila`

Alijäähdytyksellä varmistetaan, että paisuntalaitteelle tuleva kylmäaine on nestettä eikä nesteputkessa ole ennenaikaisesti syntynyttä höyryä eli flash-kaasua.

### Tulistuksen ja alijäähdytyksen laskuesimerkki

Lähtötietoina ovat saman esimerkkitilanteen paineet, putkilämpötilat ja niistä käytetyn kylmäaineen paine–lämpötila-tiedolla saadut kyllästymislämpötilat. Kylmäainetta ja paineiden viitetasoa ei alkuperäisessä harjoituksessa ilmoitettu, joten näitä lukemia ei voi käyttää toisen laitteen tavoitearvoina.

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

Harjoitusmuistiinpanoissa tulistuksen suuntaa-antavaksi alueeksi on merkitty **6–10 K** ja alijäähdytyksen alueeksi **2–4 K**. Tulistuksesta esiintyy myös laajempi **6–15 K** alue. Oikea tavoite määräytyy laitteen, kylmäaineen, paisuntalaitteen ja valmistajan ohjeiden mukaan.

Kyllästymislämpötila luetaan aina käytetyn kylmäaineen paine–lämpötila-taulukosta tai mittarista. Laskussa pitää huomioida myös, ilmoitetaanko paine yli- vai absoluuttisena paineena. Jos kylmäaineella on lämpötilaliukuma, tulistuksessa käytetään kastepistelämpötilaa ja alijäähdytyksessä kuplapistelämpötilaa.

## Entalpia

Kylmätekniikassa käytetään tavallisesti **ominaista entalpiaa** `h`, jonka yksikkö on `kJ/kg`. Se kuvaa kylmäaineen energiasisältöä massayksikköä kohti valittuun vertailutasoon nähden. Kylmäprosessin lämmönsiirtoa ja kompressorityötä tarkastellaan entalpiaerojen avulla.

## Kylmäkaavion visuaalinen symbolisanasto

Alla oleva sarja on kylmäkierron kaavioiden lukemiseen tehty SVG-kirjasto. Symbolit ovat samassa 64 × 64 -järjestelmässä kuin sähköpiirustusten symbolit. **Lähdevertailtu** tarkoittaa, että merkki on piirretty nimetyn lähteen perusteella. **Sovellettu** tarkoittaa, että merkki on koottu tai yksinkertaistettu lähteistetystä perusmerkistä tiettyyn kylmäalan käyttötarkoitukseen.

### Peruskylmäkierto

Peruskylmäkierron neljä pääkomponenttia voidaan lukea järjestyksessä:

**kompressori → lauhdutin → paisuntalaite → höyrystin → kompressori**

| Symboli                                                                         | Nimi                                       | Tehtävä                                                                    |
| ------------------------------------------------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------------- |
| ![Piirrosmerkki: kylma kompressori](symbolit/kylma-kompressori.svg)             | Kompressori                                | Nostaa kylmäainehöyryn painetta ja ylläpitää kiertoa.                      |
| ![Piirrosmerkki: kylma lauhdutin](symbolit/kylma-lauhdutin.svg)                 | Lauhdutin                                  | Luovuttaa lämpöä ja lauhduttaa kylmäainetta.                               |
| ![Piirrosmerkki: kylma paisuntaventtiili](symbolit/kylma-paisuntaventtiili.svg) | Termostaattinen paisuntaventtiili, TEV/TXV | Säätelee kylmäaineen syöttöä höyrystimeen ja aiheuttaa paineen alenemisen. |
| ![Piirrosmerkki: kylma hoyrystin](symbolit/kylma-hoyrystin.svg)                 | Höyrystin                                  | Ottaa lämpöä jäähdytettävästä kohteesta kylmäaineen höyrystyessä.          |

![Piirrosmerkki: kylma putki](symbolit/kylma-putki.svg)

**Kylmäaineputken viiva ei yksin kerro, onko kyse imu-, neste- vai kuumakaasuputkesta.** Putken tehtävä päätellään sijainnista kierrossa ja kaavion selitteestä.

### Säiliöt, erotus ja nestelinja

| Symboli                                                             | Nimi                            | Tehtävä / rajaus                                                                              |
| ------------------------------------------------------------------- | ------------------------------- | --------------------------------------------------------------------------------------------- |
| ![Piirrosmerkki: kylma nestesailio](symbolit/kylma-nestesailio.svg) | Nestesäiliö                     | Varastoi nestemäistä kylmäainetta korkeapainepuolella. Sovellettu painesäiliön perusmerkistä. |
| ![Piirrosmerkki: kylma imuvaraaja](symbolit/kylma-imuvaraaja.svg)   | Imuvaraaja / nesteenerotin      | Erottaa nestemäistä kylmäainetta imukaasusta ennen kompressoria.                              |
| ![Piirrosmerkki: kylma oljynerotin](symbolit/kylma-oljynerotin.svg) | Öljynerotin                     | Erottaa öljyä kompressorin painepuolen kylmäainehöyrystä. Sovellettu erottimen yleismerkistä. |
| ![Piirrosmerkki: kylma kuivain](symbolit/kylma-kuivain.svg)         | Suodatinkuivain                 | Poistaa kylmäaineesta kosteutta ja epäpuhtauksia.                                             |
| ![Piirrosmerkki: kylma nakolasi](symbolit/kylma-nakolasi.svg)       | Näkölasi kosteusindikaattorilla | Mahdollistaa kylmäaineen tilan tarkastelun; indikaattori tulkitaan valmistajan ohjeesta.      |

Tyypillisessä nestelinjassa voidaan nähdä esimerkiksi **nestesäiliö → suodatinkuivain → näkölasi → paisuntaventtiili**, mutta todellinen komponenttijärjestys tarkistetaan aina kyseisen järjestelmän kaaviosta.

### Venttiilit

| Symboli                                                                           | Nimi                              | Tehtävä / rajaus                                                                                         |
| --------------------------------------------------------------------------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------- |
| ![Piirrosmerkki: kylma sulkuventtiili](symbolit/kylma-sulkuventtiili.svg)         | Sulkuventtiili, yleismerkki       | Katkaisee virtausreitin; ei ilmaise venttiilin rakennetyyppiä tai asentoa.                               |
| ![Piirrosmerkki: kylma palloventtiili](symbolit/kylma-palloventtiili.svg)         | Palloventtiili                    | Pallorakenteinen sulkuventtiili.                                                                         |
| ![Piirrosmerkki: kylma takaiskuventtiili](symbolit/kylma-takaiskuventtiili.svg)   | Takaiskuventtiili                 | Sallii virtauksen yhteen suuntaan.                                                                       |
| ![Piirrosmerkki: kylma magneettiventtiili](symbolit/kylma-magneettiventtiili.svg) | Magneettiventtiili                | Sähkömagneetilla käytettävä kylmäaineventtiili; merkki ei yksin kerro NC/NO-perustilaa.                  |
| ![Piirrosmerkki: kylma paisuntaventtiili](symbolit/kylma-paisuntaventtiili.svg)   | Termostaattinen paisuntaventtiili | Säätelee kylmäaineen syöttöä höyrystimeen lämpötila-anturin avulla. Sovellettu, tiivistetty perusesitys. |

### Paineen mittaus ja valvonta

| Symboli                                                               | Nimi                    | Mitä merkki kertoo                                                                                     |
| --------------------------------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------ |
| ![Piirrosmerkki: kylma painemittari](symbolit/kylma-painemittari.svg) | Painemittauspiste P     | Paineen mittauskohta; ei määritä mittarityyppiä tai mitta-aluetta.                                     |
| ![Piirrosmerkki: kylma psh](symbolit/kylma-psh.svg)                   | Korkeapainekytkin PSH   | Korkeapaineen kytkintoiminto; ei kerro laukaisuarvoa tai kuittaustapaa.                                |
| ![Piirrosmerkki: kylma psl](symbolit/kylma-psl.svg)                   | Matalapainekytkin PSL   | Matalapaineen kytkintoiminto; ei kerro laukaisuarvoa tai kuittaustapaa.                                |
| ![Piirrosmerkki: kylma pshl](symbolit/kylma-pshl.svg)                 | Kaksoispainekytkin PSHL | Yhdistää korkea- ja matalapaineen valvonnan. Kirjaston sovellettu yhdistelmä PSH- ja PSL-merkinnöistä. |

### Symbolien lähderajaus

Kirjaston 18 kylmäkierron merkistä **12 on lähdevertailtuja ja 6 sovellettuja**. Sovelletut merkit ovat:

- lauhdutin
- höyrystin
- nestesäiliö
- termostaattinen paisuntaventtiili
- kaksoispainekytkin PSHL
- öljynerotin

Sovellettujen symbolien tarkoitus on tehdä opiskelukaavioista johdonmukaisia. Niitä ei pidä tulkita väitteeksi siitä, että juuri kyseinen geometria olisi yleispätevä standardimerkki kaikissa kylmäkaavioissa. Laitetunnus, kaavion selite ja valmistajan dokumentaatio ratkaisevat tulkinnan.

## Apu-, ohjaus- ja suojalaitteita

- **Nestesäiliö** lauhduttimen jälkeen varastoi nestemäistä kylmäainetta ja tasaa järjestelmän kylmäainemäärää.
- Nestelinjassa voi olla sulku- ja huoltoventtiilejä, kuivain/suodatin ja tarkastuslasi.
- Paisuntalaitteen anturi mittaa höyrystimen jälkeistä lämpötilaa ja ohjaa kylmäaineen syöttöä niin, että kylmäaine ehtii höyrystyä ennen kompressoria.
- **PSH** on korkeapaineen turvakytkin.
- **PSHL** valvoo korkea- ja matalapainetta. Painekytkimet pysäyttävät tai estävät kompressorin käynnin, jos paine joutuu sallitun alueen ulkopuolelle.

Edellä kuvattu peruskierto on pelkistetty malli. Todellisen järjestelmän komponentit ja putkiston järjestys voivat olla toteutuksesta riippuen yksityiskohtaisemmat.

## ILP-asennus – oppitunnin muistiinpanot 8.9.2026

ILP = ilmalämpöpumppu. Seuraavat arvot ja ajat ovat yhden opetustilanteen ohjearvoja, eivät yleispäteviä valmistajan raja-arvoja tai täydellinen asennusohje. Todellisen asennuksen menetelmät ja hyväksymisrajat määräytyvät laitteen ohjeiden ja soveltuvien vaatimusten mukaan.

### Vakuumointi

- Harjoituksessa vakuumoinnin tavoitelukemaksi kirjattiin **2,7 mbar = 0,0027 bar**; paineen viitetasoa ei merkitty muistiin.
- Kun kyseinen paine on saavutettu, vakuumointia jatketaan noin **30 minuuttia**.
- Muistiinpanoon kirjattu tarkoitus: **kosteuden poisto**.

### Tiiveyskoe ja liitosten tarkastus

Harjoituksen vaiheet:

- ”Tiiveyskoe \~5 min.”
- ”Poista vakuumimittari.”
- ”Testaa liitokset vuotovaahdolla.”

**Harjoituksen rajaus:** tiedoissa ei määritellä kokeen painetta, hyväksymiskriteeriä eikä sitä, missä vaiheessa järjestelmä paineistetaan liitosten vuotovaahtotarkastusta varten. Näiden puuttuessa luetteloa ei voi käyttää työjärjestyksenä. Käytännön harjoittelussa vaiheet varmistetaan opettajalta ja laitteen asennusohjeesta.

### Koekäyttö ja viimeistely

- Koekäyttö **lämmityksellä ja jäähdytyksellä**.
- Irrota mittarisarja (**”huom. kylmäaine”**).
- Tiivistä läpivienti.

## ILP:n mahdollisia vikaoireita

Seuraava luettelo kuvaa havaittavia oireita. Oire yksin ei osoita vian syytä eikä kerro korjaustapaa.

- Sisäyksikön puhallinmoottori pitää meteliä tai resonoi.
- Laite puhaltaa, mutta ei jäähdytä eikä lämmitä.
- Laite lämmittää, mutta ei jäähdytä, tai päinvastoin.
- Sisäyksikkö vuotaa vettä.
- Sulake palaa tai vikavirtasuoja laukeaa.
- Kaukosäädin ei toimi.
- Ulkoyksikkö on jäässä.
- Sisäyksikkö on jäässä.

## Työsaliharjoitus 15.9.2026 — tyhjiöinti, täyttö ja talteenotto

Seuraava järjestys ja lukuarvot on kirjattu valvottua työsaliharjoitusta varten. Ne kuvaavat kyseistä harjoitusta; lähtötiedot eivät riitä itsenäiseksi työohjeeksi.

1. Mittaa varaajan paine.
2. Typpitäytös poistetaan harjoituksessa opettajan valvonnassa. Alkuperäinen merkintä ei määritä turvallista purkumenetelmää.
3. Tyhjiöi säiliö alle **2,7 mbar** lukemaan.
4. Täytä kylmäainetta, esimerkiksi **1 kg**.
5. Ota kylmäaine pois **talteenottopumpun avulla**.
6. Tyhjiöi säiliö alle **2,7 mbar**.
7. Täytä säiliöön typpeä **10 bar** paineeseen.

Harjoitustiedoissa ei nimetä käytettävää kylmäainetta eikä täsmennetä paineiden viitetasoa. Myös kytkennät ja venttiilien käyttö jäävät valvotun opetuksen ja laiteohjeiden varaan.

## Lähteet ja alkuperäismateriaali

Pääasiallisina lähteinä ovat GUNTin kylmätekniikan kaavioaineisto ja imuvaraajan osalta Danfossin ACC-aineisto.
