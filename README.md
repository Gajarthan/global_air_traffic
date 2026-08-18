# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_10:59:41_UTC-green)

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

**Latest saved flight:** 2026-08-18 10:59:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 10:59:41 UTC

- **211,506** saved flights
- **67,126** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **211,506** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,543,318.2 tonnes** estimated CO2 emissions
- **147,438,734 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8375 |
| 2 | SkyWest Airlines | 7600 |
| 3 | EJA | 4113 |
| 4 | IndiGo | 3615 |
| 5 | American Airlines | 3534 |
| 6 | Southwest Airlines | 3386 |
| 7 | Delta Air Lines | 2729 |
| 8 | ENY | 2625 |
| 9 | LATAM Airlines | 1987 |
| 10 | AZU | 1913 |
| 11 | Lufthansa | 1775 |
| 12 | Vueling | 1767 |
| 13 | WIF | 1699 |
| 14 | LXJ | 1669 |
| 15 | easyJet | 1467 |
| 16 | Swiss International | 1415 |
| 17 | AXM | 1384 |
| 18 | United Airlines | 1341 |
| 19 | QLK | 1320 |
| 20 | Alaska Airlines | 1302 |
| 21 | EJU | 1298 |
| 22 | All Nippon Airways | 1284 |
| 23 | VIV | 1164 |
| 24 | Air France | 1141 |
| 25 | GLO | 1139 |
| 26 | PGT | 1132 |
| 27 | JetBlue | 1080 |
| 28 | WMT | 1076 |
| 29 | AEE | 1072 |
| 30 | Wizz Air | 1050 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 178888 |
| 2 | 🇪🇸 ES | 13544 |
| 3 | 🇧🇷 BR | 12098 |
| 4 | 🇦🇺 AU | 11952 |
| 5 | 🇨🇦 CA | 11696 |
| 6 | 🇮🇳 IN | 11267 |
| 7 | 🇮🇹 IT | 11077 |
| 8 | 🇩🇪 DE | 10437 |
| 9 | 🇬🇧 GB | 9851 |
| 10 | 🇯🇵 JP | 8772 |
| 11 | 🇨🇴 CO | 8486 |
| 12 | 🇫🇷 FR | 8405 |
| 13 | 🇬🇷 GR | 6200 |
| 14 | 🇹🇷 TR | 6033 |
| 15 | 🇲🇽 MX | 5931 |
| 16 | 🇨🇭 CH | 5609 |
| 17 | 🇳🇴 NO | 5267 |
| 18 | 🇲🇾 MY | 3655 |
| 19 | 🇿🇦 ZA | 3563 |
| 20 | 🇵🇱 PL | 3490 |
| 21 | 🇹🇭 TH | 3421 |
| 22 | 🇳🇿 NZ | 2945 |
| 23 | 🇵🇭 PH | 2819 |
| 24 | 🇬🇹 GT | 2703 |
| 25 | 🇰🇷 KR | 2579 |
| 26 | 🇭🇷 HR | 2286 |
| 27 | 🇲🇦 MA | 2132 |
| 28 | 🇳🇱 NL | 1884 |
| 29 | 🇲🇪 ME | 1810 |
| 30 | 🇮🇩 ID | 1764 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4448 |
| 2 | Denver International Airport |  | US | 3457 |
| 3 | Tokyo International Airport |  | JP | 2629 |
| 4 | Indira Gandhi International Airport |  | IN | 2570 |
| 5 | Guaymaral Airport |  | CO | 2531 |
| 6 | Harry Reid International Airport |  | US | 2373 |
| 7 | Zurich Airport |  | CH | 2205 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2184 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2183 |
| 10 | La Aurora Airport |  | GT | 2056 |
| 11 | Chicago O'Hare International Airport |  | US | 1956 |
| 12 | El Dorado International Airport |  | CO | 1940 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1875 |
| 14 | Salt Lake City International Airport |  | US | 1874 |
| 15 | Congonhas Airport |  | BR | 1759 |
| 16 | Frankfurt am Main International Airport |  | DE | 1727 |
| 17 | Madrid Barajas International Airport |  | ES | 1657 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1599 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1595 |
| 20 | Capua Airport |  | IT | 1593 |
| 21 | Macau International Airport |  | MO | 1551 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1539 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1489 |
| 24 | Malpensa International Airport |  | IT | 1466 |
| 25 | Charles de Gaulle International Airport |  | FR | 1454 |
| 26 | Charlotte/Douglas International Airport |  | US | 1426 |
| 27 | Kuala Lumpur International Airport |  | MY | 1348 |
| 28 | Ninoy Aquino International Airport |  | PH | 1336 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1306 |
| 30 | Bengaluru International Airport |  | IN | 1297 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1281 |
| 32 | Barcelona International Airport |  | ES | 1275 |
| 33 | Seattle-Tacoma International Airport |  | US | 1262 |
| 34 | Viracopos International Airport |  | BR | 1224 |
| 35 | Calgary International Airport |  | CA | 1201 |
| 36 | Oslo Gardermoen Airport |  | NO | 1171 |
| 37 | Vitoria/Foronda Airport |  | ES | 1168 |
| 38 | Reno/Tahoe International Airport |  | US | 1150 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1143 |
| 40 | Don Mueang International Airport |  | TH | 1131 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1038 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 752 | 21m | 244 km | 3,166.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 523 | 1h 7m | 770 km | 6,947.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 493 | 24m | 225 km | 1,912.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 478 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 430 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 351 | 27m | 275 km | 1,663.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 348 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 311 | 1h 49m | 1,423 km | 7,632.4 t |
| 10 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 311 | 14m | 114 km | 610.0 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 309 | 44m | 241 km | 1,283.5 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 290 | 22m | 55 km | 275.6 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 274 | 21m | 250 km | 1,183.5 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 263 | 19m | 99 km | 450.5 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 258 | 27m | 215 km | 955.5 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 257 | 1h 37m | 1,156 km | 5,127.1 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 250 | 19m | 165 km | 711.1 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 250 | 1h 14m | 961 km | 4,143.9 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 249 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 242 | 31m | 369 km | 1,540.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 242 | 19m | 144 km | 602.0 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 227 | 1h 49m | 1,304 km | 5,106.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AAL962 | American Airlines | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-18 01:26 UTC | 2026-08-18 10:59 UTC | 9h 33m |
| SGA2563 | SGA | Sharjah International Airport (OMSJ) | Zhuhai Airport (ZGSD) | 2026-08-18 03:12 UTC | 2026-08-18 10:52 UTC | 7h 39m |
| NSZ3085 | NSZ | Aalborg Airport (EKYT) | Copenhagen Kastrup Airport (EKCH) | 2026-08-18 10:22 UTC | 2026-08-18 10:51 UTC | 29m |
| R21200 |  | Scotts Airport (0AK0) | Ladd Army Air Field (PAFB) | 2026-08-18 10:16 UTC | 2026-08-18 10:51 UTC | 34m |
| N704VY |  | Ocala International-Jim Taylor Field (KOCF) | Williston Regional Airport (KX60) | 2026-08-18 10:22 UTC | 2026-08-18 10:50 UTC | 28m |
| ZAM40 | ZAM | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-08-18 10:34 UTC | 2026-08-18 10:50 UTC | 16m |
| UAE9846 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-08-18 03:40 UTC | 2026-08-18 10:48 UTC | 7h 7m |
| N212HF |  | New Richmond Regional Airport (KRNH) | Flying Cloud Airport (KFCM) | 2026-08-18 10:28 UTC | 2026-08-18 10:41 UTC | 13m |
| AMX001 | Aeromexico | Licenciado Benito Juarez International Airport (MMMX) | Madrid Barajas International Airport (LEMD) | 2026-08-18 00:14 UTC | 2026-08-18 10:30 UTC | 10h 15m |
| OKUUR14 | OKU | Breclav Airport (LKBA) | Breclav Airport (LKBA) | 2026-08-18 10:12 UTC | 2026-08-18 10:28 UTC | 15m |
| GAG131H | GAG | Aarhus Airport (EKAH) | Aarhus Airport (EKAH) | 2026-08-18 10:22 UTC | 2026-08-18 10:22 UTC | 0m |
| QTR9950 | Qatar Airways | Doha International Airport (OTBD) | Doha International Airport (OTBD) | 2026-08-18 09:51 UTC | 2026-08-18 10:22 UTC | 31m |
| GBBXW | GBB | Gloucestershire Airport (EGBJ) | Wellesbourne Mountford Airport (EGBW) | 2026-08-18 09:51 UTC | 2026-08-18 10:19 UTC | 27m |
| ZSILE | ZSI | Wonderboom Airport (FAWB) | Witbank Airport (FAWI) | 2026-08-18 10:00 UTC | 2026-08-18 10:14 UTC | 14m |
| HFA851 | HFA | Haifa International Airport (LLHA) | Paphos International Airport (LCPH) | 2026-08-18 09:25 UTC | 2026-08-18 10:13 UTC | 48m |
| EZY51MN | easyJet | Edinburgh Airport (EGPH) | London Stansted Airport (EGSS) | 2026-08-18 09:13 UTC | 2026-08-18 10:07 UTC | 54m |
| ANE2218 | ANE | Palma De Mallorca Airport (LEPA) | Pamplona Airport (LEPP) | 2026-08-18 08:42 UTC | 2026-08-18 10:00 UTC | 1h 18m |
| IGO38E | IndiGo | Abu Dhabi International Airport (OMAA) | Mysore Airport (VOMY) | 2026-08-17 22:03 UTC | 2026-08-18 10:00 UTC | 11h 56m |
| ABY130 | ABY | Sharjah International Airport (OMSJ) | Sirri Island Airport (OIBS) | 2026-08-18 09:42 UTC | 2026-08-18 09:57 UTC | 15m |
| ANE2328 | ANE | Palma De Mallorca Airport (LEPA) | Calaf-Sallavinera Airport (LECF) | 2026-08-18 09:12 UTC | 2026-08-18 09:56 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
