# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_19:18:17_UTC-green)

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

**Latest saved flight:** 2026-05-16 19:18:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-16 19:18:17 UTC

- **85,163** saved flights
- **30,613** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **85,163** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,049,921.7 tonnes** estimated CO2 emissions
- **60,865,026 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3649 |
| 2 | SkyWest Airlines | 3144 |
| 3 | IndiGo | 1835 |
| 4 | EJA | 1602 |
| 5 | American Airlines | 1304 |
| 6 | Southwest Airlines | 1240 |
| 7 | Lufthansa | 1083 |
| 8 | ENY | 1057 |
| 9 | Delta Air Lines | 928 |
| 10 | Vueling | 807 |
| 11 | LATAM Airlines | 771 |
| 12 | AXM | 769 |
| 13 | WIF | 734 |
| 14 | AZU | 668 |
| 15 | Swiss International | 660 |
| 16 | All Nippon Airways | 659 |
| 17 | LXJ | 624 |
| 18 | QLK | 620 |
| 19 | Alaska Airlines | 602 |
| 20 | easyJet | 560 |
| 21 | EJU | 538 |
| 22 | AEE | 535 |
| 23 | Cathay Pacific | 533 |
| 24 | VIV | 512 |
| 25 | Air France | 498 |
| 26 | Japan Airlines | 474 |
| 27 | CXK | 451 |
| 28 | AXB | 450 |
| 29 | MXY | 426 |
| 30 | United Airlines | 418 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 69783 |
| 2 | 🇪🇸 ES | 6018 |
| 3 | 🇮🇳 IN | 5747 |
| 4 | 🇦🇺 AU | 5418 |
| 5 | 🇩🇪 DE | 4748 |
| 6 | 🇧🇷 BR | 4692 |
| 7 | 🇮🇹 IT | 4690 |
| 8 | 🇯🇵 JP | 4258 |
| 9 | 🇨🇦 CA | 4234 |
| 10 | 🇬🇧 GB | 3625 |
| 11 | 🇫🇷 FR | 3386 |
| 12 | 🇨🇴 CO | 2860 |
| 13 | 🇲🇽 MX | 2612 |
| 14 | 🇬🇷 GR | 2473 |
| 15 | 🇳🇴 NO | 2374 |
| 16 | 🇨🇭 CH | 2242 |
| 17 | 🇲🇾 MY | 1929 |
| 18 | 🇿🇦 ZA | 1603 |
| 19 | 🇹🇷 TR | 1519 |
| 20 | 🇳🇿 NZ | 1490 |
| 21 | 🇹🇭 TH | 1475 |
| 22 | 🇵🇱 PL | 1414 |
| 23 | 🇵🇭 PH | 1334 |
| 24 | 🇰🇷 KR | 1312 |
| 25 | 🇬🇹 GT | 1286 |
| 26 | 🇲🇦 MA | 989 |
| 27 | 🇲🇴 MO | 983 |
| 28 | 🇲🇪 ME | 887 |
| 29 | 🇳🇱 NL | 866 |
| 30 | 🇭🇷 HR | 760 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1857 |
| 2 | Denver International Airport |  | US | 1426 |
| 3 | Tokyo International Airport |  | JP | 1423 |
| 4 | Indira Gandhi International Airport |  | IN | 1230 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1189 |
| 6 | Frankfurt am Main International Airport |  | DE | 1093 |
| 7 | Harry Reid International Airport |  | US | 1073 |
| 8 | Zurich Airport |  | CH | 1012 |
| 9 | Macau International Airport |  | MO | 983 |
| 10 | La Aurora Airport |  | GT | 975 |
| 11 | Guaymaral Airport |  | CO | 970 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 941 |
| 13 | El Dorado International Airport |  | CO | 918 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 856 |
| 15 | Chicago O'Hare International Airport |  | US | 822 |
| 16 | Madrid Barajas International Airport |  | ES | 776 |
| 17 | Kuala Lumpur International Airport |  | MY | 766 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 735 |
| 19 | Salt Lake City International Airport |  | US | 707 |
| 20 | Malpensa International Airport |  | IT | 707 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 707 |
| 22 | Bengaluru International Airport |  | IN | 699 |
| 23 | Capua Airport |  | IT | 696 |
| 24 | Charles de Gaulle International Airport |  | FR | 663 |
| 25 | Charlotte/Douglas International Airport |  | US | 659 |
| 26 | Congonhas Airport |  | BR | 659 |
| 27 | Daniel K Inouye International Airport |  | US | 620 |
| 28 | Tenerife Norte Airport |  | ES | 617 |
| 29 | Ninoy Aquino International Airport |  | PH | 611 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 594 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 579 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 569 |
| 33 | Barcelona International Airport |  | ES | 569 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 549 |
| 35 | Vitoria/Foronda Airport |  | ES | 540 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 536 |
| 37 | Don Mueang International Airport |  | TH | 534 |
| 38 | Amsterdam Airport Schiphol |  | NL | 526 |
| 39 | O. R. Tambo International Airport |  | ZA | 506 |
| 40 | Calgary International Airport |  | CA | 498 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 402 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 315 | 21m | 244 km | 1,326.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 275 | 1h 7m | 706 km | 3,348.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 240 | 24m | 225 km | 931.1 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 225 | 1h 26m | 910 km | 3,530.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 224 | 28m | 304 km | 1,174.3 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 219 | 14m | 114 km | 429.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 217 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 199 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 193 | 1h 11m | 770 km | 2,563.9 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 192 | 19m | 165 km | 546.1 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 178 | 26m | 275 km | 843.5 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 146 | 21m | 99 km | 250.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 133 | 31m | 369 km | 846.6 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 128 | 27m | 152 km | 334.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 126 | 27m | 215 km | 466.7 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 125 | 20m | 147 km | 316.3 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 122 | 14m | 154 km | 323.3 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 122 | 23m | 55 km | 116.0 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 121 | 20m | 250 km | 522.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 115 | 1h 2m | 695 km | 1,378.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 108 | 1h 43m | 1,423 km | 2,650.5 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 108 | 13m | - | - |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 108 | 18m | 144 km | 268.6 t |
| 28 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 104 | 12m | - | - |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 103 | 1h 52m | 1,304 km | 2,317.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1590V |  | Dupage Airport (KDPA) | Lake In The Hills Airport (K3CK) | 2026-05-16 18:50 UTC | 2026-05-16 19:18 UTC | 28m |
| N272LP |  | Essex County Airport (KCDW) | Ocean County Airport (KMJX) | 2026-05-16 17:53 UTC | 2026-05-16 19:17 UTC | 1h 23m |
| BCS548 | BCS | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-05-16 15:00 UTC | 2026-05-16 19:13 UTC | 4h 13m |
| N24775 |  | Livermore Municipal Airport (KLVK) | Buchanan Field (KCCR) | 2026-05-16 18:57 UTC | 2026-05-16 19:12 UTC | 15m |
| CAP4240 | CAP | Tyler Pounds Regional Airport (KTYR) | TX24 (TX24) | 2026-05-16 19:01 UTC | 2026-05-16 19:12 UTC | 10m |
| N51582 |  | Gwinnett County/Briscoe Field (KLZU) | Cox Field (30GA) | 2026-05-16 18:45 UTC | 2026-05-16 19:11 UTC | 26m |
| N941SC |  | Fort Worth Spinks Airport (KFWS) | Fort Worth Meacham International Airport (KFTW) | 2026-05-16 18:49 UTC | 2026-05-16 19:10 UTC | 21m |
| CXK678 | CXK | Santa Barbara Municipal Airport (KSBA) | Riverside Airport (KRAL) | 2026-05-16 17:59 UTC | 2026-05-16 19:10 UTC | 1h 11m |
| N82769 |  | Big Lake Airport (PAGQ) | Little Susitna Airport (8AK6) | 2026-05-16 18:08 UTC | 2026-05-16 19:09 UTC | 1h 0m |
| N2CK |  | William P Gwinn Airport (06FA) | William P Gwinn Airport (06FA) | 2026-05-16 18:52 UTC | 2026-05-16 19:04 UTC | 11m |
| EVA095 | EVA Air | Taiwan Taoyuan International Airport (RCTP) | Chanmyathazi Airport (VYCZ) | 2026-05-16 15:41 UTC | 2026-05-16 19:03 UTC | 3h 21m |
| JCO655 | JCO | Indira Gandhi International Airport (VIDP) | Jammu Airport (VIJU) | 2026-05-16 18:30 UTC | 2026-05-16 19:02 UTC | 32m |
| N920AW |  | Fred Netterville Lumber Company/Wilkinson Commnty Airport (MS57) | Lakefront Airport (KNEW) | 2026-05-16 18:20 UTC | 2026-05-16 19:00 UTC | 39m |
| XBONC | XBO | Tlaxcala Airport (MMTA) | Hermanos Serdan International Airport (MMPB) | 2026-05-16 18:32 UTC | 2026-05-16 18:58 UTC | 26m |
| SKW4609 | SkyWest Airlines | Hartsfield/Jackson Atlanta International Airport (KATL) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-05-16 16:14 UTC | 2026-05-16 18:56 UTC | 2h 42m |
| GOJUMP3 | GOJ | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-05-16 18:33 UTC | 2026-05-16 18:55 UTC | 22m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-16 18:38 UTC | 2026-05-16 18:54 UTC | 15m |
| FIN132 | Finnair | Changi Air Base (WSAC) | Jammu Airport (VIJU) | 2026-05-16 13:43 UTC | 2026-05-16 18:54 UTC | 5h 10m |
| N618GL |  | Hannen Airport (0IA8) | Iowa City Municipal Airport (KIOW) | 2026-05-16 18:33 UTC | 2026-05-16 18:53 UTC | 20m |
| SPTN074 | SPT | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-05-16 18:33 UTC | 2026-05-16 18:53 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
