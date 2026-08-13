# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_11:23:41_UTC-green)

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

**Latest saved flight:** 2026-08-13 11:23:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-13 11:23:41 UTC

- **191,896** saved flights
- **60,469** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **191,896** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,295,899.1 tonnes** estimated CO2 emissions
- **133,095,598 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7619 |
| 2 | SkyWest Airlines | 6935 |
| 3 | EJA | 3785 |
| 4 | IndiGo | 3330 |
| 5 | Southwest Airlines | 2994 |
| 6 | American Airlines | 2974 |
| 7 | ENY | 2375 |
| 8 | Delta Air Lines | 2256 |
| 9 | LATAM Airlines | 1797 |
| 10 | AZU | 1730 |
| 11 | Lufthansa | 1667 |
| 12 | Vueling | 1597 |
| 13 | WIF | 1589 |
| 14 | LXJ | 1505 |
| 15 | easyJet | 1322 |
| 16 | Swiss International | 1303 |
| 17 | AXM | 1258 |
| 18 | QLK | 1186 |
| 19 | EJU | 1185 |
| 20 | All Nippon Airways | 1165 |
| 21 | Alaska Airlines | 1144 |
| 22 | VIV | 1057 |
| 23 | GLO | 1033 |
| 24 | Air France | 1003 |
| 25 | PGT | 993 |
| 26 | CXK | 983 |
| 27 | AEE | 982 |
| 28 | United Airlines | 977 |
| 29 | WMT | 953 |
| 30 | Wizz Air | 952 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 163383 |
| 2 | 🇪🇸 ES | 12357 |
| 3 | 🇧🇷 BR | 11016 |
| 4 | 🇦🇺 AU | 10804 |
| 5 | 🇨🇦 CA | 10514 |
| 6 | 🇮🇳 IN | 10429 |
| 7 | 🇮🇹 IT | 9989 |
| 8 | 🇩🇪 DE | 9492 |
| 9 | 🇬🇧 GB | 8954 |
| 10 | 🇯🇵 JP | 7870 |
| 11 | 🇫🇷 FR | 7671 |
| 12 | 🇨🇴 CO | 7385 |
| 13 | 🇬🇷 GR | 5602 |
| 14 | 🇲🇽 MX | 5426 |
| 15 | 🇨🇭 CH | 5150 |
| 16 | 🇹🇷 TR | 5146 |
| 17 | 🇳🇴 NO | 4930 |
| 18 | 🇲🇾 MY | 3294 |
| 19 | 🇿🇦 ZA | 3242 |
| 20 | 🇵🇱 PL | 3167 |
| 21 | 🇹🇭 TH | 2972 |
| 22 | 🇳🇿 NZ | 2708 |
| 23 | 🇵🇭 PH | 2536 |
| 24 | 🇬🇹 GT | 2424 |
| 25 | 🇰🇷 KR | 2347 |
| 26 | 🇭🇷 HR | 1978 |
| 27 | 🇲🇦 MA | 1945 |
| 28 | 🇳🇱 NL | 1718 |
| 29 | 🇲🇪 ME | 1686 |
| 30 | 🇮🇩 ID | 1549 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3983 |
| 2 | Denver International Airport |  | US | 3143 |
| 3 | Tokyo International Airport |  | JP | 2419 |
| 4 | Guaymaral Airport |  | CO | 2365 |
| 5 | Indira Gandhi International Airport |  | IN | 2349 |
| 6 | Harry Reid International Airport |  | US | 2229 |
| 7 | Zurich Airport |  | CH | 2034 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2029 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1982 |
| 10 | La Aurora Airport |  | GT | 1862 |
| 11 | El Dorado International Airport |  | CO | 1733 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1731 |
| 13 | Salt Lake City International Airport |  | US | 1710 |
| 14 | Chicago O'Hare International Airport |  | US | 1680 |
| 15 | Frankfurt am Main International Airport |  | DE | 1629 |
| 16 | Congonhas Airport |  | BR | 1603 |
| 17 | Macau International Airport |  | MO | 1527 |
| 18 | Madrid Barajas International Airport |  | ES | 1510 |
| 19 | Capua Airport |  | IT | 1484 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1483 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1416 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1375 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1342 |
| 24 | Malpensa International Airport |  | IT | 1325 |
| 25 | Charles de Gaulle International Airport |  | FR | 1316 |
| 26 | Charlotte/Douglas International Airport |  | US | 1278 |
| 27 | Bengaluru International Airport |  | IN | 1232 |
| 28 | Kuala Lumpur International Airport |  | MY | 1231 |
| 29 | Ninoy Aquino International Airport |  | PH | 1199 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1198 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1177 |
| 32 | Barcelona International Airport |  | ES | 1147 |
| 33 | Viracopos International Airport |  | BR | 1113 |
| 34 | Seattle-Tacoma International Airport |  | US | 1104 |
| 35 | Reno/Tahoe International Airport |  | US | 1097 |
| 36 | Calgary International Airport |  | CA | 1097 |
| 37 | Daniel K Inouye International Airport |  | US | 1078 |
| 38 | Oslo Gardermoen Airport |  | NO | 1076 |
| 39 | Tenerife Norte Airport |  | ES | 1054 |
| 40 | Vitoria/Foronda Airport |  | ES | 1043 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 976 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 706 | 21m | 244 km | 2,972.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 468 | 1h 7m | 770 km | 6,217.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 445 | 24m | 225 km | 1,726.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 445 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 334 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 322 | 27m | 275 km | 1,525.8 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 309 | 14m | 114 km | 606.0 t |
| 9 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 306 | 8m | - | - |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 285 | 44m | 241 km | 1,183.8 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 276 | 1h 49m | 1,423 km | 6,773.5 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 276 | 22m | 55 km | 262.3 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 257 | 20m | 250 km | 1,110.1 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 240 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 239 | 27m | 215 km | 885.2 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 234 | 19m | 99 km | 400.8 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 234 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 233 | 1h 15m | 961 km | 3,862.1 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 231 | 24m | 218 km | 870.3 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 228 | 19m | 144 km | 567.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 226 | 1h 38m | 1,156 km | 4,508.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 220 | 31m | 369 km | 1,400.4 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 208 | 1h 48m | 1,304 km | 4,679.5 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 207 | 28m | 152 km | 541.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| YRZEF | YRZ | Baneasa International Airport (LRBS) | Baneasa International Airport (LRBS) | 2026-08-13 11:03 UTC | 2026-08-13 11:23 UTC | 20m |
| UFX63 | UFX | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-08-13 10:31 UTC | 2026-08-13 11:05 UTC | 33m |
| ZKHUP | ZKH | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-08-13 10:41 UTC | 2026-08-13 10:57 UTC | 15m |
| HYD164 | HYD | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Val-d'Or Airport (CYVO) | 2026-08-13 10:03 UTC | 2026-08-13 10:51 UTC | 48m |
| UZT | UZT | Melbourne Moorabbin Airport (YMMB) | Albury Airport (YMAY) | 2026-08-13 09:18 UTC | 2026-08-13 10:40 UTC | 1h 22m |
| RYS5029 | RYS | John Paul II International Airport Kraków-Balice Airport (EPKK) | Antalya International Airport (LTAI) | 2026-08-13 08:22 UTC | 2026-08-13 10:36 UTC | 2h 14m |
| FNA570 | FNA | Reykjavik Airport (BIRK) | Hrafnseyri Airport (BIHS) | 2026-08-13 10:03 UTC | 2026-08-13 10:30 UTC | 26m |
| VOE65ND | VOE | Asturias Airport (LEAS) | Valencia Airport (LEVC) | 2026-08-13 09:24 UTC | 2026-08-13 10:28 UTC | 1h 3m |
| EIN55G | Aer Lingus | Lyon Saint-Exupery Airport (LFLL) | Dublin Airport (EIDW) | 2026-08-13 08:37 UTC | 2026-08-13 10:28 UTC | 1h 50m |
| BHA615 | BHA | Tribhuvan International Airport (VNKT) | Tribhuvan International Airport (VNKT) | 2026-08-13 10:19 UTC | 2026-08-13 10:27 UTC | 8m |
| GOLDN61 | GOL | Lisbon Portela Airport (LPPT) | Madeira Airport (LPMA) | 2026-08-13 08:55 UTC | 2026-08-13 10:26 UTC | 1h 31m |
| TUTOR983 | TUT | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-13 09:57 UTC | 2026-08-13 10:24 UTC | 27m |
| RGA10 | RGA | Reichenbach Air Base (LSGR) | Muenster Aero Airport (LSPU) | 2026-08-13 10:14 UTC | 2026-08-13 10:24 UTC | 9m |
| INOST | INO | Torino / Aeritalia Airport (LIMA) | Sollieres Sardieres Airport (LFKD) | 2026-08-13 10:10 UTC | 2026-08-13 10:21 UTC | 11m |
| MCK311 | MCK | Salzburg Airport (LOWS) | St Stephan Airport (LSTS) | 2026-08-13 09:37 UTC | 2026-08-13 10:20 UTC | 43m |
| FSF120A | FSF | La Mole Airport (LFTZ) | Sondrio Caiolo Airport (LILO) | 2026-08-13 09:07 UTC | 2026-08-13 10:19 UTC | 1h 12m |
| TUTOR862 | TUT | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-13 09:53 UTC | 2026-08-13 10:19 UTC | 25m |
| CHX22 | CHX | Gerstetten Airport (EDPT) | Erbach Airport (EDNE) | 2026-08-13 10:08 UTC | 2026-08-13 10:14 UTC | 5m |
| RYR71JD | Ryanair | Nantes Atlantique Airport (LFRS) | Fes Sefrou Airport (GMFU) | 2026-08-13 08:19 UTC | 2026-08-13 10:14 UTC | 1h 54m |
| LHX6UW | LHX | Munich International Airport (EDDM) | Caransebes Airport (LRCS) | 2026-08-13 09:17 UTC | 2026-08-13 10:13 UTC | 56m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
