---
title: "Kaavat ja yksiköt"
publish: true
---

## Lämpöoppi

### Suureet ja tunnukset

| Suure                   | Tunnus | Yksikkö                            | Yksikön tunnus |
| ----------------------- | -----: | ---------------------------------- | -------------: |
| Teho                    |      P | watti                              |              W |
| Lämpötila               |      T | kelvin                             |              K |
| Lämpömäärä / energia    |      Q | joule                              |              J |
| Massa                   |      m | kilogramma                         |             kg |
| Aika                    |      t | sekunti                            |              s |
| Ominaislämpö            |      c | kilojoule per kilogramma ja kelvin |      kJ/(kg·K) |
| Massavirta              |      ṁ | kilogramma sekunnissa              |           kg/s |
| Lämpötilaero            |     ΔT | kelvin                             |              K |
| Tulistus                |     SH | kelvin                             |              K |
| Alijäähdytys            |     SC | kelvin                             |              K |
| Sulamislämpö            |      s | kilojoule per kilogramma           |          kJ/kg |
| Ominaishöyrystymislämpö |      r | kilojoule per kilogramma           |          kJ/kg |

### Lämpömäärä / energia

- Jäähdytys tai lämmitys: `Q = c × m × ΔT`
- Sulaminen tai jäätyminen: `Q = s × m`
- Höyrystyminen: `Q = r × m`

### Teho

- Jäähdytys tai lämmitys: `P = c × ṁ × ΔT`
- Sulaminen tai jäätyminen: `P = s × ṁ`
- Höyrystyminen: `P = r × ṁ`
- Energian ja ajan avulla: `P = Q / t`

### Tulistus ja alijäähdytys

- Tulistus: `SH = imuputken lämpötila − imupainetta vastaava kyllästymislämpötila`
- Alijäähdytys: `SC = korkeapainetta vastaava kyllästymislämpötila − nesteputken lämpötila`

**Kurssin muistisääntö:** imupainetta vastaavan kyllästymis- eli höyrystymislämpötilan tulisi olla **5–15 K kylmälaitteen tavoitelämpötilaa alempi**.

Paineita vastaavat kyllästymislämpötilat katsotaan kyseisen kylmäaineen paine–lämpötila-taulukosta tai mittarista. Jos kylmäaineella on lämpötilaliukuma, tulistuksessa käytetään kastepistelämpötilaa ja alijäähdytyksessä kuplapistelämpötilaa.

### Muistettavat arvot

- Veden ominaislämpö: **4,2 kJ/(kg·K)**
- Ilman ominaislämpö: **1 kJ/(kg·K)**
- Veden sulamislämpö: **333 kJ/kg**
- Veden höyrystymislämpö: **2260 kJ/kg**

### Lämpöopin yksikkömuisti

- Lämpötilaeron lukuarvo on sama kelvineinä ja celsiusasteina: 10 °C:n ero = 10 K.
- Kun energia-arvot ovat kilojouleina ja massa kilogrammoina, `Q` saadaan kilojouleina.
- Tehokaavoissa `kJ/s = kW`.
- `1 kJ = 1 000 J` ja `1 kW = 1 000 W`.

## Kylmäaineet ja CO₂-ekvivalentti

- **GWP** ja **ODP** ovat yksiköttömiä suhdelukuja.
- **ekvt** = muistiinpanoissa ekvivalenttitonni; tässä **t CO₂-ekv.**
- `CO₂-ekvivalentti [t CO₂-ekv.] = kylmäaineen massa [kg] × GWP / 1000`
- Täydentävä esimerkki oppitunnin R410A-arvolla: `1 kg × 2088 / 1000 = 2,088 t CO₂-ekv.`
- Oppitunnin R744-esimerkki: `100 kg × 1 / 1000 = 0,1 t CO₂-ekv.` eli 100 kg CO₂-ekv. R744:n GWP on 1.

Käsitteet, esimerkin rajaus ja lähteet: [Kylmäaineet](kylmaaineet.md). Alkuperäiset kuvat: oppitunnin lähdeaineisto.

## Paineen yksikkömuunnokset

- `1 bar = 1 000 mbar`
- `1 mbar = 0,001 bar`
- Kuvan ILP-vakuumointiesimerkki: **2,7 mbar = 0,0027 bar**.

Lähde: oppitunnin lähdeaineisto. Esimerkin asiayhteys ja ohjearvojen rajaus: [ILP-asennus – oppitunnin muistiinpanot 8.9.2026](kylmatekniikan-perusteet.md#ilp-asennus--oppitunnin-muistiinpanot-892026).

## Sähköoppi

### Suureet ja tunnukset

| Suure                    |  Tunnus | Yksikkö                   | Yksikön tunnus |
| ------------------------ | ------: | ------------------------- | -------------: |
| Jännite                  |       U | voltti                    |              V |
| Virta                    |       I | ampeeri                   |              A |
| Resistanssi              |       R | ohmi                      |              Ω |
| Resistiivisyys           |       ρ | ohmimetri                 |            Ω·m |
| Sähkönjohtavuus          |       σ | siemens metriä kohti      |            S/m |
| Johtimen pituus          |       l | metri                     |              m |
| Johtimen poikkipinta-ala |       A | neliömetri                |             m² |
| Teho                     |       P | watti                     |              W |
| Sähköenergia             | W tai E | wattitunti                |             Wh |
| Sähkövaraus              |       Q | coulombi / ampeerisekunti |         C / As |
| Aika                     |       t | sekunti                   |              s |
| Kapasitanssi             |       C | faradi                    |              F |
| Induktanssi              |       L | henry                     |              H |
| Taajuus                  |       f | hertsi                    |             Hz |

Sama tunnus voi tarkoittaa eri yhteyksissä eri suuretta. Esimerkiksi `Q` tarkoittaa lämpöopissa lämpömäärää ja tässä sähkövarausta. Myös `C` voi tarkoittaa joko sähkövarauksen yksikköä coulombia tai kapasitanssin tunnusta. `A` voi olla poikkipinta-alan tunnus tai virran yksikön ampeerin tunnus; asiayhteys ratkaisee.

### Resistiivisyys ja johtavuus

- Resistiivisyys: `ρ = R × A / l`
- Johtimen resistanssi: `R = ρ × l / A`
- Poikkipinta-ala: `A = ρ × l / R`
- Pituus: `l = R × A / ρ`
- Materiaalin sähkönjohtavuus: `σ = 1 / ρ`

Kaavat koskevat tasalaatuista johdinta, jonka poikkipinta-ala on vakio. `R` annetaan ohmeina ja `l` metreinä. Kun `A` on neliömetreinä, `ρ` on yksikössä `Ω·m` ja `σ` yksikössä `S/m`.

Johdinlaskuissa myös: `A` yksikössä `mm²` ja `ρ` yksikössä `Ω·mm²/m`. Älä sekoita tämän ja SI-muodon lukuarvoja.

- `1 mm² = 10⁻⁶ m²`
- `1 Ω·mm²/m = 10⁻⁶ Ω·m`

Johtimen lämpöhäviöteho: `P_häviö = I² × R`. Pienempi resistanssi pienentää lämpöhäviötehoa **samalla virralla**.

Lähde ja selitys: [Resistiivisyys ja johtavuus](sahkoopin-perusteet.md#resistiivisyys-ja-johtavuus) — oppitunti 21.9.2026 sekä erikseen merkityt selittävät täydennykset.

### Sähkövaraus, virta ja aika

- `Q = I × t`
- `I = Q / t`
- `t = Q / I`

Yksiköiden yhteys: `1 C = 1 As`.

Esimerkki: `Q = 3 600 As` ja `I = 1 A`:

`t = Q / I = 3 600 As / 1 A = 3 600 s = 1 h`

### Vastusten sarja- ja rinnankytkentä

| Kytkentä               | Kokonaisresistanssi              | Virta ja jännite                        |
| ---------------------- | -------------------------------- | --------------------------------------- |
| Sarja                  | `Rkok = R1 + R2 + …`             | `I = I1 = I2 = …`, `U = U1 + U2 + …`    |
| Rinnan, yleinen        | `1 / Rkok = 1 / R1 + 1 / R2 + …` | `U = U1 = U2 = …`, `Ikok = I1 + I2 + …` |
| Rinnan, kaksi vastusta | `Rkok = (R1 × R2) / (R1 + R2)`   | Sama jännite kummankin vastuksen yli    |

Kahdelle rinnakkaiselle vastukselle myös `Rkok = 1 / (1 / R1 + 1 / R2)` ja `1 / Rkok = (R1 + R2) / (R1 × R2)`. Jälkimmäinen antaa resistanssin käänteisluvun.

Resistanssien yksikkö on ohmi (Ω); käytä laskussa samaa yksikköä kaikille vastuksille. Rinnankytkennän kokonaisresistanssi on pienempi kuin pienin yksittäinen vastus (positiiviset, äärelliset vastukset).

Selitys ja esimerkit: [Vastusten sarjakytkentä](sahkoopin-perusteet.md#vastusten-sarjakytkentä) ja [Vastusten rinnankytkentä](sahkoopin-perusteet.md#vastusten-rinnankytkentä).

### Hyötysuhde

- `η = P₂ / P₁`
- `P₂` = antoteho
- `P₁` = ottoteho
- prosentteina: `η% = (P₂ / P₁) × 100 %`

Tehohäviöiden vuoksi laitteen hyötysuhde on alle yksi.

Lähde: oppitunti 21.9.2026, [Hyötysuhde](sahkoopin-perusteet.md#hyötysuhde).

### Sähköteho

- `P = U × I`
- `U = P / I`
- `I = P / U`

Kun `U` annetaan voltteina ja `I` ampeereina, tulos saadaan watteina: `V × A = W`.

### Sinimuotoisen vaihtosähkön arvot ja taajuus

- Tehollisarvo: `U_eff = 0,707 × Û = Û / √2`
- Huippuarvo: `Û = √2 × U_eff`
- Huipusta huippuun: `U_pp = 2 × Û`
- Taajuus: `f = 1 / T`
- Jaksonaika: `T = 1 / f`
- Hetkellisarvo: `u = û × sin α`, missä `û` on jännitteen huippuarvo ja `α` vaihekulma

Esimerkki 230 V / 50 Hz: `Û ≈ 325 V`, `U_pp ≈ 650 V` ja `T = 20 ms`.

Lähde: oppitunti 21.9.2026, [Hetkellis-, huippu- ja tehollisarvo](sahkoopin-perusteet.md#hetkellis--huippu--ja-tehollisarvo).

### Sähköenergia

- `E = P × t`
- `P = E / t`
- `t = E / P`

Kun teho annetaan watteina ja aika tunteina, energia saadaan wattitunteina: `W × h = Wh`.

## Kerrannaisyksiköt

| Etuliite     | Tunnus | Kymmenpotenssi |   Kerroin |
| ------------ | -----: | -------------: | --------: |
| mikro        |      µ |           10⁻⁶ | 0,000 001 |
| milli        |      m |           10⁻³ |     0,001 |
| perusyksikkö |      – |            10⁰ |         1 |
| kilo         |      k |            10³ |     1 000 |
| mega         |      M |            10⁶ | 1 000 000 |

Esimerkkejä:

- `13 µA = 0,000 013 A`
- `257 mA = 0,257 A`
- `0,754 kΩ = 754 Ω`
- `1,342 MΩ = 1 342 000 Ω`
- `1 kW = 1 000 W`
- `1 kWh = 1 000 Wh`
- `1 h = 3 600 s`

## Lähdekuvat

- oppitunnin lähdeaineisto — lämpöopin kaavat ja yksiköt
- oppitunnin lähdeaineisto — sähköopin suureet ja yksiköt
- oppitunnin lähdeaineisto — kerrannaisyksiköt ja mittarin lukemat
- oppitunnin lähdeaineisto — sähkövarauksen kaava
- oppitunnin lähdeaineisto — tulistuksen ja alijäähdytyksen kaavat
- oppitunnin lähdeaineisto — tulistuksen ja alijäähdytyksen mittausesimerkki
- oppitunnin lähdeaineisto — vastusten sarja- ja rinnankytkennän kaavat (7.9.2026)
