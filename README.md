# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_20:29:46_UTC-green)

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

**Latest saved flight:** 2026-04-19 20:29:46 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-19 20:29:46 UTC

- **43,984** saved flights
- **18,309** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **43,984** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **528,791.8 tonnes** estimated CO2 emissions
- **30,654,594 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1863 |
| 2 | SkyWest Airlines | 1708 |
| 3 | IndiGo | 1071 |
| 4 | EJA | 756 |
| 5 | American Airlines | 726 |
| 6 | Southwest Airlines | 624 |
| 7 | ENY | 570 |
| 8 | AXM | 446 |
| 9 | Vueling | 439 |
| 10 | Lufthansa | 438 |
| 11 | LATAM Airlines | 435 |
| 12 | All Nippon Airways | 397 |
| 13 | AZU | 385 |
| 14 | Delta Air Lines | 375 |
| 15 | QLK | 354 |
| 16 | LXJ | 348 |
| 17 | WIF | 344 |
| 18 | Swiss International | 338 |
| 19 | AEE | 300 |
| 20 | Alaska Airlines | 297 |
| 21 | EJU | 291 |
| 22 | easyJet | 281 |
| 23 | VIV | 278 |
| 24 | Japan Airlines | 269 |
| 25 | Air France | 250 |
| 26 | United Airlines | 237 |
| 27 | AXB | 232 |
| 28 | JetBlue | 231 |
| 29 | GLO | 230 |
| 30 | EDV | 224 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 34776 |
| 2 | 🇮🇳 IN | 3299 |
| 3 | 🇪🇸 ES | 3245 |
| 4 | 🇦🇺 AU | 3034 |
| 5 | 🇧🇷 BR | 2622 |
| 6 | 🇯🇵 JP | 2411 |
| 7 | 🇮🇹 IT | 2335 |
| 8 | 🇩🇪 DE | 2236 |
| 9 | 🇨🇦 CA | 2141 |
| 10 | 🇨🇴 CO | 2029 |
| 11 | 🇬🇧 GB | 1785 |
| 12 | 🇫🇷 FR | 1683 |
| 13 | 🇲🇽 MX | 1365 |
| 14 | 🇬🇷 GR | 1357 |
| 15 | 🇨🇭 CH | 1203 |
| 16 | 🇳🇴 NO | 1095 |
| 17 | 🇲🇾 MY | 1090 |
| 18 | 🇿🇦 ZA | 917 |
| 19 | 🇳🇿 NZ | 875 |
| 20 | 🇵🇭 PH | 792 |
| 21 | 🇹🇭 TH | 780 |
| 22 | 🇹🇷 TR | 780 |
| 23 | 🇰🇷 KR | 728 |
| 24 | 🇬🇹 GT | 724 |
| 25 | 🇵🇱 PL | 701 |
| 26 | 🇲🇦 MA | 548 |
| 27 | 🇲🇪 ME | 464 |
| 28 | 🇳🇱 NL | 451 |
| 29 | 🇧🇸 BS | 407 |
| 30 | 🇲🇴 MO | 401 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1028 |
| 2 | Tokyo International Airport |  | JP | 825 |
| 3 | Denver International Airport |  | US | 731 |
| 4 | Indira Gandhi International Airport |  | IN | 710 |
| 5 | El Dorado International Airport |  | CO | 708 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 674 |
| 7 | Harry Reid International Airport |  | US | 562 |
| 8 | Guaymaral Airport |  | CO | 556 |
| 9 | La Aurora Airport |  | GT | 534 |
| 10 | Zurich Airport |  | CH | 527 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 433 |
| 12 | Chicago O'Hare International Airport |  | US | 433 |
| 13 | Kuala Lumpur International Airport |  | MY | 432 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 427 |
| 15 | Frankfurt am Main International Airport |  | DE | 412 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 407 |
| 17 | Macau International Airport |  | MO | 401 |
| 18 | Bengaluru International Airport |  | IN | 392 |
| 19 | Madrid Barajas International Airport |  | ES | 391 |
| 20 | Tenerife Norte Airport |  | ES | 388 |
| 21 | Charlotte/Douglas International Airport |  | US | 382 |
| 22 | Congonhas Airport |  | BR | 375 |
| 23 | Ninoy Aquino International Airport |  | PH | 367 |
| 24 | Malpensa International Airport |  | IT | 366 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 333 |
| 26 | Salt Lake City International Airport |  | US | 333 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 328 |
| 28 | Daniel K Inouye International Airport |  | US | 325 |
| 29 | Charles de Gaulle International Airport |  | FR | 324 |
| 30 | Reno/Tahoe International Airport |  | US | 307 |
| 31 | Vitoria/Foronda Airport |  | ES | 307 |
| 32 | Capua Airport |  | IT | 305 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 303 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 297 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 296 |
| 36 | O. R. Tambo International Airport |  | ZA | 294 |
| 37 | Barcelona International Airport |  | ES | 283 |
| 38 | Viracopos International Airport |  | BR | 267 |
| 39 | Don Mueang International Airport |  | TH | 265 |
| 40 | Calgary International Airport |  | CA | 263 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 224 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 204 | 1h 8m | 706 km | 2,483.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 166 | 14m | 114 km | 325.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 160 | 24m | 225 km | 620.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 132 | 28m | 304 km | 692.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 128 | 1h 27m | 910 km | 2,008.6 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 122 | 21m | 244 km | 513.7 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 118 | 19m | 165 km | 335.7 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 117 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 108 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 102 | 26m | 275 km | 483.3 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 96 | 54m | 546 km | 903.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 91 | 44m | 452 km | 709.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 91 | 20m | 99 km | 155.9 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 83 | 1h 11m | 770 km | 1,102.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 77 | 31m | 369 km | 490.1 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 72 | 20m | 147 km | 182.2 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 72 | 20m | 250 km | 311.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 71 | 52m | 556 km | 680.6 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 68 | 26m | 215 km | 251.8 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 23 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 25 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 62 | 13m | 99 km | 106.3 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 61 | 57m | 493 km | 519.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 61 | 1h 52m | 1,304 km | 1,372.3 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 60 | 1h 21m | 961 km | 994.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 0m | 695 km | 707.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RAM801F | Royal Air Maroc | London Heathrow Airport (EGLL) | Mohammed V International Airport (GMMN) | 2026-04-19 17:46 UTC | 2026-04-19 20:29 UTC | 2h 43m |
| N540AW |  | Palo Alto Airport (KPAO) | Las Trancas Airport (17CL) | 2026-04-19 20:11 UTC | 2026-04-19 20:29 UTC | 18m |
| N80790 |  | Dupage Airport (KDPA) | IS63 (IS63) | 2026-04-19 20:03 UTC | 2026-04-19 20:26 UTC | 23m |
| PTXHP | PTX | Sao Joao da Boa Vista Airport (SDJV) | Rachid Saliba Airport (SNRH) | 2026-04-19 20:08 UTC | 2026-04-19 20:25 UTC | 17m |
| N361L |  | Palo Alto Airport (KPAO) | Livermore Municipal Airport (KLVK) | 2026-04-19 19:39 UTC | 2026-04-19 20:18 UTC | 39m |
| N96FA |  | Van Nuys Airport (KVNY) | Riverside Airport (KRAL) | 2026-04-19 19:39 UTC | 2026-04-19 20:18 UTC | 38m |
| N62AZ |  | Hayward Executive Airport (KHWD) | Hayward Executive Airport (KHWD) | 2026-04-19 19:47 UTC | 2026-04-19 20:16 UTC | 29m |
| CPA064 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-04-19 09:01 UTC | 2026-04-19 20:16 UTC | 11h 14m |
| MNB504 | MNB | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-04-19 13:31 UTC | 2026-04-19 20:13 UTC | 6h 42m |
| NWX478 | NWX | Post Oak Airfield (TA19) | Mafrige Ranch Inc Airport (2TA9) | 2026-04-19 20:03 UTC | 2026-04-19 20:13 UTC | 10m |
| N5296Z |  | Searchlight Airport (K1L3) | Henderson Executive Airport (KHND) | 2026-04-19 19:51 UTC | 2026-04-19 20:09 UTC | 17m |
| RFS720 | RFS | Auburn Municipal Airport (KS50) | Renton Municipal Airport (KRNT) | 2026-04-19 19:38 UTC | 2026-04-19 20:07 UTC | 29m |
| N5395H |  | Seattle Paine Field International Airport (KPAE) | Renton Municipal Airport (KRNT) | 2026-04-19 19:36 UTC | 2026-04-19 20:07 UTC | 30m |
| VT504 |  | Faa'a International Airport (NTAA) | Tikehau Airport (NTGC) | 2026-04-19 19:25 UTC | 2026-04-19 20:06 UTC | 41m |
| RFS706 | RFS | Boeing Field/King County International Airport (KBFI) | Renton Municipal Airport (KRNT) | 2026-04-19 19:46 UTC | 2026-04-19 20:05 UTC | 19m |
| N2459S |  | Centennial Airport (KAPA) | Rocky Mountain Metro Airport (KBJC) | 2026-04-19 19:42 UTC | 2026-04-19 20:05 UTC | 22m |
| N172BH |  | Auburn Municipal Airport (KS50) | Auburn Municipal Airport (KS50) | 2026-04-19 19:04 UTC | 2026-04-19 20:02 UTC | 57m |
| N5566A |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-04-19 18:44 UTC | 2026-04-19 19:59 UTC | 1h 15m |
| CGMPE | CGM | Athabasca Airport (CYWM) | Regina Beach Airport (CKL9) | 2026-04-19 18:49 UTC | 2026-04-19 19:59 UTC | 1h 10m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-19 19:44 UTC | 2026-04-19 19:59 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
