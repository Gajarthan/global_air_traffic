# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_17:42:26_UTC-green)

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

**Latest saved flight:** 2026-04-15 17:42:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-15 17:42:26 UTC

- **36,269** saved flights
- **15,843** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **36,269** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **439,389.7 tonnes** estimated CO2 emissions
- **25,471,865 km** total distance flown
- **840 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1550 |
| 2 | SkyWest Airlines | 1428 |
| 3 | IndiGo | 906 |
| 4 | EJA | 618 |
| 5 | American Airlines | 613 |
| 6 | Southwest Airlines | 510 |
| 7 | ENY | 477 |
| 8 | AXM | 386 |
| 9 | Lufthansa | 383 |
| 10 | LATAM Airlines | 369 |
| 11 | Vueling | 368 |
| 12 | AZU | 323 |
| 13 | All Nippon Airways | 321 |
| 14 | Delta Air Lines | 303 |
| 15 | QLK | 302 |
| 16 | LXJ | 287 |
| 17 | Swiss International | 276 |
| 18 | WIF | 269 |
| 19 | AEE | 246 |
| 20 | easyJet | 240 |
| 21 | Alaska Airlines | 237 |
| 22 | EJU | 236 |
| 23 | VIV | 231 |
| 24 | Japan Airlines | 222 |
| 25 | Air France | 208 |
| 26 | EDV | 203 |
| 27 | United Airlines | 199 |
| 28 | GLO | 196 |
| 29 | AIQ | 191 |
| 30 | JetBlue | 191 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 28379 |
| 2 | 🇮🇳 IN | 2770 |
| 3 | 🇪🇸 ES | 2706 |
| 4 | 🇦🇺 AU | 2549 |
| 5 | 🇧🇷 BR | 2145 |
| 6 | 🇯🇵 JP | 1968 |
| 7 | 🇮🇹 IT | 1945 |
| 8 | 🇩🇪 DE | 1872 |
| 9 | 🇨🇴 CO | 1784 |
| 10 | 🇨🇦 CA | 1760 |
| 11 | 🇬🇧 GB | 1501 |
| 12 | 🇫🇷 FR | 1373 |
| 13 | 🇲🇽 MX | 1137 |
| 14 | 🇬🇷 GR | 1102 |
| 15 | 🇨🇭 CH | 1003 |
| 16 | 🇲🇾 MY | 930 |
| 17 | 🇳🇴 NO | 880 |
| 18 | 🇳🇿 NZ | 772 |
| 19 | 🇿🇦 ZA | 770 |
| 20 | 🇵🇭 PH | 687 |
| 21 | 🇹🇭 TH | 669 |
| 22 | 🇹🇷 TR | 661 |
| 23 | 🇬🇹 GT | 620 |
| 24 | 🇰🇷 KR | 611 |
| 25 | 🇵🇱 PL | 568 |
| 26 | 🇲🇦 MA | 454 |
| 27 | 🇳🇱 NL | 363 |
| 28 | 🇧🇸 BS | 352 |
| 29 | 🇲🇪 ME | 351 |
| 30 | 🇮🇩 ID | 345 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 854 |
| 2 | Tokyo International Airport |  | JP | 667 |
| 3 | El Dorado International Airport |  | CO | 635 |
| 4 | Denver International Airport |  | US | 607 |
| 5 | Indira Gandhi International Airport |  | IN | 588 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 542 |
| 7 | Harry Reid International Airport |  | US | 475 |
| 8 | La Aurora Airport |  | GT | 455 |
| 9 | Zurich Airport |  | CH | 448 |
| 10 | Guaymaral Airport |  | CO | 448 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 365 |
| 12 | Kuala Lumpur International Airport |  | MY | 361 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 360 |
| 14 | Chicago O'Hare International Airport |  | US | 358 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 345 |
| 16 | Frankfurt am Main International Airport |  | DE | 339 |
| 17 | Madrid Barajas International Airport |  | ES | 327 |
| 18 | Tenerife Norte Airport |  | ES | 324 |
| 19 | Charlotte/Douglas International Airport |  | US | 323 |
| 20 | Bengaluru International Airport |  | IN | 323 |
| 21 | Macau International Airport |  | MO | 322 |
| 22 | Congonhas Airport |  | BR | 321 |
| 23 | Ninoy Aquino International Airport |  | PH | 318 |
| 24 | Malpensa International Airport |  | IT | 296 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 283 |
| 26 | Daniel K Inouye International Airport |  | US | 272 |
| 27 | Charles de Gaulle International Airport |  | FR | 272 |
| 28 | Salt Lake City International Airport |  | US | 271 |
| 29 | Capua Airport |  | IT | 262 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 256 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 255 |
| 32 | Reno/Tahoe International Airport |  | US | 251 |
| 33 | O. R. Tambo International Airport |  | ZA | 248 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 247 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 239 |
| 36 | Vitoria/Foronda Airport |  | ES | 238 |
| 37 | Barcelona International Airport |  | ES | 237 |
| 38 | Viracopos International Airport |  | BR | 227 |
| 39 | Don Mueang International Airport |  | TH | 226 |
| 40 | Seattle-Tacoma International Airport |  | US | 224 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 176 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 168 | 1h 8m | 706 km | 2,045.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 147 | 14m | 114 km | 288.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 134 | 24m | 225 km | 519.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 104 | 1h 27m | 910 km | 1,632.0 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 96 | 19m | 165 km | 273.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 91 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 87 | 9m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 86 | 21m | 244 km | 362.1 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 78 | 27m | 275 km | 369.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 78 | 21m | 99 km | 133.6 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 75 | 1h 11m | 770 km | 996.3 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 69 | 31m | 369 km | 439.2 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 68 | 45m | 452 km | 530.0 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 61 | 20m | 147 km | 154.4 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 60 | 52m | 556 km | 575.1 t |
| 22 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 56 | 13m | 99 km | 96.0 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 53 | 1h 41m | 1,423 km | 1,300.7 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 53 | 16m | 162 km | 148.6 t |
| 28 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 52 | 26m | 215 km | 192.6 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 51 | 1h 20m | 961 km | 845.4 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 51 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-04-15 16:01 UTC | 2026-04-15 17:42 UTC | 1h 41m |
| AFL1219 | AFL | Sheremetyevo International Airport (UUEE) | Sheremetyevo International Airport (UUEE) | 2026-04-15 13:21 UTC | 2026-04-15 17:31 UTC | 4h 10m |
| THNDR03 | THN | RAF Kinloss (EGQK) | RAF Lossiemouth (EGQS) | 2026-04-15 13:01 UTC | 2026-04-15 17:30 UTC | 4h 28m |
| N445B |  | Doylestown Airport (KDYL) | Doylestown Airport (KDYL) | 2026-04-15 16:32 UTC | 2026-04-15 17:27 UTC | 55m |
| N3909Q |  | 2FL8 (2FL8) | Bent Willies Airport (52FA) | 2026-04-15 17:13 UTC | 2026-04-15 17:25 UTC | 11m |
| RDHK765 | RDH | Felker Army Air Field (KFAF) | Norfolk Ns (Chambers Field) Airport (KNGU) | 2026-04-15 16:50 UTC | 2026-04-15 17:19 UTC | 29m |
| N474F |  | Rimrock Airport (48AZ) | Telluride Regional Airport (KTEX) | 2026-04-15 15:15 UTC | 2026-04-15 17:18 UTC | 2h 2m |
| N5QD |  | 0PA0 (0PA0) | Gunden Airport (PS54) | 2026-04-15 17:16 UTC | 2026-04-15 17:17 UTC | 1m |
| N9994R |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-04-15 16:58 UTC | 2026-04-15 17:16 UTC | 18m |
| N697ND |  | Brookings Regional Airport (KBKX) | Brookings Regional Airport (KBKX) | 2026-04-15 16:28 UTC | 2026-04-15 17:14 UTC | 46m |
| N281MG |  | Henderson Executive Airport (KHND) | Mesquite Airport (K67L) | 2026-04-15 16:41 UTC | 2026-04-15 17:10 UTC | 28m |
| N116TU |  | Corona Municipal Airport (KAJO) | Riverside Airport (KRAL) | 2026-04-15 16:13 UTC | 2026-04-15 17:06 UTC | 52m |
| N5676V |  | Gillespie Field (KSEE) | Gillespie Field (KSEE) | 2026-04-15 17:04 UTC | 2026-04-15 17:05 UTC | 1m |
| LXJ448 | LXJ | Casper/Natrona County International Airport (KCPR) | Van Nuys Airport (KVNY) | 2026-04-15 15:04 UTC | 2026-04-15 17:05 UTC | 2h 0m |
| N194TS |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-04-15 16:48 UTC | 2026-04-15 17:05 UTC | 17m |
| N66HC |  | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-04-15 16:56 UTC | 2026-04-15 17:02 UTC | 6m |
| N688WG |  | Chino Airport (KCNO) | Big Bear City Airport (KL35) | 2026-04-15 16:45 UTC | 2026-04-15 17:01 UTC | 16m |
| N1545Y |  | San Gabriel Valley Airport (KEMT) | Big Bear City Airport (KL35) | 2026-04-15 16:38 UTC | 2026-04-15 17:00 UTC | 22m |
| OAL084 | OAL | Thessaloniki Macedonia International Airport (LGTS) | Olimboi Airport (LG56) | 2026-04-15 16:10 UTC | 2026-04-15 16:59 UTC | 48m |
| CHX1 | CHX | Vogtareuth Airport (EDNV) | Oberschleisheim Airfield (EDNX) | 2026-04-15 16:48 UTC | 2026-04-15 16:58 UTC | 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
