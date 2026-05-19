# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_22:01:25_UTC-green)

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

**Latest saved flight:** 2026-05-19 22:01:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-19 22:01:25 UTC

- **88,627** saved flights
- **31,668** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **88,627** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,096,768.8 tonnes** estimated CO2 emissions
- **63,580,799 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3797 |
| 2 | SkyWest Airlines | 3289 |
| 3 | IndiGo | 1876 |
| 4 | EJA | 1679 |
| 5 | American Airlines | 1360 |
| 6 | Southwest Airlines | 1288 |
| 7 | Lufthansa | 1112 |
| 8 | ENY | 1095 |
| 9 | Delta Air Lines | 973 |
| 10 | Vueling | 847 |
| 11 | LATAM Airlines | 796 |
| 12 | AXM | 786 |
| 13 | WIF | 765 |
| 14 | AZU | 702 |
| 15 | Swiss International | 682 |
| 16 | All Nippon Airways | 669 |
| 17 | LXJ | 652 |
| 18 | Alaska Airlines | 628 |
| 19 | QLK | 627 |
| 20 | easyJet | 586 |
| 21 | EJU | 569 |
| 22 | Cathay Pacific | 566 |
| 23 | AEE | 547 |
| 24 | VIV | 532 |
| 25 | Air France | 519 |
| 26 | Japan Airlines | 479 |
| 27 | CXK | 466 |
| 28 | AXB | 458 |
| 29 | MXY | 452 |
| 30 | AIQ | 431 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 72900 |
| 2 | 🇪🇸 ES | 6293 |
| 3 | 🇮🇳 IN | 5886 |
| 4 | 🇦🇺 AU | 5514 |
| 5 | 🇩🇪 DE | 4922 |
| 6 | 🇮🇹 IT | 4904 |
| 7 | 🇧🇷 BR | 4863 |
| 8 | 🇨🇦 CA | 4431 |
| 9 | 🇯🇵 JP | 4344 |
| 10 | 🇬🇧 GB | 3776 |
| 11 | 🇫🇷 FR | 3550 |
| 12 | 🇨🇴 CO | 3035 |
| 13 | 🇲🇽 MX | 2752 |
| 14 | 🇬🇷 GR | 2561 |
| 15 | 🇳🇴 NO | 2459 |
| 16 | 🇨🇭 CH | 2334 |
| 17 | 🇲🇾 MY | 1974 |
| 18 | 🇿🇦 ZA | 1637 |
| 19 | 🇹🇷 TR | 1605 |
| 20 | 🇳🇿 NZ | 1531 |
| 21 | 🇹🇭 TH | 1519 |
| 22 | 🇵🇱 PL | 1472 |
| 23 | 🇰🇷 KR | 1365 |
| 24 | 🇵🇭 PH | 1357 |
| 25 | 🇬🇹 GT | 1332 |
| 26 | 🇲🇴 MO | 1025 |
| 27 | 🇲🇦 MA | 1024 |
| 28 | 🇲🇪 ME | 914 |
| 29 | 🇳🇱 NL | 899 |
| 30 | 🇭🇷 HR | 799 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1942 |
| 2 | Denver International Airport |  | US | 1488 |
| 3 | Tokyo International Airport |  | JP | 1449 |
| 4 | Indira Gandhi International Airport |  | IN | 1271 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1210 |
| 6 | Harry Reid International Airport |  | US | 1129 |
| 7 | Frankfurt am Main International Airport |  | DE | 1119 |
| 8 | Zurich Airport |  | CH | 1055 |
| 9 | Guaymaral Airport |  | CO | 1040 |
| 10 | Macau International Airport |  | MO | 1025 |
| 11 | La Aurora Airport |  | GT | 1012 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 980 |
| 13 | El Dorado International Airport |  | CO | 965 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 905 |
| 15 | Chicago O'Hare International Airport |  | US | 857 |
| 16 | Madrid Barajas International Airport |  | ES | 805 |
| 17 | Kuala Lumpur International Airport |  | MY | 784 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 763 |
| 19 | Capua Airport |  | IT | 749 |
| 20 | Salt Lake City International Airport |  | US | 741 |
| 21 | Malpensa International Airport |  | IT | 725 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 717 |
| 23 | Bengaluru International Airport |  | IN | 708 |
| 24 | Charles de Gaulle International Airport |  | FR | 691 |
| 25 | Charlotte/Douglas International Airport |  | US | 683 |
| 26 | Congonhas Airport |  | BR | 679 |
| 27 | Daniel K Inouye International Airport |  | US | 650 |
| 28 | Tenerife Norte Airport |  | ES | 648 |
| 29 | Ninoy Aquino International Airport |  | PH | 622 |
| 30 | Barcelona International Airport |  | ES | 600 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 597 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 586 |
| 34 | Vitoria/Foronda Airport |  | ES | 567 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 558 |
| 37 | Don Mueang International Airport |  | TH | 553 |
| 38 | Amsterdam Airport Schiphol |  | NL | 550 |
| 39 | Calgary International Airport |  | CA | 525 |
| 40 | O. R. Tambo International Airport |  | ZA | 518 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 426 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 331 | 21m | 244 km | 1,393.8 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 277 | 1h 7m | 706 km | 3,372.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 243 | 24m | 225 km | 942.7 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 231 | 1h 26m | 910 km | 3,624.9 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 229 | 14m | 114 km | 449.1 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 227 | 28m | 304 km | 1,190.0 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 226 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 202 | 1h 10m | 770 km | 2,683.4 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 194 | 19m | 165 km | 551.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 184 | 26m | 275 km | 871.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 148 | 21m | 99 km | 253.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 136 | 31m | 369 km | 865.7 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 129 | 27m | 215 km | 477.8 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 125 | 14m | 154 km | 331.2 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 125 | 23m | 55 km | 118.8 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 123 | 20m | 250 km | 531.3 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 114 | 13m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 114 | 18m | 144 km | 283.6 t |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 108 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 107 | 1h 41m | 1,156 km | 2,134.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 107 | 1h 18m | 961 km | 1,773.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UAL15 | United Airlines | London Heathrow Airport (EGLL) | Newark Liberty International Airport (KEWR) | 2026-05-19 14:46 UTC | 2026-05-19 22:01 UTC | 7h 14m |
| N248SF |  | Dupage Airport (KDPA) | Willadae Farms Airport (4LL7) | 2026-05-19 21:45 UTC | 2026-05-19 21:59 UTC | 13m |
| N1213P |  | Prescott Regional/Ernest A Love Field (KPRC) | Phoenix Sky Harbor International Airport (KPHX) | 2026-05-19 21:23 UTC | 2026-05-19 21:55 UTC | 32m |
| N875CF |  | Page Field (KFMY) | La Belle Municipal Airport (KX14) | 2026-05-19 21:36 UTC | 2026-05-19 21:55 UTC | 19m |
| 0   P |  | Jacksonville Nas (Towers Field) Airport (KNIP) | Wayne Executive Jetport Airport (KGWW) | 2026-05-19 20:38 UTC | 2026-05-19 21:49 UTC | 1h 11m |
| ZHJ | ZHJ | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-05-19 21:29 UTC | 2026-05-19 21:49 UTC | 19m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-05-19 17:32 UTC | 2026-05-19 21:48 UTC | 4h 15m |
| N605FF |  | Riverside Airport (KRAL) | Santa Monica Municipal Airport (KSMO) | 2026-05-19 21:07 UTC | 2026-05-19 21:48 UTC | 40m |
| N19AK |  | Kodiak Airport (PADQ) | Kodiak Municipal Airport (PAKD) | 2026-05-19 21:37 UTC | 2026-05-19 21:46 UTC | 8m |
| LXJ345 | LXJ | John Wayne/Orange County Airport (KSNA) | San Francisco International Airport (KSFO) | 2026-05-19 20:36 UTC | 2026-05-19 21:42 UTC | 1h 6m |
| N441HL |  | Long Beach (Daugherty Field) Airport (KLGB) | Meadows Field (KBFL) | 2026-05-19 20:59 UTC | 2026-05-19 21:39 UTC | 39m |
| N563DJ |  | Flying R Airport (11UT) | Flying R Airport (11UT) | 2026-05-19 14:01 UTC | 2026-05-19 21:38 UTC | 7h 36m |
| JANET27 | JAN | Harry Reid International Airport (KLAS) | NV11 (NV11) | 2026-05-19 21:19 UTC | 2026-05-19 21:35 UTC | 15m |
| UPS4 | UPS | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-05-19 10:12 UTC | 2026-05-19 21:34 UTC | 11h 21m |
| N500JJ |  | Mc Ghee Tyson Airport (KTYS) | Nelson Airfield (TN99) | 2026-05-19 21:19 UTC | 2026-05-19 21:33 UTC | 14m |
| ZKSXG | ZKS | Hood Airport (NZMS) | Hood Airport (NZMS) | 2026-05-19 19:33 UTC | 2026-05-19 21:32 UTC | 1h 59m |
| N371DS |  | Colonel James Jabara Airport (KAAO) | Augusta Municipal Airport (K3AU) | 2026-05-19 20:25 UTC | 2026-05-19 21:32 UTC | 1h 6m |
| N9044D |  | Ralph Wien Memorial Airport (PAOT) | Ralph Wien Memorial Airport (PAOT) | 2026-05-19 21:19 UTC | 2026-05-19 21:29 UTC | 9m |
| N554SC |  | Christmas Flying Service Airport (MS03) | Christmas Flying Service Airport (MS03) | 2026-05-19 17:39 UTC | 2026-05-19 21:29 UTC | 3h 50m |
| FHBVG | FHB | Dax Seyresse Airport (LFBY) | Dax Seyresse Airport (LFBY) | 2026-05-19 20:54 UTC | 2026-05-19 21:27 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
