---
title: "Kylmäkierron piirrosmerkit"
publish: true
---

Visuaalinen sanasto kylmäkaavioiden lukemiseen ja piirtämiseen. Symbolit käyttävät samaa 64 × 64 -järjestelmää kuin sähköpiirustusten symbolikirjasto.

**Lähdevertailtu** tarkoittaa, että merkki on piirretty nimetyn lähteen perusteella. **Sovellettu** tarkoittaa, että merkki on koottu tai yksinkertaistettu lähteistetystä perusmerkistä tiettyyn kylmäalan käyttötarkoitukseen.

## Peruskylmäkierto

Peruskylmäkierron neljä pääkomponenttia luetaan järjestyksessä:

**kompressori → lauhdutin → paisuntalaite → höyrystin → kompressori**

| Symboli                                                                              | Nimi                                       | Tehtävä                                                                    |
| ------------------------------------------------------------------------------------ | ------------------------------------------ | -------------------------------------------------------------------------- |
| ![Sähköpiirrosmerkki: kylma kompressori](symbolit/kylma-kompressori.svg)             | Kompressori                                | Nostaa kylmäainehöyryn painetta ja ylläpitää kiertoa.                      |
| ![Sähköpiirrosmerkki: kylma lauhdutin](symbolit/kylma-lauhdutin.svg)                 | Lauhdutin                                  | Luovuttaa lämpöä ja lauhduttaa kylmäainetta.                               |
| ![Sähköpiirrosmerkki: kylma paisuntaventtiili](symbolit/kylma-paisuntaventtiili.svg) | Termostaattinen paisuntaventtiili, TEV/TXV | Säätelee kylmäaineen syöttöä höyrystimeen ja aiheuttaa paineen alenemisen. |
| ![Sähköpiirrosmerkki: kylma hoyrystin](symbolit/kylma-hoyrystin.svg)                 | Höyrystin                                  | Ottaa lämpöä jäähdytettävästä kohteesta kylmäaineen höyrystyessä.          |

### Kylmäaineputki

![Sähköpiirrosmerkki: kylma putki](symbolit/kylma-putki.svg)

Putkiviiva ei yksin kerro, onko kyse imu-, neste- vai kuumakaasuputkesta. Putken tehtävä päätellään sijainnista kierrossa ja kaavion selitteestä.

## Säiliöt, erotus ja nestelinja

| Symboli                                                                  | Nimi                            | Tehtävä / rajaus                                                                              |
| ------------------------------------------------------------------------ | ------------------------------- | --------------------------------------------------------------------------------------------- |
| ![Sähköpiirrosmerkki: kylma nestesailio](symbolit/kylma-nestesailio.svg) | Nestesäiliö                     | Varastoi nestemäistä kylmäainetta korkeapainepuolella. Sovellettu painesäiliön perusmerkistä. |
| ![Sähköpiirrosmerkki: kylma imuvaraaja](symbolit/kylma-imuvaraaja.svg)   | Imuvaraaja / nesteenerotin      | Erottaa nestemäistä kylmäainetta imukaasusta ennen kompressoria.                              |
| ![Sähköpiirrosmerkki: kylma oljynerotin](symbolit/kylma-oljynerotin.svg) | Öljynerotin                     | Erottaa öljyä kompressorin painepuolen kylmäainehöyrystä. Sovellettu erottimen yleismerkistä. |
| ![Sähköpiirrosmerkki: kylma kuivain](symbolit/kylma-kuivain.svg)         | Suodatinkuivain                 | Poistaa kylmäaineesta kosteutta ja epäpuhtauksia.                                             |
| ![Sähköpiirrosmerkki: kylma nakolasi](symbolit/kylma-nakolasi.svg)       | Näkölasi kosteusindikaattorilla | Näyttää kylmäaineen tilaa; indikaattori tulkitaan valmistajan ohjeesta.                       |

Tyypillisessä nestelinjassa voidaan nähdä esimerkiksi **nestesäiliö → suodatinkuivain → näkölasi → paisuntaventtiili**, mutta todellinen komponenttijärjestys tarkistetaan aina kyseisen järjestelmän kaaviosta.

## Venttiilit

| Symboli                                                                                | Nimi                              | Tehtävä / rajaus                                                                                         |
| -------------------------------------------------------------------------------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------- |
| ![Sähköpiirrosmerkki: kylma sulkuventtiili](symbolit/kylma-sulkuventtiili.svg)         | Sulkuventtiili, yleismerkki       | Katkaisee virtausreitin; ei ilmaise venttiilin rakennetyyppiä tai asentoa.                               |
| ![Sähköpiirrosmerkki: kylma palloventtiili](symbolit/kylma-palloventtiili.svg)         | Palloventtiili                    | Pallorakenteinen sulkuventtiili.                                                                         |
| ![Sähköpiirrosmerkki: kylma takaiskuventtiili](symbolit/kylma-takaiskuventtiili.svg)   | Takaiskuventtiili                 | Sallii virtauksen yhteen suuntaan.                                                                       |
| ![Sähköpiirrosmerkki: kylma magneettiventtiili](symbolit/kylma-magneettiventtiili.svg) | Magneettiventtiili                | Sähkömagneetilla käytettävä kylmäaineventtiili; merkki ei yksin kerro NC/NO-perustilaa.                  |
| ![Sähköpiirrosmerkki: kylma paisuntaventtiili](symbolit/kylma-paisuntaventtiili.svg)   | Termostaattinen paisuntaventtiili | Säätelee kylmäaineen syöttöä höyrystimeen lämpötila-anturin avulla. Sovellettu, tiivistetty perusesitys. |

## Paineen mittaus ja valvonta

| Symboli                                                                    | Nimi                    | Mitä merkki kertoo                                                                                     |
| -------------------------------------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------ |
| ![Sähköpiirrosmerkki: kylma painemittari](symbolit/kylma-painemittari.svg) | Painemittauspiste P     | Paineen mittauskohta; ei määritä mittarityyppiä tai mitta-aluetta.                                     |
| ![Sähköpiirrosmerkki: kylma psh](symbolit/kylma-psh.svg)                   | Korkeapainekytkin PSH   | Korkeapaineen kytkintoiminto; ei kerro laukaisuarvoa tai kuittaustapaa.                                |
| ![Sähköpiirrosmerkki: kylma psl](symbolit/kylma-psl.svg)                   | Matalapainekytkin PSL   | Matalapaineen kytkintoiminto; ei kerro laukaisuarvoa tai kuittaustapaa.                                |
| ![Sähköpiirrosmerkki: kylma pshl](symbolit/kylma-pshl.svg)                 | Kaksoispainekytkin PSHL | Yhdistää korkea- ja matalapaineen valvonnan. Kirjaston sovellettu yhdistelmä PSH- ja PSL-merkinnöistä. |

## Lähderajaus

Kirjaston 18 kylmäkierron merkistä **12 on lähdevertailtuja ja 6 sovellettuja**. Sovelletut merkit ovat:

- lauhdutin
- höyrystin
- nestesäiliö
- termostaattinen paisuntaventtiili
- kaksoispainekytkin PSHL
- öljynerotin

Sovellettujen symbolien tarkoitus on tehdä opiskelukaavioista johdonmukaisia. Niitä ei pidä tulkita väitteeksi siitä, että juuri kyseinen geometria olisi yleispätevä standardimerkki kaikissa kylmäkaavioissa. Laitetunnus, kaavion selite ja valmistajan dokumentaatio ratkaisevat tulkinnan.

Lähteet ja tarkemmat rajaukset on kirjattu yksityisen lähderepon symbolikirjaston manifestiin. Pääasiallisina lähteinä sarjassa on käytetty GUNTin kylmätekniikan kaavioaineistoa sekä imuvaraajan osalta Danfossin ACC-aineistoa.

Katso myös [Kylmätekniikan perusteet](kylmatekniikan-perusteet.md).
