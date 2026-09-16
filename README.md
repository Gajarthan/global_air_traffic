# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_18:11:14_UTC-green)

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

**Latest saved flight:** 2026-09-16 18:11:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-16 18:11:14 UTC

- **260,452** saved flights
- **77,215** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **260,452** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,154,634.5 tonnes** estimated CO2 emissions
- **182,877,365 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10311 |
| 2 | SkyWest Airlines | 9070 |
| 3 | EJA | 5051 |
| 4 | IndiGo | 4371 |
| 5 | American Airlines | 4099 |
| 6 | Southwest Airlines | 3826 |
| 7 | Delta Air Lines | 3255 |
| 8 | ENY | 3083 |
| 9 | LATAM Airlines | 2509 |
| 10 | AZU | 2445 |
| 11 | Vueling | 2196 |
| 12 | WIF | 2095 |
| 13 | LXJ | 2034 |
| 14 | Lufthansa | 2023 |
| 15 | easyJet | 1768 |
| 16 | Swiss International | 1733 |
| 17 | QLK | 1681 |
| 18 | AXM | 1649 |
| 19 | EJU | 1647 |
| 20 | United Airlines | 1605 |
| 21 | Alaska Airlines | 1547 |
| 22 | All Nippon Airways | 1511 |
| 23 | WMT | 1469 |
| 24 | PGT | 1452 |
| 25 | GLO | 1451 |
| 26 | Air France | 1431 |
| 27 | VIV | 1426 |
| 28 | Wizz Air | 1414 |
| 29 | AEE | 1260 |
| 30 | TKR | 1260 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 216258 |
| 2 | 🇪🇸 ES | 16484 |
| 3 | 🇧🇷 BR | 15231 |
| 4 | 🇦🇺 AU | 14881 |
| 5 | 🇨🇦 CA | 14503 |
| 6 | 🇮🇹 IT | 14176 |
| 7 | 🇮🇳 IN | 13769 |
| 8 | 🇩🇪 DE | 12639 |
| 9 | 🇬🇧 GB | 12117 |
| 10 | 🇨🇴 CO | 11724 |
| 11 | 🇫🇷 FR | 10447 |
| 12 | 🇯🇵 JP | 10125 |
| 13 | 🇹🇷 TR | 7865 |
| 14 | 🇬🇷 GR | 7570 |
| 15 | 🇲🇽 MX | 7175 |
| 16 | 🇨🇭 CH | 6983 |
| 17 | 🇳🇴 NO | 6430 |
| 18 | 🇹🇭 TH | 4679 |
| 19 | 🇲🇾 MY | 4442 |
| 20 | 🇿🇦 ZA | 4406 |
| 21 | 🇵🇱 PL | 4295 |
| 22 | 🇳🇿 NZ | 3609 |
| 23 | 🇵🇭 PH | 3487 |
| 24 | 🇬🇹 GT | 3327 |
| 25 | 🇭🇷 HR | 2979 |
| 26 | 🇰🇷 KR | 2970 |
| 27 | 🇲🇦 MA | 2609 |
| 28 | 🇲🇪 ME | 2449 |
| 29 | 🇳🇱 NL | 2332 |
| 30 | 🇮🇩 ID | 2199 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5334 |
| 2 | Denver International Airport |  | US | 4213 |
| 3 | Indira Gandhi International Airport |  | IN | 3139 |
| 4 | Tokyo International Airport |  | JP | 3021 |
| 5 | Guaymaral Airport |  | CO | 2770 |
| 6 | Harry Reid International Airport |  | US | 2763 |
| 7 | El Dorado International Airport |  | CO | 2733 |
| 8 | Zurich Airport |  | CH | 2725 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2620 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2534 |
| 11 | La Aurora Airport |  | GT | 2524 |
| 12 | Salt Lake City International Airport |  | US | 2296 |
| 13 | Chicago O'Hare International Airport |  | US | 2258 |
| 14 | Congonhas Airport |  | BR | 2225 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2128 |
| 16 | Capua Airport |  | IT | 2033 |
| 17 | Madrid Barajas International Airport |  | ES | 2017 |
| 18 | Frankfurt am Main International Airport |  | DE | 1996 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1961 |
| 20 | Malpensa International Airport |  | IT | 1876 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1873 |
| 22 | Charles de Gaulle International Airport |  | FR | 1842 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1835 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1792 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1778 |
| 26 | Macau International Airport |  | MO | 1723 |
| 27 | Ninoy Aquino International Airport |  | PH | 1711 |
| 28 | Barcelona International Airport |  | ES | 1627 |
| 29 | Charlotte/Douglas International Airport |  | US | 1624 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1601 |
| 31 | Kuala Lumpur International Airport |  | MY | 1595 |
| 32 | Viracopos International Airport |  | BR | 1577 |
| 33 | Seattle-Tacoma International Airport |  | US | 1528 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1516 |
| 35 | Don Mueang International Airport |  | TH | 1495 |
| 36 | Calgary International Airport |  | CA | 1489 |
| 37 | Bengaluru International Airport |  | IN | 1478 |
| 38 | Oslo Gardermoen Airport |  | NO | 1464 |
| 39 | Vancouver International Airport |  | CA | 1460 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1400 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1110 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 972 | 21m | 244 km | 4,092.8 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 705 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 653 | 1h 6m | 770 km | 8,674.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 650 | 24m | 225 km | 2,521.7 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 584 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 423 | 44m | 555 km | 4,050.4 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 420 | 27m | 275 km | 1,990.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 412 | 1h 50m | 1,423 km | 10,111.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 395 | 44m | 241 km | 1,640.8 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 366 | 24m | 218 km | 1,378.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 359 | 21m | 250 km | 1,550.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 349 | 23m | 55 km | 331.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 332 | 19m | 99 km | 568.7 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 327 | 1h 6m | 706 km | 3,981.2 t |
| 18 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 324 | 12m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 323 | 26m | 215 km | 1,196.3 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 317 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 300 | 1h 14m | 961 km | 4,972.7 t |
| 23 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 299 | 19m | 144 km | 743.7 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 281 | 1h 50m | 1,304 km | 6,321.8 t |
| 26 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 278 | 28m | 152 km | 726.5 t |
| 27 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 277 | 42m | 535 km | 2,558.3 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RYR3TJ | Ryanair | Lamezia Terme Airport (LICA) | Malpensa International Airport (LIMC) | 2026-09-16 16:50 UTC | 2026-09-16 18:11 UTC | 1h 21m |
| N496LA |  | Northeast Philadelphia Airport (KPNE) | Lancaster Airport (KLNS) | 2026-09-16 17:27 UTC | 2026-09-16 18:11 UTC | 43m |
| G72236 |  | Mcnary Field (KSLE) | Portland-Hillsboro Airport (KHIO) | 2026-09-16 17:15 UTC | 2026-09-16 18:06 UTC | 50m |
| N6500J |  | Newnan Coweta County Airport (KCCO) | Newnan Coweta County Airport (KCCO) | 2026-09-16 17:50 UTC | 2026-09-16 18:03 UTC | 12m |
| PERRIS1 | PER | Perris Valley Airport (KL65) | Perris Valley Airport (KL65) | 2026-09-16 16:57 UTC | 2026-09-16 18:02 UTC | 1h 4m |
| STW023 | STW | Antalya International Airport (LTAI) | Bezymyanka Airfield (UWWG) | 2026-09-16 15:12 UTC | 2026-09-16 18:02 UTC | 2h 49m |
| PAT072 | PAT | Orlando International Airport (KMCO) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-09-16 15:58 UTC | 2026-09-16 18:02 UTC | 2h 3m |
| N76091 |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-09-16 17:35 UTC | 2026-09-16 18:01 UTC | 26m |
| KLM877 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-16 10:13 UTC | 2026-09-16 18:01 UTC | 7h 48m |
| LY700 |  | Whiting Field Nas South Airport (KNDZ) | Spencer Nolf Airport (KNRQ) | 2026-09-16 17:06 UTC | 2026-09-16 17:54 UTC | 48m |
| VENUS42 | VEN | Atlantic City International Airport (KACY) | Dover Afb Airport (KDOV) | 2026-09-16 17:10 UTC | 2026-09-16 17:54 UTC | 43m |
| AER121 | AER | Ted Stevens Anchorage International Airport (PANC) | Fairbanks International Airport (PAFA) | 2026-09-16 16:34 UTC | 2026-09-16 17:54 UTC | 1h 19m |
| MSR788 | EgyptAir | Munich International Airport (EDDM) | HE12 (HE12) | 2026-09-16 14:47 UTC | 2026-09-16 17:52 UTC | 3h 5m |
| N729TA |  | Guernsey Airport (EGJB) | Guernsey Airport (EGJB) | 2026-09-16 16:44 UTC | 2026-09-16 17:51 UTC | 1h 7m |
| N55A |  | Cub Field (VA81) | Cub Field (VA81) | 2026-09-16 17:45 UTC | 2026-09-16 17:50 UTC | 4m |
| OUA34 | OUA | University Of Oklahoma Westheimer Airport (KOUN) | Square Air Airport (TS63) | 2026-09-16 16:26 UTC | 2026-09-16 17:49 UTC | 1h 23m |
| N9968F |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-09-16 17:28 UTC | 2026-09-16 17:47 UTC | 18m |
| N916FT |  | Montgomery-Gibbs Executive Airport (KMYF) | Gillespie Field (KSEE) | 2026-09-16 16:50 UTC | 2026-09-16 17:46 UTC | 55m |
| N192JK |  | Gillespie Field (KSEE) | Gillespie Field (KSEE) | 2026-09-16 17:40 UTC | 2026-09-16 17:44 UTC | 4m |
| N241PC |  | Corona Municipal Airport (KAJO) | French Valley Airport (KF70) | 2026-09-16 17:25 UTC | 2026-09-16 17:44 UTC | 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
