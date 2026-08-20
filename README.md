# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_21:26:56_UTC-green)

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

**Latest saved flight:** 2026-08-20 21:26:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 21:26:56 UTC

- **220,449** saved flights
- **69,174** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **220,449** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,654,414.6 tonnes** estimated CO2 emissions
- **153,879,107 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8836 |
| 2 | SkyWest Airlines | 7856 |
| 3 | EJA | 4279 |
| 4 | IndiGo | 3732 |
| 5 | American Airlines | 3656 |
| 6 | Southwest Airlines | 3484 |
| 7 | Delta Air Lines | 2841 |
| 8 | ENY | 2718 |
| 9 | LATAM Airlines | 2094 |
| 10 | AZU | 2018 |
| 11 | Vueling | 1857 |
| 12 | Lufthansa | 1830 |
| 13 | WIF | 1763 |
| 14 | LXJ | 1743 |
| 15 | easyJet | 1528 |
| 16 | Swiss International | 1466 |
| 17 | AXM | 1445 |
| 18 | United Airlines | 1388 |
| 19 | QLK | 1375 |
| 20 | EJU | 1374 |
| 21 | Alaska Airlines | 1343 |
| 22 | All Nippon Airways | 1319 |
| 23 | GLO | 1204 |
| 24 | VIV | 1202 |
| 25 | Air France | 1196 |
| 26 | PGT | 1195 |
| 27 | WMT | 1163 |
| 28 | Wizz Air | 1124 |
| 29 | JetBlue | 1116 |
| 30 | AEE | 1104 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 185567 |
| 2 | 🇪🇸 ES | 14132 |
| 3 | 🇧🇷 BR | 12727 |
| 4 | 🇦🇺 AU | 12419 |
| 5 | 🇨🇦 CA | 12172 |
| 6 | 🇮🇹 IT | 11735 |
| 7 | 🇮🇳 IN | 11635 |
| 8 | 🇩🇪 DE | 10889 |
| 9 | 🇬🇧 GB | 10360 |
| 10 | 🇨🇴 CO | 9053 |
| 11 | 🇯🇵 JP | 8963 |
| 12 | 🇫🇷 FR | 8781 |
| 13 | 🇬🇷 GR | 6434 |
| 14 | 🇹🇷 TR | 6347 |
| 15 | 🇲🇽 MX | 6122 |
| 16 | 🇨🇭 CH | 5829 |
| 17 | 🇳🇴 NO | 5481 |
| 18 | 🇲🇾 MY | 3820 |
| 19 | 🇿🇦 ZA | 3763 |
| 20 | 🇵🇱 PL | 3658 |
| 21 | 🇹🇭 TH | 3655 |
| 22 | 🇳🇿 NZ | 3041 |
| 23 | 🇵🇭 PH | 2961 |
| 24 | 🇬🇹 GT | 2786 |
| 25 | 🇰🇷 KR | 2635 |
| 26 | 🇭🇷 HR | 2446 |
| 27 | 🇲🇦 MA | 2218 |
| 28 | 🇳🇱 NL | 1960 |
| 29 | 🇲🇪 ME | 1949 |
| 30 | 🇮🇩 ID | 1866 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4625 |
| 2 | Denver International Airport |  | US | 3599 |
| 3 | Tokyo International Airport |  | JP | 2689 |
| 4 | Indira Gandhi International Airport |  | IN | 2668 |
| 5 | Guaymaral Airport |  | CO | 2604 |
| 6 | Harry Reid International Airport |  | US | 2423 |
| 7 | Zurich Airport |  | CH | 2288 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2267 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2239 |
| 10 | La Aurora Airport |  | GT | 2123 |
| 11 | El Dorado International Airport |  | CO | 2061 |
| 12 | Chicago O'Hare International Airport |  | US | 2021 |
| 13 | Salt Lake City International Airport |  | US | 1943 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1906 |
| 15 | Congonhas Airport |  | BR | 1865 |
| 16 | Frankfurt am Main International Airport |  | DE | 1797 |
| 17 | Madrid Barajas International Airport |  | ES | 1731 |
| 18 | Capua Airport |  | IT | 1685 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1655 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1624 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1620 |
| 22 | Macau International Airport |  | MO | 1583 |
| 23 | Malpensa International Airport |  | IT | 1548 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1542 |
| 25 | Charles de Gaulle International Airport |  | FR | 1518 |
| 26 | Charlotte/Douglas International Airport |  | US | 1467 |
| 27 | Ninoy Aquino International Airport |  | PH | 1408 |
| 28 | Kuala Lumpur International Airport |  | MY | 1403 |
| 29 | Barcelona International Airport |  | ES | 1352 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1337 |
| 31 | Bengaluru International Airport |  | IN | 1325 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1310 |
| 33 | Seattle-Tacoma International Airport |  | US | 1302 |
| 34 | Viracopos International Airport |  | BR | 1290 |
| 35 | Calgary International Airport |  | CA | 1245 |
| 36 | Enrique Olaya Herrera Airport |  | CO | 1227 |
| 37 | Vitoria/Foronda Airport |  | ES | 1225 |
| 38 | Oslo Gardermoen Airport |  | NO | 1224 |
| 39 | Don Mueang International Airport |  | TH | 1202 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1184 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1063 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 790 | 21m | 244 km | 3,326.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 543 | 1h 7m | 770 km | 7,213.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 521 | 24m | 225 km | 2,021.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 498 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 496 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 371 | 27m | 275 km | 1,758.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 325 | 1h 50m | 1,423 km | 7,976.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 324 | 44m | 241 km | 1,345.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 292 | 21m | 250 km | 1,261.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 274 | 1h 38m | 1,156 km | 5,466.2 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 273 | 24m | 218 km | 1,028.5 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 272 | 27m | 215 km | 1,007.4 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 260 | 1h 14m | 961 km | 4,309.6 t |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 251 | 44m | 555 km | 2,403.4 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 251 | 19m | 144 km | 624.3 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 247 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 237 | 1h 49m | 1,304 km | 5,331.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| 00000000 |  | Charlotte/Douglas International Airport (KCLT) | Mobile International Airport (KBFM) | 2026-08-20 20:03 UTC | 2026-08-20 21:26 UTC | 1h 22m |
| N1954T |  | Savannah/Hilton Head International Airport (KSAV) | K88J (K88J) | 2026-08-20 20:59 UTC | 2026-08-20 21:26 UTC | 26m |
| CPA640 | Cathay Pacific | Tribhuvan International Airport (VNKT) | Macau International Airport (VMMC) | 2026-08-20 17:32 UTC | 2026-08-20 21:22 UTC | 3h 49m |
| N407DK |  | Eulogio Sanchez Airport (SCTB) | Cristo Redentor Airport (SAMC) | 2026-08-20 21:10 UTC | 2026-08-20 21:17 UTC | 6m |
| N986SA |  | Hayward Executive Airport (KHWD) | Portland-Hillsboro Airport (KHIO) | 2026-08-20 19:58 UTC | 2026-08-20 21:12 UTC | 1h 14m |
| N98GX |  | 1MT2 (1MT2) | Flying Cloud Airport (KFCM) | 2026-08-20 19:03 UTC | 2026-08-20 21:12 UTC | 2h 9m |
| THY8TW | Turkish Airlines | Milas Bodrum International Airport (LTFE) | Smolensk North Airport (XUBS) | 2026-08-20 18:38 UTC | 2026-08-20 21:11 UTC | 2h 32m |
| DADDY11 | DAD | RAF Mildenhall (EGUN) | RAF Mildenhall (EGUN) | 2026-08-20 19:48 UTC | 2026-08-20 21:08 UTC | 1h 19m |
| FOX1 | FOX | Phoenix Deer Valley Airport (KDVT) | Thunder Ridge Airpark (AZ28) | 2026-08-20 20:22 UTC | 2026-08-20 21:04 UTC | 42m |
| LXJ428 | LXJ | Monterey Regional Airport (KMRY) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-20 20:39 UTC | 2026-08-20 21:02 UTC | 23m |
| TKR168 | TKR | Tok 2 Airport (8AK9) | Fairbanks International Airport (PAFA) | 2026-08-20 20:15 UTC | 2026-08-20 21:00 UTC | 45m |
| N18ZD |  | Greeley-Weld County Airport (KGXY) | Burley Municipal Airport (KBYI) | 2026-08-20 19:46 UTC | 2026-08-20 21:00 UTC | 1h 13m |
| BULETXX | BUL | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-20 20:02 UTC | 2026-08-20 20:58 UTC | 55m |
| N737GS |  | Casper/Natrona County International Airport (KCPR) | Casper/Natrona County International Airport (KCPR) | 2026-08-20 20:47 UTC | 2026-08-20 20:58 UTC | 10m |
| QTR8394 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-08-20 13:18 UTC | 2026-08-20 20:56 UTC | 7h 38m |
| LYM3710 | LYM | Telluride Regional Airport (KTEX) | Telluride Regional Airport (KTEX) | 2026-08-20 17:48 UTC | 2026-08-20 20:55 UTC | 3h 6m |
| N412MH |  | Portland International Airport (KPDX) | Oxbow Airport (OR12) | 2026-08-20 20:15 UTC | 2026-08-20 20:55 UTC | 39m |
| N5679U |  | Flying Frog Field (91GA) | Ashland/Lineville Airport (K26A) | 2026-08-20 20:21 UTC | 2026-08-20 20:49 UTC | 28m |
| N883MT |  | University Of Oklahoma Westheimer Airport (KOUN) | 0AR1 (0AR1) | 2026-08-20 20:07 UTC | 2026-08-20 20:48 UTC | 41m |
| NIT265 | NIT | Atlanta Regional Falcon Field (KFFC) | W H 'Bud' Barron Airport (KDBN) | 2026-08-20 19:43 UTC | 2026-08-20 20:47 UTC | 1h 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
