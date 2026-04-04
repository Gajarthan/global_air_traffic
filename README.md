# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_19:28:40_UTC-green)

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

**Latest saved flight:** 2026-04-04 19:28:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 19:28:40 UTC

- **16,598** saved flights
- **8,781** unique routes
- **113** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **16,598** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **206,442.9 tonnes** estimated CO2 emissions
- **11,967,706 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 716 |
| 2 | Ryanair | 673 |
| 3 | IndiGo | 479 |
| 4 | EJA | 316 |
| 5 | American Airlines | 296 |
| 6 | Lufthansa | 237 |
| 7 | Southwest Airlines | 235 |
| 8 | ENY | 215 |
| 9 | Vueling | 185 |
| 10 | LATAM Airlines | 178 |
| 11 | AXM | 161 |
| 12 | LXJ | 143 |
| 13 | All Nippon Airways | 141 |
| 14 | Delta Air Lines | 137 |
| 15 | QLK | 137 |
| 16 | AZU | 127 |
| 17 | Swiss International | 123 |
| 18 | VIV | 123 |
| 19 | EJU | 109 |
| 20 | Alaska Airlines | 107 |
| 21 | Japan Airlines | 107 |
| 22 | Avianca | 106 |
| 23 | AEE | 105 |
| 24 | AXB | 104 |
| 25 | United Airlines | 104 |
| 26 | easyJet | 102 |
| 27 | WIF | 102 |
| 28 | EDV | 101 |
| 29 | BRC | 97 |
| 30 | GLO | 96 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 13145 |
| 2 | 🇮🇳 IN | 1458 |
| 3 | 🇪🇸 ES | 1372 |
| 4 | 🇦🇺 AU | 1210 |
| 5 | 🇧🇷 BR | 970 |
| 6 | 🇩🇪 DE | 869 |
| 7 | 🇯🇵 JP | 860 |
| 8 | 🇨🇴 CO | 843 |
| 9 | 🇮🇹 IT | 772 |
| 10 | 🇨🇦 CA | 730 |
| 11 | 🇬🇧 GB | 646 |
| 12 | 🇫🇷 FR | 605 |
| 13 | 🇲🇽 MX | 567 |
| 14 | 🇬🇷 GR | 457 |
| 15 | 🇨🇭 CH | 443 |
| 16 | 🇳🇿 NZ | 379 |
| 17 | 🇲🇾 MY | 369 |
| 18 | 🇿🇦 ZA | 350 |
| 19 | 🇳🇴 NO | 338 |
| 20 | 🇬🇹 GT | 318 |
| 21 | 🇵🇭 PH | 305 |
| 22 | 🇹🇷 TR | 303 |
| 23 | 🇰🇷 KR | 291 |
| 24 | 🇵🇱 PL | 236 |
| 25 | 🇹🇭 TH | 232 |
| 26 | 🇲🇦 MA | 202 |
| 27 | 🇧🇸 BS | 183 |
| 28 | 🇮🇩 ID | 177 |
| 29 | 🇲🇪 ME | 170 |
| 30 | 🇲🇴 MO | 165 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 390 |
| 2 | El Dorado International Airport |  | CO | 315 |
| 3 | Indira Gandhi International Airport |  | IN | 302 |
| 4 | Denver International Airport |  | US | 299 |
| 5 | Tokyo International Airport |  | JP | 299 |
| 6 | La Aurora Airport |  | GT | 223 |
| 7 | Harry Reid International Airport |  | US | 218 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 215 |
| 9 | Frankfurt am Main International Airport |  | DE | 212 |
| 10 | Zurich Airport |  | CH | 202 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 178 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 177 |
| 13 | Guaymaral Airport |  | CO | 175 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 168 |
| 15 | Macau International Airport |  | MO | 165 |
| 16 | Bengaluru International Airport |  | IN | 160 |
| 17 | Chicago O'Hare International Airport |  | US | 159 |
| 18 | Madrid Barajas International Airport |  | ES | 153 |
| 19 | Charlotte/Douglas International Airport |  | US | 152 |
| 20 | Congonhas Airport |  | BR | 152 |
| 21 | Tenerife Norte Airport |  | ES | 149 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 146 |
| 23 | Ninoy Aquino International Airport |  | PH | 140 |
| 24 | Netaji Subhash Chandra Bose International Airport |  | IN | 136 |
| 25 | Salt Lake City International Airport |  | US | 133 |
| 26 | Reno/Tahoe International Airport |  | US | 131 |
| 27 | Kuala Lumpur International Airport |  | MY | 131 |
| 28 | Malpensa International Airport |  | IT | 130 |
| 29 | Daniel K Inouye International Airport |  | US | 128 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 126 |
| 31 | Vitoria/Foronda Airport |  | ES | 123 |
| 32 | Charles de Gaulle International Airport |  | FR | 122 |
| 33 | Barcelona International Airport |  | ES | 118 |
| 34 | George Bush Intcntl/Houston Airport |  | US | 115 |
| 35 | Pune Airport |  | IN | 113 |
| 36 | Miami International Airport |  | US | 111 |
| 37 | General Edward Lawrence Logan International Airport |  | US | 109 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 109 |
| 39 | Austin-Bergstrom International Airport |  | US | 103 |
| 40 | Seattle-Tacoma International Airport |  | US | 102 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 76 | 14m | 114 km | 149.1 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 73 | 1h 8m | 706 km | 888.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 67 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 59 | 24m | 225 km | 228.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 57 | 29m | 304 km | 298.8 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 50 | 1h 45m | 1,156 km | 997.5 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 49 | 31m | - | - |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 47 | 1h 26m | 910 km | 737.5 t |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 45 | 26m | 152 km | 117.6 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 44 | 22m | 99 km | 75.4 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 42 | 16m | 206 km | 149.3 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 38 | 28m | 275 km | 180.1 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 36 | 19m | 165 km | 102.4 t |
| 14 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 36 | 52m | 556 km | 345.1 t |
| 16 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 34 | 1h 11m | 770 km | 451.7 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 34 | 30m | 369 km | 216.4 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 34 | 1h 54m | 1,304 km | 764.9 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 32 | 1h 43m | 1,423 km | 785.3 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 31 | 23m | 252 km | 134.6 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 30 | 9m | - | - |
| 23 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 29 | 59m | 723 km | 361.5 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 29 | 13m | 99 km | 49.7 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 28 | 11m | 127 km | 61.3 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 27 | 20m | 147 km | 68.3 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 27 | 46m | 452 km | 210.4 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 25 | 16m | 183 km | 78.8 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 25 | 1h 24m | 961 km | 414.4 t |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 24 | 52m | 493 km | 204.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N545GC |  | Lompoc Airport (KLPC) | Lompoc Airport (KLPC) | 2026-04-04 18:49 UTC | 2026-04-04 19:28 UTC | 39m |
| AAE127 | AAE | Henri Coanda International Airport (LROP) | Zhuhai Airport (ZGSD) | 2026-04-04 10:10 UTC | 2026-04-04 19:27 UTC | 9h 17m |
| PERRIS5 | PER | Perris Valley Airport (KL65) | Perris Valley Airport (KL65) | 2026-04-04 19:08 UTC | 2026-04-04 19:26 UTC | 17m |
| N407SL |  | Tanner Field (CO27) | Tanner Field (CO27) | 2026-04-04 19:15 UTC | 2026-04-04 19:25 UTC | 10m |
| LXJ423 | LXJ | Mc Clellan-Palomar Airport (KCRQ) | Henderson Executive Airport (KHND) | 2026-04-04 18:38 UTC | 2026-04-04 19:20 UTC | 42m |
| N48ZA |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-04-04 18:09 UTC | 2026-04-04 19:12 UTC | 1h 2m |
| N204EH |  | Zephyrhills Municipal Airport (KZPH) | Zephyrhills Municipal Airport (KZPH) | 2026-04-04 17:45 UTC | 2026-04-04 19:10 UTC | 1h 25m |
| N329HP |  | Deck Airport (K9D4) | Deck Airport (K9D4) | 2026-04-04 19:05 UTC | 2026-04-04 19:09 UTC | 4m |
| CAO8420 | CAO | Los Angeles International Airport (KLAX) | Sharypovo Airport (UNKO) | 2026-04-03 21:09 UTC | 2026-04-04 19:07 UTC | 21h 57m |
| N61718 |  | La Porte Municipal Airport (KT41) | La Porte Municipal Airport (KT41) | 2026-04-04 18:54 UTC | 2026-04-04 19:05 UTC | 10m |
| SCU19 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-04-04 18:50 UTC | 2026-04-04 19:04 UTC | 13m |
| N488UV |  | Provo Municipal Airport (KPVU) | Telluride Regional Airport (KTEX) | 2026-04-04 17:26 UTC | 2026-04-04 19:01 UTC | 1h 35m |
| N855GJ |  | NV13 (NV13) | Desert Creek Airport (NV97) | 2026-04-04 18:43 UTC | 2026-04-04 19:00 UTC | 17m |
| N65474 |  | Melby Ranch Airstrip (33CO) | Ohkay Owingeh Airport (KE14) | 2026-04-04 18:40 UTC | 2026-04-04 18:57 UTC | 17m |
| AR2 |  | Miami-Opa Locka Executive Airport (KOPF) | Miami Executive Airport (KTMB) | 2026-04-04 18:39 UTC | 2026-04-04 18:57 UTC | 17m |
| N2520A |  | Hicks Airfield (KT67) | Eagle Airport (TA51) | 2026-04-04 18:31 UTC | 2026-04-04 18:56 UTC | 25m |
| N672CC |  | Savannah/Hilton Head International Airport (KSAV) | Hunter Army Air Field (KSVN) | 2026-04-04 18:02 UTC | 2026-04-04 18:54 UTC | 51m |
| VTE3080 | VTE | Chicago O'Hare International Airport (KORD) | Klein-Oneal Airport (IL16) | 2026-04-04 17:57 UTC | 2026-04-04 18:52 UTC | 54m |
| TGCYC | TGC | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-04-04 18:28 UTC | 2026-04-04 18:52 UTC | 23m |
| LXJ514 | LXJ | Teterboro Airport (KTEB) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-04 13:15 UTC | 2026-04-04 18:51 UTC | 5h 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
