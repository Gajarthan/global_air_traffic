# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_13:00:22_UTC-green)

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

**Latest saved flight:** 2026-08-09 13:00:22 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 13:00:22 UTC

- **180,973** saved flights
- **57,844** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **180,973** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,175,723.1 tonnes** estimated CO2 emissions
- **126,128,874 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7172 |
| 2 | SkyWest Airlines | 6582 |
| 3 | EJA | 3555 |
| 4 | IndiGo | 3176 |
| 5 | Southwest Airlines | 2840 |
| 6 | American Airlines | 2818 |
| 7 | ENY | 2250 |
| 8 | Delta Air Lines | 2142 |
| 9 | LATAM Airlines | 1683 |
| 10 | AZU | 1616 |
| 11 | Lufthansa | 1611 |
| 12 | Vueling | 1500 |
| 13 | WIF | 1499 |
| 14 | LXJ | 1407 |
| 15 | easyJet | 1239 |
| 16 | Swiss International | 1235 |
| 17 | AXM | 1226 |
| 18 | QLK | 1116 |
| 19 | All Nippon Airways | 1107 |
| 20 | EJU | 1107 |
| 21 | Alaska Airlines | 1097 |
| 22 | VIV | 997 |
| 23 | GLO | 965 |
| 24 | Cathay Pacific | 947 |
| 25 | CXK | 947 |
| 26 | AEE | 946 |
| 27 | Air France | 937 |
| 28 | United Airlines | 929 |
| 29 | PGT | 909 |
| 30 | MXY | 905 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 154760 |
| 2 | 🇪🇸 ES | 11651 |
| 3 | 🇧🇷 BR | 10360 |
| 4 | 🇦🇺 AU | 10200 |
| 5 | 🇮🇳 IN | 9957 |
| 6 | 🇨🇦 CA | 9854 |
| 7 | 🇮🇹 IT | 9366 |
| 8 | 🇩🇪 DE | 8964 |
| 9 | 🇬🇧 GB | 8369 |
| 10 | 🇯🇵 JP | 7378 |
| 11 | 🇫🇷 FR | 7210 |
| 12 | 🇨🇴 CO | 6710 |
| 13 | 🇬🇷 GR | 5302 |
| 14 | 🇲🇽 MX | 5166 |
| 15 | 🇨🇭 CH | 4833 |
| 16 | 🇳🇴 NO | 4663 |
| 17 | 🇹🇷 TR | 4657 |
| 18 | 🇲🇾 MY | 3195 |
| 19 | 🇵🇱 PL | 3042 |
| 20 | 🇿🇦 ZA | 2978 |
| 21 | 🇹🇭 TH | 2783 |
| 22 | 🇳🇿 NZ | 2608 |
| 23 | 🇵🇭 PH | 2404 |
| 24 | 🇬🇹 GT | 2294 |
| 25 | 🇰🇷 KR | 2263 |
| 26 | 🇲🇦 MA | 1823 |
| 27 | 🇭🇷 HR | 1804 |
| 28 | 🇲🇪 ME | 1643 |
| 29 | 🇳🇱 NL | 1628 |
| 30 | 🇲🇴 MO | 1516 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3733 |
| 2 | Denver International Airport |  | US | 2987 |
| 3 | Tokyo International Airport |  | JP | 2287 |
| 4 | Indira Gandhi International Airport |  | IN | 2225 |
| 5 | Guaymaral Airport |  | CO | 2224 |
| 6 | Harry Reid International Airport |  | US | 2127 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1949 |
| 8 | Zurich Airport |  | CH | 1928 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1878 |
| 10 | La Aurora Airport |  | GT | 1762 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1648 |
| 12 | Chicago O'Hare International Airport |  | US | 1626 |
| 13 | Salt Lake City International Airport |  | US | 1616 |
| 14 | El Dorado International Airport |  | CO | 1612 |
| 15 | Frankfurt am Main International Airport |  | DE | 1574 |
| 16 | Macau International Airport |  | MO | 1516 |
| 17 | Congonhas Airport |  | BR | 1503 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1437 |
| 19 | Madrid Barajas International Airport |  | ES | 1423 |
| 20 | Capua Airport |  | IT | 1416 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1351 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1287 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1270 |
| 24 | Malpensa International Airport |  | IT | 1248 |
| 25 | Charles de Gaulle International Airport |  | FR | 1232 |
| 26 | Charlotte/Douglas International Airport |  | US | 1224 |
| 27 | Kuala Lumpur International Airport |  | MY | 1201 |
| 28 | Bengaluru International Airport |  | IN | 1180 |
| 29 | Ninoy Aquino International Airport |  | PH | 1133 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1123 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1109 |
| 32 | Barcelona International Airport |  | ES | 1077 |
| 33 | Daniel K Inouye International Airport |  | US | 1041 |
| 34 | Seattle-Tacoma International Airport |  | US | 1041 |
| 35 | Viracopos International Airport |  | BR | 1038 |
| 36 | Reno/Tahoe International Airport |  | US | 1032 |
| 37 | Calgary International Airport |  | CA | 1030 |
| 38 | Oslo Gardermoen Airport |  | NO | 1002 |
| 39 | Tenerife Norte Airport |  | ES | 992 |
| 40 | Vitoria/Foronda Airport |  | ES | 980 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 918 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 670 | 21m | 244 km | 2,821.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 434 | 1h 8m | 770 km | 5,765.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 428 | 24m | 225 km | 1,660.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 417 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 305 | 27m | 275 km | 1,445.3 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 298 | 1h 7m | 706 km | 3,628.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 271 | 44m | 241 km | 1,125.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 254 | 1h 48m | 1,423 km | 6,233.6 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 241 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 239 | 20m | 250 km | 1,032.3 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 228 | 26m | 215 km | 844.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 221 | 19m | 99 km | 378.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 219 | 31m | 49 km | 185.1 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 219 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 218 | 1h 15m | 961 km | 3,613.5 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 218 | 50m | 556 km | 2,089.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 216 | 19m | 144 km | 537.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 213 | 1h 38m | 1,156 km | 4,249.3 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 211 | 31m | 369 km | 1,343.1 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 210 | 24m | 218 km | 791.2 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 203 | 28m | 152 km | 530.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 197 | 1h 1m | 695 km | 2,361.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N567R |  | Blue Grass Airport (KLEX) | Cynthiana-Harrison County Airport (K0I8) | 2026-08-09 12:35 UTC | 2026-08-09 13:00 UTC | 24m |
| N43MJ |  | Flying W Airport (KN14) | Flying W Airport (KN14) | 2026-08-09 12:33 UTC | 2026-08-09 12:48 UTC | 15m |
| TRP7 | TRP | Robinson Airport (MD14) | Joint Base Andrews Airport (KADW) | 2026-08-09 12:32 UTC | 2026-08-09 12:45 UTC | 12m |
| PA |  | Ptuj Airport (LJPT) | Ptuj Airport (LJPT) | 2026-08-09 12:26 UTC | 2026-08-09 12:44 UTC | 18m |
| N779SA |  | Rocky Mountain Metro Airport (KBJC) | Erie Municipal Airport (KEIK) | 2026-08-09 12:22 UTC | 2026-08-09 12:43 UTC | 21m |
| N9721N |  | Brighton Airport (K45G) | Lenawee County Airport (KADG) | 2026-08-09 11:03 UTC | 2026-08-09 12:43 UTC | 1h 40m |
| N228DT |  | Gibbs Field (03OH) | 02OH (02OH) | 2026-08-09 11:53 UTC | 2026-08-09 12:36 UTC | 42m |
| PSHFH | PSH | Estancia Santana Airport (SWER) | Porto dos Gauchos Airport (SWPG) | 2026-08-09 11:23 UTC | 2026-08-09 12:29 UTC | 1h 5m |
| N654FL |  | Skyhaven Airport (KDAW) | Salmon Falls Airport (ME61) | 2026-08-09 12:27 UTC | 2026-08-09 12:27 UTC | 0m |
| CXK1104 | CXK | St Pete-Clearwater International Airport (KPIE) | St Pete-Clearwater International Airport (KPIE) | 2026-08-09 12:09 UTC | 2026-08-09 12:20 UTC | 11m |
| DFPTF | DFP | Tannheim Airport (EDMT) | Tannheim Airport (EDMT) | 2026-08-09 11:56 UTC | 2026-08-09 12:17 UTC | 21m |
| SEH6JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Chania International Airport (LGSA) | 2026-08-09 11:47 UTC | 2026-08-09 12:14 UTC | 27m |
| S5DOT |  | Novo Mesto Airport (LJNM) | Novo Mesto Airport (LJNM) | 2026-08-09 11:56 UTC | 2026-08-09 12:13 UTC | 17m |
| INOST | INO | Torino / Aeritalia Airport (LIMA) | Torino / Aeritalia Airport (LIMA) | 2026-08-09 12:02 UTC | 2026-08-09 12:12 UTC | 9m |
| AFR34MZ | Air France | Charles de Gaulle International Airport (LFPG) | Zurich Airport (LSZH) | 2026-08-09 11:14 UTC | 2026-08-09 12:11 UTC | 57m |
| AFL2126 | AFL | Batumi International Airport (UGSB) | Isparta Airport (LTBM) | 2026-08-09 10:38 UTC | 2026-08-09 12:11 UTC | 1h 32m |
| CHX29 | CHX | Hamburg Airport (EDDH) | Luneburg Airport (EDHG) | 2026-08-09 11:53 UTC | 2026-08-09 12:11 UTC | 18m |
| ASL77B | ASL | Belgrade Nikola Tesla Airport (LYBE) | Vienna International Airport (LOWW) | 2026-08-09 10:56 UTC | 2026-08-09 12:10 UTC | 1h 14m |
| AAL2782 | American Airlines | Indianapolis International Airport (KIND) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-09 10:26 UTC | 2026-08-09 12:09 UTC | 1h 43m |
| DKFGF | DKF | EDJG (EDJG) | Mauterndorf Airport (LOSM) | 2026-08-09 10:50 UTC | 2026-08-09 12:09 UTC | 1h 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
