# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_16:31:20_UTC-green)

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

**Latest saved flight:** 2026-05-30 16:31:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-30 16:31:20 UTC

- **97,357** saved flights
- **34,213** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **97,357** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,191,346.6 tonnes** estimated CO2 emissions
- **69,063,571 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4087 |
| 2 | SkyWest Airlines | 3615 |
| 3 | IndiGo | 2004 |
| 4 | EJA | 1841 |
| 5 | American Airlines | 1473 |
| 6 | Southwest Airlines | 1410 |
| 7 | ENY | 1195 |
| 8 | Lufthansa | 1166 |
| 9 | Delta Air Lines | 1064 |
| 10 | Vueling | 920 |
| 11 | LATAM Airlines | 872 |
| 12 | WIF | 865 |
| 13 | AXM | 854 |
| 14 | AZU | 786 |
| 15 | LXJ | 741 |
| 16 | Swiss International | 724 |
| 17 | All Nippon Airways | 710 |
| 18 | Alaska Airlines | 674 |
| 19 | QLK | 669 |
| 20 | easyJet | 636 |
| 21 | EJU | 619 |
| 22 | Cathay Pacific | 587 |
| 23 | AEE | 585 |
| 24 | VIV | 575 |
| 25 | Air France | 572 |
| 26 | CXK | 525 |
| 27 | MXY | 515 |
| 28 | Japan Airlines | 497 |
| 29 | AXB | 490 |
| 30 | AIQ | 466 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 80544 |
| 2 | 🇪🇸 ES | 6808 |
| 3 | 🇮🇳 IN | 6329 |
| 4 | 🇦🇺 AU | 5926 |
| 5 | 🇩🇪 DE | 5365 |
| 6 | 🇧🇷 BR | 5364 |
| 7 | 🇮🇹 IT | 5262 |
| 8 | 🇨🇦 CA | 4946 |
| 9 | 🇯🇵 JP | 4604 |
| 10 | 🇬🇧 GB | 4178 |
| 11 | 🇫🇷 FR | 3950 |
| 12 | 🇨🇴 CO | 3389 |
| 13 | 🇲🇽 MX | 2991 |
| 14 | 🇬🇷 GR | 2815 |
| 15 | 🇳🇴 NO | 2740 |
| 16 | 🇨🇭 CH | 2559 |
| 17 | 🇲🇾 MY | 2172 |
| 18 | 🇹🇷 TR | 1816 |
| 19 | 🇿🇦 ZA | 1735 |
| 20 | 🇳🇿 NZ | 1651 |
| 21 | 🇹🇭 TH | 1640 |
| 22 | 🇵🇱 PL | 1589 |
| 23 | 🇰🇷 KR | 1589 |
| 24 | 🇬🇹 GT | 1462 |
| 25 | 🇵🇭 PH | 1457 |
| 26 | 🇲🇦 MA | 1102 |
| 27 | 🇲🇴 MO | 1044 |
| 28 | 🇳🇱 NL | 988 |
| 29 | 🇲🇪 ME | 954 |
| 30 | 🇭🇷 HR | 880 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2104 |
| 2 | Denver International Airport |  | US | 1644 |
| 3 | Tokyo International Airport |  | JP | 1525 |
| 4 | Indira Gandhi International Airport |  | IN | 1371 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1284 |
| 6 | Harry Reid International Airport |  | US | 1245 |
| 7 | Guaymaral Airport |  | CO | 1213 |
| 8 | Frankfurt am Main International Airport |  | DE | 1172 |
| 9 | Zurich Airport |  | CH | 1137 |
| 10 | La Aurora Airport |  | GT | 1122 |
| 11 | El Dorado International Airport |  | CO | 1048 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1047 |
| 13 | Macau International Airport |  | MO | 1044 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 973 |
| 15 | Chicago O'Hare International Airport |  | US | 933 |
| 16 | Madrid Barajas International Airport |  | ES | 863 |
| 17 | Kuala Lumpur International Airport |  | MY | 858 |
| 18 | Salt Lake City International Airport |  | US | 818 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 813 |
| 20 | Capua Airport |  | IT | 806 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 769 |
| 22 | Malpensa International Airport |  | IT | 762 |
| 23 | Charles de Gaulle International Airport |  | FR | 757 |
| 24 | Bengaluru International Airport |  | IN | 757 |
| 25 | Congonhas Airport |  | BR | 743 |
| 26 | Charlotte/Douglas International Airport |  | US | 740 |
| 27 | Daniel K Inouye International Airport |  | US | 688 |
| 28 | Tenerife Norte Airport |  | ES | 682 |
| 29 | Ninoy Aquino International Airport |  | PH | 665 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 651 |
| 31 | Barcelona International Airport |  | ES | 650 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 626 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 623 |
| 34 | Amsterdam Airport Schiphol |  | NL | 607 |
| 35 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 36 | Don Mueang International Airport |  | TH | 601 |
| 37 | Vitoria/Foronda Airport |  | ES | 599 |
| 38 | Calgary International Airport |  | CA | 574 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 572 |
| 40 | O. R. Tambo International Airport |  | ZA | 553 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 501 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 358 | 21m | 244 km | 1,507.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 263 | 24m | 225 km | 1,020.3 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 262 | 9m | - | - |
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
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 115 | 1h 43m | 1,423 km | 2,822.3 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 115 | 1h 18m | 961 km | 1,906.2 t |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N929NX |  | Ted Stevens Anchorage International Airport (PANC) | Wasilla Airport (PAWS) | 2026-05-30 16:14 UTC | 2026-05-30 16:31 UTC | 17m |
| N9525D |  | Warren County/John Lane Field (KI68) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-05-30 16:12 UTC | 2026-05-30 16:30 UTC | 17m |
| N174PM |  | Aero Country Airport (KT31) | TX68 (TX68) | 2026-05-30 16:11 UTC | 2026-05-30 16:25 UTC | 14m |
| CXK183 | CXK | Flying Cloud Airport (KFCM) | Flying Cloud Airport (KFCM) | 2026-05-30 16:08 UTC | 2026-05-30 16:23 UTC | 14m |
| SD1 |  | Tri-County Aerodrome (48TX) | Tri-County Aerodrome (48TX) | 2026-05-30 14:03 UTC | 2026-05-30 16:23 UTC | 2h 19m |
| CONGO63 | CON | Southeast Colorado Regional Airport (KLAA) | Southeast Colorado Regional Airport (KLAA) | 2026-05-30 16:06 UTC | 2026-05-30 16:17 UTC | 11m |
| CXK695 | CXK | Wiley Post Airport (KPWA) | El Reno Regional Airport (KRQO) | 2026-05-30 16:00 UTC | 2026-05-30 16:16 UTC | 15m |
| DIPFM | DIP | Palma De Mallorca Airport (LEPA) | Hoefen Airport (LOIR) | 2026-05-30 14:07 UTC | 2026-05-30 16:10 UTC | 2h 3m |
| SCU47 | SCU | Cherokee Ranch Airport (OK25) | Haskell Airport (K2K9) | 2026-05-30 15:54 UTC | 2026-05-30 16:08 UTC | 13m |
| N7079F |  | Payson Airport (KPAN) | Payson Airport (KPAN) | 2026-05-30 15:44 UTC | 2026-05-30 16:05 UTC | 21m |
| N399AB |  | Pensacola International Airport (KPNS) | Jonesboro Airport (KF88) | 2026-05-30 15:00 UTC | 2026-05-30 16:00 UTC | 59m |
| TCF659 | TCF | Melbourne Orlando International Airport (KMLB) | Palm Beach County Park Airport (KLNA) | 2026-05-30 15:00 UTC | 2026-05-30 15:58 UTC | 58m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-05-30 15:43 UTC | 2026-05-30 15:58 UTC | 15m |
| N175EM |  | Van Nuys Airport (KVNY) | Henderson Executive Airport (KHND) | 2026-05-30 15:10 UTC | 2026-05-30 15:57 UTC | 46m |
| N96FM |  | Santa Fe Regional Airport (KSAF) | Ohkay Owingeh Airport (KE14) | 2026-05-30 15:32 UTC | 2026-05-30 15:57 UTC | 25m |
| N611CA |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-05-30 15:24 UTC | 2026-05-30 15:56 UTC | 31m |
| DFSCM | DFS | Munster-Telgte Airport (EDLT) | Munster-Telgte Airport (EDLT) | 2026-05-30 15:09 UTC | 2026-05-30 15:56 UTC | 46m |
| N8838P |  | Fairfield County Airport (KLHQ) | Fairfield County Airport (KLHQ) | 2026-05-30 15:16 UTC | 2026-05-30 15:54 UTC | 38m |
| N16NW |  | Albuquerque International Sunport Airport (KABQ) | San Miguel Ranch Airport (NM53) | 2026-05-30 13:34 UTC | 2026-05-30 15:54 UTC | 2h 19m |
| EWG8UC | EWG | Palma De Mallorca Airport (LEPA) | Stuttgart Airport (EDDS) | 2026-05-30 14:05 UTC | 2026-05-30 15:53 UTC | 1h 48m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
