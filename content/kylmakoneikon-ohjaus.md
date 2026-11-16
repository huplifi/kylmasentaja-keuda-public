---
title: "Kylmäkoneikon ohjaus"
publish: true
---

Seuraa ensin yhden kylmiön pysäytystä. Kahden kompressorin esimerkissä voit sitten seurata, miten imupaineen muutos johtaa toisen kompressorin käynnistymiseen. [Releen, kontaktorin ja aikareleiden perusteet](releet-ja-kontaktorit.md)

## Kylmiön pump-down-ohjaus

Harjoituksessa on yksi kylmiö, nestelinjan jännitteettömänä sulkeutuva magneettiventtiili Y1 ja suorakäynnisteinen kompressori M1. Kylmiön lämmetessä termostaatti avaa venttiilin. Kompressori käynnistyy imupaineen noustessa. Kun lämpötila on saavutettu, venttiili sulkeutuu ensin ja kompressori käy vielä hetken. Tätä kutsutaan pump-down-ohjaukseksi. Tunnukset ja 24 V DC ovat tämän harjoituksen valintoja.

Piirrä ensin M1 ja Y1, sitten niiden virtalähteet. Moottorilähtö ja ohjausvirtalähde saavat sähkön pääkytkimen Q0 jälkeisestä jakelusta. Moottorin kontaktori KM1 on vain moottorihaarassa, jotta termostaatti voi avata venttiilin myös moottorin seistessä.

| Seurattava reitti         | Osat lukujärjestyksessä                                                                                                                                                                                                                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Moottorin pääpiiri        | L1, L2, L3 → Q0 → moottorilähdön oikosulkusuoja → KM1:n kolme pääkosketinta → ylikuormitusreleen F2 kolme virtaelementtiä → M1:n käämit. Käyttövirran reitti sulkeutuu vaiheiden välillä. PE yhdistää moottorin rungon suojamaahan.                                                              |
| Ohjausjännitteen lähde    | Q0:n jälkeinen jakelu → virtalähteen syötön suoja → virtalähde PS1 → +24 V ja 0 V.                                                                                                                                                                                                               |
| Molemmille yhteiset ehdot | +24 V → ohjauspiirin suoja → käyttökytkin S1 → korkeapainekatkaisimen HP kosketin → F2:n avautuva apukosketin 95–96 → uudelleenkäynnistyksen salliva viivekosketin → haaroitus. Viivetoiminto seuraa kompressorin pysähtymistä ja sallii seuraavan käynnistyksen vähimmäisseisonta-ajan jälkeen. |
| Venttiilin ohjaushaara    | Haaroitus → kylmää pyytävän termostaatin kosketin → Y1:n kela → 0 V.                                                                                                                                                                                                                             |
| Kompressorin ohjaushaara  | Haaroitus → pump-down-matalapainekytkimen LP kosketin → KM1:n kela A1–A2 → 0 V.                                                                                                                                                                                                                  |

Yhteiset ehdot ovat sarjassa, joten jokaisen täytyy sallia käynti. Venttiilin ja kontaktorin kelat ovat omissa rinnakkaishaaroissaan. Termostaatin avautuminen katkaisee vain venttiilin kelavirran. HP:n tai ylikuormitussuojan laukeaminen katkaisee molempien haarojen syötön. KM1:n kelan ja pääkoskettimien välillä on mekaaninen yhteys. F2 puolestaan seuraa pääpiirin moottorivirtaa ja voi avata koskettimen 95–96 ohjauspiirissä.

**Seuraa yhtä pysäytystä.** Kun termostaatti saavuttaa katkaisulämpötilan, Y1 sulkeutuu. LP:n kosketin on vielä kiinni ja KM1 pitää moottorin käynnissä. Kompressori imee höyryä höyrystimestä, imupaine laskee ja LP avaa koskettimensa pysäytysrajalla. KM1 päästää ja sen pääkoskettimet avaavat kaikki kolme vaihetta. Seuraavalla jäähdytyspyynnöllä Y1 avautuu, ja LP sulkee koskettimensa vasta imupaineen noustua käynnistysrajalle. Automaattisessa pump-downissa myös paineen nousu seisokin aikana voi aiheuttaa uuden pumppauksen viiveen jälkeen.

Haarat kuvaavat kompressorin ja nesteventtiilin ohjausta. Oikean koneen puhaltimilla, sulatuksella ja mahdollisella öljynvalvonnalla on omat laitekohtaiset piirinsä. Valmistajan piiristä selviävät myös todelliset liittimet, jännitteet ja suojaukset.

## Kahden kompressorin koneikko

Kuvittele, että usean kylmäkalusteen höyrystimet palauttavat kylmäainehöyryn yhteiseen imuputkeen. Ensimmäinen kompressori on nopeussäädetty ja toinen käy vakionopeudella. Kun höyryä tulee imuputkeen enemmän kuin käynnissä oleva kompressori ehtii imeä, imupaine (LP) nousee.

1. **Mittaus ja säätö.** Paineanturi ilmoittaa imupaineen koneikkosäätimelle. Säädin pyytää ensimmäisen kompressorin taajuusmuuttajaa lisäämään moottorin nopeutta. Kompressori imee enemmän höyryä.
2. **Toinen kompressori avuksi.** Jos ensimmäisen teho ei riitä ja imupaine pysyy tavoitealueen yläpuolella, säädin pyytää toisen kompressorin käyntiin. Käynnistys edellyttää, että suojaukset sallivat sen ja vähimmäisseisonta-aika on kulunut.
3. **Ohjauspiiri.** Tässä esimerkissä säädin ohjaa välirelettä K1 ja K1 moottorikontaktoria KM2. Kun K1 vetää, yhteys 11–12 avautuu ja 11–14 sulkeutuu. Jos käyntiehdot täyttyvät, virta pääsee kulkemaan KM2:n kelan läpi. K1:n toinen kosketin 21–24 voi samalla sytyttää käyntipyyntöä osoittavan merkkivalon. Katkoviiva piirrosmerkissä kertoo, että molemmat koskettimet liikkuvat yhdessä.
4. **Päävirtapiiri.** KM2:n ankkuri liikuttaa kosketinsiltoja, ja kolme pääkosketinta sulkeutuu. Kukin johtaa yhden vaiheen virran kompressorin moottorille. K1:n pieni kosketin kantaa vain KM2:n kelavirran. Nopeussäädetty ensimmäinen moottori saa tehonsa taajuusmuuttajan kautta.
5. **Pysäytys.** Kun toista kompressoria ei enää tarvita, säädin poistaa käyntipyynnön. K1:n jousi palauttaa vaihtokoskettimen lepoasentoon 11–12. Yhteys 11–14 aukeaa, KM2:n kela jää virrattomaksi ja kontaktorin jousi avaa pääkoskettimet. Moottorin sähkönsyöttö katkeaa. Lauennut moottorisuoja voi estää käynnin myös silloin, kun jäähdytyspyyntö on edelleen voimassa.

### Seuraa toisen kompressorin virtareittejä

Tässä suorakäynnistysesimerkissä moottorin pääpiiri saa kolmivaihesyötön keskuksen jakelusta. Ohjauspiirin 24 V DC tulee keskuksen virtalähteestä. Virtalähde saa syöttönsä omasta suojatusta haarastaan ennen moottorin kontaktoria. Näin ohjaus on käytettävissä jo moottorin seistessä. K1 on säätimen ohjaama välirele, KM2 moottorikontaktori.

| Virtapiiri              | Seurattava reitti                                                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Ohjauspiiri, 24 V DC    | +24 V → K1:n käyntipyynnön kosketin → ylikuormitusreleen apukosketin → KM2:n kela A1–A2 → 0 V                       |
| Päävirtapiiri, 400 V AC | L1, L2, L3, suojattu syöttö → KM2:n kolme pääkosketinta → ylikuormitusreleen virtaelementit → kompressorin moottori |

Ohjauspiirin reittiä luetaan virtalähteen plussasta kelan kautta takaisin 0 V:iin. Pääpiirin reitti näyttää kolmivaihesyötön reitin moottorille. KM2:n kelan vetäminen liikuttaa saman kontaktorin pääkoskettimia mekaanisesti. Ylikuormitusrele seuraa pääpiirin virtaa ja avaa lauetessaan ohjauspiirin apukoskettimen. Vaikka K1 pyytäisi edelleen käyntiä, KM2:n kelavirta katkeaa ja pääkoskettimet avautuvat.

### Etsi kontaktori valmistajan kaaviosta

Daikinin LREQ8–12BY1-ulkoyksikön kokonaiskaaviossa A1P-ohjauskortin rele K1R ohjaa kontaktoria K2M, jonka pääkoskettimien kautta vakiokierroskompressori M2C saa tehonsa. Kompressorin M1C syöttö kulkee invertterin kautta. Imupaineanturi S1NPL tuottaa mittaustiedon, kun taas S1PH ja S2PH ovat korkeapainesuojia. Etsi kaaviosta ensin M2C, seuraa sen kolmea johdinta K2M:lle ja etsi sitten saman tunnuksen kela.

## Lähteet ja ylläpitotiedot

Oppitunti 16.11.2026. Muistio kokoaa oppitunnin esimerkit ja niitä täydentävät selitykset. Laitetunnukset ja esimerkkijännitteet kuuluvat kuhunkin kuvattuun harjoitukseen.

### Täydentävät valmistajalähteet

- [BITZERin pump-down-piirrosmerkit, kaaviot ja toimintaselostus](https://www.bitzer.de/shared_media/html/st-600/en-GB/652036491652038283.html)
- [Danfoss AK-PC 551, erityisesti s. 4 ja 11](https://assets.danfoss.com/documents/latest/192581/BC212486423949en-000501.pdf)
- [Schneider Electric, suorakäynnistin ja ylikuormitusrele](https://www.se.com/nl/nl/faqs/FA139744/)
- [Daikinin ulkoyksikön sähkökaavio, yksi PDF-sivu](https://www.daikin.es/content/dam/MDM/TechnicalDrawings/Refrigeration/EN/LREQ8-12BY1_wir3_3D070677J_EN.pdf)
