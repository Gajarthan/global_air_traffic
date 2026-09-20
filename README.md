# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_20:34:03_UTC-green)

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

**Latest saved flight:** 2026-09-20 20:34:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-20 20:34:03 UTC

- **264,881** saved flights
- **78,113** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **264,881** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,209,988.2 tonnes** estimated CO2 emissions
- **186,086,274 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10490 |
| 2 | SkyWest Airlines | 9206 |
| 3 | EJA | 5147 |
| 4 | IndiGo | 4449 |
| 5 | American Airlines | 4138 |
| 6 | Southwest Airlines | 3895 |
| 7 | Delta Air Lines | 3300 |
| 8 | ENY | 3120 |
| 9 | LATAM Airlines | 2554 |
| 10 | AZU | 2492 |
| 11 | Vueling | 2225 |
| 12 | WIF | 2142 |
| 13 | LXJ | 2080 |
| 14 | Lufthansa | 2037 |
| 15 | easyJet | 1785 |
| 16 | Swiss International | 1745 |
| 17 | QLK | 1708 |
| 18 | EJU | 1672 |
| 19 | AXM | 1662 |
| 20 | United Airlines | 1624 |
| 21 | Alaska Airlines | 1568 |
| 22 | All Nippon Airways | 1525 |
| 23 | WMT | 1489 |
| 24 | PGT | 1488 |
| 25 | GLO | 1477 |
| 26 | Air France | 1451 |
| 27 | VIV | 1445 |
| 28 | Wizz Air | 1440 |
| 29 | CXK | 1282 |
| 30 | AEE | 1281 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 220107 |
| 2 | 🇪🇸 ES | 16676 |
| 3 | 🇧🇷 BR | 15507 |
| 4 | 🇦🇺 AU | 15145 |
| 5 | 🇨🇦 CA | 14737 |
| 6 | 🇮🇹 IT | 14436 |
| 7 | 🇮🇳 IN | 14072 |
| 8 | 🇩🇪 DE | 12784 |
| 9 | 🇬🇧 GB | 12289 |
| 10 | 🇨🇴 CO | 12031 |
| 11 | 🇫🇷 FR | 10578 |
| 12 | 🇯🇵 JP | 10226 |
| 13 | 🇹🇷 TR | 8026 |
| 14 | 🇬🇷 GR | 7679 |
| 15 | 🇲🇽 MX | 7288 |
| 16 | 🇨🇭 CH | 7066 |
| 17 | 🇳🇴 NO | 6549 |
| 18 | 🇹🇭 TH | 4749 |
| 19 | 🇲🇾 MY | 4480 |
| 20 | 🇿🇦 ZA | 4452 |
| 21 | 🇵🇱 PL | 4363 |
| 22 | 🇳🇿 NZ | 3680 |
| 23 | 🇵🇭 PH | 3522 |
| 24 | 🇬🇹 GT | 3377 |
| 25 | 🇭🇷 HR | 3025 |
| 26 | 🇰🇷 KR | 2999 |
| 27 | 🇲🇦 MA | 2652 |
| 28 | 🇲🇪 ME | 2482 |
| 29 | 🇳🇱 NL | 2376 |
| 30 | 🇮🇩 ID | 2220 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5407 |
| 2 | Denver International Airport |  | US | 4288 |
| 3 | Indira Gandhi International Airport |  | IN | 3183 |
| 4 | Tokyo International Airport |  | JP | 3055 |
| 5 | Harry Reid International Airport |  | US | 2823 |
| 6 | El Dorado International Airport |  | CO | 2819 |
| 7 | Guaymaral Airport |  | CO | 2786 |
| 8 | Zurich Airport |  | CH | 2754 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2661 |
| 10 | La Aurora Airport |  | GT | 2565 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2563 |
| 12 | Salt Lake City International Airport |  | US | 2336 |
| 13 | Chicago O'Hare International Airport |  | US | 2275 |
| 14 | Congonhas Airport |  | BR | 2260 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2164 |
| 16 | Capua Airport |  | IT | 2078 |
| 17 | Madrid Barajas International Airport |  | ES | 2044 |
| 18 | Frankfurt am Main International Airport |  | DE | 2022 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2000 |
| 20 | Malpensa International Airport |  | IT | 1916 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1893 |
| 22 | Charles de Gaulle International Airport |  | FR | 1872 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1862 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1845 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1807 |
| 26 | Macau International Airport |  | MO | 1761 |
| 27 | Ninoy Aquino International Airport |  | PH | 1730 |
| 28 | Barcelona International Airport |  | ES | 1655 |
| 29 | Charlotte/Douglas International Airport |  | US | 1651 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1631 |
| 31 | Viracopos International Airport |  | BR | 1607 |
| 32 | Kuala Lumpur International Airport |  | MY | 1606 |
| 33 | Seattle-Tacoma International Airport |  | US | 1552 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1542 |
| 35 | Calgary International Airport |  | CA | 1509 |
| 36 | Don Mueang International Airport |  | TH | 1506 |
| 37 | Bengaluru International Airport |  | IN | 1501 |
| 38 | Oslo Gardermoen Airport |  | NO | 1492 |
| 39 | Vancouver International Airport |  | CA | 1481 |
| 40 | Antalya International Airport |  | TR | 1420 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1113 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 990 | 21m | 244 km | 4,168.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 728 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 665 | 1h 6m | 770 km | 8,834.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 659 | 24m | 225 km | 2,556.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 592 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 432 | 44m | 555 km | 4,136.6 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 426 | 27m | 275 km | 2,018.6 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 420 | 1h 50m | 1,423 km | 10,307.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 404 | 44m | 241 km | 1,678.1 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 380 | 24m | 218 km | 1,431.6 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 361 | 21m | 250 km | 1,559.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 350 | 23m | 55 km | 332.7 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 338 | 12m | - | - |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 336 | 19m | 99 km | 575.5 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 18 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 333 | 1h 6m | 706 km | 4,054.3 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 329 | 26m | 215 km | 1,218.5 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 329 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 308 | 19m | 144 km | 766.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 286 | 42m | 535 km | 2,641.4 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 286 | 1h 50m | 1,304 km | 6,434.3 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 283 | 28m | 152 km | 739.6 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 29 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 269 | 18m | 14 km | 67.3 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N98485 |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-09-20 20:10 UTC | 2026-09-20 20:34 UTC | 23m |
| N125PM |  | Erie Municipal Airport (KEIK) | Vance Brand Airport (KLMO) | 2026-09-20 18:57 UTC | 2026-09-20 20:32 UTC | 1h 34m |
| JUMP13 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-09-20 19:45 UTC | 2026-09-20 20:29 UTC | 44m |
| VAR466 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-09-20 19:17 UTC | 2026-09-20 20:25 UTC | 1h 7m |
| N221TR |  | Addison Airport (KADS) | Majors Airport (KGVT) | 2026-09-20 20:07 UTC | 2026-09-20 20:23 UTC | 15m |
| AEE473 | AEE | Nuevo Aeropuerto Internacional Mariscal Sucre (SEQM) | Nuevo Aeropuerto Internacional Mariscal Sucre (SEQM) | 2026-09-20 19:39 UTC | 2026-09-20 20:16 UTC | 37m |
| ADZ4202 | ADZ | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-09-20 13:13 UTC | 2026-09-20 20:16 UTC | 7h 2m |
| PAL684 | Philippine Airlines | Ninoy Aquino International Airport (RPLL) | Al Udeid Air Base (OTBH) | 2026-09-20 11:26 UTC | 2026-09-20 20:15 UTC | 8h 48m |
| CFRKF | CFR | Yarmouth Airport (CYQI) | Havelock Airport (CCS5) | 2026-09-20 19:51 UTC | 2026-09-20 20:10 UTC | 18m |
| N9552A |  | Addison Airport (KADS) | Mesquite Metro Airport (KHQZ) | 2026-09-20 19:11 UTC | 2026-09-20 20:06 UTC | 55m |
| N32WS |  | Cecil Ranch Airport (37CN) | 6CL4 (6CL4) | 2026-09-20 19:11 UTC | 2026-09-20 20:06 UTC | 54m |
| ZKTAN | ZKT | Mercer1 PDZ Airport (NZME) | Mercer1 PDZ Airport (NZME) | 2026-09-20 19:59 UTC | 2026-09-20 20:03 UTC | 4m |
| N98KC |  | Tyler Pounds Regional Airport (KTYR) | Comanche County-City Airport (KMKN) | 2026-09-20 19:17 UTC | 2026-09-20 20:00 UTC | 43m |
| N721WR |  | KFTG (KFTG) | Moore County Airport (KDUX) | 2026-09-20 19:15 UTC | 2026-09-20 19:58 UTC | 42m |
| N59FH |  | K47A (K47A) | Booneville/Baldwyn Airport (K8M1) | 2026-09-20 19:15 UTC | 2026-09-20 19:56 UTC | 41m |
| N373KM |  | St George Regional Airport (KSGU) | Citabriair Airport (UT43) | 2026-09-20 19:46 UTC | 2026-09-20 19:56 UTC | 10m |
| EJA352 | EJA | St George Regional Airport (KSGU) | Santa Fe Regional Airport (KSAF) | 2026-09-20 19:01 UTC | 2026-09-20 19:55 UTC | 54m |
| JSX160 | JSX | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 2026-09-20 19:03 UTC | 2026-09-20 19:54 UTC | 50m |
| N921RA |  | MHLE (MHLE) | La Aurora Airport (MGGT) | 2026-09-20 19:22 UTC | 2026-09-20 19:50 UTC | 28m |
| WIF149 | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-09-20 19:11 UTC | 2026-09-20 19:50 UTC | 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
