# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_17:33:05_UTC-green)

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

**Latest saved flight:** 2026-04-18 17:33:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-18 17:33:05 UTC

- **41,586** saved flights
- **17,557** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **41,586** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **499,648.8 tonnes** estimated CO2 emissions
- **28,965,149 km** total distance flown
- **836 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1747 |
| 2 | SkyWest Airlines | 1602 |
| 3 | IndiGo | 1027 |
| 4 | EJA | 718 |
| 5 | American Airlines | 686 |
| 6 | Southwest Airlines | 583 |
| 7 | ENY | 529 |
| 8 | AXM | 434 |
| 9 | Vueling | 416 |
| 10 | LATAM Airlines | 411 |
| 11 | Lufthansa | 410 |
| 12 | All Nippon Airways | 377 |
| 13 | AZU | 370 |
| 14 | Delta Air Lines | 349 |
| 15 | QLK | 341 |
| 16 | LXJ | 326 |
| 17 | WIF | 324 |
| 18 | Swiss International | 320 |
| 19 | AEE | 281 |
| 20 | Alaska Airlines | 279 |
| 21 | EJU | 273 |
| 22 | easyJet | 269 |
| 23 | VIV | 266 |
| 24 | Japan Airlines | 257 |
| 25 | Air France | 235 |
| 26 | United Airlines | 223 |
| 27 | JetBlue | 222 |
| 28 | GLO | 220 |
| 29 | AXB | 219 |
| 30 | EDV | 216 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 32740 |
| 2 | 🇮🇳 IN | 3139 |
| 3 | 🇪🇸 ES | 3070 |
| 4 | 🇦🇺 AU | 2918 |
| 5 | 🇧🇷 BR | 2482 |
| 6 | 🇯🇵 JP | 2291 |
| 7 | 🇮🇹 IT | 2159 |
| 8 | 🇩🇪 DE | 2117 |
| 9 | 🇨🇦 CA | 2026 |
| 10 | 🇨🇴 CO | 1961 |
| 11 | 🇬🇧 GB | 1691 |
| 12 | 🇫🇷 FR | 1601 |
| 13 | 🇲🇽 MX | 1303 |
| 14 | 🇬🇷 GR | 1268 |
| 15 | 🇨🇭 CH | 1169 |
| 16 | 🇲🇾 MY | 1053 |
| 17 | 🇳🇴 NO | 1031 |
| 18 | 🇿🇦 ZA | 867 |
| 19 | 🇳🇿 NZ | 844 |
| 20 | 🇵🇭 PH | 756 |
| 21 | 🇹🇭 TH | 740 |
| 22 | 🇹🇷 TR | 725 |
| 23 | 🇬🇹 GT | 701 |
| 24 | 🇰🇷 KR | 687 |
| 25 | 🇵🇱 PL | 661 |
| 26 | 🇲🇦 MA | 513 |
| 27 | 🇳🇱 NL | 429 |
| 28 | 🇲🇪 ME | 425 |
| 29 | 🇧🇸 BS | 393 |
| 30 | 🇮🇩 ID | 380 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 953 |
| 2 | Tokyo International Airport |  | JP | 783 |
| 3 | El Dorado International Airport |  | CO | 689 |
| 4 | Denver International Airport |  | US | 682 |
| 5 | Indira Gandhi International Airport |  | IN | 676 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 630 |
| 7 | Harry Reid International Airport |  | US | 533 |
| 8 | Guaymaral Airport |  | CO | 523 |
| 9 | La Aurora Airport |  | GT | 517 |
| 10 | Zurich Airport |  | CH | 503 |
| 11 | Kuala Lumpur International Airport |  | MY | 415 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 408 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 400 |
| 14 | Chicago O'Hare International Airport |  | US | 397 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 394 |
| 16 | Frankfurt am Main International Airport |  | DE | 379 |
| 17 | Madrid Barajas International Airport |  | ES | 378 |
| 18 | Macau International Airport |  | MO | 377 |
| 19 | Bengaluru International Airport |  | IN | 370 |
| 20 | Tenerife Norte Airport |  | ES | 363 |
| 21 | Charlotte/Douglas International Airport |  | US | 362 |
| 22 | Congonhas Airport |  | BR | 361 |
| 23 | Ninoy Aquino International Airport |  | PH | 351 |
| 24 | Malpensa International Airport |  | IT | 335 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 324 |
| 26 | Salt Lake City International Airport |  | US | 314 |
| 27 | Daniel K Inouye International Airport |  | US | 309 |
| 28 | Charles de Gaulle International Airport |  | FR | 304 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 304 |
| 30 | Vitoria/Foronda Airport |  | ES | 295 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 290 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 287 |
| 33 | Reno/Tahoe International Airport |  | US | 282 |
| 34 | O. R. Tambo International Airport |  | ZA | 281 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 281 |
| 36 | Capua Airport |  | IT | 277 |
| 37 | Barcelona International Airport |  | ES | 266 |
| 38 | Viracopos International Airport |  | BR | 255 |
| 39 | Calgary International Airport |  | CA | 247 |
| 40 | Don Mueang International Airport |  | TH | 246 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 209 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 196 | 1h 7m | 706 km | 2,386.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 150 | 24m | 225 km | 581.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 124 | 28m | 304 km | 650.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 121 | 1h 27m | 910 km | 1,898.8 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 112 | 31m | - | - |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 112 | 19m | 165 km | 318.6 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 111 | 21m | 244 km | 467.4 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 105 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 99 | 26m | 275 km | 469.1 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 91 | 54m | 546 km | 856.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 88 | 21m | 99 km | 150.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 85 | 44m | 452 km | 662.5 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 82 | 1h 11m | 770 km | 1,089.3 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 76 | 27m | 152 km | 198.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 75 | 31m | 369 km | 477.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 69 | 20m | 250 km | 298.0 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 66 | 20m | 147 km | 167.0 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 66 | 52m | 556 km | 632.7 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 63 | 26m | 215 km | 233.3 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 62 | 16m | 162 km | 173.8 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 59 | 12m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 53m | 1,304 km | 1,327.3 t |
| 28 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 58 | 1h 21m | 961 km | 961.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 57 | 14m | 154 km | 151.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N724KB |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-04-18 16:59 UTC | 2026-04-18 17:33 UTC | 33m |
| N7367E |  | Aztec Municipal Airport (KN19) | Animas Air Park (K00C) | 2026-04-18 17:08 UTC | 2026-04-18 17:30 UTC | 22m |
| N92DV |  | Vance Brand Airport (KLMO) | Erie Municipal Airport (KEIK) | 2026-04-18 16:05 UTC | 2026-04-18 17:29 UTC | 1h 23m |
| N21SZ |  | Whiteman Airport (KWHP) | Whiteman Airport (KWHP) | 2026-04-18 16:38 UTC | 2026-04-18 17:29 UTC | 50m |
| N247LM |  | Centennial Airport (KAPA) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-18 17:11 UTC | 2026-04-18 17:24 UTC | 12m |
| N360SP |  | Witham Field (KSUA) | Sarasota/Bradenton International Airport (KSRQ) | 2026-04-18 16:10 UTC | 2026-04-18 17:22 UTC | 1h 11m |
| G20628 |  | IA48 (IA48) | IA48 (IA48) | 2026-04-18 16:15 UTC | 2026-04-18 17:22 UTC | 1h 6m |
| N521NG |  | Carson City Airport (KCXP) | Lake Tahoe Airport (KTVL) | 2026-04-18 16:59 UTC | 2026-04-18 17:19 UTC | 20m |
| N3558Y |  | Cable Airport (KCCB) | Brackett Field (KPOC) | 2026-04-18 16:31 UTC | 2026-04-18 17:19 UTC | 48m |
| N294DS |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-04-18 16:46 UTC | 2026-04-18 17:19 UTC | 33m |
| N220BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-04-18 16:33 UTC | 2026-04-18 17:18 UTC | 44m |
| RNGR855 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Mustang Beach Airport (KRAS) | 2026-04-18 16:32 UTC | 2026-04-18 17:11 UTC | 38m |
| N19688 |  | Whiteman Airport (KWHP) | Whiteman Airport (KWHP) | 2026-04-18 16:45 UTC | 2026-04-18 17:08 UTC | 22m |
| SCU38 | SCU | Tulsa Riverside Airport (KRVS) | William R Pogue Municipal Airport (KOWP) | 2026-04-18 16:39 UTC | 2026-04-18 17:08 UTC | 28m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-18 15:42 UTC | 2026-04-18 17:05 UTC | 1h 22m |
| CXK260 | CXK | Hartford-Brainard Airport (KHFD) | Hartford-Brainard Airport (KHFD) | 2026-04-18 17:00 UTC | 2026-04-18 17:03 UTC | 2m |
| BBC495 | BBC | VGZR (VGZR) | Hashimara Air Force Station (VE44) | 2026-04-18 16:28 UTC | 2026-04-18 17:03 UTC | 34m |
| N2621Z |  | Montgomery County Airpark (KGAI) | Three J Airport (MD56) | 2026-04-18 16:20 UTC | 2026-04-18 17:02 UTC | 42m |
| N66849 |  | New Smyrna Beach Airport (8FA4) | Spruce Creek Airport (7FL6) | 2026-04-18 16:57 UTC | 2026-04-18 17:01 UTC | 4m |
| FCM1M | FCM | Tampere-Pirkkala Airport (EFTP) | Tampere-Pirkkala Airport (EFTP) | 2026-04-18 16:02 UTC | 2026-04-18 16:59 UTC | 56m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
