# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_23:40:05_UTC-green)

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

**Latest saved flight:** 2026-08-21 23:40:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 23:40:05 UTC

- **224,221** saved flights
- **69,960** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **224,221** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,700,848.0 tonnes** estimated CO2 emissions
- **156,570,897 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8987 |
| 2 | SkyWest Airlines | 7985 |
| 3 | EJA | 4351 |
| 4 | IndiGo | 3782 |
| 5 | American Airlines | 3701 |
| 6 | Southwest Airlines | 3517 |
| 7 | Delta Air Lines | 2876 |
| 8 | ENY | 2759 |
| 9 | LATAM Airlines | 2138 |
| 10 | AZU | 2071 |
| 11 | Vueling | 1890 |
| 12 | Lufthansa | 1842 |
| 13 | WIF | 1787 |
| 14 | LXJ | 1773 |
| 15 | easyJet | 1551 |
| 16 | Swiss International | 1491 |
| 17 | AXM | 1467 |
| 18 | United Airlines | 1413 |
| 19 | QLK | 1406 |
| 20 | EJU | 1405 |
| 21 | Alaska Airlines | 1360 |
| 22 | All Nippon Airways | 1334 |
| 23 | GLO | 1243 |
| 24 | PGT | 1229 |
| 25 | VIV | 1224 |
| 26 | Air France | 1214 |
| 27 | WMT | 1194 |
| 28 | Wizz Air | 1154 |
| 29 | JetBlue | 1126 |
| 30 | AEE | 1117 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 188389 |
| 2 | 🇪🇸 ES | 14363 |
| 3 | 🇧🇷 BR | 13042 |
| 4 | 🇦🇺 AU | 12665 |
| 5 | 🇨🇦 CA | 12432 |
| 6 | 🇮🇹 IT | 11976 |
| 7 | 🇮🇳 IN | 11795 |
| 8 | 🇩🇪 DE | 11028 |
| 9 | 🇬🇧 GB | 10515 |
| 10 | 🇨🇴 CO | 9247 |
| 11 | 🇯🇵 JP | 9060 |
| 12 | 🇫🇷 FR | 8933 |
| 13 | 🇹🇷 TR | 6537 |
| 14 | 🇬🇷 GR | 6531 |
| 15 | 🇲🇽 MX | 6237 |
| 16 | 🇨🇭 CH | 5889 |
| 17 | 🇳🇴 NO | 5560 |
| 18 | 🇲🇾 MY | 3887 |
| 19 | 🇿🇦 ZA | 3861 |
| 20 | 🇹🇭 TH | 3774 |
| 21 | 🇵🇱 PL | 3717 |
| 22 | 🇳🇿 NZ | 3110 |
| 23 | 🇵🇭 PH | 3034 |
| 24 | 🇬🇹 GT | 2846 |
| 25 | 🇰🇷 KR | 2659 |
| 26 | 🇭🇷 HR | 2503 |
| 27 | 🇲🇦 MA | 2256 |
| 28 | 🇳🇱 NL | 1992 |
| 29 | 🇲🇪 ME | 1989 |
| 30 | 🇮🇩 ID | 1909 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4705 |
| 2 | Denver International Airport |  | US | 3663 |
| 3 | Tokyo International Airport |  | JP | 2717 |
| 4 | Indira Gandhi International Airport |  | IN | 2713 |
| 5 | Guaymaral Airport |  | CO | 2628 |
| 6 | Harry Reid International Airport |  | US | 2462 |
| 7 | Zurich Airport |  | CH | 2321 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2301 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2268 |
| 10 | La Aurora Airport |  | GT | 2170 |
| 11 | El Dorado International Airport |  | CO | 2080 |
| 12 | Chicago O'Hare International Airport |  | US | 2048 |
| 13 | Salt Lake City International Airport |  | US | 1967 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1924 |
| 15 | Congonhas Airport |  | BR | 1908 |
| 16 | Frankfurt am Main International Airport |  | DE | 1812 |
| 17 | Madrid Barajas International Airport |  | ES | 1754 |
| 18 | Capua Airport |  | IT | 1717 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1674 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1666 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1632 |
| 22 | Macau International Airport |  | MO | 1589 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1572 |
| 24 | Malpensa International Airport |  | IT | 1570 |
| 25 | Charles de Gaulle International Airport |  | FR | 1547 |
| 26 | Charlotte/Douglas International Airport |  | US | 1482 |
| 27 | Ninoy Aquino International Airport |  | PH | 1446 |
| 28 | Kuala Lumpur International Airport |  | MY | 1420 |
| 29 | Barcelona International Airport |  | ES | 1385 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1363 |
| 31 | Bengaluru International Airport |  | IN | 1334 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1330 |
| 33 | Seattle-Tacoma International Airport |  | US | 1324 |
| 34 | Viracopos International Airport |  | BR | 1321 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1303 |
| 36 | Calgary International Airport |  | CA | 1275 |
| 37 | Oslo Gardermoen Airport |  | NO | 1251 |
| 38 | Vitoria/Foronda Airport |  | ES | 1240 |
| 39 | Don Mueang International Airport |  | TH | 1239 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1208 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1072 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 806 | 21m | 244 km | 3,393.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 557 | 1h 7m | 770 km | 7,399.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 540 | 24m | 225 km | 2,094.9 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 527 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 510 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 377 | 27m | 275 km | 1,786.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 353 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 333 | 1h 50m | 1,423 km | 8,172.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 326 | 44m | 241 km | 1,354.1 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 299 | 21m | 250 km | 1,291.5 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 298 | 22m | 55 km | 283.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 283 | 1h 39m | 1,156 km | 5,645.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 279 | 24m | 218 km | 1,051.1 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 278 | 19m | 99 km | 476.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 275 | 27m | 215 km | 1,018.5 t |
| 20 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 274 | 44m | 555 km | 2,623.7 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 264 | 1h 14m | 961 km | 4,375.9 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 256 | 19m | 144 km | 636.8 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 255 | 12m | - | - |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 244 | 1h 50m | 1,304 km | 5,489.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 238 | 28m | 152 km | 622.0 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UAL2028 | United Airlines | Frederick W Smith International/Memphis Airport (KMEM) | Hoxie-Sheridan County Airport (K1F5) | 2026-08-21 21:49 UTC | 2026-08-21 23:40 UTC | 1h 50m |
| N181BL |  | Lancaster Airport (KLNS) | Lancaster Airport (KLNS) | 2026-08-21 23:14 UTC | 2026-08-21 23:27 UTC | 12m |
| UAL1494 | United Airlines | Richmond International Airport (KRIC) | Rans Airport (8KS4) | 2026-08-21 20:28 UTC | 2026-08-21 23:19 UTC | 2h 50m |
| ES800 |  | Castle Airport (KMER) | Sacramento Mather Airport (KMHR) | 2026-08-21 22:15 UTC | 2026-08-21 23:18 UTC | 1h 2m |
| N8085A |  | Mahlon Sweet Field (KEUG) | Aurora State Airport (KUAO) | 2026-08-21 22:34 UTC | 2026-08-21 23:17 UTC | 43m |
| XLF | XLF | Elderslie Airport (YEES) | Elderslie Airport (YEES) | 2026-08-21 23:01 UTC | 2026-08-21 23:14 UTC | 13m |
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-08-21 21:52 UTC | 2026-08-21 23:13 UTC | 1h 21m |
| ZKICU | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-08-21 23:11 UTC | 2026-08-21 23:13 UTC | 1m |
| DAL2431 | Delta Air Lines | Detroit Metro Wayne County Airport (KDTW) | Hoxie-Sheridan County Airport (K1F5) | 2026-08-21 20:38 UTC | 2026-08-21 23:12 UTC | 2h 34m |
| UAL2297 | United Airlines | General Edward Lawrence Logan International Airport (KBOS) | Kennedy Airport (7KS7) | 2026-08-21 19:19 UTC | 2026-08-21 23:11 UTC | 3h 51m |
| N13UA |  | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-08-21 22:51 UTC | 2026-08-21 23:10 UTC | 18m |
| N540MA |  | Lakefront Airport (KNEW) | Austin Field (TN66) | 2026-08-21 21:28 UTC | 2026-08-21 23:09 UTC | 1h 41m |
| QLK9D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-08-21 22:43 UTC | 2026-08-21 23:06 UTC | 23m |
| SWA2970 | Southwest Airlines | Oakland San Francisco Bay Airport (KOAK) | 5CO7 (5CO7) | 2026-08-21 21:11 UTC | 2026-08-21 23:02 UTC | 1h 50m |
| ASP869 | ASP | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Toronto Pearson International Airport (CYYZ) | 2026-08-21 22:08 UTC | 2026-08-21 23:01 UTC | 53m |
| SKW5312 | SkyWest Airlines | San Francisco International Airport (KSFO) | Palm Springs International Airport (KPSP) | 2026-08-21 22:02 UTC | 2026-08-21 23:00 UTC | 58m |
| VIV9035 | VIV | Cancun International Airport (MMUN) | General Lucio Blanco International Airport (MMRX) | 2026-08-21 19:23 UTC | 2026-08-21 22:59 UTC | 3h 36m |
| SCU21 | SCU | Cherokee Ranch Airport (OK25) | Haskell Airport (K2K9) | 2026-08-21 22:56 UTC | 2026-08-21 22:59 UTC | 2m |
| N694DA |  | Fort Morgan Municipal Airport (KFMM) | Fort Morgan Municipal Airport (KFMM) | 2026-08-21 22:47 UTC | 2026-08-21 22:56 UTC | 9m |
| SKW4262 | SkyWest Airlines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | The Sigurd Anderson Airport (K1D7) | 2026-08-21 22:22 UTC | 2026-08-21 22:56 UTC | 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
