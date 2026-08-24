# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_05:39:08_UTC-green)

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

**Latest saved flight:** 2026-08-24 05:39:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 05:39:08 UTC

- **230,944** saved flights
- **71,193** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **230,944** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,784,696.7 tonnes** estimated CO2 emissions
- **161,431,690 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9258 |
| 2 | SkyWest Airlines | 8205 |
| 3 | EJA | 4472 |
| 4 | IndiGo | 3903 |
| 5 | American Airlines | 3785 |
| 6 | Southwest Airlines | 3573 |
| 7 | Delta Air Lines | 2957 |
| 8 | ENY | 2818 |
| 9 | LATAM Airlines | 2224 |
| 10 | AZU | 2148 |
| 11 | Vueling | 1958 |
| 12 | Lufthansa | 1874 |
| 13 | LXJ | 1824 |
| 14 | WIF | 1814 |
| 15 | easyJet | 1608 |
| 16 | Swiss International | 1539 |
| 17 | AXM | 1534 |
| 18 | EJU | 1470 |
| 19 | United Airlines | 1469 |
| 20 | QLK | 1462 |
| 21 | Alaska Airlines | 1396 |
| 22 | All Nippon Airways | 1377 |
| 23 | GLO | 1289 |
| 24 | VIV | 1271 |
| 25 | WMT | 1264 |
| 26 | PGT | 1262 |
| 27 | Air France | 1253 |
| 28 | Wizz Air | 1212 |
| 29 | JetBlue | 1151 |
| 30 | AEE | 1150 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 192817 |
| 2 | 🇪🇸 ES | 14785 |
| 3 | 🇧🇷 BR | 13513 |
| 4 | 🇦🇺 AU | 13087 |
| 5 | 🇨🇦 CA | 12753 |
| 6 | 🇮🇹 IT | 12484 |
| 7 | 🇮🇳 IN | 12145 |
| 8 | 🇩🇪 DE | 11332 |
| 9 | 🇬🇧 GB | 10848 |
| 10 | 🇨🇴 CO | 9611 |
| 11 | 🇯🇵 JP | 9381 |
| 12 | 🇫🇷 FR | 9220 |
| 13 | 🇹🇷 TR | 6812 |
| 14 | 🇬🇷 GR | 6786 |
| 15 | 🇲🇽 MX | 6430 |
| 16 | 🇨🇭 CH | 6117 |
| 17 | 🇳🇴 NO | 5661 |
| 18 | 🇲🇾 MY | 4095 |
| 19 | 🇹🇭 TH | 4034 |
| 20 | 🇿🇦 ZA | 4015 |
| 21 | 🇵🇱 PL | 3829 |
| 22 | 🇳🇿 NZ | 3206 |
| 23 | 🇵🇭 PH | 3169 |
| 24 | 🇬🇹 GT | 2903 |
| 25 | 🇰🇷 KR | 2718 |
| 26 | 🇭🇷 HR | 2638 |
| 27 | 🇲🇦 MA | 2339 |
| 28 | 🇲🇪 ME | 2112 |
| 29 | 🇳🇱 NL | 2059 |
| 30 | 🇮🇩 ID | 2003 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4820 |
| 2 | Denver International Airport |  | US | 3764 |
| 3 | Indira Gandhi International Airport |  | IN | 2814 |
| 4 | Tokyo International Airport |  | JP | 2799 |
| 5 | Guaymaral Airport |  | CO | 2654 |
| 6 | Harry Reid International Airport |  | US | 2491 |
| 7 | Zurich Airport |  | CH | 2404 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2363 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2325 |
| 10 | La Aurora Airport |  | GT | 2212 |
| 11 | El Dorado International Airport |  | CO | 2148 |
| 12 | Chicago O'Hare International Airport |  | US | 2096 |
| 13 | Salt Lake City International Airport |  | US | 2038 |
| 14 | Congonhas Airport |  | BR | 1970 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1958 |
| 16 | Frankfurt am Main International Airport |  | DE | 1843 |
| 17 | Madrid Barajas International Airport |  | ES | 1808 |
| 18 | Capua Airport |  | IT | 1807 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1737 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1719 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1655 |
| 22 | Malpensa International Airport |  | IT | 1649 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1626 |
| 24 | Macau International Airport |  | MO | 1602 |
| 25 | Charles de Gaulle International Airport |  | FR | 1598 |
| 26 | Ninoy Aquino International Airport |  | PH | 1524 |
| 27 | Charlotte/Douglas International Airport |  | US | 1507 |
| 28 | Kuala Lumpur International Airport |  | MY | 1484 |
| 29 | Barcelona International Airport |  | ES | 1442 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1400 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1388 |
| 32 | Viracopos International Airport |  | BR | 1374 |
| 33 | Seattle-Tacoma International Airport |  | US | 1362 |
| 34 | Bengaluru International Airport |  | IN | 1362 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1360 |
| 36 | Don Mueang International Airport |  | TH | 1319 |
| 37 | Calgary International Airport |  | CA | 1316 |
| 38 | Oslo Gardermoen Airport |  | NO | 1283 |
| 39 | Vancouver International Airport |  | CA | 1253 |
| 40 | Vitoria/Foronda Airport |  | ES | 1252 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1076 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 844 | 21m | 244 km | 3,553.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 581 | 1h 6m | 770 km | 7,718.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 576 | 24m | 225 km | 2,234.6 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 563 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 517 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 380 | 27m | 275 km | 1,800.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 356 | 1h 50m | 1,423 km | 8,736.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 334 | 44m | 241 km | 1,387.4 t |
| 11 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 325 | 21m | 250 km | 1,403.8 t |
| 12 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 316 | 44m | 555 km | 3,025.9 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 307 | 22m | 55 km | 291.8 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 300 | 24m | 218 km | 1,130.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 299 | 1h 38m | 1,156 km | 5,964.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 285 | 19m | 99 km | 488.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 280 | 27m | 215 km | 1,037.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 275 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 270 | 1h 14m | 961 km | 4,475.4 t |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 266 | 29m | 304 km | 1,394.4 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 265 | 13m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 262 | 19m | 144 km | 651.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 247 | 1h 50m | 1,304 km | 5,556.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 245 | 28m | 152 km | 640.3 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 244 | 15m | 154 km | 646.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N738EP |  | Skagit Regional Airport (KBVS) | Bremerton Ntl Airport (KPWT) | 2026-08-24 04:41 UTC | 2026-08-24 05:39 UTC | 57m |
| XCN70 | XCN | Ephrata Municipal Airport (KEPH) | Fowler Field (02WN) | 2026-08-24 04:41 UTC | 2026-08-24 05:27 UTC | 46m |
| TMN121 | TMN | Melbourne International Airport (YMML) | Chek Lap Kok International Airport (VHHH) | 2026-08-23 20:17 UTC | 2026-08-24 05:25 UTC | 9h 8m |
| ZKHUP | ZKH | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-08-24 05:10 UTC | 2026-08-24 05:23 UTC | 13m |
| CPA250 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-08-23 18:03 UTC | 2026-08-24 05:18 UTC | 11h 15m |
| AM313 |  | Melbourne Essendon Airport (YMEN) | Strathbogie Airport (YSBG) | 2026-08-24 04:51 UTC | 2026-08-24 05:12 UTC | 20m |
| RXA6133 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Cooma/Polo Flat (Unlic) Airport (YPFT) | 2026-08-24 04:26 UTC | 2026-08-24 05:06 UTC | 40m |
| DBB | DBB | Brisbane Archerfield Airport (YBAF) | Toowoomba Airport (YTWB) | 2026-08-24 03:26 UTC | 2026-08-24 05:05 UTC | 1h 39m |
| NIA232 | NIA | King Fahd International Airport (OEDF) | Hulwan (HE15) | 2026-08-24 02:44 UTC | 2026-08-24 05:00 UTC | 2h 15m |
| JA08NA |  | Iruma Air Base (RJTJ) | Iruma Air Base (RJTJ) | 2026-08-24 04:22 UTC | 2026-08-24 04:59 UTC | 37m |
| SKY713 | SKY | Tokyo International Airport (RJTT) | Chitose Air Base (RJCJ) | 2026-08-24 03:36 UTC | 2026-08-24 04:54 UTC | 1h 18m |
| ASA1112 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-08-24 04:30 UTC | 2026-08-24 04:53 UTC | 22m |
| ADO83 | ADO | Tokyo International Airport (RJTT) | Asahikawa Airport (RJCA) | 2026-08-24 03:34 UTC | 2026-08-24 04:53 UTC | 1h 18m |
| FC79 |  | Gimpo International Airport (RKSS) | G 417 Airport (RK34) | 2026-08-24 04:33 UTC | 2026-08-24 04:51 UTC | 18m |
| RYR4FL | Ryanair | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Bari / Palese International Airport (LIBD) | 2026-08-24 04:18 UTC | 2026-08-24 04:50 UTC | 31m |
| AXM6490 | AXM | Kota Kinabalu International Airport (WBKK) | Telupid Airport (WBKE) | 2026-08-24 04:35 UTC | 2026-08-24 04:48 UTC | 12m |
| YTK | YTK | Watts Bridge Airport (YWSG) | Sunshine Coast Airport (YBMC) | 2026-08-24 04:21 UTC | 2026-08-24 04:46 UTC | 24m |
| IGO363C | IndiGo | Bengaluru International Airport (VOBL) | Purnea Airport (VEPU) | 2026-08-24 01:07 UTC | 2026-08-24 04:45 UTC | 3h 37m |
| J937KT |  | Adi Sutjipto International Airport (WARJ) | Gading Wonosari Airport (WI1G) | 2026-08-24 04:35 UTC | 2026-08-24 04:44 UTC | 8m |
| SEH1JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Mikonos Airport (LGMK) | 2026-08-24 04:22 UTC | 2026-08-24 04:42 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
