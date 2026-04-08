# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_22:59:09_UTC-green)

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

**Latest saved flight:** 2026-04-08 22:59:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-08 22:59:09 UTC

- **24,271** saved flights
- **11,756** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **24,271** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **300,113.4 tonnes** estimated CO2 emissions
- **17,397,881 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1012 |
| 2 | Ryanair | 1000 |
| 3 | IndiGo | 666 |
| 4 | American Airlines | 445 |
| 5 | EJA | 442 |
| 6 | Southwest Airlines | 350 |
| 7 | ENY | 320 |
| 8 | Lufthansa | 308 |
| 9 | Vueling | 250 |
| 10 | AXM | 244 |
| 11 | LATAM Airlines | 243 |
| 12 | QLK | 219 |
| 13 | All Nippon Airways | 218 |
| 14 | Delta Air Lines | 207 |
| 15 | LXJ | 197 |
| 16 | AZU | 191 |
| 17 | Swiss International | 174 |
| 18 | Alaska Airlines | 165 |
| 19 | Japan Airlines | 162 |
| 20 | VIV | 162 |
| 21 | easyJet | 161 |
| 22 | EJU | 156 |
| 23 | AEE | 151 |
| 24 | WIF | 150 |
| 25 | United Airlines | 148 |
| 26 | Avianca | 143 |
| 27 | EDV | 143 |
| 28 | AXB | 138 |
| 29 | Air France | 125 |
| 30 | ANZ | 125 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 19104 |
| 2 | 🇮🇳 IN | 2031 |
| 3 | 🇪🇸 ES | 1831 |
| 4 | 🇦🇺 AU | 1782 |
| 5 | 🇧🇷 BR | 1359 |
| 6 | 🇯🇵 JP | 1355 |
| 7 | 🇨🇴 CO | 1240 |
| 8 | 🇩🇪 DE | 1233 |
| 9 | 🇮🇹 IT | 1231 |
| 10 | 🇨🇦 CA | 1116 |
| 11 | 🇬🇧 GB | 981 |
| 12 | 🇫🇷 FR | 891 |
| 13 | 🇲🇽 MX | 777 |
| 14 | 🇬🇷 GR | 690 |
| 15 | 🇨🇭 CH | 664 |
| 16 | 🇲🇾 MY | 577 |
| 17 | 🇳🇿 NZ | 523 |
| 18 | 🇳🇴 NO | 517 |
| 19 | 🇿🇦 ZA | 516 |
| 20 | 🇬🇹 GT | 480 |
| 21 | 🇹🇷 TR | 465 |
| 22 | 🇵🇭 PH | 451 |
| 23 | 🇰🇷 KR | 428 |
| 24 | 🇹🇭 TH | 390 |
| 25 | 🇵🇱 PL | 357 |
| 26 | 🇲🇦 MA | 295 |
| 27 | 🇮🇩 ID | 251 |
| 28 | 🇧🇸 BS | 251 |
| 29 | 🇲🇪 ME | 250 |
| 30 | 🇳🇱 NL | 239 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 580 |
| 2 | El Dorado International Airport |  | CO | 459 |
| 3 | Tokyo International Airport |  | JP | 449 |
| 4 | Denver International Airport |  | US | 425 |
| 5 | Indira Gandhi International Airport |  | IN | 419 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 336 |
| 7 | La Aurora Airport |  | GT | 331 |
| 8 | Harry Reid International Airport |  | US | 320 |
| 9 | Zurich Airport |  | CH | 287 |
| 10 | Frankfurt am Main International Airport |  | DE | 263 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 258 |
| 12 | Guaymaral Airport |  | CO | 257 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 252 |
| 14 | Chicago O'Hare International Airport |  | US | 251 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 247 |
| 16 | Macau International Airport |  | MO | 236 |
| 17 | Charlotte/Douglas International Airport |  | US | 228 |
| 18 | Bengaluru International Airport |  | IN | 228 |
| 19 | Madrid Barajas International Airport |  | ES | 211 |
| 20 | Kuala Lumpur International Airport |  | MY | 211 |
| 21 | Tenerife Norte Airport |  | ES | 209 |
| 22 | Ninoy Aquino International Airport |  | PH | 208 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 197 |
| 24 | Malpensa International Airport |  | IT | 196 |
| 25 | Congonhas Airport |  | BR | 195 |
| 26 | Salt Lake City International Airport |  | US | 190 |
| 27 | Daniel K Inouye International Airport |  | US | 184 |
| 28 | Reno/Tahoe International Airport |  | US | 184 |
| 29 | Charles de Gaulle International Airport |  | FR | 175 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 171 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 170 |
| 32 | Miami International Airport |  | US | 164 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 163 |
| 34 | O. R. Tambo International Airport |  | ZA | 161 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 160 |
| 36 | Pune Airport |  | IN | 158 |
| 37 | Seattle-Tacoma International Airport |  | US | 156 |
| 38 | Barcelona International Airport |  | ES | 155 |
| 39 | Vitoria/Foronda Airport |  | ES | 154 |
| 40 | Calgary International Airport |  | CA | 143 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 114 | 1h 8m | 706 km | 1,388.0 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 100 | 14m | 114 km | 196.1 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 95 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 90 | 24m | 225 km | 349.2 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 84 | 28m | 304 km | 440.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 70 | 1h 27m | 910 km | 1,098.5 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 70 | 22m | 99 km | 119.9 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 67 | 27m | 152 km | 175.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 66 | 1h 42m | 1,156 km | 1,316.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 58 | 19m | 165 km | 165.0 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 52 | 55m | 546 km | 489.6 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 52 | 1h 13m | 770 km | 690.8 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 49 | 27m | 275 km | 232.2 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 47 | 31m | 369 km | 299.2 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 47 | 52m | 556 km | 450.5 t |
| 19 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 44 | 46m | 452 km | 342.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 44 | 20m | 250 km | 190.1 t |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 43 | 4m | - | - |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 43 | 9m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 41 | 1h 43m | 1,423 km | 1,006.2 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 40 | 13m | 99 km | 68.6 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 36 | 20m | 147 km | 91.1 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 36 | 12m | 15 km | 9.5 t |
| 29 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 34 | 1h 21m | 961 km | 563.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TRP2 | TRP | Maryland Airport (K2W5) | Joint Base Andrews Airport (KADW) | 2026-04-08 22:50 UTC | 2026-04-08 22:59 UTC | 8m |
| N4025F |  | Windy Tales Airport (TX34) | 27XA (27XA) | 2026-04-08 22:44 UTC | 2026-04-08 22:55 UTC | 10m |
| DHX852 | DHX | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-04-08 06:57 UTC | 2026-04-08 22:52 UTC | 15h 55m |
| N365CV |  | Firebaugh Airport (KF34) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-08 22:20 UTC | 2026-04-08 22:52 UTC | 31m |
| BOE511 | BOE | Renton Municipal Airport (KRNT) | Othello Municipal Airport (KS70) | 2026-04-08 21:02 UTC | 2026-04-08 22:51 UTC | 1h 48m |
| CPA640 | Cathay Pacific | Thamkharka Airport (VNTH) | Macau International Airport (VMMC) | 2026-04-08 19:54 UTC | 2026-04-08 22:48 UTC | 2h 54m |
| N15102 |  | Sutter County Airport (KO52) | Sutter County Airport (KO52) | 2026-04-08 22:29 UTC | 2026-04-08 22:44 UTC | 15m |
| RUDY36 | RUD | North Island Nas (Halsey Field) Airport (KNZY) | Camp Pendleton Mcas (Munn Field) Airport (KNFG) | 2026-04-08 22:09 UTC | 2026-04-08 22:44 UTC | 34m |
| N8366N |  | Laconia Municipal Airport (KLCI) | Westerly State Airport (KWST) | 2026-04-08 21:22 UTC | 2026-04-08 22:41 UTC | 1h 19m |
| SWT2CW | SWT | Copernicus Wrocław Airport (EPWR) | Bergneustadt/Auf dem Dumpel Airport (EDKF) | 2026-04-08 20:43 UTC | 2026-04-08 22:36 UTC | 1h 53m |
| N831X |  | Roberts Field (KRDM) | Dry Creek Airpark (OG21) | 2026-04-08 22:17 UTC | 2026-04-08 22:34 UTC | 16m |
| CPA372 | Cathay Pacific | Madrid Barajas International Airport (LEMD) | Macau International Airport (VMMC) | 2026-04-08 10:41 UTC | 2026-04-08 22:30 UTC | 11h 49m |
| JANET09 | JAN | Trona Airport (KL72) | Boron Airstrip (57CL) | 2026-04-08 22:16 UTC | 2026-04-08 22:28 UTC | 11m |
| N996TA |  | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-04-08 21:54 UTC | 2026-04-08 22:28 UTC | 33m |
| N222LX |  | Van Nuys Airport (KVNY) | Glen-Aspen Airport (4CO0) | 2026-04-08 21:07 UTC | 2026-04-08 22:27 UTC | 1h 20m |
| ASA1082 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-04-08 22:04 UTC | 2026-04-08 22:25 UTC | 21m |
| N6182A |  | Bolingbrook's Clow International Airport (K1C5) | Eldon Model Airpark (KH79) | 2026-04-08 21:12 UTC | 2026-04-08 22:24 UTC | 1h 11m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-08 22:13 UTC | 2026-04-08 22:24 UTC | 10m |
| RENO71 | REN | 75OK (75OK) | Good Life Ranch Airport (17OK) | 2026-04-08 21:57 UTC | 2026-04-08 22:23 UTC | 26m |
| N601RC |  | Tucson International Airport (KTUS) | Walter's Camp Airport (CN98) | 2026-04-08 19:51 UTC | 2026-04-08 22:23 UTC | 2h 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
