# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--11_14:23:39_UTC-green)

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

**Latest saved flight:** 2026-09-11 14:23:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-11 14:23:39 UTC

- **254,873** saved flights
- **76,120** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **254,873** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,075,987.0 tonnes** estimated CO2 emissions
- **178,318,090 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10164 |
| 2 | SkyWest Airlines | 8882 |
| 3 | EJA | 4921 |
| 4 | IndiGo | 4271 |
| 5 | American Airlines | 4040 |
| 6 | Southwest Airlines | 3755 |
| 7 | Delta Air Lines | 3199 |
| 8 | ENY | 3032 |
| 9 | LATAM Airlines | 2457 |
| 10 | AZU | 2374 |
| 11 | Vueling | 2164 |
| 12 | WIF | 2047 |
| 13 | Lufthansa | 1996 |
| 14 | LXJ | 1991 |
| 15 | easyJet | 1739 |
| 16 | Swiss International | 1708 |
| 17 | QLK | 1646 |
| 18 | AXM | 1638 |
| 19 | EJU | 1629 |
| 20 | United Airlines | 1583 |
| 21 | Alaska Airlines | 1515 |
| 22 | All Nippon Airways | 1489 |
| 23 | WMT | 1441 |
| 24 | GLO | 1418 |
| 25 | PGT | 1402 |
| 26 | VIV | 1392 |
| 27 | Air France | 1388 |
| 28 | Wizz Air | 1387 |
| 29 | JetBlue | 1239 |
| 30 | AEE | 1238 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 211525 |
| 2 | 🇪🇸 ES | 16234 |
| 3 | 🇧🇷 BR | 14882 |
| 4 | 🇦🇺 AU | 14555 |
| 5 | 🇨🇦 CA | 14178 |
| 6 | 🇮🇹 IT | 13942 |
| 7 | 🇮🇳 IN | 13373 |
| 8 | 🇩🇪 DE | 12455 |
| 9 | 🇬🇧 GB | 11907 |
| 10 | 🇨🇴 CO | 11306 |
| 11 | 🇫🇷 FR | 10245 |
| 12 | 🇯🇵 JP | 9979 |
| 13 | 🇹🇷 TR | 7638 |
| 14 | 🇬🇷 GR | 7449 |
| 15 | 🇲🇽 MX | 7020 |
| 16 | 🇨🇭 CH | 6844 |
| 17 | 🇳🇴 NO | 6325 |
| 18 | 🇹🇭 TH | 4589 |
| 19 | 🇲🇾 MY | 4405 |
| 20 | 🇿🇦 ZA | 4349 |
| 21 | 🇵🇱 PL | 4228 |
| 22 | 🇳🇿 NZ | 3511 |
| 23 | 🇵🇭 PH | 3441 |
| 24 | 🇬🇹 GT | 3174 |
| 25 | 🇰🇷 KR | 2930 |
| 26 | 🇭🇷 HR | 2922 |
| 27 | 🇲🇦 MA | 2572 |
| 28 | 🇲🇪 ME | 2395 |
| 29 | 🇳🇱 NL | 2293 |
| 30 | 🇮🇩 ID | 2175 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5231 |
| 2 | Denver International Airport |  | US | 4116 |
| 3 | Indira Gandhi International Airport |  | IN | 3085 |
| 4 | Tokyo International Airport |  | JP | 2978 |
| 5 | Guaymaral Airport |  | CO | 2755 |
| 6 | Harry Reid International Airport |  | US | 2700 |
| 7 | Zurich Airport |  | CH | 2666 |
| 8 | El Dorado International Airport |  | CO | 2613 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2575 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2500 |
| 11 | La Aurora Airport |  | GT | 2421 |
| 12 | Salt Lake City International Airport |  | US | 2247 |
| 13 | Chicago O'Hare International Airport |  | US | 2219 |
| 14 | Congonhas Airport |  | BR | 2184 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2083 |
| 16 | Capua Airport |  | IT | 2008 |
| 17 | Madrid Barajas International Airport |  | ES | 1991 |
| 18 | Frankfurt am Main International Airport |  | DE | 1968 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1910 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1846 |
| 21 | Malpensa International Airport |  | IT | 1831 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1791 |
| 23 | Charles de Gaulle International Airport |  | FR | 1791 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1771 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1704 |
| 26 | Macau International Airport |  | MO | 1685 |
| 27 | Ninoy Aquino International Airport |  | PH | 1682 |
| 28 | Barcelona International Airport |  | ES | 1604 |
| 29 | Charlotte/Douglas International Airport |  | US | 1600 |
| 30 | Kuala Lumpur International Airport |  | MY | 1586 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1563 |
| 32 | Viracopos International Airport |  | BR | 1525 |
| 33 | Seattle-Tacoma International Airport |  | US | 1496 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1481 |
| 35 | Don Mueang International Airport |  | TH | 1469 |
| 36 | Calgary International Airport |  | CA | 1467 |
| 37 | Bengaluru International Airport |  | IN | 1449 |
| 38 | Oslo Gardermoen Airport |  | NO | 1441 |
| 39 | Vancouver International Airport |  | CA | 1428 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1375 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1108 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 947 | 21m | 244 km | 3,987.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 679 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 639 | 1h 6m | 770 km | 8,488.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 638 | 24m | 225 km | 2,475.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 570 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 416 | 27m | 275 km | 1,971.2 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 408 | 44m | 555 km | 3,906.8 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 405 | 1h 50m | 1,423 km | 9,939.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 384 | 44m | 241 km | 1,595.1 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 355 | 24m | 218 km | 1,337.4 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 354 | 21m | 250 km | 1,529.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 339 | 23m | 55 km | 322.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 315 | 26m | 215 km | 1,166.6 t |
| 18 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 310 | 19m | 99 km | 531.0 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 307 | 12m | - | - |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 301 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 293 | 1h 14m | 961 km | 4,856.6 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 291 | 19m | 144 km | 723.8 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 274 | 1h 50m | 1,304 km | 6,164.3 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 267 | 41m | 535 km | 2,465.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 262 | 28m | 152 km | 684.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1033A |  | Plant City Airport (KPCM) | Plant City Airport (KPCM) | 2026-09-11 13:59 UTC | 2026-09-11 14:23 UTC | 23m |
| IGO9290 | IndiGo | Cochin International Airport (VOCI) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-11 12:47 UTC | 2026-09-11 14:22 UTC | 1h 34m |
| N578JZ |  | Oakland San Francisco Bay Airport (KOAK) | Sacramento Executive Airport (KSAC) | 2026-09-11 14:01 UTC | 2026-09-11 14:20 UTC | 18m |
| SCU57 | SCU | OK13 (OK13) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-09-11 13:56 UTC | 2026-09-11 14:14 UTC | 18m |
| DKH1662 | DKH | Manchester Airport (EGCC) | Ukhta Airport (UUYH) | 2026-09-11 10:18 UTC | 2026-09-11 14:13 UTC | 3h 55m |
| ERASR42 | ERA | Devil's River Ranch Airport (4TE7) | Devil's River Ranch Airport (4TE7) | 2026-09-11 13:53 UTC | 2026-09-11 14:07 UTC | 13m |
| CHH490 | CHH | Berlin Brandenburg Airport (EDDB) | Tunoshna Airport (UUDL) | 2026-09-11 12:05 UTC | 2026-09-11 14:06 UTC | 2h 0m |
| NDU32 | NDU | Grand Forks Afb Airport (KRDR) | Morten Airport (62ND) | 2026-09-11 13:50 UTC | 2026-09-11 14:00 UTC | 10m |
| TGARH | TGA | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-09-11 13:27 UTC | 2026-09-11 13:59 UTC | 32m |
| N69FH |  | Tampa Executive Airport (KVDF) | Southwest Georgia Regional Airport (KABY) | 2026-09-11 13:17 UTC | 2026-09-11 13:58 UTC | 41m |
| TGBOP | TGB | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-09-11 13:30 UTC | 2026-09-11 13:57 UTC | 27m |
| OKEUD22 | OKE | Medlanky Airport (LKCM) | Medlanky Airport (LKCM) | 2026-09-11 13:44 UTC | 2026-09-11 13:56 UTC | 12m |
| N57UP |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-09-11 13:40 UTC | 2026-09-11 13:55 UTC | 15m |
| N5656E |  | Reno/Tahoe International Airport (KRNO) | NV44 (NV44) | 2026-09-11 13:41 UTC | 2026-09-11 13:55 UTC | 13m |
| TGGAP | TGG | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-09-11 13:32 UTC | 2026-09-11 13:54 UTC | 21m |
| SCU47 | SCU | Pheasant Wings Airport (26OK) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-09-11 13:38 UTC | 2026-09-11 13:54 UTC | 16m |
| MAI333 | MAI | LRPV (LRPV) | LRPV (LRPV) | 2026-09-11 13:47 UTC | 2026-09-11 13:54 UTC | 6m |
| N77400 |  | Southwest Michigan Regional Airport (KBEH) | Charlevoix Municipal Airport (KCVX) | 2026-09-11 12:59 UTC | 2026-09-11 13:53 UTC | 53m |
| CAL163 | CAL | Incheon International Airport (RKSI) | Hsinchu Air Base (RCPO) | 2026-09-11 11:51 UTC | 2026-09-11 13:50 UTC | 1h 59m |
| NWX477 | NWX | Lebanon Municipal Airport (KM54) | Lebanon Municipal Airport (KM54) | 2026-09-11 13:46 UTC | 2026-09-11 13:49 UTC | 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
