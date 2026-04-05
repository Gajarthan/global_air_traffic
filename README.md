# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_11:36:45_UTC-green)

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

**Latest saved flight:** 2026-04-05 11:36:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 11:36:45 UTC

- **17,740** saved flights
- **9,157** unique routes
- **114** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **17,740** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **224,795.1 tonnes** estimated CO2 emissions
- **13,031,598 km** total distance flown
- **869 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 769 |
| 2 | Ryanair | 715 |
| 3 | IndiGo | 511 |
| 4 | EJA | 328 |
| 5 | American Airlines | 323 |
| 6 | Lufthansa | 251 |
| 7 | Southwest Airlines | 247 |
| 8 | ENY | 234 |
| 9 | Vueling | 198 |
| 10 | LATAM Airlines | 184 |
| 11 | AXM | 182 |
| 12 | All Nippon Airways | 160 |
| 13 | QLK | 154 |
| 14 | Delta Air Lines | 151 |
| 15 | LXJ | 149 |
| 16 | Swiss International | 132 |
| 17 | AZU | 131 |
| 18 | VIV | 131 |
| 19 | Alaska Airlines | 123 |
| 20 | Japan Airlines | 122 |
| 21 | easyJet | 116 |
| 22 | United Airlines | 116 |
| 23 | Avianca | 113 |
| 24 | AEE | 112 |
| 25 | AXB | 111 |
| 26 | EJU | 111 |
| 27 | EDV | 108 |
| 28 | Cathay Pacific | 103 |
| 29 | WIF | 102 |
| 30 | BRC | 101 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 13918 |
| 2 | 🇮🇳 IN | 1557 |
| 3 | 🇪🇸 ES | 1470 |
| 4 | 🇦🇺 AU | 1306 |
| 5 | 🇧🇷 BR | 1002 |
| 6 | 🇯🇵 JP | 980 |
| 7 | 🇩🇪 DE | 925 |
| 8 | 🇨🇴 CO | 905 |
| 9 | 🇮🇹 IT | 820 |
| 10 | 🇨🇦 CA | 781 |
| 11 | 🇬🇧 GB | 693 |
| 12 | 🇫🇷 FR | 640 |
| 13 | 🇲🇽 MX | 609 |
| 14 | 🇬🇷 GR | 499 |
| 15 | 🇨🇭 CH | 468 |
| 16 | 🇲🇾 MY | 419 |
| 17 | 🇳🇿 NZ | 394 |
| 18 | 🇿🇦 ZA | 389 |
| 19 | 🇵🇭 PH | 348 |
| 20 | 🇳🇴 NO | 342 |
| 21 | 🇬🇹 GT | 337 |
| 22 | 🇹🇷 TR | 333 |
| 23 | 🇰🇷 KR | 322 |
| 24 | 🇹🇭 TH | 257 |
| 25 | 🇵🇱 PL | 252 |
| 26 | 🇲🇦 MA | 216 |
| 27 | 🇮🇩 ID | 201 |
| 28 | 🇲🇴 MO | 193 |
| 29 | 🇧🇸 BS | 192 |
| 30 | 🇲🇪 ME | 186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 420 |
| 2 | El Dorado International Airport |  | CO | 343 |
| 3 | Tokyo International Airport |  | JP | 334 |
| 4 | Denver International Airport |  | US | 327 |
| 5 | Indira Gandhi International Airport |  | IN | 325 |
| 6 | La Aurora Airport |  | GT | 237 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 234 |
| 8 | Harry Reid International Airport |  | US | 232 |
| 9 | Frankfurt am Main International Airport |  | DE | 223 |
| 10 | Zurich Airport |  | CH | 216 |
| 11 | Macau International Airport |  | MO | 193 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 190 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 189 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 182 |
| 15 | Guaymaral Airport |  | CO | 182 |
| 16 | Bengaluru International Airport |  | IN | 174 |
| 17 | Chicago O'Hare International Airport |  | US | 172 |
| 18 | Madrid Barajas International Airport |  | ES | 168 |
| 19 | Charlotte/Douglas International Airport |  | US | 165 |
| 20 | Ninoy Aquino International Airport |  | PH | 159 |
| 21 | Tenerife Norte Airport |  | ES | 158 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 157 |
| 23 | Congonhas Airport |  | BR | 154 |
| 24 | Kuala Lumpur International Airport |  | MY | 148 |
| 25 | Daniel K Inouye International Airport |  | US | 144 |
| 26 | Salt Lake City International Airport |  | US | 142 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 138 |
| 28 | Malpensa International Airport |  | IT | 137 |
| 29 | Vitoria/Foronda Airport |  | ES | 137 |
| 30 | Reno/Tahoe International Airport |  | US | 136 |
| 31 | Charles de Gaulle International Airport |  | FR | 131 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 129 |
| 33 | Miami International Airport |  | US | 124 |
| 34 | Barcelona International Airport |  | ES | 123 |
| 35 | Pune Airport |  | IN | 120 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 118 |
| 37 | O. R. Tambo International Airport |  | ZA | 118 |
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
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 63 | 29m | 304 km | 330.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 53 | 31m | - | - |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 53 | 27m | 152 km | 138.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 52 | 1h 44m | 1,156 km | 1,037.4 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 52 | 1h 27m | 910 km | 816.0 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 49 | 16m | 206 km | 174.2 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 46 | 22m | 99 km | 78.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 45 | 28m | 275 km | 213.2 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 42 | 19m | 165 km | 119.5 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 39 | 1h 11m | 770 km | 518.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 39 | 30m | 369 km | 248.2 t |
| 16 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 38 | 1h 54m | 1,304 km | 854.9 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 37 | 52m | 556 km | 354.7 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 36 | 54m | 546 km | 338.9 t |
| 19 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 34 | 1h 43m | 1,423 km | 834.4 t |
| 21 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 34 | 23m | 252 km | 147.6 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 33 | 46m | 452 km | 257.2 t |
| 23 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 32 | 58m | 723 km | 398.9 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 31 | 11m | 127 km | 67.9 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 30 | 13m | 99 km | 51.4 t |
| 26 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 30 | 9m | - | - |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 27 | 20m | 147 km | 68.3 t |
| 28 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 27 | 21m | 250 km | 116.6 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 26 | 1h 23m | 961 km | 431.0 t |
| 30 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 25 | 16m | 183 km | 78.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HKC6652 | HKC | VGZR (VGZR) | Macau International Airport (VMMC) | 2026-04-05 08:51 UTC | 2026-04-05 11:36 UTC | 2h 45m |
| YLERA | YLE | Vilnius International Airport (EYVI) | S. Darius and S. Girenas Airport (EYKS) | 2026-04-05 10:48 UTC | 2026-04-05 11:20 UTC | 32m |
| S3AGG |  | Barisal Airport (VGBR) | VGZR (VGZR) | 2026-04-05 10:22 UTC | 2026-04-05 10:49 UTC | 26m |
| CCA115 | Air China | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-04-05 07:55 UTC | 2026-04-05 10:41 UTC | 2h 45m |
| AUL504 | AUL | Pushkin Airport (ULLP) | Pushkin Airport (ULLP) | 2026-04-05 10:40 UTC | 2026-04-05 10:41 UTC | 0m |
| IGO6547 | IndiGo | Bengaluru International Airport (VOBL) | Ozar Airport (VAOZ) | 2026-04-05 09:33 UTC | 2026-04-05 10:41 UTC | 1h 7m |
| AEE242 | AEE | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-04-05 10:08 UTC | 2026-04-05 10:39 UTC | 31m |
| GIA867 | Garuda Indonesia | Suvarnabhumi Airport (VTBS) | Halim Perdanakusuma International Airport (WIHH) | 2026-04-05 07:31 UTC | 2026-04-05 10:37 UTC | 3h 5m |
| B7797 |  | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-04-05 07:43 UTC | 2026-04-05 10:32 UTC | 2h 49m |
| CPA805 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-04-04 20:34 UTC | 2026-04-05 10:29 UTC | 13h 55m |
| EWG9JL | EWG | Dusseldorf International Airport (EDDL) | Vlora Internationa Airport (LAVL) | 2026-04-05 08:33 UTC | 2026-04-05 10:29 UTC | 1h 56m |
| ANE1099 | ANE | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 2026-04-05 10:03 UTC | 2026-04-05 10:28 UTC | 25m |
| KLM1977 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Dubrovnik Airport (LDDU) | 2026-04-05 08:26 UTC | 2026-04-05 10:25 UTC | 1h 58m |
| AXM6032 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-05 10:08 UTC | 2026-04-05 10:25 UTC | 16m |
| MNE311 | MNE | Zurich Airport (LSZH) | Dubrovnik Airport (LDDU) | 2026-04-05 09:10 UTC | 2026-04-05 10:24 UTC | 1h 13m |
| SFR672 | SFR | O. R. Tambo International Airport (FAOR) | Carolina Airport (FACL) | 2026-04-05 10:04 UTC | 2026-04-05 10:23 UTC | 18m |
| JST713 | JST | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 2026-04-05 09:47 UTC | 2026-04-05 10:22 UTC | 35m |
| ITY1285 | ITY | Linate Airport (LIML) | Capua Airport (LIAU) | 2026-04-05 09:34 UTC | 2026-04-05 10:21 UTC | 47m |
| TWB844 | TWB | Taiwan Taoyuan International Airport (RCTP) | Cheongju International Airport (RKTU) | 2026-04-05 06:45 UTC | 2026-04-05 10:21 UTC | 3h 36m |
| WZZ9073 | Wizz Air | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Kopitnari Airport (UGKO) | 2026-04-05 07:01 UTC | 2026-04-05 10:21 UTC | 3h 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
