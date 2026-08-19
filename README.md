# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_03:19:16_UTC-green)

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

**Latest saved flight:** 2026-08-19 03:19:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 03:19:16 UTC

- **214,235** saved flights
- **67,706** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **214,235** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,574,941.9 tonnes** estimated CO2 emissions
- **149,271,994 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8487 |
| 2 | SkyWest Airlines | 7694 |
| 3 | EJA | 4183 |
| 4 | IndiGo | 3650 |
| 5 | American Airlines | 3579 |
| 6 | Southwest Airlines | 3428 |
| 7 | Delta Air Lines | 2765 |
| 8 | ENY | 2660 |
| 9 | LATAM Airlines | 2026 |
| 10 | AZU | 1960 |
| 11 | Vueling | 1791 |
| 12 | Lufthansa | 1784 |
| 13 | WIF | 1712 |
| 14 | LXJ | 1693 |
| 15 | easyJet | 1483 |
| 16 | Swiss International | 1427 |
| 17 | AXM | 1397 |
| 18 | United Airlines | 1360 |
| 19 | QLK | 1329 |
| 20 | Alaska Airlines | 1317 |
| 21 | EJU | 1316 |
| 22 | All Nippon Airways | 1292 |
| 23 | VIV | 1181 |
| 24 | GLO | 1163 |
| 25 | PGT | 1156 |
| 26 | Air France | 1154 |
| 27 | WMT | 1103 |
| 28 | JetBlue | 1091 |
| 29 | AEE | 1080 |
| 30 | Wizz Air | 1068 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 181272 |
| 2 | 🇪🇸 ES | 13682 |
| 3 | 🇧🇷 BR | 12337 |
| 4 | 🇦🇺 AU | 12040 |
| 5 | 🇨🇦 CA | 11843 |
| 6 | 🇮🇳 IN | 11374 |
| 7 | 🇮🇹 IT | 11267 |
| 8 | 🇩🇪 DE | 10542 |
| 9 | 🇬🇧 GB | 9971 |
| 10 | 🇯🇵 JP | 8808 |
| 11 | 🇨🇴 CO | 8737 |
| 12 | 🇫🇷 FR | 8490 |
| 13 | 🇬🇷 GR | 6263 |
| 14 | 🇹🇷 TR | 6138 |
| 15 | 🇲🇽 MX | 6014 |
| 16 | 🇨🇭 CH | 5656 |
| 17 | 🇳🇴 NO | 5310 |
| 18 | 🇲🇾 MY | 3693 |
| 19 | 🇿🇦 ZA | 3606 |
| 20 | 🇵🇱 PL | 3526 |
| 21 | 🇹🇭 TH | 3461 |
| 22 | 🇳🇿 NZ | 2977 |
| 23 | 🇵🇭 PH | 2859 |
| 24 | 🇬🇹 GT | 2730 |
| 25 | 🇰🇷 KR | 2595 |
| 26 | 🇭🇷 HR | 2326 |
| 27 | 🇲🇦 MA | 2154 |
| 28 | 🇳🇱 NL | 1903 |
| 29 | 🇲🇪 ME | 1849 |
| 30 | 🇮🇩 ID | 1781 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4513 |
| 2 | Denver International Airport |  | US | 3508 |
| 3 | Tokyo International Airport |  | JP | 2643 |
| 4 | Indira Gandhi International Airport |  | IN | 2597 |
| 5 | Guaymaral Airport |  | CO | 2561 |
| 6 | Harry Reid International Airport |  | US | 2394 |
| 7 | Zurich Airport |  | CH | 2223 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2212 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2200 |
| 10 | La Aurora Airport |  | GT | 2076 |
| 11 | El Dorado International Airport |  | CO | 1997 |
| 12 | Chicago O'Hare International Airport |  | US | 1979 |
| 13 | Salt Lake City International Airport |  | US | 1898 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1889 |
| 15 | Congonhas Airport |  | BR | 1798 |
| 16 | Frankfurt am Main International Airport |  | DE | 1741 |
| 17 | Madrid Barajas International Airport |  | ES | 1667 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1617 |
| 19 | Capua Airport |  | IT | 1617 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1605 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1572 |
| 22 | Macau International Airport |  | MO | 1555 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1501 |
| 24 | Malpensa International Airport |  | IT | 1491 |
| 25 | Charles de Gaulle International Airport |  | FR | 1473 |
| 26 | Charlotte/Douglas International Airport |  | US | 1442 |
| 27 | Kuala Lumpur International Airport |  | MY | 1362 |
| 28 | Ninoy Aquino International Airport |  | PH | 1356 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1319 |
| 30 | Bengaluru International Airport |  | IN | 1306 |
| 31 | Barcelona International Airport |  | ES | 1305 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1288 |
| 33 | Seattle-Tacoma International Airport |  | US | 1276 |
| 34 | Viracopos International Airport |  | BR | 1253 |
| 35 | Calgary International Airport |  | CA | 1216 |
| 36 | Oslo Gardermoen Airport |  | NO | 1182 |
| 37 | Vitoria/Foronda Airport |  | ES | 1176 |
| 38 | Reno/Tahoe International Airport |  | US | 1161 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1152 |
| 40 | Don Mueang International Airport |  | TH | 1142 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1047 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 765 | 21m | 244 km | 3,221.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 528 | 1h 7m | 770 km | 7,014.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 498 | 24m | 225 km | 1,932.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 483 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 458 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 353 | 27m | 275 km | 1,672.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 349 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 314 | 1h 49m | 1,423 km | 7,706.1 t |
| 10 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 312 | 44m | 241 km | 1,296.0 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 281 | 21m | 250 km | 1,213.8 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 267 | 1h 38m | 1,156 km | 5,326.5 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 266 | 19m | 99 km | 455.6 t |
| 19 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 261 | 27m | 215 km | 966.6 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 254 | 1h 14m | 961 km | 4,210.2 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 250 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 248 | 31m | 369 km | 1,578.6 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 244 | 19m | 144 km | 606.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 243 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 231 | 1h 49m | 1,304 km | 5,196.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 30 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 223 | 44m | 555 km | 2,135.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| MVK69 | MVK | Mankato Regional Airport (KMKT) | Rochester International Airport (KRST) | 2026-08-19 02:32 UTC | 2026-08-19 03:19 UTC | 46m |
| IYQ1 | IYQ | Seoul Air Base (RKSM) | G 418 Airport (RK33) | 2026-08-19 02:39 UTC | 2026-08-19 03:15 UTC | 35m |
| PGT1801 | PGT | Queen Alia International Airport (OJAI) | OS70 (OS70) | 2026-08-19 02:42 UTC | 2026-08-19 03:08 UTC | 25m |
| CBC511 | CBC | Mc Clellan Airfield (KMCC) | Sacramento Mather Airport (KMHR) | 2026-08-19 02:36 UTC | 2026-08-19 03:03 UTC | 26m |
| UNA | UNA | Sydney Bankstown Airport (YSBK) | Bathurst Airport (YBTH) | 2026-08-19 02:30 UTC | 2026-08-19 03:02 UTC | 31m |
| IYQ2 | IYQ | Seoul Air Base (RKSM) | G 418 Airport (RK33) | 2026-08-19 02:41 UTC | 2026-08-19 03:01 UTC | 19m |
| LBQ791 | LBQ | Alexander Salamon Airport (KAMT) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-19 02:40 UTC | 2026-08-19 02:53 UTC | 13m |
| N3248D |  | Merrill Field (PAMR) | Ted Stevens Anchorage International Airport (PANC) | 2026-08-19 02:02 UTC | 2026-08-19 02:52 UTC | 49m |
| ZKPDZ | ZKP | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-08-19 02:34 UTC | 2026-08-19 02:47 UTC | 13m |
| N814SS |  | Drift River Airport (3AK5) | Kenai Municipal Airport (PAEN) | 2026-08-19 02:30 UTC | 2026-08-19 02:45 UTC | 14m |
| N720LE |  | Sydney Kingsford Smith International Airport (YSSY) | Adelaide International Airport (YPAD) | 2026-08-19 00:58 UTC | 2026-08-19 02:41 UTC | 1h 43m |
| GJS3379 | GJS | Chicago O'Hare International Airport (KORD) | Antrim County Airport (KACB) | 2026-08-19 01:54 UTC | 2026-08-19 02:34 UTC | 40m |
| N570FG |  | Trenton Mercer Airport (KTTN) | Northeast Philadelphia Airport (KPNE) | 2026-08-19 01:35 UTC | 2026-08-19 02:31 UTC | 56m |
| N6515G |  | Tacoma Narrows Airport (KTIW) | William R Fairchild International Airport (KCLM) | 2026-08-19 01:36 UTC | 2026-08-19 02:31 UTC | 55m |
| N123ED |  | Ranchaero Airport (CL56) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-19 02:00 UTC | 2026-08-19 02:27 UTC | 27m |
| AVR4864 | AVR | El Dorado International Airport (SKBO) | Alfonso Lopez Pumarejo Airport (SKVP) | 2026-08-19 01:23 UTC | 2026-08-19 02:24 UTC | 1h 0m |
| AIQ3201 | AIQ | Don Mueang International Airport (VTBD) | VLXL (VLXL) | 2026-08-19 01:22 UTC | 2026-08-19 02:20 UTC | 58m |
| QLK322D | QLK | Brisbane International Airport (YBBN) | Childers Airport (YCDS) | 2026-08-19 01:50 UTC | 2026-08-19 02:19 UTC | 28m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-19 02:11 UTC | 2026-08-19 02:16 UTC | 4m |
| QLK223D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Tumut Airport (YTMU) | 2026-08-19 01:35 UTC | 2026-08-19 02:12 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
