# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_13:08:41_UTC-green)

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

**Latest saved flight:** 2026-04-12 13:08:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-12 13:08:41 UTC

- **30,405** saved flights
- **13,892** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **30,405** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **372,694.5 tonnes** estimated CO2 emissions
- **21,605,480 km** total distance flown
- **847 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1259 |
| 2 | SkyWest Airlines | 1230 |
| 3 | IndiGo | 799 |
| 4 | American Airlines | 524 |
| 5 | EJA | 523 |
| 6 | Southwest Airlines | 436 |
| 7 | ENY | 408 |
| 8 | Lufthansa | 364 |
| 9 | AXM | 332 |
| 10 | Vueling | 314 |
| 11 | LATAM Airlines | 299 |
| 12 | All Nippon Airways | 286 |
| 13 | AZU | 263 |
| 14 | QLK | 260 |
| 15 | Delta Air Lines | 247 |
| 16 | LXJ | 240 |
| 17 | Swiss International | 225 |
| 18 | Alaska Airlines | 201 |
| 19 | easyJet | 201 |
| 20 | EJU | 199 |
| 21 | Japan Airlines | 197 |
| 22 | VIV | 196 |
| 23 | AEE | 193 |
| 24 | WIF | 191 |
| 25 | United Airlines | 179 |
| 26 | EDV | 178 |
| 27 | Avianca | 167 |
| 28 | Air France | 161 |
| 29 | AIQ | 161 |
| 30 | GLO | 161 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 23844 |
| 2 | 🇮🇳 IN | 2449 |
| 3 | 🇪🇸 ES | 2258 |
| 4 | 🇦🇺 AU | 2168 |
| 5 | 🇧🇷 BR | 1747 |
| 6 | 🇯🇵 JP | 1710 |
| 7 | 🇮🇹 IT | 1575 |
| 8 | 🇩🇪 DE | 1531 |
| 9 | 🇨🇴 CO | 1526 |
| 10 | 🇨🇦 CA | 1478 |
| 11 | 🇬🇧 GB | 1230 |
| 12 | 🇫🇷 FR | 1119 |
| 13 | 🇲🇽 MX | 975 |
| 14 | 🇬🇷 GR | 872 |
| 15 | 🇨🇭 CH | 855 |
| 16 | 🇲🇾 MY | 797 |
| 17 | 🇳🇿 NZ | 665 |
| 18 | 🇳🇴 NO | 647 |
| 19 | 🇿🇦 ZA | 626 |
| 20 | 🇵🇭 PH | 573 |
| 21 | 🇹🇭 TH | 565 |
| 22 | 🇹🇷 TR | 554 |
| 23 | 🇬🇹 GT | 553 |
| 24 | 🇰🇷 KR | 531 |
| 25 | 🇵🇱 PL | 460 |
| 26 | 🇲🇦 MA | 389 |
| 27 | 🇧🇸 BS | 319 |
| 28 | 🇲🇪 ME | 306 |
| 29 | 🇳🇱 NL | 293 |
| 30 | 🇮🇩 ID | 293 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 720 |
| 2 | Tokyo International Airport |  | JP | 575 |
| 3 | El Dorado International Airport |  | CO | 544 |
| 4 | Indira Gandhi International Airport |  | IN | 514 |
| 5 | Denver International Airport |  | US | 512 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 427 |
| 7 | La Aurora Airport |  | GT | 394 |
| 8 | Harry Reid International Airport |  | US | 392 |
| 9 | Zurich Airport |  | CH | 368 |
| 10 | Guaymaral Airport |  | CO | 362 |
| 11 | Chicago O'Hare International Airport |  | US | 314 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 313 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 311 |
| 14 | Frankfurt am Main International Airport |  | DE | 307 |
| 15 | Kuala Lumpur International Airport |  | MY | 302 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 301 |
| 17 | Macau International Airport |  | MO | 288 |
| 18 | Bengaluru International Airport |  | IN | 277 |
| 19 | Charlotte/Douglas International Airport |  | US | 271 |
| 20 | Tenerife Norte Airport |  | ES | 268 |
| 21 | Madrid Barajas International Airport |  | ES | 265 |
| 22 | Ninoy Aquino International Airport |  | PH | 263 |
| 23 | Congonhas Airport |  | BR | 256 |
| 24 | Malpensa International Airport |  | IT | 243 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 234 |
| 26 | Daniel K Inouye International Airport |  | US | 232 |
| 27 | Reno/Tahoe International Airport |  | US | 230 |
| 28 | Salt Lake City International Airport |  | US | 230 |
| 29 | Charles de Gaulle International Airport |  | FR | 219 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 213 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 210 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 209 |
| 33 | Capua Airport |  | IT | 209 |
| 34 | Miami International Airport |  | US | 203 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 202 |
| 36 | O. R. Tambo International Airport |  | ZA | 200 |
| 37 | Vitoria/Foronda Airport |  | ES | 199 |
| 38 | Barcelona International Airport |  | ES | 194 |
| 39 | Seattle-Tacoma International Airport |  | US | 192 |
| 40 | Don Mueang International Airport |  | TH | 191 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 145 | 1h 8m | 706 km | 1,765.4 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 140 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 126 | 14m | 114 km | 247.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 112 | 24m | 225 km | 434.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 104 | 28m | 304 km | 545.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 91 | 1h 28m | 910 km | 1,428.0 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 80 | 19m | 165 km | 227.6 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 76 | 21m | 99 km | 130.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 75 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 70 | 55m | 546 km | 659.1 t |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 12 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 66 | 1h 12m | 770 km | 876.8 t |
| 14 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 65 | 9m | - | - |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 64 | 27m | 275 km | 303.3 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 60 | 31m | 369 km | 381.9 t |
| 17 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 57 | 45m | 452 km | 444.2 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 57 | 52m | 556 km | 546.4 t |
| 20 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 55 | 21m | 244 km | 231.6 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 51 | 20m | 250 km | 220.3 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 50 | 13m | 99 km | 85.7 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 48 | 20m | 147 km | 121.5 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 46 | 1h 42m | 1,423 km | 1,128.9 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 42 | 12m | 15 km | 11.1 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 42 | 1h 19m | 961 km | 696.2 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 41 | 14m | 154 km | 108.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N683TM |  | West Memphis Municipal Airport (KAWM) | Jonesboro Municipal Airport (KJBR) | 2026-04-12 12:46 UTC | 2026-04-12 13:08 UTC | 22m |
| N55458 |  | Groton-New London Airport (KGON) | RI20 (RI20) | 2026-04-12 12:33 UTC | 2026-04-12 13:08 UTC | 35m |
| N916PC |  | Tampa International Airport (KTPA) | Mobile International Airport (KBFM) | 2026-04-12 12:08 UTC | 2026-04-12 13:05 UTC | 57m |
| LNPFH | LNP | Rakkestad Åstorp Airport (ENRK) | Kjeller Airport (ENKJ) | 2026-04-12 12:27 UTC | 2026-04-12 13:01 UTC | 33m |
| ETD947 | Etihad Airways | OM11 (OM11) | Zhuhai Airport (ZGSD) | 2026-04-12 06:46 UTC | 2026-04-12 13:00 UTC | 6h 13m |
| N264SF |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-04-12 12:40 UTC | 2026-04-12 12:57 UTC | 17m |
| LTA903 | LTA | Indianapolis International Airport (KIND) | II29 (II29) | 2026-04-12 12:34 UTC | 2026-04-12 12:53 UTC | 18m |
|  |  | Ampfing-Waldkraiburg Airport (EDNA) | Ampfing-Waldkraiburg Airport (EDNA) | 2026-04-12 12:51 UTC | 2026-04-12 12:52 UTC | 0m |
| ANA868 | All Nippon Airways | Gimpo International Airport (RKSS) | Tokyo International Airport (RJTT) | 2026-04-12 11:09 UTC | 2026-04-12 12:50 UTC | 1h 41m |
| PHHWM | PHH | Stockholm-Bromma Airport (ESSB) | Berlin Brandenburg Airport (EDDB) | 2026-04-12 11:36 UTC | 2026-04-12 12:49 UTC | 1h 12m |
| PH1483 |  | Teuge Airport (EHTE) | Teuge Airport (EHTE) | 2026-04-12 12:06 UTC | 2026-04-12 12:42 UTC | 35m |
| RYR78YR | Ryanair | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Pantelleria Airport (LICG) | 2026-04-12 12:08 UTC | 2026-04-12 12:41 UTC | 32m |
| SAS671 | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Hannover Airport (EDDV) | 2026-04-12 11:30 UTC | 2026-04-12 12:33 UTC | 1h 3m |
| BBC395 | BBC | VGZR (VGZR) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-12 11:41 UTC | 2026-04-12 12:31 UTC | 49m |
| PSAMA | PSA | Nascimento I Airport (SDNI) | Congonhas Airport (SBSP) | 2026-04-12 12:12 UTC | 2026-04-12 12:28 UTC | 16m |
| N11DT |  | Malin Airport (SOML) | Quiruvilca Airport (SPQR) | 2026-04-12 12:11 UTC | 2026-04-12 12:22 UTC | 11m |
| RYR3615 | Ryanair | Brussels South Charleroi Airport (EBCI) | Visoko Sport Airfield (LQVI) | 2026-04-12 10:47 UTC | 2026-04-12 12:20 UTC | 1h 33m |
| OEFAF | OEF | St Gallen Altenrhein Airport (LSZR) | Hoefen Airport (LOIR) | 2026-04-12 12:05 UTC | 2026-04-12 12:19 UTC | 14m |
| RYR6743 | Ryanair | Ibn Batouta Airport (GMTT) | Angads Airport (GMFO) | 2026-04-12 11:44 UTC | 2026-04-12 12:18 UTC | 33m |
| RYR51DD | Ryanair | Catania / Fontanarossa Airport (LICC) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-12 10:18 UTC | 2026-04-12 12:18 UTC | 2h 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
