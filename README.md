# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_16:54:34_UTC-green)

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

**Latest saved flight:** 2026-08-25 16:54:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 16:54:34 UTC

- **235,765** saved flights
- **72,080** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **235,765** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,839,151.5 tonnes** estimated CO2 emissions
- **164,588,491 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9455 |
| 2 | SkyWest Airlines | 8316 |
| 3 | EJA | 4568 |
| 4 | IndiGo | 3983 |
| 5 | American Airlines | 3822 |
| 6 | Southwest Airlines | 3600 |
| 7 | Delta Air Lines | 2999 |
| 8 | ENY | 2861 |
| 9 | LATAM Airlines | 2263 |
| 10 | AZU | 2196 |
| 11 | Vueling | 2020 |
| 12 | Lufthansa | 1918 |
| 13 | WIF | 1878 |
| 14 | LXJ | 1846 |
| 15 | easyJet | 1644 |
| 16 | Swiss International | 1585 |
| 17 | AXM | 1575 |
| 18 | EJU | 1510 |
| 19 | QLK | 1497 |
| 20 | United Airlines | 1489 |
| 21 | Alaska Airlines | 1417 |
| 22 | All Nippon Airways | 1401 |
| 23 | WMT | 1317 |
| 24 | GLO | 1313 |
| 25 | VIV | 1299 |
| 26 | PGT | 1286 |
| 27 | Air France | 1281 |
| 28 | Wizz Air | 1260 |
| 29 | AEE | 1171 |
| 30 | JetBlue | 1166 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 195755 |
| 2 | 🇪🇸 ES | 15156 |
| 3 | 🇧🇷 BR | 13761 |
| 4 | 🇦🇺 AU | 13340 |
| 5 | 🇨🇦 CA | 13027 |
| 6 | 🇮🇹 IT | 12859 |
| 7 | 🇮🇳 IN | 12408 |
| 8 | 🇩🇪 DE | 11635 |
| 9 | 🇬🇧 GB | 11122 |
| 10 | 🇨🇴 CO | 9973 |
| 11 | 🇯🇵 JP | 9545 |
| 12 | 🇫🇷 FR | 9472 |
| 13 | 🇹🇷 TR | 6997 |
| 14 | 🇬🇷 GR | 6951 |
| 15 | 🇲🇽 MX | 6543 |
| 16 | 🇨🇭 CH | 6307 |
| 17 | 🇳🇴 NO | 5849 |
| 18 | 🇲🇾 MY | 4224 |
| 19 | 🇹🇭 TH | 4218 |
| 20 | 🇿🇦 ZA | 4137 |
| 21 | 🇵🇱 PL | 3934 |
| 22 | 🇳🇿 NZ | 3249 |
| 23 | 🇵🇭 PH | 3241 |
| 24 | 🇬🇹 GT | 2949 |
| 25 | 🇰🇷 KR | 2757 |
| 26 | 🇭🇷 HR | 2712 |
| 27 | 🇲🇦 MA | 2389 |
| 28 | 🇲🇪 ME | 2192 |
| 29 | 🇳🇱 NL | 2121 |
| 30 | 🇮🇩 ID | 2057 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4888 |
| 2 | Denver International Airport |  | US | 3808 |
| 3 | Indira Gandhi International Airport |  | IN | 2878 |
| 4 | Tokyo International Airport |  | JP | 2842 |
| 5 | Guaymaral Airport |  | CO | 2685 |
| 6 | Harry Reid International Airport |  | US | 2522 |
| 7 | Zurich Airport |  | CH | 2470 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2406 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2362 |
| 10 | La Aurora Airport |  | GT | 2248 |
| 11 | El Dorado International Airport |  | CO | 2234 |
| 12 | Chicago O'Hare International Airport |  | US | 2123 |
| 13 | Salt Lake City International Airport |  | US | 2074 |
| 14 | Congonhas Airport |  | BR | 2008 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1975 |
| 16 | Frankfurt am Main International Airport |  | DE | 1877 |
| 17 | Madrid Barajas International Airport |  | ES | 1854 |
| 18 | Capua Airport |  | IT | 1850 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1773 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1738 |
| 21 | Malpensa International Airport |  | IT | 1689 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1669 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1649 |
| 24 | Charles de Gaulle International Airport |  | FR | 1642 |
| 25 | Macau International Airport |  | MO | 1612 |
| 26 | Ninoy Aquino International Airport |  | PH | 1567 |
| 27 | Kuala Lumpur International Airport |  | MY | 1526 |
| 28 | Charlotte/Douglas International Airport |  | US | 1517 |
| 29 | Barcelona International Airport |  | ES | 1490 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1466 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1426 |
| 32 | Viracopos International Airport |  | BR | 1405 |
| 33 | Bengaluru International Airport |  | IN | 1384 |
| 34 | Seattle-Tacoma International Airport |  | US | 1381 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1380 |
| 36 | Don Mueang International Airport |  | TH | 1368 |
| 37 | Calgary International Airport |  | CA | 1346 |
| 38 | Oslo Gardermoen Airport |  | NO | 1324 |
| 39 | O. R. Tambo International Airport |  | ZA | 1286 |
| 40 | Vancouver International Airport |  | CA | 1285 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1088 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 864 | 21m | 244 km | 3,638.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 598 | 1h 6m | 770 km | 7,944.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 595 | 24m | 225 km | 2,308.3 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 594 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 528 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 390 | 27m | 275 km | 1,848.0 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 365 | 1h 50m | 1,423 km | 8,957.7 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 362 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 343 | 44m | 555 km | 3,284.4 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 341 | 44m | 241 km | 1,416.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 333 | 21m | 250 km | 1,438.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 317 | 1h 7m | 706 km | 3,859.5 t |
| 14 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 316 | 24m | 218 km | 1,190.5 t |
| 15 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 311 | 1h 40m | 1,156 km | 6,204.3 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 311 | 22m | 55 km | 295.6 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 292 | 19m | 99 km | 500.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 290 | 27m | 215 km | 1,074.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 273 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 272 | 1h 14m | 961 km | 4,508.5 t |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 267 | 29m | 304 km | 1,399.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 267 | 19m | 144 km | 664.1 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 262 | 15m | 154 km | 694.2 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 252 | 1h 50m | 1,304 km | 5,669.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N273ND |  | Resler Airport (19IN) | II19 (II19) | 2026-08-25 16:40 UTC | 2026-08-25 16:54 UTC | 13m |
| N42022 |  | Mason City Municipal Airport (KMCW) | Mason City Municipal Airport (KMCW) | 2026-08-25 16:20 UTC | 2026-08-25 16:51 UTC | 31m |
| N669FG |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-08-25 16:14 UTC | 2026-08-25 16:48 UTC | 34m |
| OXF2781 | OXF | Chandler Municipal Airport (KCHD) | Phoenix Goodyear Airport (KGYR) | 2026-08-25 16:19 UTC | 2026-08-25 16:47 UTC | 28m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-08-25 16:31 UTC | 2026-08-25 16:44 UTC | 12m |
| TKR855 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-08-25 16:32 UTC | 2026-08-25 16:43 UTC | 11m |
| TKR873 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-08-25 16:31 UTC | 2026-08-25 16:43 UTC | 11m |
| N729JF |  | Santa Barbara Municipal Airport (KSBA) | Colonel James Jabara Airport (KAAO) | 2026-08-25 14:09 UTC | 2026-08-25 16:42 UTC | 2h 32m |
| MANLY21 | MAN | Enid Woodring Regional Airport (KWDG) | Ramey 1 Airport (0OK8) | 2026-08-25 16:18 UTC | 2026-08-25 16:31 UTC | 12m |
| N331US |  | Portland-Troutdale Airport (KTTD) | Shangri-La Airport (0WN1) | 2026-08-25 16:12 UTC | 2026-08-25 16:30 UTC | 17m |
| GRZLY37 | GRZ | Travis Afb Airport (KSUU) | Travis Afb Airport (KSUU) | 2026-08-25 16:15 UTC | 2026-08-25 16:28 UTC | 13m |
| N503SP |  | Norwood Memorial Airport (KOWD) | Norwood Memorial Airport (KOWD) | 2026-08-25 15:44 UTC | 2026-08-25 16:27 UTC | 43m |
| ETH3640 | Ethiopian Airlines | Oslo Gardermoen Airport (ENGM) | Ukhta Airport (UUYH) | 2026-08-25 13:52 UTC | 2026-08-25 16:25 UTC | 2h 32m |
| TORA21 | TOR | Enid Woodring Regional Airport (KWDG) | Lariat Ranch Airport (OK42) | 2026-08-25 16:06 UTC | 2026-08-25 16:24 UTC | 17m |
| THY8CD | Turkish Airlines | Antalya International Airport (LTAI) | Antalya International Airport (LTAI) | 2026-08-25 16:24 UTC | 2026-08-25 16:24 UTC | 0m |
| N408GG |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-25 14:01 UTC | 2026-08-25 16:23 UTC | 2h 21m |
| N49TT |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-25 15:56 UTC | 2026-08-25 16:21 UTC | 25m |
| BOE760 | BOE | Charleston Afb/International Airport (KCHS) | Conway-Horry County Airport (KHYW) | 2026-08-25 14:09 UTC | 2026-08-25 16:20 UTC | 2h 10m |
| XSN06 | XSN | Buchanan Field (KCCR) | Palm Springs International Airport (KPSP) | 2026-08-25 14:46 UTC | 2026-08-25 16:20 UTC | 1h 34m |
| N1220A |  | San Rafael Airport (CA35) | Truckee-Tahoe Airport (KTRK) | 2026-08-25 15:47 UTC | 2026-08-25 16:18 UTC | 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
