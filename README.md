# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_21:08:52_UTC-green)

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

**Latest saved flight:** 2026-08-04 21:08:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-04 21:08:52 UTC

- **171,190** saved flights
- **55,717** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **171,190** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,063,198.9 tonnes** estimated CO2 emissions
- **119,605,731 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6821 |
| 2 | SkyWest Airlines | 6256 |
| 3 | EJA | 3399 |
| 4 | IndiGo | 3005 |
| 5 | Southwest Airlines | 2698 |
| 6 | American Airlines | 2692 |
| 7 | ENY | 2131 |
| 8 | Delta Air Lines | 2036 |
| 9 | LATAM Airlines | 1585 |
| 10 | Lufthansa | 1564 |
| 11 | AZU | 1507 |
| 12 | WIF | 1433 |
| 13 | Vueling | 1407 |
| 14 | LXJ | 1342 |
| 15 | AXM | 1176 |
| 16 | Swiss International | 1167 |
| 17 | easyJet | 1155 |
| 18 | EJU | 1048 |
| 19 | Alaska Airlines | 1044 |
| 20 | QLK | 1041 |
| 21 | All Nippon Airways | 1036 |
| 22 | VIV | 943 |
| 23 | Cathay Pacific | 918 |
| 24 | CXK | 913 |
| 25 | United Airlines | 901 |
| 26 | GLO | 896 |
| 27 | AEE | 893 |
| 28 | Air France | 879 |
| 29 | MXY | 871 |
| 30 | JetBlue | 858 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 147589 |
| 2 | 🇪🇸 ES | 10977 |
| 3 | 🇧🇷 BR | 9732 |
| 4 | 🇦🇺 AU | 9521 |
| 5 | 🇮🇳 IN | 9413 |
| 6 | 🇨🇦 CA | 9353 |
| 7 | 🇮🇹 IT | 8860 |
| 8 | 🇩🇪 DE | 8506 |
| 9 | 🇬🇧 GB | 7941 |
| 10 | 🇯🇵 JP | 6872 |
| 11 | 🇫🇷 FR | 6788 |
| 12 | 🇨🇴 CO | 6225 |
| 13 | 🇬🇷 GR | 4977 |
| 14 | 🇲🇽 MX | 4901 |
| 15 | 🇨🇭 CH | 4499 |
| 16 | 🇳🇴 NO | 4469 |
| 17 | 🇹🇷 TR | 4183 |
| 18 | 🇲🇾 MY | 3057 |
| 19 | 🇵🇱 PL | 2876 |
| 20 | 🇿🇦 ZA | 2770 |
| 21 | 🇹🇭 TH | 2486 |
| 22 | 🇳🇿 NZ | 2471 |
| 23 | 🇵🇭 PH | 2255 |
| 24 | 🇬🇹 GT | 2200 |
| 25 | 🇰🇷 KR | 2161 |
| 26 | 🇲🇦 MA | 1722 |
| 27 | 🇭🇷 HR | 1650 |
| 28 | 🇲🇪 ME | 1573 |
| 29 | 🇳🇱 NL | 1555 |
| 30 | 🇲🇴 MO | 1463 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3524 |
| 2 | Denver International Airport |  | US | 2831 |
| 3 | Tokyo International Airport |  | JP | 2156 |
| 4 | Guaymaral Airport |  | CO | 2122 |
| 5 | Indira Gandhi International Airport |  | IN | 2088 |
| 6 | Harry Reid International Airport |  | US | 2054 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1868 |
| 8 | Zurich Airport |  | CH | 1809 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1802 |
| 10 | La Aurora Airport |  | GT | 1698 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1579 |
| 12 | Chicago O'Hare International Airport |  | US | 1553 |
| 13 | El Dorado International Airport |  | CO | 1552 |
| 14 | Salt Lake City International Airport |  | US | 1535 |
| 15 | Frankfurt am Main International Airport |  | DE | 1527 |
| 16 | Macau International Airport |  | MO | 1463 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1404 |
| 18 | Congonhas Airport |  | BR | 1401 |
| 19 | Madrid Barajas International Airport |  | ES | 1341 |
| 20 | Capua Airport |  | IT | 1336 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1292 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1208 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1193 |
| 24 | Charlotte/Douglas International Airport |  | US | 1188 |
| 25 | Charles de Gaulle International Airport |  | FR | 1161 |
| 26 | Malpensa International Airport |  | IT | 1154 |
| 27 | Kuala Lumpur International Airport |  | MY | 1151 |
| 28 | Bengaluru International Airport |  | IN | 1120 |
| 29 | Norman Y Mineta San Jose International Airport |  | US | 1065 |
| 30 | Ninoy Aquino International Airport |  | PH | 1061 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1055 |
| 32 | Barcelona International Airport |  | ES | 1014 |
| 33 | Daniel K Inouye International Airport |  | US | 992 |
| 34 | Seattle-Tacoma International Airport |  | US | 988 |
| 35 | Viracopos International Airport |  | BR | 973 |
| 36 | Calgary International Airport |  | CA | 970 |
| 37 | Reno/Tahoe International Airport |  | US | 964 |
| 38 | Oslo Gardermoen Airport |  | NO | 954 |
| 39 | Tenerife Norte Airport |  | ES | 952 |
| 40 | Scottsdale Airport |  | US | 941 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 879 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 625 | 21m | 244 km | 2,631.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 405 | 24m | 225 km | 1,571.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 405 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 387 | 1h 8m | 770 km | 5,141.0 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 318 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 292 | 27m | 275 km | 1,383.7 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 256 | 44m | 241 km | 1,063.4 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 255 | 22m | 55 km | 242.4 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 235 | 1h 47m | 1,423 km | 5,767.3 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 224 | 20m | 250 km | 967.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 222 | 26m | 215 km | 822.2 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 218 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 211 | 20m | 99 km | 361.4 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 204 | 50m | 556 km | 1,955.5 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 203 | 1h 15m | 961 km | 3,364.8 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 203 | 19m | 144 km | 505.0 t |
| 24 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 199 | 12m | - | - |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 197 | 31m | 369 km | 1,254.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 194 | 1h 38m | 1,156 km | 3,870.2 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 188 | 24m | 218 km | 708.3 t |
| 29 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 188 | 8m | - | - |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 186 | 1h 1m | 695 km | 2,229.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N250RM |  | Pioneer Village Field (K0V3) | Lincoln Airport (KLNK) | 2026-08-04 20:40 UTC | 2026-08-04 21:08 UTC | 28m |
| POE146 | POE | Montréal / St-Hubert Airport (CYHU) | Peterborough Airport (CYPQ) | 2026-08-04 20:03 UTC | 2026-08-04 21:03 UTC | 1h 0m |
| N9887C |  | Michigan City Municipal-Phillips Field (KMGC) | La Porte Municipal Airport (KPPO) | 2026-08-04 20:50 UTC | 2026-08-04 21:02 UTC | 11m |
| N5721T |  | Boeing Field/King County International Airport (KBFI) | WA05 (WA05) | 2026-08-04 20:02 UTC | 2026-08-04 21:01 UTC | 59m |
| N272SF |  | Bellingham International Airport (KBLI) | William R Fairchild International Airport (KCLM) | 2026-08-04 20:02 UTC | 2026-08-04 20:58 UTC | 55m |
| N424RP |  | Falcon Field (KFFZ) | Coolidge Municipal Airport (KP08) | 2026-08-04 20:01 UTC | 2026-08-04 20:55 UTC | 54m |
| MAC828Q | MAC | Charles de Gaulle International Airport (LFPG) | Kenitra Airport (GMMY) | 2026-08-04 18:35 UTC | 2026-08-04 20:54 UTC | 2h 19m |
| N32403 |  | Phyllis Field (6IL2) | De Kalb Taylor Municipal Airport (KDKB) | 2026-08-04 20:33 UTC | 2026-08-04 20:54 UTC | 21m |
| EJU63MP | EJU | Ibiza Airport (LEIB) | Napoli / Capodichino International Airport (LIRN) | 2026-08-04 19:18 UTC | 2026-08-04 20:50 UTC | 1h 32m |
| N53402 |  | Concord Municipal Airport (KCON) | Concord Municipal Airport (KCON) | 2026-08-04 20:18 UTC | 2026-08-04 20:49 UTC | 30m |
| EDV5343 | EDV | Laguardia Airport (KLGA) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-08-04 20:02 UTC | 2026-08-04 20:46 UTC | 44m |
| VTM503 | VTM | Plan De Guadalupe International Airport (MMIO) | Monclova International Airport (MMMV) | 2026-08-04 20:29 UTC | 2026-08-04 20:46 UTC | 17m |
| JIA5667 | JIA | Ronald Reagan Washington Ntl Airport (KDCA) | Toronto Pearson International Airport (CYYZ) | 2026-08-04 19:49 UTC | 2026-08-04 20:46 UTC | 56m |
| ARCAS11 | ARC | Danaher Airport (7TX0) | 54TS (54TS) | 2026-08-04 20:32 UTC | 2026-08-04 20:45 UTC | 12m |
| N441BW |  | Chicago Executive Airport (KPWK) | Thunder Bay Airport (CYQT) | 2026-08-04 19:09 UTC | 2026-08-04 20:39 UTC | 1h 30m |
| N605T |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-04 19:47 UTC | 2026-08-04 20:36 UTC | 48m |
| BOE115 | BOE | Boeing Field/King County International Airport (KBFI) | Christensen Field (8WA6) | 2026-08-04 18:16 UTC | 2026-08-04 20:34 UTC | 2h 18m |
| N509CX |  | Rhode Island Tf Green International Airport (KPVD) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-04 18:58 UTC | 2026-08-04 20:34 UTC | 1h 35m |
| N408GG |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-04 20:06 UTC | 2026-08-04 20:33 UTC | 26m |
| N914LD |  | John Wayne/Orange County Airport (KSNA) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-04 19:41 UTC | 2026-08-04 20:32 UTC | 51m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
