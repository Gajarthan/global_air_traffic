# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_11:55:55_UTC-green)

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

**Latest saved flight:** 2026-04-05 11:55:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 11:55:55 UTC

- **17,794** saved flights
- **9,171** unique routes
- **114** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **17,794** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **225,773.8 tonnes** estimated CO2 emissions
- **13,088,336 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 769 |
| 2 | Ryanair | 719 |
| 3 | IndiGo | 513 |
| 4 | EJA | 328 |
| 5 | American Airlines | 323 |
| 6 | Lufthansa | 252 |
| 7 | Southwest Airlines | 247 |
| 8 | ENY | 234 |
| 9 | Vueling | 199 |
| 10 | AXM | 185 |
| 11 | LATAM Airlines | 184 |
| 12 | All Nippon Airways | 161 |
| 13 | QLK | 154 |
| 14 | Delta Air Lines | 151 |
| 15 | LXJ | 149 |
| 16 | Swiss International | 132 |
| 17 | AZU | 131 |
| 18 | VIV | 131 |
| 19 | Japan Airlines | 124 |
| 20 | Alaska Airlines | 123 |
| 21 | easyJet | 119 |
| 22 | United Airlines | 117 |
| 23 | Avianca | 115 |
| 24 | AEE | 113 |
| 25 | AXB | 111 |
| 26 | EJU | 111 |
| 27 | EDV | 108 |
| 28 | Cathay Pacific | 104 |
| 29 | WIF | 103 |
| 30 | BRC | 101 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 13923 |
| 2 | 🇮🇳 IN | 1565 |
| 3 | 🇪🇸 ES | 1476 |
| 4 | 🇦🇺 AU | 1306 |
| 5 | 🇧🇷 BR | 1002 |
| 6 | 🇯🇵 JP | 989 |
| 7 | 🇩🇪 DE | 929 |
| 8 | 🇨🇴 CO | 915 |
| 9 | 🇮🇹 IT | 822 |
| 10 | 🇨🇦 CA | 781 |
| 11 | 🇬🇧 GB | 699 |
| 12 | 🇫🇷 FR | 643 |
| 13 | 🇲🇽 MX | 609 |
| 14 | 🇬🇷 GR | 502 |
| 15 | 🇨🇭 CH | 471 |
| 16 | 🇲🇾 MY | 425 |
| 17 | 🇳🇿 NZ | 394 |
| 18 | 🇿🇦 ZA | 393 |
| 19 | 🇵🇭 PH | 350 |
| 20 | 🇳🇴 NO | 344 |
| 21 | 🇬🇹 GT | 337 |
| 22 | 🇹🇷 TR | 336 |
| 23 | 🇰🇷 KR | 325 |
| 24 | 🇹🇭 TH | 263 |
| 25 | 🇵🇱 PL | 257 |
| 26 | 🇲🇦 MA | 216 |
| 27 | 🇮🇩 ID | 201 |
| 28 | 🇲🇴 MO | 194 |
| 29 | 🇧🇸 BS | 192 |
| 30 | 🇲🇪 ME | 187 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 420 |
| 2 | El Dorado International Airport |  | CO | 348 |
| 3 | Tokyo International Airport |  | JP | 337 |
| 4 | Denver International Airport |  | US | 327 |
| 5 | Indira Gandhi International Airport |  | IN | 326 |
| 6 | La Aurora Airport |  | GT | 237 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 235 |
| 8 | Harry Reid International Airport |  | US | 232 |
| 9 | Frankfurt am Main International Airport |  | DE | 223 |
| 10 | Zurich Airport |  | CH | 216 |
| 11 | Macau International Airport |  | MO | 194 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 190 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 189 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 182 |
| 15 | Guaymaral Airport |  | CO | 182 |
| 16 | Bengaluru International Airport |  | IN | 174 |
| 17 | Chicago O'Hare International Airport |  | US | 173 |
| 18 | Madrid Barajas International Airport |  | ES | 169 |
| 19 | Charlotte/Douglas International Airport |  | US | 165 |
| 20 | Ninoy Aquino International Airport |  | PH | 160 |
| 21 | Tenerife Norte Airport |  | ES | 158 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 157 |
| 23 | Congonhas Airport |  | BR | 154 |
| 24 | Kuala Lumpur International Airport |  | MY | 150 |
| 25 | Daniel K Inouye International Airport |  | US | 144 |
| 26 | Salt Lake City International Airport |  | US | 142 |
| 27 | Malpensa International Airport |  | IT | 138 |
| 28 | Vitoria/Foronda Airport |  | ES | 138 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 138 |
| 30 | Reno/Tahoe International Airport |  | US | 136 |
| 31 | Charles de Gaulle International Airport |  | FR | 131 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 129 |
| 33 | Miami International Airport |  | US | 124 |
| 34 | Barcelona International Airport |  | ES | 123 |
| 35 | Pune Airport |  | IN | 120 |
| 36 | O. R. Tambo International Airport |  | ZA | 119 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 118 |
| 38 | George Bush Intcntl/Houston Airport |  | US | 117 |
| 39 | Seattle-Tacoma International Airport |  | US | 115 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 112 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 84 | 1h 8m | 706 km | 1,022.7 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 79 | 14m | 114 km | 154.9 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 69 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 68 | 24m | 225 km | 263.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 64 | 28m | 304 km | 335.5 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 54 | 31m | - | - |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 53 | 1h 27m | 910 km | 831.7 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 53 | 27m | 152 km | 138.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 52 | 1h 44m | 1,156 km | 1,037.4 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 49 | 16m | 206 km | 174.2 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 46 | 22m | 99 km | 78.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 45 | 28m | 275 km | 213.2 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 42 | 19m | 165 km | 119.5 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 40 | 1h 11m | 770 km | 531.4 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 40 | 30m | 369 km | 254.6 t |
| 16 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 38 | 1h 54m | 1,304 km | 854.9 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 37 | 54m | 546 km | 348.4 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 37 | 52m | 556 km | 354.7 t |
| 19 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 35 | 23m | 252 km | 152.0 t |
| 21 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 34 | 1h 43m | 1,423 km | 834.4 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 33 | 46m | 452 km | 257.2 t |
| 23 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 32 | 58m | 723 km | 398.9 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 32 | 13m | 99 km | 54.9 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 31 | 11m | 127 km | 67.9 t |
| 26 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 30 | 9m | - | - |
| 27 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 28 | 20m | 250 km | 120.9 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 27 | 20m | 147 km | 68.3 t |
| 29 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 27 | 17m | 183 km | 85.1 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 26 | 1h 23m | 961 km | 431.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N258EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-04-05 11:01 UTC | 2026-04-05 11:55 UTC | 54m |
| SD1 |  | Wiener Neustadt West Airport (LOXN) | Wiener Neustadt West Airport (LOXN) | 2026-04-05 11:28 UTC | 2026-04-05 11:47 UTC | 18m |
| CPA801 | Cathay Pacific | Chicago O'Hare International Airport (KORD) | Macau International Airport (VMMC) | 2026-04-04 21:36 UTC | 2026-04-05 11:44 UTC | 14h 8m |
| HKC6652 | HKC | VGZR (VGZR) | Macau International Airport (VMMC) | 2026-04-05 08:51 UTC | 2026-04-05 11:36 UTC | 2h 45m |
| AGV08 | AGV | Reichenbach Air Base (LSGR) | Muenster Aero Airport (LSPU) | 2026-04-05 11:24 UTC | 2026-04-05 11:28 UTC | 3m |
| BOV701 | BOV | Ministro Pistarini International Airport (SAEZ) | Laja Airport (SLLJ) | 2026-04-05 06:44 UTC | 2026-04-05 11:21 UTC | 4h 37m |
| YLERA | YLE | Vilnius International Airport (EYVI) | S. Darius and S. Girenas Airport (EYKS) | 2026-04-05 10:48 UTC | 2026-04-05 11:20 UTC | 32m |
| RYR177D | Ryanair | Brussels South Charleroi Airport (EBCI) | Vitoria/Foronda Airport (LEVT) | 2026-04-05 09:57 UTC | 2026-04-05 11:17 UTC | 1h 20m |
| WZZ9XL | Wizz Air | Warsaw Chopin Airport (EPWA) | Paris-Orly Airport (LFPO) | 2026-04-05 09:00 UTC | 2026-04-05 11:12 UTC | 2h 11m |
| VLG883P | Vueling | Paris-Orly Airport (LFPO) | Santa Cilia De Jaca Airport (LECI) | 2026-04-05 10:12 UTC | 2026-04-05 11:11 UTC | 59m |
| JAL613M | Japan Airlines | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 2026-04-05 09:42 UTC | 2026-04-05 11:10 UTC | 1h 27m |
| JAL377 | Japan Airlines | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-04-05 09:58 UTC | 2026-04-05 11:08 UTC | 1h 9m |
| EZY46AB | easyJet | Palma De Mallorca Airport (LEPA) | Liverpool John Lennon Airport (EGGP) | 2026-04-05 08:41 UTC | 2026-04-05 11:04 UTC | 2h 22m |
| AVA9785 | Avianca | Rafael Nunez International Airport (SKCG) | El Dorado International Airport (SKBO) | 2026-04-05 09:59 UTC | 2026-04-05 11:03 UTC | 1h 4m |
| AXM6484 | AXM | Kota Kinabalu International Airport (WBKK) | Ranau Airport (WBKR) | 2026-04-05 10:48 UTC | 2026-04-05 11:02 UTC | 14m |
| UBG155 | UBG | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-04-05 10:32 UTC | 2026-04-05 11:02 UTC | 30m |
| RYR4YT | Ryanair | Vienna International Airport (LOWW) | Malpensa International Airport (LIMC) | 2026-04-05 09:51 UTC | 2026-04-05 10:55 UTC | 1h 3m |
| AIC5SA | Air India | Juhu Aerodrome (VAJJ) | Ambala Air Force Station (VIAM) | 2026-04-05 09:15 UTC | 2026-04-05 10:55 UTC | 1h 39m |
| WZZ2728 | Wizz Air | Lesnovo Airport (LBLS) | Boboc Air Base (LR82) | 2026-04-05 10:22 UTC | 2026-04-05 10:54 UTC | 32m |
| RYR1WE | Ryanair | Alicante International Airport (LEAL) | Liverpool John Lennon Airport (EGGP) | 2026-04-05 08:27 UTC | 2026-04-05 10:52 UTC | 2h 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
