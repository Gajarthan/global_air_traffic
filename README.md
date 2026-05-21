# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_00:01:52_UTC-green)

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

**Latest saved flight:** 2026-05-21 00:01:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-21 00:01:52 UTC

- **89,621** saved flights
- **31,960** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **89,621** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,109,004.0 tonnes** estimated CO2 emissions
- **64,290,089 km** total distance flown
- **871 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3840 |
| 2 | SkyWest Airlines | 3333 |
| 3 | IndiGo | 1887 |
| 4 | EJA | 1696 |
| 5 | American Airlines | 1368 |
| 6 | Southwest Airlines | 1300 |
| 7 | Lufthansa | 1116 |
| 8 | ENY | 1106 |
| 9 | Delta Air Lines | 986 |
| 10 | Vueling | 853 |
| 11 | LATAM Airlines | 807 |
| 12 | AXM | 790 |
| 13 | WIF | 776 |
| 14 | AZU | 713 |
| 15 | Swiss International | 688 |
| 16 | All Nippon Airways | 673 |
| 17 | LXJ | 668 |
| 18 | Alaska Airlines | 635 |
| 19 | QLK | 634 |
| 20 | easyJet | 589 |
| 21 | Cathay Pacific | 578 |
| 22 | EJU | 576 |
| 23 | AEE | 552 |
| 24 | VIV | 535 |
| 25 | Air France | 524 |
| 26 | Japan Airlines | 480 |
| 27 | CXK | 470 |
| 28 | AXB | 459 |
| 29 | MXY | 457 |
| 30 | AIQ | 433 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 73824 |
| 2 | 🇪🇸 ES | 6350 |
| 3 | 🇮🇳 IN | 5916 |
| 4 | 🇦🇺 AU | 5579 |
| 5 | 🇩🇪 DE | 4956 |
| 6 | 🇮🇹 IT | 4955 |
| 7 | 🇧🇷 BR | 4920 |
| 8 | 🇨🇦 CA | 4492 |
| 9 | 🇯🇵 JP | 4371 |
| 10 | 🇬🇧 GB | 3820 |
| 11 | 🇫🇷 FR | 3592 |
| 12 | 🇨🇴 CO | 3075 |
| 13 | 🇲🇽 MX | 2776 |
| 14 | 🇬🇷 GR | 2582 |
| 15 | 🇳🇴 NO | 2487 |
| 16 | 🇨🇭 CH | 2355 |
| 17 | 🇲🇾 MY | 1985 |
| 18 | 🇿🇦 ZA | 1641 |
| 19 | 🇹🇷 TR | 1629 |
| 20 | 🇳🇿 NZ | 1548 |
| 21 | 🇹🇭 TH | 1523 |
| 22 | 🇵🇱 PL | 1480 |
| 23 | 🇰🇷 KR | 1400 |
| 24 | 🇵🇭 PH | 1379 |
| 25 | 🇬🇹 GT | 1339 |
| 26 | 🇲🇴 MO | 1034 |
| 27 | 🇲🇦 MA | 1032 |
| 28 | 🇲🇪 ME | 917 |
| 29 | 🇳🇱 NL | 907 |
| 30 | 🇭🇷 HR | 808 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1963 |
| 2 | Denver International Airport |  | US | 1507 |
| 3 | Tokyo International Airport |  | JP | 1457 |
| 4 | Indira Gandhi International Airport |  | IN | 1279 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1216 |
| 6 | Harry Reid International Airport |  | US | 1145 |
| 7 | Frankfurt am Main International Airport |  | DE | 1125 |
| 8 | Zurich Airport |  | CH | 1066 |
| 9 | Guaymaral Airport |  | CO | 1049 |
| 10 | Macau International Airport |  | MO | 1034 |
| 11 | La Aurora Airport |  | GT | 1019 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 992 |
| 13 | El Dorado International Airport |  | CO | 978 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 913 |
| 15 | Chicago O'Hare International Airport |  | US | 867 |
| 16 | Madrid Barajas International Airport |  | ES | 814 |
| 17 | Kuala Lumpur International Airport |  | MY | 787 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 770 |
| 19 | Capua Airport |  | IT | 761 |
| 20 | Salt Lake City International Airport |  | US | 756 |
| 21 | Malpensa International Airport |  | IT | 727 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 726 |
| 23 | Bengaluru International Airport |  | IN | 712 |
| 24 | Charles de Gaulle International Airport |  | FR | 698 |
| 25 | Congonhas Airport |  | BR | 690 |
| 26 | Charlotte/Douglas International Airport |  | US | 689 |
| 27 | Daniel K Inouye International Airport |  | US | 656 |
| 28 | Tenerife Norte Airport |  | ES | 654 |
| 29 | Ninoy Aquino International Airport |  | PH | 634 |
| 30 | Barcelona International Airport |  | ES | 602 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 600 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 588 |
| 34 | Vitoria/Foronda Airport |  | ES | 568 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 567 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 37 | Amsterdam Airport Schiphol |  | NL | 557 |
| 38 | Don Mueang International Airport |  | TH | 555 |
| 39 | Calgary International Airport |  | CA | 533 |
| 40 | O. R. Tambo International Airport |  | ZA | 519 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 429 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 333 | 21m | 244 km | 1,402.2 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 277 | 1h 7m | 706 km | 3,372.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 247 | 24m | 225 km | 958.2 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 234 | 14m | 114 km | 459.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 231 | 1h 26m | 910 km | 3,624.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 229 | 28m | 304 km | 1,200.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 229 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 204 | 1h 10m | 770 km | 2,710.0 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 194 | 19m | 165 km | 551.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 185 | 26m | 275 km | 876.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 148 | 21m | 99 km | 253.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 137 | 31m | 369 km | 872.0 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 132 | 22m | 55 km | 125.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 131 | 27m | 215 km | 485.2 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 126 | 14m | 154 km | 333.8 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 123 | 20m | 250 km | 531.3 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 116 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 116 | 18m | 144 km | 288.5 t |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 109 | 1h 18m | 961 km | 1,806.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 109 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 107 | 1h 41m | 1,156 km | 2,134.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZJO | ZJO | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-05-20 23:32 UTC | 2026-05-21 00:01 UTC | 29m |
| N92AK |  | Homer Airport (PAHO) | Homer Airport (PAHO) | 2026-05-20 23:47 UTC | 2026-05-20 23:59 UTC | 11m |
| N114PT |  | Norman Y Mineta San Jose International Airport (KSJC) | Palo Alto Airport (KPAO) | 2026-05-20 23:43 UTC | 2026-05-20 23:50 UTC | 6m |
| TYPN | TYP | West Sale Airport (YWSL) | Latrobe Valley Airport (YLTV) | 2026-05-20 23:23 UTC | 2026-05-20 23:49 UTC | 26m |
| N73574 |  | Dupage Airport (KDPA) | 95LL (95LL) | 2026-05-20 23:10 UTC | 2026-05-20 23:48 UTC | 37m |
| LW11 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-05-20 21:20 UTC | 2026-05-20 23:45 UTC | 2h 24m |
| TROY328 | TRO | San Clemente Island Nalf Airport (KNUC) | San Clemente Island Nalf Airport (KNUC) | 2026-05-20 23:27 UTC | 2026-05-20 23:44 UTC | 16m |
| N682RV |  | Cincinnati Municipal/Lunken Field (KLUK) | Fetters Construction Airport (PA70) | 2026-05-20 22:35 UTC | 2026-05-20 23:44 UTC | 1h 9m |
| N540M |  | Dupage Airport (KDPA) | Dane County Regional/Truax Field (KMSN) | 2026-05-20 23:19 UTC | 2026-05-20 23:41 UTC | 22m |
| BRG622 | BRG | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-05-20 22:51 UTC | 2026-05-20 23:38 UTC | 46m |
| N543JW |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-05-20 23:15 UTC | 2026-05-20 23:38 UTC | 23m |
| N72NG |  | Montgomery-Gibbs Executive Airport (KMYF) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-05-20 23:03 UTC | 2026-05-20 23:35 UTC | 32m |
| N137TM |  | Logan-Cache Airport (KLGU) | Wendover Airport (KENV) | 2026-05-20 22:48 UTC | 2026-05-20 23:30 UTC | 41m |
| N739BZ |  | Cheyenne Regional/Jerry Olson Field (KCYS) | Vowers Ranch Airport (WY29) | 2026-05-20 23:16 UTC | 2026-05-20 23:28 UTC | 11m |
| N738GB |  | Kingfield Airport (6IL6) | Colonial Acres Airport (4LL8) | 2026-05-20 23:20 UTC | 2026-05-20 23:25 UTC | 5m |
| N76SJ |  | Carson City Airport (KCXP) | Hayward Executive Airport (KHWD) | 2026-05-20 22:39 UTC | 2026-05-20 23:24 UTC | 45m |
| CSN304 | China Southern | London Heathrow Airport (EGLL) | Ukhta Airport (UUYH) | 2026-05-19 21:31 UTC | 2026-05-20 23:20 UTC | 25h 48m |
| N891QS |  | Bradshaw Army Airfield (PHSF) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-05-20 23:02 UTC | 2026-05-20 23:17 UTC | 15m |
| BAW34 | British Airways | Kuala Lumpur International Airport (WMKK) | UG28 (UG28) | 2026-05-20 15:10 UTC | 2026-05-20 23:17 UTC | 8h 6m |
| WSN8 | WSN | Albuquerque International Sunport Airport (KABQ) | Casas Adobes Airpark (NM69) | 2026-05-20 22:34 UTC | 2026-05-20 23:16 UTC | 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
