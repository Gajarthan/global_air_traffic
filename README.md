# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_23:19:26_UTC-green)

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

**Latest saved flight:** 2026-05-30 23:19:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-30 23:19:26 UTC

- **98,122** saved flights
- **34,466** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **98,122** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,201,346.2 tonnes** estimated CO2 emissions
- **69,643,256 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4115 |
| 2 | SkyWest Airlines | 3668 |
| 3 | IndiGo | 2010 |
| 4 | EJA | 1860 |
| 5 | American Airlines | 1489 |
| 6 | Southwest Airlines | 1426 |
| 7 | ENY | 1206 |
| 8 | Lufthansa | 1172 |
| 9 | Delta Air Lines | 1077 |
| 10 | Vueling | 928 |
| 11 | LATAM Airlines | 877 |
| 12 | WIF | 866 |
| 13 | AXM | 854 |
| 14 | AZU | 797 |
| 15 | LXJ | 746 |
| 16 | Swiss International | 726 |
| 17 | All Nippon Airways | 710 |
| 18 | Alaska Airlines | 677 |
| 19 | QLK | 669 |
| 20 | easyJet | 645 |
| 21 | EJU | 623 |
| 22 | Cathay Pacific | 591 |
| 23 | AEE | 587 |
| 24 | VIV | 576 |
| 25 | Air France | 574 |
| 26 | CXK | 528 |
| 27 | MXY | 523 |
| 28 | Japan Airlines | 497 |
| 29 | AXB | 492 |
| 30 | GLO | 467 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 81401 |
| 2 | 🇪🇸 ES | 6874 |
| 3 | 🇮🇳 IN | 6350 |
| 4 | 🇦🇺 AU | 5934 |
| 5 | 🇧🇷 BR | 5409 |
| 6 | 🇩🇪 DE | 5393 |
| 7 | 🇮🇹 IT | 5294 |
| 8 | 🇨🇦 CA | 4994 |
| 9 | 🇯🇵 JP | 4604 |
| 10 | 🇬🇧 GB | 4211 |
| 11 | 🇫🇷 FR | 3963 |
| 12 | 🇨🇴 CO | 3440 |
| 13 | 🇲🇽 MX | 3009 |
| 14 | 🇬🇷 GR | 2841 |
| 15 | 🇳🇴 NO | 2746 |
| 16 | 🇨🇭 CH | 2568 |
| 17 | 🇲🇾 MY | 2172 |
| 18 | 🇹🇷 TR | 1851 |
| 19 | 🇿🇦 ZA | 1737 |
| 20 | 🇳🇿 NZ | 1651 |
| 21 | 🇹🇭 TH | 1640 |
| 22 | 🇵🇱 PL | 1594 |
| 23 | 🇰🇷 KR | 1590 |
| 24 | 🇬🇹 GT | 1469 |
| 25 | 🇵🇭 PH | 1458 |
| 26 | 🇲🇦 MA | 1110 |
| 27 | 🇲🇴 MO | 1046 |
| 28 | 🇳🇱 NL | 992 |
| 29 | 🇲🇪 ME | 956 |
| 30 | 🇭🇷 HR | 881 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2128 |
| 2 | Denver International Airport |  | US | 1664 |
| 3 | Tokyo International Airport |  | JP | 1525 |
| 4 | Indira Gandhi International Airport |  | IN | 1378 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1288 |
| 6 | Harry Reid International Airport |  | US | 1260 |
| 7 | Guaymaral Airport |  | CO | 1238 |
| 8 | Frankfurt am Main International Airport |  | DE | 1177 |
| 9 | Zurich Airport |  | CH | 1141 |
| 10 | La Aurora Airport |  | GT | 1129 |
| 11 | El Dorado International Airport |  | CO | 1060 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1054 |
| 13 | Macau International Airport |  | MO | 1046 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 989 |
| 15 | Chicago O'Hare International Airport |  | US | 941 |
| 16 | Madrid Barajas International Airport |  | ES | 867 |
| 17 | Kuala Lumpur International Airport |  | MY | 858 |
| 18 | Salt Lake City International Airport |  | US | 830 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 823 |
| 20 | Capua Airport |  | IT | 819 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 769 |
| 22 | Malpensa International Airport |  | IT | 764 |
| 23 | Bengaluru International Airport |  | IN | 761 |
| 24 | Charles de Gaulle International Airport |  | FR | 760 |
| 25 | Charlotte/Douglas International Airport |  | US | 751 |
| 26 | Congonhas Airport |  | BR | 748 |
| 27 | Daniel K Inouye International Airport |  | US | 690 |
| 28 | Tenerife Norte Airport |  | ES | 688 |
| 29 | Ninoy Aquino International Airport |  | PH | 665 |
| 30 | Barcelona International Airport |  | ES | 658 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 652 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 630 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 627 |
| 34 | Amsterdam Airport Schiphol |  | NL | 610 |
| 35 | Vitoria/Foronda Airport |  | ES | 606 |
| 36 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 37 | Don Mueang International Airport |  | TH | 601 |
| 38 | Calgary International Airport |  | CA | 580 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 572 |
| 40 | O. R. Tambo International Airport |  | ZA | 554 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 512 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 360 | 21m | 244 km | 1,515.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 265 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 263 | 24m | 225 km | 1,020.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 251 | 14m | 114 km | 492.3 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 243 | 1h 26m | 910 km | 3,813.2 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 242 | 28m | 304 km | 1,268.6 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 223 | 1h 10m | 770 km | 2,962.4 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 209 | 19m | 165 km | 594.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 195 | 26m | 275 km | 924.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 155 | 20m | 99 km | 265.5 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 146 | 27m | 215 km | 540.7 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 142 | 44m | 452 km | 1,106.7 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 141 | 22m | 55 km | 134.0 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 140 | 27m | 152 km | 365.9 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 129 | 20m | 147 km | 326.4 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 129 | 13m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 127 | 18m | 144 km | 315.9 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 124 | 1h 39m | 1,156 km | 2,473.8 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 124 | 1h 1m | 695 km | 1,486.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 117 | 1h 43m | 1,423 km | 2,871.4 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 115 | 1h 18m | 961 km | 1,906.2 t |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N24143 |  | Merrill Field (PAMR) | Grand Home Airport (AK99) | 2026-05-30 23:05 UTC | 2026-05-30 23:19 UTC | 13m |
| SKW4309 | SkyWest Airlines | Salt Lake City International Airport (KSLC) | Huskey Airport (ID72) | 2026-05-30 22:49 UTC | 2026-05-30 23:18 UTC | 29m |
| WXQ | WXQ | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-05-30 23:01 UTC | 2026-05-30 23:13 UTC | 11m |
| N88765 |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-30 22:46 UTC | 2026-05-30 23:07 UTC | 21m |
| N959LA |  | Long Beach (Daugherty Field) Airport (KLGB) | Whiteman Airport (KWHP) | 2026-05-30 22:21 UTC | 2026-05-30 23:06 UTC | 45m |
| N51168 |  | II34 (II34) | II34 (II34) | 2026-05-30 22:37 UTC | 2026-05-30 23:06 UTC | 28m |
| N801AG |  | KA09 (KA09) | Lake Havasu City Airport (KHII) | 2026-05-30 22:49 UTC | 2026-05-30 23:05 UTC | 15m |
| N931PA |  | Falcon Field (KFFZ) | Rimrock Airport (48AZ) | 2026-05-30 22:34 UTC | 2026-05-30 23:01 UTC | 26m |
| PDT6118 | PDT | Charlotte/Douglas International Airport (KCLT) | MS66 (MS66) | 2026-05-30 21:23 UTC | 2026-05-30 22:41 UTC | 1h 17m |
| EJA347 | EJA | Borges - Clarksburg Airport (CN13) | Oakland San Francisco Bay Airport (KOAK) | 2026-05-30 22:18 UTC | 2026-05-30 22:40 UTC | 21m |
| N310AW |  | Holenthawall Airport (3TN9) | Dickson Municipal Airport (KM02) | 2026-05-30 22:22 UTC | 2026-05-30 22:39 UTC | 16m |
| N400WF |  | Colonel James Jabara Airport (KAAO) | 97MO (97MO) | 2026-05-30 21:58 UTC | 2026-05-30 22:38 UTC | 39m |
| N86AW |  | Music Mountain Air Ranch Airport (68AZ) | Grand Canyon West Airport (K1G4) | 2026-05-30 22:20 UTC | 2026-05-30 22:37 UTC | 16m |
| 8089E |  | Gulf Shores International/Jack Edwards Field (KJKA) | Gulf Shores International/Jack Edwards Field (KJKA) | 2026-05-30 22:34 UTC | 2026-05-30 22:34 UTC | 0m |
| JZA138 | JZA | Olds-Didsbury Airport (CEA3) | Wetaskiwin Regional Airport (CEX3) | 2026-05-30 22:18 UTC | 2026-05-30 22:34 UTC | 15m |
| JRE851 | JRE | William P Hobby Airport (KHOU) | II14 (II14) | 2026-05-30 20:29 UTC | 2026-05-30 22:33 UTC | 2h 3m |
| N88765 |  | Talkeetna Airport (PATK) | Talkeetna Airport (PATK) | 2026-05-30 21:35 UTC | 2026-05-30 22:33 UTC | 58m |
| N1039T |  | William B Greene Jr Regional Airport (K0A9) | TN62 (TN62) | 2026-05-30 22:19 UTC | 2026-05-30 22:32 UTC | 12m |
| N616EA |  | Felts Field (KSFF) | Vancouver International Airport (CYVR) | 2026-05-30 21:16 UTC | 2026-05-30 22:31 UTC | 1h 14m |
| CGSSC | CGS | Vancouver International Airport (CYVR) | Victoria International Airport (CYYJ) | 2026-05-30 22:01 UTC | 2026-05-30 22:30 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
