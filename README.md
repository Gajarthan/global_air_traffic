# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_08:20:43_UTC-green)

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

**Latest saved flight:** 2026-04-06 08:20:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-06 08:20:43 UTC

- **19,521** saved flights
- **9,831** unique routes
- **115** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **19,521** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **246,345.2 tonnes** estimated CO2 emissions
- **14,280,883 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 855 |
| 2 | Ryanair | 798 |
| 3 | IndiGo | 548 |
| 4 | American Airlines | 379 |
| 5 | EJA | 365 |
| 6 | Southwest Airlines | 282 |
| 7 | ENY | 267 |
| 8 | Lufthansa | 257 |
| 9 | Vueling | 212 |
| 10 | LATAM Airlines | 208 |
| 11 | AXM | 193 |
| 12 | Delta Air Lines | 177 |
| 13 | LXJ | 171 |
| 14 | All Nippon Airways | 167 |
| 15 | QLK | 162 |
| 16 | AZU | 149 |
| 17 | VIV | 149 |
| 18 | Swiss International | 144 |
| 19 | United Airlines | 133 |
| 20 | Alaska Airlines | 132 |
| 21 | Avianca | 130 |
| 22 | easyJet | 128 |
| 23 | Japan Airlines | 127 |
| 24 | AEE | 123 |
| 25 | EJU | 123 |
| 26 | EDV | 118 |
| 27 | WIF | 117 |
| 28 | AXB | 114 |
| 29 | Air France | 106 |
| 30 | Cathay Pacific | 105 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 15352 |
| 2 | 🇮🇳 IN | 1678 |
| 3 | 🇪🇸 ES | 1580 |
| 4 | 🇦🇺 AU | 1385 |
| 5 | 🇧🇷 BR | 1124 |
| 6 | 🇨🇴 CO | 1056 |
| 7 | 🇯🇵 JP | 1046 |
| 8 | 🇩🇪 DE | 974 |
| 9 | 🇮🇹 IT | 923 |
| 10 | 🇨🇦 CA | 857 |
| 11 | 🇬🇧 GB | 753 |
| 12 | 🇫🇷 FR | 708 |
| 13 | 🇲🇽 MX | 679 |
| 14 | 🇬🇷 GR | 551 |
| 15 | 🇨🇭 CH | 513 |
| 16 | 🇬🇹 GT | 452 |
| 17 | 🇲🇾 MY | 451 |
| 18 | 🇿🇦 ZA | 427 |
| 19 | 🇳🇿 NZ | 416 |
| 20 | 🇳🇴 NO | 393 |
| 21 | 🇹🇷 TR | 373 |
| 22 | 🇵🇭 PH | 372 |
| 23 | 🇰🇷 KR | 339 |
| 24 | 🇹🇭 TH | 294 |
| 25 | 🇵🇱 PL | 281 |
| 26 | 🇲🇦 MA | 241 |
| 27 | 🇧🇸 BS | 215 |
| 28 | 🇮🇩 ID | 209 |
| 29 | 🇲🇪 ME | 202 |
| 30 | 🇲🇴 MO | 199 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 482 |
| 2 | El Dorado International Airport |  | CO | 404 |
| 3 | Denver International Airport |  | US | 363 |
| 4 | Tokyo International Airport |  | JP | 358 |
| 5 | Indira Gandhi International Airport |  | IN | 347 |
| 6 | La Aurora Airport |  | GT | 309 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 259 |
| 8 | Harry Reid International Airport |  | US | 256 |
| 9 | Zurich Airport |  | CH | 236 |
| 10 | Frankfurt am Main International Airport |  | DE | 228 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 216 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 211 |
| 13 | Chicago O'Hare International Airport |  | US | 210 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 202 |
| 15 | Guaymaral Airport |  | CO | 201 |
| 16 | Macau International Airport |  | MO | 199 |
| 17 | Charlotte/Douglas International Airport |  | US | 190 |
| 18 | Bengaluru International Airport |  | IN | 187 |
| 19 | Madrid Barajas International Airport |  | ES | 186 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 179 |
| 21 | Tenerife Norte Airport |  | ES | 175 |
| 22 | Ninoy Aquino International Airport |  | PH | 170 |
| 23 | Congonhas Airport |  | BR | 167 |
| 24 | Salt Lake City International Airport |  | US | 157 |
| 25 | Kuala Lumpur International Airport |  | MY | 157 |
| 26 | Reno/Tahoe International Airport |  | US | 156 |
| 27 | Daniel K Inouye International Airport |  | US | 153 |
| 28 | Malpensa International Airport |  | IT | 148 |
| 29 | Vitoria/Foronda Airport |  | ES | 145 |
| 30 | Charles de Gaulle International Airport |  | FR | 144 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 144 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 144 |
| 33 | Miami International Airport |  | US | 140 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 134 |
| 35 | O. R. Tambo International Airport |  | ZA | 132 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 131 |
| 37 | George Bush Intcntl/Houston Airport |  | US | 131 |
| 38 | Pune Airport |  | IN | 131 |
| 39 | Barcelona International Airport |  | ES | 131 |
| 40 | Seattle-Tacoma International Airport |  | US | 127 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 91 | 1h 8m | 706 km | 1,107.9 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 89 | 14m | 114 km | 174.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 73 | 24m | 225 km | 283.2 t |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 73 | 27m | - | - |
| 5 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 67 | 22m | 99 km | 114.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 65 | 28m | 304 km | 340.7 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 57 | 1h 27m | 910 km | 894.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 56 | 1h 43m | 1,156 km | 1,117.2 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 55 | 31m | - | - |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 54 | 16m | 206 km | 192.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 45 | 19m | 165 km | 128.0 t |
| 14 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 44 | 1h 53m | 1,304 km | 989.9 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 41 | 1h 12m | 770 km | 544.7 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 40 | 23m | 252 km | 173.7 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 40 | 54m | 546 km | 376.6 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 40 | 30m | 369 km | 254.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 39 | 52m | 556 km | 373.8 t |
| 20 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 38 | 4m | - | - |
| 21 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 37 | 1h 43m | 1,423 km | 908.0 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 37 | 9m | - | - |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 36 | 13m | 99 km | 61.7 t |
| 24 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 35 | 58m | 723 km | 436.3 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 34 | 46m | 452 km | 265.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 28 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 32 | 20m | 250 km | 138.2 t |
| 29 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 31 | 16m | 183 km | 97.8 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 30 | 12m | 15 km | 7.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DETCN | DET | Frankfurt-Egelsbach Airport (EDFE) | Frankfurt-Egelsbach Airport (EDFE) | 2026-04-06 07:50 UTC | 2026-04-06 08:20 UTC | 29m |
| HBZVS | HBZ | Courchevel Airport (LFLJ) | Muenster Aero Airport (LSPU) | 2026-04-06 07:31 UTC | 2026-04-06 07:56 UTC | 25m |
| RYR8976 | Ryanair | Sofia Airport (LBSF) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-06 06:29 UTC | 2026-04-06 07:54 UTC | 1h 24m |
| SAS38H | Scandinavian Airlines | Stockholm-Arlanda Airport (ESSA) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-06 04:34 UTC | 2026-04-06 07:45 UTC | 3h 10m |
| WMT6UQ | WMT | Memmingen Allgau Airport (EDJA) | Trstenik Airport (LYTR) | 2026-04-06 06:21 UTC | 2026-04-06 07:39 UTC | 1h 18m |
| RYR83JA | Ryanair | Sevilla Airport (LEZL) | Bari / Palese International Airport (LIBD) | 2026-04-06 04:52 UTC | 2026-04-06 07:34 UTC | 2h 41m |
| MNE101 | MNE | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 2026-04-06 07:07 UTC | 2026-04-06 07:28 UTC | 21m |
| HLC260 | HLC | Osan Air Base (RKSO) | Osan Air Base (RKSO) | 2026-04-06 07:11 UTC | 2026-04-06 07:26 UTC | 15m |
| N770SL |  | Cape Town International Airport (FACT) | Hendrik Swellengrebel Airport (FASX) | 2026-04-06 07:09 UTC | 2026-04-06 07:25 UTC | 16m |
| WUK712 | WUK | London Gatwick Airport (EGKK) | Niksic Airport (LYNK) | 2026-04-06 05:20 UTC | 2026-04-06 07:23 UTC | 2h 2m |
| ANA1643 | All Nippon Airways | Osaka International Airport (RJOO) | Kohnan Airport (RJBK) | 2026-04-06 07:03 UTC | 2026-04-06 07:21 UTC | 18m |
| WIF8XA | WIF | Trondheim Airport Vaernes (ENVA) | Bardufoss Airport (ENDU) | 2026-04-06 05:59 UTC | 2026-04-06 07:19 UTC | 1h 20m |
| UBG535 | UBG | VGZR (VGZR) | Shillong Airport (VEBI) | 2026-04-06 07:04 UTC | 2026-04-06 07:19 UTC | 14m |
| LN43MF |  | Albuquerque International Sunport Airport (KABQ) | Grants-Milan Municipal Airport (KGNT) | 2026-04-06 07:04 UTC | 2026-04-06 07:18 UTC | 13m |
| APG227 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-04-06 06:51 UTC | 2026-04-06 07:18 UTC | 27m |
| SNJ95 | SNJ | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 2026-04-06 05:57 UTC | 2026-04-06 07:14 UTC | 1h 17m |
| AIQ3146 | AIQ | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 2026-04-06 06:53 UTC | 2026-04-06 07:14 UTC | 20m |
| IGO127 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 2026-04-06 06:33 UTC | 2026-04-06 07:13 UTC | 40m |
| ZSFCW | ZSF | Cape Town International Airport (FACT) | Hendrik Swellengrebel Airport (FASX) | 2026-04-06 06:51 UTC | 2026-04-06 07:11 UTC | 19m |
| CSI571 | CSI | Las Cruces International Airport (KLRU) | Mystic Bluffs Airport (NM56) | 2026-04-06 06:22 UTC | 2026-04-06 07:10 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
