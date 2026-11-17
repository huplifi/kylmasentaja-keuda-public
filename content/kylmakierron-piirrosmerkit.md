---
title: "Kylmäkierron piirrosmerkit"
publish: true
---

Kylmäkaavion viivat kuvaavat putkia ja piirrosmerkit niihin liittyviä laitteita. Kun luet kaaviota, etsi ensin kompressori. Seuraa sen lähtöputkea kylmäaineen virtaussuuntaan. Alla olevista taulukoista näet, mitä kylmäaineelle tapahtuu kussakin laitteessa.

**Lähdevertailtu** tarkoittaa, että merkki on piirretty nimetyn lähteen perusteella. **Sovellettu** tarkoittaa, että merkki on koottu tai yksinkertaistettu lähteistetystä perusmerkistä tiettyyn kylmäalan käyttötarkoitukseen.

## Peruskylmäkierto

Peruskylmäkierron neljä pääkomponenttia luetaan järjestyksessä:

**kompressori → lauhdutin → paisuntalaite → höyrystin → kompressori**

| Symboli                                                                         | Nimi                                       | Tehtävä                                                                    |
| ------------------------------------------------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------------- |
| ![Piirrosmerkki: kylma kompressori](symbolit/kylma-kompressori.svg)             | Kompressori                                | Nostaa kylmäainehöyryn painetta ja ylläpitää kiertoa.                      |
| ![Piirrosmerkki: kylma lauhdutin](symbolit/kylma-lauhdutin.svg)                 | Lauhdutin                                  | Luovuttaa lämpöä ja lauhduttaa kylmäainetta.                               |
| ![Piirrosmerkki: kylma paisuntaventtiili](symbolit/kylma-paisuntaventtiili.svg) | Termostaattinen paisuntaventtiili, TEV/TXV | Säätelee kylmäaineen syöttöä höyrystimeen ja aiheuttaa paineen alenemisen. |
| ![Piirrosmerkki: kylma hoyrystin](symbolit/kylma-hoyrystin.svg)                 | Höyrystin                                  | Ottaa lämpöä jäähdytettävästä kohteesta kylmäaineen höyrystyessä.          |

### Kylmäaineputki

![Piirrosmerkki: kylma putki](symbolit/kylma-putki.svg)

Tunnista putki sen perusteella, mistä se tulee ja mihin se vie. Kompressorilta lauhduttimeen virtaa kuumaa, korkeapaineista kylmäainehöyryä **kuumakaasuputkessa**. Lauhduttimelta kohti paisuntaventtiiliä kulkee nestemäistä kylmäainetta **nestelinjassa**. Höyrystimeltä takaisin kompressorille palaa matalapaineista höyryä eli imukaasua **imuputkessa**.

## Säiliöt, erotus ja nestelinja

| Symboli                                                             | Nimi                            | Tehtävä / rajaus                                                                              |
| ------------------------------------------------------------------- | ------------------------------- | --------------------------------------------------------------------------------------------- |
| ![Piirrosmerkki: kylma nestesailio](symbolit/kylma-nestesailio.svg) | Nestesäiliö                     | Varastoi nestemäistä kylmäainetta korkeapainepuolella. Sovellettu painesäiliön perusmerkistä. |
| ![Piirrosmerkki: kylma imuvaraaja](symbolit/kylma-imuvaraaja.svg)   | Imuvaraaja / nesteenerotin      | Erottaa nestemäistä kylmäainetta imukaasusta ennen kompressoria.                              |
| ![Piirrosmerkki: kylma oljynerotin](symbolit/kylma-oljynerotin.svg) | Öljynerotin                     | Erottaa öljyä kompressorin painepuolen kylmäainehöyrystä. Sovellettu erottimen yleismerkistä. |
| ![Piirrosmerkki: kylma kuivain](symbolit/kylma-kuivain.svg)         | Suodatinkuivain                 | Poistaa kylmäaineesta kosteutta ja epäpuhtauksia.                                             |
| ![Piirrosmerkki: kylma nakolasi](symbolit/kylma-nakolasi.svg)       | Näkölasi kosteusindikaattorilla | Näyttää kylmäaineen tilaa; indikaattori tulkitaan valmistajan ohjeesta.                       |

Tyypillisessä nestelinjassa voidaan nähdä esimerkiksi **nestesäiliö → suodatinkuivain → näkölasi → paisuntaventtiili**, mutta todellinen komponenttijärjestys tarkistetaan aina kyseisen järjestelmän kaaviosta.

## Venttiilit

| Symboli                                                                           | Nimi                              | Tehtävä / rajaus                                                                                                                                |
| --------------------------------------------------------------------------------- | --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Piirrosmerkki: kylma sulkuventtiili](symbolit/kylma-sulkuventtiili.svg)         | Sulkuventtiili, yleismerkki       | Katkaisee virtausreitin; ei ilmaise venttiilin rakennetyyppiä tai asentoa.                                                                      |
| ![Piirrosmerkki: kylma palloventtiili](symbolit/kylma-palloventtiili.svg)         | Palloventtiili                    | Pallorakenteinen sulkuventtiili.                                                                                                                |
| ![Piirrosmerkki: kylma takaiskuventtiili](symbolit/kylma-takaiskuventtiili.svg)   | Takaiskuventtiili                 | Sallii virtauksen yhteen suuntaan.                                                                                                              |
| ![Piirrosmerkki: kylma magneettiventtiili](symbolit/kylma-magneettiventtiili.svg) | Magneettiventtiili                | Sähkömagneetti ohjaa venttiiliä. Kun kela on jännitteetön, NC-venttiili on kiinni ja NO-venttiili auki. Perustila selviää laitteen merkinnästä. |
| ![Piirrosmerkki: kylma paisuntaventtiili](symbolit/kylma-paisuntaventtiili.svg)   | Termostaattinen paisuntaventtiili | Säätelee kylmäaineen syöttöä höyrystimeen lämpötila-anturin avulla. Sovellettu, tiivistetty perusesitys.                                        |

## Paineen mittaus ja valvonta

Mittauspiste kertoo, mistä paine voidaan mitata. Painekytkin puolestaan vaihtaa sähkökoskettimen tilaa, kun paine saavuttaa sille asetetun rajan. Esimerkiksi matalapainekytkin voi pysäyttää kompressorin imupaineen laskiessa.

| Symboli                                                               | Nimi                    | Mitä merkki kertoo                                                                                     |
| --------------------------------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------ |
| ![Piirrosmerkki: kylma painemittari](symbolit/kylma-painemittari.svg) | Painemittauspiste P     | Paineen mittauskohta; ei määritä mittarityyppiä tai mitta-aluetta.                                     |
| ![Piirrosmerkki: kylma psh](symbolit/kylma-psh.svg)                   | Korkeapainekytkin PSH   | Korkeapaineen kytkintoiminto; ei kerro laukaisuarvoa tai kuittaustapaa.                                |
| ![Piirrosmerkki: kylma psl](symbolit/kylma-psl.svg)                   | Matalapainekytkin PSL   | Matalapaineen kytkintoiminto; ei kerro laukaisuarvoa tai kuittaustapaa.                                |
| ![Piirrosmerkki: kylma pshl](symbolit/kylma-pshl.svg)                 | Kaksoispainekytkin PSHL | Yhdistää korkea- ja matalapaineen valvonnan. Kirjaston sovellettu yhdistelmä PSH- ja PSL-merkinnöistä. |

## Lähderajaus

Kirjaston 18 kylmäkierron merkistä **12 on lähdevertailtuja ja 6 sovellettuja**. Sovelletut merkit ovat:

- lauhdutin
- höyrystin
- nestesäiliö
- termostaattinen paisuntaventtiili
- kaksoispainekytkin PSHL
- öljynerotin

Sovellettujen symbolien tarkoitus on tehdä opiskelukaavioista johdonmukaisia. Niitä ei pidä tulkita väitteeksi siitä, että juuri kyseinen geometria olisi yleispätevä standardimerkki kaikissa kylmäkaavioissa. Laitetunnus, kaavion selite ja valmistajan dokumentaatio ratkaisevat tulkinnan.

Pääasiallisina lähteinä sarjassa on käytetty GUNTin kylmätekniikan kaavioaineistoa sekä imuvaraajan osalta Danfossin ACC-aineistoa.

Katso myös [Kylmätekniikan perusteet](kylmatekniikan-perusteet.md).
