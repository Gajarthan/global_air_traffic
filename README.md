# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_23:12:37_UTC-green)

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

**Latest saved flight:** 2026-04-13 23:12:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-13 23:12:37 UTC

- **33,233** saved flights
- **14,875** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **33,233** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **409,524.7 tonnes** estimated CO2 emissions
- **23,740,561 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1414 |
| 2 | SkyWest Airlines | 1345 |
| 3 | IndiGo | 839 |
| 4 | American Airlines | 582 |
| 5 | EJA | 577 |
| 6 | Southwest Airlines | 484 |
| 7 | ENY | 448 |
| 8 | Lufthansa | 377 |
| 9 | AXM | 345 |
| 10 | Vueling | 340 |
| 11 | LATAM Airlines | 333 |
| 12 | All Nippon Airways | 297 |
| 13 | AZU | 295 |
| 14 | Delta Air Lines | 281 |
| 15 | LXJ | 271 |
| 16 | QLK | 271 |
| 17 | Swiss International | 252 |
| 18 | Alaska Airlines | 225 |
| 19 | WIF | 225 |
| 20 | easyJet | 222 |
| 21 | EJU | 221 |
| 22 | AEE | 216 |
| 23 | VIV | 216 |
| 24 | Japan Airlines | 206 |
| 25 | EDV | 193 |
| 26 | United Airlines | 193 |
| 27 | Avianca | 181 |
| 28 | GLO | 180 |
| 29 | JetBlue | 180 |
| 30 | Air France | 178 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 26259 |
| 2 | 🇮🇳 IN | 2564 |
| 3 | 🇪🇸 ES | 2497 |
| 4 | 🇦🇺 AU | 2279 |
| 5 | 🇧🇷 BR | 1954 |
| 6 | 🇯🇵 JP | 1783 |
| 7 | 🇮🇹 IT | 1771 |
| 8 | 🇩🇪 DE | 1664 |
| 9 | 🇨🇴 CO | 1663 |
| 10 | 🇨🇦 CA | 1632 |
| 11 | 🇬🇧 GB | 1359 |
| 12 | 🇫🇷 FR | 1221 |
| 13 | 🇲🇽 MX | 1060 |
| 14 | 🇬🇷 GR | 969 |
| 15 | 🇨🇭 CH | 922 |
| 16 | 🇲🇾 MY | 835 |
| 17 | 🇳🇴 NO | 747 |
| 18 | 🇳🇿 NZ | 706 |
| 19 | 🇿🇦 ZA | 682 |
| 20 | 🇹🇷 TR | 618 |
| 21 | 🇵🇭 PH | 617 |
| 22 | 🇬🇹 GT | 598 |
| 23 | 🇹🇭 TH | 597 |
| 24 | 🇰🇷 KR | 560 |
| 25 | 🇵🇱 PL | 518 |
| 26 | 🇲🇦 MA | 425 |
| 27 | 🇧🇸 BS | 340 |
| 28 | 🇲🇪 ME | 330 |
| 29 | 🇳🇱 NL | 321 |
| 30 | 🇲🇴 MO | 314 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 799 |
| 2 | Tokyo International Airport |  | JP | 605 |
| 3 | El Dorado International Airport |  | CO | 593 |
| 4 | Denver International Airport |  | US | 565 |
| 5 | Indira Gandhi International Airport |  | IN | 544 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 473 |
| 7 | Harry Reid International Airport |  | US | 437 |
| 8 | La Aurora Airport |  | GT | 435 |
| 9 | Zurich Airport |  | CH | 413 |
| 10 | Guaymaral Airport |  | CO | 405 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 343 |
| 12 | Chicago O'Hare International Airport |  | US | 342 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 338 |
| 14 | Frankfurt am Main International Airport |  | DE | 325 |
| 15 | Kuala Lumpur International Airport |  | MY | 321 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 315 |
| 17 | Macau International Airport |  | MO | 314 |
| 18 | Charlotte/Douglas International Airport |  | US | 303 |
| 19 | Madrid Barajas International Airport |  | ES | 303 |
| 20 | Bengaluru International Airport |  | IN | 296 |
| 21 | Tenerife Norte Airport |  | ES | 294 |
| 22 | Congonhas Airport |  | BR | 290 |
| 23 | Ninoy Aquino International Airport |  | PH | 287 |
| 24 | Malpensa International Airport |  | IT | 272 |
| 25 | Daniel K Inouye International Airport |  | US | 255 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 253 |
| 27 | Salt Lake City International Airport |  | US | 251 |
| 28 | Reno/Tahoe International Airport |  | US | 243 |
| 29 | Charles de Gaulle International Airport |  | FR | 240 |
| 30 | Capua Airport |  | IT | 236 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 235 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 228 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 228 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 226 |
| 35 | O. R. Tambo International Airport |  | ZA | 223 |
| 36 | Vitoria/Foronda Airport |  | ES | 222 |
| 37 | Miami International Airport |  | US | 214 |
| 38 | Barcelona International Airport |  | ES | 214 |
| 39 | Seattle-Tacoma International Airport |  | US | 209 |
| 40 | Calgary International Airport |  | CA | 205 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 157 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 153 | 1h 8m | 706 km | 1,862.8 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 138 | 14m | 114 km | 270.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 119 | 24m | 225 km | 461.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 106 | 28m | 304 km | 555.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 93 | 1h 27m | 910 km | 1,459.4 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 85 | 19m | 165 km | 241.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 80 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 80 | 9m | - | - |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 74 | 54m | 546 km | 696.7 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 73 | 21m | 244 km | 307.4 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 73 | 27m | 275 km | 345.9 t |
| 14 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 68 | 1h 12m | 770 km | 903.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 65 | 31m | 369 km | 413.7 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 60 | 45m | 452 km | 467.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 20 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 57 | 20m | 250 km | 246.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 53 | 20m | 147 km | 134.1 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 52 | 1h 41m | 1,423 km | 1,276.2 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 51 | 13m | 99 km | 87.4 t |
| 25 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 49 | 16m | 162 km | 137.4 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 48 | 23m | 252 km | 208.4 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 47 | 12m | 15 km | 12.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 47 | 1h 20m | 961 km | 779.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 46 | 1h 53m | 1,304 km | 1,034.9 t |
| 30 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| QXE2315 | QXE | Seattle Paine Field International Airport (KPAE) | Yucca Valley Airport (KL22) | 2026-04-13 21:04 UTC | 2026-04-13 23:12 UTC | 2h 8m |
| ALFT6 | ALF | Jefferson County International Airport (K0S9) | Boeing Field/King County International Airport (KBFI) | 2026-04-13 22:48 UTC | 2026-04-13 23:09 UTC | 21m |
| N6967C |  | Middle Georgia Regional Airport (KMCN) | Perry-Houston County Airport (KPXE) | 2026-04-13 22:39 UTC | 2026-04-13 23:02 UTC | 23m |
| CGNOR | CGN | King George Airpark (CSK8) | Pitt Meadows Airport (CYPK) | 2026-04-13 22:49 UTC | 2026-04-13 22:57 UTC | 8m |
| N7196R |  | Mesquite Metro Airport (KHQZ) | Commerce Municipal Airport (K2F7) | 2026-04-13 22:07 UTC | 2026-04-13 22:57 UTC | 50m |
| N737JA |  | Monterey Bay Academy Airport (CA66) | Watsonville Municipal Airport (KWVI) | 2026-04-13 22:38 UTC | 2026-04-13 22:55 UTC | 16m |
| N1569P |  | Gillespie Field (KSEE) | Gillespie Field (KSEE) | 2026-04-13 22:53 UTC | 2026-04-13 22:53 UTC | 0m |
| CPA294 | Cathay Pacific | Brussels Airport (EBBR) | Zhuhai Airport (ZGSD) | 2026-04-13 11:26 UTC | 2026-04-13 22:46 UTC | 11h 19m |
| N49TW |  | Cavanaugh Airport (NE29) | Wilkens Airport (32KS) | 2026-04-13 22:06 UTC | 2026-04-13 22:45 UTC | 39m |
| N366CA |  | KU42 (KU42) | KU42 (KU42) | 2026-04-13 22:00 UTC | 2026-04-13 22:44 UTC | 44m |
| XBM | XBM | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-04-13 22:13 UTC | 2026-04-13 22:44 UTC | 31m |
| CPA300 | Cathay Pacific | Munich International Airport (EDDM) | Zhuhai Airport (ZGSD) | 2026-04-13 12:18 UTC | 2026-04-13 22:43 UTC | 10h 25m |
| CPA014 | Cathay Pacific | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-04-13 11:52 UTC | 2026-04-13 22:40 UTC | 10h 48m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Macau International Airport (VMMC) | 2026-04-13 10:23 UTC | 2026-04-13 22:35 UTC | 12h 11m |
| N89815 |  | Mc Clellan-Palomar Airport (KCRQ) | Mc Clellan-Palomar Airport (KCRQ) | 2026-04-13 21:48 UTC | 2026-04-13 22:34 UTC | 46m |
| N73047 |  | Merrill Field (PAMR) | Beluga Airport (PABG) | 2026-04-13 22:07 UTC | 2026-04-13 22:33 UTC | 26m |
| TKR105 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | Perry Stokes Airport (KTAD) | 2026-04-13 22:13 UTC | 2026-04-13 22:30 UTC | 17m |
| LXJ301 | LXJ | Harry Reid International Airport (KLAS) | Lake Tahoe Airport (KTVL) | 2026-04-13 21:38 UTC | 2026-04-13 22:29 UTC | 50m |
| XBCPE | XBC | General Abelardo L. Rodriguez International Airport (MMTJ) | General Abelardo L. Rodriguez International Airport (MMTJ) | 2026-04-13 22:17 UTC | 2026-04-13 22:28 UTC | 11m |
| SAMU13 | SAM | Chateau-Arnoux-Saint-Auban Airport (LFMX) | Marseille Provence Airport (LFML) | 2026-04-13 22:04 UTC | 2026-04-13 22:28 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
