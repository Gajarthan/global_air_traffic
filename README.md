# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--03_22:12:26_UTC-green)

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

**Latest saved flight:** 2026-09-03 22:12:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-03 22:12:26 UTC

- **246,467** saved flights
- **74,393** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **246,467** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,965,788.5 tonnes** estimated CO2 emissions
- **171,929,766 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9876 |
| 2 | SkyWest Airlines | 8619 |
| 3 | EJA | 4755 |
| 4 | IndiGo | 4122 |
| 5 | American Airlines | 3959 |
| 6 | Southwest Airlines | 3679 |
| 7 | Delta Air Lines | 3130 |
| 8 | ENY | 2948 |
| 9 | LATAM Airlines | 2371 |
| 10 | AZU | 2290 |
| 11 | Vueling | 2110 |
| 12 | WIF | 1975 |
| 13 | Lufthansa | 1968 |
| 14 | LXJ | 1911 |
| 15 | easyJet | 1710 |
| 16 | Swiss International | 1658 |
| 17 | AXM | 1616 |
| 18 | EJU | 1588 |
| 19 | QLK | 1578 |
| 20 | United Airlines | 1551 |
| 21 | Alaska Airlines | 1470 |
| 22 | All Nippon Airways | 1448 |
| 23 | WMT | 1387 |
| 24 | GLO | 1376 |
| 25 | VIV | 1352 |
| 26 | PGT | 1350 |
| 27 | Air France | 1347 |
| 28 | Wizz Air | 1334 |
| 29 | AEE | 1214 |
| 30 | JetBlue | 1214 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 204332 |
| 2 | 🇪🇸 ES | 15806 |
| 3 | 🇧🇷 BR | 14384 |
| 4 | 🇦🇺 AU | 14001 |
| 5 | 🇨🇦 CA | 13715 |
| 6 | 🇮🇹 IT | 13500 |
| 7 | 🇮🇳 IN | 12854 |
| 8 | 🇩🇪 DE | 12139 |
| 9 | 🇬🇧 GB | 11599 |
| 10 | 🇨🇴 CO | 10728 |
| 11 | 🇫🇷 FR | 9945 |
| 12 | 🇯🇵 JP | 9773 |
| 13 | 🇹🇷 TR | 7316 |
| 14 | 🇬🇷 GR | 7264 |
| 15 | 🇲🇽 MX | 6805 |
| 16 | 🇨🇭 CH | 6630 |
| 17 | 🇳🇴 NO | 6122 |
| 18 | 🇹🇭 TH | 4446 |
| 19 | 🇲🇾 MY | 4331 |
| 20 | 🇿🇦 ZA | 4275 |
| 21 | 🇵🇱 PL | 4131 |
| 22 | 🇳🇿 NZ | 3370 |
| 23 | 🇵🇭 PH | 3364 |
| 24 | 🇬🇹 GT | 3086 |
| 25 | 🇰🇷 KR | 2878 |
| 26 | 🇭🇷 HR | 2833 |
| 27 | 🇲🇦 MA | 2492 |
| 28 | 🇲🇪 ME | 2302 |
| 29 | 🇳🇱 NL | 2228 |
| 30 | 🇮🇩 ID | 2142 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5074 |
| 2 | Denver International Airport |  | US | 3984 |
| 3 | Indira Gandhi International Airport |  | IN | 3002 |
| 4 | Tokyo International Airport |  | JP | 2914 |
| 5 | Guaymaral Airport |  | CO | 2721 |
| 6 | Harry Reid International Airport |  | US | 2625 |
| 7 | Zurich Airport |  | CH | 2585 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2510 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2454 |
| 10 | El Dorado International Airport |  | CO | 2450 |
| 11 | La Aurora Airport |  | GT | 2348 |
| 12 | Salt Lake City International Airport |  | US | 2185 |
| 13 | Chicago O'Hare International Airport |  | US | 2166 |
| 14 | Congonhas Airport |  | BR | 2112 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2033 |
| 16 | Capua Airport |  | IT | 1940 |
| 17 | Frankfurt am Main International Airport |  | DE | 1938 |
| 18 | Madrid Barajas International Airport |  | ES | 1930 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1852 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1806 |
| 21 | Malpensa International Airport |  | IT | 1765 |
| 22 | Charles de Gaulle International Airport |  | FR | 1733 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1725 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1725 |
| 25 | Ninoy Aquino International Airport |  | PH | 1637 |
| 26 | Macau International Airport |  | MO | 1632 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1608 |
| 28 | Charlotte/Douglas International Airport |  | US | 1568 |
| 29 | Barcelona International Airport |  | ES | 1563 |
| 30 | Kuala Lumpur International Airport |  | MY | 1560 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1504 |
| 32 | Viracopos International Airport |  | BR | 1464 |
| 33 | Seattle-Tacoma International Airport |  | US | 1447 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1433 |
| 35 | Don Mueang International Airport |  | TH | 1428 |
| 36 | Bengaluru International Airport |  | IN | 1424 |
| 37 | Calgary International Airport |  | CA | 1419 |
| 38 | Oslo Gardermoen Airport |  | NO | 1389 |
| 39 | Vancouver International Airport |  | CA | 1376 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1343 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 912 | 21m | 244 km | 3,840.2 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 646 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 625 | 24m | 225 km | 2,424.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 618 | 1h 6m | 770 km | 8,209.7 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 553 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 406 | 27m | 275 km | 1,923.9 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 390 | 1h 50m | 1,423 km | 9,571.2 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 379 | 44m | 555 km | 3,629.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 364 | 44m | 241 km | 1,512.0 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 350 | 21m | 250 km | 1,511.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 343 | 24m | 218 km | 1,292.2 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 331 | 1h 39m | 1,156 km | 6,603.3 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 329 | 22m | 55 km | 312.7 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 322 | 1h 6m | 706 km | 3,920.4 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 305 | 26m | 215 km | 1,129.6 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 291 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 286 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 285 | 1h 14m | 961 km | 4,724.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 281 | 19m | 144 km | 699.0 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 267 | 1h 50m | 1,304 km | 6,006.8 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 252 | 28m | 152 km | 658.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| YGW | YGW | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-09-03 21:41 UTC | 2026-09-03 22:12 UTC | 31m |
| N5254K |  | Fort Lauderdale Executive Airport (KFXE) | Palm Beach County Park Airport (KLNA) | 2026-09-03 21:32 UTC | 2026-09-03 22:10 UTC | 38m |
| AFR570 | Air France | Charles de Gaulle International Airport (LFPG) | HE42 (HE42) | 2026-09-03 18:36 UTC | 2026-09-03 22:09 UTC | 3h 33m |
| CAP4109 | CAP | Lovell Field (KCHA) | Possum Bottom Airport (TN89) | 2026-09-03 21:54 UTC | 2026-09-03 22:05 UTC | 11m |
|  |  | Bentonville Municipal/Louise M Thaden Field (KVBT) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-09-03 20:31 UTC | 2026-09-03 22:02 UTC | 1h 30m |
| N887DC |  | Modesto City-County-Harry Sham Field (KMOD) | Oakland San Francisco Bay Airport (KOAK) | 2026-09-03 21:41 UTC | 2026-09-03 22:00 UTC | 19m |
| RFS729 | RFS | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-09-03 21:37 UTC | 2026-09-03 21:59 UTC | 22m |
| CHH491 | CHH | Beijing Capital International Airport (ZBAA) | Sharypovo Airport (UNKO) | 2026-09-03 18:46 UTC | 2026-09-03 21:57 UTC | 3h 11m |
| N782AZ |  | Tracy Municipal Airport (KTCY) | Tracy Municipal Airport (KTCY) | 2026-09-03 21:55 UTC | 2026-09-03 21:57 UTC | 1m |
| N987MT |  | Zamperini Field (KTOA) | Mc Clellan-Palomar Airport (KCRQ) | 2026-09-03 21:11 UTC | 2026-09-03 21:56 UTC | 45m |
| EQO | EQO | Toowoomba Wellcamp Airport (YBWW) | Sunshine Coast Airport (YBMC) | 2026-09-03 21:13 UTC | 2026-09-03 21:55 UTC | 41m |
| YGN | YGN | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-09-03 21:15 UTC | 2026-09-03 21:52 UTC | 37m |
| LXJ410 | LXJ | Teterboro Airport (KTEB) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-09-03 20:30 UTC | 2026-09-03 21:51 UTC | 1h 21m |
| MAS115 | Malaysia Airlines | Tribhuvan International Airport (VNKT) | Jendarata Airport (WMAJ) | 2026-09-03 17:51 UTC | 2026-09-03 21:51 UTC | 3h 59m |
| N12JS |  | Harry Reid International Airport (KLAS) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-09-03 20:45 UTC | 2026-09-03 21:49 UTC | 1h 3m |
| N18ZD |  | Greeley-Weld County Airport (KGXY) | Burley Municipal Airport (KBYI) | 2026-09-03 20:37 UTC | 2026-09-03 21:48 UTC | 1h 11m |
| N2074A |  | Billy Joe Airport (37CA) | Hemet-Ryan Airport (KHMT) | 2026-09-03 21:08 UTC | 2026-09-03 21:48 UTC | 39m |
| N260FL |  | Trenton Mercer Airport (KTTN) | Ocean County Airport (KMJX) | 2026-09-03 20:58 UTC | 2026-09-03 21:44 UTC | 45m |
| ARCAS31 | ARC | Danaher Airport (7TX0) | Arledge Field (KF56) | 2026-09-03 21:28 UTC | 2026-09-03 21:39 UTC | 11m |
| AIC2386 | Air India | Indira Gandhi International Airport (VIDP) | Ulu Bernam Airport (WMBF) | 2026-09-03 16:44 UTC | 2026-09-03 21:38 UTC | 4h 53m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
