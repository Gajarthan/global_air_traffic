# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_06:20:01_UTC-green)

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

**Latest saved flight:** 2026-04-19 06:20:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-19 06:20:01 UTC

- **42,466** saved flights
- **17,825** unique routes
- **122** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **42,466** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **508,969.8 tonnes** estimated CO2 emissions
- **29,505,494 km** total distance flown
- **834 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1770 |
| 2 | SkyWest Airlines | 1653 |
| 3 | IndiGo | 1035 |
| 4 | EJA | 733 |
| 5 | American Airlines | 706 |
| 6 | Southwest Airlines | 599 |
| 7 | ENY | 556 |
| 8 | AXM | 438 |
| 9 | LATAM Airlines | 424 |
| 10 | Vueling | 424 |
| 11 | Lufthansa | 415 |
| 12 | All Nippon Airways | 383 |
| 13 | AZU | 378 |
| 14 | Delta Air Lines | 363 |
| 15 | QLK | 348 |
| 16 | LXJ | 333 |
| 17 | Swiss International | 324 |
| 18 | WIF | 324 |
| 19 | Alaska Airlines | 288 |
| 20 | AEE | 284 |
| 21 | EJU | 278 |
| 22 | easyJet | 272 |
| 23 | VIV | 271 |
| 24 | Japan Airlines | 262 |
| 25 | Air France | 236 |
| 26 | United Airlines | 230 |
| 27 | JetBlue | 228 |
| 28 | GLO | 224 |
| 29 | AXB | 221 |
| 30 | EDV | 219 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 33664 |
| 2 | 🇮🇳 IN | 3172 |
| 3 | 🇪🇸 ES | 3100 |
| 4 | 🇦🇺 AU | 3001 |
| 5 | 🇧🇷 BR | 2545 |
| 6 | 🇯🇵 JP | 2357 |
| 7 | 🇮🇹 IT | 2190 |
| 8 | 🇩🇪 DE | 2131 |
| 9 | 🇨🇦 CA | 2083 |
| 10 | 🇨🇴 CO | 1971 |
| 11 | 🇬🇧 GB | 1709 |
| 12 | 🇫🇷 FR | 1620 |
| 13 | 🇲🇽 MX | 1335 |
| 14 | 🇬🇷 GR | 1285 |
| 15 | 🇨🇭 CH | 1179 |
| 16 | 🇲🇾 MY | 1067 |
| 17 | 🇳🇴 NO | 1034 |
| 18 | 🇿🇦 ZA | 873 |
| 19 | 🇳🇿 NZ | 872 |
| 20 | 🇵🇭 PH | 773 |
| 21 | 🇹🇭 TH | 753 |
| 22 | 🇹🇷 TR | 740 |
| 23 | 🇰🇷 KR | 711 |
| 24 | 🇬🇹 GT | 707 |
| 25 | 🇵🇱 PL | 665 |
| 26 | 🇲🇦 MA | 522 |
| 27 | 🇳🇱 NL | 433 |
| 28 | 🇲🇪 ME | 430 |
| 29 | 🇧🇸 BS | 397 |
| 30 | 🇮🇩 ID | 386 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 994 |
| 2 | Tokyo International Airport |  | JP | 802 |
| 3 | Denver International Airport |  | US | 705 |
| 4 | El Dorado International Airport |  | CO | 689 |
| 5 | Indira Gandhi International Airport |  | IN | 686 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 637 |
| 7 | Harry Reid International Airport |  | US | 548 |
| 8 | Guaymaral Airport |  | CO | 533 |
| 9 | La Aurora Airport |  | GT | 522 |
| 10 | Zurich Airport |  | CH | 508 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 422 |
| 12 | Kuala Lumpur International Airport |  | MY | 421 |
| 13 | Chicago O'Hare International Airport |  | US | 414 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 410 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 403 |
| 16 | Frankfurt am Main International Airport |  | DE | 384 |
| 17 | Madrid Barajas International Airport |  | ES | 379 |
| 18 | Macau International Airport |  | MO | 378 |
| 19 | Bengaluru International Airport |  | IN | 374 |
| 20 | Charlotte/Douglas International Airport |  | US | 371 |
| 21 | Tenerife Norte Airport |  | ES | 368 |
| 22 | Congonhas Airport |  | BR | 366 |
| 23 | Ninoy Aquino International Airport |  | PH | 359 |
| 24 | Malpensa International Airport |  | IT | 343 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 329 |
| 26 | Salt Lake City International Airport |  | US | 324 |
| 27 | Daniel K Inouye International Airport |  | US | 316 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 311 |
| 29 | Charles de Gaulle International Airport |  | FR | 306 |
| 30 | Vitoria/Foronda Airport |  | ES | 299 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 298 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 293 |
| 33 | Reno/Tahoe International Airport |  | US | 293 |
| 34 | O. R. Tambo International Airport |  | ZA | 283 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 283 |
| 36 | Capua Airport |  | IT | 282 |
| 37 | Barcelona International Airport |  | ES | 269 |
| 38 | Viracopos International Airport |  | BR | 261 |
| 39 | Calgary International Airport |  | CA | 256 |
| 40 | Seattle-Tacoma International Airport |  | US | 253 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 214 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 200 | 1h 7m | 706 km | 2,435.0 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 156 | 24m | 225 km | 605.2 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 129 | 28m | 304 km | 676.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 125 | 1h 27m | 910 km | 1,961.5 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 116 | 21m | 244 km | 488.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 115 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 114 | 19m | 165 km | 324.3 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 106 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 99 | 26m | 275 km | 469.1 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 92 | 54m | 546 km | 866.2 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 88 | 44m | 452 km | 685.8 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 88 | 21m | 99 km | 150.7 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 83 | 1h 11m | 770 km | 1,102.6 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 76 | 27m | 152 km | 198.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 75 | 31m | 369 km | 477.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 70 | 20m | 250 km | 302.4 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 69 | 52m | 556 km | 661.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 66 | 20m | 147 km | 167.0 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 63 | 26m | 215 km | 233.3 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 60 | 1h 53m | 1,304 km | 1,349.8 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 59 | 12m | - | - |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 0m | 695 km | 707.2 t |
| 29 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 58 | 1h 21m | 961 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| QLK6D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Tamworth Airport (YSTW) | 2026-04-19 05:36 UTC | 2026-04-19 06:20 UTC | 43m |
| N90JX |  | Albuquerque International Sunport Airport (KABQ) | Roswell Air Center Airport (KROW) | 2026-04-19 05:33 UTC | 2026-04-19 06:12 UTC | 39m |
| BBC371 | BBC | VGZR (VGZR) | Tribhuvan International Airport (VNKT) | 2026-04-19 04:51 UTC | 2026-04-19 06:11 UTC | 1h 19m |
| OKPMF | OKP | Pribram Airport (LKPM) | St. Johann In Tirol Airport (LOIJ) | 2026-04-19 05:30 UTC | 2026-04-19 06:10 UTC | 40m |
| 8EV |  | Aldinga Airport (YADG) | Aldinga Airport (YADG) | 2026-04-19 05:52 UTC | 2026-04-19 06:09 UTC | 17m |
| VQBQV | VQB | Narita International Airport (RJAA) | Kansai International Airport (RJBB) | 2026-04-19 05:20 UTC | 2026-04-19 06:08 UTC | 48m |
| TWY522 | TWY | Van Nuys Airport (KVNY) | Moffett Federal Airfield (KNUQ) | 2026-04-19 05:24 UTC | 2026-04-19 06:06 UTC | 42m |
| APG227 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-04-19 05:42 UTC | 2026-04-19 06:05 UTC | 23m |
| AEE241 | AEE | Ikaria Airport (LGIK) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-19 05:23 UTC | 2026-04-19 06:05 UTC | 41m |
| EJU79TX | EJU | Malpensa International Airport (LIMC) | Dusseldorf International Airport (EDDL) | 2026-04-19 04:52 UTC | 2026-04-19 06:02 UTC | 1h 10m |
| SHA222 | SHA | Baitadi Airport (VNBT) | Langtang Airport (VNLT) | 2026-04-19 05:04 UTC | 2026-04-19 06:01 UTC | 57m |
| AYT101 | AYT | Hatzor Air Base (LLHS) | Mitzpe Ramon Airfield (LLMR) | 2026-04-19 05:45 UTC | 2026-04-19 05:58 UTC | 13m |
| VLG5QN | Vueling | Palma De Mallorca Airport (LEPA) | Bilbao Airport (LEBB) | 2026-04-19 05:03 UTC | 2026-04-19 05:58 UTC | 54m |
| RXA6133 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-04-19 05:11 UTC | 2026-04-19 05:57 UTC | 46m |
| ALFT | ALF | 3WA1 (3WA1) | Boeing Field/King County International Airport (KBFI) | 2026-04-19 05:34 UTC | 2026-04-19 05:57 UTC | 22m |
| BTN700 | BTN | Bagdogra Airport (VEBD) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-19 05:13 UTC | 2026-04-19 05:55 UTC | 41m |
| THA570 | Thai Airways | Suvarnabhumi Airport (VTBS) | Wattay International Airport (VLVT) | 2026-04-19 05:06 UTC | 2026-04-19 05:51 UTC | 44m |
| EAI34A | EAI | Dublin Airport (EIDW) | Donegal Airport (EIDL) | 2026-04-19 05:16 UTC | 2026-04-19 05:47 UTC | 30m |
| THY8FW | Turkish Airlines | Istanbul Hezarfen Airfield (LTBW) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-19 04:51 UTC | 2026-04-19 05:45 UTC | 54m |
| APJ165 | APJ | Kansai International Airport (RJBB) | Saga Airport (RJFS) | 2026-04-19 05:02 UTC | 2026-04-19 05:45 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
