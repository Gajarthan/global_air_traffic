# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--06_21:48:32_UTC-green)

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

**Latest saved flight:** 2026-07-06 21:48:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-06 21:48:32 UTC

- **131,528** saved flights
- **44,693** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **131,528** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,586,763.3 tonnes** estimated CO2 emissions
- **91,986,277 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5353 |
| 2 | SkyWest Airlines | 4879 |
| 3 | EJA | 2583 |
| 4 | IndiGo | 2458 |
| 5 | American Airlines | 2047 |
| 6 | Southwest Airlines | 1981 |
| 7 | ENY | 1655 |
| 8 | Delta Air Lines | 1577 |
| 9 | Lufthansa | 1370 |
| 10 | LATAM Airlines | 1207 |
| 11 | Vueling | 1159 |
| 12 | WIF | 1147 |
| 13 | AZU | 1117 |
| 14 | LXJ | 1016 |
| 15 | AXM | 1012 |
| 16 | Swiss International | 919 |
| 17 | All Nippon Airways | 863 |
| 18 | easyJet | 843 |
| 19 | Alaska Airlines | 841 |
| 20 | QLK | 821 |
| 21 | EJU | 812 |
| 22 | VIV | 726 |
| 23 | AEE | 716 |
| 24 | Cathay Pacific | 716 |
| 25 | Air France | 714 |
| 26 | CXK | 707 |
| 27 | United Airlines | 702 |
| 28 | JetBlue | 690 |
| 29 | MXY | 685 |
| 30 | GLO | 676 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 112779 |
| 2 | 🇪🇸 ES | 8770 |
| 3 | 🇮🇳 IN | 7705 |
| 4 | 🇦🇺 AU | 7569 |
| 5 | 🇧🇷 BR | 7415 |
| 6 | 🇨🇦 CA | 6943 |
| 7 | 🇩🇪 DE | 6878 |
| 8 | 🇮🇹 IT | 6857 |
| 9 | 🇬🇧 GB | 5872 |
| 10 | 🇯🇵 JP | 5653 |
| 11 | 🇫🇷 FR | 5230 |
| 12 | 🇨🇴 CO | 4127 |
| 13 | 🇲🇽 MX | 3838 |
| 14 | 🇬🇷 GR | 3764 |
| 15 | 🇳🇴 NO | 3563 |
| 16 | 🇨🇭 CH | 3380 |
| 17 | 🇹🇷 TR | 2924 |
| 18 | 🇲🇾 MY | 2623 |
| 19 | 🇿🇦 ZA | 2171 |
| 20 | 🇵🇱 PL | 2159 |
| 21 | 🇳🇿 NZ | 2090 |
| 22 | 🇹🇭 TH | 2034 |
| 23 | 🇰🇷 KR | 1966 |
| 24 | 🇵🇭 PH | 1815 |
| 25 | 🇬🇹 GT | 1786 |
| 26 | 🇲🇦 MA | 1400 |
| 27 | 🇲🇪 ME | 1300 |
| 28 | 🇳🇱 NL | 1232 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1155 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2750 |
| 2 | Denver International Airport |  | US | 2240 |
| 3 | Tokyo International Airport |  | JP | 1856 |
| 4 | Indira Gandhi International Airport |  | IN | 1700 |
| 5 | Harry Reid International Airport |  | US | 1638 |
| 6 | Guaymaral Airport |  | CO | 1594 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1551 |
| 8 | Zurich Airport |  | CH | 1448 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1403 |
| 10 | La Aurora Airport |  | GT | 1380 |
| 11 | Frankfurt am Main International Airport |  | DE | 1327 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1271 |
| 13 | Chicago O'Hare International Airport |  | US | 1267 |
| 14 | Macau International Airport |  | MO | 1186 |
| 15 | El Dorado International Airport |  | CO | 1178 |
| 16 | Salt Lake City International Airport |  | US | 1172 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1131 |
| 18 | Madrid Barajas International Airport |  | ES | 1083 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1079 |
| 20 | Capua Airport |  | IT | 1077 |
| 21 | Congonhas Airport |  | BR | 1047 |
| 22 | Kuala Lumpur International Airport |  | MY | 1018 |
| 23 | Charlotte/Douglas International Airport |  | US | 978 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 952 |
| 25 | Charles de Gaulle International Airport |  | FR | 952 |
| 26 | Bengaluru International Airport |  | IN | 931 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 900 |
| 28 | Malpensa International Airport |  | IT | 880 |
| 29 | Ninoy Aquino International Airport |  | PH | 842 |
| 30 | Daniel K Inouye International Airport |  | US | 823 |
| 31 | Barcelona International Airport |  | ES | 815 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 806 |
| 33 | Tenerife Norte Airport |  | ES | 793 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 775 |
| 35 | Calgary International Airport |  | CA | 769 |
| 36 | Seattle-Tacoma International Airport |  | US | 759 |
| 37 | Vitoria/Foronda Airport |  | ES | 754 |
| 38 | Viracopos International Airport |  | BR | 753 |
| 39 | Scottsdale Airport |  | US | 751 |
| 40 | Amsterdam Airport Schiphol |  | NL | 744 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 668 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 476 | 21m | 244 km | 2,004.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 329 | 24m | 225 km | 1,276.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 328 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 317 | 1h 10m | 770 km | 4,211.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 282 | 14m | 114 km | 553.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 249 | 26m | 275 km | 1,179.9 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 241 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 192 | 22m | 55 km | 182.5 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 184 | 44m | 241 km | 764.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 183 | 26m | 215 km | 677.8 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 180 | 20m | 99 km | 308.3 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 178 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 173 | 1h 46m | 1,423 km | 4,245.7 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 164 | 31m | 369 km | 1,043.9 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 162 | 18m | 144 km | 403.0 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 161 | 20m | 250 km | 695.4 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 158 | 44m | 452 km | 1,231.4 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 158 | 30m | 49 km | 133.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 155 | 1h 1m | 695 km | 1,858.0 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 154 | 1h 16m | 961 km | 2,552.6 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 153 | 54m | 136 km | 358.7 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 149 | 1h 38m | 1,156 km | 2,972.5 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 147 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N30EA |  | Skydive Chicago Airport (K8N2) | Skydive Chicago Airport (K8N2) | 2026-07-06 21:37 UTC | 2026-07-06 21:48 UTC | 11m |
| N718TA |  | Conroe/North Houston Regional Airport (KCXO) | Easterwood Field (KCLL) | 2026-07-06 20:53 UTC | 2026-07-06 21:46 UTC | 52m |
| N48JA |  | Aurora Municipal Airport (KARR) | 0IL8 (0IL8) | 2026-07-06 21:27 UTC | 2026-07-06 21:39 UTC | 12m |
| N25BQ |  | Dupage Airport (KDPA) | Humm Airport (06IL) | 2026-07-06 21:09 UTC | 2026-07-06 21:39 UTC | 30m |
| N851MB |  | Boulder Municipal Airport (KBDU) | Elk Park Ranch Airport (34CD) | 2026-07-06 21:25 UTC | 2026-07-06 21:38 UTC | 12m |
| THY1FV | Turkish Airlines | Istanbul Airport (LTFM) | Gaziemir Airport (LTBK) | 2026-07-06 21:02 UTC | 2026-07-06 21:34 UTC | 31m |
| N5138R |  | 89CO (89CO) | Rocky Mountain Metro Airport (KBJC) | 2026-07-06 20:44 UTC | 2026-07-06 21:34 UTC | 49m |
| N558LM |  | Soldotna Airport (PASX) | Ted Stevens Anchorage International Airport (PANC) | 2026-07-06 21:03 UTC | 2026-07-06 21:30 UTC | 27m |
| SIL1507 | SIL | Ted Stevens Anchorage International Airport (PANC) | King Salmon Airport (PAKN) | 2026-07-06 20:27 UTC | 2026-07-06 21:30 UTC | 1h 3m |
| CAP481 | CAP | Oakland San Francisco Bay Airport (KOAK) | Oakland San Francisco Bay Airport (KOAK) | 2026-07-06 19:42 UTC | 2026-07-06 21:26 UTC | 1h 43m |
| BOE194 | BOE | Portland International Airport (KPDX) | Boeing Field/King County International Airport (KBFI) | 2026-07-06 20:20 UTC | 2026-07-06 21:25 UTC | 1h 4m |
| N8314W |  | City Of Colorado Springs Municipal Airport (KCOS) | 97CO (97CO) | 2026-07-06 20:50 UTC | 2026-07-06 21:24 UTC | 34m |
| GFY1124 | GFY | Portland-Hillsboro Airport (KHIO) | Portland-Hillsboro Airport (KHIO) | 2026-07-06 20:39 UTC | 2026-07-06 21:24 UTC | 44m |
| N33RK |  | North Perry Airport (KHWO) | Orlando Executive Airport (KORL) | 2026-07-06 19:22 UTC | 2026-07-06 21:23 UTC | 2h 1m |
| LYRE71 | LYR | Randolph Afb Airport (KRND) | Richie Rich Airport (8TE1) | 2026-07-06 20:55 UTC | 2026-07-06 21:17 UTC | 22m |
| EJM37 | EJM | Washington Dulles International Airport (KIAD) | Henderson Executive Airport (KHND) | 2026-07-06 16:38 UTC | 2026-07-06 21:16 UTC | 4h 37m |
| TKR914 | TKR | Mesa Gateway Airport (KIWA) | A Z Minerals Corporation Airport (03UT) | 2026-07-06 20:31 UTC | 2026-07-06 21:13 UTC | 42m |
| N182KQ |  | Decatur Shores Airport (WN07) | Boeing Field/King County International Airport (KBFI) | 2026-07-06 20:48 UTC | 2026-07-06 21:13 UTC | 24m |
| N654BH |  | Buchanan Field (KCCR) | Truckee-Tahoe Airport (KTRK) | 2026-07-06 20:32 UTC | 2026-07-06 21:13 UTC | 40m |
| CXK131 | CXK | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-07-06 20:41 UTC | 2026-07-06 21:11 UTC | 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
