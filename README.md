# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_14:52:22_UTC-green)

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

**Latest saved flight:** 2026-08-19 14:52:22 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 14:52:22 UTC

- **215,963** saved flights
- **68,252** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **215,963** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,599,132.8 tonnes** estimated CO2 emissions
- **150,674,362 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8637 |
| 2 | SkyWest Airlines | 7709 |
| 3 | EJA | 4189 |
| 4 | IndiGo | 3684 |
| 5 | American Airlines | 3594 |
| 6 | Southwest Airlines | 3435 |
| 7 | Delta Air Lines | 2788 |
| 8 | ENY | 2663 |
| 9 | LATAM Airlines | 2043 |
| 10 | AZU | 1970 |
| 11 | Vueling | 1818 |
| 12 | Lufthansa | 1809 |
| 13 | WIF | 1728 |
| 14 | LXJ | 1699 |
| 15 | easyJet | 1501 |
| 16 | Swiss International | 1441 |
| 17 | AXM | 1417 |
| 18 | United Airlines | 1366 |
| 19 | QLK | 1346 |
| 20 | EJU | 1345 |
| 21 | Alaska Airlines | 1324 |
| 22 | All Nippon Airways | 1304 |
| 23 | VIV | 1185 |
| 24 | PGT | 1173 |
| 25 | Air France | 1171 |
| 26 | GLO | 1167 |
| 27 | WMT | 1126 |
| 28 | JetBlue | 1100 |
| 29 | Wizz Air | 1098 |
| 30 | AEE | 1086 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 181861 |
| 2 | 🇪🇸 ES | 13871 |
| 3 | 🇧🇷 BR | 12419 |
| 4 | 🇦🇺 AU | 12161 |
| 5 | 🇨🇦 CA | 11881 |
| 6 | 🇮🇳 IN | 11470 |
| 7 | 🇮🇹 IT | 11448 |
| 8 | 🇩🇪 DE | 10721 |
| 9 | 🇬🇧 GB | 10137 |
| 10 | 🇯🇵 JP | 8868 |
| 11 | 🇨🇴 CO | 8807 |
| 12 | 🇫🇷 FR | 8635 |
| 13 | 🇬🇷 GR | 6330 |
| 14 | 🇹🇷 TR | 6206 |
| 15 | 🇲🇽 MX | 6035 |
| 16 | 🇨🇭 CH | 5748 |
| 17 | 🇳🇴 NO | 5366 |
| 18 | 🇲🇾 MY | 3744 |
| 19 | 🇿🇦 ZA | 3669 |
| 20 | 🇵🇱 PL | 3573 |
| 21 | 🇹🇭 TH | 3535 |
| 22 | 🇳🇿 NZ | 2998 |
| 23 | 🇵🇭 PH | 2898 |
| 24 | 🇬🇹 GT | 2741 |
| 25 | 🇰🇷 KR | 2608 |
| 26 | 🇭🇷 HR | 2365 |
| 27 | 🇲🇦 MA | 2175 |
| 28 | 🇳🇱 NL | 1930 |
| 29 | 🇲🇪 ME | 1880 |
| 30 | 🇮🇩 ID | 1818 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4520 |
| 2 | Denver International Airport |  | US | 3511 |
| 3 | Tokyo International Airport |  | JP | 2662 |
| 4 | Indira Gandhi International Airport |  | IN | 2620 |
| 5 | Guaymaral Airport |  | CO | 2575 |
| 6 | Harry Reid International Airport |  | US | 2400 |
| 7 | Zurich Airport |  | CH | 2247 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2213 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2208 |
| 10 | La Aurora Airport |  | GT | 2083 |
| 11 | El Dorado International Airport |  | CO | 2012 |
| 12 | Chicago O'Hare International Airport |  | US | 1985 |
| 13 | Salt Lake City International Airport |  | US | 1901 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1889 |
| 15 | Congonhas Airport |  | BR | 1807 |
| 16 | Frankfurt am Main International Airport |  | DE | 1768 |
| 17 | Madrid Barajas International Airport |  | ES | 1690 |
| 18 | Capua Airport |  | IT | 1642 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1627 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1609 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1585 |
| 22 | Macau International Airport |  | MO | 1562 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1516 |
| 24 | Malpensa International Airport |  | IT | 1515 |
| 25 | Charles de Gaulle International Airport |  | FR | 1485 |
| 26 | Charlotte/Douglas International Airport |  | US | 1448 |
| 27 | Kuala Lumpur International Airport |  | MY | 1378 |
| 28 | Ninoy Aquino International Airport |  | PH | 1376 |
| 29 | Barcelona International Airport |  | ES | 1325 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1320 |
| 31 | Bengaluru International Airport |  | IN | 1314 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1290 |
| 33 | Seattle-Tacoma International Airport |  | US | 1281 |
| 34 | Viracopos International Airport |  | BR | 1260 |
| 35 | Calgary International Airport |  | CA | 1217 |
| 36 | Oslo Gardermoen Airport |  | NO | 1197 |
| 37 | Vitoria/Foronda Airport |  | ES | 1193 |
| 38 | Don Mueang International Airport |  | TH | 1166 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1166 |
| 40 | Reno/Tahoe International Airport |  | US | 1164 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1053 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 770 | 21m | 244 km | 3,242.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 534 | 1h 7m | 770 km | 7,093.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 507 | 24m | 225 km | 1,966.9 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 484 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 465 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 359 | 27m | 275 km | 1,701.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 349 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 316 | 1h 49m | 1,423 km | 7,755.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 315 | 44m | 241 km | 1,308.4 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 283 | 21m | 250 km | 1,222.4 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 270 | 19m | 99 km | 462.5 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 269 | 1h 38m | 1,156 km | 5,366.4 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 264 | 27m | 215 km | 977.7 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 255 | 1h 14m | 961 km | 4,226.8 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 254 | 13m | - | - |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 253 | 31m | 369 km | 1,610.4 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 246 | 19m | 144 km | 611.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 243 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 28 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 232 | 44m | 555 km | 2,221.5 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 232 | 1h 49m | 1,304 km | 5,219.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CONGO64 | CON | City Of Colorado Springs Municipal Airport (KCOS) | Usaf Academy Davis Airfield (KAFF) | 2026-08-19 14:40 UTC | 2026-08-19 14:52 UTC | 12m |
| CXK1150 | CXK | Arlington Municipal Airport (KGKY) | 2TS6 (2TS6) | 2026-08-19 14:01 UTC | 2026-08-19 14:51 UTC | 50m |
| N1115M |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-08-19 14:24 UTC | 2026-08-19 14:48 UTC | 24m |
| N460AA |  | K4R4 (K4R4) | Bay Minette Municipal Airport (K1R8) | 2026-08-19 14:24 UTC | 2026-08-19 14:44 UTC | 19m |
| FIRE02 | FIR | Ovar Airport (LPOV) | Viseu Airport (LPVZ) | 2026-08-19 13:58 UTC | 2026-08-19 14:44 UTC | 46m |
| ECNZM | ECN | Viseu Airport (LPVZ) | Viseu Airport (LPVZ) | 2026-08-19 12:41 UTC | 2026-08-19 14:42 UTC | 2h 1m |
| N74SW |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-08-19 14:28 UTC | 2026-08-19 14:40 UTC | 12m |
| N4746N |  | Chehalis-Centralia Airport (KCLS) | Portland-Hillsboro Airport (KHIO) | 2026-08-19 13:41 UTC | 2026-08-19 14:40 UTC | 59m |
| IHACF | IHA | LIVD (LIVD) | Zell Am See Airport (LOWZ) | 2026-08-19 14:22 UTC | 2026-08-19 14:38 UTC | 16m |
| FHPCJ | FHP | Rochefort-Saint-Agnant (BA 721) Airport (LFDN) | Rochefort-Saint-Agnant (BA 721) Airport (LFDN) | 2026-08-19 14:24 UTC | 2026-08-19 14:37 UTC | 13m |
| G08864 |  | St Paul Downtown Holman Field (KSTP) | Mankato Regional Airport (KMKT) | 2026-08-19 13:57 UTC | 2026-08-19 14:36 UTC | 38m |
| N862TC |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-08-19 13:54 UTC | 2026-08-19 14:36 UTC | 42m |
| GRIM01 | GRI | Tlc Airport (OK71) | Christman Airfield (KO65) | 2026-08-19 14:28 UTC | 2026-08-19 14:34 UTC | 6m |
| N626LM |  | Sussex Airport (KFWN) | Sussex Airport (KFWN) | 2026-08-19 14:16 UTC | 2026-08-19 14:32 UTC | 15m |
| N746TW |  | KU42 (KU42) | KU42 (KU42) | 2026-08-19 14:05 UTC | 2026-08-19 14:31 UTC | 25m |
| PA |  | Ptuj Airport (LJPT) | Ptuj Airport (LJPT) | 2026-08-19 14:12 UTC | 2026-08-19 14:29 UTC | 17m |
| A14 |  | Viseu Airport (LPVZ) | Viseu Airport (LPVZ) | 2026-08-19 12:41 UTC | 2026-08-19 14:29 UTC | 1h 48m |
| DEVIL62 | DEV | Frontier Airport (55XS) | Dunbar Ranch Airport (0XS8) | 2026-08-19 14:02 UTC | 2026-08-19 14:25 UTC | 22m |
| N93KK |  | Lakewood Airport (KN12) | Dix Field (0NJ6) | 2026-08-19 13:19 UTC | 2026-08-19 14:23 UTC | 1h 4m |
| LSI113 | LSI | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-08-19 03:19 UTC | 2026-08-19 14:23 UTC | 11h 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
