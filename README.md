# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_14:57:23_UTC-green)

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

**Latest saved flight:** 2026-08-13 14:57:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-13 14:57:23 UTC

- **192,341** saved flights
- **60,557** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **192,341** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,300,251.6 tonnes** estimated CO2 emissions
- **133,347,918 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7641 |
| 2 | SkyWest Airlines | 6938 |
| 3 | EJA | 3788 |
| 4 | IndiGo | 3336 |
| 5 | Southwest Airlines | 2997 |
| 6 | American Airlines | 2975 |
| 7 | ENY | 2376 |
| 8 | Delta Air Lines | 2262 |
| 9 | LATAM Airlines | 1804 |
| 10 | AZU | 1737 |
| 11 | Lufthansa | 1669 |
| 12 | Vueling | 1603 |
| 13 | WIF | 1593 |
| 14 | LXJ | 1512 |
| 15 | easyJet | 1322 |
| 16 | Swiss International | 1306 |
| 17 | AXM | 1258 |
| 18 | EJU | 1186 |
| 19 | QLK | 1186 |
| 20 | All Nippon Airways | 1168 |
| 21 | Alaska Airlines | 1144 |
| 22 | VIV | 1058 |
| 23 | GLO | 1034 |
| 24 | Air France | 1005 |
| 25 | PGT | 996 |
| 26 | CXK | 985 |
| 27 | AEE | 984 |
| 28 | United Airlines | 979 |
| 29 | WMT | 957 |
| 30 | Wizz Air | 955 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 163642 |
| 2 | 🇪🇸 ES | 12405 |
| 3 | 🇧🇷 BR | 11055 |
| 4 | 🇦🇺 AU | 10810 |
| 5 | 🇨🇦 CA | 10531 |
| 6 | 🇮🇳 IN | 10448 |
| 7 | 🇮🇹 IT | 10006 |
| 8 | 🇩🇪 DE | 9527 |
| 9 | 🇬🇧 GB | 8987 |
| 10 | 🇯🇵 JP | 7884 |
| 11 | 🇫🇷 FR | 7690 |
| 12 | 🇨🇴 CO | 7429 |
| 13 | 🇬🇷 GR | 5620 |
| 14 | 🇲🇽 MX | 5436 |
| 15 | 🇨🇭 CH | 5179 |
| 16 | 🇹🇷 TR | 5163 |
| 17 | 🇳🇴 NO | 4941 |
| 18 | 🇲🇾 MY | 3297 |
| 19 | 🇿🇦 ZA | 3256 |
| 20 | 🇵🇱 PL | 3177 |
| 21 | 🇹🇭 TH | 2985 |
| 22 | 🇳🇿 NZ | 2710 |
| 23 | 🇵🇭 PH | 2536 |
| 24 | 🇬🇹 GT | 2433 |
| 25 | 🇰🇷 KR | 2349 |
| 26 | 🇭🇷 HR | 1988 |
| 27 | 🇲🇦 MA | 1952 |
| 28 | 🇳🇱 NL | 1725 |
| 29 | 🇲🇪 ME | 1686 |
| 30 | 🇮🇩 ID | 1556 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3985 |
| 2 | Denver International Airport |  | US | 3148 |
| 3 | Tokyo International Airport |  | JP | 2424 |
| 4 | Guaymaral Airport |  | CO | 2380 |
| 5 | Indira Gandhi International Airport |  | IN | 2354 |
| 6 | Harry Reid International Airport |  | US | 2235 |
| 7 | Zurich Airport |  | CH | 2040 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2031 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1984 |
| 10 | La Aurora Airport |  | GT | 1868 |
| 11 | El Dorado International Airport |  | CO | 1744 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1731 |
| 13 | Salt Lake City International Airport |  | US | 1712 |
| 14 | Chicago O'Hare International Airport |  | US | 1681 |
| 15 | Frankfurt am Main International Airport |  | DE | 1634 |
| 16 | Congonhas Airport |  | BR | 1607 |
| 17 | Macau International Airport |  | MO | 1528 |
| 18 | Madrid Barajas International Airport |  | ES | 1515 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1484 |
| 20 | Capua Airport |  | IT | 1484 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1417 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1379 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1342 |
| 24 | Malpensa International Airport |  | IT | 1327 |
| 25 | Charles de Gaulle International Airport |  | FR | 1319 |
| 26 | Charlotte/Douglas International Airport |  | US | 1278 |
| 27 | Bengaluru International Airport |  | IN | 1235 |
| 28 | Kuala Lumpur International Airport |  | MY | 1231 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1201 |
| 30 | Ninoy Aquino International Airport |  | PH | 1199 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1179 |
| 32 | Barcelona International Airport |  | ES | 1150 |
| 33 | Viracopos International Airport |  | BR | 1118 |
| 34 | Seattle-Tacoma International Airport |  | US | 1106 |
| 35 | Calgary International Airport |  | CA | 1100 |
| 36 | Reno/Tahoe International Airport |  | US | 1098 |
| 37 | Oslo Gardermoen Airport |  | NO | 1081 |
| 38 | Daniel K Inouye International Airport |  | US | 1079 |
| 39 | Tenerife Norte Airport |  | ES | 1057 |
| 40 | Vitoria/Foronda Airport |  | ES | 1051 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 983 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 707 | 21m | 244 km | 2,977.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 469 | 1h 7m | 770 km | 6,230.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 446 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 445 | 24m | 225 km | 1,726.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 334 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 323 | 27m | 275 km | 1,530.6 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 309 | 14m | 114 km | 606.0 t |
| 9 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 309 | 8m | - | - |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 286 | 44m | 241 km | 1,188.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 277 | 1h 49m | 1,423 km | 6,798.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 276 | 22m | 55 km | 262.3 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 259 | 20m | 250 km | 1,118.7 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 241 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 239 | 27m | 215 km | 885.2 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 235 | 19m | 99 km | 402.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 234 | 12m | - | - |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 233 | 24m | 218 km | 877.8 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 233 | 1h 15m | 961 km | 3,862.1 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 228 | 19m | 144 km | 567.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 227 | 1h 38m | 1,156 km | 4,528.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 220 | 31m | 369 km | 1,400.4 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 208 | 1h 48m | 1,304 km | 4,679.5 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 208 | 28m | 152 km | 543.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N407AP |  | Lake Tahoe Airport (KTVL) | Alpine County Airport (KM45) | 2026-08-13 14:31 UTC | 2026-08-13 14:57 UTC | 26m |
| DFOLE | DFO | Hasfurt-Schweinfurt Airport (EDQT) | Hasfurt-Schweinfurt Airport (EDQT) | 2026-08-13 14:31 UTC | 2026-08-13 14:52 UTC | 21m |
| N1831T |  | Addison Airport (KADS) | Commerce Municipal Airport (K2F7) | 2026-08-13 14:17 UTC | 2026-08-13 14:50 UTC | 32m |
| DAL1731 | Delta Air Lines | Denver International Airport (KDEN) | Seattle-Tacoma International Airport (KSEA) | 2026-08-13 12:30 UTC | 2026-08-13 14:50 UTC | 2h 20m |
| SCX281 | SCX | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Boeing Field/King County International Airport (KBFI) | 2026-08-13 11:23 UTC | 2026-08-13 14:50 UTC | 3h 27m |
| CSZ308 | CSZ | Suvarnabhumi Airport (VTBS) | Zhuhai Airport (ZGSD) | 2026-08-13 12:42 UTC | 2026-08-13 14:50 UTC | 2h 7m |
| CXK471 | CXK | Airnautique, Inc Airport (0GA2) | Airnautique, Inc Airport (0GA2) | 2026-08-13 14:30 UTC | 2026-08-13 14:49 UTC | 19m |
| N33LA |  | Ryan Field (KRYN) | Marana Regional Airport (KAVQ) | 2026-08-13 14:31 UTC | 2026-08-13 14:46 UTC | 15m |
| UPS2971 | UPS | Portland International Airport (KPDX) | Stanford Field (KU12) | 2026-08-13 13:37 UTC | 2026-08-13 14:42 UTC | 1h 4m |
| UAL419 | United Airlines | San Francisco International Airport (KSFO) | Bear Lake County Airport (K1U7) | 2026-08-13 13:25 UTC | 2026-08-13 14:42 UTC | 1h 17m |
| JBU116 | JetBlue | San Francisco International Airport (KSFO) | Melody Ranch Airport (WY31) | 2026-08-13 12:14 UTC | 2026-08-13 14:42 UTC | 2h 27m |
| DAL2987 | Delta Air Lines | Reno/Tahoe International Airport (KRNO) | Afton Lincoln County/General Boyd L Eddins Field (KAFO) | 2026-08-13 13:39 UTC | 2026-08-13 14:42 UTC | 1h 2m |
| N256AA |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-08-13 14:15 UTC | 2026-08-13 14:40 UTC | 25m |
| EIN627 | Aer Lingus | Oslo Gardermoen Airport (ENGM) | Dublin Airport (EIDW) | 2026-08-13 12:36 UTC | 2026-08-13 14:38 UTC | 2h 1m |
| PAT351 | PAT | Nashville International Airport (KBNA) | Austin-Bergstrom International Airport (KAUS) | 2026-08-13 11:45 UTC | 2026-08-13 14:34 UTC | 2h 49m |
| N35XP |  | Spruce Creek Airport (7FL6) | KXFL (KXFL) | 2026-08-13 14:00 UTC | 2026-08-13 14:33 UTC | 33m |
| N423RM |  | Clearwater Executive Airport (KCLW) | Brooksville-Tampa Bay Regional Airport (KBKV) | 2026-08-13 13:59 UTC | 2026-08-13 14:32 UTC | 32m |
| 4XCDE |  | Haifa International Airport (LLHA) | Haifa International Airport (LLHA) | 2026-08-13 14:03 UTC | 2026-08-13 14:30 UTC | 27m |
| N236PS |  | Portland International Airport (KPDX) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-13 13:03 UTC | 2026-08-13 14:30 UTC | 1h 26m |
| N308AJ |  | Tilstock Airfield (EGCT) | Tilstock Airfield (EGCT) | 2026-08-13 13:07 UTC | 2026-08-13 14:28 UTC | 1h 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
