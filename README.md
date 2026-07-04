# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_19:48:43_UTC-green)

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

**Latest saved flight:** 2026-07-04 19:48:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-04 19:48:43 UTC

- **129,126** saved flights
- **43,944** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **129,126** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,558,750.7 tonnes** estimated CO2 emissions
- **90,362,362 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5252 |
| 2 | SkyWest Airlines | 4791 |
| 3 | EJA | 2525 |
| 4 | IndiGo | 2425 |
| 5 | American Airlines | 1993 |
| 6 | Southwest Airlines | 1944 |
| 7 | ENY | 1620 |
| 8 | Delta Air Lines | 1539 |
| 9 | Lufthansa | 1360 |
| 10 | LATAM Airlines | 1173 |
| 11 | Vueling | 1144 |
| 12 | WIF | 1133 |
| 13 | AZU | 1096 |
| 14 | AXM | 1003 |
| 15 | LXJ | 999 |
| 16 | Swiss International | 898 |
| 17 | All Nippon Airways | 858 |
| 18 | Alaska Airlines | 833 |
| 19 | easyJet | 827 |
| 20 | QLK | 808 |
| 21 | EJU | 799 |
| 22 | VIV | 715 |
| 23 | Cathay Pacific | 712 |
| 24 | AEE | 706 |
| 25 | Air France | 703 |
| 26 | CXK | 694 |
| 27 | United Airlines | 687 |
| 28 | MXY | 676 |
| 29 | JetBlue | 671 |
| 30 | GLO | 655 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 110526 |
| 2 | 🇪🇸 ES | 8603 |
| 3 | 🇮🇳 IN | 7606 |
| 4 | 🇦🇺 AU | 7481 |
| 5 | 🇧🇷 BR | 7240 |
| 6 | 🇨🇦 CA | 6804 |
| 7 | 🇩🇪 DE | 6793 |
| 8 | 🇮🇹 IT | 6763 |
| 9 | 🇬🇧 GB | 5728 |
| 10 | 🇯🇵 JP | 5609 |
| 11 | 🇫🇷 FR | 5125 |
| 12 | 🇨🇴 CO | 4080 |
| 13 | 🇲🇽 MX | 3768 |
| 14 | 🇬🇷 GR | 3680 |
| 15 | 🇳🇴 NO | 3519 |
| 16 | 🇨🇭 CH | 3306 |
| 17 | 🇹🇷 TR | 2798 |
| 18 | 🇲🇾 MY | 2603 |
| 19 | 🇿🇦 ZA | 2137 |
| 20 | 🇵🇱 PL | 2122 |
| 21 | 🇳🇿 NZ | 2069 |
| 22 | 🇹🇭 TH | 2001 |
| 23 | 🇰🇷 KR | 1963 |
| 24 | 🇵🇭 PH | 1808 |
| 25 | 🇬🇹 GT | 1766 |
| 26 | 🇲🇦 MA | 1384 |
| 27 | 🇲🇪 ME | 1283 |
| 28 | 🇳🇱 NL | 1214 |
| 29 | 🇲🇴 MO | 1185 |
| 30 | 🇭🇷 HR | 1129 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2692 |
| 2 | Denver International Airport |  | US | 2196 |
| 3 | Tokyo International Airport |  | JP | 1848 |
| 4 | Indira Gandhi International Airport |  | IN | 1677 |
| 5 | Harry Reid International Airport |  | US | 1610 |
| 6 | Guaymaral Airport |  | CO | 1567 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1530 |
| 8 | Zurich Airport |  | CH | 1420 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1375 |
| 10 | La Aurora Airport |  | GT | 1366 |
| 11 | Frankfurt am Main International Airport |  | DE | 1315 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1259 |
| 13 | Chicago O'Hare International Airport |  | US | 1239 |
| 14 | Macau International Airport |  | MO | 1185 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1150 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1080 |
| 18 | Capua Airport |  | IT | 1067 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1060 |
| 20 | Madrid Barajas International Airport |  | ES | 1058 |
| 21 | Congonhas Airport |  | BR | 1018 |
| 22 | Kuala Lumpur International Airport |  | MY | 1013 |
| 23 | Charlotte/Douglas International Airport |  | US | 969 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 940 |
| 25 | Charles de Gaulle International Airport |  | FR | 938 |
| 26 | Bengaluru International Airport |  | IN | 920 |
| 27 | Malpensa International Airport |  | IT | 878 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 869 |
| 29 | Ninoy Aquino International Airport |  | PH | 838 |
| 30 | Daniel K Inouye International Airport |  | US | 814 |
| 31 | Barcelona International Airport |  | ES | 803 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 790 |
| 33 | Tenerife Norte Airport |  | ES | 784 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 759 |
| 35 | Calgary International Airport |  | CA | 753 |
| 36 | Vitoria/Foronda Airport |  | ES | 748 |
| 37 | Seattle-Tacoma International Airport |  | US | 745 |
| 38 | Scottsdale Airport |  | US | 743 |
| 39 | Viracopos International Airport |  | BR | 739 |
| 40 | Amsterdam Airport Schiphol |  | NL | 731 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 656 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 467 | 21m | 244 km | 1,966.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 328 | 24m | 225 km | 1,272.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 325 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 314 | 1h 10m | 770 km | 4,171.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 247 | 26m | 275 km | 1,170.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 237 | 31m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 189 | 22m | 55 km | 179.6 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 182 | 26m | 215 km | 674.1 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 180 | 44m | 241 km | 747.7 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 179 | 20m | 99 km | 306.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 173 | 27m | 152 km | 452.1 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 168 | 1h 45m | 1,423 km | 4,123.0 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 163 | 31m | 369 km | 1,037.5 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 159 | 20m | 250 km | 686.8 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 158 | 18m | 144 km | 393.0 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 157 | 44m | 452 km | 1,223.6 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 154 | 30m | 49 km | 130.2 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 153 | 1h 1m | 695 km | 1,834.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 149 | 1h 17m | 961 km | 2,469.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 147 | 54m | 136 km | 344.6 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 145 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AAE125 | AAE | Liege Airport (EBLG) | Zhuhai Airport (ZGSD) | 2026-07-04 08:56 UTC | 2026-07-04 19:48 UTC | 10h 51m |
| N474J |  | 9CL5 (9CL5) | Santa Monica Municipal Airport (KSMO) | 2026-07-04 19:09 UTC | 2026-07-04 19:46 UTC | 36m |
| N9454F |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-07-04 19:27 UTC | 2026-07-04 19:38 UTC | 11m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-07-04 19:21 UTC | 2026-07-04 19:35 UTC | 13m |
| TKR914 | TKR | Mesa Gateway Airport (KIWA) | Rimrock Airport (48AZ) | 2026-07-04 19:18 UTC | 2026-07-04 19:34 UTC | 16m |
| N61733 |  | Miami Executive Airport (KTMB) | Homestead Arb Airport (KHST) | 2026-07-04 18:50 UTC | 2026-07-04 19:34 UTC | 43m |
| N27NW |  | Petawawa Airport (CYWA) | Petawawa Airport (CYWA) | 2026-07-04 19:01 UTC | 2026-07-04 19:32 UTC | 30m |
| N611MV |  | Mc Clellan Airfield (KMCC) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-07-04 19:04 UTC | 2026-07-04 19:29 UTC | 25m |
| JOLLY91 | JOL | Moffett Federal Airfield (KNUQ) | Moffett Federal Airfield (KNUQ) | 2026-07-04 17:45 UTC | 2026-07-04 19:28 UTC | 1h 42m |
| JBU68 | JetBlue | Charleston Afb/International Airport (KCHS) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-04 17:32 UTC | 2026-07-04 19:27 UTC | 1h 55m |
| N26NR |  | Hunter Army Air Field (KSVN) | Hunter Army Air Field (KSVN) | 2026-07-04 19:17 UTC | 2026-07-04 19:23 UTC | 5m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-07-04 19:05 UTC | 2026-07-04 19:17 UTC | 11m |
| UPS22 | UPS | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-07-04 08:28 UTC | 2026-07-04 19:15 UTC | 10h 47m |
| CKS703 | CKS | Ben Gurion International Airport (LLBG) | Zhuhai Airport (ZGSD) | 2026-07-04 10:15 UTC | 2026-07-04 19:12 UTC | 8h 57m |
| N762GB |  | Provo Municipal Airport (KPVU) | KU77 (KU77) | 2026-07-04 18:45 UTC | 2026-07-04 19:07 UTC | 21m |
| TKR910 | TKR | Mesa Gateway Airport (KIWA) | Rimrock Airport (48AZ) | 2026-07-04 18:49 UTC | 2026-07-04 19:05 UTC | 16m |
| N747EE |  | Essex County Airport (KCDW) | Newark Liberty International Airport (KEWR) | 2026-07-04 16:57 UTC | 2026-07-04 19:00 UTC | 2h 3m |
| N39VA |  | Lancaster Airport (KLNS) | Philadelphia International Airport (KPHL) | 2026-07-04 18:29 UTC | 2026-07-04 18:57 UTC | 28m |
| RYR5909 | Ryanair | Nimes-Arles-Camargue Airport (LFTW) | Fes Sefrou Airport (GMFU) | 2026-07-04 17:15 UTC | 2026-07-04 18:56 UTC | 1h 41m |
| N682AC |  | Hidden Valley Ranch Airport (TS90) | Bb Airpark (TE88) | 2026-07-04 18:41 UTC | 2026-07-04 18:53 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
