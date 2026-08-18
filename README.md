# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_05:47:32_UTC-green)

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

**Latest saved flight:** 2026-08-18 05:47:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 05:47:32 UTC

- **210,946** saved flights
- **67,051** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **210,946** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,535,958.0 tonnes** estimated CO2 emissions
- **147,012,057 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8331 |
| 2 | SkyWest Airlines | 7600 |
| 3 | EJA | 4113 |
| 4 | IndiGo | 3591 |
| 5 | American Airlines | 3533 |
| 6 | Southwest Airlines | 3386 |
| 7 | Delta Air Lines | 2729 |
| 8 | ENY | 2625 |
| 9 | LATAM Airlines | 1987 |
| 10 | AZU | 1912 |
| 11 | Lufthansa | 1769 |
| 12 | Vueling | 1751 |
| 13 | WIF | 1692 |
| 14 | LXJ | 1669 |
| 15 | easyJet | 1461 |
| 16 | Swiss International | 1405 |
| 17 | AXM | 1373 |
| 18 | United Airlines | 1340 |
| 19 | QLK | 1312 |
| 20 | Alaska Airlines | 1300 |
| 21 | EJU | 1286 |
| 22 | All Nippon Airways | 1279 |
| 23 | VIV | 1163 |
| 24 | GLO | 1139 |
| 25 | Air France | 1133 |
| 26 | PGT | 1128 |
| 27 | JetBlue | 1079 |
| 28 | AEE | 1069 |
| 29 | WMT | 1069 |
| 30 | Wizz Air | 1045 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 178857 |
| 2 | 🇪🇸 ES | 13457 |
| 3 | 🇧🇷 BR | 12095 |
| 4 | 🇦🇺 AU | 11894 |
| 5 | 🇨🇦 CA | 11686 |
| 6 | 🇮🇳 IN | 11205 |
| 7 | 🇮🇹 IT | 11006 |
| 8 | 🇩🇪 DE | 10380 |
| 9 | 🇬🇧 GB | 9816 |
| 10 | 🇯🇵 JP | 8734 |
| 11 | 🇨🇴 CO | 8482 |
| 12 | 🇫🇷 FR | 8353 |
| 13 | 🇬🇷 GR | 6187 |
| 14 | 🇹🇷 TR | 6008 |
| 15 | 🇲🇽 MX | 5928 |
| 16 | 🇨🇭 CH | 5589 |
| 17 | 🇳🇴 NO | 5238 |
| 18 | 🇲🇾 MY | 3620 |
| 19 | 🇿🇦 ZA | 3519 |
| 20 | 🇵🇱 PL | 3480 |
| 21 | 🇹🇭 TH | 3379 |
| 22 | 🇳🇿 NZ | 2941 |
| 23 | 🇵🇭 PH | 2797 |
| 24 | 🇬🇹 GT | 2703 |
| 25 | 🇰🇷 KR | 2569 |
| 26 | 🇭🇷 HR | 2263 |
| 27 | 🇲🇦 MA | 2122 |
| 28 | 🇳🇱 NL | 1874 |
| 29 | 🇲🇪 ME | 1792 |
| 30 | 🇮🇩 ID | 1744 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4447 |
| 2 | Denver International Airport |  | US | 3457 |
| 3 | Tokyo International Airport |  | JP | 2620 |
| 4 | Indira Gandhi International Airport |  | IN | 2554 |
| 5 | Guaymaral Airport |  | CO | 2531 |
| 6 | Harry Reid International Airport |  | US | 2373 |
| 7 | Zurich Airport |  | CH | 2193 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2183 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2181 |
| 10 | La Aurora Airport |  | GT | 2056 |
| 11 | Chicago O'Hare International Airport |  | US | 1956 |
| 12 | El Dorado International Airport |  | CO | 1938 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1875 |
| 14 | Salt Lake City International Airport |  | US | 1873 |
| 15 | Congonhas Airport |  | BR | 1759 |
| 16 | Frankfurt am Main International Airport |  | DE | 1723 |
| 17 | Madrid Barajas International Airport |  | ES | 1646 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1599 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1594 |
| 20 | Capua Airport |  | IT | 1585 |
| 21 | Macau International Airport |  | MO | 1548 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1538 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1483 |
| 24 | Malpensa International Airport |  | IT | 1458 |
| 25 | Charles de Gaulle International Airport |  | FR | 1445 |
| 26 | Charlotte/Douglas International Airport |  | US | 1426 |
| 27 | Kuala Lumpur International Airport |  | MY | 1338 |
| 28 | Ninoy Aquino International Airport |  | PH | 1325 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1306 |
| 30 | Bengaluru International Airport |  | IN | 1293 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1281 |
| 32 | Seattle-Tacoma International Airport |  | US | 1262 |
| 33 | Barcelona International Airport |  | ES | 1262 |
| 34 | Viracopos International Airport |  | BR | 1224 |
| 35 | Calgary International Airport |  | CA | 1201 |
| 36 | Oslo Gardermoen Airport |  | NO | 1161 |
| 37 | Vitoria/Foronda Airport |  | ES | 1160 |
| 38 | Reno/Tahoe International Airport |  | US | 1150 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1134 |
| 40 | Daniel K Inouye International Airport |  | US | 1123 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1038 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 749 | 21m | 244 km | 3,153.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 519 | 1h 7m | 770 km | 6,894.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 489 | 24m | 225 km | 1,897.1 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 478 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 430 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 350 | 27m | 275 km | 1,658.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 346 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 310 | 1h 49m | 1,423 km | 7,607.9 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 308 | 44m | 241 km | 1,279.4 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 290 | 22m | 55 km | 275.6 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 270 | 21m | 250 km | 1,166.2 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 263 | 19m | 99 km | 450.5 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 257 | 27m | 215 km | 951.8 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 253 | 1h 37m | 1,156 km | 5,047.3 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 250 | 1h 14m | 961 km | 4,143.9 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 248 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 241 | 31m | 369 km | 1,534.0 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 241 | 19m | 144 km | 599.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 227 | 1h 49m | 1,304 km | 5,106.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| 72250 |  | Falcon Dam Airport (MM38) | Falcon Dam Airport (MM38) | 2026-08-18 04:43 UTC | 2026-08-18 05:47 UTC | 1h 3m |
| ALDN71 | ALD | West Sale Airport (YWSL) | West Sale Airport (YWSL) | 2026-08-18 05:35 UTC | 2026-08-18 05:38 UTC | 2m |
| NPN | NPN | Kyneton Airport (YKTN) | Melbourne Essendon Airport (YMEN) | 2026-08-18 05:06 UTC | 2026-08-18 05:38 UTC | 31m |
| STALK51 | STA | Albuquerque International Sunport Airport (KABQ) | Los Alamos Airport (KLAM) | 2026-08-18 03:27 UTC | 2026-08-18 05:23 UTC | 1h 56m |
| RYR7SN | Ryanair | Riga International Airport (EVRA) | Memmingen Allgau Airport (EDJA) | 2026-08-18 03:16 UTC | 2026-08-18 05:18 UTC | 2h 1m |
| ZSASN | ZSA | Lanseria Airport (FALA) | Ventersdorp Airport (FAVE) | 2026-08-18 04:42 UTC | 2026-08-18 05:15 UTC | 32m |
| SWR | Swiss International | Zurich Airport (LSZH) | Zurich Airport (LSZH) | 2026-08-18 05:12 UTC | 2026-08-18 05:12 UTC | 0m |
| QLK324D | QLK | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-08-18 04:45 UTC | 2026-08-18 05:12 UTC | 27m |
| NPF | NPF | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-08-18 04:56 UTC | 2026-08-18 05:09 UTC | 13m |
| IGO479 | IndiGo | Chennai International Airport (VOMM) | Hosur Airport (VO95) | 2026-08-18 04:38 UTC | 2026-08-18 05:09 UTC | 30m |
| WPF | WPF | Perth Jandakot Airport (YPJT) | Wagin Airport (YWGN) | 2026-08-18 04:48 UTC | 2026-08-18 05:08 UTC | 20m |
|  |  | Jomo Kenyatta International Airport (HKJK) | Nyeri Airport (HKNI) | 2026-08-18 04:53 UTC | 2026-08-18 05:07 UTC | 13m |
| N3854W |  | Ruder Airport (59IL) | Ruder Airport (59IL) | 2026-08-18 05:01 UTC | 2026-08-18 05:02 UTC | 0m |
| ANZ832L | ANZ | Christchurch International Airport (NZCH) | Hokitika Airfield (NZHK) | 2026-08-18 04:41 UTC | 2026-08-18 04:59 UTC | 17m |
| ANE001 | ANE | Madrid Barajas International Airport (LEMD) | Almeria International Airport (LEAM) | 2026-08-18 04:16 UTC | 2026-08-18 04:59 UTC | 42m |
| EPI258 | EPI | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-08-18 03:22 UTC | 2026-08-18 04:56 UTC | 1h 34m |
| EJU19PK | EJU | Napoli / Capodichino International Airport (LIRN) | Corte Airport (LFKT) | 2026-08-18 04:23 UTC | 2026-08-18 04:55 UTC | 31m |
| OAL098 | OAL | Limnos Airport (LGLM) | Ikaria Airport (LGIK) | 2026-08-18 04:11 UTC | 2026-08-18 04:52 UTC | 40m |
| ETD925 | Etihad Airways | Abu Dhabi International Airport (OMAA) | Zhuhai Airport (ZGSD) | 2026-08-17 21:23 UTC | 2026-08-18 04:51 UTC | 7h 27m |
| N3854W |  | B & C Airport (IL99) | Ruder Airport (59IL) | 2026-08-18 04:25 UTC | 2026-08-18 04:49 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
