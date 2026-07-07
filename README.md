# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--07_18:11:46_UTC-green)

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

**Latest saved flight:** 2026-07-07 18:11:46 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-07 18:11:46 UTC

- **132,467** saved flights
- **44,953** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **132,467** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,595,685.9 tonnes** estimated CO2 emissions
- **92,503,530 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5390 |
| 2 | SkyWest Airlines | 4902 |
| 3 | EJA | 2602 |
| 4 | IndiGo | 2468 |
| 5 | American Airlines | 2064 |
| 6 | Southwest Airlines | 1996 |
| 7 | ENY | 1666 |
| 8 | Delta Air Lines | 1587 |
| 9 | Lufthansa | 1379 |
| 10 | LATAM Airlines | 1218 |
| 11 | Vueling | 1163 |
| 12 | WIF | 1155 |
| 13 | AZU | 1124 |
| 14 | LXJ | 1020 |
| 15 | AXM | 1017 |
| 16 | Swiss International | 941 |
| 17 | All Nippon Airways | 868 |
| 18 | easyJet | 846 |
| 19 | Alaska Airlines | 842 |
| 20 | QLK | 825 |
| 21 | EJU | 817 |
| 22 | VIV | 731 |
| 23 | AEE | 719 |
| 24 | Air France | 718 |
| 25 | Cathay Pacific | 716 |
| 26 | CXK | 712 |
| 27 | United Airlines | 703 |
| 28 | JetBlue | 695 |
| 29 | MXY | 686 |
| 30 | GLO | 680 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 113559 |
| 2 | 🇪🇸 ES | 8813 |
| 3 | 🇮🇳 IN | 7739 |
| 4 | 🇦🇺 AU | 7610 |
| 5 | 🇧🇷 BR | 7473 |
| 6 | 🇨🇦 CA | 7001 |
| 7 | 🇩🇪 DE | 6933 |
| 8 | 🇮🇹 IT | 6914 |
| 9 | 🇬🇧 GB | 5919 |
| 10 | 🇯🇵 JP | 5685 |
| 11 | 🇫🇷 FR | 5269 |
| 12 | 🇨🇴 CO | 4165 |
| 13 | 🇲🇽 MX | 3867 |
| 14 | 🇬🇷 GR | 3792 |
| 15 | 🇳🇴 NO | 3588 |
| 16 | 🇨🇭 CH | 3426 |
| 17 | 🇹🇷 TR | 2953 |
| 18 | 🇲🇾 MY | 2634 |
| 19 | 🇵🇱 PL | 2186 |
| 20 | 🇿🇦 ZA | 2181 |
| 21 | 🇳🇿 NZ | 2091 |
| 22 | 🇹🇭 TH | 2039 |
| 23 | 🇰🇷 KR | 1968 |
| 24 | 🇵🇭 PH | 1817 |
| 25 | 🇬🇹 GT | 1800 |
| 26 | 🇲🇦 MA | 1406 |
| 27 | 🇲🇪 ME | 1314 |
| 28 | 🇳🇱 NL | 1248 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1168 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2768 |
| 2 | Denver International Airport |  | US | 2247 |
| 3 | Tokyo International Airport |  | JP | 1865 |
| 4 | Indira Gandhi International Airport |  | IN | 1712 |
| 5 | Harry Reid International Airport |  | US | 1646 |
| 6 | Guaymaral Airport |  | CO | 1621 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1556 |
| 8 | Zurich Airport |  | CH | 1475 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1411 |
| 10 | La Aurora Airport |  | GT | 1390 |
| 11 | Frankfurt am Main International Airport |  | DE | 1336 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1274 |
| 13 | Chicago O'Hare International Airport |  | US | 1272 |
| 14 | Macau International Airport |  | MO | 1186 |
| 15 | El Dorado International Airport |  | CO | 1183 |
| 16 | Salt Lake City International Airport |  | US | 1180 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1144 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1085 |
| 19 | Madrid Barajas International Airport |  | ES | 1085 |
| 20 | Capua Airport |  | IT | 1083 |
| 21 | Congonhas Airport |  | BR | 1058 |
| 22 | Kuala Lumpur International Airport |  | MY | 1023 |
| 23 | Charlotte/Douglas International Airport |  | US | 986 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 957 |
| 25 | Charles de Gaulle International Airport |  | FR | 957 |
| 26 | Bengaluru International Airport |  | IN | 933 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 909 |
| 28 | Malpensa International Airport |  | IT | 881 |
| 29 | Ninoy Aquino International Airport |  | PH | 843 |
| 30 | Daniel K Inouye International Airport |  | US | 826 |
| 31 | Barcelona International Airport |  | ES | 817 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 808 |
| 33 | Tenerife Norte Airport |  | ES | 797 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 779 |
| 35 | Calgary International Airport |  | CA | 773 |
| 36 | Seattle-Tacoma International Airport |  | US | 761 |
| 37 | Scottsdale Airport |  | US | 761 |
| 38 | Vitoria/Foronda Airport |  | ES | 755 |
| 39 | Viracopos International Airport |  | BR | 754 |
| 40 | Amsterdam Airport Schiphol |  | NL | 750 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 681 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 479 | 21m | 244 km | 2,016.9 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 331 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 329 | 24m | 225 km | 1,276.4 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 321 | 1h 10m | 770 km | 4,264.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 284 | 14m | 114 km | 557.0 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 250 | 26m | 275 km | 1,184.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 241 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 194 | 22m | 55 km | 184.4 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 185 | 44m | 241 km | 768.5 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 184 | 26m | 215 km | 681.5 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 183 | 20m | 99 km | 313.5 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 178 | 1h 46m | 1,423 km | 4,368.4 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 178 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 165 | 31m | 369 km | 1,050.3 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 162 | 18m | 144 km | 403.0 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 161 | 20m | 250 km | 695.4 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 160 | 30m | 49 km | 135.2 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 159 | 44m | 452 km | 1,239.2 t |
| 25 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 155 | 1h 1m | 695 km | 1,858.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 154 | 1h 16m | 961 km | 2,552.6 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 150 | 1h 38m | 1,156 km | 2,992.4 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 148 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N144PW |  | Charlotte/Monroe Executive Airport (KEQY) | Burlington/Alamance Regional Airport (KBUY) | 2026-07-07 16:49 UTC | 2026-07-07 18:11 UTC | 1h 22m |
| N440EH |  | Carson City Airport (KCXP) | Crowley Ranch Airstrip (78OR) | 2026-07-07 15:07 UTC | 2026-07-07 18:06 UTC | 2h 58m |
| OUA6 | OUA | University Of Oklahoma Westheimer Airport (KOUN) | University Of Oklahoma Westheimer Airport (KOUN) | 2026-07-07 17:37 UTC | 2026-07-07 18:01 UTC | 24m |
| BRW149 | BRW | Flying Cloud Airport (KFCM) | Flying Cloud Airport (KFCM) | 2026-07-07 17:32 UTC | 2026-07-07 17:59 UTC | 26m |
| N268DS |  | Frederick Douglass/Greater Rochester International Airport (KROC) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-07-07 17:28 UTC | 2026-07-07 17:55 UTC | 26m |
| N1082F |  | San Marcos Regional Airport (KHYI) | San Marcos Regional Airport (KHYI) | 2026-07-07 17:47 UTC | 2026-07-07 17:52 UTC | 5m |
| N7273M |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-07-07 16:46 UTC | 2026-07-07 17:50 UTC | 1h 3m |
| AWH92A | AWH | Hamburg Airport (EDDH) | Kiel-Holtenau Airport (EDHK) | 2026-07-07 17:29 UTC | 2026-07-07 17:49 UTC | 19m |
| ECA2SJ | ECA | Dusseldorf International Airport (EDDL) | Cologne Bonn Airport (EDDK) | 2026-07-07 17:26 UTC | 2026-07-07 17:48 UTC | 22m |
| AAL1451 | American Airlines | Los Angeles International Airport (KLAX) | Philadelphia International Airport (KPHL) | 2026-07-07 13:24 UTC | 2026-07-07 17:48 UTC | 4h 23m |
| N9831G |  | Chicago Executive Airport (KPWK) | Lake In The Hills Airport (K3CK) | 2026-07-07 17:27 UTC | 2026-07-07 17:47 UTC | 19m |
| N998RA |  | Frederick Douglass/Greater Rochester International Airport (KROC) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-07-07 16:58 UTC | 2026-07-07 17:41 UTC | 42m |
| N823SF |  | Licking County Regional Airport (KVTA) | Gerald R Ford International Airport (KGRR) | 2026-07-07 16:43 UTC | 2026-07-07 17:39 UTC | 55m |
| N8062W |  | Downey/Hyde Memorial/ Airport (KU58) | Downey/Hyde Memorial/ Airport (KU58) | 2026-07-07 16:47 UTC | 2026-07-07 17:39 UTC | 52m |
| CGOLC | CGO | Sechelt-Gibsons Airport (CAP3) | Nanaimo Airport (CYCD) | 2026-07-07 17:19 UTC | 2026-07-07 17:39 UTC | 19m |
| BTQ987 | BTQ | Coopers Landing Airport (0WN2) | OG08 (OG08) | 2026-07-07 17:27 UTC | 2026-07-07 17:38 UTC | 11m |
| ERU36 | ERU | AZ86 (AZ86) | 42AZ (42AZ) | 2026-07-07 17:14 UTC | 2026-07-07 17:38 UTC | 23m |
| BRG621 | BRG | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-07-07 16:51 UTC | 2026-07-07 17:36 UTC | 44m |
| CXK147 | CXK | Ann Arbor Municipal Airport (KARB) | Lautzenhiser Airpark (IN83) | 2026-07-07 16:28 UTC | 2026-07-07 17:35 UTC | 1h 6m |
| EJA888 | EJA | Van Nuys Airport (KVNY) | Moffett Federal Airfield (KNUQ) | 2026-07-07 16:49 UTC | 2026-07-07 17:35 UTC | 45m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
