# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--28_00:41:15_UTC-green)

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

**Latest saved flight:** 2026-08-28 00:41:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-28 00:41:15 UTC

- **240,113** saved flights
- **72,935** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **240,113** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,890,883.9 tonnes** estimated CO2 emissions
- **167,587,472 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9635 |
| 2 | SkyWest Airlines | 8432 |
| 3 | EJA | 4652 |
| 4 | IndiGo | 4044 |
| 5 | American Airlines | 3874 |
| 6 | Southwest Airlines | 3619 |
| 7 | Delta Air Lines | 3059 |
| 8 | ENY | 2903 |
| 9 | LATAM Airlines | 2302 |
| 10 | AZU | 2238 |
| 11 | Vueling | 2063 |
| 12 | Lufthansa | 1936 |
| 13 | WIF | 1903 |
| 14 | LXJ | 1862 |
| 15 | easyJet | 1669 |
| 16 | Swiss International | 1612 |
| 17 | AXM | 1593 |
| 18 | EJU | 1537 |
| 19 | QLK | 1536 |
| 20 | United Airlines | 1512 |
| 21 | Alaska Airlines | 1436 |
| 22 | All Nippon Airways | 1425 |
| 23 | WMT | 1352 |
| 24 | GLO | 1338 |
| 25 | VIV | 1319 |
| 26 | Air France | 1312 |
| 27 | PGT | 1306 |
| 28 | Wizz Air | 1284 |
| 29 | JetBlue | 1190 |
| 30 | AEE | 1189 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 199040 |
| 2 | 🇪🇸 ES | 15437 |
| 3 | 🇧🇷 BR | 14008 |
| 4 | 🇦🇺 AU | 13651 |
| 5 | 🇨🇦 CA | 13353 |
| 6 | 🇮🇹 IT | 13135 |
| 7 | 🇮🇳 IN | 12598 |
| 8 | 🇩🇪 DE | 11852 |
| 9 | 🇬🇧 GB | 11324 |
| 10 | 🇨🇴 CO | 10286 |
| 11 | 🇯🇵 JP | 9663 |
| 12 | 🇫🇷 FR | 9660 |
| 13 | 🇹🇷 TR | 7120 |
| 14 | 🇬🇷 GR | 7069 |
| 15 | 🇲🇽 MX | 6642 |
| 16 | 🇨🇭 CH | 6429 |
| 17 | 🇳🇴 NO | 5932 |
| 18 | 🇹🇭 TH | 4347 |
| 19 | 🇲🇾 MY | 4268 |
| 20 | 🇿🇦 ZA | 4207 |
| 21 | 🇵🇱 PL | 4000 |
| 22 | 🇳🇿 NZ | 3299 |
| 23 | 🇵🇭 PH | 3297 |
| 24 | 🇬🇹 GT | 3014 |
| 25 | 🇰🇷 KR | 2845 |
| 26 | 🇭🇷 HR | 2772 |
| 27 | 🇲🇦 MA | 2428 |
| 28 | 🇲🇪 ME | 2246 |
| 29 | 🇳🇱 NL | 2173 |
| 30 | 🇮🇩 ID | 2106 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4963 |
| 2 | Denver International Airport |  | US | 3877 |
| 3 | Indira Gandhi International Airport |  | IN | 2932 |
| 4 | Tokyo International Airport |  | JP | 2877 |
| 5 | Guaymaral Airport |  | CO | 2694 |
| 6 | Harry Reid International Airport |  | US | 2551 |
| 7 | Zurich Airport |  | CH | 2512 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2459 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2396 |
| 10 | El Dorado International Airport |  | CO | 2320 |
| 11 | La Aurora Airport |  | GT | 2300 |
| 12 | Chicago O'Hare International Airport |  | US | 2142 |
| 13 | Salt Lake City International Airport |  | US | 2117 |
| 14 | Congonhas Airport |  | BR | 2046 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1997 |
| 16 | Frankfurt am Main International Airport |  | DE | 1900 |
| 17 | Capua Airport |  | IT | 1895 |
| 18 | Madrid Barajas International Airport |  | ES | 1890 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1807 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1767 |
| 21 | Malpensa International Airport |  | IT | 1721 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1696 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1686 |
| 24 | Charles de Gaulle International Airport |  | FR | 1678 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1600 |
| 27 | Kuala Lumpur International Airport |  | MY | 1543 |
| 28 | Charlotte/Douglas International Airport |  | US | 1538 |
| 29 | Enrique Olaya Herrera Airport |  | CO | 1526 |
| 30 | Barcelona International Airport |  | ES | 1526 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1454 |
| 32 | Viracopos International Airport |  | BR | 1434 |
| 33 | Don Mueang International Airport |  | TH | 1403 |
| 34 | Bengaluru International Airport |  | IN | 1402 |
| 35 | Seattle-Tacoma International Airport |  | US | 1399 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1397 |
| 37 | Calgary International Airport |  | CA | 1380 |
| 38 | Oslo Gardermoen Airport |  | NO | 1346 |
| 39 | Vancouver International Airport |  | CA | 1320 |
| 40 | O. R. Tambo International Airport |  | ZA | 1312 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1091 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 884 | 21m | 244 km | 3,722.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 618 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 610 | 24m | 225 km | 2,366.5 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 608 | 1h 6m | 770 km | 8,076.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 543 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 397 | 27m | 275 km | 1,881.2 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 377 | 1h 50m | 1,423 km | 9,252.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 365 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 363 | 44m | 555 km | 3,475.9 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 348 | 44m | 241 km | 1,445.5 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 345 | 21m | 250 km | 1,490.2 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 326 | 24m | 218 km | 1,228.2 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 320 | 22m | 55 km | 304.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 319 | 1h 40m | 1,156 km | 6,363.9 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 298 | 19m | 99 km | 510.5 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 293 | 27m | 215 km | 1,085.1 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 277 | 13m | - | - |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 277 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 273 | 1h 14m | 961 km | 4,525.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 271 | 19m | 144 km | 674.1 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 263 | 15m | 154 km | 696.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 258 | 1h 50m | 1,304 km | 5,804.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 248 | 28m | 152 km | 648.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N5276P |  | Livermore Municipal Airport (KLVK) | Livermore Municipal Airport (KLVK) | 2026-08-28 00:11 UTC | 2026-08-28 00:41 UTC | 29m |
| N714F |  | Dupage Airport (KDPA) | Logan-Cache Airport (KLGU) | 2026-08-27 21:54 UTC | 2026-08-28 00:40 UTC | 2h 45m |
| N149TH |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-27 23:17 UTC | 2026-08-28 00:38 UTC | 1h 20m |
| N987MT |  | Zamperini Field (KTOA) | Zamperini Field (KTOA) | 2026-08-28 00:09 UTC | 2026-08-28 00:31 UTC | 22m |
| CUTLS53 | CUT | Catalina Airport (KAVX) | Bob Maxwell Memorial Airfield (KOKB) | 2026-08-28 00:10 UTC | 2026-08-28 00:30 UTC | 20m |
| N15EW |  | Mckinney Ntl Airport (KTKI) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-27 22:47 UTC | 2026-08-28 00:26 UTC | 1h 38m |
| N79204 |  | Ennis Municipal Airport (KF41) | C David Campbell Field-Corsicana Municipal Airport (KCRS) | 2026-08-27 23:48 UTC | 2026-08-28 00:24 UTC | 36m |
| N900AA |  | Sacramento Mather Airport (KMHR) | San Carlos Airport (KSQL) | 2026-08-27 23:11 UTC | 2026-08-28 00:21 UTC | 1h 10m |
| N12ED |  | Mankato Regional Airport (KMKT) | Mankato Regional Airport (KMKT) | 2026-08-27 23:59 UTC | 2026-08-28 00:17 UTC | 18m |
| N14AK |  | Kodiak Airport (PADQ) | Kodiak Municipal Airport (PAKD) | 2026-08-28 00:03 UTC | 2026-08-28 00:12 UTC | 9m |
| N527FB |  | Hunter Army Air Field (KSVN) | Hunter Army Air Field (KSVN) | 2026-08-27 23:53 UTC | 2026-08-28 00:07 UTC | 13m |
| N500EH |  | Soldotna Airport (PASX) | Mcgahan Industrial Airpark (AK73) | 2026-08-27 23:44 UTC | 2026-08-28 00:06 UTC | 22m |
| OKC711 | OKC | Wiley Post Airport (KPWA) | Miller-Herrold Airport (28MI) | 2026-08-27 22:11 UTC | 2026-08-28 00:05 UTC | 1h 54m |
| N680ND |  | Brookings Regional Airport (KBKX) | Brookings Regional Airport (KBKX) | 2026-08-27 23:13 UTC | 2026-08-28 00:04 UTC | 50m |
| N484FA |  | Skypark Airport (KBTF) | Morgan County Airport (K42U) | 2026-08-27 23:45 UTC | 2026-08-28 00:02 UTC | 17m |
| N31MK |  | K00V (K00V) | High Plains Airport Airport (CD15) | 2026-08-27 23:47 UTC | 2026-08-28 00:00 UTC | 12m |
| N5276P |  | Palo Alto Airport (KPAO) | Livermore Municipal Airport (KLVK) | 2026-08-27 23:41 UTC | 2026-08-27 23:59 UTC | 18m |
| PUJ | PUJ | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-08-27 23:35 UTC | 2026-08-27 23:59 UTC | 24m |
| N408NG |  | New Century Aircenter Airport (KIXD) | 3TE6 (3TE6) | 2026-08-27 22:28 UTC | 2026-08-27 23:58 UTC | 1h 29m |
| N72MZ |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-08-27 23:36 UTC | 2026-08-27 23:57 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
