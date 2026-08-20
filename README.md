# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_01:43:44_UTC-green)

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

**Latest saved flight:** 2026-08-20 01:43:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 01:43:44 UTC

- **217,961** saved flights
- **68,668** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **217,961** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,622,203.1 tonnes** estimated CO2 emissions
- **152,011,776 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8714 |
| 2 | SkyWest Airlines | 7813 |
| 3 | EJA | 4246 |
| 4 | IndiGo | 3694 |
| 5 | American Airlines | 3635 |
| 6 | Southwest Airlines | 3465 |
| 7 | Delta Air Lines | 2820 |
| 8 | ENY | 2698 |
| 9 | LATAM Airlines | 2068 |
| 10 | AZU | 2000 |
| 11 | Vueling | 1827 |
| 12 | Lufthansa | 1813 |
| 13 | WIF | 1738 |
| 14 | LXJ | 1726 |
| 15 | easyJet | 1511 |
| 16 | Swiss International | 1448 |
| 17 | AXM | 1418 |
| 18 | United Airlines | 1382 |
| 19 | EJU | 1355 |
| 20 | QLK | 1352 |
| 21 | Alaska Airlines | 1333 |
| 22 | All Nippon Airways | 1306 |
| 23 | VIV | 1194 |
| 24 | GLO | 1187 |
| 25 | Air France | 1178 |
| 26 | PGT | 1178 |
| 27 | WMT | 1142 |
| 28 | JetBlue | 1109 |
| 29 | Wizz Air | 1105 |
| 30 | AEE | 1089 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 184004 |
| 2 | 🇪🇸 ES | 13942 |
| 3 | 🇧🇷 BR | 12591 |
| 4 | 🇦🇺 AU | 12234 |
| 5 | 🇨🇦 CA | 12037 |
| 6 | 🇮🇹 IT | 11562 |
| 7 | 🇮🇳 IN | 11503 |
| 8 | 🇩🇪 DE | 10766 |
| 9 | 🇬🇧 GB | 10214 |
| 10 | 🇨🇴 CO | 8960 |
| 11 | 🇯🇵 JP | 8884 |
| 12 | 🇫🇷 FR | 8667 |
| 13 | 🇬🇷 GR | 6347 |
| 14 | 🇹🇷 TR | 6262 |
| 15 | 🇲🇽 MX | 6087 |
| 16 | 🇨🇭 CH | 5768 |
| 17 | 🇳🇴 NO | 5405 |
| 18 | 🇲🇾 MY | 3748 |
| 19 | 🇿🇦 ZA | 3685 |
| 20 | 🇵🇱 PL | 3597 |
| 21 | 🇹🇭 TH | 3548 |
| 22 | 🇳🇿 NZ | 3019 |
| 23 | 🇵🇭 PH | 2910 |
| 24 | 🇬🇹 GT | 2767 |
| 25 | 🇰🇷 KR | 2614 |
| 26 | 🇭🇷 HR | 2390 |
| 27 | 🇲🇦 MA | 2189 |
| 28 | 🇳🇱 NL | 1940 |
| 29 | 🇲🇪 ME | 1909 |
| 30 | 🇮🇩 ID | 1821 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4591 |
| 2 | Denver International Airport |  | US | 3574 |
| 3 | Tokyo International Airport |  | JP | 2669 |
| 4 | Indira Gandhi International Airport |  | IN | 2632 |
| 5 | Guaymaral Airport |  | CO | 2595 |
| 6 | Harry Reid International Airport |  | US | 2415 |
| 7 | Zurich Airport |  | CH | 2258 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2244 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2213 |
| 10 | La Aurora Airport |  | GT | 2106 |
| 11 | El Dorado International Airport |  | CO | 2044 |
| 12 | Chicago O'Hare International Airport |  | US | 2007 |
| 13 | Salt Lake City International Airport |  | US | 1928 |
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
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1519 |
| 25 | Charles de Gaulle International Airport |  | FR | 1494 |
| 26 | Charlotte/Douglas International Airport |  | US | 1462 |
| 27 | Ninoy Aquino International Airport |  | PH | 1382 |
| 28 | Kuala Lumpur International Airport |  | MY | 1379 |
| 29 | Barcelona International Airport |  | ES | 1333 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1330 |
| 31 | Bengaluru International Airport |  | IN | 1316 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1304 |
| 33 | Seattle-Tacoma International Airport |  | US | 1297 |
| 34 | Viracopos International Airport |  | BR | 1277 |
| 35 | Calgary International Airport |  | CA | 1233 |
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
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 537 | 1h 7m | 770 km | 7,133.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 510 | 24m | 225 km | 1,978.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 493 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 485 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 363 | 27m | 275 km | 1,720.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 318 | 1h 49m | 1,423 km | 7,804.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 316 | 44m | 241 km | 1,312.6 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 311 | 1h 7m | 706 km | 3,786.4 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 294 | 22m | 55 km | 279.4 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 285 | 21m | 250 km | 1,231.0 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 269 | 1h 38m | 1,156 km | 5,366.4 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 267 | 27m | 215 km | 988.9 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 258 | 1h 14m | 961 km | 4,276.5 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 258 | 13m | - | - |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 256 | 31m | 369 km | 1,629.5 t |
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
| MOJO06 | MOJ | Hammond Northshore Regional Airport (KHDC) | Slidell Airport (KASD) | 2026-08-20 01:13 UTC | 2026-08-20 01:43 UTC | 30m |
| ZJI | ZJI | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-08-20 01:20 UTC | 2026-08-20 01:41 UTC | 21m |
| ICL851 | ICL | Ben Gurion International Airport (LLBG) | Zhuhai Airport (ZGSD) | 2026-08-19 16:42 UTC | 2026-08-20 01:32 UTC | 8h 49m |
| YGW | YGW | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-08-20 00:51 UTC | 2026-08-20 01:29 UTC | 37m |
| JTZ435 | JTZ | Dekalb-Peachtree Airport (KPDK) | Dekalb-Peachtree Airport (KPDK) | 2026-08-20 01:25 UTC | 2026-08-20 01:27 UTC | 2m |
| C6037 |  | New Orleans Nas Jrb (Alvin Callender Field) Airport (KNBG) | New Orleans Nas Jrb (Alvin Callender Field) Airport (KNBG) | 2026-08-20 00:18 UTC | 2026-08-20 01:27 UTC | 1h 8m |
| N1630 |  | Fulton County Executive/Charlie Brown Field (KFTY) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-08-20 00:48 UTC | 2026-08-20 01:24 UTC | 36m |
| OXM | OXM | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-20 01:11 UTC | 2026-08-20 01:22 UTC | 11m |
| N455RS |  | Chino Airport (KCNO) | Big Bear City Airport (KL35) | 2026-08-20 00:59 UTC | 2026-08-20 01:12 UTC | 13m |
| PAG14 | PAG | Winnipeg James Armstrong Richardson International Airport (CYWG) | Brandon Municipal Airport (CYBR) | 2026-08-20 00:40 UTC | 2026-08-20 01:11 UTC | 30m |
| ZHA | ZHA | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-08-20 00:46 UTC | 2026-08-20 01:11 UTC | 24m |
| TKR03 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | Lux Field (25CD) | 2026-08-20 00:55 UTC | 2026-08-20 01:10 UTC | 15m |
|  |  | Billings Logan International Airport (KBIL) | Laurel Municipal Airport (K6S8) | 2026-08-20 01:03 UTC | 2026-08-20 01:07 UTC | 4m |
| N100UH |  | Austin-Bergstrom International Airport (KAUS) | Castle Lakes Airport (CD32) | 2026-08-19 23:34 UTC | 2026-08-20 01:07 UTC | 1h 32m |
| N625DW |  | Northeast Philadelphia Airport (KPNE) | Harrisburg International Airport (KMDT) | 2026-08-20 00:04 UTC | 2026-08-20 01:06 UTC | 1h 1m |
| N591SS |  | Reno/Tahoe International Airport (KRNO) | Lake Tahoe Airport (KTVL) | 2026-08-20 00:38 UTC | 2026-08-20 01:03 UTC | 24m |
| N41369 |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-08-20 00:23 UTC | 2026-08-20 01:01 UTC | 38m |
| N588LA |  | Northeast Philadelphia Airport (KPNE) | Lancaster Airport (KLNS) | 2026-08-20 00:19 UTC | 2026-08-20 01:01 UTC | 41m |
| JMU | JMU | Melbourne Essendon Airport (YMEN) | Kyabram Airport (YKYB) | 2026-08-20 00:35 UTC | 2026-08-20 01:00 UTC | 24m |
| TRCH39 | TRC | Mount Hotham Airport (YHOT) | Tocumwal Airport (YTOC) | 2026-08-20 00:25 UTC | 2026-08-20 00:58 UTC | 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
