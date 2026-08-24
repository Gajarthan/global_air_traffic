# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_16:08:18_UTC-green)

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

**Latest saved flight:** 2026-08-24 16:08:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 16:08:18 UTC

- **232,376** saved flights
- **71,458** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **232,376** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,800,855.6 tonnes** estimated CO2 emissions
- **162,368,439 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9332 |
| 2 | SkyWest Airlines | 8214 |
| 3 | EJA | 4487 |
| 4 | IndiGo | 3937 |
| 5 | American Airlines | 3786 |
| 6 | Southwest Airlines | 3578 |
| 7 | Delta Air Lines | 2965 |
| 8 | ENY | 2824 |
| 9 | LATAM Airlines | 2236 |
| 10 | AZU | 2160 |
| 11 | Vueling | 1988 |
| 12 | Lufthansa | 1895 |
| 13 | WIF | 1847 |
| 14 | LXJ | 1827 |
| 15 | easyJet | 1628 |
| 16 | Swiss International | 1557 |
| 17 | AXM | 1551 |
| 18 | EJU | 1487 |
| 19 | United Airlines | 1476 |
| 20 | QLK | 1474 |
| 21 | Alaska Airlines | 1397 |
| 22 | All Nippon Airways | 1386 |
| 23 | GLO | 1295 |
| 24 | WMT | 1289 |
| 25 | VIV | 1275 |
| 26 | PGT | 1269 |
| 27 | Air France | 1263 |
| 28 | Wizz Air | 1228 |
| 29 | AEE | 1157 |
| 30 | JetBlue | 1155 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 193340 |
| 2 | 🇪🇸 ES | 14930 |
| 3 | 🇧🇷 BR | 13576 |
| 4 | 🇦🇺 AU | 13162 |
| 5 | 🇨🇦 CA | 12780 |
| 6 | 🇮🇹 IT | 12649 |
| 7 | 🇮🇳 IN | 12266 |
| 8 | 🇩🇪 DE | 11462 |
| 9 | 🇬🇧 GB | 10967 |
| 10 | 🇨🇴 CO | 9682 |
| 11 | 🇯🇵 JP | 9448 |
| 12 | 🇫🇷 FR | 9306 |
| 13 | 🇹🇷 TR | 6871 |
| 14 | 🇬🇷 GR | 6844 |
| 15 | 🇲🇽 MX | 6451 |
| 16 | 🇨🇭 CH | 6203 |
| 17 | 🇳🇴 NO | 5749 |
| 18 | 🇲🇾 MY | 4143 |
| 19 | 🇹🇭 TH | 4108 |
| 20 | 🇿🇦 ZA | 4065 |
| 21 | 🇵🇱 PL | 3867 |
| 22 | 🇳🇿 NZ | 3212 |
| 23 | 🇵🇭 PH | 3184 |
| 24 | 🇬🇹 GT | 2922 |
| 25 | 🇰🇷 KR | 2726 |
| 26 | 🇭🇷 HR | 2676 |
| 27 | 🇲🇦 MA | 2358 |
| 28 | 🇲🇪 ME | 2142 |
| 29 | 🇳🇱 NL | 2084 |
| 30 | 🇮🇩 ID | 2015 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4825 |
| 2 | Denver International Airport |  | US | 3766 |
| 3 | Indira Gandhi International Airport |  | IN | 2837 |
| 4 | Tokyo International Airport |  | JP | 2818 |
| 5 | Guaymaral Airport |  | CO | 2668 |
| 6 | Harry Reid International Airport |  | US | 2496 |
| 7 | Zurich Airport |  | CH | 2428 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2372 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2336 |
| 10 | La Aurora Airport |  | GT | 2225 |
| 11 | El Dorado International Airport |  | CO | 2157 |
| 12 | Chicago O'Hare International Airport |  | US | 2098 |
| 13 | Salt Lake City International Airport |  | US | 2042 |
| 14 | Congonhas Airport |  | BR | 1980 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1961 |
| 16 | Frankfurt am Main International Airport |  | DE | 1854 |
| 17 | Madrid Barajas International Airport |  | ES | 1827 |
| 18 | Capua Airport |  | IT | 1826 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1749 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1720 |
| 21 | Malpensa International Airport |  | IT | 1667 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1659 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1636 |
| 24 | Charles de Gaulle International Airport |  | FR | 1614 |
| 25 | Macau International Airport |  | MO | 1605 |
| 26 | Ninoy Aquino International Airport |  | PH | 1533 |
| 27 | Charlotte/Douglas International Airport |  | US | 1507 |
| 28 | Kuala Lumpur International Airport |  | MY | 1498 |
| 29 | Barcelona International Airport |  | ES | 1468 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1406 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1403 |
| 32 | Viracopos International Airport |  | BR | 1382 |
| 33 | Bengaluru International Airport |  | IN | 1372 |
| 34 | Seattle-Tacoma International Airport |  | US | 1364 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1361 |
| 36 | Don Mueang International Airport |  | TH | 1339 |
| 37 | Calgary International Airport |  | CA | 1317 |
| 38 | Oslo Gardermoen Airport |  | NO | 1303 |
| 39 | O. R. Tambo International Airport |  | ZA | 1263 |
| 40 | Vitoria/Foronda Airport |  | ES | 1259 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1083 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 847 | 21m | 244 km | 3,566.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 586 | 1h 6m | 770 km | 7,784.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 581 | 24m | 225 km | 2,254.0 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 570 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 520 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 383 | 27m | 275 km | 1,814.9 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 359 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 359 | 1h 50m | 1,423 km | 8,810.4 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 338 | 44m | 241 km | 1,404.0 t |
| 11 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 327 | 44m | 555 km | 3,131.2 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 327 | 21m | 250 km | 1,412.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 308 | 24m | 218 km | 1,160.4 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 308 | 22m | 55 km | 292.7 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 303 | 1h 38m | 1,156 km | 6,044.7 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 289 | 19m | 99 km | 495.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 284 | 27m | 215 km | 1,051.8 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 275 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 270 | 1h 14m | 961 km | 4,475.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 268 | 13m | - | - |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 266 | 29m | 304 km | 1,394.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 264 | 19m | 144 km | 656.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 251 | 15m | 154 km | 665.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 248 | 1h 50m | 1,304 km | 5,579.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N859SP |  | Wittman Regional Airport (KOSH) | Baraboo/Wisconsin Dells Regional Airport (KDLL) | 2026-08-24 15:32 UTC | 2026-08-24 16:08 UTC | 36m |
| N945PC |  | Sacramento Mather Airport (KMHR) | KO70 (KO70) | 2026-08-24 15:33 UTC | 2026-08-24 16:07 UTC | 33m |
| FTO382 | FTO | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-08-24 15:38 UTC | 2026-08-24 16:07 UTC | 29m |
| N960TV |  | Weatherford Stafford Airport (KOJA) | Weatherford Stafford Airport (KOJA) | 2026-08-24 15:12 UTC | 2026-08-24 16:06 UTC | 53m |
| N136LM |  | Cobb County International/Mccollum Field (KRYY) | Pickens County Airport (KJZP) | 2026-08-24 15:41 UTC | 2026-08-24 16:02 UTC | 20m |
| CREEP31 | CRE | 75OK (75OK) | Blackwell-Tonkawa Municipal Airport (KBKN) | 2026-08-24 15:31 UTC | 2026-08-24 16:00 UTC | 28m |
| N141DA |  | Boire Field (KASH) | Boire Field (KASH) | 2026-08-24 15:51 UTC | 2026-08-24 15:59 UTC | 8m |
| N5950K |  | Merritt Island Airport (KCOI) | Merritt Island Airport (KCOI) | 2026-08-24 15:28 UTC | 2026-08-24 15:53 UTC | 25m |
| N904AZ |  | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-24 15:41 UTC | 2026-08-24 15:52 UTC | 10m |
| N859BT |  | Blue Grass Airport (KLEX) | Georgetown-Scott County Regional Airport (K27K) | 2026-08-24 14:19 UTC | 2026-08-24 15:52 UTC | 1h 32m |
| FGIBV | FGI | Chambery-Challes-les-Eaux Airport (LFLE) | Chambery-Savoie Airport (LFLB) | 2026-08-24 15:22 UTC | 2026-08-24 15:52 UTC | 29m |
| N55297 |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-08-24 15:05 UTC | 2026-08-24 15:50 UTC | 44m |
| N701NW |  | Las Cruces International Airport (KLRU) | Las Cruces International Airport (KLRU) | 2026-08-24 15:30 UTC | 2026-08-24 15:47 UTC | 17m |
| N664RM |  | Samuels Field (KBRY) | Samuels Field (KBRY) | 2026-08-24 15:06 UTC | 2026-08-24 15:47 UTC | 40m |
| N7824W |  | Reno/Tahoe International Airport (KRNO) | Silver Springs Airport (KSPZ) | 2026-08-24 15:23 UTC | 2026-08-24 15:47 UTC | 23m |
| N971WH |  | Eppley Airfield (KOMA) | Voller Airport (ND41) | 2026-08-24 14:55 UTC | 2026-08-24 15:46 UTC | 50m |
| CFG6FE | CFG | Palma De Mallorca Airport (LEPA) | Stuttgart Airport (EDDS) | 2026-08-24 14:24 UTC | 2026-08-24 15:45 UTC | 1h 21m |
| N540PL |  | Savannah/Hilton Head International Airport (KSAV) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-08-24 15:00 UTC | 2026-08-24 15:42 UTC | 41m |
| WIF74D | WIF | Bodø Airport (ENBO) | Svolvær Helle Airport (ENSH) | 2026-08-24 15:25 UTC | 2026-08-24 15:42 UTC | 17m |
| FJLRF | FJL | Pontoise - Cormeilles-en-Vexin Airport (LFPT) | Pontoise - Cormeilles-en-Vexin Airport (LFPT) | 2026-08-24 15:31 UTC | 2026-08-24 15:41 UTC | 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
