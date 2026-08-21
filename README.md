# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_15:06:12_UTC-green)

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

**Latest saved flight:** 2026-08-21 15:06:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 15:06:12 UTC

- **222,389** saved flights
- **69,539** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **222,389** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,678,134.1 tonnes** estimated CO2 emissions
- **155,254,150 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8922 |
| 2 | SkyWest Airlines | 7893 |
| 3 | EJA | 4292 |
| 4 | IndiGo | 3773 |
| 5 | American Airlines | 3674 |
| 6 | Southwest Airlines | 3493 |
| 7 | Delta Air Lines | 2854 |
| 8 | ENY | 2725 |
| 9 | LATAM Airlines | 2116 |
| 10 | AZU | 2043 |
| 11 | Vueling | 1876 |
| 12 | Lufthansa | 1840 |
| 13 | WIF | 1781 |
| 14 | LXJ | 1746 |
| 15 | easyJet | 1540 |
| 16 | Swiss International | 1480 |
| 17 | AXM | 1466 |
| 18 | QLK | 1405 |
| 19 | EJU | 1392 |
| 20 | United Airlines | 1392 |
| 21 | Alaska Airlines | 1353 |
| 22 | All Nippon Airways | 1333 |
| 23 | PGT | 1220 |
| 24 | GLO | 1216 |
| 25 | VIV | 1210 |
| 26 | Air France | 1207 |
| 27 | WMT | 1184 |
| 28 | Wizz Air | 1144 |
| 29 | JetBlue | 1119 |
| 30 | AEE | 1110 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 186561 |
| 2 | 🇪🇸 ES | 14257 |
| 3 | 🇧🇷 BR | 12859 |
| 4 | 🇦🇺 AU | 12653 |
| 5 | 🇨🇦 CA | 12271 |
| 6 | 🇮🇹 IT | 11859 |
| 7 | 🇮🇳 IN | 11769 |
| 8 | 🇩🇪 DE | 10979 |
| 9 | 🇬🇧 GB | 10436 |
| 10 | 🇨🇴 CO | 9149 |
| 11 | 🇯🇵 JP | 9054 |
| 12 | 🇫🇷 FR | 8869 |
| 13 | 🇬🇷 GR | 6493 |
| 14 | 🇹🇷 TR | 6453 |
| 15 | 🇲🇽 MX | 6167 |
| 16 | 🇨🇭 CH | 5862 |
| 17 | 🇳🇴 NO | 5538 |
| 18 | 🇲🇾 MY | 3885 |
| 19 | 🇿🇦 ZA | 3835 |
| 20 | 🇹🇭 TH | 3770 |
| 21 | 🇵🇱 PL | 3693 |
| 22 | 🇳🇿 NZ | 3089 |
| 23 | 🇵🇭 PH | 3016 |
| 24 | 🇬🇹 GT | 2805 |
| 25 | 🇰🇷 KR | 2656 |
| 26 | 🇭🇷 HR | 2484 |
| 27 | 🇲🇦 MA | 2238 |
| 28 | 🇲🇪 ME | 1979 |
| 29 | 🇳🇱 NL | 1975 |
| 30 | 🇮🇩 ID | 1909 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4650 |
| 2 | Denver International Airport |  | US | 3618 |
| 3 | Tokyo International Airport |  | JP | 2714 |
| 4 | Indira Gandhi International Airport |  | IN | 2704 |
| 5 | Guaymaral Airport |  | CO | 2615 |
| 6 | Harry Reid International Airport |  | US | 2445 |
| 7 | Zurich Airport |  | CH | 2305 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2276 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2257 |
| 10 | La Aurora Airport |  | GT | 2137 |
| 11 | El Dorado International Airport |  | CO | 2078 |
| 12 | Chicago O'Hare International Airport |  | US | 2027 |
| 13 | Salt Lake City International Airport |  | US | 1949 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1910 |
| 15 | Congonhas Airport |  | BR | 1878 |
| 16 | Frankfurt am Main International Airport |  | DE | 1804 |
| 17 | Madrid Barajas International Airport |  | ES | 1741 |
| 18 | Capua Airport |  | IT | 1700 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1662 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1640 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1625 |
| 22 | Macau International Airport |  | MO | 1588 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1571 |
| 24 | Malpensa International Airport |  | IT | 1559 |
| 25 | Charles de Gaulle International Airport |  | FR | 1533 |
| 26 | Charlotte/Douglas International Airport |  | US | 1473 |
| 27 | Ninoy Aquino International Airport |  | PH | 1436 |
| 28 | Kuala Lumpur International Airport |  | MY | 1418 |
| 29 | Barcelona International Airport |  | ES | 1372 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1348 |
| 31 | Bengaluru International Airport |  | IN | 1332 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1316 |
| 33 | Seattle-Tacoma International Airport |  | US | 1313 |
| 34 | Viracopos International Airport |  | BR | 1307 |
| 35 | Calgary International Airport |  | CA | 1258 |
| 36 | Enrique Olaya Herrera Airport |  | CO | 1252 |
| 37 | Oslo Gardermoen Airport |  | NO | 1240 |
| 38 | Don Mueang International Airport |  | TH | 1238 |
| 39 | Vitoria/Foronda Airport |  | ES | 1234 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1195 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1068 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 801 | 21m | 244 km | 3,372.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 556 | 1h 7m | 770 km | 7,386.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 538 | 24m | 225 km | 2,087.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 505 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 501 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 375 | 27m | 275 km | 1,777.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 352 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 330 | 1h 50m | 1,423 km | 8,098.7 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 325 | 44m | 241 km | 1,350.0 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 296 | 21m | 250 km | 1,278.5 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 280 | 1h 39m | 1,156 km | 5,585.9 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 277 | 24m | 218 km | 1,043.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 275 | 27m | 215 km | 1,018.5 t |
| 19 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 273 | 44m | 555 km | 2,614.1 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 273 | 19m | 99 km | 467.6 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 262 | 1h 14m | 961 km | 4,342.8 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 253 | 19m | 144 km | 629.3 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 252 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 241 | 1h 50m | 1,304 km | 5,421.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 234 | 28m | 152 km | 611.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N971AC |  | Coral Creek Airport (FA54) | Venice Municipal Airport (KVNC) | 2026-08-21 14:55 UTC | 2026-08-21 15:06 UTC | 10m |
| CPA801 | Cathay Pacific | Chicago O'Hare International Airport (KORD) | Zhuhai Airport (ZGSD) | 2026-08-21 00:28 UTC | 2026-08-21 14:55 UTC | 14h 26m |
| N442BG |  | Wood County Regional Airport (K1G0) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-08-21 12:49 UTC | 2026-08-21 14:54 UTC | 2h 4m |
| GUNN41 | GUN | Flysooner Field (OK50) | Trust Landing Airport (OK72) | 2026-08-21 14:32 UTC | 2026-08-21 14:54 UTC | 22m |
| N969YC |  | Newark Liberty International Airport (KEWR) | Laguardia Airport (KLGA) | 2026-08-21 14:09 UTC | 2026-08-21 14:49 UTC | 39m |
| N32YA |  | Fort Lauderdale Executive Airport (KFXE) | Fort Lauderdale Executive Airport (KFXE) | 2026-08-21 14:29 UTC | 2026-08-21 14:46 UTC | 17m |
| CKS285 | CKS | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2026-08-21 04:28 UTC | 2026-08-21 14:40 UTC | 10h 12m |
| CONGO63 | CON | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-08-21 14:23 UTC | 2026-08-21 14:40 UTC | 16m |
| FKH8050 | FKH | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-08-21 09:52 UTC | 2026-08-21 14:39 UTC | 4h 46m |
| N46VB |  | Danbury Municipal Airport (KDXR) | Waterbury-Oxford Airport (KOXC) | 2026-08-21 14:05 UTC | 2026-08-21 14:38 UTC | 32m |
| FHIGE | FHI | Hamburg Airport (EDDH) | Uetersen/Heist Airport (EDHE) | 2026-08-21 14:11 UTC | 2026-08-21 14:37 UTC | 26m |
| N628SR |  | Palo Alto Airport (KPAO) | Truckee-Tahoe Airport (KTRK) | 2026-08-21 14:03 UTC | 2026-08-21 14:37 UTC | 34m |
| N722UE |  | North Las Vegas Airport (KVGT) | Caas Airport (NV98) | 2026-08-21 14:22 UTC | 2026-08-21 14:36 UTC | 13m |
| LYBAY | LYB | Klaipeda Airport (EYKL) | Klaipeda Airport (EYKL) | 2026-08-21 14:33 UTC | 2026-08-21 14:35 UTC | 2m |
| CAP2912 | CAP | South Jersey Regional Airport (KVAY) | Trenton-Robbinsville Airport (KN87) | 2026-08-21 14:12 UTC | 2026-08-21 14:34 UTC | 22m |
| CXK368 | CXK | Arlington Municipal Airport (KGKY) | Arlington Municipal Airport (KGKY) | 2026-08-21 14:30 UTC | 2026-08-21 14:34 UTC | 3m |
| N1424V |  | Central Jersey Regional Airport (K47N) | Central Jersey Regional Airport (K47N) | 2026-08-21 13:41 UTC | 2026-08-21 14:32 UTC | 51m |
| N27NW |  | San Antonio International Airport (KSAT) | Laughlin Afb Aux Nr 1 Airport (KT70) | 2026-08-21 13:52 UTC | 2026-08-21 14:29 UTC | 36m |
| N8675 |  | Rocky Mountain Metro Airport (KBJC) | Mc Elroy Airfield (K20V) | 2026-08-21 14:13 UTC | 2026-08-21 14:24 UTC | 11m |
| N498SP |  | Monroe County Airport (KBMG) | Monroe County Airport (KBMG) | 2026-08-21 13:47 UTC | 2026-08-21 14:24 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
