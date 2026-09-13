# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_19:28:59_UTC-green)

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

**Latest saved flight:** 2026-09-13 19:28:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-13 19:28:59 UTC

- **257,665** saved flights
- **76,676** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **257,665** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,117,617.3 tonnes** estimated CO2 emissions
- **180,731,439 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10243 |
| 2 | SkyWest Airlines | 8971 |
| 3 | EJA | 4984 |
| 4 | IndiGo | 4326 |
| 5 | American Airlines | 4069 |
| 6 | Southwest Airlines | 3789 |
| 7 | Delta Air Lines | 3223 |
| 8 | ENY | 3052 |
| 9 | LATAM Airlines | 2475 |
| 10 | AZU | 2407 |
| 11 | Vueling | 2181 |
| 12 | WIF | 2069 |
| 13 | Lufthansa | 2016 |
| 14 | LXJ | 2014 |
| 15 | easyJet | 1760 |
| 16 | Swiss International | 1723 |
| 17 | QLK | 1660 |
| 18 | AXM | 1646 |
| 19 | EJU | 1638 |
| 20 | United Airlines | 1595 |
| 21 | Alaska Airlines | 1528 |
| 22 | All Nippon Airways | 1497 |
| 23 | WMT | 1456 |
| 24 | GLO | 1436 |
| 25 | PGT | 1431 |
| 26 | Air France | 1409 |
| 27 | VIV | 1409 |
| 28 | Wizz Air | 1402 |
| 29 | JetBlue | 1248 |
| 30 | AEE | 1247 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 213832 |
| 2 | 🇪🇸 ES | 16360 |
| 3 | 🇧🇷 BR | 15035 |
| 4 | 🇦🇺 AU | 14661 |
| 5 | 🇨🇦 CA | 14345 |
| 6 | 🇮🇹 IT | 14066 |
| 7 | 🇮🇳 IN | 13578 |
| 8 | 🇩🇪 DE | 12558 |
| 9 | 🇬🇧 GB | 12018 |
| 10 | 🇨🇴 CO | 11552 |
| 11 | 🇫🇷 FR | 10363 |
| 12 | 🇯🇵 JP | 10042 |
| 13 | 🇹🇷 TR | 7761 |
| 14 | 🇬🇷 GR | 7513 |
| 15 | 🇲🇽 MX | 7105 |
| 16 | 🇨🇭 CH | 6918 |
| 17 | 🇳🇴 NO | 6373 |
| 18 | 🇹🇭 TH | 4640 |
| 19 | 🇲🇾 MY | 4425 |
| 20 | 🇿🇦 ZA | 4388 |
| 21 | 🇵🇱 PL | 4273 |
| 22 | 🇳🇿 NZ | 3556 |
| 23 | 🇵🇭 PH | 3466 |
| 24 | 🇬🇹 GT | 3261 |
| 25 | 🇭🇷 HR | 2962 |
| 26 | 🇰🇷 KR | 2948 |
| 27 | 🇲🇦 MA | 2590 |
| 28 | 🇲🇪 ME | 2427 |
| 29 | 🇳🇱 NL | 2319 |
| 30 | 🇮🇩 ID | 2185 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5277 |
| 2 | Denver International Airport |  | US | 4166 |
| 3 | Indira Gandhi International Airport |  | IN | 3116 |
| 4 | Tokyo International Airport |  | JP | 2997 |
| 5 | Guaymaral Airport |  | CO | 2764 |
| 6 | Harry Reid International Airport |  | US | 2729 |
| 7 | Zurich Airport |  | CH | 2701 |
| 8 | El Dorado International Airport |  | CO | 2686 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2599 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2518 |
| 11 | La Aurora Airport |  | GT | 2477 |
| 12 | Salt Lake City International Airport |  | US | 2270 |
| 13 | Chicago O'Hare International Airport |  | US | 2243 |
| 14 | Congonhas Airport |  | BR | 2205 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2103 |
| 16 | Capua Airport |  | IT | 2023 |
| 17 | Madrid Barajas International Airport |  | ES | 2010 |
| 18 | Frankfurt am Main International Airport |  | DE | 1988 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1930 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1859 |
| 21 | Malpensa International Airport |  | IT | 1856 |
| 22 | Charles de Gaulle International Airport |  | FR | 1818 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1809 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1783 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1748 |
| 26 | Macau International Airport |  | MO | 1708 |
| 27 | Ninoy Aquino International Airport |  | PH | 1697 |
| 28 | Barcelona International Airport |  | ES | 1619 |
| 29 | Charlotte/Douglas International Airport |  | US | 1611 |
| 30 | Kuala Lumpur International Airport |  | MY | 1592 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1578 |
| 32 | Viracopos International Airport |  | BR | 1547 |
| 33 | Seattle-Tacoma International Airport |  | US | 1510 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1497 |
| 35 | Don Mueang International Airport |  | TH | 1483 |
| 36 | Calgary International Airport |  | CA | 1474 |
| 37 | Bengaluru International Airport |  | IN | 1463 |
| 38 | Oslo Gardermoen Airport |  | NO | 1454 |
| 39 | Vancouver International Airport |  | CA | 1447 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1389 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 960 | 21m | 244 km | 4,042.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 694 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 644 | 1h 6m | 770 km | 8,555.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 644 | 24m | 225 km | 2,498.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 576 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 418 | 27m | 275 km | 1,980.7 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 418 | 44m | 555 km | 4,002.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 411 | 1h 50m | 1,423 km | 10,086.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 389 | 44m | 241 km | 1,615.8 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 361 | 24m | 218 km | 1,360.0 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 356 | 21m | 250 km | 1,537.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 343 | 23m | 55 km | 326.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 325 | 1h 6m | 706 km | 3,956.9 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 320 | 19m | 99 km | 548.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 319 | 26m | 215 km | 1,181.4 t |
| 19 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 311 | 12m | - | - |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 308 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 299 | 19m | 144 km | 743.7 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 297 | 1h 14m | 961 km | 4,922.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 275 | 1h 50m | 1,304 km | 6,186.8 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 273 | 42m | 535 km | 2,521.3 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 270 | 28m | 152 km | 705.6 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JOLLY93 | JOL | Moffett Federal Airfield (KNUQ) | Moffett Federal Airfield (KNUQ) | 2026-09-13 18:16 UTC | 2026-09-13 19:28 UTC | 1h 12m |
| N223LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | 2026-09-13 17:50 UTC | 2026-09-13 19:26 UTC | 1h 36m |
| N248PA |  | Wheeler Army Air Field (PHHI) | Kawaihapai Airfield (PHDH) | 2026-09-13 19:11 UTC | 2026-09-13 19:23 UTC | 11m |
| EJA124 | EJA | Dallas Love Field (KDAL) | Austin-Bergstrom International Airport (KAUS) | 2026-09-13 18:50 UTC | 2026-09-13 19:21 UTC | 31m |
| SCU11 | SCU | 2OL2 (2OL2) | Haskell Airport (K2K9) | 2026-09-13 18:37 UTC | 2026-09-13 19:21 UTC | 44m |
| N938GC |  | St Simons Island Airport (KSSI) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-09-13 18:30 UTC | 2026-09-13 19:15 UTC | 44m |
| PGC64A | PGC | La Mole Airport (LFTZ) | Brussels Airport (EBBR) | 2026-09-13 17:29 UTC | 2026-09-13 19:14 UTC | 1h 44m |
| THA313 | Thai Airways | Suvarnabhumi Airport (VTBS) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-09-13 17:05 UTC | 2026-09-13 19:12 UTC | 2h 7m |
| UAE9862 | Emirates | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-09-13 11:54 UTC | 2026-09-13 19:11 UTC | 7h 17m |
| STW081 | STW | Istanbul Airport (LTFM) | Smolensk North Airport (XUBS) | 2026-09-13 17:03 UTC | 2026-09-13 19:11 UTC | 2h 7m |
| N246SF |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-09-13 18:09 UTC | 2026-09-13 19:07 UTC | 58m |
| N8467B |  | Ohio University Airport (KUNI) | Ohio University Airport (KUNI) | 2026-09-13 19:04 UTC | 2026-09-13 19:06 UTC | 1m |
| MSR794 | EgyptAir | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | HE42 (HE42) | 2026-09-13 16:37 UTC | 2026-09-13 19:05 UTC | 2h 28m |
| C6043 |  | Longmere Lake Air Strip (AK07) | Homer Airport (PAHO) | 2026-09-13 18:49 UTC | 2026-09-13 19:04 UTC | 15m |
| KING54 | KIN | Moffett Federal Airfield (KNUQ) | Moffett Federal Airfield (KNUQ) | 2026-09-13 18:21 UTC | 2026-09-13 18:59 UTC | 37m |
| N450PD |  | Mc Clellan-Palomar Airport (KCRQ) | Fairbanks Airfield (1ID7) | 2026-09-13 17:31 UTC | 2026-09-13 18:57 UTC | 1h 25m |
| IGO1186 | IndiGo | Chennai International Airport (VOMM) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-13 14:35 UTC | 2026-09-13 18:57 UTC | 4h 21m |
| USC101 | USC | Charlotte/Douglas International Airport (KCLT) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-09-13 18:17 UTC | 2026-09-13 18:56 UTC | 39m |
| N768LP |  | Santa Barbara Municipal Airport (KSBA) | Oakland San Francisco Bay Airport (KOAK) | 2026-09-13 18:08 UTC | 2026-09-13 18:56 UTC | 47m |
| MSR776 | EgyptAir | Dublin Airport (EIDW) | HE42 (HE42) | 2026-09-13 14:16 UTC | 2026-09-13 18:53 UTC | 4h 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
