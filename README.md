# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_20:42:03_UTC-green)

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

**Latest saved flight:** 2026-08-09 20:42:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 20:42:03 UTC

- **182,592** saved flights
- **58,291** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **182,592** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,194,863.7 tonnes** estimated CO2 emissions
- **127,238,474 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7255 |
| 2 | SkyWest Airlines | 6638 |
| 3 | EJA | 3605 |
| 4 | IndiGo | 3195 |
| 5 | Southwest Airlines | 2865 |
| 6 | American Airlines | 2852 |
| 7 | ENY | 2274 |
| 8 | Delta Air Lines | 2162 |
| 9 | LATAM Airlines | 1703 |
| 10 | AZU | 1636 |
| 11 | Lufthansa | 1618 |
| 12 | WIF | 1509 |
| 13 | Vueling | 1507 |
| 14 | LXJ | 1438 |
| 15 | Swiss International | 1252 |
| 16 | easyJet | 1249 |
| 17 | AXM | 1226 |
| 18 | EJU | 1123 |
| 19 | QLK | 1116 |
| 20 | All Nippon Airways | 1107 |
| 21 | Alaska Airlines | 1099 |
| 22 | VIV | 1005 |
| 23 | GLO | 980 |
| 24 | AEE | 953 |
| 25 | CXK | 951 |
| 26 | Air France | 948 |
| 27 | Cathay Pacific | 947 |
| 28 | United Airlines | 938 |
| 29 | PGT | 924 |
| 30 | MXY | 914 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 156215 |
| 2 | 🇪🇸 ES | 11745 |
| 3 | 🇧🇷 BR | 10480 |
| 4 | 🇦🇺 AU | 10203 |
| 5 | 🇮🇳 IN | 10009 |
| 6 | 🇨🇦 CA | 9940 |
| 7 | 🇮🇹 IT | 9464 |
| 8 | 🇩🇪 DE | 9051 |
| 9 | 🇬🇧 GB | 8465 |
| 10 | 🇯🇵 JP | 7379 |
| 11 | 🇫🇷 FR | 7282 |
| 12 | 🇨🇴 CO | 6810 |
| 13 | 🇬🇷 GR | 5357 |
| 14 | 🇲🇽 MX | 5214 |
| 15 | 🇨🇭 CH | 4879 |
| 16 | 🇹🇷 TR | 4737 |
| 17 | 🇳🇴 NO | 4696 |
| 18 | 🇲🇾 MY | 3195 |
| 19 | 🇵🇱 PL | 3063 |
| 20 | 🇿🇦 ZA | 3031 |
| 21 | 🇹🇭 TH | 2804 |
| 22 | 🇳🇿 NZ | 2608 |
| 23 | 🇵🇭 PH | 2410 |
| 24 | 🇬🇹 GT | 2335 |
| 25 | 🇰🇷 KR | 2263 |
| 26 | 🇲🇦 MA | 1849 |
| 27 | 🇭🇷 HR | 1826 |
| 28 | 🇲🇪 ME | 1649 |
| 29 | 🇳🇱 NL | 1641 |
| 30 | 🇲🇴 MO | 1518 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3783 |
| 2 | Denver International Airport |  | US | 3016 |
| 3 | Tokyo International Airport |  | JP | 2287 |
| 4 | Indira Gandhi International Airport |  | IN | 2237 |
| 5 | Guaymaral Airport |  | CO | 2233 |
| 6 | Harry Reid International Airport |  | US | 2139 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1961 |
| 8 | Zurich Airport |  | CH | 1953 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1898 |
| 10 | La Aurora Airport |  | GT | 1793 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1665 |
| 12 | Chicago O'Hare International Airport |  | US | 1634 |
| 13 | El Dorado International Airport |  | CO | 1632 |
| 14 | Salt Lake City International Airport |  | US | 1629 |
| 15 | Frankfurt am Main International Airport |  | DE | 1584 |
| 16 | Congonhas Airport |  | BR | 1521 |
| 17 | Macau International Airport |  | MO | 1518 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1445 |
| 19 | Madrid Barajas International Airport |  | ES | 1437 |
| 20 | Capua Airport |  | IT | 1434 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1364 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1303 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1270 |
| 24 | Malpensa International Airport |  | IT | 1262 |
| 25 | Charles de Gaulle International Airport |  | FR | 1247 |
| 26 | Charlotte/Douglas International Airport |  | US | 1239 |
| 27 | Kuala Lumpur International Airport |  | MY | 1201 |
| 28 | Bengaluru International Airport |  | IN | 1187 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1138 |
| 30 | Ninoy Aquino International Airport |  | PH | 1135 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1115 |
| 32 | Barcelona International Airport |  | ES | 1081 |
| 33 | Viracopos International Airport |  | BR | 1049 |
| 34 | Reno/Tahoe International Airport |  | US | 1048 |
| 35 | Seattle-Tacoma International Airport |  | US | 1048 |
| 36 | Daniel K Inouye International Airport |  | US | 1043 |
| 37 | Calgary International Airport |  | CA | 1039 |
| 38 | Oslo Gardermoen Airport |  | NO | 1012 |
| 39 | Tenerife Norte Airport |  | ES | 998 |
| 40 | Amsterdam Airport Schiphol |  | NL | 991 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 921 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 671 | 21m | 244 km | 2,825.4 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 434 | 1h 8m | 770 km | 5,765.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 428 | 24m | 225 km | 1,660.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 424 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 327 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 308 | 27m | 275 km | 1,459.5 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 298 | 1h 7m | 706 km | 3,628.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 271 | 44m | 241 km | 1,125.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 267 | 22m | 55 km | 253.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 257 | 1h 48m | 1,423 km | 6,307.2 t |
| 15 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 250 | 8m | - | - |
| 16 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 246 | 20m | 250 km | 1,062.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 230 | 26m | 215 km | 851.8 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 229 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 224 | 19m | 99 km | 383.7 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 222 | 1h 15m | 961 km | 3,679.8 t |
| 22 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 221 | 31m | 49 km | 186.8 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 220 | 50m | 556 km | 2,108.9 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 220 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 219 | 19m | 144 km | 544.8 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 216 | 1h 38m | 1,156 km | 4,309.1 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 215 | 24m | 218 km | 810.0 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 211 | 31m | 369 km | 1,343.1 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 198 | 1h 1m | 695 km | 2,373.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| PROOU | PRO | Eurico de Aguiar Salles Airport (SBVT) | SBMM (SBMM) | 2026-08-09 19:07 UTC | 2026-08-09 20:42 UTC | 1h 34m |
| N9898M |  | Palm Beach County Park Airport (KLNA) | Valkaria Airport (KX59) | 2026-08-09 19:17 UTC | 2026-08-09 20:34 UTC | 1h 17m |
| N5620B |  | Minden-Tahoe Airport (KMEV) | Minden-Tahoe Airport (KMEV) | 2026-08-09 20:05 UTC | 2026-08-09 20:33 UTC | 28m |
| XSN40 | XSN | Truckee-Tahoe Airport (KTRK) | San Carlos Airport (KSQL) | 2026-08-09 19:55 UTC | 2026-08-09 20:31 UTC | 36m |
| N441EH |  | Millington/Memphis Airport (KNQA) | KH21 (KH21) | 2026-08-09 18:30 UTC | 2026-08-09 20:28 UTC | 1h 58m |
| UBG341 | UBG | VGZR (VGZR) | Buraimi Airport (OOBR) | 2026-08-09 16:25 UTC | 2026-08-09 20:23 UTC | 3h 57m |
| TVS78S | TVS | Larnaca International Airport (LCLK) | Queen Alia International Airport (OJAI) | 2026-08-09 20:02 UTC | 2026-08-09 20:17 UTC | 14m |
| S411 |  | 0OR9 (0OR9) | Ken Jernstedt Airfield (K4S2) | 2026-08-09 20:09 UTC | 2026-08-09 20:16 UTC | 6m |
| N200KS |  | Sanderson Field (KSHN) | Sanderson Field (KSHN) | 2026-08-09 19:30 UTC | 2026-08-09 20:14 UTC | 43m |
| RYR34QP | Ryanair | Bristol International Airport (EGGD) | Dublin Airport (EIDW) | 2026-08-09 19:26 UTC | 2026-08-09 20:11 UTC | 45m |
| N78AB |  | Minden-Tahoe Airport (KMEV) | Bryant Field (KO57) | 2026-08-09 18:41 UTC | 2026-08-09 20:11 UTC | 1h 29m |
| JAS59 | JAS | Washington Dulles International Airport (KIAD) | Brunswick Golden Isles Airport (KBQK) | 2026-08-09 18:55 UTC | 2026-08-09 20:10 UTC | 1h 15m |
| EIN27T | Aer Lingus | Dublin Airport (EIDW) | DCAE Cosford Airport (EGWC) | 2026-08-09 19:30 UTC | 2026-08-09 20:09 UTC | 39m |
| EJA449 | EJA | Telluride Regional Airport (KTEX) | Durango-La Plata County Airport (KDRO) | 2026-08-09 19:52 UTC | 2026-08-09 20:06 UTC | 14m |
| N769SR |  | False River Regional Airport (KHZR) | False River Regional Airport (KHZR) | 2026-08-09 19:53 UTC | 2026-08-09 20:04 UTC | 10m |
| TKR132 | TKR | Citabriair Airport (UT43) | Caas Airport (NV98) | 2026-08-09 19:26 UTC | 2026-08-09 20:03 UTC | 37m |
| N560BE |  | Laramie Regional Airport (KLAR) | Kimball Municipal/Robert E Arraj Field (KIBM) | 2026-08-09 19:45 UTC | 2026-08-09 20:03 UTC | 17m |
| TKR105 | TKR | Hill Afb Airport (KHIF) | Morgan County Airport (K42U) | 2026-08-09 19:57 UTC | 2026-08-09 20:01 UTC | 3m |
| LRS1105 | LRS | El Ron Ron Airport (MRER) | Juan Santamaria International Airport (MROC) | 2026-08-09 19:49 UTC | 2026-08-09 20:00 UTC | 11m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-09 19:46 UTC | 2026-08-09 20:00 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
