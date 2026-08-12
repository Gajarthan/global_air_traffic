# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_10:14:48_UTC-green)

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

**Latest saved flight:** 2026-08-12 10:14:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-12 10:14:48 UTC

- **189,013** saved flights
- **59,783** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **189,013** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,264,836.4 tonnes** estimated CO2 emissions
- **131,294,864 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7500 |
| 2 | SkyWest Airlines | 6863 |
| 3 | EJA | 3722 |
| 4 | IndiGo | 3286 |
| 5 | Southwest Airlines | 2956 |
| 6 | American Airlines | 2934 |
| 7 | ENY | 2344 |
| 8 | Delta Air Lines | 2220 |
| 9 | LATAM Airlines | 1762 |
| 10 | AZU | 1699 |
| 11 | Lufthansa | 1651 |
| 12 | Vueling | 1570 |
| 13 | WIF | 1567 |
| 14 | LXJ | 1478 |
| 15 | easyJet | 1301 |
| 16 | Swiss International | 1286 |
| 17 | AXM | 1250 |
| 18 | QLK | 1168 |
| 19 | EJU | 1165 |
| 20 | All Nippon Airways | 1154 |
| 21 | Alaska Airlines | 1132 |
| 22 | VIV | 1045 |
| 23 | GLO | 1017 |
| 24 | Air France | 985 |
| 25 | PGT | 974 |
| 26 | AEE | 971 |
| 27 | United Airlines | 971 |
| 28 | CXK | 966 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 938 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 161170 |
| 2 | 🇪🇸 ES | 12173 |
| 3 | 🇧🇷 BR | 10835 |
| 4 | 🇦🇺 AU | 10642 |
| 5 | 🇨🇦 CA | 10341 |
| 6 | 🇮🇳 IN | 10304 |
| 7 | 🇮🇹 IT | 9797 |
| 8 | 🇩🇪 DE | 9339 |
| 9 | 🇬🇧 GB | 8782 |
| 10 | 🇯🇵 JP | 7745 |
| 11 | 🇫🇷 FR | 7551 |
| 12 | 🇨🇴 CO | 7180 |
| 13 | 🇬🇷 GR | 5534 |
| 14 | 🇲🇽 MX | 5383 |
| 15 | 🇨🇭 CH | 5061 |
| 16 | 🇹🇷 TR | 5012 |
| 17 | 🇳🇴 NO | 4859 |
| 18 | 🇲🇾 MY | 3271 |
| 19 | 🇿🇦 ZA | 3164 |
| 20 | 🇵🇱 PL | 3130 |
| 21 | 🇹🇭 TH | 2930 |
| 22 | 🇳🇿 NZ | 2682 |
| 23 | 🇵🇭 PH | 2503 |
| 24 | 🇬🇹 GT | 2399 |
| 25 | 🇰🇷 KR | 2331 |
| 26 | 🇲🇦 MA | 1918 |
| 27 | 🇭🇷 HR | 1915 |
| 28 | 🇳🇱 NL | 1685 |
| 29 | 🇲🇪 ME | 1685 |
| 30 | 🇲🇴 MO | 1525 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3924 |
| 2 | Denver International Airport |  | US | 3116 |
| 3 | Tokyo International Airport |  | JP | 2391 |
| 4 | Indira Gandhi International Airport |  | IN | 2323 |
| 5 | Guaymaral Airport |  | CO | 2312 |
| 6 | Harry Reid International Airport |  | US | 2210 |
| 7 | Zurich Airport |  | CH | 2006 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2004 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1956 |
| 10 | La Aurora Airport |  | GT | 1843 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1714 |
| 12 | El Dorado International Airport |  | CO | 1699 |
| 13 | Salt Lake City International Airport |  | US | 1681 |
| 14 | Chicago O'Hare International Airport |  | US | 1661 |
| 15 | Frankfurt am Main International Airport |  | DE | 1620 |
| 16 | Congonhas Airport |  | BR | 1575 |
| 17 | Macau International Airport |  | MO | 1525 |
| 18 | Madrid Barajas International Airport |  | ES | 1488 |
| 19 | Capua Airport |  | IT | 1471 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1466 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1398 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1350 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1323 |
| 24 | Malpensa International Airport |  | IT | 1303 |
| 25 | Charles de Gaulle International Airport |  | FR | 1292 |
| 26 | Charlotte/Douglas International Airport |  | US | 1264 |
| 27 | Kuala Lumpur International Airport |  | MY | 1223 |
| 28 | Bengaluru International Airport |  | IN | 1213 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1184 |
| 30 | Ninoy Aquino International Airport |  | PH | 1182 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1161 |
| 32 | Barcelona International Airport |  | ES | 1133 |
| 33 | Reno/Tahoe International Airport |  | US | 1094 |
| 34 | Viracopos International Airport |  | BR | 1091 |
| 35 | Seattle-Tacoma International Airport |  | US | 1090 |
| 36 | Calgary International Airport |  | CA | 1077 |
| 37 | Daniel K Inouye International Airport |  | US | 1064 |
| 38 | Oslo Gardermoen Airport |  | NO | 1053 |
| 39 | Tenerife Norte Airport |  | ES | 1038 |
| 40 | Vitoria/Foronda Airport |  | ES | 1023 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 953 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 692 | 21m | 244 km | 2,913.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 458 | 1h 7m | 770 km | 6,084.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 442 | 24m | 225 km | 1,714.8 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 439 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 332 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 317 | 27m | 275 km | 1,502.1 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 307 | 14m | 114 km | 602.1 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 284 | 8m | - | - |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 282 | 44m | 241 km | 1,171.4 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 271 | 22m | 55 km | 257.6 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 270 | 1h 49m | 1,423 km | 6,626.2 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 251 | 20m | 250 km | 1,084.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 236 | 27m | 215 km | 874.0 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 235 | 13m | - | - |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 232 | 12m | - | - |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 231 | 19m | 99 km | 395.7 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 230 | 1h 15m | 961 km | 3,812.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 225 | 1h 38m | 1,156 km | 4,488.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 225 | 19m | 144 km | 559.7 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 223 | 24m | 218 km | 840.1 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 218 | 31m | 369 km | 1,387.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 206 | 1h 48m | 1,304 km | 4,634.5 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 206 | 28m | 152 km | 538.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GBIHO | GBI | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-12 09:50 UTC | 2026-08-12 10:14 UTC | 24m |
| UAL966 | United Airlines | Newark Liberty International Airport (KEWR) | Napoli / Capodichino International Airport (LIRN) | 2026-08-12 02:21 UTC | 2026-08-12 10:07 UTC | 7h 45m |
| RTV2M | RTV | Viseu Airport (LPVZ) | Viseu Airport (LPVZ) | 2026-08-12 09:45 UTC | 2026-08-12 10:02 UTC | 16m |
| N958AL |  | Boeing Field/King County International Airport (KBFI) | Boeing Field/King County International Airport (KBFI) | 2026-08-12 09:57 UTC | 2026-08-12 09:57 UTC | 0m |
| CJT488 | CJT | Louisville Muhammad Ali International Airport (KSDF) | Toronto Pearson International Airport (CYYZ) | 2026-08-12 08:31 UTC | 2026-08-12 09:53 UTC | 1h 22m |
| JJP519 | JJP | Narita International Airport (RJAA) | Ashiya Airport (RJFA) | 2026-08-12 08:34 UTC | 2026-08-12 09:51 UTC | 1h 16m |
| HKS51 | HKS | Humberside Airport (EGNJ) | EGYO (EGYO) | 2026-08-12 09:33 UTC | 2026-08-12 09:51 UTC | 17m |
| LEADER | LEA | Nevatim Air Base (LLNV) | Yotvata Airfield (LLYT) | 2026-08-12 09:16 UTC | 2026-08-12 09:45 UTC | 28m |
|  |  | Viseu Airport (LPVZ) | Viseu Airport (LPVZ) | 2026-08-12 09:38 UTC | 2026-08-12 09:43 UTC | 4m |
| JAL327 | Japan Airlines | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-08-12 08:26 UTC | 2026-08-12 09:39 UTC | 1h 13m |
| RTV2M | RTV | Vilar Da Luz Airport (LPVL) | Viseu Airport (LPVZ) | 2026-08-12 08:58 UTC | 2026-08-12 09:34 UTC | 36m |
| BYA651 | BYA | Rickenbacker International Airport (KLCK) | Trenton Mercer Airport (KTTN) | 2026-08-12 08:10 UTC | 2026-08-12 09:33 UTC | 1h 22m |
| HBZYW | HBZ | Wangen-Lachen Airport (LSPV) | Wangen-Lachen Airport (LSPV) | 2026-08-12 08:46 UTC | 2026-08-12 09:33 UTC | 46m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Sandane Airport Anda (ENSD) | 2026-08-12 09:08 UTC | 2026-08-12 09:31 UTC | 23m |
| RYR23DQ | Ryanair | Alicante International Airport (LEAL) | Pardubice Airport (LKPD) | 2026-08-12 06:58 UTC | 2026-08-12 09:30 UTC | 2h 31m |
| TUTOR895 | TUT | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-12 09:07 UTC | 2026-08-12 09:30 UTC | 22m |
| O288 |  | Casement Air Base (EIME) | Casement Air Base (EIME) | 2026-08-12 08:53 UTC | 2026-08-12 09:29 UTC | 36m |
| GFD1 | GFD | Schleswig Airport (ETNS) | Wunstorf Airport (ETNW) | 2026-08-12 08:05 UTC | 2026-08-12 09:29 UTC | 1h 24m |
| JJP587 | JJP | Chubu Centrair International Airport (RJGG) | Ashiya Airport (RJFA) | 2026-08-12 08:41 UTC | 2026-08-12 09:29 UTC | 47m |
| HBZVS | HBZ | Courchevel Airport (LFLJ) | Muenster Aero Airport (LSPU) | 2026-08-12 08:20 UTC | 2026-08-12 09:27 UTC | 1h 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
