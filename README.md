# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_19:43:52_UTC-green)

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

**Latest saved flight:** 2026-04-18 19:43:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-18 19:43:52 UTC

- **41,951** saved flights
- **17,680** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **41,951** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **504,427.3 tonnes** estimated CO2 emissions
- **29,242,160 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1764 |
| 2 | SkyWest Airlines | 1636 |
| 3 | IndiGo | 1027 |
| 4 | EJA | 725 |
| 5 | American Airlines | 697 |
| 6 | Southwest Airlines | 591 |
| 7 | ENY | 537 |
| 8 | AXM | 434 |
| 9 | Vueling | 421 |
| 10 | LATAM Airlines | 415 |
| 11 | Lufthansa | 413 |
| 12 | All Nippon Airways | 377 |
| 13 | AZU | 375 |
| 14 | Delta Air Lines | 358 |
| 15 | QLK | 341 |
| 16 | LXJ | 331 |
| 17 | Swiss International | 324 |
| 18 | WIF | 324 |
| 19 | Alaska Airlines | 285 |
| 20 | AEE | 281 |
| 21 | EJU | 277 |
| 22 | easyJet | 270 |
| 23 | VIV | 269 |
| 24 | Japan Airlines | 257 |
| 25 | Air France | 236 |
| 26 | United Airlines | 229 |
| 27 | JetBlue | 225 |
| 28 | GLO | 222 |
| 29 | AXB | 220 |
| 30 | EDV | 219 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 33187 |
| 2 | 🇮🇳 IN | 3143 |
| 3 | 🇪🇸 ES | 3091 |
| 4 | 🇦🇺 AU | 2918 |
| 5 | 🇧🇷 BR | 2514 |
| 6 | 🇯🇵 JP | 2291 |
| 7 | 🇮🇹 IT | 2184 |
| 8 | 🇩🇪 DE | 2125 |
| 9 | 🇨🇦 CA | 2048 |
| 10 | 🇨🇴 CO | 1967 |
| 11 | 🇬🇧 GB | 1706 |
| 12 | 🇫🇷 FR | 1616 |
| 13 | 🇲🇽 MX | 1320 |
| 14 | 🇬🇷 GR | 1273 |
| 15 | 🇨🇭 CH | 1178 |
| 16 | 🇲🇾 MY | 1053 |
| 17 | 🇳🇴 NO | 1032 |
| 18 | 🇿🇦 ZA | 869 |
| 19 | 🇳🇿 NZ | 844 |
| 20 | 🇵🇭 PH | 756 |
| 21 | 🇹🇭 TH | 741 |
| 22 | 🇹🇷 TR | 731 |
| 23 | 🇬🇹 GT | 705 |
| 24 | 🇰🇷 KR | 687 |
| 25 | 🇵🇱 PL | 664 |
| 26 | 🇲🇦 MA | 520 |
| 27 | 🇳🇱 NL | 431 |
| 28 | 🇲🇪 ME | 429 |
| 29 | 🇧🇸 BS | 395 |
| 30 | 🇮🇩 ID | 380 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 972 |
| 2 | Tokyo International Airport |  | JP | 783 |
| 3 | Denver International Airport |  | US | 696 |
| 4 | El Dorado International Airport |  | CO | 689 |
| 5 | Indira Gandhi International Airport |  | IN | 678 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 630 |
| 7 | Harry Reid International Airport |  | US | 541 |
| 8 | Guaymaral Airport |  | CO | 529 |
| 9 | La Aurora Airport |  | GT | 520 |
| 10 | Zurich Airport |  | CH | 507 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 418 |
| 12 | Kuala Lumpur International Airport |  | MY | 415 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 408 |
| 14 | Chicago O'Hare International Airport |  | US | 405 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 394 |
| 16 | Frankfurt am Main International Airport |  | DE | 383 |
| 17 | Madrid Barajas International Airport |  | ES | 378 |
| 18 | Macau International Airport |  | MO | 377 |
| 19 | Bengaluru International Airport |  | IN | 370 |
| 20 | Tenerife Norte Airport |  | ES | 368 |
| 21 | Charlotte/Douglas International Airport |  | US | 365 |
| 22 | Congonhas Airport |  | BR | 365 |
| 23 | Ninoy Aquino International Airport |  | PH | 351 |
| 24 | Malpensa International Airport |  | IT | 341 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 325 |
| 26 | Salt Lake City International Airport |  | US | 323 |
| 27 | Daniel K Inouye International Airport |  | US | 314 |
| 28 | Charles de Gaulle International Airport |  | FR | 306 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 305 |
| 30 | Vitoria/Foronda Airport |  | ES | 299 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 291 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 289 |
| 33 | Reno/Tahoe International Airport |  | US | 287 |
| 34 | O. R. Tambo International Airport |  | ZA | 282 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 282 |
| 36 | Capua Airport |  | IT | 282 |
| 37 | Barcelona International Airport |  | ES | 267 |
| 38 | Viracopos International Airport |  | BR | 259 |
| 39 | Calgary International Airport |  | CA | 252 |
| 40 | Seattle-Tacoma International Airport |  | US | 248 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 212 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 196 | 1h 7m | 706 km | 2,386.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 150 | 24m | 225 km | 581.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 124 | 28m | 304 km | 650.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 121 | 1h 27m | 910 km | 1,898.8 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 115 | 21m | 244 km | 484.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 112 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 112 | 19m | 165 km | 318.6 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 105 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 99 | 26m | 275 km | 469.1 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 91 | 54m | 546 km | 856.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 88 | 21m | 99 km | 150.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 85 | 44m | 452 km | 662.5 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 82 | 1h 11m | 770 km | 1,089.3 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 76 | 27m | 152 km | 198.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 75 | 31m | 369 km | 477.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 70 | 20m | 250 km | 302.4 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 67 | 52m | 556 km | 642.3 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 66 | 20m | 147 km | 167.0 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 63 | 26m | 215 km | 233.3 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 59 | 12m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 53m | 1,304 km | 1,327.3 t |
| 28 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 58 | 1h 21m | 961 km | 961.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 57 | 14m | 154 km | 151.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EDV5157 | EDV | Hartsfield/Jackson Atlanta International Airport (KATL) | Yazoo County Airport (K87I) | 2026-04-18 18:53 UTC | 2026-04-18 19:43 UTC | 50m |
| LXJ435 | LXJ | Lake County Airport (KLXV) | Centennial Airport (KAPA) | 2026-04-18 19:18 UTC | 2026-04-18 19:38 UTC | 19m |
| CFWFK | CFW | Lethbridge / J3 Airfield (CLJ3) | Banff Airport (CYBA) | 2026-04-18 17:42 UTC | 2026-04-18 19:33 UTC | 1h 50m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-04-18 19:16 UTC | 2026-04-18 19:33 UTC | 16m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-18 18:53 UTC | 2026-04-18 19:32 UTC | 39m |
| N4788D |  | Galt Field (K10C) | Galt Field (K10C) | 2026-04-18 19:27 UTC | 2026-04-18 19:31 UTC | 3m |
| N383BP |  | St Louis Downtown Airport (KCPS) | Johnson County Executive Airport (KOJC) | 2026-04-18 18:36 UTC | 2026-04-18 19:28 UTC | 52m |
| N183TS |  | Columbus Airport (KCSG) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-18 19:02 UTC | 2026-04-18 19:28 UTC | 25m |
| N747EE |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-04-18 17:50 UTC | 2026-04-18 19:26 UTC | 1h 36m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-18 18:40 UTC | 2026-04-18 19:26 UTC | 45m |
| N54PV |  | Long Beach (Daugherty Field) Airport (KLGB) | San Bernardino International Airport (KSBD) | 2026-04-18 19:05 UTC | 2026-04-18 19:25 UTC | 20m |
| N555NL |  | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-04-18 18:58 UTC | 2026-04-18 19:24 UTC | 25m |
| N20543 |  | Yucca Valley Airport (KL22) | Big Bear City Airport (KL35) | 2026-04-18 19:03 UTC | 2026-04-18 19:23 UTC | 19m |
| N929HG |  | Scottsdale Airport (KSDL) | Montezuma Airport (19AZ) | 2026-04-18 18:55 UTC | 2026-04-18 19:21 UTC | 25m |
| N529LF |  | Albuquerque International Sunport Airport (KABQ) | NM74 (NM74) | 2026-04-18 18:40 UTC | 2026-04-18 19:20 UTC | 39m |
| N132CA |  | Montgomery-Gibbs Executive Airport (KMYF) | Ramona Airport (KRNM) | 2026-04-18 17:18 UTC | 2026-04-18 19:19 UTC | 2h 1m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-18 18:51 UTC | 2026-04-18 19:15 UTC | 23m |
| N545GC |  | Lompoc Airport (KLPC) | Lompoc Airport (KLPC) | 2026-04-18 18:53 UTC | 2026-04-18 19:14 UTC | 20m |
| N980RR |  | Lancaster Airport (KLNS) | Lancaster Airport (KLNS) | 2026-04-18 19:10 UTC | 2026-04-18 19:13 UTC | 2m |
| N916JR |  | Albuquerque International Sunport Airport (KABQ) | Grant County Airport (KSVC) | 2026-04-18 18:29 UTC | 2026-04-18 19:13 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
