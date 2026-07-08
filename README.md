# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--08_19:35:27_UTC-green)

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

**Latest saved flight:** 2026-07-08 19:35:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-08 19:35:27 UTC

- **133,300** saved flights
- **45,183** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **133,300** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,604,806.4 tonnes** estimated CO2 emissions
- **93,032,256 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5412 |
| 2 | SkyWest Airlines | 4923 |
| 3 | EJA | 2617 |
| 4 | IndiGo | 2487 |
| 5 | American Airlines | 2084 |
| 6 | Southwest Airlines | 2003 |
| 7 | ENY | 1675 |
| 8 | Delta Air Lines | 1593 |
| 9 | Lufthansa | 1383 |
| 10 | LATAM Airlines | 1226 |
| 11 | Vueling | 1170 |
| 12 | WIF | 1161 |
| 13 | AZU | 1131 |
| 14 | LXJ | 1022 |
| 15 | AXM | 1019 |
| 16 | Swiss International | 945 |
| 17 | All Nippon Airways | 871 |
| 18 | easyJet | 858 |
| 19 | Alaska Airlines | 846 |
| 20 | QLK | 830 |
| 21 | EJU | 820 |
| 22 | VIV | 735 |
| 23 | AEE | 724 |
| 24 | Cathay Pacific | 719 |
| 25 | CXK | 719 |
| 26 | Air France | 718 |
| 27 | United Airlines | 705 |
| 28 | JetBlue | 700 |
| 29 | MXY | 689 |
| 30 | GLO | 680 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 114281 |
| 2 | 🇪🇸 ES | 8854 |
| 3 | 🇮🇳 IN | 7795 |
| 4 | 🇦🇺 AU | 7702 |
| 5 | 🇧🇷 BR | 7502 |
| 6 | 🇨🇦 CA | 7040 |
| 7 | 🇩🇪 DE | 6961 |
| 8 | 🇮🇹 IT | 6936 |
| 9 | 🇬🇧 GB | 5965 |
| 10 | 🇯🇵 JP | 5719 |
| 11 | 🇫🇷 FR | 5299 |
| 12 | 🇨🇴 CO | 4173 |
| 13 | 🇲🇽 MX | 3882 |
| 14 | 🇬🇷 GR | 3817 |
| 15 | 🇳🇴 NO | 3611 |
| 16 | 🇨🇭 CH | 3445 |
| 17 | 🇹🇷 TR | 3007 |
| 18 | 🇲🇾 MY | 2647 |
| 19 | 🇵🇱 PL | 2199 |
| 20 | 🇿🇦 ZA | 2195 |
| 21 | 🇳🇿 NZ | 2097 |
| 22 | 🇹🇭 TH | 2053 |
| 23 | 🇰🇷 KR | 1973 |
| 24 | 🇵🇭 PH | 1836 |
| 25 | 🇬🇹 GT | 1808 |
| 26 | 🇲🇦 MA | 1416 |
| 27 | 🇲🇪 ME | 1325 |
| 28 | 🇳🇱 NL | 1252 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1183 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2780 |
| 2 | Denver International Airport |  | US | 2256 |
| 3 | Tokyo International Airport |  | JP | 1870 |
| 4 | Indira Gandhi International Airport |  | IN | 1721 |
| 5 | Harry Reid International Airport |  | US | 1654 |
| 6 | Guaymaral Airport |  | CO | 1627 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1565 |
| 8 | Zurich Airport |  | CH | 1484 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1413 |
| 10 | La Aurora Airport |  | GT | 1396 |
| 11 | Frankfurt am Main International Airport |  | DE | 1339 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1286 |
| 13 | Chicago O'Hare International Airport |  | US | 1277 |
| 14 | Salt Lake City International Airport |  | US | 1186 |
| 15 | Macau International Airport |  | MO | 1186 |
| 16 | El Dorado International Airport |  | CO | 1184 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1153 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1092 |
| 19 | Capua Airport |  | IT | 1092 |
| 20 | Madrid Barajas International Airport |  | ES | 1090 |
| 21 | Congonhas Airport |  | BR | 1062 |
| 22 | Kuala Lumpur International Airport |  | MY | 1029 |
| 23 | Charlotte/Douglas International Airport |  | US | 986 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 966 |
| 25 | Charles de Gaulle International Airport |  | FR | 958 |
| 26 | Bengaluru International Airport |  | IN | 940 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 914 |
| 28 | Malpensa International Airport |  | IT | 883 |
| 29 | Ninoy Aquino International Airport |  | PH | 853 |
| 30 | Daniel K Inouye International Airport |  | US | 831 |
| 31 | Barcelona International Airport |  | ES | 819 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 813 |
| 33 | Tenerife Norte Airport |  | ES | 802 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 784 |
| 35 | Calgary International Airport |  | CA | 775 |
| 36 | Seattle-Tacoma International Airport |  | US | 766 |
| 37 | Scottsdale Airport |  | US | 762 |
| 38 | Viracopos International Airport |  | BR | 759 |
| 39 | Vitoria/Foronda Airport |  | ES | 758 |
| 40 | Amsterdam Airport Schiphol |  | NL | 752 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 684 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 483 | 21m | 244 km | 2,033.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 333 | 24m | 225 km | 1,291.9 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 333 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 322 | 1h 10m | 770 km | 4,277.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 285 | 14m | 114 km | 559.0 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 251 | 26m | 275 km | 1,189.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 242 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 196 | 22m | 55 km | 186.3 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 185 | 26m | 215 km | 685.2 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 185 | 44m | 241 km | 768.5 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 184 | 20m | 99 km | 315.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 179 | 1h 46m | 1,423 km | 4,392.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 179 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 166 | 31m | 369 km | 1,056.6 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 162 | 18m | 144 km | 403.0 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 161 | 20m | 250 km | 695.4 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 160 | 30m | 49 km | 135.2 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 159 | 44m | 452 km | 1,239.2 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 156 | 1h 1m | 695 km | 1,870.0 t |
| 26 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 154 | 1h 16m | 961 km | 2,552.6 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 151 | 1h 38m | 1,156 km | 3,012.4 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 148 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N4692Q |  | Rogue Valley International/Medford Airport (KMFR) | Rogue Valley International/Medford Airport (KMFR) | 2026-07-08 18:36 UTC | 2026-07-08 19:35 UTC | 59m |
| N596HP |  | Atlanta Regional Falcon Field (KFFC) | Griffin-Spalding County Airport (K6A2) | 2026-07-08 19:17 UTC | 2026-07-08 19:28 UTC | 10m |
| MDANZ | MDA | Farnborough Airport (EGLF) | London City Airport (EGLC) | 2026-07-08 19:08 UTC | 2026-07-08 19:23 UTC | 15m |
| N5852K |  | Hopkins Field (KAIB) | Tanner Field (CO27) | 2026-07-08 18:06 UTC | 2026-07-08 19:21 UTC | 1h 15m |
| N90422 |  | Mirth Airport (WA22) | Boeing Field/King County International Airport (KBFI) | 2026-07-08 19:03 UTC | 2026-07-08 19:18 UTC | 15m |
| GLF84 | GLF | Savannah/Hilton Head International Airport (KSAV) | Plantation Airpark (KJYL) | 2026-07-08 18:04 UTC | 2026-07-08 19:18 UTC | 1h 13m |
| N212HF |  | Centennial Airport (KAPA) | Staples Municipal Airport (KSAZ) | 2026-07-08 17:53 UTC | 2026-07-08 19:16 UTC | 1h 23m |
| N9125M |  | Cortez Municipal Airport (KCEZ) | Tanner Field (CO27) | 2026-07-08 18:58 UTC | 2026-07-08 19:16 UTC | 17m |
| CGICZ | CGI | Morden Airport (CJA3) | Morden Airport (CJA3) | 2026-07-08 19:15 UTC | 2026-07-08 19:15 UTC | 0m |
| FRLD55 | FRL | Telluride Regional Airport (KTEX) | Blanding Municipal Airport (KBDG) | 2026-07-08 18:06 UTC | 2026-07-08 19:15 UTC | 1h 9m |
| N5378D |  | Lanett Regional Airport (K7A3) | Lanett Regional Airport (K7A3) | 2026-07-08 18:47 UTC | 2026-07-08 19:13 UTC | 26m |
| N647AG |  | Camarillo Airport (KCMA) | Santa Monica Municipal Airport (KSMO) | 2026-07-08 18:43 UTC | 2026-07-08 19:09 UTC | 25m |
| N922RA |  | Frederick Douglass/Greater Rochester International Airport (KROC) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-07-08 17:45 UTC | 2026-07-08 19:08 UTC | 1h 23m |
| N57MG |  | Reedley Municipal Airport (KO32) | Lake Tahoe Airport (KTVL) | 2026-07-08 18:36 UTC | 2026-07-08 19:07 UTC | 31m |
| N754MH |  | Warren County/John Lane Field (KI68) | Warren County/John Lane Field (KI68) | 2026-07-08 18:28 UTC | 2026-07-08 19:05 UTC | 36m |
| AAL1151 | American Airlines | Los Angeles International Airport (KLAX) | Philadelphia International Airport (KPHL) | 2026-07-08 14:23 UTC | 2026-07-08 19:05 UTC | 4h 42m |
| CXK404 | CXK | Ogden-Hinckley Airport (KOGD) | Ogden-Hinckley Airport (KOGD) | 2026-07-08 18:30 UTC | 2026-07-08 19:02 UTC | 31m |
| N537AR |  | CL24 (CL24) | Table Mountain Field (5CL9) | 2026-07-08 16:10 UTC | 2026-07-08 19:00 UTC | 2h 50m |
| N17ED |  | Ross County Airport (KRZT) | Murphy Airport (3II0) | 2026-07-08 18:31 UTC | 2026-07-08 18:59 UTC | 28m |
| N354WA |  | Midwest Ntl Air Center Airport (KGPH) | Miller-Herrold Airport (28MI) | 2026-07-08 17:09 UTC | 2026-07-08 18:59 UTC | 1h 50m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
