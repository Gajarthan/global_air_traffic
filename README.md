# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_17:35:22_UTC-green)

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

**Latest saved flight:** 2026-08-16 17:35:22 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 17:35:22 UTC

- **205,418** saved flights
- **65,557** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **205,418** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,469,263.6 tonnes** estimated CO2 emissions
- **143,145,718 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8095 |
| 2 | SkyWest Airlines | 7376 |
| 3 | EJA | 3975 |
| 4 | IndiGo | 3519 |
| 5 | American Airlines | 3410 |
| 6 | Southwest Airlines | 3310 |
| 7 | Delta Air Lines | 2627 |
| 8 | ENY | 2559 |
| 9 | LATAM Airlines | 1927 |
| 10 | AZU | 1856 |
| 11 | Lufthansa | 1747 |
| 12 | Vueling | 1700 |
| 13 | WIF | 1655 |
| 14 | LXJ | 1616 |
| 15 | easyJet | 1419 |
| 16 | Swiss International | 1372 |
| 17 | AXM | 1339 |
| 18 | United Airlines | 1296 |
| 19 | Alaska Airlines | 1276 |
| 20 | QLK | 1261 |
| 21 | EJU | 1260 |
| 22 | All Nippon Airways | 1245 |
| 23 | VIV | 1127 |
| 24 | GLO | 1106 |
| 25 | Air France | 1100 |
| 26 | PGT | 1096 |
| 27 | JetBlue | 1053 |
| 28 | AEE | 1051 |
| 29 | WMT | 1035 |
| 30 | CXK | 1014 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 174465 |
| 2 | 🇪🇸 ES | 13134 |
| 3 | 🇧🇷 BR | 11749 |
| 4 | 🇦🇺 AU | 11483 |
| 5 | 🇨🇦 CA | 11322 |
| 6 | 🇮🇳 IN | 10981 |
| 7 | 🇮🇹 IT | 10711 |
| 8 | 🇩🇪 DE | 10173 |
| 9 | 🇬🇧 GB | 9586 |
| 10 | 🇯🇵 JP | 8453 |
| 11 | 🇫🇷 FR | 8143 |
| 12 | 🇨🇴 CO | 8127 |
| 13 | 🇬🇷 GR | 6054 |
| 14 | 🇹🇷 TR | 5812 |
| 15 | 🇲🇽 MX | 5761 |
| 16 | 🇨🇭 CH | 5500 |
| 17 | 🇳🇴 NO | 5125 |
| 18 | 🇲🇾 MY | 3528 |
| 19 | 🇿🇦 ZA | 3452 |
| 20 | 🇵🇱 PL | 3390 |
| 21 | 🇹🇭 TH | 3246 |
| 22 | 🇳🇿 NZ | 2843 |
| 23 | 🇵🇭 PH | 2729 |
| 24 | 🇬🇹 GT | 2588 |
| 25 | 🇰🇷 KR | 2504 |
| 26 | 🇭🇷 HR | 2197 |
| 27 | 🇲🇦 MA | 2072 |
| 28 | 🇳🇱 NL | 1836 |
| 29 | 🇲🇪 ME | 1727 |
| 30 | 🇮🇩 ID | 1686 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4309 |
| 2 | Denver International Airport |  | US | 3351 |
| 3 | Tokyo International Airport |  | JP | 2550 |
| 4 | Indira Gandhi International Airport |  | IN | 2490 |
| 5 | Guaymaral Airport |  | CO | 2488 |
| 6 | Harry Reid International Airport |  | US | 2323 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2148 |
| 8 | Zurich Airport |  | CH | 2145 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2129 |
| 10 | La Aurora Airport |  | GT | 1977 |
| 11 | Chicago O'Hare International Airport |  | US | 1905 |
| 12 | El Dorado International Airport |  | CO | 1872 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1831 |
| 14 | Salt Lake City International Airport |  | US | 1815 |
| 15 | Congonhas Airport |  | BR | 1713 |
| 16 | Frankfurt am Main International Airport |  | DE | 1704 |
| 17 | Madrid Barajas International Airport |  | ES | 1611 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1571 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1560 |
| 20 | Capua Airport |  | IT | 1559 |
| 21 | Macau International Airport |  | MO | 1541 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1485 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1436 |
| 24 | Malpensa International Airport |  | IT | 1419 |
| 25 | Charles de Gaulle International Airport |  | FR | 1409 |
| 26 | Charlotte/Douglas International Airport |  | US | 1398 |
| 27 | Kuala Lumpur International Airport |  | MY | 1308 |
| 28 | Ninoy Aquino International Airport |  | PH | 1293 |
| 29 | Bengaluru International Airport |  | IN | 1276 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1261 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1234 |
| 32 | Barcelona International Airport |  | ES | 1225 |
| 33 | Seattle-Tacoma International Airport |  | US | 1218 |
| 34 | Viracopos International Airport |  | BR | 1189 |
| 35 | Calgary International Airport |  | CA | 1160 |
| 36 | Reno/Tahoe International Airport |  | US | 1138 |
| 37 | Oslo Gardermoen Airport |  | NO | 1135 |
| 38 | Vitoria/Foronda Airport |  | ES | 1133 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1106 |
| 40 | Daniel K Inouye International Airport |  | US | 1103 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1024 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 500 | 1h 7m | 770 km | 6,642.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 478 | 24m | 225 km | 1,854.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 467 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 392 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 345 | 27m | 275 km | 1,634.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 303 | 44m | 241 km | 1,258.6 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 297 | 1h 49m | 1,423 km | 7,288.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 268 | 21m | 250 km | 1,157.6 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 256 | 24m | 218 km | 964.5 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 250 | 27m | 215 km | 925.9 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 20 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 247 | 1h 14m | 961 km | 4,094.2 t |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 247 | 19m | 99 km | 423.1 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 241 | 1h 37m | 1,156 km | 4,807.9 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 236 | 19m | 144 km | 587.0 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 233 | 31m | 369 km | 1,483.1 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 221 | 1h 49m | 1,304 km | 4,971.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 218 | 28m | 152 km | 569.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N87RM |  | Perrotti Skyranch Airfield (09ME) | Skydive New England Airport (ME64) | 2026-08-16 16:58 UTC | 2026-08-16 17:35 UTC | 36m |
| N473CA |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-08-16 17:01 UTC | 2026-08-16 17:33 UTC | 31m |
| N92DV |  | Vance Brand Airport (KLMO) | Vance Brand Airport (KLMO) | 2026-08-16 16:42 UTC | 2026-08-16 17:32 UTC | 50m |
| CAN11 | CAN | Pescara International Airport (LIBP) | Pescara International Airport (LIBP) | 2026-08-16 17:15 UTC | 2026-08-16 17:31 UTC | 15m |
| CFR440 | CFR | Columbia Airport (KO22) | Bear Valley Airport (73CA) | 2026-08-16 16:54 UTC | 2026-08-16 17:26 UTC | 31m |
| N371CW |  | Montgomery-Gibbs Executive Airport (KMYF) | WN95 (WN95) | 2026-08-16 14:20 UTC | 2026-08-16 17:26 UTC | 3h 5m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-16 17:02 UTC | 2026-08-16 17:18 UTC | 16m |
| EIN68R | Aer Lingus | Geneva Cointrin International Airport (LSGG) | Dublin Airport (EIDW) | 2026-08-16 15:19 UTC | 2026-08-16 17:12 UTC | 1h 53m |
| N4736Y |  | Cy Nunnally Memorial Airport (KD73) | Cy Nunnally Memorial Airport (KD73) | 2026-08-16 16:53 UTC | 2026-08-16 17:11 UTC | 18m |
| N93EP |  | Martha's Vineyard Airport (KMVY) | Wings Field (KLOM) | 2026-08-16 16:21 UTC | 2026-08-16 17:10 UTC | 48m |
| RFS713 | RFS | Boeing Field/King County International Airport (KBFI) | Renton Municipal Airport (KRNT) | 2026-08-16 16:25 UTC | 2026-08-16 17:06 UTC | 41m |
| CCDBA | CCD | Municipal de Vitacura Airport (SCLC) | Eulogio Sanchez Airport (SCTB) | 2026-08-16 16:54 UTC | 2026-08-16 17:06 UTC | 11m |
| N71560 |  | Abilene Municipal Airport (KK78) | Abilene Municipal Airport (KK78) | 2026-08-16 16:53 UTC | 2026-08-16 17:06 UTC | 12m |
| N66HC |  | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-08-16 16:54 UTC | 2026-08-16 17:05 UTC | 11m |
| TGSZC | TGS | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-08-16 16:52 UTC | 2026-08-16 17:02 UTC | 9m |
| TCN782 | TCN | John Wayne/Orange County Airport (KSNA) | K36U (K36U) | 2026-08-16 15:50 UTC | 2026-08-16 17:01 UTC | 1h 10m |
| N2182H |  | University Airport (KEDU) | San Carlos Airport (KSQL) | 2026-08-16 16:16 UTC | 2026-08-16 17:01 UTC | 44m |
| N2593G |  | Shreveport Downtown Airport (KDTN) | LS90 (LS90) | 2026-08-16 14:25 UTC | 2026-08-16 17:00 UTC | 2h 35m |
| SKW4979 | SkyWest Airlines | Phoenix Sky Harbor International Airport (KPHX) | Sedona Airport (KSEZ) | 2026-08-16 16:37 UTC | 2026-08-16 16:59 UTC | 21m |
| N100LE |  | Logan-Cache Airport (KLGU) | Malad City Airport (KMLD) | 2026-08-16 16:31 UTC | 2026-08-16 16:57 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
