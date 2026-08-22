# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_17:24:03_UTC-green)

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

**Latest saved flight:** 2026-08-22 17:24:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-22 17:24:03 UTC

- **226,254** saved flights
- **70,313** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **226,254** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,726,194.2 tonnes** estimated CO2 emissions
- **158,040,246 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9083 |
| 2 | SkyWest Airlines | 8019 |
| 3 | EJA | 4366 |
| 4 | IndiGo | 3826 |
| 5 | American Airlines | 3709 |
| 6 | Southwest Airlines | 3527 |
| 7 | Delta Air Lines | 2892 |
| 8 | ENY | 2764 |
| 9 | LATAM Airlines | 2164 |
| 10 | AZU | 2093 |
| 11 | Vueling | 1916 |
| 12 | Lufthansa | 1858 |
| 13 | WIF | 1797 |
| 14 | LXJ | 1783 |
| 15 | easyJet | 1568 |
| 16 | Swiss International | 1508 |
| 17 | AXM | 1493 |
| 18 | EJU | 1430 |
| 19 | United Airlines | 1424 |
| 20 | QLK | 1421 |
| 21 | Alaska Airlines | 1369 |
| 22 | All Nippon Airways | 1356 |
| 23 | GLO | 1260 |
| 24 | PGT | 1244 |
| 25 | VIV | 1236 |
| 26 | Air France | 1234 |
| 27 | WMT | 1223 |
| 28 | Wizz Air | 1173 |
| 29 | JetBlue | 1130 |
| 30 | AEE | 1126 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 189334 |
| 2 | 🇪🇸 ES | 14508 |
| 3 | 🇧🇷 BR | 13198 |
| 4 | 🇦🇺 AU | 12778 |
| 5 | 🇨🇦 CA | 12516 |
| 6 | 🇮🇹 IT | 12160 |
| 7 | 🇮🇳 IN | 11926 |
| 8 | 🇩🇪 DE | 11151 |
| 9 | 🇬🇧 GB | 10636 |
| 10 | 🇨🇴 CO | 9306 |
| 11 | 🇯🇵 JP | 9194 |
| 12 | 🇫🇷 FR | 9068 |
| 13 | 🇹🇷 TR | 6633 |
| 14 | 🇬🇷 GR | 6620 |
| 15 | 🇲🇽 MX | 6289 |
| 16 | 🇨🇭 CH | 5981 |
| 17 | 🇳🇴 NO | 5592 |
| 18 | 🇲🇾 MY | 3981 |
| 19 | 🇿🇦 ZA | 3913 |
| 20 | 🇹🇭 TH | 3889 |
| 21 | 🇵🇱 PL | 3765 |
| 22 | 🇳🇿 NZ | 3140 |
| 23 | 🇵🇭 PH | 3087 |
| 24 | 🇬🇹 GT | 2865 |
| 25 | 🇰🇷 KR | 2676 |
| 26 | 🇭🇷 HR | 2552 |
| 27 | 🇲🇦 MA | 2285 |
| 28 | 🇲🇪 ME | 2035 |
| 29 | 🇳🇱 NL | 2025 |
| 30 | 🇮🇩 ID | 1952 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4721 |
| 2 | Denver International Airport |  | US | 3681 |
| 3 | Tokyo International Airport |  | JP | 2748 |
| 4 | Indira Gandhi International Airport |  | IN | 2747 |
| 5 | Guaymaral Airport |  | CO | 2637 |
| 6 | Harry Reid International Airport |  | US | 2465 |
| 7 | Zurich Airport |  | CH | 2351 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2310 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2288 |
| 10 | La Aurora Airport |  | GT | 2182 |
| 11 | El Dorado International Airport |  | CO | 2081 |
| 12 | Chicago O'Hare International Airport |  | US | 2051 |
| 13 | Salt Lake City International Airport |  | US | 1986 |
| 14 | Congonhas Airport |  | BR | 1930 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1926 |
| 16 | Frankfurt am Main International Airport |  | DE | 1823 |
| 17 | Madrid Barajas International Airport |  | ES | 1765 |
| 18 | Capua Airport |  | IT | 1752 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1685 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1683 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1639 |
| 22 | Malpensa International Airport |  | IT | 1604 |
| 23 | Macau International Airport |  | MO | 1594 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1589 |
| 25 | Charles de Gaulle International Airport |  | FR | 1569 |
| 26 | Charlotte/Douglas International Airport |  | US | 1484 |
| 27 | Ninoy Aquino International Airport |  | PH | 1476 |
| 28 | Kuala Lumpur International Airport |  | MY | 1446 |
| 29 | Barcelona International Airport |  | ES | 1407 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1375 |
| 31 | Bengaluru International Airport |  | IN | 1345 |
| 32 | Viracopos International Airport |  | BR | 1338 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1337 |
| 34 | Seattle-Tacoma International Airport |  | US | 1330 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1321 |
| 36 | Calgary International Airport |  | CA | 1280 |
| 37 | Don Mueang International Airport |  | TH | 1276 |
| 38 | Oslo Gardermoen Airport |  | NO | 1259 |
| 39 | Vitoria/Foronda Airport |  | ES | 1245 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1226 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1074 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 817 | 21m | 244 km | 3,440.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 563 | 1h 6m | 770 km | 7,479.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 555 | 24m | 225 km | 2,153.1 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 535 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 511 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 356 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 341 | 1h 50m | 1,423 km | 8,368.7 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 313 | 1h 7m | 706 km | 3,810.8 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 302 | 22m | 55 km | 287.0 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 301 | 21m | 250 km | 1,300.1 t |
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
| N902KC |  | John Wayne/Orange County Airport (KSNA) | Chino Airport (KCNO) | 2026-08-22 17:01 UTC | 2026-08-22 17:24 UTC | 22m |
| CGEBB | CGE | Red Deer Regional Airport (CYQF) | Three Hills Airport (CEN3) | 2026-08-22 16:47 UTC | 2026-08-22 17:23 UTC | 36m |
| LJC5 | LJC | Oxford (Kidlington) Airport (EGTK) | Guernsey Airport (EGJB) | 2026-08-22 16:39 UTC | 2026-08-22 17:14 UTC | 35m |
| N784CA |  | Wings Field (KLOM) | Lancaster Airport (KLNS) | 2026-08-22 16:05 UTC | 2026-08-22 17:10 UTC | 1h 4m |
| N40EA |  | Knoxville Municipal Airport (KOXV) | Knoxville Municipal Airport (KOXV) | 2026-08-22 16:50 UTC | 2026-08-22 17:09 UTC | 19m |
| ASP858 | ASP | Boeing Field/King County International Airport (KBFI) | Calgary International Airport (CYYC) | 2026-08-22 15:59 UTC | 2026-08-22 17:03 UTC | 1h 3m |
| N6023S |  | Glendale Regional Airport (KGEU) | Phoenix Goodyear Airport (KGYR) | 2026-08-22 16:41 UTC | 2026-08-22 17:00 UTC | 18m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-22 16:45 UTC | 2026-08-22 16:59 UTC | 14m |
| N89721 |  | Daytona Beach International Airport (KDAB) | Daytona Beach International Airport (KDAB) | 2026-08-22 16:34 UTC | 2026-08-22 16:58 UTC | 23m |
| N245EM |  | South St Paul Municipal/Richard E Fleming Field (KSGS) | South St Paul Municipal/Richard E Fleming Field (KSGS) | 2026-08-22 15:56 UTC | 2026-08-22 16:56 UTC | 59m |
| N9993E |  | Pratermill Flight Park Airport (GA72) | Flying G Ranch Airport (86GA) | 2026-08-22 16:40 UTC | 2026-08-22 16:55 UTC | 15m |
| N90RV |  | Catalina Airport (KAVX) | Big Bear City Airport (KL35) | 2026-08-22 16:19 UTC | 2026-08-22 16:54 UTC | 35m |
| N5659K |  | Abraham Lincoln Capital Airport (KSPI) | Minder Airport (37IL) | 2026-08-22 16:40 UTC | 2026-08-22 16:53 UTC | 13m |
| N113BB |  | Gillespie Field (KSEE) | Hemet-Ryan Airport (KHMT) | 2026-08-22 16:22 UTC | 2026-08-22 16:53 UTC | 30m |
| N511MT |  | Vinton Veterans Memorial Airpark (KVTI) | Iowa City Municipal Airport (KIOW) | 2026-08-22 16:34 UTC | 2026-08-22 16:50 UTC | 16m |
| XCLRF | XCL | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-08-22 16:46 UTC | 2026-08-22 16:49 UTC | 2m |
| AXEL21 | AXE | Robert Gray Army Air Field (KGRK) | Meade Municipal Airport (KMEJ) | 2026-08-22 15:47 UTC | 2026-08-22 16:46 UTC | 58m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-22 16:28 UTC | 2026-08-22 16:45 UTC | 16m |
| N1533K |  | Wayne County Airport (KBJJ) | Wayne County Airport (KBJJ) | 2026-08-22 16:33 UTC | 2026-08-22 16:43 UTC | 10m |
| N340GV |  | Lafayette Regional/Paul Fournet Field (KLFT) | Le Gros Memorial Airport (K3R2) | 2026-08-22 16:17 UTC | 2026-08-22 16:43 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
