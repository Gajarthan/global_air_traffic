# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_13:45:50_UTC-green)

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

**Latest saved flight:** 2026-08-25 13:45:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 13:45:50 UTC

- **235,134** saved flights
- **71,956** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **235,134** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,833,419.4 tonnes** estimated CO2 emissions
- **164,256,198 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9431 |
| 2 | SkyWest Airlines | 8300 |
| 3 | EJA | 4555 |
| 4 | IndiGo | 3978 |
| 5 | American Airlines | 3817 |
| 6 | Southwest Airlines | 3599 |
| 7 | Delta Air Lines | 2991 |
| 8 | ENY | 2855 |
| 9 | LATAM Airlines | 2260 |
| 10 | AZU | 2192 |
| 11 | Vueling | 2014 |
| 12 | Lufthansa | 1913 |
| 13 | WIF | 1872 |
| 14 | LXJ | 1845 |
| 15 | easyJet | 1642 |
| 16 | Swiss International | 1582 |
| 17 | AXM | 1575 |
| 18 | EJU | 1504 |
| 19 | QLK | 1497 |
| 20 | United Airlines | 1485 |
| 21 | Alaska Airlines | 1417 |
| 22 | All Nippon Airways | 1401 |
| 23 | WMT | 1309 |
| 24 | GLO | 1308 |
| 25 | VIV | 1295 |
| 26 | PGT | 1282 |
| 27 | Air France | 1279 |
| 28 | Wizz Air | 1251 |
| 29 | AEE | 1168 |
| 30 | JetBlue | 1162 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 195216 |
| 2 | 🇪🇸 ES | 15116 |
| 3 | 🇧🇷 BR | 13727 |
| 4 | 🇦🇺 AU | 13336 |
| 5 | 🇨🇦 CA | 12985 |
| 6 | 🇮🇹 IT | 12799 |
| 7 | 🇮🇳 IN | 12390 |
| 8 | 🇩🇪 DE | 11600 |
| 9 | 🇬🇧 GB | 11094 |
| 10 | 🇨🇴 CO | 9905 |
| 11 | 🇯🇵 JP | 9545 |
| 12 | 🇫🇷 FR | 9429 |
| 13 | 🇹🇷 TR | 6977 |
| 14 | 🇬🇷 GR | 6934 |
| 15 | 🇲🇽 MX | 6529 |
| 16 | 🇨🇭 CH | 6291 |
| 17 | 🇳🇴 NO | 5820 |
| 18 | 🇲🇾 MY | 4223 |
| 19 | 🇹🇭 TH | 4210 |
| 20 | 🇿🇦 ZA | 4121 |
| 21 | 🇵🇱 PL | 3925 |
| 22 | 🇳🇿 NZ | 3247 |
| 23 | 🇵🇭 PH | 3239 |
| 24 | 🇬🇹 GT | 2939 |
| 25 | 🇰🇷 KR | 2757 |
| 26 | 🇭🇷 HR | 2704 |
| 27 | 🇲🇦 MA | 2384 |
| 28 | 🇲🇪 ME | 2185 |
| 29 | 🇳🇱 NL | 2110 |
| 30 | 🇮🇩 ID | 2054 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4875 |
| 2 | Denver International Airport |  | US | 3800 |
| 3 | Indira Gandhi International Airport |  | IN | 2874 |
| 4 | Tokyo International Airport |  | JP | 2842 |
| 5 | Guaymaral Airport |  | CO | 2677 |
| 6 | Harry Reid International Airport |  | US | 2521 |
| 7 | Zurich Airport |  | CH | 2467 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2398 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2359 |
| 10 | La Aurora Airport |  | GT | 2238 |
| 11 | El Dorado International Airport |  | CO | 2214 |
| 12 | Chicago O'Hare International Airport |  | US | 2118 |
| 13 | Salt Lake City International Airport |  | US | 2070 |
| 14 | Congonhas Airport |  | BR | 2002 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1973 |
| 16 | Frankfurt am Main International Airport |  | DE | 1875 |
| 17 | Madrid Barajas International Airport |  | ES | 1849 |
| 18 | Capua Airport |  | IT | 1849 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1771 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1732 |
| 21 | Malpensa International Airport |  | IT | 1685 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1666 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1649 |
| 24 | Charles de Gaulle International Airport |  | FR | 1636 |
| 25 | Macau International Airport |  | MO | 1609 |
| 26 | Ninoy Aquino International Airport |  | PH | 1565 |
| 27 | Kuala Lumpur International Airport |  | MY | 1526 |
| 28 | Charlotte/Douglas International Airport |  | US | 1515 |
| 29 | Barcelona International Airport |  | ES | 1485 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1454 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1421 |
| 32 | Viracopos International Airport |  | BR | 1402 |
| 33 | Bengaluru International Airport |  | IN | 1381 |
| 34 | Seattle-Tacoma International Airport |  | US | 1378 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1377 |
| 36 | Don Mueang International Airport |  | TH | 1366 |
| 37 | Calgary International Airport |  | CA | 1345 |
| 38 | Oslo Gardermoen Airport |  | NO | 1320 |
| 39 | Vancouver International Airport |  | CA | 1284 |
| 40 | O. R. Tambo International Airport |  | ZA | 1281 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1085 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 863 | 21m | 244 km | 3,633.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 598 | 1h 6m | 770 km | 7,944.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 595 | 24m | 225 km | 2,308.3 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 589 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 523 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 387 | 27m | 275 km | 1,833.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 364 | 1h 50m | 1,423 km | 8,933.1 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 361 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 341 | 44m | 555 km | 3,265.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 341 | 44m | 241 km | 1,416.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 330 | 21m | 250 km | 1,425.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 317 | 1h 7m | 706 km | 3,859.5 t |
| 14 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 316 | 24m | 218 km | 1,190.5 t |
| 15 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 310 | 1h 40m | 1,156 km | 6,184.4 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 292 | 19m | 99 km | 500.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 289 | 27m | 215 km | 1,070.3 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 273 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 272 | 1h 14m | 961 km | 4,508.5 t |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 267 | 29m | 304 km | 1,399.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 267 | 19m | 144 km | 664.1 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 262 | 15m | 154 km | 694.2 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 251 | 1h 50m | 1,304 km | 5,646.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DESERT3 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-08-25 13:32 UTC | 2026-08-25 13:45 UTC | 13m |
| N8286E |  | Albuquerque International Sunport Airport (KABQ) | KE80 (KE80) | 2026-08-25 12:45 UTC | 2026-08-25 13:42 UTC | 56m |
| FGJFI | FGJ | Lezignan-Corbieres Airport (LFMZ) | Lezignan-Corbieres Airport (LFMZ) | 2026-08-25 13:04 UTC | 2026-08-25 13:41 UTC | 37m |
| AIP1842 | AIP | Denver International Airport (KDEN) | 1CO7 (1CO7) | 2026-08-25 13:14 UTC | 2026-08-25 13:41 UTC | 27m |
| UIA188 | UIA | Shenzhen Bao'an International Airport (ZGSZ) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-25 12:13 UTC | 2026-08-25 13:38 UTC | 1h 24m |
| N528LP |  | Essex County Airport (KCDW) | Lehigh Valley International Airport (KABE) | 2026-08-25 12:49 UTC | 2026-08-25 13:36 UTC | 47m |
| PRCBJ | PRC | Congonhas Airport (SBSP) | Araraquara Airport (SBAQ) | 2026-08-25 12:40 UTC | 2026-08-25 13:30 UTC | 49m |
| YOQ | YOQ | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-08-25 12:41 UTC | 2026-08-25 13:29 UTC | 48m |
| PAIN21 | PAI | 2TX3 (2TX3) | Tularosa Airport (TA31) | 2026-08-25 12:57 UTC | 2026-08-25 13:28 UTC | 31m |
| ROKT14 | ROK | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Bird Nest Airport (4MS5) | 2026-08-25 12:28 UTC | 2026-08-25 13:27 UTC | 59m |
| N50376 |  | Claremore Regional Airport (KGCM) | Tulsa International Airport (KTUL) | 2026-08-25 11:57 UTC | 2026-08-25 13:27 UTC | 1h 30m |
| HBPMP | HBP | Lausanne-la Blecherette Airport (LSGL) | Lausanne-la Blecherette Airport (LSGL) | 2026-08-25 13:16 UTC | 2026-08-25 13:25 UTC | 9m |
| N967VS |  | Centennial Airport (KAPA) | KFTG (KFTG) | 2026-08-25 13:09 UTC | 2026-08-25 13:25 UTC | 16m |
| YOA | YOA | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-08-25 12:45 UTC | 2026-08-25 13:24 UTC | 38m |
| GHANC | GHA | Wolverhampton Halfpenny Green Airport (EGBO) | Wolverhampton Halfpenny Green Airport (EGBO) | 2026-08-25 12:58 UTC | 2026-08-25 13:24 UTC | 26m |
| ANTARES1 | ANT | Pirassununga Airport (SDPY) | Adhemar Ribeiro Airport (SDRD) | 2026-08-25 13:09 UTC | 2026-08-25 13:22 UTC | 13m |
| UAE380 | Emirates | Dubai International Airport (OMDB) | Zhuhai Airport (ZGSD) | 2026-08-25 06:23 UTC | 2026-08-25 13:22 UTC | 6h 58m |
| CFG1 | CFG | Leipzig Halle Airport (EDDP) | Leipzig Halle Airport (EDDP) | 2026-08-25 12:34 UTC | 2026-08-25 13:20 UTC | 45m |
| HSOVJ5 | HSO | De Kooy Airport (EHKD) | Rotterdam Airport (EHRD) | 2026-08-25 12:54 UTC | 2026-08-25 13:20 UTC | 25m |
| QTR816 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-08-25 05:53 UTC | 2026-08-25 13:20 UTC | 7h 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
