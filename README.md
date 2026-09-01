# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--01_13:27:41_UTC-green)

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

**Latest saved flight:** 2026-09-01 13:27:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-01 13:27:41 UTC

- **243,541** saved flights
- **73,772** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **243,541** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,933,719.7 tonnes** estimated CO2 emissions
- **170,070,707 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9782 |
| 2 | SkyWest Airlines | 8529 |
| 3 | EJA | 4703 |
| 4 | IndiGo | 4094 |
| 5 | American Airlines | 3918 |
| 6 | Southwest Airlines | 3656 |
| 7 | Delta Air Lines | 3103 |
| 8 | ENY | 2932 |
| 9 | LATAM Airlines | 2336 |
| 10 | AZU | 2263 |
| 11 | Vueling | 2088 |
| 12 | Lufthansa | 1955 |
| 13 | WIF | 1937 |
| 14 | LXJ | 1883 |
| 15 | easyJet | 1697 |
| 16 | Swiss International | 1643 |
| 17 | AXM | 1609 |
| 18 | EJU | 1565 |
| 19 | QLK | 1556 |
| 20 | United Airlines | 1531 |
| 21 | Alaska Airlines | 1455 |
| 22 | All Nippon Airways | 1438 |
| 23 | WMT | 1369 |
| 24 | GLO | 1361 |
| 25 | VIV | 1333 |
| 26 | PGT | 1331 |
| 27 | Air France | 1330 |
| 28 | Wizz Air | 1321 |
| 29 | JetBlue | 1204 |
| 30 | AEE | 1203 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 201678 |
| 2 | 🇪🇸 ES | 15657 |
| 3 | 🇧🇷 BR | 14197 |
| 4 | 🇦🇺 AU | 13830 |
| 5 | 🇨🇦 CA | 13546 |
| 6 | 🇮🇹 IT | 13339 |
| 7 | 🇮🇳 IN | 12753 |
| 8 | 🇩🇪 DE | 12018 |
| 9 | 🇬🇧 GB | 11502 |
| 10 | 🇨🇴 CO | 10514 |
| 11 | 🇫🇷 FR | 9829 |
| 12 | 🇯🇵 JP | 9735 |
| 13 | 🇹🇷 TR | 7243 |
| 14 | 🇬🇷 GR | 7187 |
| 15 | 🇲🇽 MX | 6714 |
| 16 | 🇨🇭 CH | 6558 |
| 17 | 🇳🇴 NO | 6030 |
| 18 | 🇹🇭 TH | 4408 |
| 19 | 🇲🇾 MY | 4317 |
| 20 | 🇿🇦 ZA | 4243 |
| 21 | 🇵🇱 PL | 4097 |
| 22 | 🇳🇿 NZ | 3347 |
| 23 | 🇵🇭 PH | 3340 |
| 24 | 🇬🇹 GT | 3064 |
| 25 | 🇰🇷 KR | 2865 |
| 26 | 🇭🇷 HR | 2809 |
| 27 | 🇲🇦 MA | 2466 |
| 28 | 🇲🇪 ME | 2278 |
| 29 | 🇳🇱 NL | 2203 |
| 30 | 🇮🇩 ID | 2126 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5021 |
| 2 | Denver International Airport |  | US | 3918 |
| 3 | Indira Gandhi International Airport |  | IN | 2973 |
| 4 | Tokyo International Airport |  | JP | 2900 |
| 5 | Guaymaral Airport |  | CO | 2708 |
| 6 | Harry Reid International Airport |  | US | 2589 |
| 7 | Zurich Airport |  | CH | 2560 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2485 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2429 |
| 10 | El Dorado International Airport |  | CO | 2389 |
| 11 | La Aurora Airport |  | GT | 2331 |
| 12 | Salt Lake City International Airport |  | US | 2152 |
| 13 | Chicago O'Hare International Airport |  | US | 2152 |
| 14 | Congonhas Airport |  | BR | 2081 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2017 |
| 16 | Frankfurt am Main International Airport |  | DE | 1926 |
| 17 | Capua Airport |  | IT | 1917 |
| 18 | Madrid Barajas International Airport |  | ES | 1915 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1828 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1790 |
| 21 | Malpensa International Airport |  | IT | 1741 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1720 |
| 23 | Charles de Gaulle International Airport |  | FR | 1709 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1707 |
| 25 | Ninoy Aquino International Airport |  | PH | 1625 |
| 26 | Macau International Airport |  | MO | 1624 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1558 |
| 28 | Charlotte/Douglas International Airport |  | US | 1555 |
| 29 | Kuala Lumpur International Airport |  | MY | 1555 |
| 30 | Barcelona International Airport |  | ES | 1546 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1471 |
| 32 | Viracopos International Airport |  | BR | 1445 |
| 33 | Seattle-Tacoma International Airport |  | US | 1426 |
| 34 | Don Mueang International Airport |  | TH | 1420 |
| 35 | Bengaluru International Airport |  | IN | 1412 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1410 |
| 37 | Calgary International Airport |  | CA | 1397 |
| 38 | Oslo Gardermoen Airport |  | NO | 1371 |
| 39 | Vancouver International Airport |  | CA | 1354 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1330 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1097 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 898 | 21m | 244 km | 3,781.2 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 628 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 621 | 24m | 225 km | 2,409.2 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 615 | 1h 6m | 770 km | 8,169.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 548 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 400 | 27m | 275 km | 1,895.4 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 385 | 1h 50m | 1,423 km | 9,448.5 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 373 | 44m | 555 km | 3,571.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 357 | 44m | 241 km | 1,482.9 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 347 | 21m | 250 km | 1,498.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 335 | 24m | 218 km | 1,262.1 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 325 | 1h 39m | 1,156 km | 6,483.6 t |
| 15 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 322 | 1h 6m | 706 km | 3,920.4 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 322 | 22m | 55 km | 306.1 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 302 | 19m | 99 km | 517.3 t |
| 19 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 296 | 26m | 215 km | 1,096.3 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 287 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 282 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 279 | 1h 14m | 961 km | 4,624.6 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 275 | 19m | 144 km | 684.0 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 262 | 1h 50m | 1,304 km | 5,894.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 251 | 28m | 152 km | 656.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N701NW |  | Las Cruces International Airport (KLRU) | Las Cruces International Airport (KLRU) | 2026-09-01 12:39 UTC | 2026-09-01 13:27 UTC | 47m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-09-01 13:10 UTC | 2026-09-01 13:25 UTC | 15m |
| N309DA |  | Barrow County Airport (KWDR) | Barrow County Airport (KWDR) | 2026-09-01 12:49 UTC | 2026-09-01 13:24 UTC | 35m |
| LHX849 | LHX | Helsinki Vantaa Airport (EFHK) | Frankfurt am Main International Airport (EDDF) | 2026-09-01 11:13 UTC | 2026-09-01 13:23 UTC | 2h 9m |
| N4405T |  | Savannah/Hilton Head International Airport (KSAV) | Statesboro-Bulloch County Airport (KTBR) | 2026-09-01 12:43 UTC | 2026-09-01 13:13 UTC | 29m |
| SWR5131 | Swiss International | London Gatwick Airport (EGKK) | Zurich Airport (LSZH) | 2026-09-01 11:58 UTC | 2026-09-01 13:12 UTC | 1h 13m |
| N33RJ |  | FA64 (FA64) | Orlando Executive Airport (KORL) | 2026-09-01 12:32 UTC | 2026-09-01 13:07 UTC | 34m |
| N725CS |  | Dillant/Hopkins Airport (KEEN) | Laurence G Hanscom Field (KBED) | 2026-09-01 12:47 UTC | 2026-09-01 13:05 UTC | 17m |
| N737TY |  | Mckinney Ntl Airport (KTKI) | Jones Field (KF00) | 2026-09-01 12:40 UTC | 2026-09-01 13:05 UTC | 24m |
| PHBAT | PHB | Seppe Airport (EHSE) | Rotterdam Airport (EHRD) | 2026-09-01 12:38 UTC | 2026-09-01 13:01 UTC | 22m |
| DUKE40 | DUK | Wiesbaden Army Airfield (ETOU) | Wiesbaden Army Airfield (ETOU) | 2026-09-01 12:42 UTC | 2026-09-01 12:59 UTC | 17m |
| RGA08 | RGA | Ambri Airport (LSPM) | Ambri Airport (LSPM) | 2026-09-01 12:56 UTC | 2026-09-01 12:58 UTC | 1m |
| CAL187 | CAL | Gimhae International Airport (RKPK) | Taiwan Taoyuan International Airport (RCTP) | 2026-09-01 11:02 UTC | 2026-09-01 12:57 UTC | 1h 55m |
| N3563Q |  | Schaumburg Regional Airport (K06C) | De Kalb Taylor Municipal Airport (KDKB) | 2026-09-01 12:25 UTC | 2026-09-01 12:57 UTC | 31m |
| N501PJ |  | Georgetown Executive Airport (KGTU) | Roy Hurd Memorial Airport (KE01) | 2026-09-01 12:02 UTC | 2026-09-01 12:56 UTC | 54m |
| OB2088 |  | Jorge Chavez International Airport (SPJC) | Laguna Choclococha Airport (SPNH) | 2026-09-01 11:57 UTC | 2026-09-01 12:50 UTC | 52m |
| ZKIDH | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-09-01 12:41 UTC | 2026-09-01 12:49 UTC | 8m |
| N905NY |  | Capitan FAP Carlos Martinez De Pinillos International Airport (SPRU) | Quiruvilca Airport (SPQR) | 2026-09-01 12:34 UTC | 2026-09-01 12:49 UTC | 14m |
| N756TC |  | Doylestown Airport (KDYL) | Elephant Path Airport (PS03) | 2026-09-01 12:33 UTC | 2026-09-01 12:48 UTC | 14m |
| CKS221 | CKS | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-09-01 02:33 UTC | 2026-09-01 12:47 UTC | 10h 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
