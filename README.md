# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_11:39:44_UTC-green)

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

**Latest saved flight:** 2026-04-25 11:39:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-25 11:39:44 UTC

- **53,276** saved flights
- **21,202** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **53,276** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **638,401.1 tonnes** estimated CO2 emissions
- **37,008,758 km** total distance flown
- **836 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2237 |
| 2 | SkyWest Airlines | 2007 |
| 3 | IndiGo | 1216 |
| 4 | EJA | 944 |
| 5 | American Airlines | 857 |
| 6 | Southwest Airlines | 754 |
| 7 | ENY | 671 |
| 8 | Lufthansa | 619 |
| 9 | Vueling | 536 |
| 10 | AXM | 519 |
| 11 | LATAM Airlines | 509 |
| 12 | All Nippon Airways | 478 |
| 13 | AZU | 450 |
| 14 | WIF | 442 |
| 15 | Delta Air Lines | 440 |
| 16 | QLK | 416 |
| 17 | Swiss International | 407 |
| 18 | LXJ | 392 |
| 19 | AEE | 357 |
| 20 | Alaska Airlines | 353 |
| 21 | easyJet | 343 |
| 22 | EJU | 338 |
| 23 | VIV | 338 |
| 24 | Japan Airlines | 313 |
| 25 | Air France | 305 |
| 26 | AXB | 285 |
| 27 | Cathay Pacific | 284 |
| 28 | AIQ | 276 |
| 29 | JetBlue | 272 |
| 30 | United Airlines | 272 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 42396 |
| 2 | 🇪🇸 ES | 3864 |
| 3 | 🇮🇳 IN | 3832 |
| 4 | 🇦🇺 AU | 3619 |
| 5 | 🇧🇷 BR | 3059 |
| 6 | 🇯🇵 JP | 2886 |
| 7 | 🇮🇹 IT | 2865 |
| 8 | 🇩🇪 DE | 2830 |
| 9 | 🇨🇦 CA | 2658 |
| 10 | 🇨🇴 CO | 2444 |
| 11 | 🇬🇧 GB | 2230 |
| 12 | 🇫🇷 FR | 2069 |
| 13 | 🇲🇽 MX | 1641 |
| 14 | 🇬🇷 GR | 1602 |
| 15 | 🇨🇭 CH | 1500 |
| 16 | 🇳🇴 NO | 1436 |
| 17 | 🇲🇾 MY | 1262 |
| 18 | 🇿🇦 ZA | 1105 |
| 19 | 🇳🇿 NZ | 1014 |
| 20 | 🇹🇭 TH | 972 |
| 21 | 🇹🇷 TR | 956 |
| 22 | 🇵🇭 PH | 913 |
| 23 | 🇰🇷 KR | 872 |
| 24 | 🇵🇱 PL | 852 |
| 25 | 🇬🇹 GT | 815 |
| 26 | 🇲🇦 MA | 658 |
| 27 | 🇲🇪 ME | 573 |
| 28 | 🇳🇱 NL | 543 |
| 29 | 🇲🇴 MO | 524 |
| 30 | 🇧🇸 BS | 462 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1214 |
| 2 | Tokyo International Airport |  | JP | 979 |
| 3 | Denver International Airport |  | US | 881 |
| 4 | El Dorado International Airport |  | CO | 830 |
| 5 | Indira Gandhi International Airport |  | IN | 814 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 793 |
| 7 | Guaymaral Airport |  | CO | 730 |
| 8 | Harry Reid International Airport |  | US | 687 |
| 9 | Zurich Airport |  | CH | 625 |
| 10 | La Aurora Airport |  | GT | 609 |
| 11 | Frankfurt am Main International Airport |  | DE | 606 |
| 12 | Chicago O'Hare International Airport |  | US | 525 |
| 13 | Macau International Airport |  | MO | 524 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 520 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 506 |
| 16 | Kuala Lumpur International Airport |  | MY | 503 |
| 17 | Madrid Barajas International Airport |  | ES | 494 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 471 |
| 19 | Bengaluru International Airport |  | IN | 457 |
| 20 | Malpensa International Airport |  | IT | 445 |
| 21 | Congonhas Airport |  | BR | 442 |
| 22 | Charlotte/Douglas International Airport |  | US | 435 |
| 23 | Tenerife Norte Airport |  | ES | 425 |
| 24 | Ninoy Aquino International Airport |  | PH | 421 |
| 25 | Charles de Gaulle International Airport |  | FR | 401 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 397 |
| 27 | Salt Lake City International Airport |  | US | 395 |
| 28 | Daniel K Inouye International Airport |  | US | 387 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 380 |
| 30 | Capua Airport |  | IT | 379 |
| 31 | Vitoria/Foronda Airport |  | ES | 365 |
| 32 | Barcelona International Airport |  | ES | 359 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 357 |
| 34 | Reno/Tahoe International Airport |  | US | 355 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 353 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 350 |
| 37 | O. R. Tambo International Airport |  | ZA | 347 |
| 38 | Don Mueang International Airport |  | TH | 330 |
| 39 | Calgary International Airport |  | CA | 320 |
| 40 | Viracopos International Airport |  | BR | 313 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 295 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 246 | 1h 7m | 706 km | 2,995.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 200 | 14m | 114 km | 392.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 175 | 24m | 225 km | 678.9 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 162 | 21m | 244 km | 682.1 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 156 | 28m | 304 km | 817.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 152 | 1h 27m | 910 km | 2,385.2 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 138 | 19m | 165 km | 392.5 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 131 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 129 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 124 | 26m | 275 km | 587.6 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 107 | 44m | 452 km | 833.9 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 98 | 1h 11m | 770 km | 1,301.9 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 98 | 20m | 99 km | 167.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 92 | 31m | 369 km | 585.6 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 89 | 27m | 215 km | 329.6 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 88 | 20m | 250 km | 380.1 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 84 | 20m | 147 km | 212.6 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 83 | 52m | 556 km | 795.6 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 81 | 27m | 152 km | 211.7 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 76 | 1h 1m | 695 km | 911.0 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 75 | 1h 41m | 1,156 km | 1,496.2 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 75 | 13m | 99 km | 128.6 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 71 | 58m | 493 km | 604.0 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 70 | 13m | - | - |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 69 | 12m | 15 km | 18.2 t |
| 28 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 69 | 24m | 55 km | 65.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 69 | 1h 53m | 1,304 km | 1,552.3 t |
| 30 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 67 | 16m | 162 km | 187.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA801 | Cathay Pacific | Chicago O'Hare International Airport (KORD) | Macau International Airport (VMMC) | 2026-04-24 21:46 UTC | 2026-04-25 11:39 UTC | 13h 53m |
| GDSJT | GDS | Bournemouth Airport (EGHH) | Bournemouth Airport (EGHH) | 2026-04-25 10:57 UTC | 2026-04-25 11:13 UTC | 15m |
| HB2281 |  | Hausen am Albis Airport (LSZN) | Ambri Airport (LSPM) | 2026-04-25 09:00 UTC | 2026-04-25 11:11 UTC | 2h 11m |
| CPA038 | Cathay Pacific | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-04-25 00:39 UTC | 2026-04-25 11:11 UTC | 10h 31m |
| DKAGX | DKA | Juist Airport (EDWJ) | Norderney Airport (EDWY) | 2026-04-25 11:01 UTC | 2026-04-25 11:05 UTC | 4m |
| FGSAT | FGS | Verona / Boscomantico Airport (LIPN) | Verona / Boscomantico Airport (LIPN) | 2026-04-25 10:46 UTC | 2026-04-25 11:00 UTC | 13m |
| AM316 |  | Melbourne Essendon Airport (YMEN) | Benalla Airport (YBLA) | 2026-04-25 10:32 UTC | 2026-04-25 10:53 UTC | 21m |
| VJT569 | VJT | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-04-25 10:22 UTC | 2026-04-25 10:52 UTC | 30m |
| INI361 | INI | Madrid Barajas International Airport (LEMD) | Leon Airport (LELN) | 2026-04-25 10:16 UTC | 2026-04-25 10:52 UTC | 35m |
| LSI143 | LSI | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-04-24 23:56 UTC | 2026-04-25 10:46 UTC | 10h 50m |
| PEV580 | PEV | St Gallen Altenrhein Airport (LSZR) | Capua Airport (LIAU) | 2026-04-25 09:41 UTC | 2026-04-25 10:46 UTC | 1h 5m |
| AIQ3310 | AIQ | Don Mueang International Airport (VTBD) | Nakhon Sawan Airport (VTPN) | 2026-04-25 10:28 UTC | 2026-04-25 10:45 UTC | 17m |
| LOT3KY | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Lesnovo Airport (LBLS) | 2026-04-25 09:21 UTC | 2026-04-25 10:45 UTC | 1h 23m |
| IGO6393 | IndiGo | Juhu Aerodrome (VAJJ) | Ambala Air Force Station (VIAM) | 2026-04-25 09:02 UTC | 2026-04-25 10:43 UTC | 1h 41m |
| DELAR | DEL | Attendorn-Finnentrop Airport (EDKU) | Attendorn-Finnentrop Airport (EDKU) | 2026-04-25 10:32 UTC | 2026-04-25 10:42 UTC | 10m |
| IGO6724 | IndiGo | Agartala Airport (VEAT) | Shillong Airport (VEBI) | 2026-04-25 10:20 UTC | 2026-04-25 10:41 UTC | 21m |
| JAL613M | Japan Airlines | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 2026-04-25 09:00 UTC | 2026-04-25 10:40 UTC | 1h 40m |
| THY2PL | Turkish Airlines | Ataturk International Airport (LTBA) | Gaziemir Airport (LTBK) | 2026-04-25 10:12 UTC | 2026-04-25 10:40 UTC | 27m |
| AIC219 | Air India | Indira Gandhi International Airport (VIDP) | Tribhuvan International Airport (VNKT) | 2026-04-25 09:24 UTC | 2026-04-25 10:39 UTC | 1h 14m |
| LNK651R | LNK | Cape Town International Airport (FACT) | Barberton Airport (FABR) | 2026-04-25 08:57 UTC | 2026-04-25 10:39 UTC | 1h 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
