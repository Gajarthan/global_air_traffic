# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_19:50:18_UTC-green)

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

**Latest saved flight:** 2026-06-28 19:50:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-28 19:50:18 UTC

- **123,305** saved flights
- **42,293** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **123,305** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,490,458.0 tonnes** estimated CO2 emissions
- **86,403,361 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5044 |
| 2 | SkyWest Airlines | 4553 |
| 3 | EJA | 2395 |
| 4 | IndiGo | 2361 |
| 5 | American Airlines | 1905 |
| 6 | Southwest Airlines | 1848 |
| 7 | ENY | 1545 |
| 8 | Delta Air Lines | 1462 |
| 9 | Lufthansa | 1330 |
| 10 | LATAM Airlines | 1107 |
| 11 | Vueling | 1098 |
| 12 | WIF | 1092 |
| 13 | AZU | 1035 |
| 14 | AXM | 988 |
| 15 | LXJ | 952 |
| 16 | Swiss International | 870 |
| 17 | All Nippon Airways | 832 |
| 18 | Alaska Airlines | 804 |
| 19 | easyJet | 788 |
| 20 | QLK | 778 |
| 21 | EJU | 773 |
| 22 | Cathay Pacific | 689 |
| 23 | AEE | 683 |
| 24 | Air France | 675 |
| 25 | VIV | 670 |
| 26 | United Airlines | 662 |
| 27 | CXK | 653 |
| 28 | MXY | 644 |
| 29 | JetBlue | 621 |
| 30 | GLO | 617 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 104839 |
| 2 | 🇪🇸 ES | 8301 |
| 3 | 🇮🇳 IN | 7401 |
| 4 | 🇦🇺 AU | 7181 |
| 5 | 🇧🇷 BR | 6844 |
| 6 | 🇩🇪 DE | 6576 |
| 7 | 🇮🇹 IT | 6557 |
| 8 | 🇨🇦 CA | 6472 |
| 9 | 🇬🇧 GB | 5437 |
| 10 | 🇯🇵 JP | 5427 |
| 11 | 🇫🇷 FR | 4905 |
| 12 | 🇨🇴 CO | 4031 |
| 13 | 🇲🇽 MX | 3584 |
| 14 | 🇬🇷 GR | 3519 |
| 15 | 🇳🇴 NO | 3401 |
| 16 | 🇨🇭 CH | 3174 |
| 17 | 🇹🇷 TR | 2587 |
| 18 | 🇲🇾 MY | 2557 |
| 19 | 🇿🇦 ZA | 2043 |
| 20 | 🇵🇱 PL | 2026 |
| 21 | 🇳🇿 NZ | 1986 |
| 22 | 🇹🇭 TH | 1932 |
| 23 | 🇰🇷 KR | 1926 |
| 24 | 🇵🇭 PH | 1758 |
| 25 | 🇬🇹 GT | 1708 |
| 26 | 🇲🇦 MA | 1321 |
| 27 | 🇲🇪 ME | 1230 |
| 28 | 🇲🇴 MO | 1176 |
| 29 | 🇳🇱 NL | 1174 |
| 30 | 🇧🇸 BS | 1074 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2593 |
| 2 | Denver International Airport |  | US | 2068 |
| 3 | Tokyo International Airport |  | JP | 1797 |
| 4 | Indira Gandhi International Airport |  | IN | 1631 |
| 5 | Harry Reid International Airport |  | US | 1540 |
| 6 | Guaymaral Airport |  | CO | 1519 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1486 |
| 8 | Zurich Airport |  | CH | 1374 |
| 9 | La Aurora Airport |  | GT | 1319 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1310 |
| 11 | Frankfurt am Main International Airport |  | DE | 1284 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1213 |
| 13 | Chicago O'Hare International Airport |  | US | 1194 |
| 14 | Macau International Airport |  | MO | 1176 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1080 |
| 17 | Capua Airport |  | IT | 1057 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1029 |
| 19 | Madrid Barajas International Airport |  | ES | 1028 |
| 20 | Kuala Lumpur International Airport |  | MY | 993 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 975 |
| 22 | Congonhas Airport |  | BR | 961 |
| 23 | Charlotte/Douglas International Airport |  | US | 929 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 905 |
| 25 | Charles de Gaulle International Airport |  | FR | 903 |
| 26 | Bengaluru International Airport |  | IN | 889 |
| 27 | Malpensa International Airport |  | IT | 853 |
| 28 | Ninoy Aquino International Airport |  | PH | 815 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 811 |
| 30 | Daniel K Inouye International Airport |  | US | 788 |
| 31 | Barcelona International Airport |  | ES | 769 |
| 32 | Tenerife Norte Airport |  | ES | 764 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 749 |
| 34 | Calgary International Airport |  | CA | 724 |
| 35 | Vitoria/Foronda Airport |  | ES | 717 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 713 |
| 37 | Amsterdam Airport Schiphol |  | NL | 711 |
| 38 | Scottsdale Airport |  | US | 709 |
| 39 | Seattle-Tacoma International Airport |  | US | 706 |
| 40 | Don Mueang International Airport |  | TH | 698 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 633 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 447 | 21m | 244 km | 1,882.2 t |
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
| 13 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 178 | 26m | 215 km | 659.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 178 | 22m | 55 km | 169.2 t |
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
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 140 | 1h 17m | 961 km | 2,320.6 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 138 | 13m | - | - |
| 29 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 137 | 29m | 49 km | 115.8 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 135 | 20m | 147 km | 341.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9452B |  | CA54 (CA54) | New Jerusalem Airport (K1Q4) | 2026-06-28 19:08 UTC | 2026-06-28 19:50 UTC | 41m |
| N32WA |  | Fairbanks International Airport (PAFA) | Ambler Airport (PAFM) | 2026-06-28 18:00 UTC | 2026-06-28 19:46 UTC | 1h 45m |
| N916KT |  | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-06-28 19:17 UTC | 2026-06-28 19:35 UTC | 18m |
| N4593Y |  | Boulder Municipal Airport (KBDU) | Boulder Municipal Airport (KBDU) | 2026-06-28 18:53 UTC | 2026-06-28 19:32 UTC | 39m |
| N707PD |  | Northern Colorado Regional Airport (KFNL) | Laramie Regional Airport (KLAR) | 2026-06-28 18:53 UTC | 2026-06-28 19:30 UTC | 37m |
| N560PB |  | Centennial Airport (KAPA) | Hualapai Airport (3AZ5) | 2026-06-28 18:00 UTC | 2026-06-28 19:29 UTC | 1h 28m |
| N66LP |  | Gnoss Field (KDVO) | Gnoss Field (KDVO) | 2026-06-28 18:58 UTC | 2026-06-28 19:28 UTC | 29m |
| N26760 |  | San Luis Obispo County Regional Airport (KSBP) | Robert Oliver Airpark (5CL1) | 2026-06-28 19:06 UTC | 2026-06-28 19:24 UTC | 18m |
| JRE730 | JRE | Northwest Florida Beaches International Airport (KECP) | DE29 (DE29) | 2026-06-28 17:00 UTC | 2026-06-28 19:23 UTC | 2h 22m |
| CXK670 | CXK | Hayward Executive Airport (KHWD) | Hayward Executive Airport (KHWD) | 2026-06-28 18:56 UTC | 2026-06-28 19:22 UTC | 25m |
| MSR794 | EgyptAir | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | HE42 (HE42) | 2026-06-28 16:34 UTC | 2026-06-28 19:17 UTC | 2h 43m |
| ASP864 | ASP | Oakland San Francisco Bay Airport (KOAK) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-06-28 18:45 UTC | 2026-06-28 19:15 UTC | 29m |
| MSR772 | EgyptAir | Geneva Cointrin International Airport (LSGG) | HE42 (HE42) | 2026-06-28 15:29 UTC | 2026-06-28 19:14 UTC | 3h 45m |
| N2054S |  | Lewis University Airport (KLOT) | 3IL2 (3IL2) | 2026-06-28 18:44 UTC | 2026-06-28 19:13 UTC | 29m |
| N909MJ |  | Smith County Airport (MS39) | Stevens Field (KPSO) | 2026-06-28 15:26 UTC | 2026-06-28 19:06 UTC | 3h 40m |
| SWR90A | Swiss International | Westerland Sylt Airport (EDXW) | Zurich Airport (LSZH) | 2026-06-28 17:46 UTC | 2026-06-28 19:06 UTC | 1h 20m |
| N332HC |  | Cortez Municipal Airport (KCEZ) | Tanner Field (CO27) | 2026-06-28 18:09 UTC | 2026-06-28 19:05 UTC | 55m |
| N432RJ |  | Parker Field (AL18) | Chenango Bridge Airport (1NK8) | 2026-06-28 17:04 UTC | 2026-06-28 19:04 UTC | 1h 59m |
| N730VB |  | Cartys Airstrip (8AK2) | Cartys Airstrip (8AK2) | 2026-06-28 18:08 UTC | 2026-06-28 19:03 UTC | 54m |
| NOZ36S | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Kiruna Airport (ESNQ) | 2026-06-28 17:43 UTC | 2026-06-28 19:03 UTC | 1h 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
