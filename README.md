# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--11_14:40:26_UTC-green)

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

**Latest saved flight:** 2026-06-11 14:40:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-11 14:40:26 UTC

- **108,104** saved flights
- **37,840** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **108,104** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,321,164.6 tonnes** estimated CO2 emissions
- **76,589,250 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4459 |
| 2 | SkyWest Airlines | 4048 |
| 3 | IndiGo | 2145 |
| 4 | EJA | 2082 |
| 5 | American Airlines | 1715 |
| 6 | Southwest Airlines | 1621 |
| 7 | ENY | 1348 |
| 8 | Delta Air Lines | 1281 |
| 9 | Lufthansa | 1231 |
| 10 | Vueling | 988 |
| 11 | LATAM Airlines | 959 |
| 12 | WIF | 953 |
| 13 | AXM | 917 |
| 14 | AZU | 882 |
| 15 | LXJ | 814 |
| 16 | Swiss International | 788 |
| 17 | All Nippon Airways | 751 |
| 18 | Alaska Airlines | 740 |
| 19 | QLK | 717 |
| 20 | easyJet | 699 |
| 21 | EJU | 690 |
| 22 | Cathay Pacific | 650 |
| 23 | AEE | 616 |
| 24 | VIV | 616 |
| 25 | Air France | 611 |
| 26 | United Airlines | 594 |
| 27 | MXY | 582 |
| 28 | CXK | 569 |
| 29 | Japan Airlines | 534 |
| 30 | AXB | 532 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 90846 |
| 2 | 🇪🇸 ES | 7424 |
| 3 | 🇮🇳 IN | 6758 |
| 4 | 🇦🇺 AU | 6480 |
| 5 | 🇧🇷 BR | 5959 |
| 6 | 🇩🇪 DE | 5805 |
| 7 | 🇮🇹 IT | 5794 |
| 8 | 🇨🇦 CA | 5667 |
| 9 | 🇯🇵 JP | 4928 |
| 10 | 🇬🇧 GB | 4594 |
| 11 | 🇫🇷 FR | 4311 |
| 12 | 🇨🇴 CO | 3740 |
| 13 | 🇲🇽 MX | 3230 |
| 14 | 🇬🇷 GR | 3072 |
| 15 | 🇳🇴 NO | 2995 |
| 16 | 🇨🇭 CH | 2761 |
| 17 | 🇲🇾 MY | 2353 |
| 18 | 🇹🇷 TR | 2101 |
| 19 | 🇿🇦 ZA | 1849 |
| 20 | 🇰🇷 KR | 1794 |
| 21 | 🇳🇿 NZ | 1794 |
| 22 | 🇹🇭 TH | 1779 |
| 23 | 🇵🇱 PL | 1769 |
| 24 | 🇵🇭 PH | 1586 |
| 25 | 🇬🇹 GT | 1551 |
| 26 | 🇲🇦 MA | 1193 |
| 27 | 🇲🇴 MO | 1136 |
| 28 | 🇳🇱 NL | 1066 |
| 29 | 🇲🇪 ME | 1045 |
| 30 | 🇭🇷 HR | 949 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2329 |
| 2 | Denver International Airport |  | US | 1829 |
| 3 | Tokyo International Airport |  | JP | 1631 |
| 4 | Indira Gandhi International Airport |  | IN | 1470 |
| 5 | Guaymaral Airport |  | CO | 1379 |
| 6 | Harry Reid International Airport |  | US | 1374 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1354 |
| 8 | Zurich Airport |  | CH | 1227 |
| 9 | Frankfurt am Main International Airport |  | DE | 1214 |
| 10 | La Aurora Airport |  | GT | 1193 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1161 |
| 12 | Macau International Airport |  | MO | 1136 |
| 13 | El Dorado International Airport |  | CO | 1132 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1081 |
| 15 | Chicago O'Hare International Airport |  | US | 1075 |
| 16 | Madrid Barajas International Airport |  | ES | 941 |
| 17 | Capua Airport |  | IT | 929 |
| 18 | Kuala Lumpur International Airport |  | MY | 922 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 920 |
| 20 | Salt Lake City International Airport |  | US | 915 |
| 21 | Charlotte/Douglas International Airport |  | US | 834 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 823 |
| 23 | Congonhas Airport |  | BR | 823 |
| 24 | Charles de Gaulle International Airport |  | FR | 817 |
| 25 | Bengaluru International Airport |  | IN | 816 |
| 26 | Malpensa International Airport |  | IT | 800 |
| 27 | Daniel K Inouye International Airport |  | US | 728 |
| 28 | Ninoy Aquino International Airport |  | PH | 728 |
| 29 | Tenerife Norte Airport |  | ES | 724 |
| 30 | Barcelona International Airport |  | ES | 706 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 703 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 701 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 699 |
| 34 | Amsterdam Airport Schiphol |  | NL | 656 |
| 35 | Don Mueang International Airport |  | TH | 650 |
| 36 | Vitoria/Foronda Airport |  | ES | 646 |
| 37 | Calgary International Airport |  | CA | 636 |
| 38 | Seattle-Tacoma International Airport |  | US | 621 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 619 |
| 40 | Netaji Subhash Chandra Bose International Airport |  | IN | 610 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 571 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 396 | 21m | 244 km | 1,667.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 288 | 24m | 225 km | 1,117.3 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 283 | 1h 7m | 706 km | 3,445.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 279 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 263 | 1h 25m | 910 km | 4,127.1 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 259 | 28m | 304 km | 1,357.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 250 | 1h 10m | 770 km | 3,321.1 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 221 | 19m | 165 km | 628.6 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 217 | 26m | 275 km | 1,028.3 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 208 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 162 | 20m | 99 km | 277.5 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 158 | 27m | 215 km | 585.2 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 158 | 22m | 55 km | 150.2 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 152 | 14m | 154 km | 402.7 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 150 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 150 | 27m | 152 km | 392.0 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 147 | 31m | 369 km | 935.7 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 145 | 44m | 452 km | 1,130.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 140 | 18m | 144 km | 348.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 132 | 1h 1m | 695 km | 1,582.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 26 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 130 | 44m | 241 km | 540.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 128 | 1h 43m | 1,423 km | 3,141.3 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 123 | 1h 17m | 961 km | 2,038.8 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TGJAK | TGJ | La Retama Southwest Airport (MM17) | Piedras Negras International Airport (MMPG) | 2026-06-11 12:53 UTC | 2026-06-11 14:40 UTC | 1h 47m |
| N2857Q |  | Treasure Coast International Airport (KFPR) | Baggett Airport (FD57) | 2026-06-11 13:37 UTC | 2026-06-11 14:38 UTC | 1h 1m |
| N6896H |  | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-06-11 14:21 UTC | 2026-06-11 14:36 UTC | 14m |
| N103LU |  | Boca Raton Airport (KBCT) | Duda Airstrip (FA69) | 2026-06-11 13:57 UTC | 2026-06-11 14:31 UTC | 33m |
| N553XB |  | New York Stewart International Airport (KSWF) | Newark Liberty International Airport (KEWR) | 2026-06-11 14:11 UTC | 2026-06-11 14:29 UTC | 18m |
| LYRE71 | LYR | Randolph Afb Airport (KRND) | Tee Pee Creek Airport (8TE0) | 2026-06-11 13:36 UTC | 2026-06-11 14:28 UTC | 51m |
| SCA42 | SCA | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-06-11 13:55 UTC | 2026-06-11 14:23 UTC | 27m |
| N5522X |  | 19OK (19OK) | 19OK (19OK) | 2026-06-11 13:56 UTC | 2026-06-11 14:23 UTC | 26m |
| N378BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-06-11 13:04 UTC | 2026-06-11 14:19 UTC | 1h 15m |
| AXY99BT | AXY | Graz Airport (LOWG) | Graz Airport (LOWG) | 2026-06-11 13:41 UTC | 2026-06-11 14:17 UTC | 35m |
| N5437F |  | Marv Skie-Lincoln County Airport (KY14) | Brookings Regional Airport (KBKX) | 2026-06-11 13:39 UTC | 2026-06-11 14:17 UTC | 37m |
| CGNNQ | CGN | Colonial Airport (NY24) | Colonial Airport (NY24) | 2026-06-11 13:19 UTC | 2026-06-11 14:17 UTC | 57m |
| EJA676 | EJA | Linwood Airport (MS06) | Akron-Canton Regional Airport (KCAK) | 2026-06-11 12:39 UTC | 2026-06-11 14:16 UTC | 1h 36m |
| HBZNP | HBZ | Langenthal Airport (LSPL) | Kagiswil Airport (LSPG) | 2026-06-11 13:57 UTC | 2026-06-11 14:16 UTC | 18m |
| N680ND |  | Brookings Regional Airport (KBKX) | Brookings Regional Airport (KBKX) | 2026-06-11 13:39 UTC | 2026-06-11 14:16 UTC | 36m |
| N94986 |  | Usaf Academy Davis Airfield (KAFF) | Perry Stokes Airport (KTAD) | 2026-06-11 13:21 UTC | 2026-06-11 14:13 UTC | 51m |
| N507CC |  | Savannah/Hilton Head International Airport (KSAV) | Savannah/Hilton Head International Airport (KSAV) | 2026-06-11 13:47 UTC | 2026-06-11 14:10 UTC | 22m |
| RSCU440 | RSC | Melbourne Essendon Airport (YMEN) | Blinman Airport (YBLM) | 2026-06-11 12:27 UTC | 2026-06-11 14:10 UTC | 1h 43m |
| PTZNG | PTZ | Marchesan S.A. Airport (SDME) | Eurico de Aguiar Salles Airport (SBVT) | 2026-06-11 12:48 UTC | 2026-06-11 14:06 UTC | 1h 18m |
| HK5463X |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-06-11 13:50 UTC | 2026-06-11 14:04 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
