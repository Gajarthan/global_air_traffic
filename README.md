# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_13:41:06_UTC-green)

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

**Latest saved flight:** 2026-08-13 13:41:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-13 13:41:06 UTC

- **192,159** saved flights
- **60,511** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **192,159** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,298,324.3 tonnes** estimated CO2 emissions
- **133,236,192 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7628 |
| 2 | SkyWest Airlines | 6936 |
| 3 | EJA | 3785 |
| 4 | IndiGo | 3335 |
| 5 | Southwest Airlines | 2994 |
| 6 | American Airlines | 2974 |
| 7 | ENY | 2375 |
| 8 | Delta Air Lines | 2256 |
| 9 | LATAM Airlines | 1801 |
| 10 | AZU | 1736 |
| 11 | Lufthansa | 1669 |
| 12 | Vueling | 1601 |
| 13 | WIF | 1593 |
| 14 | LXJ | 1509 |
| 15 | easyJet | 1322 |
| 16 | Swiss International | 1305 |
| 17 | AXM | 1258 |
| 18 | EJU | 1186 |
| 19 | QLK | 1186 |
| 20 | All Nippon Airways | 1168 |
| 21 | Alaska Airlines | 1144 |
| 22 | VIV | 1057 |
| 23 | GLO | 1034 |
| 24 | Air France | 1004 |
| 25 | PGT | 996 |
| 26 | CXK | 984 |
| 27 | AEE | 983 |
| 28 | United Airlines | 978 |
| 29 | WMT | 956 |
| 30 | Wizz Air | 953 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 163486 |
| 2 | 🇪🇸 ES | 12390 |
| 3 | 🇧🇷 BR | 11045 |
| 4 | 🇦🇺 AU | 10810 |
| 5 | 🇨🇦 CA | 10519 |
| 6 | 🇮🇳 IN | 10443 |
| 7 | 🇮🇹 IT | 9999 |
| 8 | 🇩🇪 DE | 9514 |
| 9 | 🇬🇧 GB | 8975 |
| 10 | 🇯🇵 JP | 7884 |
| 11 | 🇫🇷 FR | 7682 |
| 12 | 🇨🇴 CO | 7413 |
| 13 | 🇬🇷 GR | 5609 |
| 14 | 🇲🇽 MX | 5428 |
| 15 | 🇨🇭 CH | 5173 |
| 16 | 🇹🇷 TR | 5159 |
| 17 | 🇳🇴 NO | 4940 |
| 18 | 🇲🇾 MY | 3297 |
| 19 | 🇿🇦 ZA | 3252 |
| 20 | 🇵🇱 PL | 3173 |
| 21 | 🇹🇭 TH | 2982 |
| 22 | 🇳🇿 NZ | 2710 |
| 23 | 🇵🇭 PH | 2536 |
| 24 | 🇬🇹 GT | 2432 |
| 25 | 🇰🇷 KR | 2349 |
| 26 | 🇭🇷 HR | 1986 |
| 27 | 🇲🇦 MA | 1951 |
| 28 | 🇳🇱 NL | 1724 |
| 29 | 🇲🇪 ME | 1686 |
| 30 | 🇮🇩 ID | 1554 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3983 |
| 2 | Denver International Airport |  | US | 3146 |
| 3 | Tokyo International Airport |  | JP | 2424 |
| 4 | Guaymaral Airport |  | CO | 2374 |
| 5 | Indira Gandhi International Airport |  | IN | 2353 |
| 6 | Harry Reid International Airport |  | US | 2234 |
| 7 | Zurich Airport |  | CH | 2039 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2030 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1982 |
| 10 | La Aurora Airport |  | GT | 1867 |
| 11 | El Dorado International Airport |  | CO | 1741 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1731 |
| 13 | Salt Lake City International Airport |  | US | 1710 |
| 14 | Chicago O'Hare International Airport |  | US | 1680 |
| 15 | Frankfurt am Main International Airport |  | DE | 1633 |
| 16 | Congonhas Airport |  | BR | 1605 |
| 17 | Macau International Airport |  | MO | 1528 |
| 18 | Madrid Barajas International Airport |  | ES | 1514 |
| 19 | Capua Airport |  | IT | 1484 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1483 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1416 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1379 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1342 |
| 24 | Malpensa International Airport |  | IT | 1326 |
| 25 | Charles de Gaulle International Airport |  | FR | 1318 |
| 26 | Charlotte/Douglas International Airport |  | US | 1278 |
| 27 | Bengaluru International Airport |  | IN | 1233 |
| 28 | Kuala Lumpur International Airport |  | MY | 1231 |
| 29 | Ninoy Aquino International Airport |  | PH | 1199 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1198 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1177 |
| 32 | Barcelona International Airport |  | ES | 1148 |
| 33 | Viracopos International Airport |  | BR | 1118 |
| 34 | Seattle-Tacoma International Airport |  | US | 1104 |
| 35 | Calgary International Airport |  | CA | 1098 |
| 36 | Reno/Tahoe International Airport |  | US | 1097 |
| 37 | Oslo Gardermoen Airport |  | NO | 1080 |
| 38 | Daniel K Inouye International Airport |  | US | 1079 |
| 39 | Tenerife Norte Airport |  | ES | 1056 |
| 40 | Vitoria/Foronda Airport |  | ES | 1049 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 980 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 707 | 21m | 244 km | 2,977.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 469 | 1h 7m | 770 km | 6,230.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 446 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 445 | 24m | 225 km | 1,726.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 334 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 322 | 27m | 275 km | 1,525.8 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 309 | 14m | 114 km | 606.0 t |
| 9 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 307 | 8m | - | - |
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
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 233 | 1h 15m | 961 km | 3,862.1 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 232 | 24m | 218 km | 874.0 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 228 | 19m | 144 km | 567.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 227 | 1h 38m | 1,156 km | 4,528.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 220 | 31m | 369 km | 1,400.4 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 208 | 1h 48m | 1,304 km | 4,679.5 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 207 | 28m | 152 km | 541.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DKAJA | DKA | Muenster Aero Airport (LSPU) | Muenster Aero Airport (LSPU) | 2026-08-13 11:07 UTC | 2026-08-13 13:41 UTC | 2h 33m |
| N229SF |  | Jim Pettijohn Memorial Airport (7OK8) | Tinker Afb Airport (KTIK) | 2026-08-13 13:23 UTC | 2026-08-13 13:40 UTC | 17m |
| DKYCK | DKY | EDJG (EDJG) | EDJG (EDJG) | 2026-08-13 13:37 UTC | 2026-08-13 13:38 UTC | 1m |
| HBZVU | HBZ | St Stephan Airport (LSTS) | Raron Airport (LSTA) | 2026-08-13 13:20 UTC | 2026-08-13 13:38 UTC | 17m |
| AIP1842 | AIP | Denver International Airport (KDEN) | 1CO7 (1CO7) | 2026-08-13 12:55 UTC | 2026-08-13 13:34 UTC | 39m |
| SMOKN71 | SMO | 2TX3 (2TX3) | Benson Airstrip (2XS8) | 2026-08-13 13:11 UTC | 2026-08-13 13:33 UTC | 22m |
| WWIND228 | WWI | RAF Mona (EGOQ) | Caernarfon Airport (EGCK) | 2026-08-13 13:05 UTC | 2026-08-13 13:29 UTC | 23m |
| N78385 |  | Earl L Small Jr  Field/Stockmar Airport (20GA) | West Georgia Regional/O V Gray Field (KCTJ) | 2026-08-13 12:53 UTC | 2026-08-13 13:25 UTC | 31m |
| N5679U |  | Newnan Coweta County Airport (KCCO) | Roosevelt Memorial Airport (K5A9) | 2026-08-13 12:58 UTC | 2026-08-13 13:25 UTC | 26m |
| GZR614 | GZR | Linate Airport (LIML) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-13 12:32 UTC | 2026-08-13 13:23 UTC | 50m |
| RAM981E | Royal Air Maroc | Lisbon Portela Airport (LPPT) | Mohammed V International Airport (GMMN) | 2026-08-13 12:28 UTC | 2026-08-13 13:18 UTC | 49m |
| GIMAB | GIM | RAF Lossiemouth (EGQS) | RAF Lossiemouth (EGQS) | 2026-08-13 13:05 UTC | 2026-08-13 13:17 UTC | 11m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-08-13 13:09 UTC | 2026-08-13 13:16 UTC | 7m |
| LXJ422 | LXJ | Lehigh Valley International Airport (KABE) | Lehigh Valley International Airport (KABE) | 2026-08-13 13:14 UTC | 2026-08-13 13:16 UTC | 1m |
| N216PC |  | Los Alamos Airport (KLAM) | NM74 (NM74) | 2026-08-13 12:41 UTC | 2026-08-13 13:16 UTC | 34m |
| N395SS |  | Washington Dulles International Airport (KIAD) | 8NK3 (8NK3) | 2026-08-13 12:10 UTC | 2026-08-13 13:15 UTC | 1h 5m |
| N800FV |  | Kennett Memorial Airport (KTKX) | 1AR0 (1AR0) | 2026-08-13 12:29 UTC | 2026-08-13 13:15 UTC | 45m |
| N715LL |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-08-13 13:08 UTC | 2026-08-13 13:13 UTC | 5m |
| N218LG |  | MY19 (MY19) | The Sigurd Anderson Airport (K1D7) | 2026-08-13 12:47 UTC | 2026-08-13 13:10 UTC | 23m |
| LTG8514 | LTG | Brussels Airport (EBBR) | Brussels Airport (EBBR) | 2026-08-13 11:54 UTC | 2026-08-13 13:07 UTC | 1h 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
