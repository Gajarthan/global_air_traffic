# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_12:10:02_UTC-green)

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

**Latest saved flight:** 2026-04-11 12:10:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-11 12:10:02 UTC

- **28,579** saved flights
- **13,325** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **28,579** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **348,204.4 tonnes** estimated CO2 emissions
- **20,185,764 km** total distance flown
- **842 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1168 |
| 2 | SkyWest Airlines | 1155 |
| 3 | IndiGo | 754 |
| 4 | EJA | 502 |
| 5 | American Airlines | 495 |
| 6 | Southwest Airlines | 406 |
| 7 | ENY | 382 |
| 8 | Lufthansa | 349 |
| 9 | AXM | 310 |
| 10 | Vueling | 293 |
| 11 | LATAM Airlines | 276 |
| 12 | All Nippon Airways | 263 |
| 13 | QLK | 254 |
| 14 | Delta Air Lines | 240 |
| 15 | AZU | 237 |
| 16 | LXJ | 232 |
| 17 | Swiss International | 207 |
| 18 | Alaska Airlines | 190 |
| 19 | Japan Airlines | 190 |
| 20 | easyJet | 186 |
| 21 | WIF | 185 |
| 22 | EJU | 184 |
| 23 | VIV | 184 |
| 24 | AEE | 180 |
| 25 | United Airlines | 174 |
| 26 | EDV | 166 |
| 27 | Avianca | 160 |
| 28 | AXB | 150 |
| 29 | JetBlue | 150 |
| 30 | Air France | 146 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 22475 |
| 2 | 🇮🇳 IN | 2320 |
| 3 | 🇪🇸 ES | 2109 |
| 4 | 🇦🇺 AU | 2086 |
| 5 | 🇧🇷 BR | 1607 |
| 6 | 🇯🇵 JP | 1604 |
| 7 | 🇮🇹 IT | 1453 |
| 8 | 🇩🇪 DE | 1440 |
| 9 | 🇨🇴 CO | 1411 |
| 10 | 🇨🇦 CA | 1395 |
| 11 | 🇬🇧 GB | 1158 |
| 12 | 🇫🇷 FR | 1054 |
| 13 | 🇲🇽 MX | 900 |
| 14 | 🇬🇷 GR | 822 |
| 15 | 🇨🇭 CH | 798 |
| 16 | 🇲🇾 MY | 743 |
| 17 | 🇳🇿 NZ | 634 |
| 18 | 🇳🇴 NO | 622 |
| 19 | 🇿🇦 ZA | 593 |
| 20 | 🇵🇭 PH | 545 |
| 21 | 🇬🇹 GT | 525 |
| 22 | 🇹🇷 TR | 520 |
| 23 | 🇹🇭 TH | 511 |
| 24 | 🇰🇷 KR | 497 |
| 25 | 🇵🇱 PL | 432 |
| 26 | 🇲🇦 MA | 350 |
| 27 | 🇧🇸 BS | 296 |
| 28 | 🇲🇪 ME | 286 |
| 29 | 🇳🇱 NL | 279 |
| 30 | 🇮🇩 ID | 276 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 676 |
| 2 | Tokyo International Airport |  | JP | 539 |
| 3 | El Dorado International Airport |  | CO | 512 |
| 4 | Indira Gandhi International Airport |  | IN | 484 |
| 5 | Denver International Airport |  | US | 478 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 402 |
| 7 | La Aurora Airport |  | GT | 370 |
| 8 | Harry Reid International Airport |  | US | 365 |
| 9 | Zurich Airport |  | CH | 342 |
| 10 | Guaymaral Airport |  | CO | 312 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 297 |
| 12 | Chicago O'Hare International Airport |  | US | 294 |
| 13 | Frankfurt am Main International Airport |  | DE | 293 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 290 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 289 |
| 16 | Kuala Lumpur International Airport |  | MY | 278 |
| 17 | Macau International Airport |  | MO | 263 |
| 18 | Bengaluru International Airport |  | IN | 260 |
| 19 | Charlotte/Douglas International Airport |  | US | 257 |
| 20 | Ninoy Aquino International Airport |  | PH | 250 |
| 21 | Madrid Barajas International Airport |  | ES | 247 |
| 22 | Tenerife Norte Airport |  | ES | 246 |
| 23 | Congonhas Airport |  | BR | 231 |
| 24 | Malpensa International Airport |  | IT | 223 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 221 |
| 26 | Salt Lake City International Airport |  | US | 220 |
| 27 | Daniel K Inouye International Airport |  | US | 219 |
| 28 | Reno/Tahoe International Airport |  | US | 210 |
| 29 | Charles de Gaulle International Airport |  | FR | 201 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 196 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 194 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 192 |
| 33 | Miami International Airport |  | US | 189 |
| 34 | Capua Airport |  | IT | 188 |
| 35 | O. R. Tambo International Airport |  | ZA | 187 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 187 |
| 37 | Seattle-Tacoma International Airport |  | US | 181 |
| 38 | Vitoria/Foronda Airport |  | ES | 179 |
| 39 | Barcelona International Airport |  | ES | 179 |
| 40 | Don Mueang International Airport |  | TH | 173 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 138 | 1h 8m | 706 km | 1,680.2 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 119 | 27m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 115 | 14m | 114 km | 225.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 109 | 24m | 225 km | 422.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 100 | 28m | 304 km | 524.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 86 | 1h 27m | 910 km | 1,349.5 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 74 | 21m | 99 km | 126.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 73 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 72 | 19m | 165 km | 204.8 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 65 | 55m | 546 km | 612.0 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 62 | 1h 12m | 770 km | 823.6 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 58 | 27m | 275 km | 274.8 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 56 | 31m | 369 km | 356.5 t |
| 17 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 55 | 9m | - | - |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 53 | 46m | 452 km | 413.1 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 51 | 52m | 556 km | 488.9 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 47 | 20m | 250 km | 203.0 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 46 | 1h 42m | 1,423 km | 1,128.9 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 46 | 13m | 99 km | 78.9 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 45 | 20m | 147 km | 113.9 t |
| 25 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 27 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 44 | 21m | 244 km | 185.3 t |
| 28 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 29 | Brisbane International Airport (YBBN) | Monduran Airport (YMUA) | 39 | 31m | 304 km | 204.2 t |
| 30 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 38 | 26m | 215 km | 140.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AEZ7813 | AEZ | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Olbia / Costa Smeralda Airport (LIEO) | 2026-04-11 11:50 UTC | 2026-04-11 12:10 UTC | 19m |
| OCO222Z | OCO | Ostend-Bruges International Airport (EBOS) | Antwerp International Airport (Deurne) (EBAW) | 2026-04-11 11:37 UTC | 2026-04-11 12:08 UTC | 31m |
| LBQ651 | LBQ | New Century Aircenter Airport (KIXD) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-04-11 10:08 UTC | 2026-04-11 11:59 UTC | 1h 51m |
| N202RL |  | East Texas Regional Airport (KGGG) | East Side Airport (3TS0) | 2026-04-11 11:47 UTC | 2026-04-11 11:59 UTC | 11m |
| TCTDF | TCT | Milas Bodrum International Airport (LTFE) | Milas Bodrum International Airport (LTFE) | 2026-04-11 11:38 UTC | 2026-04-11 11:53 UTC | 15m |
| DKKSZ | DKK | Schanis Airport (LSZX) | Bad Ragaz Airport (LSZE) | 2026-04-11 10:34 UTC | 2026-04-11 11:50 UTC | 1h 15m |
| N628GB |  | Hampton Roads Executive Airport (KPVG) | VA00 (VA00) | 2026-04-11 11:14 UTC | 2026-04-11 11:45 UTC | 30m |
| DLH2KH | Lufthansa | Munich International Airport (EDDM) | Stuttgart Airport (EDDS) | 2026-04-11 10:56 UTC | 2026-04-11 11:27 UTC | 30m |
| CNF212 | CNF | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 2026-04-11 11:14 UTC | 2026-04-11 11:25 UTC | 11m |
| IBEPP | Iberia | Torino / Caselle International Airport (LIMF) | Muenster Aero Airport (LSPU) | 2026-04-11 10:57 UTC | 2026-04-11 11:25 UTC | 27m |
| CPA038 | Cathay Pacific | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-04-11 00:30 UTC | 2026-04-11 11:19 UTC | 10h 49m |
| SNJ37 | SNJ | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 2026-04-11 09:53 UTC | 2026-04-11 11:18 UTC | 1h 24m |
| WIF1328 | WIF | Bodø Airport (ENBO) | Bardufoss Airport (ENDU) | 2026-04-11 10:47 UTC | 2026-04-11 11:16 UTC | 29m |
| AKJ1509 | AKJ | Bengaluru International Airport (VOBL) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-11 09:03 UTC | 2026-04-11 11:14 UTC | 2h 10m |
| PHTWM | PHT | Twenthe Airport (EHTW) | Twenthe Airport (EHTW) | 2026-04-11 10:28 UTC | 2026-04-11 11:13 UTC | 44m |
| ZSORP | ZSO | Lanseria Airport (FALA) | Rooiberg Airport (FARO) | 2026-04-11 10:43 UTC | 2026-04-11 11:09 UTC | 25m |
| AXM5754 | AXM | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 2026-04-11 09:01 UTC | 2026-04-11 11:05 UTC | 2h 4m |
| BFD65H | BFD | Paderborn Lippstadt Airport (EDLP) | Trento / Mattarello Airport (LIDT) | 2026-04-11 10:04 UTC | 2026-04-11 11:02 UTC | 57m |
| VIV5068 | VIV | General Abelardo L. Rodriguez International Airport (MMTJ) | Atizapan De Zaragoza Airport (MMJC) | 2026-04-11 08:05 UTC | 2026-04-11 11:01 UTC | 2h 55m |
| AVA8546 | Avianca | Montelibano Airport (SKML) | Ernesto Cortissoz International Airport (SKBQ) | 2026-04-11 10:30 UTC | 2026-04-11 11:00 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
