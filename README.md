# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_17:57:41_UTC-green)

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

**Latest saved flight:** 2026-08-13 17:57:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-13 17:57:41 UTC

- **193,008** saved flights
- **60,751** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **193,008** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,307,343.0 tonnes** estimated CO2 emissions
- **133,759,017 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7677 |
| 2 | SkyWest Airlines | 6960 |
| 3 | EJA | 3799 |
| 4 | IndiGo | 3343 |
| 5 | Southwest Airlines | 3008 |
| 6 | American Airlines | 2984 |
| 7 | ENY | 2389 |
| 8 | Delta Air Lines | 2276 |
| 9 | LATAM Airlines | 1811 |
| 10 | AZU | 1741 |
| 11 | Lufthansa | 1672 |
| 12 | Vueling | 1608 |
| 13 | WIF | 1599 |
| 14 | LXJ | 1522 |
| 15 | easyJet | 1329 |
| 16 | Swiss International | 1314 |
| 17 | AXM | 1258 |
| 18 | EJU | 1189 |
| 19 | QLK | 1186 |
| 20 | All Nippon Airways | 1168 |
| 21 | Alaska Airlines | 1145 |
| 22 | VIV | 1062 |
| 23 | GLO | 1038 |
| 24 | Air France | 1009 |
| 25 | PGT | 1001 |
| 26 | AEE | 990 |
| 27 | CXK | 988 |
| 28 | United Airlines | 981 |
| 29 | WMT | 960 |
| 30 | Wizz Air | 959 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 164242 |
| 2 | 🇪🇸 ES | 12463 |
| 3 | 🇧🇷 BR | 11093 |
| 4 | 🇦🇺 AU | 10810 |
| 5 | 🇨🇦 CA | 10562 |
| 6 | 🇮🇳 IN | 10467 |
| 7 | 🇮🇹 IT | 10035 |
| 8 | 🇩🇪 DE | 9569 |
| 9 | 🇬🇧 GB | 9037 |
| 10 | 🇯🇵 JP | 7884 |
| 11 | 🇫🇷 FR | 7718 |
| 12 | 🇨🇴 CO | 7478 |
| 13 | 🇬🇷 GR | 5654 |
| 14 | 🇲🇽 MX | 5448 |
| 15 | 🇨🇭 CH | 5202 |
| 16 | 🇹🇷 TR | 5190 |
| 17 | 🇳🇴 NO | 4956 |
| 18 | 🇲🇾 MY | 3297 |
| 19 | 🇿🇦 ZA | 3264 |
| 20 | 🇵🇱 PL | 3182 |
| 21 | 🇹🇭 TH | 2991 |
| 22 | 🇳🇿 NZ | 2710 |
| 23 | 🇵🇭 PH | 2536 |
| 24 | 🇬🇹 GT | 2451 |
| 25 | 🇰🇷 KR | 2349 |
| 26 | 🇭🇷 HR | 1999 |
| 27 | 🇲🇦 MA | 1960 |
| 28 | 🇳🇱 NL | 1734 |
| 29 | 🇲🇪 ME | 1686 |
| 30 | 🇮🇩 ID | 1556 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4003 |
| 2 | Denver International Airport |  | US | 3160 |
| 3 | Tokyo International Airport |  | JP | 2424 |
| 4 | Guaymaral Airport |  | CO | 2398 |
| 5 | Indira Gandhi International Airport |  | IN | 2358 |
| 6 | Harry Reid International Airport |  | US | 2239 |
| 7 | Zurich Airport |  | CH | 2049 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2040 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1992 |
| 10 | La Aurora Airport |  | GT | 1884 |
| 11 | El Dorado International Airport |  | CO | 1752 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1734 |
| 13 | Salt Lake City International Airport |  | US | 1717 |
| 14 | Chicago O'Hare International Airport |  | US | 1688 |
| 15 | Frankfurt am Main International Airport |  | DE | 1638 |
| 16 | Congonhas Airport |  | BR | 1614 |
| 17 | Macau International Airport |  | MO | 1528 |
| 18 | Madrid Barajas International Airport |  | ES | 1522 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1486 |
| 20 | Capua Airport |  | IT | 1485 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1426 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1385 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1342 |
| 24 | Malpensa International Airport |  | IT | 1333 |
| 25 | Charles de Gaulle International Airport |  | FR | 1324 |
| 26 | Charlotte/Douglas International Airport |  | US | 1287 |
| 27 | Bengaluru International Airport |  | IN | 1236 |
| 28 | Kuala Lumpur International Airport |  | MY | 1231 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1204 |
| 30 | Ninoy Aquino International Airport |  | PH | 1199 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1180 |
| 32 | Barcelona International Airport |  | ES | 1153 |
| 33 | Viracopos International Airport |  | BR | 1120 |
| 34 | Seattle-Tacoma International Airport |  | US | 1106 |
| 35 | Calgary International Airport |  | CA | 1103 |
| 36 | Reno/Tahoe International Airport |  | US | 1102 |
| 37 | Oslo Gardermoen Airport |  | NO | 1085 |
| 38 | Daniel K Inouye International Airport |  | US | 1081 |
| 39 | Tenerife Norte Airport |  | ES | 1060 |
| 40 | Vitoria/Foronda Airport |  | ES | 1056 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 991 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 709 | 21m | 244 km | 2,985.4 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 469 | 1h 7m | 770 km | 6,230.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 451 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 445 | 24m | 225 km | 1,726.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 335 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 325 | 27m | 275 km | 1,540.0 t |
| 8 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 313 | 8m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 309 | 14m | 114 km | 606.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 288 | 44m | 241 km | 1,196.3 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 278 | 1h 49m | 1,423 km | 6,822.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 276 | 22m | 55 km | 262.3 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 259 | 20m | 250 km | 1,118.7 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 241 | 27m | 215 km | 892.6 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 241 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 236 | 19m | 99 km | 404.3 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 235 | 24m | 218 km | 885.3 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 234 | 1h 15m | 961 km | 3,878.7 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 234 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 228 | 19m | 144 km | 567.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 227 | 1h 38m | 1,156 km | 4,528.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 220 | 31m | 369 km | 1,400.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 210 | 28m | 152 km | 548.8 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 208 | 1h 1m | 695 km | 2,493.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N35564 |  | 80WA (80WA) | 1WA9 (1WA9) | 2026-08-13 17:32 UTC | 2026-08-13 17:57 UTC | 25m |
| MSR788 | EgyptAir | Munich International Airport (EDDM) | HE12 (HE12) | 2026-08-13 14:44 UTC | 2026-08-13 17:54 UTC | 3h 10m |
| FFAB123 | FFA | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-13 15:22 UTC | 2026-08-13 17:54 UTC | 2h 32m |
| N611GV |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-08-13 17:22 UTC | 2026-08-13 17:48 UTC | 25m |
| RFS720 | RFS | Auburn Municipal Airport (KS50) | Auburn Municipal Airport (KS50) | 2026-08-13 17:33 UTC | 2026-08-13 17:48 UTC | 14m |
| N611AC |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-08-13 17:32 UTC | 2026-08-13 17:45 UTC | 13m |
| N285AF |  | Dekalb-Peachtree Airport (KPDK) | Pensacola International Airport (KPNS) | 2026-08-13 16:54 UTC | 2026-08-13 17:39 UTC | 44m |
| EJA691 | EJA | Samuels Field (KBRY) | Auburn University Regional Airport (KAUO) | 2026-08-13 16:44 UTC | 2026-08-13 17:37 UTC | 53m |
| N714 |  | Ted Stevens Anchorage International Airport (PANC) | Birchwood Airport (PABV) | 2026-08-13 16:22 UTC | 2026-08-13 17:37 UTC | 1h 14m |
| N373US |  | Melbourne Orlando International Airport (KMLB) | Valkaria Airport (KX59) | 2026-08-13 17:10 UTC | 2026-08-13 17:36 UTC | 25m |
| CO35 |  | Campo Fontenelle Airport (SBYS) | Campo Fontenelle Airport (SBYS) | 2026-08-13 17:24 UTC | 2026-08-13 17:34 UTC | 10m |
| EAU057B | EAU | Palma De Mallorca Airport (LEPA) | London Biggin Hill Airport (EGKB) | 2026-08-13 15:35 UTC | 2026-08-13 17:34 UTC | 1h 58m |
| N20452 |  | Tuscola Area Airport (KCFS) | Saginaw County/H W Browne Airport (KHYX) | 2026-08-13 17:25 UTC | 2026-08-13 17:32 UTC | 7m |
| HBEUQ | HBE | Triengen Airport (LSPN) | Triengen Airport (LSPN) | 2026-08-13 17:08 UTC | 2026-08-13 17:30 UTC | 21m |
| DAH4039 | DAH | Cairo International Airport (HECA) | Houari Boumediene Airport (DAAG) | 2026-08-13 13:59 UTC | 2026-08-13 17:25 UTC | 3h 25m |
| BOE368 | BOE | Boeing Field/King County International Airport (KBFI) | Othello Municipal Airport (KS70) | 2026-08-13 16:12 UTC | 2026-08-13 17:24 UTC | 1h 11m |
| BULET12 | BUL | Bob Maxwell Memorial Airfield (KOKB) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-13 17:02 UTC | 2026-08-13 17:24 UTC | 21m |
| N4593Y |  | Boulder Municipal Airport (KBDU) | Boulder Municipal Airport (KBDU) | 2026-08-13 17:07 UTC | 2026-08-13 17:23 UTC | 15m |
| N300PL |  | Roseau Municipal/Rudy Billberg Field (KROX) | Anoka County/Blaine (Janes Field) Airport (KANE) | 2026-08-13 16:28 UTC | 2026-08-13 17:19 UTC | 51m |
| N603BS |  | Manchester Boston Regional Airport (KMHT) | Laconia Municipal Airport (KLCI) | 2026-08-13 16:56 UTC | 2026-08-13 17:18 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
