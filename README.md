# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_20:52:23_UTC-green)

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

**Latest saved flight:** 2026-04-15 20:52:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-15 20:52:23 UTC

- **36,570** saved flights
- **15,942** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **36,570** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **442,989.6 tonnes** estimated CO2 emissions
- **25,680,556 km** total distance flown
- **840 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1560 |
| 2 | SkyWest Airlines | 1448 |
| 3 | IndiGo | 906 |
| 4 | EJA | 621 |
| 5 | American Airlines | 619 |
| 6 | Southwest Airlines | 513 |
| 7 | ENY | 483 |
| 8 | AXM | 386 |
| 9 | Lufthansa | 383 |
| 10 | LATAM Airlines | 373 |
| 11 | Vueling | 370 |
| 12 | AZU | 326 |
| 13 | All Nippon Airways | 321 |
| 14 | Delta Air Lines | 311 |
| 15 | QLK | 302 |
| 16 | LXJ | 290 |
| 17 | Swiss International | 277 |
| 18 | WIF | 272 |
| 19 | AEE | 247 |
| 20 | easyJet | 242 |
| 21 | Alaska Airlines | 240 |
| 22 | EJU | 238 |
| 23 | VIV | 232 |
| 24 | Japan Airlines | 222 |
| 25 | Air France | 208 |
| 26 | United Airlines | 205 |
| 27 | EDV | 204 |
| 28 | GLO | 196 |
| 29 | JetBlue | 192 |
| 30 | AIQ | 191 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 28734 |
| 2 | 🇮🇳 IN | 2772 |
| 3 | 🇪🇸 ES | 2729 |
| 4 | 🇦🇺 AU | 2549 |
| 5 | 🇧🇷 BR | 2166 |
| 6 | 🇯🇵 JP | 1968 |
| 7 | 🇮🇹 IT | 1949 |
| 8 | 🇩🇪 DE | 1878 |
| 9 | 🇨🇴 CO | 1808 |
| 10 | 🇨🇦 CA | 1792 |
| 11 | 🇬🇧 GB | 1509 |
| 12 | 🇫🇷 FR | 1386 |
| 13 | 🇲🇽 MX | 1147 |
| 14 | 🇬🇷 GR | 1108 |
| 15 | 🇨🇭 CH | 1004 |
| 16 | 🇲🇾 MY | 930 |
| 17 | 🇳🇴 NO | 884 |
| 18 | 🇳🇿 NZ | 774 |
| 19 | 🇿🇦 ZA | 770 |
| 20 | 🇵🇭 PH | 687 |
| 21 | 🇹🇭 TH | 669 |
| 22 | 🇹🇷 TR | 664 |
| 23 | 🇬🇹 GT | 624 |
| 24 | 🇰🇷 KR | 611 |
| 25 | 🇵🇱 PL | 573 |
| 26 | 🇲🇦 MA | 463 |
| 27 | 🇳🇱 NL | 363 |
| 28 | 🇧🇸 BS | 354 |
| 29 | 🇲🇪 ME | 354 |
| 30 | 🇮🇩 ID | 345 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 867 |
| 2 | Tokyo International Airport |  | JP | 667 |
| 3 | El Dorado International Airport |  | CO | 643 |
| 4 | Denver International Airport |  | US | 622 |
| 5 | Indira Gandhi International Airport |  | IN | 590 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 545 |
| 7 | Harry Reid International Airport |  | US | 480 |
| 8 | Guaymaral Airport |  | CO | 458 |
| 9 | La Aurora Airport |  | GT | 457 |
| 10 | Zurich Airport |  | CH | 449 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 369 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 365 |
| 13 | Chicago O'Hare International Airport |  | US | 361 |
| 14 | Kuala Lumpur International Airport |  | MY | 361 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 345 |
| 16 | Frankfurt am Main International Airport |  | DE | 340 |
| 17 | Madrid Barajas International Airport |  | ES | 332 |
| 18 | Charlotte/Douglas International Airport |  | US | 327 |
| 19 | Macau International Airport |  | MO | 325 |
| 20 | Tenerife Norte Airport |  | ES | 325 |
| 21 | Bengaluru International Airport |  | IN | 323 |
| 22 | Congonhas Airport |  | BR | 322 |
| 23 | Ninoy Aquino International Airport |  | PH | 318 |
| 24 | Malpensa International Airport |  | IT | 298 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 286 |
| 26 | Salt Lake City International Airport |  | US | 276 |
| 27 | Daniel K Inouye International Airport |  | US | 274 |
| 28 | Charles de Gaulle International Airport |  | FR | 272 |
| 29 | Capua Airport |  | IT | 262 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 260 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 255 |
| 32 | Reno/Tahoe International Airport |  | US | 251 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 249 |
| 34 | O. R. Tambo International Airport |  | ZA | 248 |
| 35 | Vitoria/Foronda Airport |  | ES | 241 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 240 |
| 37 | Barcelona International Airport |  | ES | 238 |
| 38 | Viracopos International Airport |  | BR | 229 |
| 39 | Don Mueang International Airport |  | TH | 226 |
| 40 | Seattle-Tacoma International Airport |  | US | 225 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 180 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 168 | 1h 8m | 706 km | 2,045.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 149 | 14m | 114 km | 292.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 134 | 24m | 225 km | 519.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 104 | 1h 27m | 910 km | 1,632.0 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 96 | 19m | 165 km | 273.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 91 | 31m | - | - |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 87 | 21m | 244 km | 366.3 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 87 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 80 | 27m | 275 km | 379.1 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 79 | 21m | 99 km | 135.3 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
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
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 52 | 12m | 15 km | 13.7 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 52 | 1h 21m | 961 km | 861.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N739LT |  | Butler County Regional/Hogan Field (KHAO) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-04-15 20:40 UTC | 2026-04-15 20:52 UTC | 12m |
| N412RK |  | Dubuque Regional Airport (KDBQ) | St Paul Downtown Holman Field (KSTP) | 2026-04-15 19:59 UTC | 2026-04-15 20:46 UTC | 47m |
| N555KB |  | San Carlos Airport (KSQL) | Tracy Municipal Airport (KTCY) | 2026-04-15 20:20 UTC | 2026-04-15 20:46 UTC | 25m |
| AAE125 | AAE | Liege Airport (EBLG) | Zhuhai Airport (ZGSD) | 2026-04-15 06:11 UTC | 2026-04-15 20:44 UTC | 14h 33m |
| N220BG |  | Birmingham-Shuttlesworth International Airport (KBHM) | Nashville International Airport (KBNA) | 2026-04-15 20:07 UTC | 2026-04-15 20:42 UTC | 34m |
| N248FS |  | Santa Monica Municipal Airport (KSMO) | San Bernardino International Airport (KSBD) | 2026-04-15 19:51 UTC | 2026-04-15 20:40 UTC | 49m |
| SVA932 | Saudia | Liege Airport (EBLG) | Macau International Airport (VMMC) | 2026-04-15 05:22 UTC | 2026-04-15 20:39 UTC | 15h 17m |
| N302L |  | Republic Airport (KFRG) | Rose Field (2NK3) | 2026-04-15 20:01 UTC | 2026-04-15 20:35 UTC | 34m |
| N113BB |  | Gillespie Field (KSEE) | Hemet-Ryan Airport (KHMT) | 2026-04-15 20:03 UTC | 2026-04-15 20:31 UTC | 27m |
| N64012 |  | Kenai Municipal Airport (PAEN) | Talkeetna Airport (PATK) | 2026-04-15 19:24 UTC | 2026-04-15 20:30 UTC | 1h 6m |
| GTI8132 | GTI | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-04-15 12:41 UTC | 2026-04-15 20:30 UTC | 7h 48m |
| HIGH73 | HIG | Lincoln Airport (KLNK) | Seward Municipal Airport (KSWT) | 2026-04-15 19:43 UTC | 2026-04-15 20:29 UTC | 46m |
| AUB121 | AUB | Auburn University Regional Airport (KAUO) | West Georgia Regional/O V Gray Field (KCTJ) | 2026-04-15 19:46 UTC | 2026-04-15 20:29 UTC | 42m |
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-04-15 06:00 UTC | 2026-04-15 20:29 UTC | 14h 28m |
| N508ND |  | Van Nuys Airport (KVNY) | Riverside Airport (KRAL) | 2026-04-15 19:50 UTC | 2026-04-15 20:28 UTC | 37m |
| N739AT |  | Hemet-Ryan Airport (KHMT) | March Arb Airport (KRIV) | 2026-04-15 20:17 UTC | 2026-04-15 20:25 UTC | 7m |
| TAY401 | TAY | Liege Airport (EBLG) | Zhuhai Airport (ZGSD) | 2026-04-15 02:33 UTC | 2026-04-15 20:23 UTC | 17h 50m |
| N222HN |  | Island Airport (WV08) | West Virginia International Yeager Airport (KCRW) | 2026-04-15 20:08 UTC | 2026-04-15 20:21 UTC | 13m |
| N80866 |  | Albuquerque International Sunport Airport (KABQ) | Santa Fe Regional Airport (KSAF) | 2026-04-15 19:58 UTC | 2026-04-15 20:21 UTC | 22m |
| TRP5 | TRP | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-04-15 20:16 UTC | 2026-04-15 20:20 UTC | 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
