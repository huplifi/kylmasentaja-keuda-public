# Kylmäasentajan muistiinpanot

Opiskelumuistiinpanoja kylmäasentajan opinnoista. Ei Keudan virallista oppimateriaalia. Aineistoa täydennetään opintojen edetessä.

Sivusto: https://huplifi.github.io/kylmasentaja-keuda-public/

`content/`, sen tarkistussummat sekä sivuston asetukset tuotetaan automaattisesti yksityisen kanonisen lähteen turvallisella exportilla. Älä ylläpidä tässä toista muistiinpanokokoelmaa: käsin tehdyt sisältömuutokset korvautuvat seuraavassa viennissä. Tässä repossa ei ole pääsyä yksityiseen lähteeseen tai sen historiaan.

## Paikallinen esikatselu

Node.js 22 ja npm 10 tai uudempi, Python 3.

```sh
npm ci
python3 scripts/validate_site.py
npx quartz build
python3 scripts/validate_site.py --build public
npx quartz build --serve
```

GitHub Actions tarkistaa sisältömanifestin, rakentaa sivuston, tarkistaa HTML-linkit ja hakuhakemiston ja julkaisee vain onnistuneen buildin GitHub Pagesiin.

Quartz 4.5.2, upstream commit `4923affa7722dfc751f1074348e6dad214fe0c08`. Quartzin ohjelmistolisenssi: [LICENSE.txt](LICENSE.txt). Muistiinpanoille ei tällä merkinnällä myönnetä erillistä uudelleenjulkaisulisenssiä.

Upstream-versioon on tehty rajatut ylläpitomuutokset: riippuvuuksien tietoturvapäivitykset (myös js-yaml 4.3.2, sharp 0.35.4 ja toml 5.0.0), mobiilivalikon saavutettava nimi ja neutraali suomenkielinen 404-teksti. Nämä sivuston ohjelmistomuutokset ylläpidetään tässä repossa; generoitu sisältö ja esitystapa tulevat lähteen exportista.
