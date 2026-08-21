# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_12:04:58_UTC-green)

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

**Latest saved flight:** 2026-08-21 12:04:58 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 12:04:58 UTC

- **221,912** saved flights
- **69,462** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **221,912** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,672,057.7 tonnes** estimated CO2 emissions
- **154,901,897 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8894 |
| 2 | SkyWest Airlines | 7891 |
| 3 | EJA | 4289 |
| 4 | IndiGo | 3769 |
| 5 | American Airlines | 3671 |
| 6 | Southwest Airlines | 3491 |
| 7 | Delta Air Lines | 2852 |
| 8 | ENY | 2724 |
| 9 | LATAM Airlines | 2104 |
| 10 | AZU | 2033 |
| 11 | Vueling | 1869 |
| 12 | Lufthansa | 1836 |
| 13 | WIF | 1776 |
| 14 | LXJ | 1746 |
| 15 | easyJet | 1535 |
| 16 | Swiss International | 1476 |
| 17 | AXM | 1466 |
| 18 | QLK | 1405 |
| 19 | United Airlines | 1390 |
| 20 | EJU | 1387 |
| 21 | Alaska Airlines | 1353 |
| 22 | All Nippon Airways | 1332 |
| 23 | PGT | 1214 |
| 24 | GLO | 1211 |
| 25 | VIV | 1206 |
| 26 | Air France | 1204 |
| 27 | WMT | 1181 |
| 28 | Wizz Air | 1139 |
| 29 | JetBlue | 1119 |
| 30 | AEE | 1108 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 186322 |
| 2 | 🇪🇸 ES | 14227 |
| 3 | 🇧🇷 BR | 12795 |
| 4 | 🇦🇺 AU | 12649 |
| 5 | 🇨🇦 CA | 12251 |
| 6 | 🇮🇹 IT | 11816 |
| 7 | 🇮🇳 IN | 11751 |
| 8 | 🇩🇪 DE | 10953 |
| 9 | 🇬🇧 GB | 10410 |
| 10 | 🇨🇴 CO | 9108 |
| 11 | 🇯🇵 JP | 9045 |
| 12 | 🇫🇷 FR | 8838 |
| 13 | 🇬🇷 GR | 6479 |
| 14 | 🇹🇷 TR | 6424 |
| 15 | 🇲🇽 MX | 6157 |
| 16 | 🇨🇭 CH | 5853 |
| 17 | 🇳🇴 NO | 5522 |
| 18 | 🇲🇾 MY | 3883 |
| 19 | 🇿🇦 ZA | 3819 |
| 20 | 🇹🇭 TH | 3748 |
| 21 | 🇵🇱 PL | 3682 |
| 22 | 🇳🇿 NZ | 3089 |
| 23 | 🇵🇭 PH | 3015 |
| 24 | 🇬🇹 GT | 2793 |
| 25 | 🇰🇷 KR | 2655 |
| 26 | 🇭🇷 HR | 2471 |
| 27 | 🇲🇦 MA | 2229 |
| 28 | 🇳🇱 NL | 1971 |
| 29 | 🇲🇪 ME | 1969 |
| 30 | 🇮🇩 ID | 1898 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4649 |
| 2 | Denver International Airport |  | US | 3615 |
| 3 | Tokyo International Airport |  | JP | 2712 |
| 4 | Indira Gandhi International Airport |  | IN | 2699 |
| 5 | Guaymaral Airport |  | CO | 2606 |
| 6 | Harry Reid International Airport |  | US | 2443 |
| 7 | Zurich Airport |  | CH | 2300 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2276 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2253 |
| 10 | La Aurora Airport |  | GT | 2128 |
| 11 | El Dorado International Airport |  | CO | 2074 |
| 12 | Chicago O'Hare International Airport |  | US | 2025 |
| 13 | Salt Lake City International Airport |  | US | 1948 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1909 |
| 15 | Congonhas Airport |  | BR | 1869 |
| 16 | Frankfurt am Main International Airport |  | DE | 1801 |
| 17 | Madrid Barajas International Airport |  | ES | 1739 |
| 18 | Capua Airport |  | IT | 1696 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1661 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1630 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1625 |
| 22 | Macau International Airport |  | MO | 1586 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1571 |
| 24 | Malpensa International Airport |  | IT | 1554 |
| 25 | Charles de Gaulle International Airport |  | FR | 1529 |
| 26 | Charlotte/Douglas International Airport |  | US | 1471 |
| 27 | Ninoy Aquino International Airport |  | PH | 1435 |
| 28 | Kuala Lumpur International Airport |  | MY | 1418 |
| 29 | Barcelona International Airport |  | ES | 1366 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1346 |
| 31 | Bengaluru International Airport |  | IN | 1331 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1315 |
| 33 | Seattle-Tacoma International Airport |  | US | 1313 |
| 34 | Viracopos International Airport |  | BR | 1300 |
| 35 | Calgary International Airport |  | CA | 1256 |
| 36 | Oslo Gardermoen Airport |  | NO | 1237 |
| 37 | Enrique Olaya Herrera Airport |  | CO | 1236 |
| 38 | Don Mueang International Airport |  | TH | 1233 |
| 39 | Vitoria/Foronda Airport |  | ES | 1231 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1193 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1064 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 800 | 21m | 244 km | 3,368.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 555 | 1h 7m | 770 km | 7,372.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 538 | 24m | 225 km | 2,087.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 499 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 499 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 374 | 27m | 275 km | 1,772.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 351 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 329 | 1h 50m | 1,423 km | 8,074.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 325 | 44m | 241 km | 1,350.0 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 295 | 21m | 250 km | 1,274.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 279 | 1h 39m | 1,156 km | 5,565.9 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 276 | 24m | 218 km | 1,039.8 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 273 | 27m | 215 km | 1,011.1 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 273 | 19m | 99 km | 467.6 t |
| 20 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 270 | 44m | 555 km | 2,585.4 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 261 | 1h 14m | 961 km | 4,326.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 252 | 19m | 144 km | 626.8 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 252 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 239 | 1h 49m | 1,304 km | 5,376.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CJT991 | CJT | Cincinnati/Northern Kentucky International Airport (KCVG) | Montréal (Mirabel) Airport (CYMX) | 2026-08-21 10:39 UTC | 2026-08-21 12:04 UTC | 1h 25m |
| PGT276N | PGT | Zurich Airport (LSZH) | Karain Airport (LTXE) | 2026-08-21 09:08 UTC | 2026-08-21 11:57 UTC | 2h 49m |
| P4JPB |  | Juhu Aerodrome (VAJJ) | Trabzon International Airport (LTCG) | 2026-08-21 06:14 UTC | 2026-08-21 11:56 UTC | 5h 41m |
| SXS5ZP | SXS | Zurich Airport (LSZH) | Karain Airport (LTXE) | 2026-08-21 08:58 UTC | 2026-08-21 11:53 UTC | 2h 54m |
| N399AA |  | Kissimmee Gateway Airport (KISM) | Lakeland Linder International Airport (KLAL) | 2026-08-21 11:25 UTC | 2026-08-21 11:51 UTC | 25m |
| N540M |  | Chippewa Valley Regional Airport (KEAU) | Dane County Regional/Truax Field (KMSN) | 2026-08-21 11:21 UTC | 2026-08-21 11:48 UTC | 27m |
| GGWMB | GGW | Turweston Airport (EGBT) | Turweston Airport (EGBT) | 2026-08-21 11:23 UTC | 2026-08-21 11:46 UTC | 22m |
| N8922V |  | Clearwater Executive Airport (KCLW) | Clearwater Executive Airport (KCLW) | 2026-08-21 11:32 UTC | 2026-08-21 11:36 UTC | 3m |
| CAN12 | CAN | Pescara International Airport (LIBP) | Pescara International Airport (LIBP) | 2026-08-21 10:56 UTC | 2026-08-21 11:33 UTC | 37m |
| GFOXP | GFO | EG32 (EG32) | EG32 (EG32) | 2026-08-21 11:09 UTC | 2026-08-21 11:29 UTC | 20m |
| ROT6451 | ROT | Henri Coanda International Airport (LROP) | Karain Airport (LTXE) | 2026-08-21 03:57 UTC | 2026-08-21 11:19 UTC | 7h 22m |
| GDK56R | GDK | Westerland Sylt Airport (EDXW) | Mayerhofen Airport (LOKM) | 2026-08-21 09:04 UTC | 2026-08-21 11:19 UTC | 2h 15m |
| SXS4GL | SXS | Leipzig Halle Airport (EDDP) | Karain Airport (LTXE) | 2026-08-21 08:19 UTC | 2026-08-21 11:16 UTC | 2h 56m |
| WIF7JE | WIF | Oslo Gardermoen Airport (ENGM) | Bringeland Airport (ENBL) | 2026-08-21 10:23 UTC | 2026-08-21 11:15 UTC | 51m |
| CAI6NE | CAI | Innsbruck Airport (LOWI) | Karain Airport (LTXE) | 2026-08-21 08:38 UTC | 2026-08-21 11:13 UTC | 2h 35m |
| MGH540 | MGH | Budapest Ferenc Liszt International Airport (LHBP) | Karain Airport (LTXE) | 2026-08-21 09:09 UTC | 2026-08-21 11:11 UTC | 2h 1m |
| LLR513 | LLR | Bengaluru International Airport (VOBL) | Hosur Airport (VO95) | 2026-08-21 10:48 UTC | 2026-08-21 11:10 UTC | 21m |
| N247EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-08-21 08:10 UTC | 2026-08-21 11:09 UTC | 2h 59m |
| SEH3DQ | SEH | Eleftherios Venizelos International Airport (LGAV) | Milos Airport (LGML) | 2026-08-21 10:41 UTC | 2026-08-21 11:07 UTC | 26m |
| HK4854 |  | Enrique Olaya Herrera Airport (SKMD) | Amalfi Airport (SKAM) | 2026-08-21 10:56 UTC | 2026-08-21 11:07 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
