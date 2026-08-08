# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_12:43:45_UTC-green)

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

**Latest saved flight:** 2026-08-08 12:43:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 12:43:45 UTC

- **178,127** saved flights
- **57,243** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **178,127** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,140,949.7 tonnes** estimated CO2 emissions
- **124,113,028 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7065 |
| 2 | SkyWest Airlines | 6496 |
| 3 | EJA | 3508 |
| 4 | IndiGo | 3134 |
| 5 | Southwest Airlines | 2804 |
| 6 | American Airlines | 2772 |
| 7 | ENY | 2213 |
| 8 | Delta Air Lines | 2100 |
| 9 | LATAM Airlines | 1649 |
| 10 | Lufthansa | 1594 |
| 11 | AZU | 1584 |
| 12 | WIF | 1490 |
| 13 | Vueling | 1468 |
| 14 | LXJ | 1397 |
| 15 | Swiss International | 1215 |
| 16 | AXM | 1209 |
| 17 | easyJet | 1207 |
| 18 | QLK | 1093 |
| 19 | All Nippon Airways | 1088 |
| 20 | EJU | 1084 |
| 21 | Alaska Airlines | 1081 |
| 22 | VIV | 979 |
| 23 | Cathay Pacific | 946 |
| 24 | CXK | 943 |
| 25 | GLO | 940 |
| 26 | AEE | 928 |
| 27 | United Airlines | 919 |
| 28 | Air France | 918 |
| 29 | MXY | 896 |
| 30 | PGT | 881 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 152775 |
| 2 | 🇪🇸 ES | 11411 |
| 3 | 🇧🇷 BR | 10152 |
| 4 | 🇦🇺 AU | 10068 |
| 5 | 🇮🇳 IN | 9826 |
| 6 | 🇨🇦 CA | 9731 |
| 7 | 🇮🇹 IT | 9211 |
| 8 | 🇩🇪 DE | 8817 |
| 9 | 🇬🇧 GB | 8229 |
| 10 | 🇯🇵 JP | 7227 |
| 11 | 🇫🇷 FR | 7081 |
| 12 | 🇨🇴 CO | 6535 |
| 13 | 🇬🇷 GR | 5197 |
| 14 | 🇲🇽 MX | 5097 |
| 15 | 🇨🇭 CH | 4740 |
| 16 | 🇳🇴 NO | 4628 |
| 17 | 🇹🇷 TR | 4469 |
| 18 | 🇲🇾 MY | 3156 |
| 19 | 🇵🇱 PL | 2966 |
| 20 | 🇿🇦 ZA | 2906 |
| 21 | 🇹🇭 TH | 2703 |
| 22 | 🇳🇿 NZ | 2582 |
| 23 | 🇵🇭 PH | 2358 |
| 24 | 🇬🇹 GT | 2270 |
| 25 | 🇰🇷 KR | 2240 |
| 26 | 🇲🇦 MA | 1799 |
| 27 | 🇭🇷 HR | 1762 |
| 28 | 🇲🇪 ME | 1622 |
| 29 | 🇳🇱 NL | 1604 |
| 30 | 🇲🇴 MO | 1510 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3673 |
| 2 | Denver International Airport |  | US | 2949 |
| 3 | Tokyo International Airport |  | JP | 2245 |
| 4 | Indira Gandhi International Airport |  | IN | 2187 |
| 5 | Guaymaral Airport |  | CO | 2177 |
| 6 | Harry Reid International Airport |  | US | 2113 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1924 |
| 8 | Zurich Airport |  | CH | 1891 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1854 |
| 10 | La Aurora Airport |  | GT | 1745 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1627 |
| 12 | Chicago O'Hare International Airport |  | US | 1599 |
| 13 | Salt Lake City International Airport |  | US | 1591 |
| 14 | El Dorado International Airport |  | CO | 1586 |
| 15 | Frankfurt am Main International Airport |  | DE | 1556 |
| 16 | Macau International Airport |  | MO | 1510 |
| 17 | Congonhas Airport |  | BR | 1474 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1428 |
| 19 | Capua Airport |  | IT | 1395 |
| 20 | Madrid Barajas International Airport |  | ES | 1390 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1322 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1257 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1248 |
| 24 | Malpensa International Airport |  | IT | 1221 |
| 25 | Charlotte/Douglas International Airport |  | US | 1212 |
| 26 | Charles de Gaulle International Airport |  | FR | 1209 |
| 27 | Kuala Lumpur International Airport |  | MY | 1189 |
| 28 | Bengaluru International Airport |  | IN | 1169 |
| 29 | Ninoy Aquino International Airport |  | PH | 1109 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1103 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1098 |
| 32 | Barcelona International Airport |  | ES | 1059 |
| 33 | Daniel K Inouye International Airport |  | US | 1025 |
| 34 | Seattle-Tacoma International Airport |  | US | 1025 |
| 35 | Viracopos International Airport |  | BR | 1018 |
| 36 | Reno/Tahoe International Airport |  | US | 1014 |
| 37 | Calgary International Airport |  | CA | 1012 |
| 38 | Oslo Gardermoen Airport |  | NO | 992 |
| 39 | Tenerife Norte Airport |  | ES | 975 |
| 40 | Amsterdam Airport Schiphol |  | NL | 963 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 899 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 655 | 21m | 244 km | 2,758.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 420 | 1h 8m | 770 km | 5,579.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 420 | 24m | 225 km | 1,629.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 414 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 299 | 27m | 275 km | 1,416.8 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 294 | 1h 7m | 706 km | 3,579.5 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 270 | 44m | 241 km | 1,121.5 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 249 | 1h 48m | 1,423 km | 6,110.9 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 231 | 20m | 250 km | 997.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 226 | 26m | 215 km | 837.0 t |
| 19 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 225 | 8m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 220 | 20m | 99 km | 376.8 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 215 | 51m | 556 km | 2,061.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 212 | 1h 15m | 961 km | 3,514.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 212 | 19m | 144 km | 527.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 209 | 1h 38m | 1,156 km | 4,169.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 208 | 12m | - | - |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 206 | 31m | 369 km | 1,311.2 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 203 | 24m | 218 km | 764.8 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 201 | 28m | 152 km | 525.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 194 | 1h 2m | 695 km | 2,325.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HBZUZ | HBZ | Samedan Airport (LSZS) | Raron Airport (LSTA) | 2026-08-08 12:00 UTC | 2026-08-08 12:43 UTC | 42m |
| MVK93 | MVK | Mankato Regional Airport (KMKT) | Waseca Municipal/Maynard Richard Stensrud Field (KACQ) | 2026-08-08 11:50 UTC | 2026-08-08 12:42 UTC | 51m |
| N621HS |  | Landings Condominium Airport (82IS) | Ruder Airport (59IL) | 2026-08-08 12:19 UTC | 2026-08-08 12:34 UTC | 14m |
| FJJJY | FJJ | Saint-Nazaire-Montoir Airport (LFRZ) | Saint-Nazaire-Montoir Airport (LFRZ) | 2026-08-08 11:55 UTC | 2026-08-08 12:31 UTC | 36m |
| CFE1T | CFE | Exeter International Airport (EGTE) | Exeter International Airport (EGTE) | 2026-08-08 12:07 UTC | 2026-08-08 12:28 UTC | 21m |
| N1679H |  | Lake Elmo Airport (K21D) | Lake Elmo Airport (K21D) | 2026-08-08 12:07 UTC | 2026-08-08 12:28 UTC | 21m |
| FIH40 | FIH | Seinajoki Airport (EFSI) | Seinajoki Airport (EFSI) | 2026-08-08 12:24 UTC | 2026-08-08 12:27 UTC | 2m |
| N68FF |  | Treasure Coast International Airport (KFPR) | Treasure Coast International Airport (KFPR) | 2026-08-08 12:15 UTC | 2026-08-08 12:26 UTC | 10m |
| N75FF |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-08-08 11:58 UTC | 2026-08-08 12:22 UTC | 24m |
| N71HR |  | Atlantic City International Airport (KACY) | Savannah/Hilton Head International Airport (KSAV) | 2026-08-08 10:50 UTC | 2026-08-08 12:16 UTC | 1h 26m |
| N1370E |  | Cobb County International/Mccollum Field (KRYY) | Athens/Ben Epps Airport (KAHN) | 2026-08-08 11:29 UTC | 2026-08-08 12:13 UTC | 44m |
| EJA419 | EJA | Toronto Pearson International Airport (CYYZ) | Toronto Pearson International Airport (CYYZ) | 2026-08-08 11:41 UTC | 2026-08-08 12:08 UTC | 26m |
| N734VQ |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-08-08 11:35 UTC | 2026-08-08 12:06 UTC | 31m |
| RYR55CW | Ryanair | Barcelona International Airport (LEBL) | Damyns Hall Aerodrome (EGML) | 2026-08-08 10:06 UTC | 2026-08-08 12:05 UTC | 1h 59m |
| HB3463 |  | St Stephan Airport (LSTS) | St Stephan Airport (LSTS) | 2026-08-08 11:50 UTC | 2026-08-08 12:05 UTC | 14m |
| RYR1599 | Ryanair | Nuremberg Airport (EDDN) | Ampuriabrava Airport (LEAP) | 2026-08-08 10:37 UTC | 2026-08-08 12:05 UTC | 1h 27m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-08 11:57 UTC | 2026-08-08 12:04 UTC | 7m |
| N41JA |  | Lakewood Airport (KN12) | Ocean County Airport (KMJX) | 2026-08-08 11:25 UTC | 2026-08-08 12:03 UTC | 38m |
| GFOXP | GFO | EG32 (EG32) | EG32 (EG32) | 2026-08-08 10:14 UTC | 2026-08-08 12:03 UTC | 1h 48m |
| N665HF |  | Sinton Airport (KT69) | Cabaniss Field Nolf Airport (KNGW) | 2026-08-08 11:50 UTC | 2026-08-08 12:02 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
