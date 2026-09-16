# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_21:16:29_UTC-green)

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

**Latest saved flight:** 2026-09-16 21:16:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-16 21:16:29 UTC

- **260,620** saved flights
- **77,250** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **260,620** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,156,543.6 tonnes** estimated CO2 emissions
- **182,988,036 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10323 |
| 2 | SkyWest Airlines | 9080 |
| 3 | EJA | 5053 |
| 4 | IndiGo | 4371 |
| 5 | American Airlines | 4102 |
| 6 | Southwest Airlines | 3828 |
| 7 | Delta Air Lines | 3255 |
| 8 | ENY | 3083 |
| 9 | LATAM Airlines | 2511 |
| 10 | AZU | 2447 |
| 11 | Vueling | 2197 |
| 12 | WIF | 2096 |
| 13 | LXJ | 2037 |
| 14 | Lufthansa | 2023 |
| 15 | easyJet | 1769 |
| 16 | Swiss International | 1733 |
| 17 | QLK | 1681 |
| 18 | AXM | 1649 |
| 19 | EJU | 1647 |
| 20 | United Airlines | 1605 |
| 21 | Alaska Airlines | 1548 |
| 22 | All Nippon Airways | 1511 |
| 23 | WMT | 1469 |
| 24 | GLO | 1453 |
| 25 | PGT | 1453 |
| 26 | Air France | 1431 |
| 27 | VIV | 1426 |
| 28 | Wizz Air | 1414 |
| 29 | TKR | 1263 |
| 30 | AEE | 1260 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 216441 |
| 2 | 🇪🇸 ES | 16492 |
| 3 | 🇧🇷 BR | 15245 |
| 4 | 🇦🇺 AU | 14885 |
| 5 | 🇨🇦 CA | 14521 |
| 6 | 🇮🇹 IT | 14187 |
| 7 | 🇮🇳 IN | 13771 |
| 8 | 🇩🇪 DE | 12639 |
| 9 | 🇬🇧 GB | 12125 |
| 10 | 🇨🇴 CO | 11736 |
| 11 | 🇫🇷 FR | 10449 |
| 12 | 🇯🇵 JP | 10125 |
| 13 | 🇹🇷 TR | 7872 |
| 14 | 🇬🇷 GR | 7571 |
| 15 | 🇲🇽 MX | 7175 |
| 16 | 🇨🇭 CH | 6983 |
| 17 | 🇳🇴 NO | 6432 |
| 18 | 🇹🇭 TH | 4680 |
| 19 | 🇲🇾 MY | 4442 |
| 20 | 🇿🇦 ZA | 4406 |
| 21 | 🇵🇱 PL | 4303 |
| 22 | 🇳🇿 NZ | 3609 |
| 23 | 🇵🇭 PH | 3487 |
| 24 | 🇬🇹 GT | 3327 |
| 25 | 🇭🇷 HR | 2979 |
| 26 | 🇰🇷 KR | 2970 |
| 27 | 🇲🇦 MA | 2610 |
| 28 | 🇲🇪 ME | 2453 |
| 29 | 🇳🇱 NL | 2332 |
| 30 | 🇮🇩 ID | 2199 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5339 |
| 2 | Denver International Airport |  | US | 4216 |
| 3 | Indira Gandhi International Airport |  | IN | 3140 |
| 4 | Tokyo International Airport |  | JP | 3021 |
| 5 | Guaymaral Airport |  | CO | 2774 |
| 6 | Harry Reid International Airport |  | US | 2764 |
| 7 | El Dorado International Airport |  | CO | 2735 |
| 8 | Zurich Airport |  | CH | 2725 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2621 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2534 |
| 11 | La Aurora Airport |  | GT | 2524 |
| 12 | Salt Lake City International Airport |  | US | 2296 |
| 13 | Chicago O'Hare International Airport |  | US | 2259 |
| 14 | Congonhas Airport |  | BR | 2228 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2128 |
| 16 | Capua Airport |  | IT | 2034 |
| 17 | Madrid Barajas International Airport |  | ES | 2018 |
| 18 | Frankfurt am Main International Airport |  | DE | 1996 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1962 |
| 20 | Malpensa International Airport |  | IT | 1876 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1873 |
| 22 | Charles de Gaulle International Airport |  | FR | 1842 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1836 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1793 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1781 |
| 26 | Macau International Airport |  | MO | 1725 |
| 27 | Ninoy Aquino International Airport |  | PH | 1711 |
| 28 | Barcelona International Airport |  | ES | 1628 |
| 29 | Charlotte/Douglas International Airport |  | US | 1626 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1601 |
| 31 | Kuala Lumpur International Airport |  | MY | 1595 |
| 32 | Viracopos International Airport |  | BR | 1578 |
| 33 | Seattle-Tacoma International Airport |  | US | 1529 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1517 |
| 35 | Don Mueang International Airport |  | TH | 1495 |
| 36 | Calgary International Airport |  | CA | 1490 |
| 37 | Bengaluru International Airport |  | IN | 1478 |
| 38 | Oslo Gardermoen Airport |  | NO | 1465 |
| 39 | Vancouver International Airport |  | CA | 1463 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1400 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1111 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 972 | 21m | 244 km | 4,092.8 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 705 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 653 | 1h 6m | 770 km | 8,674.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 650 | 24m | 225 km | 2,521.7 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 584 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 423 | 44m | 555 km | 4,050.4 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 421 | 27m | 275 km | 1,994.9 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 412 | 1h 50m | 1,423 km | 10,111.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 396 | 44m | 241 km | 1,644.9 t |
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
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 301 | 1h 14m | 961 km | 4,989.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 300 | 19m | 144 km | 746.2 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 281 | 1h 50m | 1,304 km | 6,321.8 t |
| 26 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 278 | 28m | 152 km | 726.5 t |
| 27 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 277 | 42m | 535 km | 2,558.3 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CES214 | China Eastern | London Gatwick Airport (EGKK) | Ukhta Airport (UUYH) | 2026-09-16 17:12 UTC | 2026-09-16 21:16 UTC | 4h 4m |
| PAG959T | PAG | Winnipeg James Armstrong Richardson International Airport (CYWG) | Winnipeg James Armstrong Richardson International Airport (CYWG) | 2026-09-16 19:39 UTC | 2026-09-16 21:11 UTC | 1h 32m |
| N419JS |  | Bishop International Airport (KFNT) | Livingston County/Spencer J Hardy Airport (KOZW) | 2026-09-16 20:49 UTC | 2026-09-16 21:10 UTC | 21m |
| JEDI02 | JED | Mobile Regional Airport (KMOB) | AL01 (AL01) | 2026-09-16 20:46 UTC | 2026-09-16 21:06 UTC | 20m |
| N149AH |  | Gore Airport (4FL9) | Orlando Executive Airport (KORL) | 2026-09-16 20:44 UTC | 2026-09-16 21:03 UTC | 18m |
| N239FG |  | Trenton Mercer Airport (KTTN) | Flying W Airport (KN14) | 2026-09-16 20:26 UTC | 2026-09-16 21:00 UTC | 34m |
| UGLY37 | UGL | Parr Field (TN53) | Parr Field (TN53) | 2026-09-16 19:45 UTC | 2026-09-16 20:58 UTC | 1h 12m |
| CFJKX | CFJ | Calgary / Springbank Airport (CYBW) | Arkayla Springs Airport (CKY8) | 2026-09-16 20:44 UTC | 2026-09-16 20:58 UTC | 13m |
| N26WR |  | Meadows Field (KBFL) | Santa Monica Municipal Airport (KSMO) | 2026-09-16 20:30 UTC | 2026-09-16 20:57 UTC | 27m |
| N916GW |  | Montgomery-Gibbs Executive Airport (KMYF) | Gillespie Field (KSEE) | 2026-09-16 19:52 UTC | 2026-09-16 20:57 UTC | 1h 5m |
| N64087 |  | Hayward Executive Airport (KHWD) | Tracy Municipal Airport (KTCY) | 2026-09-16 20:15 UTC | 2026-09-16 20:57 UTC | 41m |
| PREY21 | PRE | Randolph Afb Airport (KRND) | San Geronimo Airpark (K8T8) | 2026-09-16 20:24 UTC | 2026-09-16 20:55 UTC | 30m |
| CXK257 | CXK | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-09-16 20:39 UTC | 2026-09-16 20:54 UTC | 15m |
| EB720 |  | Whiting Field Nas South Airport (KNDZ) | 93FD (93FD) | 2026-09-16 20:33 UTC | 2026-09-16 20:54 UTC | 20m |
| CPA3244 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-09-16 16:25 UTC | 2026-09-16 20:52 UTC | 4h 27m |
| SCPR281 | SCP | W4 Ranch Airport (84TE) | W4 Ranch Airport (84TE) | 2026-09-16 20:48 UTC | 2026-09-16 20:48 UTC | 0m |
| RUK9605 | RUK | Belfast International Airport (EGAA) | East Midlands Airport (EGNX) | 2026-09-16 20:04 UTC | 2026-09-16 20:45 UTC | 40m |
| TKR41 | TKR | TX11 (TX11) | Reece Field (94TA) | 2026-09-16 19:13 UTC | 2026-09-16 20:43 UTC | 1h 30m |
| N6500J |  | Atlanta Regional Falcon Field (KFFC) | Newnan Coweta County Airport (KCCO) | 2026-09-16 20:25 UTC | 2026-09-16 20:43 UTC | 17m |
| N439H |  | Westover Arb/Metro Airport (KCEF) | Laguardia Airport (KLGA) | 2026-09-16 19:55 UTC | 2026-09-16 20:43 UTC | 48m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
