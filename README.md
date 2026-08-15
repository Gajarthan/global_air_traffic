# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_22:27:14_UTC-green)

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

**Latest saved flight:** 2026-08-15 22:27:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-15 22:27:14 UTC

- **200,104** saved flights
- **62,439** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **200,104** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,390,830.9 tonnes** estimated CO2 emissions
- **138,598,893 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7974 |
| 2 | SkyWest Airlines | 7198 |
| 3 | EJA | 3926 |
| 4 | IndiGo | 3446 |
| 5 | Southwest Airlines | 3101 |
| 6 | American Airlines | 3091 |
| 7 | ENY | 2476 |
| 8 | Delta Air Lines | 2370 |
| 9 | LATAM Airlines | 1886 |
| 10 | AZU | 1821 |
| 11 | Lufthansa | 1708 |
| 12 | Vueling | 1682 |
| 13 | WIF | 1640 |
| 14 | LXJ | 1590 |
| 15 | easyJet | 1382 |
| 16 | Swiss International | 1349 |
| 17 | AXM | 1308 |
| 18 | EJU | 1240 |
| 19 | QLK | 1225 |
| 20 | All Nippon Airways | 1208 |
| 21 | Alaska Airlines | 1175 |
| 22 | VIV | 1111 |
| 23 | GLO | 1088 |
| 24 | Air France | 1065 |
| 25 | PGT | 1059 |
| 26 | AEE | 1030 |
| 27 | United Airlines | 1020 |
| 28 | CXK | 1011 |
| 29 | WMT | 1009 |
| 30 | Wizz Air | 992 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 169644 |
| 2 | 🇪🇸 ES | 12934 |
| 3 | 🇧🇷 BR | 11550 |
| 4 | 🇦🇺 AU | 11152 |
| 5 | 🇨🇦 CA | 10952 |
| 6 | 🇮🇳 IN | 10764 |
| 7 | 🇮🇹 IT | 10507 |
| 8 | 🇩🇪 DE | 9924 |
| 9 | 🇬🇧 GB | 9397 |
| 10 | 🇯🇵 JP | 8160 |
| 11 | 🇨🇴 CO | 8010 |
| 12 | 🇫🇷 FR | 7989 |
| 13 | 🇬🇷 GR | 5905 |
| 14 | 🇲🇽 MX | 5667 |
| 15 | 🇹🇷 TR | 5571 |
| 16 | 🇨🇭 CH | 5414 |
| 17 | 🇳🇴 NO | 5077 |
| 18 | 🇲🇾 MY | 3428 |
| 19 | 🇿🇦 ZA | 3370 |
| 20 | 🇵🇱 PL | 3306 |
| 21 | 🇹🇭 TH | 3131 |
| 22 | 🇳🇿 NZ | 2776 |
| 23 | 🇵🇭 PH | 2649 |
| 24 | 🇬🇹 GT | 2550 |
| 25 | 🇰🇷 KR | 2419 |
| 26 | 🇭🇷 HR | 2137 |
| 27 | 🇲🇦 MA | 2029 |
| 28 | 🇳🇱 NL | 1798 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1633 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4178 |
| 2 | Denver International Airport |  | US | 3254 |
| 3 | Tokyo International Airport |  | JP | 2495 |
| 4 | Guaymaral Airport |  | CO | 2474 |
| 5 | Indira Gandhi International Airport |  | IN | 2441 |
| 6 | Harry Reid International Airport |  | US | 2278 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2115 |
| 8 | Zurich Airport |  | CH | 2109 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2071 |
| 10 | La Aurora Airport |  | GT | 1953 |
| 11 | El Dorado International Airport |  | CO | 1851 |
| 12 | Salt Lake City International Airport |  | US | 1781 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1779 |
| 14 | Chicago O'Hare International Airport |  | US | 1763 |
| 15 | Congonhas Airport |  | BR | 1691 |
| 16 | Frankfurt am Main International Airport |  | DE | 1680 |
| 17 | Madrid Barajas International Airport |  | ES | 1579 |
| 18 | Capua Airport |  | IT | 1539 |
| 19 | Macau International Airport |  | MO | 1536 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1518 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1474 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1447 |
| 23 | Malpensa International Airport |  | IT | 1398 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1383 |
| 25 | Charles de Gaulle International Airport |  | FR | 1376 |
| 26 | Charlotte/Douglas International Airport |  | US | 1319 |
| 27 | Kuala Lumpur International Airport |  | MY | 1276 |
| 28 | Bengaluru International Airport |  | IN | 1256 |
| 29 | Ninoy Aquino International Airport |  | PH | 1253 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1251 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1221 |
| 32 | Barcelona International Airport |  | ES | 1206 |
| 33 | Viracopos International Airport |  | BR | 1167 |
| 34 | Seattle-Tacoma International Airport |  | US | 1148 |
| 35 | Calgary International Airport |  | CA | 1142 |
| 36 | Reno/Tahoe International Airport |  | US | 1126 |
| 37 | Oslo Gardermoen Airport |  | NO | 1120 |
| 38 | Vitoria/Foronda Airport |  | ES | 1117 |
| 39 | Daniel K Inouye International Airport |  | US | 1102 |
| 40 | Tenerife Norte Airport |  | ES | 1095 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1019 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 488 | 1h 7m | 770 km | 6,482.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 465 | 24m | 225 km | 1,804.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 465 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 382 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 341 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 340 | 27m | 275 km | 1,611.1 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 307 | 1h 7m | 706 km | 3,737.7 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 299 | 44m | 241 km | 1,242.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 292 | 1h 49m | 1,423 km | 7,166.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 286 | 22m | 55 km | 271.8 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 262 | 21m | 250 km | 1,131.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 251 | 24m | 218 km | 945.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 248 | 26m | 215 km | 918.5 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 20 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 245 | 1h 14m | 961 km | 4,061.0 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 244 | 13m | - | - |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 244 | 19m | 99 km | 418.0 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 238 | 1h 37m | 1,156 km | 4,748.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 234 | 19m | 144 km | 582.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 227 | 31m | 369 km | 1,444.9 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 218 | 1h 48m | 1,304 km | 4,904.4 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 216 | 1h 3m | 695 km | 2,589.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N529NG |  | Erie Municipal Airport (KEIK) | Granby-Grand County Airport (KGNB) | 2026-08-15 16:21 UTC | 2026-08-15 22:27 UTC | 6h 6m |
| N469ES |  | Reb Folbre's Place Airport (TE34) | 5TA4 (5TA4) | 2026-08-15 21:45 UTC | 2026-08-15 22:17 UTC | 31m |
| CXK483 | CXK | Oakland County International Airport (KPTK) | Dupont/Lapeer Airport (KD95) | 2026-08-15 21:42 UTC | 2026-08-15 22:10 UTC | 28m |
| LFA546 | LFA | Cecil Airport (KVQQ) | Jacksonville International Airport (KJAX) | 2026-08-15 21:57 UTC | 2026-08-15 22:09 UTC | 11m |
| N785MT |  | Buffalo Niagara International Airport (KBUF) | Lancaster Airport (KLNS) | 2026-08-15 21:30 UTC | 2026-08-15 22:09 UTC | 38m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-15 21:28 UTC | 2026-08-15 22:05 UTC | 37m |
| OZN948 | OZN | The Wright Place Airport (4FD3) | The Wright Place Airport (4FD3) | 2026-08-15 21:56 UTC | 2026-08-15 22:01 UTC | 5m |
| EJA633 | EJA | Monterey Regional Airport (KMRY) | Henderson Executive Airport (KHND) | 2026-08-15 21:00 UTC | 2026-08-15 21:59 UTC | 58m |
| ASL135 | ASL | Sheremetyevo International Airport (UUEE) | Smolensk North Airport (XUBS) | 2026-08-15 21:09 UTC | 2026-08-15 21:57 UTC | 47m |
| EFY7838 | EFY | El Dorado International Airport (SKBO) | La Nubia Airport (SKMZ) | 2026-08-15 21:27 UTC | 2026-08-15 21:56 UTC | 29m |
| N579AM |  | Bremerton Ntl Airport (KPWT) | WA05 (WA05) | 2026-08-15 21:46 UTC | 2026-08-15 21:54 UTC | 7m |
| N911MN |  | Joe Foss Field (KFSD) | Lee Airport (SD83) | 2026-08-15 21:37 UTC | 2026-08-15 21:52 UTC | 14m |
| XE1182 |  | Harry Reid International Airport (KLAS) | Santa Monica Municipal Airport (KSMO) | 2026-08-15 20:48 UTC | 2026-08-15 21:50 UTC | 1h 1m |
| N100BW |  | Talkeetna Village Strip (AK44) | Nugget Bench Airport (33AK) | 2026-08-15 21:12 UTC | 2026-08-15 21:49 UTC | 37m |
| SCJ78 | SCJ | Webster Field (ME91) | Selle Airport (SD30) | 2026-08-15 18:54 UTC | 2026-08-15 21:48 UTC | 2h 53m |
| N233S |  | Desert Creek Airport (NV97) | Desert Creek Airport (NV97) | 2026-08-15 21:03 UTC | 2026-08-15 21:46 UTC | 42m |
| N781AK |  | Merrill Field (PAMR) | Big Mountain Airport (PABM) | 2026-08-15 21:03 UTC | 2026-08-15 21:44 UTC | 41m |
| JUMP16 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-08-15 20:24 UTC | 2026-08-15 21:43 UTC | 1h 18m |
| VIV9450 | VIV | Santa Lucia Air Force Base (MMSM) | Quetzalcoatl International Airport (MMNL) | 2026-08-15 20:39 UTC | 2026-08-15 21:42 UTC | 1h 2m |
| N403TD |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-15 21:25 UTC | 2026-08-15 21:38 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
