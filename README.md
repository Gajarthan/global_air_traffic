# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_17:36:34_UTC-green)

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

**Latest saved flight:** 2026-05-30 17:36:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-30 17:36:34 UTC

- **97,534** saved flights
- **34,271** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **97,534** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,193,299.6 tonnes** estimated CO2 emissions
- **69,176,788 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4094 |
| 2 | SkyWest Airlines | 3626 |
| 3 | IndiGo | 2007 |
| 4 | EJA | 1844 |
| 5 | American Airlines | 1475 |
| 6 | Southwest Airlines | 1413 |
| 7 | ENY | 1197 |
| 8 | Lufthansa | 1170 |
| 9 | Delta Air Lines | 1066 |
| 10 | Vueling | 923 |
| 11 | LATAM Airlines | 872 |
| 12 | WIF | 866 |
| 13 | AXM | 854 |
| 14 | AZU | 789 |
| 15 | LXJ | 742 |
| 16 | Swiss International | 725 |
| 17 | All Nippon Airways | 710 |
| 18 | Alaska Airlines | 674 |
| 19 | QLK | 669 |
| 20 | easyJet | 636 |
| 21 | EJU | 622 |
| 22 | Cathay Pacific | 587 |
| 23 | AEE | 586 |
| 24 | VIV | 575 |
| 25 | Air France | 574 |
| 26 | CXK | 525 |
| 27 | MXY | 516 |
| 28 | Japan Airlines | 497 |
| 29 | AXB | 492 |
| 30 | AIQ | 466 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 80722 |
| 2 | 🇪🇸 ES | 6828 |
| 3 | 🇮🇳 IN | 6337 |
| 4 | 🇦🇺 AU | 5926 |
| 5 | 🇩🇪 DE | 5374 |
| 6 | 🇧🇷 BR | 5372 |
| 7 | 🇮🇹 IT | 5272 |
| 8 | 🇨🇦 CA | 4958 |
| 9 | 🇯🇵 JP | 4604 |
| 10 | 🇬🇧 GB | 4180 |
| 11 | 🇫🇷 FR | 3953 |
| 12 | 🇨🇴 CO | 3403 |
| 13 | 🇲🇽 MX | 2996 |
| 14 | 🇬🇷 GR | 2821 |
| 15 | 🇳🇴 NO | 2745 |
| 16 | 🇨🇭 CH | 2561 |
| 17 | 🇲🇾 MY | 2172 |
| 18 | 🇹🇷 TR | 1821 |
| 19 | 🇿🇦 ZA | 1735 |
| 20 | 🇳🇿 NZ | 1651 |
| 21 | 🇹🇭 TH | 1640 |
| 22 | 🇵🇱 PL | 1590 |
| 23 | 🇰🇷 KR | 1589 |
| 24 | 🇬🇹 GT | 1469 |
| 25 | 🇵🇭 PH | 1457 |
| 26 | 🇲🇦 MA | 1104 |
| 27 | 🇲🇴 MO | 1044 |
| 28 | 🇳🇱 NL | 990 |
| 29 | 🇲🇪 ME | 954 |
| 30 | 🇭🇷 HR | 880 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2108 |
| 2 | Denver International Airport |  | US | 1646 |
| 3 | Tokyo International Airport |  | JP | 1525 |
| 4 | Indira Gandhi International Airport |  | IN | 1374 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1285 |
| 6 | Harry Reid International Airport |  | US | 1248 |
| 7 | Guaymaral Airport |  | CO | 1221 |
| 8 | Frankfurt am Main International Airport |  | DE | 1174 |
| 9 | Zurich Airport |  | CH | 1138 |
| 10 | La Aurora Airport |  | GT | 1129 |
| 11 | El Dorado International Airport |  | CO | 1051 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1049 |
| 13 | Macau International Airport |  | MO | 1044 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 976 |
| 15 | Chicago O'Hare International Airport |  | US | 934 |
| 16 | Madrid Barajas International Airport |  | ES | 863 |
| 17 | Kuala Lumpur International Airport |  | MY | 858 |
| 18 | Salt Lake City International Airport |  | US | 821 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 814 |
| 20 | Capua Airport |  | IT | 810 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 769 |
| 22 | Malpensa International Airport |  | IT | 762 |
| 23 | Charles de Gaulle International Airport |  | FR | 759 |
| 24 | Bengaluru International Airport |  | IN | 758 |
| 25 | Congonhas Airport |  | BR | 745 |
| 26 | Charlotte/Douglas International Airport |  | US | 743 |
| 27 | Daniel K Inouye International Airport |  | US | 688 |
| 28 | Tenerife Norte Airport |  | ES | 685 |
| 29 | Ninoy Aquino International Airport |  | PH | 665 |
| 30 | Barcelona International Airport |  | ES | 652 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 651 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 628 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 623 |
| 34 | Amsterdam Airport Schiphol |  | NL | 609 |
| 35 | Vitoria/Foronda Airport |  | ES | 602 |
| 36 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 37 | Don Mueang International Airport |  | TH | 601 |
| 38 | Calgary International Airport |  | CA | 576 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 572 |
| 40 | O. R. Tambo International Airport |  | ZA | 553 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 505 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 358 | 21m | 244 km | 1,507.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 265 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 263 | 24m | 225 km | 1,020.3 t |
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
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 133 | 20m | 250 km | 574.5 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 129 | 20m | 147 km | 326.4 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 129 | 13m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 126 | 18m | 144 km | 313.4 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 124 | 1h 1m | 695 km | 1,486.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 123 | 1h 39m | 1,156 km | 2,453.8 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 117 | 1h 43m | 1,423 km | 2,871.4 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 115 | 1h 18m | 961 km | 1,906.2 t |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ERU69 | ERU | Needles Airport (KEED) | Lake Havasu City Airport (KHII) | 2026-05-30 17:16 UTC | 2026-05-30 17:36 UTC | 20m |
| N3NT |  | Animas Air Park (K00C) | Hopkins Field (KAIB) | 2026-05-30 17:10 UTC | 2026-05-30 17:35 UTC | 24m |
| N630HR |  | Aero Valley Airport (K52F) | Teate Field (4XS2) | 2026-05-30 17:09 UTC | 2026-05-30 17:28 UTC | 18m |
| N4841Y |  | Kelly Air Park (CO15) | Kelly Air Park (CO15) | 2026-05-30 17:09 UTC | 2026-05-30 17:27 UTC | 17m |
| N722UE |  | North Las Vegas Airport (KVGT) | Sky Ranch Airport (K3L2) | 2026-05-30 17:10 UTC | 2026-05-30 17:26 UTC | 15m |
| DFANO | DFA | Æra Airfield (ENAE) | Æra Airfield (ENAE) | 2026-05-30 17:13 UTC | 2026-05-30 17:23 UTC | 10m |
| N932H |  | Harry P Williams Memorial Airport (KPTN) | Houma-Terrebonne Airport (KHUM) | 2026-05-30 16:58 UTC | 2026-05-30 17:15 UTC | 17m |
| N286DA |  | Santa Monica Municipal Airport (KSMO) | Lake Tahoe Airport (KTVL) | 2026-05-30 15:13 UTC | 2026-05-30 17:13 UTC | 1h 59m |
| PSFUN | PSF | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-05-30 16:53 UTC | 2026-05-30 17:10 UTC | 17m |
| N541S |  | Pensacola International Airport (KPNS) | MS68 (MS68) | 2026-05-30 16:30 UTC | 2026-05-30 17:09 UTC | 39m |
| N121TS |  | Cincinnati Municipal/Lunken Field (KLUK) | Kalkaska City Airport (KY89) | 2026-05-30 16:07 UTC | 2026-05-30 17:08 UTC | 1h 1m |
| AUA857 | Austrian Airlines | Vienna International Airport (LOWW) | Aktion National Airport (LGPZ) | 2026-05-30 15:48 UTC | 2026-05-30 17:08 UTC | 1h 19m |
| N114FA |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-05-30 16:01 UTC | 2026-05-30 17:06 UTC | 1h 5m |
| N999VP |  | IS95 (IS95) | Vogen Airport (IS41) | 2026-05-30 16:53 UTC | 2026-05-30 17:06 UTC | 13m |
| N4217W |  | Shelby Air Service Airport (93MS) | Dorr Field (MS95) | 2026-05-30 16:49 UTC | 2026-05-30 17:05 UTC | 16m |
| N62VY |  | Bend Municipal Airport (KBDN) | Goering Ranches / Chocheta Estates Airport (50OR) | 2026-05-30 16:25 UTC | 2026-05-30 17:05 UTC | 39m |
| N999DJ |  | Seminole Municipal Airport (KSRE) | Worland Municipal Airport (KWRL) | 2026-05-30 15:13 UTC | 2026-05-30 17:00 UTC | 1h 46m |
| XBONC | XBO | Hermanos Serdan International Airport (MMPB) | Cordoba Airport (MM20) | 2026-05-30 14:46 UTC | 2026-05-30 16:59 UTC | 2h 13m |
| HK5431G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-05-30 16:38 UTC | 2026-05-30 16:58 UTC | 20m |
| TGSUN | TGS | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-05-30 16:51 UTC | 2026-05-30 16:58 UTC | 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
