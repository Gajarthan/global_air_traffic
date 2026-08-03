# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_20:46:21_UTC-green)

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

**Latest saved flight:** 2026-08-03 20:46:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-03 20:46:21 UTC

- **169,315** saved flights
- **55,258** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **169,315** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,041,152.0 tonnes** estimated CO2 emissions
- **118,327,654 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6756 |
| 2 | SkyWest Airlines | 6188 |
| 3 | EJA | 3366 |
| 4 | IndiGo | 2981 |
| 5 | American Airlines | 2669 |
| 6 | Southwest Airlines | 2663 |
| 7 | ENY | 2107 |
| 8 | Delta Air Lines | 2019 |
| 9 | LATAM Airlines | 1569 |
| 10 | Lufthansa | 1557 |
| 11 | AZU | 1489 |
| 12 | WIF | 1419 |
| 13 | Vueling | 1397 |
| 14 | LXJ | 1330 |
| 15 | AXM | 1166 |
| 16 | Swiss International | 1157 |
| 17 | easyJet | 1139 |
| 18 | EJU | 1039 |
| 19 | Alaska Airlines | 1034 |
| 20 | QLK | 1028 |
| 21 | All Nippon Airways | 1023 |
| 22 | VIV | 934 |
| 23 | Cathay Pacific | 904 |
| 24 | CXK | 897 |
| 25 | United Airlines | 894 |
| 26 | AEE | 887 |
| 27 | GLO | 887 |
| 28 | Air France | 871 |
| 29 | MXY | 866 |
| 30 | JetBlue | 853 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 145974 |
| 2 | 🇪🇸 ES | 10864 |
| 3 | 🇧🇷 BR | 9628 |
| 4 | 🇦🇺 AU | 9409 |
| 5 | 🇮🇳 IN | 9336 |
| 6 | 🇨🇦 CA | 9178 |
| 7 | 🇮🇹 IT | 8747 |
| 8 | 🇩🇪 DE | 8444 |
| 9 | 🇬🇧 GB | 7873 |
| 10 | 🇯🇵 JP | 6789 |
| 11 | 🇫🇷 FR | 6712 |
| 12 | 🇨🇴 CO | 6129 |
| 13 | 🇬🇷 GR | 4923 |
| 14 | 🇲🇽 MX | 4850 |
| 15 | 🇨🇭 CH | 4460 |
| 16 | 🇳🇴 NO | 4426 |
| 17 | 🇹🇷 TR | 4109 |
| 18 | 🇲🇾 MY | 3035 |
| 19 | 🇵🇱 PL | 2858 |
| 20 | 🇿🇦 ZA | 2743 |
| 21 | 🇹🇭 TH | 2459 |
| 22 | 🇳🇿 NZ | 2450 |
| 23 | 🇵🇭 PH | 2235 |
| 24 | 🇬🇹 GT | 2190 |
| 25 | 🇰🇷 KR | 2151 |
| 26 | 🇲🇦 MA | 1712 |
| 27 | 🇭🇷 HR | 1633 |
| 28 | 🇲🇪 ME | 1565 |
| 29 | 🇳🇱 NL | 1540 |
| 30 | 🇲🇴 MO | 1436 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3477 |
| 2 | Denver International Airport |  | US | 2812 |
| 3 | Tokyo International Airport |  | JP | 2133 |
| 4 | Guaymaral Airport |  | CO | 2107 |
| 5 | Indira Gandhi International Airport |  | IN | 2069 |
| 6 | Harry Reid International Airport |  | US | 2033 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1855 |
| 8 | Zurich Airport |  | CH | 1797 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1784 |
| 10 | La Aurora Airport |  | GT | 1690 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1560 |
| 12 | Chicago O'Hare International Airport |  | US | 1537 |
| 13 | El Dorado International Airport |  | CO | 1535 |
| 14 | Salt Lake City International Airport |  | US | 1520 |
| 15 | Frankfurt am Main International Airport |  | DE | 1517 |
| 16 | Macau International Airport |  | MO | 1436 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1399 |
| 18 | Congonhas Airport |  | BR | 1385 |
| 19 | Madrid Barajas International Airport |  | ES | 1333 |
| 20 | Capua Airport |  | IT | 1320 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1281 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1196 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1184 |
| 24 | Charlotte/Douglas International Airport |  | US | 1180 |
| 25 | Charles de Gaulle International Airport |  | FR | 1150 |
| 26 | Kuala Lumpur International Airport |  | MY | 1144 |
| 27 | Malpensa International Airport |  | IT | 1142 |
| 28 | Bengaluru International Airport |  | IN | 1108 |
| 29 | Ninoy Aquino International Airport |  | PH | 1051 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1050 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1047 |
| 32 | Barcelona International Airport |  | ES | 1004 |
| 33 | Daniel K Inouye International Airport |  | US | 984 |
| 34 | Seattle-Tacoma International Airport |  | US | 980 |
| 35 | Viracopos International Airport |  | BR | 962 |
| 36 | Calgary International Airport |  | CA | 957 |
| 37 | Reno/Tahoe International Airport |  | US | 948 |
| 38 | Tenerife Norte Airport |  | ES | 943 |
| 39 | Oslo Gardermoen Airport |  | NO | 941 |
| 40 | Scottsdale Airport |  | US | 934 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 875 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 617 | 21m | 244 km | 2,598.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 403 | 24m | 225 km | 1,563.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 403 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 382 | 1h 9m | 770 km | 5,074.6 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 317 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 289 | 27m | 275 km | 1,369.4 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 251 | 44m | 241 km | 1,042.6 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 246 | 19m | 165 km | 699.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 233 | 1h 47m | 1,423 km | 5,718.2 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 223 | 20m | 250 km | 963.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 219 | 26m | 215 km | 811.1 t |
| 18 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 215 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 211 | 20m | 99 km | 361.4 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 202 | 19m | 144 km | 502.5 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 199 | 1h 15m | 961 km | 3,298.5 t |
| 23 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 198 | 50m | 556 km | 1,898.0 t |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 197 | 31m | 369 km | 1,254.0 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 197 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 190 | 1h 38m | 1,156 km | 3,790.4 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 187 | 24m | 218 km | 704.5 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 185 | 1h 1m | 695 km | 2,217.6 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 182 | 44m | 452 km | 1,418.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CHX77 | CHX | Wiesbaden Army Airfield (ETOU) | Wiesbaden Army Airfield (ETOU) | 2026-08-03 20:28 UTC | 2026-08-03 20:46 UTC | 17m |
| N997TT |  | East Troy Municipal Airport (K57C) | Plows & Props Airport (2WI4) | 2026-08-03 20:25 UTC | 2026-08-03 20:44 UTC | 19m |
| N325LA |  | Auburn University Regional Airport (KAUO) | Auburn University Regional Airport (KAUO) | 2026-08-03 19:57 UTC | 2026-08-03 20:44 UTC | 46m |
| N797TF |  | Hilton Head Airport (KHXD) | Charleston Executive Airport (KJZI) | 2026-08-03 20:19 UTC | 2026-08-03 20:41 UTC | 22m |
| GOLEM31 | GOL | 75OK (75OK) | Nelson High Point Airport (8OK7) | 2026-08-03 20:20 UTC | 2026-08-03 20:37 UTC | 16m |
| CFJEN | CFJ | Vancouver International Airport (CYVR) | Vancouver International Airport (CYVR) | 2026-08-03 20:12 UTC | 2026-08-03 20:30 UTC | 17m |
| N995JG |  | Mirth Airport (WA22) | Boeing Field/King County International Airport (KBFI) | 2026-08-03 20:15 UTC | 2026-08-03 20:30 UTC | 14m |
| RAM721P | Royal Air Maroc | Lyon Saint-Exupery Airport (LFLL) | Ben Slimane Airport (GMMB) | 2026-08-03 18:14 UTC | 2026-08-03 20:28 UTC | 2h 14m |
| JAL72 | Japan Airlines | Tokyo International Airport (RJTT) | Kalaeloa (John Rodgers Field) Airport (PHJR) | 2026-08-03 13:23 UTC | 2026-08-03 20:26 UTC | 7h 3m |
| GTI8174 | GTI | Ted Stevens Anchorage International Airport (PANC) | Atizapan De Zaragoza Airport (MMJC) | 2026-08-03 13:51 UTC | 2026-08-03 20:26 UTC | 6h 34m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-03 20:07 UTC | 2026-08-03 20:25 UTC | 18m |
| ROKT51 | ROK | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Bird Nest Airport (4MS5) | 2026-08-03 20:08 UTC | 2026-08-03 20:25 UTC | 16m |
| ACW2731 | ACW | General Servando Canales International Airport (MMMA) | Del Norte International Airport (MMAN) | 2026-08-03 19:56 UTC | 2026-08-03 20:24 UTC | 27m |
| WZZ427 | Wizz Air | Luqa Airport (LMML) | Łódź Władysław Reymont Airport (EPLL) | 2026-08-03 18:05 UTC | 2026-08-03 20:21 UTC | 2h 16m |
| ENSA47 | ENS | Santa Paula Airport (SISP) | Mirassol Airport (SDMH) | 2026-08-03 19:43 UTC | 2026-08-03 20:20 UTC | 36m |
| SKL6 | SKL | Whangarei Airport (NZWR) | Kaikohe Airport (NZKO) | 2026-08-03 20:05 UTC | 2026-08-03 20:17 UTC | 11m |
| HRT433 | HRT | Los Angeles International Airport (KLAX) | Vancouver International Airport (CYVR) | 2026-08-03 17:51 UTC | 2026-08-03 20:14 UTC | 2h 22m |
| UAL2344 | United Airlines | Austin-Bergstrom International Airport (KAUS) | Washington Dulles International Airport (KIAD) | 2026-08-03 17:19 UTC | 2026-08-03 20:09 UTC | 2h 49m |
| ENY3796 | ENY | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Ronald Reagan Washington Ntl Airport (KDCA) | 2026-08-03 18:02 UTC | 2026-08-03 20:07 UTC | 2h 4m |
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Zhuhai Airport (ZGSD) | 2026-08-03 06:01 UTC | 2026-08-03 20:07 UTC | 14h 5m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
