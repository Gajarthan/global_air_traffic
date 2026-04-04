# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_10:00:21_UTC-green)

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

**Latest saved flight:** 2026-04-04 10:00:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 10:00:21 UTC

- **15,316** saved flights
- **8,259** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **15,316** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **190,121.7 tonnes** estimated CO2 emissions
- **11,021,550 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 672 |
| 2 | Ryanair | 589 |
| 3 | IndiGo | 441 |
| 4 | EJA | 302 |
| 5 | American Airlines | 282 |
| 6 | Southwest Airlines | 226 |
| 7 | Lufthansa | 218 |
| 8 | ENY | 196 |
| 9 | Vueling | 164 |
| 10 | LATAM Airlines | 161 |
| 11 | AXM | 155 |
| 12 | QLK | 137 |
| 13 | All Nippon Airways | 134 |
| 14 | LXJ | 134 |
| 15 | Delta Air Lines | 125 |
| 16 | AZU | 115 |
| 17 | Swiss International | 114 |
| 18 | VIV | 111 |
| 19 | Alaska Airlines | 104 |
| 20 | Japan Airlines | 102 |
| 21 | EJU | 98 |
| 22 | United Airlines | 98 |
| 23 | WIF | 98 |
| 24 | AEE | 96 |
| 25 | Avianca | 96 |
| 26 | AXB | 95 |
| 27 | EDV | 93 |
| 28 | easyJet | 93 |
| 29 | Cathay Pacific | 88 |
| 30 | BRC | 87 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 12261 |
| 2 | 🇮🇳 IN | 1342 |
| 3 | 🇦🇺 AU | 1201 |
| 4 | 🇪🇸 ES | 1178 |
| 5 | 🇧🇷 BR | 873 |
| 6 | 🇯🇵 JP | 823 |
| 7 | 🇩🇪 DE | 784 |
| 8 | 🇨🇴 CO | 755 |
| 9 | 🇨🇦 CA | 696 |
| 10 | 🇮🇹 IT | 672 |
| 11 | 🇬🇧 GB | 585 |
| 12 | 🇫🇷 FR | 536 |
| 13 | 🇲🇽 MX | 523 |
| 14 | 🇬🇷 GR | 429 |
| 15 | 🇨🇭 CH | 399 |
| 16 | 🇳🇿 NZ | 379 |
| 17 | 🇲🇾 MY | 352 |
| 18 | 🇿🇦 ZA | 322 |
| 19 | 🇳🇴 NO | 317 |
| 20 | 🇵🇭 PH | 295 |
| 21 | 🇹🇷 TR | 283 |
| 22 | 🇰🇷 KR | 277 |
| 23 | 🇬🇹 GT | 267 |
| 24 | 🇵🇱 PL | 213 |
| 25 | 🇹🇭 TH | 204 |
| 26 | 🇲🇦 MA | 183 |
| 27 | 🇮🇩 ID | 169 |
| 28 | 🇲🇴 MO | 159 |
| 29 | 🇧🇸 BS | 159 |
| 30 | 🇲🇪 ME | 155 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 375 |
| 2 | El Dorado International Airport |  | CO | 285 |
| 3 | Tokyo International Airport |  | JP | 284 |
| 4 | Denver International Airport |  | US | 280 |
| 5 | Indira Gandhi International Airport |  | IN | 280 |
| 6 | Harry Reid International Airport |  | US | 214 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 203 |
| 8 | Frankfurt am Main International Airport |  | DE | 201 |
| 9 | La Aurora Airport |  | GT | 187 |
| 10 | Zurich Airport |  | CH | 183 |
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
| 23 | Netaji Subhash Chandra Bose International Airport |  | IN | 126 |
| 24 | Kuala Lumpur International Airport |  | MY | 125 |
| 25 | Reno/Tahoe International Airport |  | US | 122 |
| 26 | Salt Lake City International Airport |  | US | 121 |
| 27 | Tenerife Norte Airport |  | ES | 120 |
| 28 | Daniel K Inouye International Airport |  | US | 119 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 117 |
| 30 | Malpensa International Airport |  | IT | 115 |
| 31 | Vitoria/Foronda Airport |  | ES | 113 |
| 32 | Charles de Gaulle International Airport |  | FR | 112 |
| 33 | George Bush Intcntl/Houston Airport |  | US | 104 |
| 34 | Austin-Bergstrom International Airport |  | US | 103 |
| 35 | Barcelona International Airport |  | ES | 103 |
| 36 | Pune Airport |  | IN | 102 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 100 |
| 38 | Seattle-Tacoma International Airport |  | US | 98 |
| 39 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 98 |
| 40 | Gimpo International Airport |  | KR | 97 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 70 | 1h 7m | 706 km | 852.3 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 70 | 14m | 114 km | 137.3 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 59 | 24m | 225 km | 228.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 54 | 29m | 304 km | 283.1 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 46 | 31m | - | - |
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
| 24 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 26 | 11m | 127 km | 56.9 t |
| 25 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 26 | 9m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 25 | 46m | 452 km | 194.8 t |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 24 | 13m | 99 km | 41.2 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 22 | 16m | 183 km | 69.4 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 21 | 30m | 213 km | 77.1 t |
| 30 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 21 | 1h 15m | 924 km | 334.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DFALL | DFA | Hildesheim Airport (EDVM) | Hildesheim Airport (EDVM) | 2026-04-04 09:37 UTC | 2026-04-04 10:00 UTC | 22m |
| IBB55LF | IBB | Tenerife Norte Airport (GCXO) | Federico Garcia Lorca Airport (LEGR) | 2026-04-04 08:01 UTC | 2026-04-04 09:58 UTC | 1h 57m |
| FDX5015 | FDX | Narita International Airport (RJAA) | Akeno Airport (RJOE) | 2026-04-04 09:17 UTC | 2026-04-04 09:52 UTC | 34m |
| SPGWM | SPG | John Paul II International Airport Kraków-Balice Airport (EPKK) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-04 09:34 UTC | 2026-04-04 09:47 UTC | 12m |
| RYR54RU | Ryanair | Paris Beauvais Tille Airport (LFOB) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-04 07:53 UTC | 2026-04-04 09:39 UTC | 1h 45m |
| WIF1WL | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-04 09:06 UTC | 2026-04-04 09:37 UTC | 30m |
| EIX21X | EIX | Linate Airport (LIML) | Trento / Mattarello Airport (LIDT) | 2026-04-04 09:07 UTC | 2026-04-04 09:29 UTC | 22m |
| AFR78HN | Air France | Charles de Gaulle International Airport (LFPG) | Nice-Cote d'Azur Airport (LFMN) | 2026-04-04 08:18 UTC | 2026-04-04 09:26 UTC | 1h 7m |
| EZY42CA | easyJet | Belfast International Airport (EGAA) | Liverpool John Lennon Airport (EGGP) | 2026-04-04 08:51 UTC | 2026-04-04 09:25 UTC | 34m |
| FGSAT | FGS | Verona / Boscomantico Airport (LIPN) | Verona / Boscomantico Airport (LIPN) | 2026-04-04 09:10 UTC | 2026-04-04 09:22 UTC | 12m |
| IGO7VH | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Birsa Munda Airport (VERC) | 2026-04-04 08:44 UTC | 2026-04-04 09:22 UTC | 38m |
| PH0A4 |  | Teuge Airport (EHTE) | Teuge Airport (EHTE) | 2026-04-04 08:59 UTC | 2026-04-04 09:19 UTC | 20m |
| RYR3BU | Ryanair | Leeds Bradford Airport (EGNM) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-04 07:24 UTC | 2026-04-04 09:19 UTC | 1h 54m |
| AEE3LK | AEE | Larnaca International Airport (LCLK) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-04 07:40 UTC | 2026-04-04 09:13 UTC | 1h 33m |
| JES3152 | JES | Ministro Pistarini International Airport (SAEZ) | Bernardo De Irigoyen Airport (SATI) | 2026-04-04 07:47 UTC | 2026-04-04 09:11 UTC | 1h 24m |
| EJU18GM | EJU | Václav Havel Airport (LKPR) | Malpensa International Airport (LIMC) | 2026-04-04 07:53 UTC | 2026-04-04 09:11 UTC | 1h 18m |
| EZS58ZV | EZS | Geneva Cointrin International Airport (LSGG) | Decimomannu Airport (LIED) | 2026-04-04 08:08 UTC | 2026-04-04 09:08 UTC | 1h 0m |
| CTN39PR | CTN | Munich International Airport (EDDM) | Zemunik Airport (LDZD) | 2026-04-04 08:24 UTC | 2026-04-04 09:05 UTC | 41m |
| RYR9GA | Ryanair | London Stansted Airport (EGSS) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-04 07:09 UTC | 2026-04-04 09:05 UTC | 1h 55m |
| VLG37FQ | Vueling | Melsbroek Air Base (EBMB) | Burgos Airport (LEBG) | 2026-04-04 07:39 UTC | 2026-04-04 09:03 UTC | 1h 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
