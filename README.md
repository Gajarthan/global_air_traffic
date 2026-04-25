# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_01:36:17_UTC-green)

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

**Latest saved flight:** 2026-04-25 01:36:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-25 01:36:17 UTC

- **52,923** saved flights
- **21,120** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **52,923** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **632,405.4 tonnes** estimated CO2 emissions
- **36,661,184 km** total distance flown
- **834 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2217 |
| 2 | SkyWest Airlines | 2007 |
| 3 | IndiGo | 1197 |
| 4 | EJA | 943 |
| 5 | American Airlines | 856 |
| 6 | Southwest Airlines | 753 |
| 7 | ENY | 671 |
| 8 | Lufthansa | 614 |
| 9 | Vueling | 529 |
| 10 | AXM | 510 |
| 11 | LATAM Airlines | 509 |
| 12 | All Nippon Airways | 467 |
| 13 | AZU | 449 |
| 14 | Delta Air Lines | 438 |
| 15 | WIF | 437 |
| 16 | QLK | 412 |
| 17 | Swiss International | 402 |
| 18 | LXJ | 392 |
| 19 | AEE | 355 |
| 20 | Alaska Airlines | 351 |
| 21 | VIV | 337 |
| 22 | easyJet | 333 |
| 23 | EJU | 332 |
| 24 | Japan Airlines | 307 |
| 25 | Air France | 303 |
| 26 | AXB | 280 |
| 27 | Cathay Pacific | 280 |
| 28 | JetBlue | 272 |
| 29 | United Airlines | 272 |
| 30 | AIQ | 267 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 42340 |
| 2 | 🇪🇸 ES | 3806 |
| 3 | 🇮🇳 IN | 3773 |
| 4 | 🇦🇺 AU | 3586 |
| 5 | 🇧🇷 BR | 3057 |
| 6 | 🇯🇵 JP | 2830 |
| 7 | 🇮🇹 IT | 2828 |
| 8 | 🇩🇪 DE | 2802 |
| 9 | 🇨🇦 CA | 2655 |
| 10 | 🇨🇴 CO | 2444 |
| 11 | 🇬🇧 GB | 2192 |
| 12 | 🇫🇷 FR | 2045 |
| 13 | 🇲🇽 MX | 1639 |
| 14 | 🇬🇷 GR | 1587 |
| 15 | 🇨🇭 CH | 1474 |
| 16 | 🇳🇴 NO | 1420 |
| 17 | 🇲🇾 MY | 1244 |
| 18 | 🇿🇦 ZA | 1087 |
| 19 | 🇳🇿 NZ | 1003 |
| 20 | 🇹🇭 TH | 949 |
| 21 | 🇹🇷 TR | 949 |
| 22 | 🇵🇭 PH | 907 |
| 23 | 🇰🇷 KR | 858 |
| 24 | 🇵🇱 PL | 840 |
| 25 | 🇬🇹 GT | 814 |
| 26 | 🇲🇦 MA | 653 |
| 27 | 🇲🇪 ME | 563 |
| 28 | 🇳🇱 NL | 533 |
| 29 | 🇲🇴 MO | 512 |
| 30 | 🇧🇸 BS | 462 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1214 |
| 2 | Tokyo International Airport |  | JP | 961 |
| 3 | Denver International Airport |  | US | 881 |
| 4 | El Dorado International Airport |  | CO | 830 |
| 5 | Indira Gandhi International Airport |  | IN | 807 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 788 |
| 7 | Guaymaral Airport |  | CO | 730 |
| 8 | Harry Reid International Airport |  | US | 687 |
| 9 | Zurich Airport |  | CH | 618 |
| 10 | La Aurora Airport |  | GT | 608 |
| 11 | Frankfurt am Main International Airport |  | DE | 601 |
| 12 | Chicago O'Hare International Airport |  | US | 524 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 520 |
| 14 | Macau International Airport |  | MO | 512 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 506 |
| 16 | Kuala Lumpur International Airport |  | MY | 494 |
| 17 | Madrid Barajas International Airport |  | ES | 488 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 469 |
| 19 | Bengaluru International Airport |  | IN | 449 |
| 20 | Congonhas Airport |  | BR | 442 |
| 21 | Malpensa International Airport |  | IT | 439 |
| 22 | Charlotte/Douglas International Airport |  | US | 435 |
| 23 | Ninoy Aquino International Airport |  | PH | 419 |
| 24 | Tenerife Norte Airport |  | ES | 415 |
| 25 | Charles de Gaulle International Airport |  | FR | 399 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 397 |
| 27 | Salt Lake City International Airport |  | US | 393 |
| 28 | Daniel K Inouye International Airport |  | US | 384 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 378 |
| 30 | Capua Airport |  | IT | 370 |
| 31 | Vitoria/Foronda Airport |  | ES | 358 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 357 |
| 33 | Reno/Tahoe International Airport |  | US | 355 |
| 34 | Barcelona International Airport |  | ES | 354 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 350 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 350 |
| 37 | O. R. Tambo International Airport |  | ZA | 343 |
| 38 | Don Mueang International Airport |  | TH | 321 |
| 39 | Calgary International Airport |  | CA | 320 |
| 40 | Viracopos International Airport |  | BR | 312 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 295 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 243 | 1h 7m | 706 km | 2,958.5 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 200 | 14m | 114 km | 392.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 175 | 24m | 225 km | 678.9 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 160 | 21m | 244 km | 673.7 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 153 | 28m | 304 km | 802.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 149 | 1h 27m | 910 km | 2,338.2 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 136 | 19m | 165 km | 386.9 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 131 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 129 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 123 | 26m | 275 km | 582.8 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 105 | 44m | 452 km | 818.3 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 98 | 20m | 99 km | 167.9 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 94 | 1h 11m | 770 km | 1,248.7 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 92 | 31m | 369 km | 585.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 88 | 20m | 250 km | 380.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 87 | 27m | 215 km | 322.2 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 83 | 20m | 147 km | 210.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 83 | 52m | 556 km | 795.6 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 81 | 27m | 152 km | 211.7 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 76 | 1h 1m | 695 km | 911.0 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 75 | 1h 41m | 1,156 km | 1,496.2 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 75 | 13m | 99 km | 128.6 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 70 | 58m | 493 km | 595.5 t |
| 26 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 69 | 12m | 15 km | 18.2 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 69 | 1h 53m | 1,304 km | 1,552.3 t |
| 28 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 68 | 24m | 55 km | 64.6 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 67 | 16m | 162 km | 187.8 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 67 | 1h 20m | 961 km | 1,110.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N39JM |  | Ralph M Hall/Rockwall Municipal Airport (KF46) | Austin Executive Airport (KEDC) | 2026-04-24 23:56 UTC | 2026-04-25 01:36 UTC | 1h 39m |
| TKR169 | TKR | 6CO3 (6CO3) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-25 01:07 UTC | 2026-04-25 01:25 UTC | 18m |
| N235CD |  | West Virginia International Yeager Airport (KCRW) | Richwood Municipal Airport (K3I4) | 2026-04-25 00:57 UTC | 2026-04-25 01:25 UTC | 28m |
| N658LM |  | Cobb County International/Mccollum Field (KRYY) | Cobb County International/Mccollum Field (KRYY) | 2026-04-25 01:14 UTC | 2026-04-25 01:17 UTC | 3m |
| RDHK765 | RDH | Aberdeen Field (31VA) | Norfolk Ns (Chambers Field) Airport (KNGU) | 2026-04-25 01:07 UTC | 2026-04-25 01:16 UTC | 9m |
| N98485 |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-04-25 00:38 UTC | 2026-04-25 01:09 UTC | 31m |
| N107MY |  | Truckee-Tahoe Airport (KTRK) | Palo Alto Airport (KPAO) | 2026-04-25 00:24 UTC | 2026-04-25 01:08 UTC | 43m |
| N1507X |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-04-25 00:48 UTC | 2026-04-25 01:07 UTC | 19m |
| AES | AES | Sydney Kingsford Smith International Airport (YSSY) | Sydney Kingsford Smith International Airport (YSSY) | 2026-04-25 01:05 UTC | 2026-04-25 01:06 UTC | 0m |
| SKW5837 | SkyWest Airlines | Boise Air Trml/Gowen Field (KBOI) | Denver International Airport (KDEN) | 2026-04-24 23:32 UTC | 2026-04-25 01:06 UTC | 1h 33m |
| BOV709 | BOV | Ministro Pistarini International Airport (SAEZ) | Laja Airport (SLLJ) | 2026-04-24 19:54 UTC | 2026-04-25 00:56 UTC | 5h 1m |
| ZKLTE | ZKL | Hood Airport (NZMS) | Hood Airport (NZMS) | 2026-04-25 00:50 UTC | 2026-04-25 00:56 UTC | 5m |
| TKR16 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | 6CO3 (6CO3) | 2026-04-25 00:36 UTC | 2026-04-25 00:55 UTC | 19m |
| PNC0927 | PNC | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-25 00:14 UTC | 2026-04-25 00:55 UTC | 41m |
| TAM3964 | LATAM Airlines | Congonhas Airport (SBSP) | Clube de Marte Ibira de Para-Quedismo Airport (SWYV) | 2026-04-25 00:15 UTC | 2026-04-25 00:54 UTC | 38m |
| QXE2342 | QXE | Seattle-Tacoma International Airport (KSEA) | 6CL6 (6CL6) | 2026-04-24 23:15 UTC | 2026-04-25 00:49 UTC | 1h 34m |
| N637AS |  | Mc Clellan-Palomar Airport (KCRQ) | Borrego Valley Airport (KL08) | 2026-04-25 00:28 UTC | 2026-04-25 00:43 UTC | 14m |
| N913TC |  | Palo Alto Airport (KPAO) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-04-25 00:29 UTC | 2026-04-25 00:40 UTC | 11m |
| N250MM |  | Matehuala Airport (MM67) | Quetzalcoatl International Airport (MMNL) | 2026-04-24 23:36 UTC | 2026-04-25 00:38 UTC | 1h 2m |
| AIQ3370 | AIQ | Don Mueang International Airport (VTBD) | Surin Airport (VTUJ) | 2026-04-25 00:06 UTC | 2026-04-25 00:38 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
