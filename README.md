# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_09:44:13_UTC-green)

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

**Latest saved flight:** 2026-04-24 09:44:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-24 09:44:13 UTC

- **50,868** saved flights
- **20,415** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **50,868** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **608,567.1 tonnes** estimated CO2 emissions
- **35,279,251 km** total distance flown
- **834 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2140 |
| 2 | SkyWest Airlines | 1940 |
| 3 | IndiGo | 1181 |
| 4 | EJA | 878 |
| 5 | American Airlines | 822 |
| 6 | Southwest Airlines | 723 |
| 7 | ENY | 651 |
| 8 | Lufthansa | 586 |
| 9 | Vueling | 508 |
| 10 | AXM | 500 |
| 11 | LATAM Airlines | 492 |
| 12 | All Nippon Airways | 462 |
| 13 | AZU | 430 |
| 14 | Delta Air Lines | 419 |
| 15 | WIF | 419 |
| 16 | QLK | 410 |
| 17 | Swiss International | 384 |
| 18 | LXJ | 382 |
| 19 | AEE | 344 |
| 20 | Alaska Airlines | 337 |
| 21 | EJU | 326 |
| 22 | VIV | 322 |
| 23 | easyJet | 319 |
| 24 | Japan Airlines | 302 |
| 25 | Air France | 288 |
| 26 | AXB | 272 |
| 27 | Cathay Pacific | 268 |
| 28 | JetBlue | 263 |
| 29 | United Airlines | 263 |
| 30 | AIQ | 259 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 40389 |
| 2 | 🇮🇳 IN | 3714 |
| 3 | 🇪🇸 ES | 3673 |
| 4 | 🇦🇺 AU | 3550 |
| 5 | 🇧🇷 BR | 2932 |
| 6 | 🇯🇵 JP | 2785 |
| 7 | 🇮🇹 IT | 2722 |
| 8 | 🇩🇪 DE | 2700 |
| 9 | 🇨🇦 CA | 2540 |
| 10 | 🇨🇴 CO | 2347 |
| 11 | 🇬🇧 GB | 2091 |
| 12 | 🇫🇷 FR | 1947 |
| 13 | 🇲🇽 MX | 1571 |
| 14 | 🇬🇷 GR | 1539 |
| 15 | 🇨🇭 CH | 1402 |
| 16 | 🇳🇴 NO | 1365 |
| 17 | 🇲🇾 MY | 1223 |
| 18 | 🇿🇦 ZA | 1046 |
| 19 | 🇳🇿 NZ | 984 |
| 20 | 🇹🇭 TH | 930 |
| 21 | 🇹🇷 TR | 904 |
| 22 | 🇵🇭 PH | 887 |
| 23 | 🇰🇷 KR | 851 |
| 24 | 🇵🇱 PL | 818 |
| 25 | 🇬🇹 GT | 771 |
| 26 | 🇲🇦 MA | 624 |
| 27 | 🇲🇪 ME | 544 |
| 28 | 🇳🇱 NL | 512 |
| 29 | 🇲🇴 MO | 484 |
| 30 | 🇧🇸 BS | 444 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1176 |
| 2 | Tokyo International Airport |  | JP | 947 |
| 3 | Denver International Airport |  | US | 844 |
| 4 | El Dorado International Airport |  | CO | 803 |
| 5 | Indira Gandhi International Airport |  | IN | 793 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 761 |
| 7 | Guaymaral Airport |  | CO | 688 |
| 8 | Harry Reid International Airport |  | US | 667 |
| 9 | Zurich Airport |  | CH | 594 |
| 10 | La Aurora Airport |  | GT | 574 |
| 11 | Frankfurt am Main International Airport |  | DE | 568 |
| 12 | Chicago O'Hare International Airport |  | US | 503 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 495 |
| 14 | Kuala Lumpur International Airport |  | MY | 487 |
| 15 | Macau International Airport |  | MO | 484 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 482 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 464 |
| 18 | Madrid Barajas International Airport |  | ES | 462 |
| 19 | Bengaluru International Airport |  | IN | 442 |
| 20 | Charlotte/Douglas International Airport |  | US | 426 |
| 21 | Congonhas Airport |  | BR | 420 |
| 22 | Malpensa International Airport |  | IT | 418 |
| 23 | Ninoy Aquino International Airport |  | PH | 409 |
| 24 | Tenerife Norte Airport |  | ES | 408 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 383 |
| 26 | Charles de Gaulle International Airport |  | FR | 379 |
| 27 | Salt Lake City International Airport |  | US | 377 |
| 28 | Daniel K Inouye International Airport |  | US | 374 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 370 |
| 30 | Capua Airport |  | IT | 354 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 345 |
| 32 | Vitoria/Foronda Airport |  | ES | 344 |
| 33 | Reno/Tahoe International Airport |  | US | 342 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 342 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 340 |
| 36 | Barcelona International Airport |  | ES | 338 |
| 37 | O. R. Tambo International Airport |  | ZA | 335 |
| 38 | Don Mueang International Airport |  | TH | 315 |
| 39 | Calgary International Airport |  | CA | 309 |
| 40 | Viracopos International Airport |  | BR | 299 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 278 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 239 | 1h 7m | 706 km | 2,909.8 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 194 | 14m | 114 km | 380.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 174 | 24m | 225 km | 675.0 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 153 | 21m | 244 km | 644.2 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 153 | 28m | 304 km | 802.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 146 | 1h 27m | 910 km | 2,291.1 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 135 | 19m | 165 km | 384.0 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 128 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 122 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 118 | 26m | 275 km | 559.2 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 104 | 44m | 452 km | 810.5 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 94 | 20m | 99 km | 161.0 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 90 | 1h 11m | 770 km | 1,195.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 87 | 31m | 369 km | 553.8 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 87 | 20m | 250 km | 375.8 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 82 | 26m | 215 km | 303.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 81 | 20m | 147 km | 205.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 80 | 52m | 556 km | 766.9 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 73 | 1h 41m | 1,156 km | 1,456.3 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 72 | 1h 0m | 695 km | 863.1 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 70 | 58m | 493 km | 595.5 t |
| 26 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 67 | 12m | 15 km | 17.7 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 30 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 65 | 16m | 162 km | 182.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HKS40 | HKS | Norwich International Airport (EGSH) | Beverley/Linley Hill Airport (EGNY) | 2026-04-24 09:00 UTC | 2026-04-24 09:44 UTC | 44m |
| YGQ | YGQ | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-04-24 08:50 UTC | 2026-04-24 09:28 UTC | 38m |
| NIVAL04 | NIV | Rota Naval Station Airport (LERT) | Rota Naval Station Airport (LERT) | 2026-04-24 08:35 UTC | 2026-04-24 09:26 UTC | 50m |
| KAYI0004 | KAY | Sinop Airport (LTCM) | Sinop Airport (LTCM) | 2026-04-24 09:13 UTC | 2026-04-24 09:26 UTC | 12m |
| CSR102 | CSR | Pierrelatte Airport (LFHD) | Nimes-Arles-Camargue Airport (LFTW) | 2026-04-24 09:03 UTC | 2026-04-24 09:23 UTC | 19m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-04-23 21:56 UTC | 2026-04-24 09:23 UTC | 11h 26m |
| BAW626 | British Airways | London Heathrow Airport (EGLL) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-24 06:03 UTC | 2026-04-24 09:17 UTC | 3h 14m |
| BNOR | BNO | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-24 09:00 UTC | 2026-04-24 09:14 UTC | 14m |
| ZSBPD | ZSB | O. R. Tambo International Airport (FAOR) | Hartebeespoortdam Airport (FAHB) | 2026-04-24 08:37 UTC | 2026-04-24 09:12 UTC | 34m |
| BNO92J | BNO | Bergen Airport Flesland (ENBR) | Trondheim Airport Vaernes (ENVA) | 2026-04-24 08:20 UTC | 2026-04-24 09:10 UTC | 49m |
| RYR8831 | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-04-24 08:18 UTC | 2026-04-24 09:08 UTC | 50m |
| SWR7AK | Swiss International | Nice-Cote d'Azur Airport (LFMN) | Zurich Airport (LSZH) | 2026-04-24 08:04 UTC | 2026-04-24 09:02 UTC | 58m |
| LR5184 |  | Coffs Harbour Airport (YSCH) | Woodville Airport (YWVL) | 2026-04-24 08:41 UTC | 2026-04-24 08:55 UTC | 14m |
| WIF6F | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-24 08:39 UTC | 2026-04-24 08:53 UTC | 14m |
| SWR3KH | Swiss International | Václav Havel Airport (LKPR) | Zurich Airport (LSZH) | 2026-04-24 07:56 UTC | 2026-04-24 08:53 UTC | 56m |
| AFR188 | Air France | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-04-23 21:46 UTC | 2026-04-24 08:53 UTC | 11h 6m |
| DAL2186 | Delta Air Lines | Seattle-Tacoma International Airport (KSEA) | Fairbanks International Airport (PAFA) | 2026-04-24 05:13 UTC | 2026-04-24 08:53 UTC | 3h 39m |
| BPO318 | BPO | Bonn-Hangelar Airport (EDKB) | Wershofen/Eifel Airport (EDRV) | 2026-04-24 07:34 UTC | 2026-04-24 08:52 UTC | 1h 18m |
| EJU629M | EJU | Nice-Cote d'Azur Airport (LFMN) | La Roche-sur-Yon Airport (LFRI) | 2026-04-24 07:28 UTC | 2026-04-24 08:51 UTC | 1h 22m |
| EWG6TQ | EWG | Vienna International Airport (LOWW) | Dusseldorf International Airport (EDDL) | 2026-04-24 07:32 UTC | 2026-04-24 08:48 UTC | 1h 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
