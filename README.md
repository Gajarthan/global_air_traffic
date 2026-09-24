# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_11:49:17_UTC-green)

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

**Latest saved flight:** 2026-09-24 11:49:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-24 11:49:17 UTC

- **268,073** saved flights
- **78,695** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **268,073** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,252,119.6 tonnes** estimated CO2 emissions
- **188,528,672 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10579 |
| 2 | SkyWest Airlines | 9323 |
| 3 | EJA | 5209 |
| 4 | IndiGo | 4495 |
| 5 | American Airlines | 4172 |
| 6 | Southwest Airlines | 3938 |
| 7 | Delta Air Lines | 3333 |
| 8 | ENY | 3149 |
| 9 | LATAM Airlines | 2583 |
| 10 | AZU | 2512 |
| 11 | Vueling | 2241 |
| 12 | WIF | 2176 |
| 13 | LXJ | 2104 |
| 14 | Lufthansa | 2045 |
| 15 | easyJet | 1802 |
| 16 | Swiss International | 1760 |
| 17 | QLK | 1732 |
| 18 | EJU | 1686 |
| 19 | AXM | 1673 |
| 20 | United Airlines | 1643 |
| 21 | Alaska Airlines | 1585 |
| 22 | All Nippon Airways | 1546 |
| 23 | PGT | 1509 |
| 24 | WMT | 1501 |
| 25 | GLO | 1494 |
| 26 | Air France | 1472 |
| 27 | VIV | 1463 |
| 28 | Wizz Air | 1457 |
| 29 | CXK | 1310 |
| 30 | AEE | 1290 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 222891 |
| 2 | 🇪🇸 ES | 16829 |
| 3 | 🇧🇷 BR | 15666 |
| 4 | 🇦🇺 AU | 15441 |
| 5 | 🇨🇦 CA | 14952 |
| 6 | 🇮🇹 IT | 14533 |
| 7 | 🇮🇳 IN | 14216 |
| 8 | 🇩🇪 DE | 12886 |
| 9 | 🇬🇧 GB | 12434 |
| 10 | 🇨🇴 CO | 12259 |
| 11 | 🇫🇷 FR | 10676 |
| 12 | 🇯🇵 JP | 10330 |
| 13 | 🇹🇷 TR | 8128 |
| 14 | 🇬🇷 GR | 7755 |
| 15 | 🇲🇽 MX | 7389 |
| 16 | 🇨🇭 CH | 7140 |
| 17 | 🇳🇴 NO | 6632 |
| 18 | 🇹🇭 TH | 4805 |
| 19 | 🇲🇾 MY | 4518 |
| 20 | 🇿🇦 ZA | 4486 |
| 21 | 🇵🇱 PL | 4397 |
| 22 | 🇳🇿 NZ | 3749 |
| 23 | 🇵🇭 PH | 3558 |
| 24 | 🇬🇹 GT | 3392 |
| 25 | 🇭🇷 HR | 3059 |
| 26 | 🇰🇷 KR | 3041 |
| 27 | 🇲🇦 MA | 2675 |
| 28 | 🇲🇪 ME | 2513 |
| 29 | 🇳🇱 NL | 2402 |
| 30 | 🇮🇩 ID | 2239 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5459 |
| 2 | Denver International Airport |  | US | 4350 |
| 3 | Indira Gandhi International Airport |  | IN | 3217 |
| 4 | Tokyo International Airport |  | JP | 3091 |
| 5 | El Dorado International Airport |  | CO | 2895 |
| 6 | Harry Reid International Airport |  | US | 2866 |
| 7 | Guaymaral Airport |  | CO | 2805 |
| 8 | Zurich Airport |  | CH | 2782 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2690 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2583 |
| 11 | La Aurora Airport |  | GT | 2578 |
| 12 | Salt Lake City International Airport |  | US | 2361 |
| 13 | Chicago O'Hare International Airport |  | US | 2296 |
| 14 | Congonhas Airport |  | BR | 2283 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2193 |
| 16 | Capua Airport |  | IT | 2086 |
| 17 | Madrid Barajas International Airport |  | ES | 2065 |
| 18 | Frankfurt am Main International Airport |  | DE | 2037 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2028 |
| 20 | Malpensa International Airport |  | IT | 1925 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1913 |
| 22 | Charles de Gaulle International Airport |  | FR | 1900 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1882 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1879 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1816 |
| 26 | Macau International Airport |  | MO | 1784 |
| 27 | Ninoy Aquino International Airport |  | PH | 1746 |
| 28 | Charlotte/Douglas International Airport |  | US | 1672 |
| 29 | Barcelona International Airport |  | ES | 1669 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1656 |
| 31 | Viracopos International Airport |  | BR | 1621 |
| 32 | Kuala Lumpur International Airport |  | MY | 1617 |
| 33 | Seattle-Tacoma International Airport |  | US | 1571 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1566 |
| 35 | Calgary International Airport |  | CA | 1528 |
| 36 | Don Mueang International Airport |  | TH | 1522 |
| 37 | Bengaluru International Airport |  | IN | 1512 |
| 38 | Oslo Gardermoen Airport |  | NO | 1507 |
| 39 | Vancouver International Airport |  | CA | 1502 |
| 40 | Antalya International Airport |  | TR | 1431 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1119 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1005 | 21m | 244 km | 4,231.8 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 741 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 676 | 1h 6m | 770 km | 8,980.1 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 669 | 24m | 225 km | 2,595.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 596 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 442 | 44m | 555 km | 4,232.4 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 428 | 27m | 275 km | 2,028.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 425 | 1h 50m | 1,423 km | 10,430.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 410 | 44m | 241 km | 1,703.1 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 383 | 24m | 218 km | 1,442.9 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 364 | 21m | 250 km | 1,572.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 358 | 23m | 55 km | 340.3 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 342 | 12m | - | - |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 340 | 13m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 339 | 1h 6m | 706 km | 4,127.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 336 | 19m | 99 km | 575.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 333 | 26m | 215 km | 1,233.3 t |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 312 | 19m | 144 km | 776.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 304 | 1h 14m | 961 km | 5,039.0 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 293 | 42m | 535 km | 2,706.0 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 27 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 285 | 18m | 14 km | 71.3 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 284 | 28m | 152 km | 742.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 272 | 15m | 154 km | 720.7 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LXC12 | LXC | Saint-Etienne-Boutheon Airport (LFMH) | Clermont-Ferrand Auvergne Airport (LFLC) | 2026-09-24 11:11 UTC | 2026-09-24 11:49 UTC | 37m |
| N656HA |  | Erie International/Tom Ridge Field (KERI) | Erie International/Tom Ridge Field (KERI) | 2026-09-24 11:23 UTC | 2026-09-24 11:40 UTC | 16m |
| UPS914 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Harvard Airport (CN23) | 2026-09-24 08:01 UTC | 2026-09-24 11:29 UTC | 3h 27m |
| MGO124 | MGO | Barcelona International Airport (LEBL) | Ibiza Airport (LEIB) | 2026-09-24 10:49 UTC | 2026-09-24 11:23 UTC | 33m |
| LYPPL | LYP | Paluknys Airport (EYVP) | Paluknys Airport (EYVP) | 2026-09-24 10:39 UTC | 2026-09-24 11:21 UTC | 41m |
| RGA01 | RGA | Dubendorf Airport (LSMD) | Dubendorf Airport (LSMD) | 2026-09-24 11:16 UTC | 2026-09-24 11:19 UTC | 3m |
| GZGGY | GZG | Henstridge Airfield (EGHS) | Henstridge Airfield (EGHS) | 2026-09-24 10:51 UTC | 2026-09-24 11:14 UTC | 23m |
| WIF7JE | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-09-24 10:20 UTC | 2026-09-24 11:04 UTC | 43m |
| DHK703 | DHK | Bahrain International Airport (OBBI) | Macau International Airport (VMMC) | 2026-09-24 03:47 UTC | 2026-09-24 11:03 UTC | 7h 15m |
| IBS1695 | IBS | Madrid Barajas International Airport (LEMD) | Ibiza Airport (LEIB) | 2026-09-24 10:12 UTC | 2026-09-24 11:00 UTC | 48m |
| IGO6393 | IndiGo | Juhu Aerodrome (VAJJ) | Ambala Air Force Station (VIAM) | 2026-09-24 09:24 UTC | 2026-09-24 10:59 UTC | 1h 35m |
| GBRDM | GBR | White Waltham Airfield (EGLM) | White Waltham Airfield (EGLM) | 2026-09-24 10:37 UTC | 2026-09-24 10:56 UTC | 19m |
| WIF8HK | WIF | Bodø Airport (ENBO) | Svolvær Helle Airport (ENSH) | 2026-09-24 10:38 UTC | 2026-09-24 10:55 UTC | 17m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | KXTA (KXTA) | 2026-09-24 10:40 UTC | 2026-09-24 10:55 UTC | 14m |
| LXC12 | LXC | Clermont-Ferrand Auvergne Airport (LFLC) | Saint-Etienne-Boutheon Airport (LFMH) | 2026-09-24 10:14 UTC | 2026-09-24 10:52 UTC | 37m |
| TAM3474 | LATAM Airlines | Congonhas Airport (SBSP) | Catanduva Airport (SDCD) | 2026-09-24 10:09 UTC | 2026-09-24 10:51 UTC | 41m |
| WZZ5UW | Wizz Air | Barcelona International Airport (LEBL) | Budapest Ferenc Liszt International Airport (LHBP) | 2026-09-24 08:30 UTC | 2026-09-24 10:50 UTC | 2h 20m |
| IGO5033 | IndiGo | Indira Gandhi International Airport (VIDP) | Jaipur International Airport (VIJP) | 2026-09-24 10:30 UTC | 2026-09-24 10:49 UTC | 19m |
| LOT1LB | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Graz Airport (LOWG) | 2026-09-24 09:29 UTC | 2026-09-24 10:47 UTC | 1h 17m |
| RYR71JD | Ryanair | Nantes Atlantique Airport (LFRS) | Fes Sefrou Airport (GMFU) | 2026-09-24 08:48 UTC | 2026-09-24 10:44 UTC | 1h 55m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
