# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_21:58:56_UTC-green)

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

**Latest saved flight:** 2026-06-28 21:58:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-28 21:58:56 UTC

- **123,442** saved flights
- **42,338** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **123,442** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,492,242.7 tonnes** estimated CO2 emissions
- **86,506,823 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5051 |
| 2 | SkyWest Airlines | 4566 |
| 3 | EJA | 2401 |
| 4 | IndiGo | 2361 |
| 5 | American Airlines | 1906 |
| 6 | Southwest Airlines | 1850 |
| 7 | ENY | 1548 |
| 8 | Delta Air Lines | 1465 |
| 9 | Lufthansa | 1330 |
| 10 | LATAM Airlines | 1108 |
| 11 | Vueling | 1099 |
| 12 | WIF | 1092 |
| 13 | AZU | 1035 |
| 14 | AXM | 988 |
| 15 | LXJ | 958 |
| 16 | Swiss International | 870 |
| 17 | All Nippon Airways | 832 |
| 18 | Alaska Airlines | 807 |
| 19 | easyJet | 789 |
| 20 | QLK | 778 |
| 21 | EJU | 773 |
| 22 | Cathay Pacific | 689 |
| 23 | AEE | 683 |
| 24 | Air France | 675 |
| 25 | VIV | 672 |
| 26 | United Airlines | 662 |
| 27 | CXK | 653 |
| 28 | MXY | 645 |
| 29 | JetBlue | 621 |
| 30 | GLO | 618 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 105031 |
| 2 | 🇪🇸 ES | 8305 |
| 3 | 🇮🇳 IN | 7401 |
| 4 | 🇦🇺 AU | 7181 |
| 5 | 🇧🇷 BR | 6850 |
| 6 | 🇩🇪 DE | 6578 |
| 7 | 🇮🇹 IT | 6560 |
| 8 | 🇨🇦 CA | 6478 |
| 9 | 🇬🇧 GB | 5443 |
| 10 | 🇯🇵 JP | 5427 |
| 11 | 🇫🇷 FR | 4905 |
| 12 | 🇨🇴 CO | 4031 |
| 13 | 🇲🇽 MX | 3589 |
| 14 | 🇬🇷 GR | 3523 |
| 15 | 🇳🇴 NO | 3401 |
| 16 | 🇨🇭 CH | 3174 |
| 17 | 🇹🇷 TR | 2590 |
| 18 | 🇲🇾 MY | 2557 |
| 19 | 🇿🇦 ZA | 2043 |
| 20 | 🇵🇱 PL | 2028 |
| 21 | 🇳🇿 NZ | 1990 |
| 22 | 🇹🇭 TH | 1932 |
| 23 | 🇰🇷 KR | 1926 |
| 24 | 🇵🇭 PH | 1758 |
| 25 | 🇬🇹 GT | 1708 |
| 26 | 🇲🇦 MA | 1322 |
| 27 | 🇲🇪 ME | 1230 |
| 28 | 🇲🇴 MO | 1176 |
| 29 | 🇳🇱 NL | 1175 |
| 30 | 🇧🇸 BS | 1074 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2595 |
| 2 | Denver International Airport |  | US | 2072 |
| 3 | Tokyo International Airport |  | JP | 1797 |
| 4 | Indira Gandhi International Airport |  | IN | 1631 |
| 5 | Harry Reid International Airport |  | US | 1540 |
| 6 | Guaymaral Airport |  | CO | 1519 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1486 |
| 8 | Zurich Airport |  | CH | 1374 |
| 9 | La Aurora Airport |  | GT | 1319 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1314 |
| 11 | Frankfurt am Main International Airport |  | DE | 1284 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1213 |
| 13 | Chicago O'Hare International Airport |  | US | 1196 |
| 14 | Macau International Airport |  | MO | 1176 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1083 |
| 17 | Capua Airport |  | IT | 1057 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1029 |
| 19 | Madrid Barajas International Airport |  | ES | 1028 |
| 20 | Kuala Lumpur International Airport |  | MY | 993 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 978 |
| 22 | Congonhas Airport |  | BR | 962 |
| 23 | Charlotte/Douglas International Airport |  | US | 930 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 905 |
| 25 | Charles de Gaulle International Airport |  | FR | 903 |
| 26 | Bengaluru International Airport |  | IN | 889 |
| 27 | Malpensa International Airport |  | IT | 853 |
| 28 | Ninoy Aquino International Airport |  | PH | 815 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 811 |
| 30 | Daniel K Inouye International Airport |  | US | 791 |
| 31 | Barcelona International Airport |  | ES | 770 |
| 32 | Tenerife Norte Airport |  | ES | 764 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 751 |
| 34 | Calgary International Airport |  | CA | 725 |
| 35 | Vitoria/Foronda Airport |  | ES | 717 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 714 |
| 37 | Amsterdam Airport Schiphol |  | NL | 712 |
| 38 | Scottsdale Airport |  | US | 711 |
| 39 | Seattle-Tacoma International Airport |  | US | 707 |
| 40 | Don Mueang International Airport |  | TH | 698 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 633 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 448 | 21m | 244 km | 1,886.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 320 | 24m | 225 km | 1,241.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 310 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 296 | 1h 10m | 770 km | 3,932.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 294 | 1h 25m | 910 km | 4,613.5 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 240 | 26m | 275 km | 1,137.3 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 231 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 180 | 22m | 55 km | 171.1 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 178 | 26m | 215 km | 659.2 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 175 | 20m | 99 km | 299.8 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 172 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 170 | 44m | 241 km | 706.1 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 168 | 27m | 152 km | 439.0 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 158 | 1h 44m | 1,423 km | 3,877.6 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 158 | 31m | 369 km | 1,005.7 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 155 | 44m | 452 km | 1,208.0 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 155 | 18m | 144 km | 385.6 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 151 | 20m | 250 km | 652.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 144 | 1h 38m | 1,156 km | 2,872.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 141 | 1h 1m | 695 km | 1,690.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 141 | 1h 17m | 961 km | 2,337.1 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 139 | 13m | - | - |
| 29 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 138 | 29m | 49 km | 116.6 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 135 | 20m | 147 km | 341.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N5036M |  | Santa Barbara Municipal Airport (KSBA) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-06-28 20:57 UTC | 2026-06-28 21:58 UTC | 1h 1m |
| N10SZ |  | Nephi Municipal Airport (KU14) | KU77 (KU77) | 2026-06-28 21:09 UTC | 2026-06-28 21:37 UTC | 28m |
| N272MR |  | Nephi Municipal Airport (KU14) | KU77 (KU77) | 2026-06-28 21:09 UTC | 2026-06-28 21:34 UTC | 24m |
| N88765 |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-28 21:11 UTC | 2026-06-28 21:34 UTC | 22m |
| N3NT |  | Animas Air Park (K00C) | Telluride Regional Airport (KTEX) | 2026-06-28 21:22 UTC | 2026-06-28 21:33 UTC | 10m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-06-28 21:15 UTC | 2026-06-28 21:30 UTC | 14m |
| RPA5699 | Republic Airways | John F Kennedy International Airport (KJFK) | Deale Airport (MD22) | 2026-06-28 20:31 UTC | 2026-06-28 21:30 UTC | 58m |
| SWA1610 | Southwest Airlines | Cancun International Airport (MMUN) | Garner Field (02MD) | 2026-06-28 18:29 UTC | 2026-06-28 21:30 UTC | 3h 1m |
| N442WT |  | Lawton Airport (IA84) | Wadena Municipal Airport (KADC) | 2026-06-28 20:56 UTC | 2026-06-28 21:27 UTC | 30m |
| N562LD |  | City Of Colorado Springs Municipal Airport (KCOS) | Baker & Hall Airport (77CL) | 2026-06-28 19:12 UTC | 2026-06-28 21:25 UTC | 2h 13m |
| LTA316 | LTA | Moton Field Municipal Airport (K06A) | AL25 (AL25) | 2026-06-28 21:10 UTC | 2026-06-28 21:23 UTC | 12m |
| N540AW |  | Palo Alto Airport (KPAO) | Las Trancas Airport (17CL) | 2026-06-28 21:12 UTC | 2026-06-28 21:21 UTC | 9m |
| N530JL |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-06-28 21:02 UTC | 2026-06-28 21:20 UTC | 17m |
| N961MM |  | Indianapolis Executive Airport (KTYQ) | Laramie Regional Airport (KLAR) | 2026-06-28 19:09 UTC | 2026-06-28 21:19 UTC | 2h 10m |
| WSN9 | WSN | Albuquerque International Sunport Airport (KABQ) | Taos Regional Airport (KSKX) | 2026-06-28 20:53 UTC | 2026-06-28 21:17 UTC | 24m |
| N488GC |  | Fort Morgan Municipal Airport (KFMM) | Fort Morgan Municipal Airport (KFMM) | 2026-06-28 21:03 UTC | 2026-06-28 21:17 UTC | 13m |
| VLG858A | Vueling | Barcelona International Airport (LEBL) | Leon Airport (LELN) | 2026-06-28 20:19 UTC | 2026-06-28 21:15 UTC | 56m |
| RYR2M | Ryanair | London Luton Airport (EGGW) | Darlowek Naval Air Base (EPDA) | 2026-06-28 19:49 UTC | 2026-06-28 21:15 UTC | 1h 25m |
| LXJ327 | LXJ | Francis S Gabreski Airport (KFOK) | Rocky Mountain Metro Airport (KBJC) | 2026-06-28 17:15 UTC | 2026-06-28 21:15 UTC | 4h 0m |
| N711HA |  | Southfork Airport (23ID) | Cascade Airport (KU70) | 2026-06-28 21:03 UTC | 2026-06-28 21:15 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
