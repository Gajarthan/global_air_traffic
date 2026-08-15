# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_23:24:59_UTC-green)

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

**Latest saved flight:** 2026-08-15 23:24:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-15 23:24:59 UTC

- **200,188** saved flights
- **62,453** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **200,188** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,391,721.6 tonnes** estimated CO2 emissions
- **138,650,528 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7974 |
| 2 | SkyWest Airlines | 7209 |
| 3 | EJA | 3926 |
| 4 | IndiGo | 3446 |
| 5 | Southwest Airlines | 3102 |
| 6 | American Airlines | 3092 |
| 7 | ENY | 2481 |
| 8 | Delta Air Lines | 2371 |
| 9 | LATAM Airlines | 1891 |
| 10 | AZU | 1824 |
| 11 | Lufthansa | 1708 |
| 12 | Vueling | 1682 |
| 13 | WIF | 1640 |
| 14 | LXJ | 1590 |
| 15 | easyJet | 1382 |
| 16 | Swiss International | 1349 |
| 17 | AXM | 1308 |
| 18 | EJU | 1240 |
| 19 | QLK | 1226 |
| 20 | All Nippon Airways | 1208 |
| 21 | Alaska Airlines | 1176 |
| 22 | VIV | 1112 |
| 23 | GLO | 1089 |
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
| 1 | 🇺🇸 US | 169730 |
| 2 | 🇪🇸 ES | 12934 |
| 3 | 🇧🇷 BR | 11570 |
| 4 | 🇦🇺 AU | 11156 |
| 5 | 🇨🇦 CA | 10956 |
| 6 | 🇮🇳 IN | 10764 |
| 7 | 🇮🇹 IT | 10507 |
| 8 | 🇩🇪 DE | 9925 |
| 9 | 🇬🇧 GB | 9397 |
| 10 | 🇯🇵 JP | 8162 |
| 11 | 🇨🇴 CO | 8016 |
| 12 | 🇫🇷 FR | 7989 |
| 13 | 🇬🇷 GR | 5906 |
| 14 | 🇲🇽 MX | 5680 |
| 15 | 🇹🇷 TR | 5575 |
| 16 | 🇨🇭 CH | 5414 |
| 17 | 🇳🇴 NO | 5077 |
| 18 | 🇲🇾 MY | 3428 |
| 19 | 🇿🇦 ZA | 3370 |
| 20 | 🇵🇱 PL | 3307 |
| 21 | 🇹🇭 TH | 3131 |
| 22 | 🇳🇿 NZ | 2778 |
| 23 | 🇵🇭 PH | 2649 |
| 24 | 🇬🇹 GT | 2552 |
| 25 | 🇰🇷 KR | 2422 |
| 26 | 🇭🇷 HR | 2137 |
| 27 | 🇲🇦 MA | 2029 |
| 28 | 🇳🇱 NL | 1798 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1633 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4187 |
| 2 | Denver International Airport |  | US | 3256 |
| 3 | Tokyo International Airport |  | JP | 2496 |
| 4 | Guaymaral Airport |  | CO | 2474 |
| 5 | Indira Gandhi International Airport |  | IN | 2441 |
| 6 | Harry Reid International Airport |  | US | 2278 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2115 |
| 8 | Zurich Airport |  | CH | 2109 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2073 |
| 10 | La Aurora Airport |  | GT | 1955 |
| 11 | El Dorado International Airport |  | CO | 1852 |
| 12 | Salt Lake City International Airport |  | US | 1781 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1780 |
| 14 | Chicago O'Hare International Airport |  | US | 1765 |
| 15 | Congonhas Airport |  | BR | 1692 |
| 16 | Frankfurt am Main International Airport |  | DE | 1681 |
| 17 | Madrid Barajas International Airport |  | ES | 1579 |
| 18 | Capua Airport |  | IT | 1539 |
| 19 | Macau International Airport |  | MO | 1536 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1519 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1475 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1453 |
| 23 | Malpensa International Airport |  | IT | 1398 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1385 |
| 25 | Charles de Gaulle International Airport |  | FR | 1376 |
| 26 | Charlotte/Douglas International Airport |  | US | 1319 |
| 27 | Kuala Lumpur International Airport |  | MY | 1276 |
| 28 | Bengaluru International Airport |  | IN | 1256 |
| 29 | Ninoy Aquino International Airport |  | PH | 1253 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1252 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1221 |
| 32 | Barcelona International Airport |  | ES | 1206 |
| 33 | Viracopos International Airport |  | BR | 1170 |
| 34 | Seattle-Tacoma International Airport |  | US | 1152 |
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
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 466 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 465 | 24m | 225 km | 1,804.0 t |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 383 | 8m | - | - |
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
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 219 | 1h 48m | 1,304 km | 4,926.9 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 216 | 1h 3m | 695 km | 2,589.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N |  | Iruma Air Base (RJTJ) | Tokyo International Airport (RJTT) | 2026-08-15 23:03 UTC | 2026-08-15 23:24 UTC | 21m |
| N40NR |  | Concord Municipal Airport (KCON) | Concord Municipal Airport (KCON) | 2026-08-15 22:11 UTC | 2026-08-15 23:14 UTC | 1h 2m |
| SD3 |  | 52TA (52TA) | Tri-County Aerodrome (48TX) | 2026-08-15 21:07 UTC | 2026-08-15 23:14 UTC | 2h 6m |
| N118RF |  | Sacramento Mather Airport (KMHR) | Susanville Municipal Airport (KSVE) | 2026-08-15 17:02 UTC | 2026-08-15 23:09 UTC | 6h 6m |
| N233S |  | Desert Creek Airport (NV97) | Desert Creek Airport (NV97) | 2026-08-15 22:15 UTC | 2026-08-15 23:04 UTC | 48m |
| N609MW |  | NV13 (NV13) | Farias Wheel Airport (NV33) | 2026-08-15 22:45 UTC | 2026-08-15 23:03 UTC | 18m |
| AUB164 | AUB | Auburn University Regional Airport (KAUO) | Auburn University Regional Airport (KAUO) | 2026-08-15 22:44 UTC | 2026-08-15 22:59 UTC | 15m |
| N748MK |  | Schuylkill County/Joe Zerbey Airport (KZER) | Sunbury Airport (K71N) | 2026-08-15 22:09 UTC | 2026-08-15 22:58 UTC | 48m |
| TKR180 | TKR | WN36 (WN36) | Port Field (WS87) | 2026-08-15 22:18 UTC | 2026-08-15 22:47 UTC | 28m |
| N8144V |  | Seattle Paine Field International Airport (KPAE) | Arlington Municipal Airport (KAWO) | 2026-08-15 22:40 UTC | 2026-08-15 22:45 UTC | 5m |
| TKR186 | TKR | Wilson Creek Airport (K5W1) | 0WN9 (0WN9) | 2026-08-15 22:31 UTC | 2026-08-15 22:43 UTC | 12m |
| XBJYP | XBJ | Hermanos Serdan International Airport (MMPB) | Ingeniero Juan Guillermo Villasana Airport (MMPC) | 2026-08-15 22:06 UTC | 2026-08-15 22:42 UTC | 36m |
| TKR184 | TKR | Grant County International Airport (KMWH) | 0WN9 (0WN9) | 2026-08-15 22:29 UTC | 2026-08-15 22:42 UTC | 12m |
| SKW3262 | SkyWest Airlines | Portland International Airport (KPDX) | Spokane International Airport (KGEG) | 2026-08-15 21:54 UTC | 2026-08-15 22:40 UTC | 46m |
| N423BB |  | Aurora State Airport (KUAO) | Pangborn Memorial Airport (KEAT) | 2026-08-15 22:07 UTC | 2026-08-15 22:39 UTC | 32m |
| N38EE |  | Sweetwater (Usmc) Airport (NV72) | Desert Creek Airport (NV97) | 2026-08-15 20:52 UTC | 2026-08-15 22:35 UTC | 1h 43m |
| VOI3532 | VOI | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 2026-08-15 20:43 UTC | 2026-08-15 22:30 UTC | 1h 47m |
| N529NG |  | Erie Municipal Airport (KEIK) | Granby-Grand County Airport (KGNB) | 2026-08-15 16:21 UTC | 2026-08-15 22:27 UTC | 6h 6m |
| AAL1832 | American Airlines | Dallas-Fort Worth International Airport (KDFW) | Denver International Airport (KDEN) | 2026-08-15 20:18 UTC | 2026-08-15 22:24 UTC | 2h 5m |
| N426RB |  | Haskell Airport (K2K9) | Haskell Airport (K2K9) | 2026-08-15 22:19 UTC | 2026-08-15 22:23 UTC | 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
