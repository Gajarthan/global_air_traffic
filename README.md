# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_01:39:15_UTC-green)

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

**Latest saved flight:** 2026-08-21 01:39:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 01:39:15 UTC

- **220,940** saved flights
- **69,300** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **220,940** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,658,740.6 tonnes** estimated CO2 emissions
- **154,129,890 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8846 |
| 2 | SkyWest Airlines | 7888 |
| 3 | EJA | 4289 |
| 4 | IndiGo | 3734 |
| 5 | American Airlines | 3666 |
| 6 | Southwest Airlines | 3488 |
| 7 | Delta Air Lines | 2847 |
| 8 | ENY | 2724 |
| 9 | LATAM Airlines | 2102 |
| 10 | AZU | 2030 |
| 11 | Vueling | 1858 |
| 12 | Lufthansa | 1830 |
| 13 | WIF | 1763 |
| 14 | LXJ | 1746 |
| 15 | easyJet | 1530 |
| 16 | Swiss International | 1466 |
| 17 | AXM | 1445 |
| 18 | United Airlines | 1390 |
| 19 | QLK | 1381 |
| 20 | EJU | 1374 |
| 21 | Alaska Airlines | 1347 |
| 22 | All Nippon Airways | 1319 |
| 23 | GLO | 1210 |
| 24 | VIV | 1206 |
| 25 | PGT | 1198 |
| 26 | Air France | 1196 |
| 27 | WMT | 1163 |
| 28 | Wizz Air | 1124 |
| 29 | JetBlue | 1119 |
| 30 | AEE | 1104 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 186103 |
| 2 | 🇪🇸 ES | 14139 |
| 3 | 🇧🇷 BR | 12782 |
| 4 | 🇦🇺 AU | 12483 |
| 5 | 🇨🇦 CA | 12209 |
| 6 | 🇮🇹 IT | 11742 |
| 7 | 🇮🇳 IN | 11643 |
| 8 | 🇩🇪 DE | 10893 |
| 9 | 🇬🇧 GB | 10365 |
| 10 | 🇨🇴 CO | 9093 |
| 11 | 🇯🇵 JP | 8971 |
| 12 | 🇫🇷 FR | 8784 |
| 13 | 🇬🇷 GR | 6437 |
| 14 | 🇹🇷 TR | 6357 |
| 15 | 🇲🇽 MX | 6147 |
| 16 | 🇨🇭 CH | 5829 |
| 17 | 🇳🇴 NO | 5481 |
| 18 | 🇲🇾 MY | 3823 |
| 19 | 🇿🇦 ZA | 3763 |
| 20 | 🇵🇱 PL | 3661 |
| 21 | 🇹🇭 TH | 3657 |
| 22 | 🇳🇿 NZ | 3059 |
| 23 | 🇵🇭 PH | 2973 |
| 24 | 🇬🇹 GT | 2790 |
| 25 | 🇰🇷 KR | 2638 |
| 26 | 🇭🇷 HR | 2447 |
| 27 | 🇲🇦 MA | 2220 |
| 28 | 🇳🇱 NL | 1962 |
| 29 | 🇲🇪 ME | 1950 |
| 30 | 🇮🇩 ID | 1873 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4646 |
| 2 | Denver International Airport |  | US | 3614 |
| 3 | Tokyo International Airport |  | JP | 2692 |
| 4 | Indira Gandhi International Airport |  | IN | 2670 |
| 5 | Guaymaral Airport |  | CO | 2606 |
| 6 | Harry Reid International Airport |  | US | 2436 |
| 7 | Zurich Airport |  | CH | 2288 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2273 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2240 |
| 10 | La Aurora Airport |  | GT | 2126 |
| 11 | El Dorado International Airport |  | CO | 2070 |
| 12 | Chicago O'Hare International Airport |  | US | 2024 |
| 13 | Salt Lake City International Airport |  | US | 1946 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1908 |
| 15 | Congonhas Airport |  | BR | 1869 |
| 16 | Frankfurt am Main International Airport |  | DE | 1797 |
| 17 | Madrid Barajas International Airport |  | ES | 1731 |
| 18 | Capua Airport |  | IT | 1685 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1660 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1629 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1625 |
| 22 | Macau International Airport |  | MO | 1583 |
| 23 | Malpensa International Airport |  | IT | 1548 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1547 |
| 25 | Charles de Gaulle International Airport |  | FR | 1518 |
| 26 | Charlotte/Douglas International Airport |  | US | 1470 |
| 27 | Ninoy Aquino International Airport |  | PH | 1414 |
| 28 | Kuala Lumpur International Airport |  | MY | 1403 |
| 29 | Barcelona International Airport |  | ES | 1354 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1342 |
| 31 | Bengaluru International Airport |  | IN | 1325 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1314 |
| 33 | Seattle-Tacoma International Airport |  | US | 1309 |
| 34 | Viracopos International Airport |  | BR | 1298 |
| 35 | Calgary International Airport |  | CA | 1252 |
| 36 | Enrique Olaya Herrera Airport |  | CO | 1235 |
| 37 | Vitoria/Foronda Airport |  | ES | 1225 |
| 38 | Oslo Gardermoen Airport |  | NO | 1224 |
| 39 | Don Mueang International Airport |  | TH | 1203 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1186 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1064 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 793 | 21m | 244 km | 3,339.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 546 | 1h 7m | 770 km | 7,253.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 526 | 24m | 225 km | 2,040.6 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 499 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 499 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 371 | 27m | 275 km | 1,758.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 325 | 1h 50m | 1,423 km | 7,976.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 324 | 44m | 241 km | 1,345.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 292 | 21m | 250 km | 1,261.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 275 | 1h 38m | 1,156 km | 5,486.1 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 274 | 24m | 218 km | 1,032.3 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 272 | 27m | 215 km | 1,007.4 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 261 | 1h 14m | 961 km | 4,326.2 t |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 251 | 44m | 555 km | 2,403.4 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 251 | 19m | 144 km | 624.3 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 251 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 239 | 1h 49m | 1,304 km | 5,376.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| 14548 |  | Elmendorf Afb Airport (PAED) | Little Susitna Airport (8AK6) | 2026-08-21 00:57 UTC | 2026-08-21 01:39 UTC | 41m |
| N449DS |  | Cleveland Municipal Airport (KRNV) | Cleveland Municipal Airport (KRNV) | 2026-08-21 00:52 UTC | 2026-08-21 01:37 UTC | 44m |
| XSN40 | XSN | San Carlos Airport (KSQL) | Truckee-Tahoe Airport (KTRK) | 2026-08-21 00:56 UTC | 2026-08-21 01:31 UTC | 35m |
| DXR | DXR | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-21 01:09 UTC | 2026-08-21 01:24 UTC | 14m |
| N648HE |  | Carson City Airport (KCXP) | Carson City Airport (KCXP) | 2026-08-21 01:19 UTC | 2026-08-21 01:21 UTC | 2m |
| LS04 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-21 00:33 UTC | 2026-08-21 01:17 UTC | 43m |
| G24413 |  | Waterloo Regional Airport (KALO) | IA17 (IA17) | 2026-08-21 01:04 UTC | 2026-08-21 01:15 UTC | 11m |
| JUMP16 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-08-21 00:53 UTC | 2026-08-21 01:12 UTC | 18m |
| PGT899 | PGT | Queen Alia International Airport (OJAI) | Trabzon International Airport (LTCG) | 2026-08-20 23:45 UTC | 2026-08-21 01:11 UTC | 1h 25m |
| N2824L |  | Lincoln Airport (KLNK) | Lincoln Airport (KLNK) | 2026-08-21 00:35 UTC | 2026-08-21 01:05 UTC | 30m |
| QLK1596 | QLK | Melbourne International Airport (YMML) | Lakeside Airpark (YLAK) | 2026-08-20 22:40 UTC | 2026-08-21 01:01 UTC | 2h 21m |
| QLK863D | QLK | Brisbane International Airport (YBBN) | Cooma/Polo Flat (Unlic) Airport (YPFT) | 2026-08-20 23:09 UTC | 2026-08-21 00:58 UTC | 1h 49m |
| N515QS |  | Juneau International Airport (PAJN) | Mack Mesa Airport (10CO) | 2026-08-20 19:48 UTC | 2026-08-21 00:54 UTC | 5h 6m |
| CLY681 | CLY | Washington Dulles International Airport (KIAD) | Laurence G Hanscom Field (KBED) | 2026-08-20 23:53 UTC | 2026-08-21 00:54 UTC | 1h 0m |
| N86HD |  | Fulton County Executive/Charlie Brown Field (KFTY) | K36U (K36U) | 2026-08-20 21:36 UTC | 2026-08-21 00:50 UTC | 3h 14m |
| N327AX |  | Kaneohe Bay Mcas (Marion E Carl Field) Airport (PHNG) | Kaneohe Bay Mcas (Marion E Carl Field) Airport (PHNG) | 2026-08-20 23:09 UTC | 2026-08-21 00:46 UTC | 1h 37m |
| N7009Q |  | St George Regional Airport (KSGU) | Cedar City Regional Airport (KCDC) | 2026-08-21 00:18 UTC | 2026-08-21 00:46 UTC | 28m |
| VAR493 | VAR | John Wayne/Orange County Airport (KSNA) | Coolidge Municipal Airport (KP08) | 2026-08-20 22:24 UTC | 2026-08-21 00:46 UTC | 2h 21m |
| JAL373C | Japan Airlines | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-08-20 23:43 UTC | 2026-08-21 00:45 UTC | 1h 2m |
| GLO1419 | GLO | Fazenda Cachoeirinha Airport (SJVL) | Fazenda Caicara Airport (SDCR) | 2026-08-21 00:01 UTC | 2026-08-21 00:45 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
