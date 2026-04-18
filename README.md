# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_11:50:59_UTC-green)

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

**Latest saved flight:** 2026-04-18 11:50:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-18 11:50:59 UTC

- **41,031** saved flights
- **17,376** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **41,031** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **493,906.0 tonnes** estimated CO2 emissions
- **28,632,233 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1723 |
| 2 | SkyWest Airlines | 1590 |
| 3 | IndiGo | 1014 |
| 4 | EJA | 712 |
| 5 | American Airlines | 681 |
| 6 | Southwest Airlines | 576 |
| 7 | ENY | 523 |
| 8 | AXM | 430 |
| 9 | Vueling | 412 |
| 10 | LATAM Airlines | 401 |
| 11 | Lufthansa | 397 |
| 12 | All Nippon Airways | 374 |
| 13 | AZU | 364 |
| 14 | Delta Air Lines | 348 |
| 15 | QLK | 341 |
| 16 | LXJ | 325 |
| 17 | WIF | 321 |
| 18 | Swiss International | 312 |
| 19 | Alaska Airlines | 277 |
| 20 | AEE | 273 |
| 21 | EJU | 268 |
| 22 | easyJet | 268 |
| 23 | VIV | 264 |
| 24 | Japan Airlines | 256 |
| 25 | Air France | 234 |
| 26 | United Airlines | 222 |
| 27 | JetBlue | 220 |
| 28 | EDV | 216 |
| 29 | GLO | 213 |
| 30 | AXB | 211 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 32305 |
| 2 | 🇮🇳 IN | 3091 |
| 3 | 🇪🇸 ES | 3032 |
| 4 | 🇦🇺 AU | 2910 |
| 5 | 🇧🇷 BR | 2425 |
| 6 | 🇯🇵 JP | 2277 |
| 7 | 🇮🇹 IT | 2136 |
| 8 | 🇩🇪 DE | 2063 |
| 9 | 🇨🇦 CA | 2010 |
| 10 | 🇨🇴 CO | 1952 |
| 11 | 🇬🇧 GB | 1669 |
| 12 | 🇫🇷 FR | 1579 |
| 13 | 🇲🇽 MX | 1291 |
| 14 | 🇬🇷 GR | 1235 |
| 15 | 🇨🇭 CH | 1131 |
| 16 | 🇲🇾 MY | 1045 |
| 17 | 🇳🇴 NO | 1019 |
| 18 | 🇿🇦 ZA | 853 |
| 19 | 🇳🇿 NZ | 844 |
| 20 | 🇵🇭 PH | 754 |
| 21 | 🇹🇭 TH | 731 |
| 22 | 🇹🇷 TR | 719 |
| 23 | 🇬🇹 GT | 690 |
| 24 | 🇰🇷 KR | 686 |
| 25 | 🇵🇱 PL | 646 |
| 26 | 🇲🇦 MA | 502 |
| 27 | 🇳🇱 NL | 420 |
| 28 | 🇲🇪 ME | 415 |
| 29 | 🇧🇸 BS | 387 |
| 30 | 🇮🇩 ID | 378 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 946 |
| 2 | Tokyo International Airport |  | JP | 778 |
| 3 | El Dorado International Airport |  | CO | 688 |
| 4 | Denver International Airport |  | US | 678 |
| 5 | Indira Gandhi International Airport |  | IN | 666 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 613 |
| 7 | Harry Reid International Airport |  | US | 531 |
| 8 | Guaymaral Airport |  | CO | 516 |
| 9 | La Aurora Airport |  | GT | 509 |
| 10 | Zurich Airport |  | CH | 495 |
| 11 | Kuala Lumpur International Airport |  | MY | 411 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 404 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 399 |
| 14 | Chicago O'Hare International Airport |  | US | 392 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 392 |
| 16 | Macau International Airport |  | MO | 374 |
| 17 | Madrid Barajas International Airport |  | ES | 371 |
| 18 | Frankfurt am Main International Airport |  | DE | 363 |
| 19 | Bengaluru International Airport |  | IN | 363 |
| 20 | Tenerife Norte Airport |  | ES | 361 |
| 21 | Charlotte/Douglas International Airport |  | US | 358 |
| 22 | Congonhas Airport |  | BR | 354 |
| 23 | Ninoy Aquino International Airport |  | PH | 350 |
| 24 | Malpensa International Airport |  | IT | 332 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 322 |
| 26 | Salt Lake City International Airport |  | US | 313 |
| 27 | Daniel K Inouye International Airport |  | US | 306 |
| 28 | Charles de Gaulle International Airport |  | FR | 303 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 297 |
| 30 | Vitoria/Foronda Airport |  | ES | 288 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 283 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 281 |
| 33 | Reno/Tahoe International Airport |  | US | 280 |
| 34 | O. R. Tambo International Airport |  | ZA | 276 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 276 |
| 36 | Capua Airport |  | IT | 274 |
| 37 | Barcelona International Airport |  | ES | 262 |
| 38 | Viracopos International Airport |  | BR | 250 |
| 39 | Calgary International Airport |  | CA | 247 |
| 40 | Don Mueang International Airport |  | TH | 243 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 206 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 196 | 1h 7m | 706 km | 2,386.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 150 | 24m | 225 km | 581.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 124 | 28m | 304 km | 650.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 120 | 1h 27m | 910 km | 1,883.1 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 111 | 31m | - | - |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 110 | 19m | 165 km | 312.9 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 109 | 21m | 244 km | 459.0 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 103 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 97 | 26m | 275 km | 459.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 91 | 54m | 546 km | 856.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 86 | 21m | 99 km | 147.3 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 85 | 44m | 452 km | 662.5 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 82 | 1h 11m | 770 km | 1,089.3 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 75 | 31m | 369 km | 477.4 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 75 | 27m | 152 km | 196.0 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 67 | 20m | 250 km | 289.4 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 66 | 52m | 556 km | 632.7 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 65 | 20m | 147 km | 164.5 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 63 | 26m | 215 km | 233.3 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 62 | 16m | 162 km | 173.8 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 59 | 12m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 53m | 1,304 km | 1,327.3 t |
| 28 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 57 | 14m | 154 km | 151.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 57 | 1h 21m | 961 km | 944.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UZB232 | UZB | Frankfurt am Main International Airport (EDDF) | Smolensk North Airport (XUBS) | 2026-04-18 10:07 UTC | 2026-04-18 11:50 UTC | 1h 43m |
| STW002 | STW | Sheremetyevo International Airport (UUEE) | Smolensk North Airport (XUBS) | 2026-04-18 10:38 UTC | 2026-04-18 11:20 UTC | 42m |
| HRD07 | HRD | West Virginia International Yeager Airport (KCRW) | West Virginia International Yeager Airport (KCRW) | 2026-04-18 10:53 UTC | 2026-04-18 11:12 UTC | 18m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-04-18 11:02 UTC | 2026-04-18 11:08 UTC | 6m |
| HB3411 |  | Bern Belp Airport (LSZB) | Bern Belp Airport (LSZB) | 2026-04-18 08:19 UTC | 2026-04-18 11:00 UTC | 2h 41m |
| FGKDM | FGK | Lyon Corbas Airport (LFHJ) | Lyon Corbas Airport (LFHJ) | 2026-04-18 08:49 UTC | 2026-04-18 10:59 UTC | 2h 9m |
| PSGBJ | PSG | Fazenda Colorado Airport (SWFC) | Rio Ouro Airport (SIOM) | 2026-04-18 09:57 UTC | 2026-04-18 10:58 UTC | 1h 0m |
| FJIMU | FJI | Le Mans-Arnage Airport (LFRM) | Le Mans-Arnage Airport (LFRM) | 2026-04-18 10:56 UTC | 2026-04-18 10:58 UTC | 1m |
| HB2340 |  | Lodrino Air Base (LSML) | Lodrino Air Base (LSML) | 2026-04-18 10:32 UTC | 2026-04-18 10:51 UTC | 18m |
| DRAGO382 | DRA | L'alpe D'huez Airport (LFHU) | L'alpe D'huez Airport (LFHU) | 2026-04-18 10:43 UTC | 2026-04-18 10:47 UTC | 4m |
| FDR967 | FDR | O. R. Tambo International Airport (FAOR) | Pilanesberg International Airport (FAPN) | 2026-04-18 10:19 UTC | 2026-04-18 10:47 UTC | 28m |
| JAL613M | Japan Airlines | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 2026-04-18 09:25 UTC | 2026-04-18 10:45 UTC | 1h 20m |
| RYR88DM | Ryanair | London Stansted Airport (EGSS) | Ussel-Thalamy Airport (LFCU) | 2026-04-18 09:42 UTC | 2026-04-18 10:45 UTC | 1h 2m |
| RYR98SG | Ryanair | Copenhagen Kastrup Airport (EKCH) | Roudnice Mad Airport (LKRO) | 2026-04-18 09:44 UTC | 2026-04-18 10:42 UTC | 58m |
| ANA683 | All Nippon Airways | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 2026-04-18 09:52 UTC | 2026-04-18 10:41 UTC | 49m |
| KAL1847 | Korean Air | Gimpo International Airport (RKSS) | Daegu Airport (RKTN) | 2026-04-18 10:12 UTC | 2026-04-18 10:40 UTC | 27m |
| LOT3KY | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | LBVR (LBVR) | 2026-04-18 09:19 UTC | 2026-04-18 10:39 UTC | 1h 19m |
| OEKMT | OEK | Stalowa Wola-Turbia Airport (EPST) | Mielec Airport (EPML) | 2026-04-18 10:15 UTC | 2026-04-18 10:38 UTC | 22m |
| AEA18QC | AEA | Palma De Mallorca Airport (LEPA) | Vitoria/Foronda Airport (LEVT) | 2026-04-18 09:48 UTC | 2026-04-18 10:38 UTC | 49m |
| OAL068 | OAL | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 2026-04-18 10:18 UTC | 2026-04-18 10:37 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
