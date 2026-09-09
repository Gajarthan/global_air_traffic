# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--09_06:16:51_UTC-green)

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

**Latest saved flight:** 2026-09-09 06:16:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-09 06:16:51 UTC

- **252,286** saved flights
- **75,584** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **252,286** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,039,412.7 tonnes** estimated CO2 emissions
- **176,197,839 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10085 |
| 2 | SkyWest Airlines | 8812 |
| 3 | EJA | 4874 |
| 4 | IndiGo | 4228 |
| 5 | American Airlines | 4025 |
| 6 | Southwest Airlines | 3735 |
| 7 | Delta Air Lines | 3188 |
| 8 | ENY | 3012 |
| 9 | LATAM Airlines | 2427 |
| 10 | AZU | 2344 |
| 11 | Vueling | 2145 |
| 12 | WIF | 2021 |
| 13 | Lufthansa | 1991 |
| 14 | LXJ | 1967 |
| 15 | easyJet | 1730 |
| 16 | Swiss International | 1694 |
| 17 | AXM | 1629 |
| 18 | QLK | 1622 |
| 19 | EJU | 1617 |
| 20 | United Airlines | 1573 |
| 21 | Alaska Airlines | 1505 |
| 22 | All Nippon Airways | 1476 |
| 23 | WMT | 1429 |
| 24 | GLO | 1399 |
| 25 | PGT | 1384 |
| 26 | VIV | 1379 |
| 27 | Air France | 1376 |
| 28 | Wizz Air | 1373 |
| 29 | JetBlue | 1235 |
| 30 | AEE | 1233 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 209371 |
| 2 | 🇪🇸 ES | 16096 |
| 3 | 🇧🇷 BR | 14703 |
| 4 | 🇦🇺 AU | 14371 |
| 5 | 🇨🇦 CA | 14014 |
| 6 | 🇮🇹 IT | 13800 |
| 7 | 🇮🇳 IN | 13208 |
| 8 | 🇩🇪 DE | 12366 |
| 9 | 🇬🇧 GB | 11803 |
| 10 | 🇨🇴 CO | 11136 |
| 11 | 🇫🇷 FR | 10141 |
| 12 | 🇯🇵 JP | 9918 |
| 13 | 🇹🇷 TR | 7544 |
| 14 | 🇬🇷 GR | 7397 |
| 15 | 🇲🇽 MX | 6955 |
| 16 | 🇨🇭 CH | 6798 |
| 17 | 🇳🇴 NO | 6243 |
| 18 | 🇹🇭 TH | 4542 |
| 19 | 🇲🇾 MY | 4383 |
| 20 | 🇿🇦 ZA | 4323 |
| 21 | 🇵🇱 PL | 4199 |
| 22 | 🇳🇿 NZ | 3450 |
| 23 | 🇵🇭 PH | 3420 |
| 24 | 🇬🇹 GT | 3141 |
| 25 | 🇰🇷 KR | 2912 |
| 26 | 🇭🇷 HR | 2898 |
| 27 | 🇲🇦 MA | 2548 |
| 28 | 🇲🇪 ME | 2373 |
| 29 | 🇳🇱 NL | 2273 |
| 30 | 🇮🇩 ID | 2160 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5204 |
| 2 | Denver International Airport |  | US | 4080 |
| 3 | Indira Gandhi International Airport |  | IN | 3064 |
| 4 | Tokyo International Airport |  | JP | 2958 |
| 5 | Guaymaral Airport |  | CO | 2744 |
| 6 | Harry Reid International Airport |  | US | 2679 |
| 7 | Zurich Airport |  | CH | 2640 |
| 8 | El Dorado International Airport |  | CO | 2573 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2556 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2490 |
| 11 | La Aurora Airport |  | GT | 2396 |
| 12 | Salt Lake City International Airport |  | US | 2230 |
| 13 | Chicago O'Hare International Airport |  | US | 2199 |
| 14 | Congonhas Airport |  | BR | 2155 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2074 |
| 16 | Capua Airport |  | IT | 1988 |
| 17 | Madrid Barajas International Airport |  | ES | 1981 |
| 18 | Frankfurt am Main International Airport |  | DE | 1961 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1889 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1835 |
| 21 | Malpensa International Airport |  | IT | 1814 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1772 |
| 23 | Charles de Gaulle International Airport |  | FR | 1769 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1758 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1678 |
| 26 | Ninoy Aquino International Airport |  | PH | 1670 |
| 27 | Macau International Airport |  | MO | 1665 |
| 28 | Charlotte/Douglas International Airport |  | US | 1590 |
| 29 | Barcelona International Airport |  | ES | 1590 |
| 30 | Kuala Lumpur International Airport |  | MY | 1578 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1549 |
| 32 | Viracopos International Airport |  | BR | 1506 |
| 33 | Seattle-Tacoma International Airport |  | US | 1490 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1463 |
| 35 | Don Mueang International Airport |  | TH | 1454 |
| 36 | Calgary International Airport |  | CA | 1453 |
| 37 | Bengaluru International Airport |  | IN | 1439 |
| 38 | Oslo Gardermoen Airport |  | NO | 1421 |
| 39 | Vancouver International Airport |  | CA | 1412 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1363 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 937 | 21m | 244 km | 3,945.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 672 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 637 | 24m | 225 km | 2,471.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 633 | 1h 6m | 770 km | 8,408.9 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 565 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 414 | 27m | 275 km | 1,961.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 402 | 1h 50m | 1,423 km | 9,865.7 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 397 | 44m | 555 km | 3,801.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 376 | 44m | 241 km | 1,561.8 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 371 | 35m | - | - |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 353 | 21m | 250 km | 1,524.7 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 352 | 24m | 218 km | 1,326.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 337 | 23m | 55 km | 320.3 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 311 | 26m | 215 km | 1,151.8 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 300 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 296 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 289 | 1h 14m | 961 km | 4,790.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 289 | 19m | 144 km | 718.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 273 | 1h 50m | 1,304 km | 6,141.8 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 262 | 41m | 535 km | 2,419.7 t |
| 29 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 257 | 28m | 152 km | 671.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IGO5151 | IndiGo | Jamnagar Airport (VAJM) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-09 05:28 UTC | 2026-09-09 06:16 UTC | 48m |
| R20579 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-09-09 05:00 UTC | 2026-09-09 06:10 UTC | 1h 10m |
| IGO251V | IndiGo | Chhatrapati Shivaji International Airport (VABB) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-09 03:18 UTC | 2026-09-09 06:10 UTC | 2h 51m |
| MSR698 | EgyptAir | Cairo International Airport (HECA) | Cairo International Airport (HECA) | 2026-09-09 00:30 UTC | 2026-09-09 06:09 UTC | 5h 39m |
| CLX1632 | CLX | Luxembourg-Findel International Airport (ELLX) | Zhuhai Airport (ZGSD) | 2026-09-08 19:17 UTC | 2026-09-09 06:07 UTC | 10h 49m |
| AIC6NX | Air India | Cochin International Airport (VOCI) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-09 04:35 UTC | 2026-09-09 06:06 UTC | 1h 31m |
| IGO17FP | IndiGo | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 2026-09-09 04:53 UTC | 2026-09-09 06:00 UTC | 1h 6m |
| SEJ9014 | SEJ | Dubai International Airport (OMDB) | Pune Airport (VAPO) | 2026-09-09 03:20 UTC | 2026-09-09 05:54 UTC | 2h 33m |
| RYR9489 | Ryanair | Reggio Calabria Airport (LICR) | Malpensa International Airport (LIMC) | 2026-09-09 04:08 UTC | 2026-09-09 05:48 UTC | 1h 40m |
| N803DB |  | El Peco Ranch Airport (49CL) | San Carlos Airport (KSQL) | 2026-09-09 05:02 UTC | 2026-09-09 05:41 UTC | 39m |
| N11EF |  | Reno/Tahoe International Airport (KRNO) | Rainbow Ranch Airport (ID87) | 2026-09-09 04:45 UTC | 2026-09-09 05:36 UTC | 51m |
| N66091 |  | KFTG (KFTG) | Mertens Airport (3CO2) | 2026-09-09 04:55 UTC | 2026-09-09 05:31 UTC | 35m |
| AM311 |  | Melbourne Essendon Airport (YMEN) | Strathbogie Airport (YSBG) | 2026-09-09 05:09 UTC | 2026-09-09 05:28 UTC | 18m |
| EFC68V | EFC | Al Maktoum International Airport (OMDW) | OM11 (OM11) | 2026-09-09 04:35 UTC | 2026-09-09 05:25 UTC | 49m |
| EWG42M | EWG | Paderborn Lippstadt Airport (EDLP) | Palma De Mallorca Airport (LEPA) | 2026-09-09 03:14 UTC | 2026-09-09 05:24 UTC | 2h 9m |
| STALK51 | STA | Los Alamos Airport (KLAM) | Rancho Magdalena Airport (NM01) | 2026-09-09 04:07 UTC | 2026-09-09 05:22 UTC | 1h 14m |
| KFN | KFN | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-09-09 04:52 UTC | 2026-09-09 05:22 UTC | 29m |
| VDN | VDN | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-09-09 05:14 UTC | 2026-09-09 05:20 UTC | 5m |
| HFA601 | HFA | Haifa International Airport (LLHA) | Ovda International Airport (LLOV) | 2026-09-09 04:36 UTC | 2026-09-09 05:19 UTC | 43m |
| QLK324D | QLK | Brisbane International Airport (YBBN) | Childers Airport (YCDS) | 2026-09-09 04:48 UTC | 2026-09-09 05:15 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
