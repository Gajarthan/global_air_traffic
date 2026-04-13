# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_21:23:19_UTC-green)

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

**Latest saved flight:** 2026-04-13 21:23:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-13 21:23:19 UTC

- **32,999** saved flights
- **14,801** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **32,999** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **406,300.5 tonnes** estimated CO2 emissions
- **23,553,654 km** total distance flown
- **850 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1408 |
| 2 | SkyWest Airlines | 1330 |
| 3 | IndiGo | 839 |
| 4 | American Airlines | 577 |
| 5 | EJA | 574 |
| 6 | Southwest Airlines | 478 |
| 7 | ENY | 441 |
| 8 | Lufthansa | 377 |
| 9 | AXM | 345 |
| 10 | Vueling | 340 |
| 11 | LATAM Airlines | 331 |
| 12 | All Nippon Airways | 297 |
| 13 | AZU | 291 |
| 14 | Delta Air Lines | 275 |
| 15 | LXJ | 270 |
| 16 | QLK | 266 |
| 17 | Swiss International | 252 |
| 18 | WIF | 225 |
| 19 | Alaska Airlines | 223 |
| 20 | easyJet | 222 |
| 21 | EJU | 221 |
| 22 | AEE | 215 |
| 23 | VIV | 212 |
| 24 | Japan Airlines | 206 |
| 25 | EDV | 192 |
| 26 | United Airlines | 192 |
| 27 | GLO | 179 |
| 28 | Air France | 178 |
| 29 | JetBlue | 178 |
| 30 | Avianca | 175 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 26012 |
| 2 | 🇮🇳 IN | 2563 |
| 3 | 🇪🇸 ES | 2489 |
| 4 | 🇦🇺 AU | 2253 |
| 5 | 🇧🇷 BR | 1940 |
| 6 | 🇯🇵 JP | 1781 |
| 7 | 🇮🇹 IT | 1769 |
| 8 | 🇩🇪 DE | 1662 |
| 9 | 🇨🇴 CO | 1644 |
| 10 | 🇨🇦 CA | 1600 |
| 11 | 🇬🇧 GB | 1354 |
| 12 | 🇫🇷 FR | 1218 |
| 13 | 🇲🇽 MX | 1046 |
| 14 | 🇬🇷 GR | 966 |
| 15 | 🇨🇭 CH | 921 |
| 16 | 🇲🇾 MY | 835 |
| 17 | 🇳🇴 NO | 747 |
| 18 | 🇳🇿 NZ | 688 |
| 19 | 🇿🇦 ZA | 682 |
| 20 | 🇹🇷 TR | 618 |
| 21 | 🇵🇭 PH | 613 |
| 22 | 🇬🇹 GT | 598 |
| 23 | 🇹🇭 TH | 597 |
| 24 | 🇰🇷 KR | 559 |
| 25 | 🇵🇱 PL | 517 |
| 26 | 🇲🇦 MA | 422 |
| 27 | 🇧🇸 BS | 340 |
| 28 | 🇲🇪 ME | 329 |
| 29 | 🇳🇱 NL | 320 |
| 30 | 🇮🇩 ID | 311 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 786 |
| 2 | Tokyo International Airport |  | JP | 604 |
| 3 | El Dorado International Airport |  | CO | 583 |
| 4 | Denver International Airport |  | US | 558 |
| 5 | Indira Gandhi International Airport |  | IN | 543 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 473 |
| 7 | La Aurora Airport |  | GT | 435 |
| 8 | Harry Reid International Airport |  | US | 428 |
| 9 | Zurich Airport |  | CH | 412 |
| 10 | Guaymaral Airport |  | CO | 405 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 340 |
| 12 | Chicago O'Hare International Airport |  | US | 338 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 336 |
| 14 | Frankfurt am Main International Airport |  | DE | 325 |
| 15 | Kuala Lumpur International Airport |  | MY | 321 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 312 |
| 17 | Macau International Airport |  | MO | 310 |
| 18 | Madrid Barajas International Airport |  | ES | 302 |
| 19 | Charlotte/Douglas International Airport |  | US | 300 |
| 20 | Bengaluru International Airport |  | IN | 296 |
| 21 | Tenerife Norte Airport |  | ES | 294 |
| 22 | Congonhas Airport |  | BR | 289 |
| 23 | Ninoy Aquino International Airport |  | PH | 284 |
| 24 | Malpensa International Airport |  | IT | 271 |
| 25 | Daniel K Inouye International Airport |  | US | 254 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 250 |
| 27 | Salt Lake City International Airport |  | US | 248 |
| 28 | Reno/Tahoe International Airport |  | US | 243 |
| 29 | Charles de Gaulle International Airport |  | FR | 240 |
| 30 | Capua Airport |  | IT | 236 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 233 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 228 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 226 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 226 |
| 35 | O. R. Tambo International Airport |  | ZA | 223 |
| 36 | Vitoria/Foronda Airport |  | ES | 222 |
| 37 | Barcelona International Airport |  | ES | 214 |
| 38 | Miami International Airport |  | US | 213 |
| 39 | Seattle-Tacoma International Airport |  | US | 204 |
| 40 | Calgary International Airport |  | CA | 202 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 157 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 152 | 1h 8m | 706 km | 1,850.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 136 | 14m | 114 km | 266.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 119 | 24m | 225 km | 461.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 106 | 28m | 304 km | 555.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 93 | 1h 27m | 910 km | 1,459.4 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 85 | 19m | 165 km | 241.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 80 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 80 | 9m | - | - |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 74 | 54m | 546 km | 696.7 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 73 | 27m | 275 km | 345.9 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 72 | 21m | 244 km | 303.2 t |
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
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 46 | 1h 20m | 961 km | 762.5 t |
| 29 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 45 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N769SA |  | Charleston Executive Airport (KJZI) | Charleston Executive Airport (KJZI) | 2026-04-13 20:46 UTC | 2026-04-13 21:23 UTC | 36m |
| N39CK |  | Melbourne Orlando International Airport (KMLB) | Lake Wales Municipal Airport (KX07) | 2026-04-13 20:40 UTC | 2026-04-13 21:15 UTC | 34m |
| N483LP |  | Glendale Regional Airport (KGEU) | 42AZ (42AZ) | 2026-04-13 20:25 UTC | 2026-04-13 21:14 UTC | 49m |
| CPA640 | Cathay Pacific | Langtang Airport (VNLT) | Zhuhai Airport (ZGSD) | 2026-04-13 18:00 UTC | 2026-04-13 21:12 UTC | 3h 12m |
| N540M |  | Dupage Airport (KDPA) | Dane County Regional/Truax Field (KMSN) | 2026-04-13 20:44 UTC | 2026-04-13 21:10 UTC | 26m |
| N460CA |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-04-13 20:44 UTC | 2026-04-13 21:09 UTC | 24m |
| N54PV |  | Long Beach (Daugherty Field) Airport (KLGB) | Riverside Airport (KRAL) | 2026-04-13 20:46 UTC | 2026-04-13 21:04 UTC | 17m |
| N111EN |  | Austin Executive Airport (KEDC) | TX11 (TX11) | 2026-04-13 20:25 UTC | 2026-04-13 21:01 UTC | 35m |
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-13 06:10 UTC | 2026-04-13 21:00 UTC | 14h 50m |
| N909DP |  | Mc Neill Ranch Airport (6TE7) | K54F (K54F) | 2026-04-13 20:23 UTC | 2026-04-13 21:00 UTC | 37m |
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-04-13 19:56 UTC | 2026-04-13 20:59 UTC | 1h 2m |
| N77ZR |  | Creve Coeur Airport (K1H0) | Blackhawk Airport (6MO0) | 2026-04-13 20:48 UTC | 2026-04-13 20:58 UTC | 10m |
| BURNY41 | BUR | Wichita Valley Airport (KF14) | Smiley Johnson Municipal/Bass Field (KE34) | 2026-04-13 20:27 UTC | 2026-04-13 20:46 UTC | 19m |
| TKR105 | TKR | 25NE (25NE) | Perry Stokes Airport (KTAD) | 2026-04-13 19:57 UTC | 2026-04-13 20:45 UTC | 47m |
| SCU41 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-04-13 20:43 UTC | 2026-04-13 20:45 UTC | 1m |
| N28WS |  | Rover Airport (PA31) | Gilbert Airport (73PA) | 2026-04-13 20:30 UTC | 2026-04-13 20:44 UTC | 13m |
| DEVIL52 | DEV | Sandy Creek Airport (73TX) | Maverick County Memorial International Airport (K5T9) | 2026-04-13 20:21 UTC | 2026-04-13 20:42 UTC | 21m |
| OKC317 | OKC | Charleston Afb/International Airport (KCHS) | General Edward Lawrence Logan International Airport (KBOS) | 2026-04-13 18:46 UTC | 2026-04-13 20:40 UTC | 1h 53m |
| N65415 |  | University Airport (KEDU) | Tracy Municipal Airport (KTCY) | 2026-04-13 19:55 UTC | 2026-04-13 20:36 UTC | 41m |
| EZY18QU | easyJet | Belfast International Airport (EGAA) | Newcastle Airport (EGNT) | 2026-04-13 20:03 UTC | 2026-04-13 20:36 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
