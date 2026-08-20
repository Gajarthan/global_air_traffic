# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_15:47:53_UTC-green)

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

**Latest saved flight:** 2026-08-20 15:47:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 15:47:53 UTC

- **219,609** saved flights
- **68,958** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **219,609** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,644,225.5 tonnes** estimated CO2 emissions
- **153,288,434 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8807 |
| 2 | SkyWest Airlines | 7818 |
| 3 | EJA | 4253 |
| 4 | IndiGo | 3728 |
| 5 | American Airlines | 3640 |
| 6 | Southwest Airlines | 3473 |
| 7 | Delta Air Lines | 2830 |
| 8 | ENY | 2703 |
| 9 | LATAM Airlines | 2086 |
| 10 | AZU | 2011 |
| 11 | Vueling | 1848 |
| 12 | Lufthansa | 1821 |
| 13 | WIF | 1756 |
| 14 | LXJ | 1732 |
| 15 | easyJet | 1523 |
| 16 | Swiss International | 1462 |
| 17 | AXM | 1443 |
| 18 | United Airlines | 1382 |
| 19 | QLK | 1375 |
| 20 | EJU | 1370 |
| 21 | Alaska Airlines | 1339 |
| 22 | All Nippon Airways | 1319 |
| 23 | VIV | 1199 |
| 24 | GLO | 1198 |
| 25 | Air France | 1191 |
| 26 | PGT | 1190 |
| 27 | WMT | 1158 |
| 28 | Wizz Air | 1121 |
| 29 | JetBlue | 1115 |
| 30 | AEE | 1099 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 184647 |
| 2 | 🇪🇸 ES | 14083 |
| 3 | 🇧🇷 BR | 12683 |
| 4 | 🇦🇺 AU | 12418 |
| 5 | 🇨🇦 CA | 12111 |
| 6 | 🇮🇹 IT | 11703 |
| 7 | 🇮🇳 IN | 11625 |
| 8 | 🇩🇪 DE | 10853 |
| 9 | 🇬🇧 GB | 10323 |
| 10 | 🇨🇴 CO | 9012 |
| 11 | 🇯🇵 JP | 8959 |
| 12 | 🇫🇷 FR | 8751 |
| 13 | 🇬🇷 GR | 6406 |
| 14 | 🇹🇷 TR | 6323 |
| 15 | 🇲🇽 MX | 6103 |
| 16 | 🇨🇭 CH | 5817 |
| 17 | 🇳🇴 NO | 5457 |
| 18 | 🇲🇾 MY | 3818 |
| 19 | 🇿🇦 ZA | 3753 |
| 20 | 🇹🇭 TH | 3655 |
| 21 | 🇵🇱 PL | 3645 |
| 22 | 🇳🇿 NZ | 3041 |
| 23 | 🇵🇭 PH | 2961 |
| 24 | 🇬🇹 GT | 2781 |
| 25 | 🇰🇷 KR | 2635 |
| 26 | 🇭🇷 HR | 2432 |
| 27 | 🇲🇦 MA | 2213 |
| 28 | 🇳🇱 NL | 1955 |
| 29 | 🇲🇪 ME | 1942 |
| 30 | 🇮🇩 ID | 1866 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4599 |
| 2 | Denver International Airport |  | US | 3580 |
| 3 | Tokyo International Airport |  | JP | 2689 |
| 4 | Indira Gandhi International Airport |  | IN | 2664 |
| 5 | Guaymaral Airport |  | CO | 2597 |
| 6 | Harry Reid International Airport |  | US | 2421 |
| 7 | Zurich Airport |  | CH | 2279 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2250 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2232 |
| 10 | La Aurora Airport |  | GT | 2119 |
| 11 | El Dorado International Airport |  | CO | 2058 |
| 12 | Chicago O'Hare International Airport |  | US | 2011 |
| 13 | Salt Lake City International Airport |  | US | 1934 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1900 |
| 15 | Congonhas Airport |  | BR | 1855 |
| 16 | Frankfurt am Main International Airport |  | DE | 1788 |
| 17 | Madrid Barajas International Airport |  | ES | 1724 |
| 18 | Capua Airport |  | IT | 1677 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1643 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1622 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1615 |
| 22 | Macau International Airport |  | MO | 1578 |
| 23 | Malpensa International Airport |  | IT | 1546 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1542 |
| 25 | Charles de Gaulle International Airport |  | FR | 1511 |
| 26 | Charlotte/Douglas International Airport |  | US | 1462 |
| 27 | Ninoy Aquino International Airport |  | PH | 1408 |
| 28 | Kuala Lumpur International Airport |  | MY | 1402 |
| 29 | Barcelona International Airport |  | ES | 1347 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1333 |
| 31 | Bengaluru International Airport |  | IN | 1325 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1306 |
| 33 | Seattle-Tacoma International Airport |  | US | 1299 |
| 34 | Viracopos International Airport |  | BR | 1285 |
| 35 | Calgary International Airport |  | CA | 1237 |
| 36 | Oslo Gardermoen Airport |  | NO | 1218 |
| 37 | Vitoria/Foronda Airport |  | ES | 1218 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1211 |
| 39 | Don Mueang International Airport |  | TH | 1202 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1182 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 786 | 21m | 244 km | 3,309.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 543 | 1h 7m | 770 km | 7,213.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 521 | 24m | 225 km | 2,021.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 497 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 488 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 368 | 27m | 275 km | 1,743.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 323 | 1h 50m | 1,423 km | 7,926.9 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 322 | 44m | 241 km | 1,337.5 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 296 | 22m | 55 km | 281.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 290 | 21m | 250 km | 1,252.6 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 273 | 1h 38m | 1,156 km | 5,446.2 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 271 | 24m | 218 km | 1,021.0 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 270 | 27m | 215 km | 1,000.0 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 261 | 13m | - | - |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 258 | 1h 14m | 961 km | 4,276.5 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 251 | 44m | 555 km | 2,403.4 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 250 | 19m | 144 km | 621.9 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 246 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 237 | 1h 49m | 1,304 km | 5,331.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| VAR450 | VAR | Phoenix Goodyear Airport (KGYR) | Lake Havasu City Airport (KHII) | 2026-08-20 14:38 UTC | 2026-08-20 15:47 UTC | 1h 9m |
| MEOW01 | MEO | 75OK (75OK) | Blackwell-Tonkawa Municipal Airport (KBKN) | 2026-08-20 15:21 UTC | 2026-08-20 15:39 UTC | 17m |
| DFALB | DFA | Saarlouis-Duren Airport (EDRJ) | Saarlouis-Duren Airport (EDRJ) | 2026-08-20 14:49 UTC | 2026-08-20 15:39 UTC | 49m |
| N745U |  | Gary/Chicago International Airport (KGYY) | 89LL (89LL) | 2026-08-20 15:11 UTC | 2026-08-20 15:38 UTC | 27m |
| N732M |  | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-20 15:27 UTC | 2026-08-20 15:38 UTC | 11m |
| N851LW |  | Loxahatchee Airport (7FD6) | Palm Beach County Park Airport (KLNA) | 2026-08-20 14:57 UTC | 2026-08-20 15:35 UTC | 37m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-08-20 15:19 UTC | 2026-08-20 15:32 UTC | 13m |
| N80807 |  | Denton Enterprise Airport (KDTO) | Gainesville Municipal Airport (KGLE) | 2026-08-20 15:11 UTC | 2026-08-20 15:31 UTC | 20m |
| N357MJ |  | John Wayne/Orange County Airport (KSNA) | Henderson Executive Airport (KHND) | 2026-08-20 14:40 UTC | 2026-08-20 15:29 UTC | 48m |
| AUB1340 | AUB | Auburn University Regional Airport (KAUO) | Auburn University Regional Airport (KAUO) | 2026-08-20 14:44 UTC | 2026-08-20 15:29 UTC | 45m |
| N473AT |  | FA44 (FA44) | Palm Beach County Park Airport (KLNA) | 2026-08-20 14:46 UTC | 2026-08-20 15:28 UTC | 42m |
| N92140 |  | Poplar Grove Airport (KC77) | Tri-County Regional Airport (KLNR) | 2026-08-20 14:33 UTC | 2026-08-20 15:26 UTC | 53m |
| N401FN |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-20 14:58 UTC | 2026-08-20 15:25 UTC | 27m |
| PRE45 | PRE | Centennial Airport (KAPA) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-20 15:11 UTC | 2026-08-20 15:25 UTC | 13m |
| N739WR |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-08-20 14:36 UTC | 2026-08-20 15:25 UTC | 48m |
|  |  | Fletcher's Airport (1NC3) | Fletcher's Airport (1NC3) | 2026-08-20 15:22 UTC | 2026-08-20 15:23 UTC | 1m |
| N98EG |  | Linden Airport (KLDJ) | Newark Liberty International Airport (KEWR) | 2026-08-20 13:52 UTC | 2026-08-20 15:17 UTC | 1h 24m |
| N733TL |  | Casper/Natrona County International Airport (KCPR) | Casper/Natrona County International Airport (KCPR) | 2026-08-20 15:04 UTC | 2026-08-20 15:16 UTC | 12m |
| N732M |  | Wichita Dwight D Eisenhower Ntl Airport (KICT) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-20 13:54 UTC | 2026-08-20 15:15 UTC | 1h 21m |
| N97CJ |  | Oakland County International Airport (KPTK) | Antrim County Airport (KACB) | 2026-08-20 14:42 UTC | 2026-08-20 15:14 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
