# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_18:59:03_UTC-green)

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

**Latest saved flight:** 2026-08-16 18:59:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 18:59:03 UTC

- **205,750** saved flights
- **65,639** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **205,750** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,473,316.6 tonnes** estimated CO2 emissions
- **143,380,676 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8114 |
| 2 | SkyWest Airlines | 7389 |
| 3 | EJA | 3986 |
| 4 | IndiGo | 3521 |
| 5 | American Airlines | 3420 |
| 6 | Southwest Airlines | 3313 |
| 7 | Delta Air Lines | 2637 |
| 8 | ENY | 2568 |
| 9 | LATAM Airlines | 1931 |
| 10 | AZU | 1861 |
| 11 | Lufthansa | 1749 |
| 12 | Vueling | 1705 |
| 13 | WIF | 1655 |
| 14 | LXJ | 1624 |
| 15 | easyJet | 1422 |
| 16 | Swiss International | 1372 |
| 17 | AXM | 1339 |
| 18 | United Airlines | 1297 |
| 19 | Alaska Airlines | 1276 |
| 20 | QLK | 1261 |
| 21 | EJU | 1260 |
| 22 | All Nippon Airways | 1245 |
| 23 | VIV | 1129 |
| 24 | GLO | 1106 |
| 25 | Air France | 1101 |
| 26 | PGT | 1099 |
| 27 | JetBlue | 1055 |
| 28 | AEE | 1051 |
| 29 | WMT | 1037 |
| 30 | CXK | 1015 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 174801 |
| 2 | 🇪🇸 ES | 13158 |
| 3 | 🇧🇷 BR | 11773 |
| 4 | 🇦🇺 AU | 11483 |
| 5 | 🇨🇦 CA | 11348 |
| 6 | 🇮🇳 IN | 10985 |
| 7 | 🇮🇹 IT | 10733 |
| 8 | 🇩🇪 DE | 10189 |
| 9 | 🇬🇧 GB | 9597 |
| 10 | 🇯🇵 JP | 8453 |
| 11 | 🇫🇷 FR | 8157 |
| 12 | 🇨🇴 CO | 8143 |
| 13 | 🇬🇷 GR | 6059 |
| 14 | 🇹🇷 TR | 5830 |
| 15 | 🇲🇽 MX | 5777 |
| 16 | 🇨🇭 CH | 5505 |
| 17 | 🇳🇴 NO | 5126 |
| 18 | 🇲🇾 MY | 3528 |
| 19 | 🇿🇦 ZA | 3454 |
| 20 | 🇵🇱 PL | 3394 |
| 21 | 🇹🇭 TH | 3246 |
| 22 | 🇳🇿 NZ | 2843 |
| 23 | 🇵🇭 PH | 2729 |
| 24 | 🇬🇹 GT | 2604 |
| 25 | 🇰🇷 KR | 2505 |
| 26 | 🇭🇷 HR | 2201 |
| 27 | 🇲🇦 MA | 2077 |
| 28 | 🇳🇱 NL | 1836 |
| 29 | 🇲🇪 ME | 1730 |
| 30 | 🇮🇩 ID | 1686 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4321 |
| 2 | Denver International Airport |  | US | 3359 |
| 3 | Tokyo International Airport |  | JP | 2550 |
| 4 | Indira Gandhi International Airport |  | IN | 2492 |
| 5 | Guaymaral Airport |  | CO | 2490 |
| 6 | Harry Reid International Airport |  | US | 2325 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2148 |
| 8 | Zurich Airport |  | CH | 2148 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2135 |
| 10 | La Aurora Airport |  | GT | 1988 |
| 11 | Chicago O'Hare International Airport |  | US | 1908 |
| 12 | El Dorado International Airport |  | CO | 1874 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1836 |
| 14 | Salt Lake City International Airport |  | US | 1819 |
| 15 | Congonhas Airport |  | BR | 1714 |
| 16 | Frankfurt am Main International Airport |  | DE | 1706 |
| 17 | Madrid Barajas International Airport |  | ES | 1615 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1572 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1565 |
| 20 | Capua Airport |  | IT | 1560 |
| 21 | Macau International Airport |  | MO | 1542 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1488 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1436 |
| 24 | Malpensa International Airport |  | IT | 1419 |
| 25 | Charles de Gaulle International Airport |  | FR | 1412 |
| 26 | Charlotte/Douglas International Airport |  | US | 1403 |
| 27 | Kuala Lumpur International Airport |  | MY | 1308 |
| 28 | Ninoy Aquino International Airport |  | PH | 1293 |
| 29 | Bengaluru International Airport |  | IN | 1276 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1266 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1238 |
| 32 | Barcelona International Airport |  | ES | 1225 |
| 33 | Seattle-Tacoma International Airport |  | US | 1220 |
| 34 | Viracopos International Airport |  | BR | 1192 |
| 35 | Calgary International Airport |  | CA | 1163 |
| 36 | Reno/Tahoe International Airport |  | US | 1139 |
| 37 | Oslo Gardermoen Airport |  | NO | 1136 |
| 38 | Vitoria/Foronda Airport |  | ES | 1135 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1106 |
| 40 | Daniel K Inouye International Airport |  | US | 1103 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1025 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 500 | 1h 7m | 770 km | 6,642.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 478 | 24m | 225 km | 1,854.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 469 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 394 | 8m | - | - |
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
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 248 | 19m | 99 km | 424.8 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 247 | 1h 14m | 961 km | 4,094.2 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 242 | 1h 37m | 1,156 km | 4,827.8 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 236 | 19m | 144 km | 587.0 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 233 | 31m | 369 km | 1,483.1 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 221 | 1h 49m | 1,304 km | 4,971.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 220 | 28m | 152 km | 574.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N44SN |  | Central Florida Airpark (2FA6) | Leeward Air Ranch Airport (FD04) | 2026-08-16 18:43 UTC | 2026-08-16 18:59 UTC | 15m |
| CGNSS | CGN | Tumbler Ridge Airport (CBX7) | Tumbler Ridge Airport (CBX7) | 2026-08-16 18:45 UTC | 2026-08-16 18:57 UTC | 12m |
| N748RM |  | Graham Municipal Airport (KRPH) | Dallas Love Field (KDAL) | 2026-08-16 18:29 UTC | 2026-08-16 18:54 UTC | 25m |
| N737HJ |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-08-16 18:05 UTC | 2026-08-16 18:54 UTC | 48m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-08-16 18:37 UTC | 2026-08-16 18:52 UTC | 14m |
| N4958A |  | Montgomery-Gibbs Executive Airport (KMYF) | Santa Monica Municipal Airport (KSMO) | 2026-08-16 17:33 UTC | 2026-08-16 18:45 UTC | 1h 12m |
| N5914V |  | Linden Airport (KLDJ) | Old Bridge Airport (K3N6) | 2026-08-16 17:03 UTC | 2026-08-16 18:44 UTC | 1h 41m |
| N339CU |  | Minden-Tahoe Airport (KMEV) | Desert Creek Airport (NV97) | 2026-08-16 17:48 UTC | 2026-08-16 18:41 UTC | 53m |
| STGRY67 | STG | Brown Field Municipal Airport (KSDM) | Aztec Municipal Airport (KN19) | 2026-08-16 16:44 UTC | 2026-08-16 18:40 UTC | 1h 55m |
| N2012N |  | Orcas Island Airport (KORS) | Orcas Island Airport (KORS) | 2026-08-16 18:06 UTC | 2026-08-16 18:40 UTC | 33m |
| N8478R |  | Mt Bakewell Airfield (96TN) | K3M3 (K3M3) | 2026-08-16 18:18 UTC | 2026-08-16 18:38 UTC | 19m |
| N768AM |  | Gerald R Ford International Airport (KGRR) | Weller Airport (MI78) | 2026-08-16 18:34 UTC | 2026-08-16 18:38 UTC | 4m |
| N3049Q |  | Las Cruces International Airport (KLRU) | Las Cruces International Airport (KLRU) | 2026-08-16 18:20 UTC | 2026-08-16 18:36 UTC | 15m |
| N3563Q |  | Schaumburg Regional Airport (K06C) | Schaumburg Regional Airport (K06C) | 2026-08-16 18:05 UTC | 2026-08-16 18:35 UTC | 29m |
| CGNSS | CGN | Prince George Airport (CYXS) | Tumbler Ridge Airport (CBX7) | 2026-08-16 16:23 UTC | 2026-08-16 18:34 UTC | 2h 11m |
| N51XM |  | San Gabriel Valley Airport (KEMT) | Santa Monica Municipal Airport (KSMO) | 2026-08-16 18:14 UTC | 2026-08-16 18:33 UTC | 19m |
| N26WR |  | Santa Ynez/Kunkle Field (KIZA) | Van Nuys Airport (KVNY) | 2026-08-16 18:08 UTC | 2026-08-16 18:33 UTC | 25m |
| N555EW |  | John Wayne/Orange County Airport (KSNA) | 42AZ (42AZ) | 2026-08-16 17:12 UTC | 2026-08-16 18:30 UTC | 1h 17m |
| TGMDL | TGM | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-08-16 18:09 UTC | 2026-08-16 18:29 UTC | 20m |
| N153KD |  | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-08-16 17:54 UTC | 2026-08-16 18:28 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
