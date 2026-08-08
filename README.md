# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_11:17:28_UTC-green)

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

**Latest saved flight:** 2026-08-08 11:17:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 11:17:28 UTC

- **177,972** saved flights
- **57,212** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **177,972** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,139,067.4 tonnes** estimated CO2 emissions
- **124,003,910 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7054 |
| 2 | SkyWest Airlines | 6496 |
| 3 | EJA | 3507 |
| 4 | IndiGo | 3127 |
| 5 | Southwest Airlines | 2804 |
| 6 | American Airlines | 2772 |
| 7 | ENY | 2213 |
| 8 | Delta Air Lines | 2100 |
| 9 | LATAM Airlines | 1646 |
| 10 | Lufthansa | 1593 |
| 11 | AZU | 1581 |
| 12 | WIF | 1488 |
| 13 | Vueling | 1467 |
| 14 | LXJ | 1395 |
| 15 | Swiss International | 1214 |
| 16 | AXM | 1209 |
| 17 | easyJet | 1206 |
| 18 | QLK | 1093 |
| 19 | All Nippon Airways | 1087 |
| 20 | EJU | 1084 |
| 21 | Alaska Airlines | 1081 |
| 22 | VIV | 979 |
| 23 | Cathay Pacific | 946 |
| 24 | CXK | 943 |
| 25 | GLO | 939 |
| 26 | AEE | 927 |
| 27 | United Airlines | 918 |
| 28 | Air France | 916 |
| 29 | MXY | 896 |
| 30 | PGT | 881 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 152739 |
| 2 | 🇪🇸 ES | 11397 |
| 3 | 🇧🇷 BR | 10138 |
| 4 | 🇦🇺 AU | 10066 |
| 5 | 🇮🇳 IN | 9801 |
| 6 | 🇨🇦 CA | 9727 |
| 7 | 🇮🇹 IT | 9203 |
| 8 | 🇩🇪 DE | 8801 |
| 9 | 🇬🇧 GB | 8207 |
| 10 | 🇯🇵 JP | 7221 |
| 11 | 🇫🇷 FR | 7072 |
| 12 | 🇨🇴 CO | 6526 |
| 13 | 🇬🇷 GR | 5189 |
| 14 | 🇲🇽 MX | 5097 |
| 15 | 🇨🇭 CH | 4730 |
| 16 | 🇳🇴 NO | 4624 |
| 17 | 🇹🇷 TR | 4456 |
| 18 | 🇲🇾 MY | 3154 |
| 19 | 🇵🇱 PL | 2964 |
| 20 | 🇿🇦 ZA | 2898 |
| 21 | 🇹🇭 TH | 2689 |
| 22 | 🇳🇿 NZ | 2582 |
| 23 | 🇵🇭 PH | 2358 |
| 24 | 🇬🇹 GT | 2270 |
| 25 | 🇰🇷 KR | 2236 |
| 26 | 🇲🇦 MA | 1797 |
| 27 | 🇭🇷 HR | 1757 |
| 28 | 🇲🇪 ME | 1621 |
| 29 | 🇳🇱 NL | 1604 |
| 30 | 🇲🇴 MO | 1509 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3673 |
| 2 | Denver International Airport |  | US | 2949 |
| 3 | Tokyo International Airport |  | JP | 2242 |
| 4 | Indira Gandhi International Airport |  | IN | 2181 |
| 5 | Guaymaral Airport |  | CO | 2177 |
| 6 | Harry Reid International Airport |  | US | 2113 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1922 |
| 8 | Zurich Airport |  | CH | 1890 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1854 |
| 10 | La Aurora Airport |  | GT | 1745 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1627 |
| 12 | Chicago O'Hare International Airport |  | US | 1599 |
| 13 | Salt Lake City International Airport |  | US | 1591 |
| 14 | El Dorado International Airport |  | CO | 1584 |
| 15 | Frankfurt am Main International Airport |  | DE | 1556 |
| 16 | Macau International Airport |  | MO | 1509 |
| 17 | Congonhas Airport |  | BR | 1471 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1428 |
| 19 | Capua Airport |  | IT | 1394 |
| 20 | Madrid Barajas International Airport |  | ES | 1388 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1322 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1255 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1248 |
| 24 | Malpensa International Airport |  | IT | 1220 |
| 25 | Charlotte/Douglas International Airport |  | US | 1212 |
| 26 | Charles de Gaulle International Airport |  | FR | 1207 |
| 27 | Kuala Lumpur International Airport |  | MY | 1188 |
| 28 | Bengaluru International Airport |  | IN | 1166 |
| 29 | Ninoy Aquino International Airport |  | PH | 1109 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1103 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1098 |
| 32 | Barcelona International Airport |  | ES | 1057 |
| 33 | Daniel K Inouye International Airport |  | US | 1025 |
| 34 | Seattle-Tacoma International Airport |  | US | 1025 |
| 35 | Viracopos International Airport |  | BR | 1016 |
| 36 | Reno/Tahoe International Airport |  | US | 1014 |
| 37 | Calgary International Airport |  | CA | 1012 |
| 38 | Oslo Gardermoen Airport |  | NO | 991 |
| 39 | Tenerife Norte Airport |  | ES | 975 |
| 40 | Amsterdam Airport Schiphol |  | NL | 963 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 899 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 655 | 21m | 244 km | 2,758.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 420 | 24m | 225 km | 1,629.4 t |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 419 | 1h 8m | 770 km | 5,566.1 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 414 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 299 | 27m | 275 km | 1,416.8 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 294 | 1h 7m | 706 km | 3,579.5 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 270 | 44m | 241 km | 1,121.5 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 247 | 1h 48m | 1,423 km | 6,061.8 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 231 | 20m | 250 km | 997.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 226 | 26m | 215 km | 837.0 t |
| 19 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 223 | 8m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 220 | 20m | 99 km | 376.8 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 215 | 51m | 556 km | 2,061.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 212 | 1h 15m | 961 km | 3,514.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 212 | 19m | 144 km | 527.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 208 | 1h 38m | 1,156 km | 4,149.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 208 | 12m | - | - |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 206 | 31m | 369 km | 1,311.2 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 203 | 24m | 218 km | 764.8 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 201 | 28m | 152 km | 525.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 194 | 1h 2m | 695 km | 2,325.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HBZWE | HBZ | Courchevel Airport (LFLJ) | Bex Airport (LSGB) | 2026-08-08 10:51 UTC | 2026-08-08 11:17 UTC | 25m |
| RYR582Z | Ryanair | Helsinki Vantaa Airport (EFHK) | Rojunai Airport (EYRO) | 2026-08-08 10:10 UTC | 2026-08-08 11:01 UTC | 50m |
| WOODVALE | WOO | RAF Woodvale (EGOW) | RAF Woodvale (EGOW) | 2026-08-08 10:52 UTC | 2026-08-08 10:55 UTC | 2m |
| DFOXI | DFO | Pruszcz Gdański Airport (EPPR) | Pruszcz Gdański Airport (EPPR) | 2026-08-08 10:31 UTC | 2026-08-08 10:51 UTC | 19m |
| EIN9CX | Aer Lingus | Denver International Airport (KDEN) | Dublin Airport (EIDW) | 2026-08-08 02:53 UTC | 2026-08-08 10:47 UTC | 7h 54m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-08 10:28 UTC | 2026-08-08 10:39 UTC | 11m |
| GCKTE | GCK | Warton Airport (EGNO) | Warton Airport (EGNO) | 2026-08-08 09:56 UTC | 2026-08-08 10:39 UTC | 42m |
| GDK56R | GDK | Westerland Sylt Airport (EDXW) | Mayerhofen Airport (LOKM) | 2026-08-08 08:32 UTC | 2026-08-08 10:37 UTC | 2h 5m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-08 10:29 UTC | 2026-08-08 10:37 UTC | 8m |
| JES3100 | JES | Jorge Newbery Airpark (SABE) | Ingeniero Ambrosio Taravella Airport (SACO) | 2026-08-08 09:12 UTC | 2026-08-08 10:31 UTC | 1h 18m |
| CXK457 | CXK | Jacksonville Executive At Craig Airport (KCRG) | Jacksonville Executive At Craig Airport (KCRG) | 2026-08-08 10:20 UTC | 2026-08-08 10:27 UTC | 7m |
| ABF8 | ABF | Nice-Cote d'Azur Airport (LFMN) | Helsinki Vantaa Airport (EFHK) | 2026-08-08 07:29 UTC | 2026-08-08 10:25 UTC | 2h 56m |
| DLA6YF | DLA | Munich International Airport (EDDM) | Malpensa International Airport (LIMC) | 2026-08-08 09:21 UTC | 2026-08-08 10:23 UTC | 1h 1m |
| WIF153 | WIF | Sogndal Airport (ENSG) | Sogndal Airport (ENSG) | 2026-08-08 10:06 UTC | 2026-08-08 10:20 UTC | 13m |
| N208PC |  | Hohenems-Dornbirn Airport (LOIH) | Hohenems-Dornbirn Airport (LOIH) | 2026-08-08 07:56 UTC | 2026-08-08 10:19 UTC | 2h 23m |
| OKEUI11 | OKE | Ostrava Leos Janacek Airport (LKMT) | Ostrava Leos Janacek Airport (LKMT) | 2026-08-08 09:49 UTC | 2026-08-08 10:18 UTC | 29m |
| DESSC | DES | Friedrichshafen Airport (EDNY) | Friedrichshafen Airport (EDNY) | 2026-08-08 09:46 UTC | 2026-08-08 10:18 UTC | 32m |
| TKJ80T | TKJ | Sabiha Gokcen International Airport (LTFJ) | Uşak Airport (LTBO) | 2026-08-08 09:42 UTC | 2026-08-08 10:18 UTC | 35m |
| HB3246 |  | Zweisimmen Airport (LSTZ) | Saanen Airport (LSGK) | 2026-08-08 09:23 UTC | 2026-08-08 10:10 UTC | 47m |
| HBDIH | HBD | Ambri Airport (LSPM) | Muenster Aero Airport (LSPU) | 2026-08-08 10:07 UTC | 2026-08-08 10:10 UTC | 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
