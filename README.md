# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_15:29:50_UTC-green)

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

**Latest saved flight:** 2026-04-05 15:29:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 15:29:50 UTC

- **18,144** saved flights
- **9,296** unique routes
- **114** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **18,144** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **229,986.1 tonnes** estimated CO2 emissions
- **13,332,527 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 772 |
| 2 | Ryanair | 743 |
| 3 | IndiGo | 529 |
| 4 | EJA | 329 |
| 5 | American Airlines | 327 |
| 6 | Lufthansa | 255 |
| 7 | Southwest Airlines | 251 |
| 8 | ENY | 238 |
| 9 | Vueling | 201 |
| 10 | LATAM Airlines | 193 |
| 11 | AXM | 190 |
| 12 | All Nippon Airways | 161 |
| 13 | Delta Air Lines | 155 |
| 14 | QLK | 154 |
| 15 | LXJ | 152 |
| 16 | AZU | 140 |
| 17 | Swiss International | 137 |
| 18 | VIV | 134 |
| 19 | Japan Airlines | 124 |
| 20 | Alaska Airlines | 123 |
| 21 | easyJet | 121 |
| 22 | Avianca | 119 |
| 23 | United Airlines | 117 |
| 24 | AEE | 115 |
| 25 | EJU | 113 |
| 26 | AXB | 112 |
| 27 | EDV | 110 |
| 28 | WIF | 107 |
| 29 | Cathay Pacific | 105 |
| 30 | BRC | 101 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 14070 |
| 2 | 🇮🇳 IN | 1609 |
| 3 | 🇪🇸 ES | 1507 |
| 4 | 🇦🇺 AU | 1312 |
| 5 | 🇧🇷 BR | 1051 |
| 6 | 🇯🇵 JP | 994 |
| 7 | 🇨🇴 CO | 949 |
| 8 | 🇩🇪 DE | 941 |
| 9 | 🇮🇹 IT | 858 |
| 10 | 🇨🇦 CA | 784 |
| 11 | 🇬🇧 GB | 717 |
| 12 | 🇫🇷 FR | 671 |
| 13 | 🇲🇽 MX | 615 |
| 14 | 🇬🇷 GR | 516 |
| 15 | 🇨🇭 CH | 489 |
| 16 | 🇲🇾 MY | 436 |
| 17 | 🇿🇦 ZA | 403 |
| 18 | 🇳🇿 NZ | 396 |
| 19 | 🇳🇴 NO | 360 |
| 20 | 🇬🇹 GT | 358 |
| 21 | 🇵🇭 PH | 354 |
| 22 | 🇹🇷 TR | 345 |
| 23 | 🇰🇷 KR | 325 |
| 24 | 🇹🇭 TH | 273 |
| 25 | 🇵🇱 PL | 264 |
| 26 | 🇲🇦 MA | 226 |
| 27 | 🇮🇩 ID | 205 |
| 28 | 🇲🇴 MO | 198 |
| 29 | 🇧🇸 BS | 196 |
| 30 | 🇲🇪 ME | 192 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 427 |
| 2 | El Dorado International Airport |  | CO | 363 |
| 3 | Tokyo International Airport |  | JP | 340 |
| 4 | Indira Gandhi International Airport |  | IN | 336 |
| 5 | Denver International Airport |  | US | 327 |
| 6 | La Aurora Airport |  | GT | 251 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 243 |
| 8 | Harry Reid International Airport |  | US | 232 |
| 9 | Frankfurt am Main International Airport |  | DE | 226 |
| 10 | Zurich Airport |  | CH | 222 |
| 11 | Macau International Airport |  | MO | 198 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 191 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 190 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 188 |
| 15 | Guaymaral Airport |  | CO | 185 |
| 16 | Bengaluru International Airport |  | IN | 178 |
| 17 | Chicago O'Hare International Airport |  | US | 176 |
| 18 | Madrid Barajas International Airport |  | ES | 174 |
| 19 | Charlotte/Douglas International Airport |  | US | 169 |
| 20 | Tenerife Norte Airport |  | ES | 166 |
| 21 | Ninoy Aquino International Airport |  | PH | 162 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 160 |
| 23 | Congonhas Airport |  | BR | 158 |
| 24 | Kuala Lumpur International Airport |  | MY | 155 |
| 25 | Daniel K Inouye International Airport |  | US | 146 |
| 26 | Salt Lake City International Airport |  | US | 143 |
| 27 | Malpensa International Airport |  | IT | 141 |
| 28 | Vitoria/Foronda Airport |  | ES | 141 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 138 |
| 30 | Charles de Gaulle International Airport |  | FR | 137 |
| 31 | Reno/Tahoe International Airport |  | US | 136 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 136 |
| 33 | Miami International Airport |  | US | 126 |
| 34 | Barcelona International Airport |  | ES | 126 |
| 35 | Pune Airport |  | IN | 124 |
| 36 | O. R. Tambo International Airport |  | ZA | 124 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 122 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 118 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 117 |
| 40 | Seattle-Tacoma International Airport |  | US | 115 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 85 | 1h 7m | 706 km | 1,034.9 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 81 | 14m | 114 km | 158.9 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 70 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 68 | 24m | 225 km | 263.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 64 | 28m | 304 km | 335.5 t |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 56 | 27m | 152 km | 146.3 t |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 54 | 1h 44m | 1,156 km | 1,077.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 54 | 1h 27m | 910 km | 847.4 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 54 | 31m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 50 | 16m | 206 km | 177.8 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 48 | 22m | 99 km | 82.2 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 47 | 27m | 275 km | 222.7 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 45 | 19m | 165 km | 128.0 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 40 | 1h 11m | 770 km | 531.4 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 40 | 30m | 369 km | 254.6 t |
| 16 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 39 | 1h 54m | 1,304 km | 877.4 t |
| 17 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 37 | 23m | 252 km | 160.6 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 37 | 54m | 546 km | 348.4 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 37 | 52m | 556 km | 354.7 t |
| 20 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 21 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 35 | 1h 43m | 1,423 km | 859.0 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 33 | 46m | 452 km | 257.2 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 33 | 13m | 99 km | 56.6 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 32 | 58m | 723 km | 398.9 t |
| 26 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 32 | 8m | - | - |
| 27 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 30 | 17m | 183 km | 94.6 t |
| 28 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 29 | 20m | 250 km | 125.3 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 27 | 20m | 147 km | 68.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 27 | 1h 23m | 961 km | 447.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZXP02 | ZXP | Rotterdam Airport (EHRD) | Midden-Zeeland Airport (EHMZ) | 2026-04-05 14:06 UTC | 2026-04-05 15:29 UTC | 1h 23m |
| CXK579 | CXK | Brackett Field (KPOC) | Riverside Airport (KRAL) | 2026-04-05 15:02 UTC | 2026-04-05 15:19 UTC | 17m |
| N16NW |  | Arapahoe Municipal Airport (K37V) | 71NE (71NE) | 2026-04-05 14:50 UTC | 2026-04-05 15:18 UTC | 28m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-05 14:52 UTC | 2026-04-05 15:05 UTC | 12m |
| N9547W |  | Ogden-Hinckley Airport (KOGD) | Cavok Ranch Airport (UT90) | 2026-04-05 14:46 UTC | 2026-04-05 15:05 UTC | 19m |
| CXK434 | CXK | Centennial Airport (KAPA) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-05 13:30 UTC | 2026-04-05 15:02 UTC | 1h 31m |
| N522ND |  | Rocky Mountain Metro Airport (KBJC) | Fort Morgan Municipal Airport (KFMM) | 2026-04-05 14:15 UTC | 2026-04-05 14:59 UTC | 43m |
| CPA392 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-05 07:45 UTC | 2026-04-05 14:56 UTC | 7h 11m |
| FGKDM | FGK | Lyon Corbas Airport (LFHJ) | Lyon Corbas Airport (LFHJ) | 2026-04-05 14:15 UTC | 2026-04-05 14:55 UTC | 40m |
| CXK699 | CXK | Centennial Airport (KAPA) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-05 13:27 UTC | 2026-04-05 14:53 UTC | 1h 26m |
| EJA627 | EJA | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Lincoln Airport (KLNK) | 2026-04-05 14:03 UTC | 2026-04-05 14:53 UTC | 49m |
| GGFTA | GGF | Avranches Le Val St Pere Airport (LFRW) | Jersey Airport (EGJJ) | 2026-04-05 14:23 UTC | 2026-04-05 14:51 UTC | 28m |
| TGFYL | TGF | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-04-05 14:34 UTC | 2026-04-05 14:51 UTC | 17m |
| FFL296 | FFL | Gibbons Airport (12AR) | Shady Lane Airport (KM99) | 2026-04-05 14:28 UTC | 2026-04-05 14:51 UTC | 22m |
| ERU44 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | AZ86 (AZ86) | 2026-04-05 14:41 UTC | 2026-04-05 14:48 UTC | 6m |
| N697AM |  | Hodges Airpark (GA39) | Hunter Army Air Field (KSVN) | 2026-04-05 14:36 UTC | 2026-04-05 14:46 UTC | 9m |
| QQE201 | QQE | Tokyo International Airport (RJTT) | Macau International Airport (VMMC) | 2026-04-05 07:38 UTC | 2026-04-05 14:45 UTC | 7h 7m |
| HB3370 |  | Mont-Dauphin - St-Crepin Airport (LFNC) | Mont-Dauphin - St-Crepin Airport (LFNC) | 2026-04-05 12:32 UTC | 2026-04-05 14:42 UTC | 2h 10m |
| AUA487 | Austrian Airlines | Vienna International Airport (LOWW) | Madeira Airport (LPMA) | 2026-04-05 10:14 UTC | 2026-04-05 14:40 UTC | 4h 26m |
| N314LM |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-04-05 14:15 UTC | 2026-04-05 14:40 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
