# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_18:39:25_UTC-green)

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

**Latest saved flight:** 2026-08-19 18:39:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 18:39:25 UTC

- **216,788** saved flights
- **68,428** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **216,788** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,608,325.1 tonnes** estimated CO2 emissions
- **151,207,252 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8671 |
| 2 | SkyWest Airlines | 7737 |
| 3 | EJA | 4215 |
| 4 | IndiGo | 3691 |
| 5 | American Airlines | 3612 |
| 6 | Southwest Airlines | 3445 |
| 7 | Delta Air Lines | 2802 |
| 8 | ENY | 2676 |
| 9 | LATAM Airlines | 2051 |
| 10 | AZU | 1980 |
| 11 | Vueling | 1822 |
| 12 | Lufthansa | 1812 |
| 13 | WIF | 1733 |
| 14 | LXJ | 1706 |
| 15 | easyJet | 1505 |
| 16 | Swiss International | 1448 |
| 17 | AXM | 1417 |
| 18 | United Airlines | 1369 |
| 19 | EJU | 1352 |
| 20 | QLK | 1346 |
| 21 | Alaska Airlines | 1327 |
| 22 | All Nippon Airways | 1304 |
| 23 | VIV | 1188 |
| 24 | GLO | 1177 |
| 25 | Air France | 1176 |
| 26 | PGT | 1176 |
| 27 | WMT | 1135 |
| 28 | JetBlue | 1104 |
| 29 | Wizz Air | 1102 |
| 30 | AEE | 1088 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 182673 |
| 2 | 🇪🇸 ES | 13912 |
| 3 | 🇧🇷 BR | 12485 |
| 4 | 🇦🇺 AU | 12169 |
| 5 | 🇨🇦 CA | 11930 |
| 6 | 🇮🇹 IT | 11509 |
| 7 | 🇮🇳 IN | 11491 |
| 8 | 🇩🇪 DE | 10749 |
| 9 | 🇬🇧 GB | 10189 |
| 10 | 🇨🇴 CO | 8876 |
| 11 | 🇯🇵 JP | 8870 |
| 12 | 🇫🇷 FR | 8654 |
| 13 | 🇬🇷 GR | 6337 |
| 14 | 🇹🇷 TR | 6234 |
| 15 | 🇲🇽 MX | 6052 |
| 16 | 🇨🇭 CH | 5765 |
| 17 | 🇳🇴 NO | 5393 |
| 18 | 🇲🇾 MY | 3744 |
| 19 | 🇿🇦 ZA | 3683 |
| 20 | 🇵🇱 PL | 3584 |
| 21 | 🇹🇭 TH | 3539 |
| 22 | 🇳🇿 NZ | 2998 |
| 23 | 🇵🇭 PH | 2898 |
| 24 | 🇬🇹 GT | 2751 |
| 25 | 🇰🇷 KR | 2608 |
| 26 | 🇭🇷 HR | 2375 |
| 27 | 🇲🇦 MA | 2184 |
| 28 | 🇳🇱 NL | 1939 |
| 29 | 🇲🇪 ME | 1891 |
| 30 | 🇮🇩 ID | 1818 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4546 |
| 2 | Denver International Airport |  | US | 3525 |
| 3 | Tokyo International Airport |  | JP | 2662 |
| 4 | Indira Gandhi International Airport |  | IN | 2627 |
| 5 | Guaymaral Airport |  | CO | 2586 |
| 6 | Harry Reid International Airport |  | US | 2405 |
| 7 | Zurich Airport |  | CH | 2256 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2226 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2210 |
| 10 | La Aurora Airport |  | GT | 2092 |
| 11 | El Dorado International Airport |  | CO | 2024 |
| 12 | Chicago O'Hare International Airport |  | US | 1991 |
| 13 | Salt Lake City International Airport |  | US | 1911 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1893 |
| 15 | Congonhas Airport |  | BR | 1823 |
| 16 | Frankfurt am Main International Airport |  | DE | 1774 |
| 17 | Madrid Barajas International Airport |  | ES | 1697 |
| 18 | Capua Airport |  | IT | 1651 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1635 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1611 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1591 |
| 22 | Macau International Airport |  | MO | 1562 |
| 23 | Malpensa International Airport |  | IT | 1524 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1516 |
| 25 | Charles de Gaulle International Airport |  | FR | 1490 |
| 26 | Charlotte/Douglas International Airport |  | US | 1456 |
| 27 | Kuala Lumpur International Airport |  | MY | 1378 |
| 28 | Ninoy Aquino International Airport |  | PH | 1376 |
| 29 | Barcelona International Airport |  | ES | 1328 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1323 |
| 31 | Bengaluru International Airport |  | IN | 1315 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1292 |
| 33 | Seattle-Tacoma International Airport |  | US | 1283 |
| 34 | Viracopos International Airport |  | BR | 1263 |
| 35 | Calgary International Airport |  | CA | 1219 |
| 36 | Oslo Gardermoen Airport |  | NO | 1202 |
| 37 | Vitoria/Foronda Airport |  | ES | 1201 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1181 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1173 |
| 40 | Don Mueang International Airport |  | TH | 1167 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1058 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 773 | 21m | 244 km | 3,254.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 534 | 1h 7m | 770 km | 7,093.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 507 | 24m | 225 km | 1,966.9 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 488 | 13m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 476 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 361 | 27m | 275 km | 1,710.6 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 318 | 1h 49m | 1,423 km | 7,804.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 316 | 44m | 241 km | 1,312.6 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 293 | 22m | 55 km | 278.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 285 | 21m | 250 km | 1,231.0 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 271 | 19m | 99 km | 464.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 269 | 1h 38m | 1,156 km | 5,366.4 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 266 | 27m | 215 km | 985.2 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 256 | 1h 14m | 961 km | 4,243.3 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 255 | 13m | - | - |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 253 | 31m | 369 km | 1,610.4 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 247 | 19m | 144 km | 614.4 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 243 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 28 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 233 | 44m | 555 km | 2,231.1 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 232 | 1h 49m | 1,304 km | 5,219.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N739HP |  | Ellison Onizuka Kona International At Keahole Airport (PHKO) | Lanai Airport (PHNY) | 2026-08-19 17:40 UTC | 2026-08-19 18:39 UTC | 58m |
| VVAB705 | VVA | Jacksonville Nas (Towers Field) Airport (KNIP) | Haller Airpark (7FL4) | 2026-08-19 17:50 UTC | 2026-08-19 18:38 UTC | 47m |
| NSZ3534 | NSZ | Billund Airport (EKBI) | London Gatwick Airport (EGKK) | 2026-08-19 17:14 UTC | 2026-08-19 18:37 UTC | 1h 23m |
| N547CA |  | Gene Snyder Airport (KK62) | Gene Snyder Airport (KK62) | 2026-08-19 18:09 UTC | 2026-08-19 18:36 UTC | 27m |
| BBA47 | BBA | Wichita Dwight D Eisenhower Ntl Airport (KICT) | Vintage Field (76KS) | 2026-08-19 16:03 UTC | 2026-08-19 18:35 UTC | 2h 32m |
| NSZ4377 | NSZ | Stockholm-Arlanda Airport (ESSA) | Malpensa International Airport (LIMC) | 2026-08-19 15:47 UTC | 2026-08-19 18:34 UTC | 2h 47m |
| TKR136 | TKR | Boise Air Trml/Gowen Field (KBOI) | Harrington Airport (20ID) | 2026-08-19 18:18 UTC | 2026-08-19 18:30 UTC | 11m |
| N974CS |  | Summit Airport (PAST) | Helio Airport (2AK7) | 2026-08-19 18:13 UTC | 2026-08-19 18:29 UTC | 16m |
| PH1635 |  | EHDB (EHDB) | EHDB (EHDB) | 2026-08-19 18:23 UTC | 2026-08-19 18:27 UTC | 4m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-08-19 17:38 UTC | 2026-08-19 18:18 UTC | 40m |
| N9176H |  | Lenawee County Airport (KADG) | Lenawee County Airport (KADG) | 2026-08-19 17:43 UTC | 2026-08-19 18:18 UTC | 34m |
| SWA349 | Southwest Airlines | Harry Reid International Airport (KLAS) | San Francisco International Airport (KSFO) | 2026-08-19 17:11 UTC | 2026-08-19 18:16 UTC | 1h 5m |
| N223DA |  | Clark Regional Airport (KJVY) | Clark Regional Airport (KJVY) | 2026-08-19 18:00 UTC | 2026-08-19 18:16 UTC | 15m |
| N555NL |  | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-08-19 17:42 UTC | 2026-08-19 18:14 UTC | 32m |
| TOPCT92 | TOP | SD47 (SD47) | 0SD0 (0SD0) | 2026-08-19 18:01 UTC | 2026-08-19 18:13 UTC | 11m |
| UAL1777 | United Airlines | Newark Liberty International Airport (KEWR) | San Francisco International Airport (KSFO) | 2026-08-19 12:26 UTC | 2026-08-19 18:12 UTC | 5h 46m |
| N442AD |  | Portland-Hillsboro Airport (KHIO) | Portland-Hillsboro Airport (KHIO) | 2026-08-19 16:50 UTC | 2026-08-19 18:12 UTC | 1h 22m |
| N313NR |  | Portsmouth International At Pease Airport (KPSM) | Concord Municipal Airport (KCON) | 2026-08-19 17:39 UTC | 2026-08-19 18:11 UTC | 32m |
| N269FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-08-19 17:21 UTC | 2026-08-19 18:11 UTC | 50m |
| SPTN074 | SPT | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-08-19 17:03 UTC | 2026-08-19 18:10 UTC | 1h 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
