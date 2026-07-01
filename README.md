# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--01_10:18:09_UTC-green)

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

**Latest saved flight:** 2026-07-01 10:18:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-01 10:18:09 UTC

- **125,135** saved flights
- **42,775** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **125,135** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,511,181.2 tonnes** estimated CO2 emissions
- **87,604,705 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5096 |
| 2 | SkyWest Airlines | 4635 |
| 3 | EJA | 2448 |
| 4 | IndiGo | 2381 |
| 5 | American Airlines | 1934 |
| 6 | Southwest Airlines | 1877 |
| 7 | ENY | 1569 |
| 8 | Delta Air Lines | 1490 |
| 9 | Lufthansa | 1341 |
| 10 | LATAM Airlines | 1126 |
| 11 | Vueling | 1111 |
| 12 | WIF | 1107 |
| 13 | AZU | 1058 |
| 14 | AXM | 996 |
| 15 | LXJ | 969 |
| 16 | Swiss International | 876 |
| 17 | All Nippon Airways | 845 |
| 18 | Alaska Airlines | 820 |
| 19 | easyJet | 797 |
| 20 | QLK | 784 |
| 21 | EJU | 779 |
| 22 | Cathay Pacific | 694 |
| 23 | AEE | 691 |
| 24 | VIV | 683 |
| 25 | Air France | 682 |
| 26 | United Airlines | 669 |
| 27 | CXK | 665 |
| 28 | MXY | 652 |
| 29 | JetBlue | 641 |
| 30 | GLO | 630 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 106774 |
| 2 | 🇪🇸 ES | 8367 |
| 3 | 🇮🇳 IN | 7465 |
| 4 | 🇦🇺 AU | 7320 |
| 5 | 🇧🇷 BR | 6965 |
| 6 | 🇩🇪 DE | 6622 |
| 7 | 🇮🇹 IT | 6603 |
| 8 | 🇨🇦 CA | 6572 |
| 9 | 🇬🇧 GB | 5520 |
| 10 | 🇯🇵 JP | 5504 |
| 11 | 🇫🇷 FR | 4943 |
| 12 | 🇨🇴 CO | 4032 |
| 13 | 🇲🇽 MX | 3633 |
| 14 | 🇬🇷 GR | 3573 |
| 15 | 🇳🇴 NO | 3434 |
| 16 | 🇨🇭 CH | 3197 |
| 17 | 🇹🇷 TR | 2626 |
| 18 | 🇲🇾 MY | 2575 |
| 19 | 🇿🇦 ZA | 2060 |
| 20 | 🇵🇱 PL | 2051 |
| 21 | 🇳🇿 NZ | 2025 |
| 22 | 🇹🇭 TH | 1965 |
| 23 | 🇰🇷 KR | 1946 |
| 24 | 🇵🇭 PH | 1778 |
| 25 | 🇬🇹 GT | 1731 |
| 26 | 🇲🇦 MA | 1344 |
| 27 | 🇲🇪 ME | 1243 |
| 28 | 🇳🇱 NL | 1181 |
| 29 | 🇲🇴 MO | 1181 |
| 30 | 🇧🇸 BS | 1081 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2621 |
| 2 | Denver International Airport |  | US | 2112 |
| 3 | Tokyo International Airport |  | JP | 1818 |
| 4 | Indira Gandhi International Airport |  | IN | 1642 |
| 5 | Harry Reid International Airport |  | US | 1564 |
| 6 | Guaymaral Airport |  | CO | 1520 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1501 |
| 8 | Zurich Airport |  | CH | 1386 |
| 9 | La Aurora Airport |  | GT | 1337 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1334 |
| 11 | Frankfurt am Main International Airport |  | DE | 1294 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1229 |
| 13 | Chicago O'Hare International Airport |  | US | 1210 |
| 14 | Macau International Airport |  | MO | 1181 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1101 |
| 17 | Capua Airport |  | IT | 1064 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1040 |
| 19 | Madrid Barajas International Airport |  | ES | 1035 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1015 |
| 21 | Kuala Lumpur International Airport |  | MY | 1002 |
| 22 | Congonhas Airport |  | BR | 975 |
| 23 | Charlotte/Douglas International Airport |  | US | 944 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 920 |
| 25 | Charles de Gaulle International Airport |  | FR | 910 |
| 26 | Bengaluru International Airport |  | IN | 900 |
| 27 | Malpensa International Airport |  | IT | 863 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 832 |
| 29 | Ninoy Aquino International Airport |  | PH | 824 |
| 30 | Daniel K Inouye International Airport |  | US | 801 |
| 31 | Barcelona International Airport |  | ES | 782 |
| 32 | Tenerife Norte Airport |  | ES | 769 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 764 |
| 34 | Calgary International Airport |  | CA | 736 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 731 |
| 36 | Seattle-Tacoma International Airport |  | US | 724 |
| 37 | Vitoria/Foronda Airport |  | ES | 721 |
| 38 | Scottsdale Airport |  | US | 720 |
| 39 | Amsterdam Airport Schiphol |  | NL | 716 |
| 40 | Viracopos International Airport |  | BR | 711 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 633 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 457 | 21m | 244 km | 1,924.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 324 | 24m | 225 km | 1,257.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 315 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 301 | 1h 10m | 770 km | 3,998.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 298 | 1h 25m | 910 km | 4,676.3 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 242 | 26m | 275 km | 1,146.7 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 233 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 186 | 22m | 55 km | 176.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 179 | 26m | 215 km | 662.9 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 177 | 20m | 99 km | 303.2 t |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 173 | 44m | 241 km | 718.6 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 171 | 27m | 152 km | 446.9 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 160 | 1h 45m | 1,423 km | 3,926.7 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 159 | 31m | 369 km | 1,012.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 157 | 18m | 144 km | 390.5 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 156 | 44m | 452 km | 1,215.8 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 153 | 20m | 250 km | 660.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 146 | 1h 1m | 695 km | 1,750.1 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 143 | 1h 17m | 961 km | 2,370.3 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |
| 29 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 140 | 30m | 49 km | 118.3 t |
| 30 | Calgary International Airport (CYYC) | Moose Jaw Municipal Airport (CJS4) | 136 | 1h 1m | 611 km | 1,434.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HNL24A | HNL | De Kooy Airport (EHKD) | Rotterdam Airport (EHRD) | 2026-07-01 09:50 UTC | 2026-07-01 10:18 UTC | 27m |
| SXBDZ | SXB | Megara Airport (LGMG) | Megara Airport (LGMG) | 2026-07-01 09:50 UTC | 2026-07-01 10:08 UTC | 17m |
| UPS1014 | UPS | Louisville Muhammad Ali International Airport (KSDF) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-01 08:16 UTC | 2026-07-01 10:05 UTC | 1h 49m |
| RA07297 |  | Pulkovo Airport (ULLI) | Pulkovo Airport (ULLI) | 2026-07-01 10:04 UTC | 2026-07-01 10:05 UTC | 1m |
| BNOR | BNO | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-07-01 09:42 UTC | 2026-07-01 09:56 UTC | 14m |
| DMDTR | DMD | Trier-Fohren Airport (EDRT) | Trier-Fohren Airport (EDRT) | 2026-07-01 09:41 UTC | 2026-07-01 09:45 UTC | 4m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-07-01 08:53 UTC | 2026-07-01 09:37 UTC | 44m |
| SWR138 | Swiss International | Zurich Airport (LSZH) | Zhuhai Airport (ZGSD) | 2026-06-30 22:38 UTC | 2026-07-01 09:29 UTC | 10h 51m |
| DLH1VR | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hamburg Airport (EDDH) | 2026-07-01 08:46 UTC | 2026-07-01 09:28 UTC | 42m |
| WIF824 | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-07-01 09:17 UTC | 2026-07-01 09:28 UTC | 10m |
| AFR79NB | Air France | Charles de Gaulle International Airport (LFPG) | Vienna International Airport (LOWW) | 2026-07-01 07:46 UTC | 2026-07-01 09:25 UTC | 1h 39m |
| VLG1812 | Vueling | Barcelona International Airport (LEBL) | Munich International Airport (EDDM) | 2026-07-01 07:28 UTC | 2026-07-01 09:25 UTC | 1h 57m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Zhuhai Airport (ZGSD) | 2026-06-30 22:29 UTC | 2026-07-01 09:24 UTC | 10h 54m |
| AFR88WE | Air France | Charles de Gaulle International Airport (LFPG) | Marseille Provence Airport (LFML) | 2026-07-01 08:28 UTC | 2026-07-01 09:24 UTC | 55m |
| AXM464 | AXM | Kuala Lumpur International Airport (WMKK) | Bentayan Airport (WIPY) | 2026-07-01 08:32 UTC | 2026-07-01 09:22 UTC | 49m |
| CJT591 | CJT | Winnipeg James Armstrong Richardson International Airport (CYWG) | Whitewood Airport (CKY2) | 2026-07-01 08:47 UTC | 2026-07-01 09:19 UTC | 32m |
| IGO7VH | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Birsa Munda Airport (VERC) | 2026-07-01 08:35 UTC | 2026-07-01 09:19 UTC | 44m |
| AXM6494 | AXM | Kota Kinabalu International Airport (WBKK) | Telupid Airport (WBKE) | 2026-07-01 09:06 UTC | 2026-07-01 09:18 UTC | 12m |
| IGO2513 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Kamalpur Airport (VEKM) | 2026-07-01 08:44 UTC | 2026-07-01 09:18 UTC | 33m |
| BEL2NM | Brussels Airlines | Melsbroek Air Base (EBMB) | Václav Havel Airport (LKPR) | 2026-07-01 08:09 UTC | 2026-07-01 09:16 UTC | 1h 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
