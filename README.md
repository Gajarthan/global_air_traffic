# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_04:29:42_UTC-green)

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

**Latest saved flight:** 2026-08-22 04:29:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-22 04:29:42 UTC

- **224,557** saved flights
- **70,018** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **224,557** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,704,486.2 tonnes** estimated CO2 emissions
- **156,781,809 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8987 |
| 2 | SkyWest Airlines | 7996 |
| 3 | EJA | 4352 |
| 4 | IndiGo | 3789 |
| 5 | American Airlines | 3704 |
| 6 | Southwest Airlines | 3523 |
| 7 | Delta Air Lines | 2878 |
| 8 | ENY | 2759 |
| 9 | LATAM Airlines | 2139 |
| 10 | AZU | 2071 |
| 11 | Vueling | 1890 |
| 12 | Lufthansa | 1843 |
| 13 | WIF | 1787 |
| 14 | LXJ | 1776 |
| 15 | easyJet | 1551 |
| 16 | Swiss International | 1491 |
| 17 | AXM | 1476 |
| 18 | United Airlines | 1417 |
| 19 | QLK | 1415 |
| 20 | EJU | 1405 |
| 21 | Alaska Airlines | 1366 |
| 22 | All Nippon Airways | 1345 |
| 23 | GLO | 1244 |
| 24 | PGT | 1231 |
| 25 | VIV | 1231 |
| 26 | Air France | 1215 |
| 27 | WMT | 1194 |
| 28 | Wizz Air | 1154 |
| 29 | JetBlue | 1127 |
| 30 | AEE | 1117 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 188657 |
| 2 | 🇪🇸 ES | 14364 |
| 3 | 🇧🇷 BR | 13046 |
| 4 | 🇦🇺 AU | 12714 |
| 5 | 🇨🇦 CA | 12477 |
| 6 | 🇮🇹 IT | 11977 |
| 7 | 🇮🇳 IN | 11818 |
| 8 | 🇩🇪 DE | 11032 |
| 9 | 🇬🇧 GB | 10515 |
| 10 | 🇨🇴 CO | 9255 |
| 11 | 🇯🇵 JP | 9114 |
| 12 | 🇫🇷 FR | 8934 |
| 13 | 🇹🇷 TR | 6543 |
| 14 | 🇬🇷 GR | 6531 |
| 15 | 🇲🇽 MX | 6256 |
| 16 | 🇨🇭 CH | 5889 |
| 17 | 🇳🇴 NO | 5561 |
| 18 | 🇲🇾 MY | 3920 |
| 19 | 🇿🇦 ZA | 3861 |
| 20 | 🇹🇭 TH | 3796 |
| 21 | 🇵🇱 PL | 3718 |
| 22 | 🇳🇿 NZ | 3126 |
| 23 | 🇵🇭 PH | 3048 |
| 24 | 🇬🇹 GT | 2848 |
| 25 | 🇰🇷 KR | 2666 |
| 26 | 🇭🇷 HR | 2503 |
| 27 | 🇲🇦 MA | 2256 |
| 28 | 🇳🇱 NL | 1992 |
| 29 | 🇲🇪 ME | 1989 |
| 30 | 🇮🇩 ID | 1925 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4705 |
| 2 | Denver International Airport |  | US | 3668 |
| 3 | Tokyo International Airport |  | JP | 2730 |
| 4 | Indira Gandhi International Airport |  | IN | 2720 |
| 5 | Guaymaral Airport |  | CO | 2630 |
| 6 | Harry Reid International Airport |  | US | 2465 |
| 7 | Zurich Airport |  | CH | 2321 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2301 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2268 |
| 10 | La Aurora Airport |  | GT | 2171 |
| 11 | El Dorado International Airport |  | CO | 2080 |
| 12 | Chicago O'Hare International Airport |  | US | 2048 |
| 13 | Salt Lake City International Airport |  | US | 1977 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1926 |
| 15 | Congonhas Airport |  | BR | 1909 |
| 16 | Frankfurt am Main International Airport |  | DE | 1812 |
| 17 | Madrid Barajas International Airport |  | ES | 1754 |
| 18 | Capua Airport |  | IT | 1717 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1677 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1666 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1633 |
| 22 | Macau International Airport |  | MO | 1591 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1583 |
| 24 | Malpensa International Airport |  | IT | 1571 |
| 25 | Charles de Gaulle International Airport |  | FR | 1548 |
| 26 | Charlotte/Douglas International Airport |  | US | 1482 |
| 27 | Ninoy Aquino International Airport |  | PH | 1454 |
| 28 | Kuala Lumpur International Airport |  | MY | 1432 |
| 29 | Barcelona International Airport |  | ES | 1385 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1366 |
| 31 | Bengaluru International Airport |  | IN | 1337 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1333 |
| 33 | Seattle-Tacoma International Airport |  | US | 1328 |
| 34 | Viracopos International Airport |  | BR | 1321 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1303 |
| 36 | Calgary International Airport |  | CA | 1279 |
| 37 | Oslo Gardermoen Airport |  | NO | 1251 |
| 38 | Don Mueang International Airport |  | TH | 1247 |
| 39 | Vitoria/Foronda Airport |  | ES | 1240 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1208 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1072 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 811 | 21m | 244 km | 3,414.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 559 | 1h 7m | 770 km | 7,425.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 546 | 24m | 225 km | 2,118.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 527 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 510 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 377 | 27m | 275 km | 1,786.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 354 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 334 | 1h 50m | 1,423 km | 8,196.9 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 326 | 44m | 241 km | 1,354.1 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 299 | 21m | 250 km | 1,291.5 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 298 | 22m | 55 km | 283.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 286 | 1h 38m | 1,156 km | 5,705.6 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 279 | 24m | 218 km | 1,051.1 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 279 | 19m | 99 km | 477.9 t |
| 19 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 276 | 44m | 555 km | 2,642.8 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 275 | 27m | 215 km | 1,018.5 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 264 | 1h 14m | 961 km | 4,375.9 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 258 | 12m | - | - |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 256 | 19m | 144 km | 636.8 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 244 | 1h 50m | 1,304 km | 5,489.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 238 | 28m | 152 km | 622.0 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N712SL |  | Walker Field (4IA2) | Iowa City Municipal Airport (KIOW) | 2026-08-22 04:14 UTC | 2026-08-22 04:29 UTC | 15m |
| N |  | Tokyo International Airport (RJTT) | Tokyo International Airport (RJTT) | 2026-08-22 04:14 UTC | 2026-08-22 04:24 UTC | 10m |
| N786AC |  | Salt Lake City International Airport (KSLC) | Cascade Airport (KU70) | 2026-08-22 03:23 UTC | 2026-08-22 04:10 UTC | 47m |
| BLIND61 | BLI | City Of Colorado Springs Municipal Airport (KCOS) | Perry Park Airport (CO93) | 2026-08-22 03:42 UTC | 2026-08-22 04:05 UTC | 23m |
| N8846J |  | KFTG (KFTG) | Metrogro Farm Airport (CO25) | 2026-08-22 03:14 UTC | 2026-08-22 04:00 UTC | 45m |
| G72234 |  | Rancho Blanco Airport (TE32) | Laredo International Airport (KLRD) | 2026-08-22 02:44 UTC | 2026-08-22 03:58 UTC | 1h 13m |
| XLF | XLF | Elderslie Airport (YEES) | Elderslie Airport (YEES) | 2026-08-22 03:37 UTC | 2026-08-22 03:52 UTC | 14m |
| VVSA16 | VVS | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-22 02:10 UTC | 2026-08-22 03:49 UTC | 1h 39m |
| CFSUG | CFS | Edmonton International Airport (CYEG) | Slave Lake Airport (CYZH) | 2026-08-22 03:14 UTC | 2026-08-22 03:48 UTC | 34m |
| HTM | HTM | RAAF Base Richmond (YSRI) | RAAF Base Richmond (YSRI) | 2026-08-22 02:47 UTC | 2026-08-22 03:47 UTC | 59m |
| N539AP |  | Tillamook Airport (KTMK) | KU42 (KU42) | 2026-08-22 00:57 UTC | 2026-08-22 03:44 UTC | 2h 46m |
| N741SM |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-22 01:39 UTC | 2026-08-22 03:42 UTC | 2h 3m |
| AIQ3037 | AIQ | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 2026-08-22 02:51 UTC | 2026-08-22 03:34 UTC | 43m |
| CAL191 | CAL | Gimhae International Airport (RKPK) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-22 01:40 UTC | 2026-08-22 03:30 UTC | 1h 50m |
| TOG30 | TOG | 66CL (66CL) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-22 03:06 UTC | 2026-08-22 03:29 UTC | 22m |
| SKQ37 | SKQ | Birmingham-Shuttlesworth International Airport (KBHM) | Byerley Airport (K0M8) | 2026-08-22 02:32 UTC | 2026-08-22 03:27 UTC | 55m |
| N76015 |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-08-22 03:22 UTC | 2026-08-22 03:27 UTC | 4m |
| CARGO39 | CAR | K0J6 (K0J6) | K0J6 (K0J6) | 2026-08-22 03:15 UTC | 2026-08-22 03:25 UTC | 9m |
| ZKHUP | ZKH | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-08-22 03:16 UTC | 2026-08-22 03:20 UTC | 3m |
| QLK378D | QLK | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-08-22 02:53 UTC | 2026-08-22 03:19 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
