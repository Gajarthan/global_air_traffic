# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_09:22:40_UTC-green)

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

**Latest saved flight:** 2026-04-04 09:22:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 09:22:40 UTC

- **15,257** saved flights
- **8,237** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **15,257** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **189,283.1 tonnes** estimated CO2 emissions
- **10,972,936 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 672 |
| 2 | Ryanair | 585 |
| 3 | IndiGo | 439 |
| 4 | EJA | 302 |
| 5 | American Airlines | 282 |
| 6 | Southwest Airlines | 226 |
| 7 | Lufthansa | 216 |
| 8 | ENY | 196 |
| 9 | Vueling | 162 |
| 10 | LATAM Airlines | 161 |
| 11 | AXM | 151 |
| 12 | QLK | 137 |
| 13 | All Nippon Airways | 134 |
| 14 | LXJ | 134 |
| 15 | Delta Air Lines | 125 |
| 16 | AZU | 115 |
| 17 | Swiss International | 114 |
| 18 | VIV | 111 |
| 19 | Alaska Airlines | 104 |
| 20 | Japan Airlines | 102 |
| 21 | United Airlines | 98 |
| 22 | EJU | 97 |
| 23 | WIF | 97 |
| 24 | AEE | 95 |
| 25 | Avianca | 95 |
| 26 | AXB | 95 |
| 27 | EDV | 93 |
| 28 | easyJet | 92 |
| 29 | Cathay Pacific | 88 |
| 30 | BRC | 87 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 12259 |
| 2 | 🇮🇳 IN | 1338 |
| 3 | 🇦🇺 AU | 1201 |
| 4 | 🇪🇸 ES | 1163 |
| 5 | 🇧🇷 BR | 873 |
| 6 | 🇯🇵 JP | 816 |
| 7 | 🇩🇪 DE | 778 |
| 8 | 🇨🇴 CO | 754 |
| 9 | 🇨🇦 CA | 696 |
| 10 | 🇮🇹 IT | 665 |
| 11 | 🇬🇧 GB | 578 |
| 12 | 🇫🇷 FR | 529 |
| 13 | 🇲🇽 MX | 523 |
| 14 | 🇬🇷 GR | 425 |
| 15 | 🇨🇭 CH | 395 |
| 16 | 🇳🇿 NZ | 379 |
| 17 | 🇲🇾 MY | 341 |
| 18 | 🇳🇴 NO | 315 |
| 19 | 🇿🇦 ZA | 312 |
| 20 | 🇵🇭 PH | 295 |
| 21 | 🇹🇷 TR | 281 |
| 22 | 🇰🇷 KR | 275 |
| 23 | 🇬🇹 GT | 267 |
| 24 | 🇵🇱 PL | 208 |
| 25 | 🇹🇭 TH | 204 |
| 26 | 🇲🇦 MA | 182 |
| 27 | 🇮🇩 ID | 169 |
| 28 | 🇲🇴 MO | 159 |
| 29 | 🇧🇸 BS | 159 |
| 30 | 🇲🇪 ME | 154 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 375 |
| 2 | El Dorado International Airport |  | CO | 284 |
| 3 | Tokyo International Airport |  | JP | 284 |
| 4 | Denver International Airport |  | US | 280 |
| 5 | Indira Gandhi International Airport |  | IN | 279 |
| 6 | Harry Reid International Airport |  | US | 213 |
| 7 | Frankfurt am Main International Airport |  | DE | 201 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 200 |
| 9 | La Aurora Airport |  | GT | 187 |
| 10 | Zurich Airport |  | CH | 181 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 177 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 166 |
| 13 | Macau International Airport |  | MO | 159 |
| 14 | Guaymaral Airport |  | CO | 157 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 153 |
| 16 | Bengaluru International Airport |  | IN | 151 |
| 17 | Chicago O'Hare International Airport |  | US | 147 |
| 18 | Charlotte/Douglas International Airport |  | US | 142 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 135 |
| 20 | Ninoy Aquino International Airport |  | PH | 135 |
| 21 | Madrid Barajas International Airport |  | ES | 135 |
| 22 | Congonhas Airport |  | BR | 135 |
| 23 | Netaji Subhash Chandra Bose International Airport |  | IN | 125 |
| 24 | Reno/Tahoe International Airport |  | US | 122 |
| 25 | Salt Lake City International Airport |  | US | 121 |
| 26 | Kuala Lumpur International Airport |  | MY | 121 |
| 27 | Daniel K Inouye International Airport |  | US | 119 |
| 28 | Tenerife Norte Airport |  | ES | 118 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 117 |
| 30 | Malpensa International Airport |  | IT | 113 |
| 31 | Vitoria/Foronda Airport |  | ES | 113 |
| 32 | Charles de Gaulle International Airport |  | FR | 110 |
| 33 | George Bush Intcntl/Houston Airport |  | US | 104 |
| 34 | Austin-Bergstrom International Airport |  | US | 103 |
| 35 | Barcelona International Airport |  | ES | 103 |
| 36 | Pune Airport |  | IN | 102 |
| 37 | Seattle-Tacoma International Airport |  | US | 98 |
| 38 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 98 |
| 39 | Gimpo International Airport |  | KR | 97 |
| 40 | Miami International Airport |  | US | 96 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 70 | 1h 7m | 706 km | 852.3 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 70 | 14m | 114 km | 137.3 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 59 | 24m | 225 km | 228.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 54 | 29m | 304 km | 283.1 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 45 | 31m | - | - |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 44 | 1h 46m | 1,156 km | 877.8 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 44 | 1h 26m | 910 km | 690.5 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 38 | 16m | 206 km | 135.1 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 37 | 22m | 99 km | 63.4 t |
| 11 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 35 | 28m | 275 km | 165.9 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 35 | 19m | 165 km | 99.6 t |
| 14 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 35 | 27m | 152 km | 91.5 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 34 | 53m | 556 km | 325.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 32 | 30m | 369 km | 203.7 t |
| 17 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 32 | 1h 54m | 1,304 km | 719.9 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 19 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 31 | 1h 10m | 770 km | 411.8 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 27 | 1h 43m | 1,423 km | 662.6 t |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 27 | 59m | 723 km | 336.6 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 26 | 20m | 147 km | 65.8 t |
| 23 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 26 | 23m | 252 km | 112.9 t |
| 24 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 26 | 9m | - | - |
| 25 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 25 | 46m | 452 km | 194.8 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 25 | 11m | 127 km | 54.7 t |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 24 | 13m | 99 km | 41.2 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 22 | 16m | 183 km | 69.4 t |
| 29 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 21 | 1h 15m | 924 km | 334.9 t |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 21 | 52m | 493 km | 178.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FGSAT | FGS | Verona / Boscomantico Airport (LIPN) | Verona / Boscomantico Airport (LIPN) | 2026-04-04 09:10 UTC | 2026-04-04 09:22 UTC | 12m |
| PH0A4 |  | Teuge Airport (EHTE) | Teuge Airport (EHTE) | 2026-04-04 08:59 UTC | 2026-04-04 09:19 UTC | 20m |
| RYR5905 | Ryanair | Torino / Caselle International Airport (LIMF) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-04 07:13 UTC | 2026-04-04 08:57 UTC | 1h 44m |
| YGN | YGN | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-04 08:13 UTC | 2026-04-04 08:57 UTC | 44m |
| RYR985X | Ryanair | Dublin Airport (EIDW) | Lanzarote Airport (GCRR) | 2026-04-04 05:08 UTC | 2026-04-04 08:52 UTC | 3h 43m |
| FYS17ZD | FYS | Cuatro Vientos Airport (LECU) | E. Castellanos-Villacastin Airport (LEEV) | 2026-04-04 08:09 UTC | 2026-04-04 08:50 UTC | 40m |
| EJU85EA | EJU | Bordeaux-Merignac (BA 106) Airport (LFBD) | Madeira Airport (LPMA) | 2026-04-04 06:02 UTC | 2026-04-04 08:46 UTC | 2h 43m |
| ICE30R | ICE | Reykjavik Airport (BIRK) | Sanda Airport (BISA) | 2026-04-04 08:27 UTC | 2026-04-04 08:45 UTC | 18m |
| IGO7425 | IndiGo | Indira Gandhi International Airport (VIDP) | Pithorgarh Airport (VIDF) | 2026-04-04 08:15 UTC | 2026-04-04 08:42 UTC | 27m |
| AIC1ZL | Air India | Juhu Aerodrome (VAJJ) | Sarsawa Air Force Station (VISP) | 2026-04-04 07:08 UTC | 2026-04-04 08:38 UTC | 1h 30m |
| IXIAN | IXI | Sollieres Sardieres Airport (LFKD) | Mont-Dauphin - St-Crepin Airport (LFNC) | 2026-04-04 08:16 UTC | 2026-04-04 08:38 UTC | 22m |
| CSZ631 | CSZ | Shenzhen Bao'an International Airport (ZGSZ) | Incheon International Airport (RKSI) | 2026-04-04 05:42 UTC | 2026-04-04 08:32 UTC | 2h 49m |
| UBG149 | UBG | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-04-04 07:54 UTC | 2026-04-04 08:29 UTC | 35m |
| VLG76XU | Vueling | Barcelona International Airport (LEBL) | Paris-Orly Airport (LFPO) | 2026-04-04 06:57 UTC | 2026-04-04 08:29 UTC | 1h 32m |
| EJU34UF | EJU | Ibiza Airport (LEIB) | Malpensa International Airport (LIMC) | 2026-04-04 06:53 UTC | 2026-04-04 08:29 UTC | 1h 35m |
| RYR6671 | Ryanair | Madeira Airport (LPMA) | Malpensa International Airport (LIMC) | 2026-04-04 05:03 UTC | 2026-04-04 08:28 UTC | 3h 25m |
| IGO874 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Sarsawa Air Force Station (VISP) | 2026-04-04 06:35 UTC | 2026-04-04 08:27 UTC | 1h 52m |
| SFJ83 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-04-04 07:10 UTC | 2026-04-04 08:27 UTC | 1h 16m |
| VOE2732 | VOE | Lille-Lesquin Airport (LFQQ) | La Gomera Airport (GCGM) | 2026-04-04 04:23 UTC | 2026-04-04 08:26 UTC | 4h 3m |
| FD580 |  | Adelaide International Airport (YPAD) | Waikerie Airport (YWKI) | 2026-04-04 08:05 UTC | 2026-04-04 08:26 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
