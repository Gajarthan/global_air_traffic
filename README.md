# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_15:31:23_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-05-30 15:31:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-30 15:31:23 UTC

- **97,190** saved flights
- **34,174** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **97,190** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,189,438.2 tonnes** estimated CO2 emissions
- **68,952,940 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4080 |
| 2 | SkyWest Airlines | 3606 |
| 3 | IndiGo | 2001 |
| 4 | EJA | 1838 |
| 5 | American Airlines | 1472 |
| 6 | Southwest Airlines | 1408 |
| 7 | ENY | 1193 |
| 8 | Lufthansa | 1163 |
| 9 | Delta Air Lines | 1064 |
| 10 | Vueling | 916 |
| 11 | LATAM Airlines | 870 |
| 12 | WIF | 865 |
| 13 | AXM | 854 |
| 14 | AZU | 786 |
| 15 | LXJ | 740 |
| 16 | Swiss International | 722 |
| 17 | All Nippon Airways | 710 |
| 18 | Alaska Airlines | 674 |
| 19 | QLK | 669 |
| 20 | easyJet | 636 |
| 21 | EJU | 615 |
| 22 | Cathay Pacific | 587 |
| 23 | AEE | 584 |
| 24 | VIV | 574 |
| 25 | Air France | 569 |
| 26 | CXK | 522 |
| 27 | MXY | 514 |
| 28 | Japan Airlines | 497 |
| 29 | AXB | 488 |
| 30 | AIQ | 466 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 80407 |
| 2 | 🇪🇸 ES | 6784 |
| 3 | 🇮🇳 IN | 6319 |
| 4 | 🇦🇺 AU | 5926 |
| 5 | 🇧🇷 BR | 5357 |
| 6 | 🇩🇪 DE | 5345 |
| 7 | 🇮🇹 IT | 5248 |
| 8 | 🇨🇦 CA | 4944 |
| 9 | 🇯🇵 JP | 4600 |
| 10 | 🇬🇧 GB | 4171 |
| 11 | 🇫🇷 FR | 3940 |
| 12 | 🇨🇴 CO | 3377 |
| 13 | 🇲🇽 MX | 2988 |
| 14 | 🇬🇷 GR | 2810 |
| 15 | 🇳🇴 NO | 2738 |
| 16 | 🇨🇭 CH | 2555 |
| 17 | 🇲🇾 MY | 2171 |
| 18 | 🇹🇷 TR | 1811 |
| 19 | 🇿🇦 ZA | 1731 |
| 20 | 🇳🇿 NZ | 1651 |
| 21 | 🇹🇭 TH | 1640 |
| 22 | 🇰🇷 KR | 1589 |
| 23 | 🇵🇱 PL | 1585 |
| 24 | 🇬🇹 GT | 1455 |
| 25 | 🇵🇭 PH | 1455 |
| 26 | 🇲🇦 MA | 1101 |
| 27 | 🇲🇴 MO | 1044 |
| 28 | 🇳🇱 NL | 984 |
| 29 | 🇲🇪 ME | 953 |
| 30 | 🇭🇷 HR | 880 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2102 |
| 2 | Denver International Airport |  | US | 1640 |
| 3 | Tokyo International Airport |  | JP | 1525 |
| 4 | Indira Gandhi International Airport |  | IN | 1370 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1283 |
| 6 | Harry Reid International Airport |  | US | 1244 |
| 7 | Guaymaral Airport |  | CO | 1205 |
| 8 | Frankfurt am Main International Airport |  | DE | 1171 |
| 9 | Zurich Airport |  | CH | 1135 |
| 10 | La Aurora Airport |  | GT | 1116 |
| 11 | El Dorado International Airport |  | CO | 1046 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1045 |
| 13 | Macau International Airport |  | MO | 1044 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 972 |
| 15 | Chicago O'Hare International Airport |  | US | 932 |
| 16 | Madrid Barajas International Airport |  | ES | 862 |
| 17 | Kuala Lumpur International Airport |  | MY | 858 |
| 18 | Salt Lake City International Airport |  | US | 818 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 813 |
| 20 | Capua Airport |  | IT | 802 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 769 |
| 22 | Malpensa International Airport |  | IT | 760 |
| 23 | Bengaluru International Airport |  | IN | 755 |
| 24 | Charles de Gaulle International Airport |  | FR | 753 |
| 25 | Congonhas Airport |  | BR | 742 |
| 26 | Charlotte/Douglas International Airport |  | US | 737 |
| 27 | Daniel K Inouye International Airport |  | US | 688 |
| 28 | Tenerife Norte Airport |  | ES | 682 |
| 29 | Ninoy Aquino International Airport |  | PH | 664 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 651 |
| 31 | Barcelona International Airport |  | ES | 649 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 625 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 622 |
| 34 | Amsterdam Airport Schiphol |  | NL | 604 |
| 35 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 36 | Don Mueang International Airport |  | TH | 601 |
| 37 | Vitoria/Foronda Airport |  | ES | 598 |
| 38 | Calgary International Airport |  | CA | 573 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 571 |
| 40 | O. R. Tambo International Airport |  | ZA | 551 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 497 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 358 | 21m | 244 km | 1,507.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 263 | 24m | 225 km | 1,020.3 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 260 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 247 | 14m | 114 km | 484.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 243 | 1h 26m | 910 km | 3,813.2 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 242 | 28m | 304 km | 1,268.6 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 223 | 1h 10m | 770 km | 2,962.4 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 209 | 19m | 165 km | 594.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 194 | 26m | 275 km | 919.3 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 155 | 20m | 99 km | 265.5 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 146 | 27m | 215 km | 540.7 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 142 | 44m | 452 km | 1,106.7 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 141 | 22m | 55 km | 134.0 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 140 | 27m | 152 km | 365.9 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 132 | 20m | 250 km | 570.2 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 129 | 20m | 147 km | 326.4 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 129 | 13m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 126 | 18m | 144 km | 313.4 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 124 | 1h 1m | 695 km | 1,486.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 123 | 1h 39m | 1,156 km | 2,453.8 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 115 | 1h 18m | 961 km | 1,906.2 t |
| 28 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK147 | CXK | Ann Arbor Municipal Airport (KARB) | Ann Arbor Municipal Airport (KARB) | 2026-05-30 14:19 UTC | 2026-05-30 15:31 UTC | 1h 12m |
| BLADE5 | BLA | Ogden-Hinckley Airport (KOGD) | Ogden-Hinckley Airport (KOGD) | 2026-05-30 15:03 UTC | 2026-05-30 15:29 UTC | 25m |
| CONGO63 | CON | Southeast Colorado Regional Airport (KLAA) | Southeast Colorado Regional Airport (KLAA) | 2026-05-30 15:15 UTC | 2026-05-30 15:28 UTC | 13m |
| N649GC |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-05-30 14:40 UTC | 2026-05-30 15:20 UTC | 40m |
| N7079F |  | Rimrock Airport (48AZ) | Payson Airport (KPAN) | 2026-05-30 15:00 UTC | 2026-05-30 15:19 UTC | 18m |
| N312PH |  | Oakland/Troy Airport (KVLL) | Oakland/Troy Airport (KVLL) | 2026-05-30 15:07 UTC | 2026-05-30 15:17 UTC | 10m |
| GCPSS | GCP | Netheravon Airfield (EGDN) | Netheravon Airfield (EGDN) | 2026-05-30 13:40 UTC | 2026-05-30 15:16 UTC | 1h 36m |
|  |  | Texel Airport (EHTX) | Texel Airport (EHTX) | 2026-05-30 15:07 UTC | 2026-05-30 15:15 UTC | 7m |
| N252EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-05-30 14:15 UTC | 2026-05-30 15:14 UTC | 58m |
| 4XHSC |  | LL59 (LL59) | LL59 (LL59) | 2026-05-30 15:01 UTC | 2026-05-30 15:13 UTC | 11m |
| N526TB |  | Leesburg Executive Airport (KJYO) | Lancaster Airport (KLNS) | 2026-05-30 14:22 UTC | 2026-05-30 15:11 UTC | 49m |
| N90JF |  | Antonio/Nery/Juarbe Pol Airport (TJAB) | Antonio/Nery/Juarbe Pol Airport (TJAB) | 2026-05-30 14:57 UTC | 2026-05-30 15:11 UTC | 13m |
| N308JS |  | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-05-30 14:42 UTC | 2026-05-30 15:08 UTC | 25m |
| SCA75 | SCA | Scottsdale Airport (KSDL) | Montezuma Airport (19AZ) | 2026-05-30 14:26 UTC | 2026-05-30 15:06 UTC | 40m |
| N65842 |  | Jacksonville Executive At Craig Airport (KCRG) | Jacksonville Nas (Towers Field) Airport (KNIP) | 2026-05-30 14:42 UTC | 2026-05-30 15:04 UTC | 21m |
| CHH752 | CHH | Dublin Airport (EIDW) | Ukhta Airport (UUYH) | 2026-05-30 11:20 UTC | 2026-05-30 15:03 UTC | 3h 42m |
| CGSSC | CGS | Vancouver International Airport (CYVR) | Victoria International Airport (CYYJ) | 2026-05-30 14:33 UTC | 2026-05-30 15:02 UTC | 28m |
| N247EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-05-30 14:04 UTC | 2026-05-30 15:01 UTC | 57m |
| XBKMJ | XBK | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | General Mariano Matamoros Airport (MMCB) | 2026-05-30 14:33 UTC | 2026-05-30 15:01 UTC | 28m |
| N243EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-05-30 14:06 UTC | 2026-05-30 15:01 UTC | 54m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
