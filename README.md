# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_10:11:25_UTC-green)

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

**Latest saved flight:** 2026-08-14 10:11:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-14 10:11:25 UTC

- **194,883** saved flights
- **61,317** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **194,883** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,329,142.0 tonnes** estimated CO2 emissions
- **135,022,726 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7756 |
| 2 | SkyWest Airlines | 7016 |
| 3 | EJA | 3835 |
| 4 | IndiGo | 3359 |
| 5 | Southwest Airlines | 3031 |
| 6 | American Airlines | 3015 |
| 7 | ENY | 2410 |
| 8 | Delta Air Lines | 2298 |
| 9 | LATAM Airlines | 1825 |
| 10 | AZU | 1752 |
| 11 | Lufthansa | 1685 |
| 12 | Vueling | 1624 |
| 13 | WIF | 1613 |
| 14 | LXJ | 1542 |
| 15 | easyJet | 1344 |
| 16 | Swiss International | 1319 |
| 17 | AXM | 1271 |
| 18 | QLK | 1207 |
| 19 | EJU | 1205 |
| 20 | All Nippon Airways | 1182 |
| 21 | Alaska Airlines | 1158 |
| 22 | VIV | 1071 |
| 23 | GLO | 1047 |
| 24 | Air France | 1024 |
| 25 | PGT | 1014 |
| 26 | AEE | 1002 |
| 27 | United Airlines | 994 |
| 28 | CXK | 990 |
| 29 | WMT | 973 |
| 30 | Wizz Air | 965 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 165705 |
| 2 | 🇪🇸 ES | 12582 |
| 3 | 🇧🇷 BR | 11179 |
| 4 | 🇦🇺 AU | 11003 |
| 5 | 🇨🇦 CA | 10658 |
| 6 | 🇮🇳 IN | 10520 |
| 7 | 🇮🇹 IT | 10135 |
| 8 | 🇩🇪 DE | 9669 |
| 9 | 🇬🇧 GB | 9155 |
| 10 | 🇯🇵 JP | 7950 |
| 11 | 🇫🇷 FR | 7788 |
| 12 | 🇨🇴 CO | 7569 |
| 13 | 🇬🇷 GR | 5725 |
| 14 | 🇲🇽 MX | 5510 |
| 15 | 🇹🇷 TR | 5274 |
| 16 | 🇨🇭 CH | 5266 |
| 17 | 🇳🇴 NO | 4998 |
| 18 | 🇲🇾 MY | 3328 |
| 19 | 🇿🇦 ZA | 3278 |
| 20 | 🇵🇱 PL | 3208 |
| 21 | 🇹🇭 TH | 3028 |
| 22 | 🇳🇿 NZ | 2739 |
| 23 | 🇵🇭 PH | 2580 |
| 24 | 🇬🇹 GT | 2468 |
| 25 | 🇰🇷 KR | 2375 |
| 26 | 🇭🇷 HR | 2026 |
| 27 | 🇲🇦 MA | 1976 |
| 28 | 🇳🇱 NL | 1756 |
| 29 | 🇲🇪 ME | 1686 |
| 30 | 🇮🇩 ID | 1573 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4053 |
| 2 | Denver International Airport |  | US | 3183 |
| 3 | Tokyo International Airport |  | JP | 2440 |
| 4 | Guaymaral Airport |  | CO | 2412 |
| 5 | Indira Gandhi International Airport |  | IN | 2374 |
| 6 | Harry Reid International Airport |  | US | 2252 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2064 |
| 8 | Zurich Airport |  | CH | 2062 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2016 |
| 10 | La Aurora Airport |  | GT | 1898 |
| 11 | El Dorado International Airport |  | CO | 1774 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1746 |
| 13 | Salt Lake City International Airport |  | US | 1734 |
| 14 | Chicago O'Hare International Airport |  | US | 1702 |
| 15 | Frankfurt am Main International Airport |  | DE | 1649 |
| 16 | Congonhas Airport |  | BR | 1627 |
| 17 | Madrid Barajas International Airport |  | ES | 1532 |
| 18 | Macau International Airport |  | MO | 1529 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1493 |
| 20 | Capua Airport |  | IT | 1493 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1437 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1397 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1362 |
| 24 | Malpensa International Airport |  | IT | 1348 |
| 25 | Charles de Gaulle International Airport |  | FR | 1339 |
| 26 | Charlotte/Douglas International Airport |  | US | 1291 |
| 27 | Bengaluru International Airport |  | IN | 1239 |
| 28 | Kuala Lumpur International Airport |  | MY | 1239 |
| 29 | Ninoy Aquino International Airport |  | PH | 1219 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1215 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1197 |
| 32 | Barcelona International Airport |  | ES | 1172 |
| 33 | Viracopos International Airport |  | BR | 1128 |
| 34 | Seattle-Tacoma International Airport |  | US | 1121 |
| 35 | Calgary International Airport |  | CA | 1112 |
| 36 | Reno/Tahoe International Airport |  | US | 1104 |
| 37 | Oslo Gardermoen Airport |  | NO | 1099 |
| 38 | Daniel K Inouye International Airport |  | US | 1086 |
| 39 | Tenerife Norte Airport |  | ES | 1067 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1065 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 996 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 714 | 21m | 244 km | 3,006.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 471 | 1h 7m | 770 km | 6,256.9 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 455 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 453 | 24m | 225 km | 1,757.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 335 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 327 | 27m | 275 km | 1,549.5 t |
| 8 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 321 | 8m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 291 | 44m | 241 km | 1,208.8 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 279 | 1h 49m | 1,423 km | 6,847.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 277 | 22m | 55 km | 263.3 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 260 | 21m | 250 km | 1,123.0 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 243 | 27m | 215 km | 900.0 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 239 | 24m | 218 km | 900.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 237 | 1h 15m | 961 km | 3,928.4 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 236 | 19m | 99 km | 404.3 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 236 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 229 | 1h 38m | 1,156 km | 4,568.5 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 229 | 19m | 144 km | 569.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 221 | 31m | 369 km | 1,406.7 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 212 | 28m | 152 km | 554.0 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 211 | 1h 3m | 695 km | 2,529.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SFU51 | SFU | Isle of Wight / Sandown Airport (EGHN) | Isle of Wight / Sandown Airport (EGHN) | 2026-08-14 09:36 UTC | 2026-08-14 10:11 UTC | 35m |
| DHK366 | DHK | East Midlands Airport (EGNX) | John F Kennedy International Airport (KJFK) | 2026-08-14 02:59 UTC | 2026-08-14 10:10 UTC | 7h 10m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-14 09:34 UTC | 2026-08-14 10:06 UTC | 32m |
| DKKSY | DKK | Schanis Airport (LSZX) | Ambri Airport (LSPM) | 2026-08-14 08:51 UTC | 2026-08-14 10:04 UTC | 1h 12m |
| EFC51F | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-14 09:45 UTC | 2026-08-14 10:00 UTC | 14m |
| GPEMD | GPE | RNAS Lee-On-Solent (EGHF) | RNAS Lee-On-Solent (EGHF) | 2026-08-14 09:27 UTC | 2026-08-14 09:58 UTC | 31m |
| FIN515 | Finnair | Helsinki Vantaa Airport (EFHK) | Ranua Airport (EFRU) | 2026-08-14 08:35 UTC | 2026-08-14 09:57 UTC | 1h 22m |
| QLK916D | QLK | Canberra International Airport (YSCB) | Orange Airport (YORG) | 2026-08-14 09:38 UTC | 2026-08-14 09:56 UTC | 18m |
| EFC18A | EFC | Ras Al Khaimah International Airport (OMRK) | Ras Al Khaimah International Airport (OMRK) | 2026-08-14 09:42 UTC | 2026-08-14 09:56 UTC | 13m |
| OKCUN20 | OKC | Brno-Turany Airport (LKTB) | Kyjov Airport (LKKY) | 2026-08-14 09:16 UTC | 2026-08-14 09:56 UTC | 40m |
| OAL4MS | OAL | Eleftherios Venizelos International Airport (LGAV) | Milos Airport (LGML) | 2026-08-14 09:37 UTC | 2026-08-14 09:55 UTC | 18m |
| WIF1A | WIF | Oslo Gardermoen Airport (ENGM) | Ørsta-Volda Airport Hovden (ENOV) | 2026-08-14 08:58 UTC | 2026-08-14 09:53 UTC | 55m |
| AXM6454 | AXM | Senai International Airport (WMKJ) | Kroh Airport (WMBH) | 2026-08-14 08:56 UTC | 2026-08-14 09:50 UTC | 53m |
| KR01 |  | Václav Havel Airport (LKPR) | Letnany Airport (LKLT) | 2026-08-14 09:40 UTC | 2026-08-14 09:48 UTC | 7m |
| CHH748 | CHH | Singapore Changi International Airport (WSSS) | Shenzhen Bao'an International Airport (ZGSZ) | 2026-08-14 04:09 UTC | 2026-08-14 09:47 UTC | 5h 38m |
| WUK7BU | WUK | London Luton Airport (EGGW) | Poznań-Ławica Airport (EPPO) | 2026-08-14 08:11 UTC | 2026-08-14 09:46 UTC | 1h 34m |
| AFR11ZB | Air France | Charles de Gaulle International Airport (LFPG) | Stockholm-Arlanda Airport (ESSA) | 2026-08-14 07:38 UTC | 2026-08-14 09:42 UTC | 2h 4m |
| RYR871V | Ryanair | Sofia Airport (LBSF) | Nuremberg Airport (EDDN) | 2026-08-14 07:53 UTC | 2026-08-14 09:42 UTC | 1h 48m |
| EAI17W | EAI | Manchester Airport (EGCC) | Dublin Airport (EIDW) | 2026-08-14 08:51 UTC | 2026-08-14 09:42 UTC | 51m |
| CXK1094 | CXK | Long Island Mac Arthur Airport (KISP) | Long Island Mac Arthur Airport (KISP) | 2026-08-14 09:37 UTC | 2026-08-14 09:41 UTC | 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
