# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--08_20:36:50_UTC-green)

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

**Latest saved flight:** 2026-07-08 20:36:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-08 20:36:50 UTC

- **133,492** saved flights
- **45,237** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **133,492** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,607,183.9 tonnes** estimated CO2 emissions
- **93,170,083 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5424 |
| 2 | SkyWest Airlines | 4933 |
| 3 | EJA | 2622 |
| 4 | IndiGo | 2487 |
| 5 | American Airlines | 2088 |
| 6 | Southwest Airlines | 2006 |
| 7 | ENY | 1676 |
| 8 | Delta Air Lines | 1597 |
| 9 | Lufthansa | 1383 |
| 10 | LATAM Airlines | 1227 |
| 11 | Vueling | 1171 |
| 12 | WIF | 1162 |
| 13 | AZU | 1135 |
| 14 | LXJ | 1024 |
| 15 | AXM | 1019 |
| 16 | Swiss International | 946 |
| 17 | All Nippon Airways | 871 |
| 18 | easyJet | 861 |
| 19 | Alaska Airlines | 848 |
| 20 | QLK | 830 |
| 21 | EJU | 821 |
| 22 | VIV | 735 |
| 23 | AEE | 725 |
| 24 | Cathay Pacific | 719 |
| 25 | CXK | 719 |
| 26 | Air France | 718 |
| 27 | United Airlines | 707 |
| 28 | JetBlue | 702 |
| 29 | MXY | 691 |
| 30 | GLO | 681 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 114502 |
| 2 | 🇪🇸 ES | 8866 |
| 3 | 🇮🇳 IN | 7795 |
| 4 | 🇦🇺 AU | 7702 |
| 5 | 🇧🇷 BR | 7520 |
| 6 | 🇨🇦 CA | 7051 |
| 7 | 🇩🇪 DE | 6964 |
| 8 | 🇮🇹 IT | 6943 |
| 9 | 🇬🇧 GB | 5977 |
| 10 | 🇯🇵 JP | 5719 |
| 11 | 🇫🇷 FR | 5302 |
| 12 | 🇨🇴 CO | 4173 |
| 13 | 🇲🇽 MX | 3890 |
| 14 | 🇬🇷 GR | 3823 |
| 15 | 🇳🇴 NO | 3615 |
| 16 | 🇨🇭 CH | 3446 |
| 17 | 🇹🇷 TR | 3016 |
| 18 | 🇲🇾 MY | 2647 |
| 19 | 🇵🇱 PL | 2202 |
| 20 | 🇿🇦 ZA | 2195 |
| 21 | 🇳🇿 NZ | 2097 |
| 22 | 🇹🇭 TH | 2054 |
| 23 | 🇰🇷 KR | 1973 |
| 24 | 🇵🇭 PH | 1836 |
| 25 | 🇬🇹 GT | 1810 |
| 26 | 🇲🇦 MA | 1418 |
| 27 | 🇲🇪 ME | 1328 |
| 28 | 🇳🇱 NL | 1252 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1184 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2785 |
| 2 | Denver International Airport |  | US | 2261 |
| 3 | Tokyo International Airport |  | JP | 1870 |
| 4 | Indira Gandhi International Airport |  | IN | 1721 |
| 5 | Harry Reid International Airport |  | US | 1658 |
| 6 | Guaymaral Airport |  | CO | 1627 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1567 |
| 8 | Zurich Airport |  | CH | 1485 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1419 |
| 10 | La Aurora Airport |  | GT | 1398 |
| 11 | Frankfurt am Main International Airport |  | DE | 1339 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1288 |
| 13 | Chicago O'Hare International Airport |  | US | 1277 |
| 14 | Salt Lake City International Airport |  | US | 1187 |
| 15 | Macau International Airport |  | MO | 1186 |
| 16 | El Dorado International Airport |  | CO | 1184 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1154 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1096 |
| 19 | Capua Airport |  | IT | 1095 |
| 20 | Madrid Barajas International Airport |  | ES | 1093 |
| 21 | Congonhas Airport |  | BR | 1064 |
| 22 | Kuala Lumpur International Airport |  | MY | 1029 |
| 23 | Charlotte/Douglas International Airport |  | US | 986 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 966 |
| 25 | Charles de Gaulle International Airport |  | FR | 958 |
| 26 | Bengaluru International Airport |  | IN | 940 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 916 |
| 28 | Malpensa International Airport |  | IT | 883 |
| 29 | Ninoy Aquino International Airport |  | PH | 853 |
| 30 | Daniel K Inouye International Airport |  | US | 831 |
| 31 | Barcelona International Airport |  | ES | 821 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 814 |
| 33 | Tenerife Norte Airport |  | ES | 802 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 785 |
| 35 | Calgary International Airport |  | CA | 776 |
| 36 | Seattle-Tacoma International Airport |  | US | 767 |
| 37 | Scottsdale Airport |  | US | 764 |
| 38 | Viracopos International Airport |  | BR | 761 |
| 39 | Vitoria/Foronda Airport |  | ES | 758 |
| 40 | Amsterdam Airport Schiphol |  | NL | 752 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 684 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 483 | 21m | 244 km | 2,033.8 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 334 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 333 | 24m | 225 km | 1,291.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 322 | 1h 10m | 770 km | 4,277.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 285 | 14m | 114 km | 559.0 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 251 | 26m | 275 km | 1,189.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 242 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 196 | 22m | 55 km | 186.3 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 186 | 44m | 241 km | 772.6 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 185 | 26m | 215 km | 685.2 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 184 | 20m | 99 km | 315.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 179 | 1h 46m | 1,423 km | 4,392.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 179 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 166 | 31m | 369 km | 1,056.6 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 163 | 18m | 144 km | 405.5 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 161 | 20m | 250 km | 695.4 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 160 | 30m | 49 km | 135.2 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 159 | 44m | 452 km | 1,239.2 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 156 | 1h 1m | 695 km | 1,870.0 t |
| 26 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 155 | 1h 16m | 961 km | 2,569.2 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 151 | 1h 38m | 1,156 km | 3,012.4 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 148 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FRLD55 | FRL | Blanding Municipal Airport (KBDG) | Blanding Municipal Airport (KBDG) | 2026-07-08 20:19 UTC | 2026-07-08 20:36 UTC | 16m |
| N402HE |  | Millard Airport (KMLE) | Lincoln Airport (KLNK) | 2026-07-08 20:08 UTC | 2026-07-08 20:34 UTC | 25m |
| N893AE |  | II45 (II45) | II01 (II01) | 2026-07-08 20:00 UTC | 2026-07-08 20:28 UTC | 27m |
| N793CG |  | Lincoln Airport (KLNK) | Lincoln Airport (KLNK) | 2026-07-08 19:26 UTC | 2026-07-08 20:27 UTC | 1h 1m |
| FFAB123 | FFA | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-07-08 17:56 UTC | 2026-07-08 20:27 UTC | 2h 30m |
| JBU2184 | JetBlue | Raleigh-Durham International Airport (KRDU) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-08 19:05 UTC | 2026-07-08 20:26 UTC | 1h 21m |
| DHX821 | DHX | Bahrain International Airport (OBBI) | Zhuhai Airport (ZGSD) | 2026-07-08 09:28 UTC | 2026-07-08 20:16 UTC | 10h 47m |
| N52654 |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-07-08 19:54 UTC | 2026-07-08 20:14 UTC | 19m |
| WIRE31 | WIR | 75OK (75OK) | Miller Brothers Airport (OK47) | 2026-07-08 19:40 UTC | 2026-07-08 20:13 UTC | 33m |
| BLOOD01 | BLO | Ansbach-Petersdorf Airport (EDQF) | Ansbach-Petersdorf Airport (EDQF) | 2026-07-08 15:21 UTC | 2026-07-08 20:13 UTC | 4h 51m |
| N737LG |  | Ohio State University Airport (KOSU) | Madison County Airport (KUYF) | 2026-07-08 19:28 UTC | 2026-07-08 20:08 UTC | 39m |
| VM553 |  | Sampleys Airport (28AZ) | Massey Farm Airport (AZ34) | 2026-07-08 19:05 UTC | 2026-07-08 20:06 UTC | 1h 1m |
| N36HF |  | KHTO (KHTO) | Westchester County Airport (KHPN) | 2026-07-08 19:31 UTC | 2026-07-08 20:04 UTC | 33m |
| WDE01 | WDE | City Of Colorado Springs Municipal Airport (KCOS) | Mud Lake/West Jefferson County Airport (K1U2) | 2026-07-08 18:07 UTC | 2026-07-08 20:03 UTC | 1h 55m |
| N22271 |  | Willow Creek Airport (WI77) | 1WN2 (1WN2) | 2026-07-08 19:38 UTC | 2026-07-08 20:03 UTC | 25m |
| VAR410 | VAR | Phoenix Goodyear Airport (KGYR) | Bishop Airfield (1AZ0) | 2026-07-08 19:17 UTC | 2026-07-08 20:03 UTC | 45m |
|  |  | Nikolai Creek Airport (9AK3) | Nikolai Creek Airport (9AK3) | 2026-07-08 20:00 UTC | 2026-07-08 20:01 UTC | 0m |
| N19629 |  | Concord Municipal Airport (KCON) | Concord Municipal Airport (KCON) | 2026-07-08 19:52 UTC | 2026-07-08 19:59 UTC | 7m |
| EPA2501 | EPA | Shenzhen Bao'an International Airport (ZGSZ) | Zhuhai Airport (ZGSD) | 2026-07-08 19:46 UTC | 2026-07-08 19:59 UTC | 12m |
| TKR140 | TKR | Glenns Ferry Municipal Airport (KU89) | Crowley Ranch Airstrip (78OR) | 2026-07-08 19:36 UTC | 2026-07-08 19:57 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
