# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_18:48:31_UTC-green)

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

**Latest saved flight:** 2026-08-22 18:48:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-22 18:48:31 UTC

- **226,565** saved flights
- **70,364** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **226,565** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,730,528.3 tonnes** estimated CO2 emissions
- **158,291,497 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9092 |
| 2 | SkyWest Airlines | 8034 |
| 3 | EJA | 4372 |
| 4 | IndiGo | 3828 |
| 5 | American Airlines | 3720 |
| 6 | Southwest Airlines | 3535 |
| 7 | Delta Air Lines | 2902 |
| 8 | ENY | 2773 |
| 9 | LATAM Airlines | 2167 |
| 10 | AZU | 2098 |
| 11 | Vueling | 1917 |
| 12 | Lufthansa | 1860 |
| 13 | WIF | 1797 |
| 14 | LXJ | 1785 |
| 15 | easyJet | 1568 |
| 16 | Swiss International | 1511 |
| 17 | AXM | 1493 |
| 18 | EJU | 1433 |
| 19 | United Airlines | 1427 |
| 20 | QLK | 1421 |
| 21 | Alaska Airlines | 1371 |
| 22 | All Nippon Airways | 1356 |
| 23 | GLO | 1260 |
| 24 | PGT | 1244 |
| 25 | VIV | 1238 |
| 26 | Air France | 1235 |
| 27 | WMT | 1227 |
| 28 | Wizz Air | 1174 |
| 29 | JetBlue | 1133 |
| 30 | AEE | 1128 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 189664 |
| 2 | 🇪🇸 ES | 14526 |
| 3 | 🇧🇷 BR | 13219 |
| 4 | 🇦🇺 AU | 12778 |
| 5 | 🇨🇦 CA | 12532 |
| 6 | 🇮🇹 IT | 12179 |
| 7 | 🇮🇳 IN | 11931 |
| 8 | 🇩🇪 DE | 11159 |
| 9 | 🇬🇧 GB | 10651 |
| 10 | 🇨🇴 CO | 9329 |
| 11 | 🇯🇵 JP | 9194 |
| 12 | 🇫🇷 FR | 9080 |
| 13 | 🇹🇷 TR | 6643 |
| 14 | 🇬🇷 GR | 6625 |
| 15 | 🇲🇽 MX | 6299 |
| 16 | 🇨🇭 CH | 5989 |
| 17 | 🇳🇴 NO | 5592 |
| 18 | 🇲🇾 MY | 3981 |
| 19 | 🇿🇦 ZA | 3917 |
| 20 | 🇹🇭 TH | 3889 |
| 21 | 🇵🇱 PL | 3767 |
| 22 | 🇳🇿 NZ | 3140 |
| 23 | 🇵🇭 PH | 3087 |
| 24 | 🇬🇹 GT | 2865 |
| 25 | 🇰🇷 KR | 2676 |
| 26 | 🇭🇷 HR | 2560 |
| 27 | 🇲🇦 MA | 2288 |
| 28 | 🇲🇪 ME | 2043 |
| 29 | 🇳🇱 NL | 2026 |
| 30 | 🇮🇩 ID | 1952 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4733 |
| 2 | Denver International Airport |  | US | 3685 |
| 3 | Indira Gandhi International Airport |  | IN | 2750 |
| 4 | Tokyo International Airport |  | JP | 2748 |
| 5 | Guaymaral Airport |  | CO | 2639 |
| 6 | Harry Reid International Airport |  | US | 2466 |
| 7 | Zurich Airport |  | CH | 2357 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2318 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2289 |
| 10 | La Aurora Airport |  | GT | 2182 |
| 11 | El Dorado International Airport |  | CO | 2081 |
| 12 | Chicago O'Hare International Airport |  | US | 2059 |
| 13 | Salt Lake City International Airport |  | US | 1989 |
| 14 | Congonhas Airport |  | BR | 1931 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1930 |
| 16 | Frankfurt am Main International Airport |  | DE | 1823 |
| 17 | Madrid Barajas International Airport |  | ES | 1766 |
| 18 | Capua Airport |  | IT | 1755 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1690 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1688 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1641 |
| 22 | Malpensa International Airport |  | IT | 1607 |
| 23 | Macau International Airport |  | MO | 1594 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1589 |
| 25 | Charles de Gaulle International Airport |  | FR | 1572 |
| 26 | Charlotte/Douglas International Airport |  | US | 1488 |
| 27 | Ninoy Aquino International Airport |  | PH | 1476 |
| 28 | Kuala Lumpur International Airport |  | MY | 1446 |
| 29 | Barcelona International Airport |  | ES | 1408 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1376 |
| 31 | Bengaluru International Airport |  | IN | 1345 |
| 32 | Viracopos International Airport |  | BR | 1342 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1338 |
| 34 | Enrique Olaya Herrera Airport |  | CO | 1331 |
| 35 | Seattle-Tacoma International Airport |  | US | 1331 |
| 36 | Calgary International Airport |  | CA | 1283 |
| 37 | Don Mueang International Airport |  | TH | 1276 |
| 38 | Oslo Gardermoen Airport |  | NO | 1259 |
| 39 | Vitoria/Foronda Airport |  | ES | 1246 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1227 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1074 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 820 | 21m | 244 km | 3,452.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 563 | 1h 6m | 770 km | 7,479.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 555 | 24m | 225 km | 2,153.1 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 539 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 511 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 356 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 343 | 1h 50m | 1,423 km | 8,417.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 313 | 1h 7m | 706 km | 3,810.8 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 303 | 22m | 55 km | 288.0 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 303 | 21m | 250 km | 1,308.8 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 16 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 293 | 44m | 555 km | 2,805.6 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 289 | 1h 38m | 1,156 km | 5,765.4 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 287 | 24m | 218 km | 1,081.2 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 284 | 19m | 99 km | 486.5 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 276 | 27m | 215 km | 1,022.2 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 266 | 1h 14m | 961 km | 4,409.1 t |
| 22 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 258 | 19m | 144 km | 641.8 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 258 | 12m | - | - |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 244 | 1h 50m | 1,304 km | 5,489.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 239 | 28m | 152 km | 624.6 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N65DJ |  | Linden Airport (KLDJ) | Newark Liberty International Airport (KEWR) | 2026-08-22 13:46 UTC | 2026-08-22 18:48 UTC | 5h 1m |
| N352ME |  | Reno/Tahoe International Airport (KRNO) | Rolling Thunder Airport (NV96) | 2026-08-22 18:32 UTC | 2026-08-22 18:45 UTC | 13m |
| N4308P |  | Old Bridge Airport (K3N6) | Old Bridge Airport (K3N6) | 2026-08-22 18:29 UTC | 2026-08-22 18:42 UTC | 13m |
| VTM434 | VTM | Plan De Guadalupe International Airport (MMIO) | Plan De Guadalupe International Airport (MMIO) | 2026-08-22 18:21 UTC | 2026-08-22 18:37 UTC | 15m |
| N49TT |  | Creech Afb Airport (KINS) | North Las Vegas Airport (KVGT) | 2026-08-22 18:05 UTC | 2026-08-22 18:36 UTC | 30m |
| TSW7M | TSW | Dublin Airport (EIDW) | Farnborough Airport (EGLF) | 2026-08-22 17:41 UTC | 2026-08-22 18:36 UTC | 54m |
| N36GV |  | El Paso International Airport (KELP) | 4M Ranch Airfield (48TE) | 2026-08-22 15:01 UTC | 2026-08-22 18:34 UTC | 3h 32m |
| ITY608 | ITY | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | John F Kennedy International Airport (KJFK) | 2026-08-22 09:09 UTC | 2026-08-22 18:31 UTC | 9h 21m |
| SWR9LC | Swiss International | Zurich Airport (LSZH) | Zurich Airport (LSZH) | 2026-08-22 18:29 UTC | 2026-08-22 18:29 UTC | 0m |
| N336WB |  | Dayton/Wright Brothers Airport (KMGY) | Curanda Airport (LL39) | 2026-08-22 16:22 UTC | 2026-08-22 18:27 UTC | 2h 5m |
| N917JG |  | John Wayne/Orange County Airport (KSNA) | Truckee-Tahoe Airport (KTRK) | 2026-08-22 16:59 UTC | 2026-08-22 18:25 UTC | 1h 25m |
| N624W |  | Caldwell Executive Airport (KEUL) | Josephine Ranch Airport (2ID3) | 2026-08-22 17:48 UTC | 2026-08-22 18:20 UTC | 31m |
| N85PF |  | Kaluakoi Airport (HI49) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-08-22 16:44 UTC | 2026-08-22 18:20 UTC | 1h 35m |
| N754FG |  | Trenton Mercer Airport (KTTN) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-08-22 17:27 UTC | 2026-08-22 18:19 UTC | 51m |
| SWR204K | Swiss International | Malpensa International Airport (LIMC) | Zurich Airport (LSZH) | 2026-08-22 17:50 UTC | 2026-08-22 18:18 UTC | 27m |
| TRP7 | TRP | St Mary's County Regional Airport (K2W6) | Ronald Reagan Washington Ntl Airport (KDCA) | 2026-08-22 17:47 UTC | 2026-08-22 18:17 UTC | 30m |
| N737EE |  | Casper/Natrona County International Airport (KCPR) | Casper/Natrona County International Airport (KCPR) | 2026-08-22 18:04 UTC | 2026-08-22 18:17 UTC | 13m |
| N329MH |  | Phoenix Deer Valley Airport (KDVT) | Parsons Field (4AZ6) | 2026-08-22 17:50 UTC | 2026-08-22 18:15 UTC | 24m |
| LYM3712 | LYM | Denver International Airport (KDEN) | Telluride Regional Airport (KTEX) | 2026-08-22 17:35 UTC | 2026-08-22 18:14 UTC | 38m |
| N85FF |  | Tucson International Airport (KTUS) | Scottsdale Airport (KSDL) | 2026-08-22 17:04 UTC | 2026-08-22 18:11 UTC | 1h 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
