# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_02:54:53_UTC-green)

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

**Latest saved flight:** 2026-08-20 02:54:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 02:54:53 UTC

- **218,042** saved flights
- **68,682** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **218,042** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,622,915.7 tonnes** estimated CO2 emissions
- **152,053,084 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8714 |
| 2 | SkyWest Airlines | 7813 |
| 3 | EJA | 4247 |
| 4 | IndiGo | 3695 |
| 5 | American Airlines | 3635 |
| 6 | Southwest Airlines | 3466 |
| 7 | Delta Air Lines | 2820 |
| 8 | ENY | 2698 |
| 9 | LATAM Airlines | 2068 |
| 10 | AZU | 2000 |
| 11 | Vueling | 1827 |
| 12 | Lufthansa | 1813 |
| 13 | WIF | 1738 |
| 14 | LXJ | 1728 |
| 15 | easyJet | 1511 |
| 16 | Swiss International | 1448 |
| 17 | AXM | 1419 |
| 18 | United Airlines | 1382 |
| 19 | QLK | 1356 |
| 20 | EJU | 1355 |
| 21 | Alaska Airlines | 1333 |
| 22 | All Nippon Airways | 1308 |
| 23 | VIV | 1194 |
| 24 | GLO | 1187 |
| 25 | Air France | 1178 |
| 26 | PGT | 1178 |
| 27 | WMT | 1142 |
| 28 | JetBlue | 1110 |
| 29 | Wizz Air | 1105 |
| 30 | AEE | 1089 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 184062 |
| 2 | 🇪🇸 ES | 13942 |
| 3 | 🇧🇷 BR | 12591 |
| 4 | 🇦🇺 AU | 12259 |
| 5 | 🇨🇦 CA | 12043 |
| 6 | 🇮🇹 IT | 11562 |
| 7 | 🇮🇳 IN | 11508 |
| 8 | 🇩🇪 DE | 10767 |
| 9 | 🇬🇧 GB | 10214 |
| 10 | 🇨🇴 CO | 8970 |
| 11 | 🇯🇵 JP | 8891 |
| 12 | 🇫🇷 FR | 8667 |
| 13 | 🇬🇷 GR | 6347 |
| 14 | 🇹🇷 TR | 6264 |
| 15 | 🇲🇽 MX | 6087 |
| 16 | 🇨🇭 CH | 5768 |
| 17 | 🇳🇴 NO | 5405 |
| 18 | 🇲🇾 MY | 3751 |
| 19 | 🇿🇦 ZA | 3685 |
| 20 | 🇵🇱 PL | 3597 |
| 21 | 🇹🇭 TH | 3548 |
| 22 | 🇳🇿 NZ | 3026 |
| 23 | 🇵🇭 PH | 2914 |
| 24 | 🇬🇹 GT | 2767 |
| 25 | 🇰🇷 KR | 2617 |
| 26 | 🇭🇷 HR | 2390 |
| 27 | 🇲🇦 MA | 2189 |
| 28 | 🇳🇱 NL | 1940 |
| 29 | 🇲🇪 ME | 1909 |
| 30 | 🇮🇩 ID | 1826 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4591 |
| 2 | Denver International Airport |  | US | 3574 |
| 3 | Tokyo International Airport |  | JP | 2672 |
| 4 | Indira Gandhi International Airport |  | IN | 2635 |
| 5 | Guaymaral Airport |  | CO | 2595 |
| 6 | Harry Reid International Airport |  | US | 2416 |
| 7 | Zurich Airport |  | CH | 2258 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2244 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2213 |
| 10 | La Aurora Airport |  | GT | 2106 |
| 11 | El Dorado International Airport |  | CO | 2048 |
| 12 | Chicago O'Hare International Airport |  | US | 2007 |
| 13 | Salt Lake City International Airport |  | US | 1929 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1900 |
| 15 | Congonhas Airport |  | BR | 1840 |
| 16 | Frankfurt am Main International Airport |  | DE | 1779 |
| 17 | Madrid Barajas International Airport |  | ES | 1703 |
| 18 | Capua Airport |  | IT | 1655 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1643 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1615 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1603 |
| 22 | Macau International Airport |  | MO | 1563 |
| 23 | Malpensa International Airport |  | IT | 1534 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1520 |
| 25 | Charles de Gaulle International Airport |  | FR | 1494 |
| 26 | Charlotte/Douglas International Airport |  | US | 1462 |
| 27 | Ninoy Aquino International Airport |  | PH | 1384 |
| 28 | Kuala Lumpur International Airport |  | MY | 1380 |
| 29 | Barcelona International Airport |  | ES | 1333 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1330 |
| 31 | Bengaluru International Airport |  | IN | 1316 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1305 |
| 33 | Seattle-Tacoma International Airport |  | US | 1298 |
| 34 | Viracopos International Airport |  | BR | 1277 |
| 35 | Calgary International Airport |  | CA | 1234 |
| 36 | Oslo Gardermoen Airport |  | NO | 1205 |
| 37 | Vitoria/Foronda Airport |  | ES | 1204 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1201 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1173 |
| 40 | Reno/Tahoe International Airport |  | US | 1170 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 779 | 21m | 244 km | 3,280.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 538 | 1h 7m | 770 km | 7,146.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 511 | 24m | 225 km | 1,982.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 493 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 485 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 363 | 27m | 275 km | 1,720.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 319 | 1h 49m | 1,423 km | 7,828.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 316 | 44m | 241 km | 1,312.6 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 311 | 1h 7m | 706 km | 3,786.4 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 294 | 22m | 55 km | 279.4 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 285 | 21m | 250 km | 1,231.0 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 270 | 1h 38m | 1,156 km | 5,386.4 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 267 | 27m | 215 km | 988.9 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 258 | 1h 14m | 961 km | 4,276.5 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 258 | 13m | - | - |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 257 | 31m | 369 km | 1,635.9 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 247 | 19m | 144 km | 614.4 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 246 | 12m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 236 | 1h 49m | 1,304 km | 5,309.4 t |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 29 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 233 | 44m | 555 km | 2,231.1 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N523AB |  | Erie Municipal Airport (KEIK) | Rocky Mountain Metro Airport (KBJC) | 2026-08-20 02:39 UTC | 2026-08-20 02:54 UTC | 15m |
| CCA103 | Air China | Tianjin Binhai International Airport (ZBTJ) | Zhuhai Airport (ZGSD) | 2026-08-20 00:16 UTC | 2026-08-20 02:52 UTC | 2h 35m |
| USHER11 | USH | Hunter Army Air Field (KSVN) | Hunter Army Air Field (KSVN) | 2026-08-20 00:56 UTC | 2026-08-20 02:47 UTC | 1h 50m |
| PFA316 | PFA | Broocke Air Patch Airport (FL95) | Vero Beach Regional Airport (KVRB) | 2026-08-20 00:45 UTC | 2026-08-20 02:46 UTC | 2h 1m |
| CUL552 | CUL | WA70 (WA70) | 3WA1 (3WA1) | 2026-08-20 02:28 UTC | 2026-08-20 02:44 UTC | 15m |
| N268Z |  | Byron Airport (KC83) | Tracy Municipal Airport (KTCY) | 2026-08-20 02:18 UTC | 2026-08-20 02:43 UTC | 25m |
| C2701 |  | Point Mugu Nas (Naval Base Ventura Co) Airport (KNTD) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-20 02:02 UTC | 2026-08-20 02:41 UTC | 38m |
| N221LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Van Nuys Airport (KVNY) | 2026-08-20 01:20 UTC | 2026-08-20 02:37 UTC | 1h 17m |
| SCPR447 | SCP | Mc Gregor Airport (73WT) | Dye Seed Ranch Inc Airport (58WA) | 2026-08-20 01:20 UTC | 2026-08-20 02:28 UTC | 1h 8m |
| FFAB123 | FFA | John Nichol's Field (0CL3) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-20 01:48 UTC | 2026-08-20 02:26 UTC | 38m |
| LBQ792 | LBQ | KNY2 (KNY2) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-08-20 02:08 UTC | 2026-08-20 02:26 UTC | 17m |
| A6GBA |  | Al Maktoum International Airport (OMDW) | OM11 (OM11) | 2026-08-20 02:07 UTC | 2026-08-20 02:26 UTC | 19m |
|  |  | K36U (K36U) | K36U (K36U) | 2026-08-20 02:23 UTC | 2026-08-20 02:23 UTC | 0m |
| YOI | YOI | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-08-20 01:37 UTC | 2026-08-20 02:19 UTC | 41m |
| YOQ | YOQ | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-08-20 01:53 UTC | 2026-08-20 02:15 UTC | 21m |
| NKZ | NKZ | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-20 01:56 UTC | 2026-08-20 02:14 UTC | 18m |
| QLK322D | QLK | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-08-20 01:44 UTC | 2026-08-20 02:14 UTC | 29m |
| N22271 |  | Lawrence J Timmerman Airport (KMWC) | Lawrence J Timmerman Airport (KMWC) | 2026-08-20 02:05 UTC | 2026-08-20 02:12 UTC | 6m |
| N352HP |  | Salt Lake City International Airport (KSLC) | UT08 (UT08) | 2026-08-20 01:54 UTC | 2026-08-20 02:07 UTC | 13m |
| 494LG |  | Simonson Field (80CO) | 14CO (14CO) | 2026-08-20 01:53 UTC | 2026-08-20 02:06 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
