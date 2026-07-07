# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--07_13:38:43_UTC-green)

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

**Latest saved flight:** 2026-07-07 13:38:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-07 13:38:43 UTC

- **131,967** saved flights
- **44,806** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **131,967** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,591,234.6 tonnes** estimated CO2 emissions
- **92,245,485 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5373 |
| 2 | SkyWest Airlines | 4887 |
| 3 | EJA | 2586 |
| 4 | IndiGo | 2464 |
| 5 | American Airlines | 2055 |
| 6 | Southwest Airlines | 1984 |
| 7 | ENY | 1657 |
| 8 | Delta Air Lines | 1581 |
| 9 | Lufthansa | 1375 |
| 10 | LATAM Airlines | 1214 |
| 11 | Vueling | 1159 |
| 12 | WIF | 1152 |
| 13 | AZU | 1121 |
| 14 | AXM | 1017 |
| 15 | LXJ | 1017 |
| 16 | Swiss International | 929 |
| 17 | All Nippon Airways | 868 |
| 18 | easyJet | 844 |
| 19 | Alaska Airlines | 842 |
| 20 | QLK | 825 |
| 21 | EJU | 813 |
| 22 | VIV | 730 |
| 23 | AEE | 716 |
| 24 | Air France | 716 |
| 25 | Cathay Pacific | 716 |
| 26 | CXK | 708 |
| 27 | United Airlines | 702 |
| 28 | JetBlue | 692 |
| 29 | MXY | 686 |
| 30 | GLO | 676 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 113061 |
| 2 | 🇪🇸 ES | 8791 |
| 3 | 🇮🇳 IN | 7726 |
| 4 | 🇦🇺 AU | 7608 |
| 5 | 🇧🇷 BR | 7442 |
| 6 | 🇨🇦 CA | 6972 |
| 7 | 🇩🇪 DE | 6902 |
| 8 | 🇮🇹 IT | 6882 |
| 9 | 🇬🇧 GB | 5903 |
| 10 | 🇯🇵 JP | 5685 |
| 11 | 🇫🇷 FR | 5252 |
| 12 | 🇨🇴 CO | 4131 |
| 13 | 🇲🇽 MX | 3846 |
| 14 | 🇬🇷 GR | 3779 |
| 15 | 🇳🇴 NO | 3579 |
| 16 | 🇨🇭 CH | 3402 |
| 17 | 🇹🇷 TR | 2936 |
| 18 | 🇲🇾 MY | 2633 |
| 19 | 🇵🇱 PL | 2179 |
| 20 | 🇿🇦 ZA | 2177 |
| 21 | 🇳🇿 NZ | 2091 |
| 22 | 🇹🇭 TH | 2039 |
| 23 | 🇰🇷 KR | 1968 |
| 24 | 🇵🇭 PH | 1817 |
| 25 | 🇬🇹 GT | 1792 |
| 26 | 🇲🇦 MA | 1400 |
| 27 | 🇲🇪 ME | 1309 |
| 28 | 🇳🇱 NL | 1243 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1161 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2756 |
| 2 | Denver International Airport |  | US | 2245 |
| 3 | Tokyo International Airport |  | JP | 1865 |
| 4 | Indira Gandhi International Airport |  | IN | 1708 |
| 5 | Harry Reid International Airport |  | US | 1642 |
| 6 | Guaymaral Airport |  | CO | 1597 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1553 |
| 8 | Zurich Airport |  | CH | 1460 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1406 |
| 10 | La Aurora Airport |  | GT | 1385 |
| 11 | Frankfurt am Main International Airport |  | DE | 1332 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1271 |
| 13 | Chicago O'Hare International Airport |  | US | 1269 |
| 14 | Macau International Airport |  | MO | 1186 |
| 15 | El Dorado International Airport |  | CO | 1179 |
| 16 | Salt Lake City International Airport |  | US | 1175 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1138 |
| 18 | Madrid Barajas International Airport |  | ES | 1085 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1081 |
| 20 | Capua Airport |  | IT | 1078 |
| 21 | Congonhas Airport |  | BR | 1052 |
| 22 | Kuala Lumpur International Airport |  | MY | 1023 |
| 23 | Charlotte/Douglas International Airport |  | US | 980 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 957 |
| 25 | Charles de Gaulle International Airport |  | FR | 956 |
| 26 | Bengaluru International Airport |  | IN | 933 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 905 |
| 28 | Malpensa International Airport |  | IT | 881 |
| 29 | Ninoy Aquino International Airport |  | PH | 843 |
| 30 | Daniel K Inouye International Airport |  | US | 825 |
| 31 | Barcelona International Airport |  | ES | 815 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 808 |
| 33 | Tenerife Norte Airport |  | ES | 795 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 775 |
| 35 | Calgary International Airport |  | CA | 769 |
| 36 | Seattle-Tacoma International Airport |  | US | 760 |
| 37 | Scottsdale Airport |  | US | 756 |
| 38 | Vitoria/Foronda Airport |  | ES | 755 |
| 39 | Viracopos International Airport |  | BR | 753 |
| 40 | Amsterdam Airport Schiphol |  | NL | 746 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 669 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 478 | 21m | 244 km | 2,012.7 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 330 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 329 | 24m | 225 km | 1,276.4 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 321 | 1h 10m | 770 km | 4,264.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 282 | 14m | 114 km | 553.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 250 | 26m | 275 km | 1,184.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 241 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 192 | 22m | 55 km | 182.5 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 185 | 44m | 241 km | 768.5 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 184 | 26m | 215 km | 681.5 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 181 | 20m | 99 km | 310.0 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 178 | 13m | - | - |
| 18 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 176 | 1h 46m | 1,423 km | 4,319.3 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 165 | 31m | 369 km | 1,050.3 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 162 | 18m | 144 km | 403.0 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 161 | 20m | 250 km | 695.4 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 159 | 44m | 452 km | 1,239.2 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 159 | 30m | 49 km | 134.4 t |
| 25 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 155 | 1h 1m | 695 km | 1,858.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 154 | 1h 16m | 961 km | 2,552.6 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 149 | 1h 38m | 1,156 km | 2,972.5 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 148 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SCA42 | SCA | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-07-07 13:05 UTC | 2026-07-07 13:38 UTC | 32m |
| N172GT |  | Daytona Beach International Airport (KDAB) | KXFL (KXFL) | 2026-07-07 12:52 UTC | 2026-07-07 13:26 UTC | 34m |
| N738VY |  | Reedsburg Municipal Airport (KC35) | Reedsburg Municipal Airport (KC35) | 2026-07-07 12:40 UTC | 2026-07-07 13:23 UTC | 42m |
| N48BZ |  | Lawrence J Timmerman Airport (KMWC) | Lawrence J Timmerman Airport (KMWC) | 2026-07-07 13:00 UTC | 2026-07-07 13:22 UTC | 21m |
| A6FTS |  | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-07-07 12:48 UTC | 2026-07-07 13:20 UTC | 32m |
| N12386 |  | Lake Havasu City Airport (KHII) | Lake Havasu City Airport (KHII) | 2026-07-07 12:52 UTC | 2026-07-07 13:16 UTC | 23m |
| EVA850 | EVA Air | Chek Lap Kok International Airport (VHHH) | Kaohsiung International Airport (RCKH) | 2026-07-07 12:01 UTC | 2026-07-07 13:15 UTC | 1h 13m |
| ROK73 | ROK | Falcon Field (KFFZ) | Falcon Field (KFFZ) | 2026-07-07 12:50 UTC | 2026-07-07 13:14 UTC | 24m |
| N370D |  | Seattle-Tacoma International Airport (KSEA) | Spokane International Airport (KGEG) | 2026-07-07 12:39 UTC | 2026-07-07 13:14 UTC | 35m |
| GFA508 | Gulf Air | Udhailiyah Airport (OEUD) | Sirri Island Airport (OIBS) | 2026-07-07 12:42 UTC | 2026-07-07 13:11 UTC | 29m |
| N404FR |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-07-07 12:41 UTC | 2026-07-07 13:11 UTC | 29m |
| N18JA |  | Aurora Municipal Airport (KARR) | 2LL9 (2LL9) | 2026-07-07 12:51 UTC | 2026-07-07 13:11 UTC | 19m |
| PERRIS3 | PER | Perris Valley Airport (KL65) | Perris Valley Airport (KL65) | 2026-07-07 12:53 UTC | 2026-07-07 13:08 UTC | 14m |
| N469DM |  | MS18 (MS18) | Warren County Memorial Airport (KRNC) | 2026-07-07 12:42 UTC | 2026-07-07 13:04 UTC | 22m |
| N352SD |  | 3IN4 (3IN4) | Marion County-Rankin Fite Airport (KHAB) | 2026-07-07 12:03 UTC | 2026-07-07 13:03 UTC | 59m |
| N172SB |  | Birmingham-Shuttlesworth International Airport (KBHM) | Lazy Eight Airpark Llc Airport (AL17) | 2026-07-07 12:38 UTC | 2026-07-07 13:03 UTC | 24m |
| N460AK |  | Livermore Municipal Airport (KLVK) | Oakland San Francisco Bay Airport (KOAK) | 2026-07-07 12:51 UTC | 2026-07-07 13:02 UTC | 10m |
| CXK329 | CXK | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-07-07 12:12 UTC | 2026-07-07 13:01 UTC | 48m |
| GPD928 | GPD | Francis S Gabreski Airport (KFOK) | Westchester County Airport (KHPN) | 2026-07-07 12:43 UTC | 2026-07-07 13:00 UTC | 16m |
| N901LM |  | Bangor International Airport (KBGR) | Bangor International Airport (KBGR) | 2026-07-07 12:45 UTC | 2026-07-07 12:54 UTC | 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
