# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_17:06:00_UTC-green)

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

**Latest saved flight:** 2026-08-15 17:06:00 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-15 17:06:00 UTC

- **199,163** saved flights
- **62,221** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **199,163** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,378,601.5 tonnes** estimated CO2 emissions
- **137,889,944 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7927 |
| 2 | SkyWest Airlines | 7134 |
| 3 | EJA | 3905 |
| 4 | IndiGo | 3445 |
| 5 | Southwest Airlines | 3078 |
| 6 | American Airlines | 3060 |
| 7 | ENY | 2456 |
| 8 | Delta Air Lines | 2356 |
| 9 | LATAM Airlines | 1875 |
| 10 | AZU | 1810 |
| 11 | Lufthansa | 1702 |
| 12 | Vueling | 1675 |
| 13 | WIF | 1639 |
| 14 | LXJ | 1580 |
| 15 | easyJet | 1367 |
| 16 | Swiss International | 1346 |
| 17 | AXM | 1308 |
| 18 | EJU | 1233 |
| 19 | QLK | 1225 |
| 20 | All Nippon Airways | 1208 |
| 21 | Alaska Airlines | 1174 |
| 22 | VIV | 1099 |
| 23 | GLO | 1083 |
| 24 | Air France | 1056 |
| 25 | PGT | 1050 |
| 26 | AEE | 1027 |
| 27 | United Airlines | 1009 |
| 28 | CXK | 1008 |
| 29 | WMT | 1006 |
| 30 | Wizz Air | 986 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 168734 |
| 2 | 🇪🇸 ES | 12870 |
| 3 | 🇧🇷 BR | 11496 |
| 4 | 🇦🇺 AU | 11148 |
| 5 | 🇨🇦 CA | 10880 |
| 6 | 🇮🇳 IN | 10762 |
| 7 | 🇮🇹 IT | 10449 |
| 8 | 🇩🇪 DE | 9886 |
| 9 | 🇬🇧 GB | 9361 |
| 10 | 🇯🇵 JP | 8160 |
| 11 | 🇫🇷 FR | 7939 |
| 12 | 🇨🇴 CO | 7893 |
| 13 | 🇬🇷 GR | 5879 |
| 14 | 🇲🇽 MX | 5624 |
| 15 | 🇹🇷 TR | 5514 |
| 16 | 🇨🇭 CH | 5401 |
| 17 | 🇳🇴 NO | 5073 |
| 18 | 🇲🇾 MY | 3428 |
| 19 | 🇿🇦 ZA | 3366 |
| 20 | 🇵🇱 PL | 3296 |
| 21 | 🇹🇭 TH | 3131 |
| 22 | 🇳🇿 NZ | 2772 |
| 23 | 🇵🇭 PH | 2639 |
| 24 | 🇬🇹 GT | 2546 |
| 25 | 🇰🇷 KR | 2419 |
| 26 | 🇭🇷 HR | 2115 |
| 27 | 🇲🇦 MA | 2019 |
| 28 | 🇳🇱 NL | 1792 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1633 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4136 |
| 2 | Denver International Airport |  | US | 3232 |
| 3 | Tokyo International Airport |  | JP | 2495 |
| 4 | Guaymaral Airport |  | CO | 2459 |
| 5 | Indira Gandhi International Airport |  | IN | 2440 |
| 6 | Harry Reid International Airport |  | US | 2270 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2107 |
| 8 | Zurich Airport |  | CH | 2106 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2060 |
| 10 | La Aurora Airport |  | GT | 1950 |
| 11 | El Dorado International Airport |  | CO | 1832 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1767 |
| 13 | Salt Lake City International Airport |  | US | 1765 |
| 14 | Chicago O'Hare International Airport |  | US | 1742 |
| 15 | Congonhas Airport |  | BR | 1683 |
| 16 | Frankfurt am Main International Airport |  | DE | 1676 |
| 17 | Madrid Barajas International Airport |  | ES | 1567 |
| 18 | Macau International Airport |  | MO | 1536 |
| 19 | Capua Airport |  | IT | 1527 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1511 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1463 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1439 |
| 23 | Malpensa International Airport |  | IT | 1388 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1382 |
| 25 | Charles de Gaulle International Airport |  | FR | 1371 |
| 26 | Charlotte/Douglas International Airport |  | US | 1313 |
| 27 | Kuala Lumpur International Airport |  | MY | 1276 |
| 28 | Bengaluru International Airport |  | IN | 1256 |
| 29 | Ninoy Aquino International Airport |  | PH | 1248 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1243 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1214 |
| 32 | Barcelona International Airport |  | ES | 1200 |
| 33 | Viracopos International Airport |  | BR | 1162 |
| 34 | Seattle-Tacoma International Airport |  | US | 1140 |
| 35 | Calgary International Airport |  | CA | 1127 |
| 36 | Reno/Tahoe International Airport |  | US | 1120 |
| 37 | Oslo Gardermoen Airport |  | NO | 1118 |
| 38 | Vitoria/Foronda Airport |  | ES | 1103 |
| 39 | Daniel K Inouye International Airport |  | US | 1102 |
| 40 | Tenerife Norte Airport |  | ES | 1092 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1013 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 488 | 1h 7m | 770 km | 6,482.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 465 | 24m | 225 km | 1,804.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 465 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 367 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 341 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 336 | 27m | 275 km | 1,592.2 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 307 | 1h 7m | 706 km | 3,737.7 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 299 | 44m | 241 km | 1,242.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 291 | 1h 49m | 1,423 km | 7,141.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 284 | 22m | 55 km | 269.9 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 262 | 21m | 250 km | 1,131.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 249 | 24m | 218 km | 938.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 248 | 26m | 215 km | 918.5 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 244 | 13m | - | - |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 244 | 19m | 99 km | 418.0 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 243 | 1h 14m | 961 km | 4,027.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 238 | 1h 37m | 1,156 km | 4,748.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 233 | 19m | 144 km | 579.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 225 | 31m | 369 km | 1,432.2 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 216 | 1h 3m | 695 km | 2,589.2 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 216 | 28m | 152 km | 564.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SD3 |  | 52TA (52TA) | Tri-County Aerodrome (48TX) | 2026-08-15 16:02 UTC | 2026-08-15 17:06 UTC | 1h 3m |
| N4511E |  | Reno/Tahoe International Airport (KRNO) | Reno/Tahoe International Airport (KRNO) | 2026-08-15 16:36 UTC | 2026-08-15 17:05 UTC | 29m |
| MSR752 | EgyptAir | Budapest Ferenc Liszt International Airport (LHBP) | HE12 (HE12) | 2026-08-15 14:27 UTC | 2026-08-15 17:02 UTC | 2h 35m |
| N758PH |  | San Gabriel Valley Airport (KEMT) | San Gabriel Valley Airport (KEMT) | 2026-08-15 16:43 UTC | 2026-08-15 17:00 UTC | 16m |
| N139TJ |  | NJ64 (NJ64) | Wings Field (KLOM) | 2026-08-15 16:37 UTC | 2026-08-15 16:58 UTC | 20m |
| N628SR |  | San Carlos Airport (KSQL) | Truckee-Tahoe Airport (KTRK) | 2026-08-15 16:19 UTC | 2026-08-15 16:56 UTC | 36m |
| ASB060 | ASB | Crawford Bay Airport (CAR2) | Penticton Airport (CYYF) | 2026-08-15 15:55 UTC | 2026-08-15 16:49 UTC | 53m |
| N245MG |  | Santa Fe Regional Airport (KSAF) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-15 16:07 UTC | 2026-08-15 16:48 UTC | 41m |
| N6309B |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-08-15 16:35 UTC | 2026-08-15 16:46 UTC | 11m |
| N9086K |  | Carson City Airport (KCXP) | Lake Tahoe Airport (KTVL) | 2026-08-15 16:26 UTC | 2026-08-15 16:46 UTC | 19m |
| CWA928 | CWA | Edmonton International Airport (CYEG) | Glendon Airport (CFP5) | 2026-08-15 16:18 UTC | 2026-08-15 16:45 UTC | 26m |
| N1317T |  | K4A7 (K4A7) | Thomaston-Upson County Airport (KOPN) | 2026-08-15 16:13 UTC | 2026-08-15 16:45 UTC | 31m |
| LXJ602 | LXJ | Luis Munoz Marin International Airport (TJSJ) | St Pete-Clearwater International Airport (KPIE) | 2026-08-15 14:09 UTC | 2026-08-15 16:44 UTC | 2h 34m |
| N2369X |  | Pompano Beach Airpark (KPMP) | Pompano Beach Airpark (KPMP) | 2026-08-15 15:50 UTC | 2026-08-15 16:43 UTC | 53m |
| N3294W |  | Pompano Beach Airpark (KPMP) | Pompano Beach Airpark (KPMP) | 2026-08-15 16:38 UTC | 2026-08-15 16:42 UTC | 3m |
| N41599 |  | Baton Rouge Metro, Ryan Field (KBTR) | MS28 (MS28) | 2026-08-15 16:16 UTC | 2026-08-15 16:40 UTC | 23m |
| PPMPB | PPM | Santos Dumont Airport (SBRJ) | SNAO (SNAO) | 2026-08-15 16:23 UTC | 2026-08-15 16:39 UTC | 16m |
| FLE601 | FLE | Toronto Pearson International Airport (CYYZ) | Vancouver International Airport (CYVR) | 2026-08-15 11:49 UTC | 2026-08-15 16:39 UTC | 4h 49m |
| N95KW |  | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-08-15 16:31 UTC | 2026-08-15 16:31 UTC | 0m |
| N4841Y |  | Kelly Air Park (CO15) | Kelly Air Park (CO15) | 2026-08-15 16:26 UTC | 2026-08-15 16:31 UTC | 5m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
