# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_18:10:13_UTC-green)

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

**Latest saved flight:** 2026-04-04 18:10:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 18:10:13 UTC

- **16,345** saved flights
- **8,686** unique routes
- **113** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **16,345** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **202,877.0 tonnes** estimated CO2 emissions
- **11,760,983 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 691 |
| 2 | Ryanair | 661 |
| 3 | IndiGo | 477 |
| 4 | EJA | 308 |
| 5 | American Airlines | 292 |
| 6 | Lufthansa | 235 |
| 7 | Southwest Airlines | 234 |
| 8 | ENY | 209 |
| 9 | Vueling | 181 |
| 10 | LATAM Airlines | 173 |
| 11 | AXM | 160 |
| 12 | All Nippon Airways | 141 |
| 13 | LXJ | 139 |
| 14 | QLK | 137 |
| 15 | Delta Air Lines | 133 |
| 16 | AZU | 123 |
| 17 | Swiss International | 123 |
| 18 | VIV | 118 |
| 19 | EJU | 108 |
| 20 | Japan Airlines | 107 |
| 21 | AEE | 105 |
| 22 | Alaska Airlines | 105 |
| 23 | Avianca | 104 |
| 24 | WIF | 102 |
| 25 | AXB | 101 |
| 26 | easyJet | 100 |
| 27 | EDV | 99 |
| 28 | United Airlines | 98 |
| 29 | BRC | 96 |
| 30 | GLO | 95 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 12862 |
| 2 | 🇮🇳 IN | 1445 |
| 3 | 🇪🇸 ES | 1348 |
| 4 | 🇦🇺 AU | 1210 |
| 5 | 🇧🇷 BR | 951 |
| 6 | 🇯🇵 JP | 860 |
| 7 | 🇩🇪 DE | 857 |
| 8 | 🇨🇴 CO | 827 |
| 9 | 🇮🇹 IT | 758 |
| 10 | 🇨🇦 CA | 723 |
| 11 | 🇬🇧 GB | 639 |
| 12 | 🇫🇷 FR | 599 |
| 13 | 🇲🇽 MX | 554 |
| 14 | 🇬🇷 GR | 452 |
| 15 | 🇨🇭 CH | 439 |
| 16 | 🇳🇿 NZ | 379 |
| 17 | 🇲🇾 MY | 368 |
| 18 | 🇿🇦 ZA | 348 |
| 19 | 🇳🇴 NO | 338 |
| 20 | 🇬🇹 GT | 309 |
| 21 | 🇵🇭 PH | 305 |
| 22 | 🇹🇷 TR | 299 |
| 23 | 🇰🇷 KR | 291 |
| 24 | 🇵🇱 PL | 235 |
| 25 | 🇹🇭 TH | 231 |
| 26 | 🇲🇦 MA | 199 |
| 27 | 🇧🇸 BS | 179 |
| 28 | 🇮🇩 ID | 177 |
| 29 | 🇲🇪 ME | 169 |
| 30 | 🇲🇴 MO | 165 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 382 |
| 2 | El Dorado International Airport |  | CO | 310 |
| 3 | Tokyo International Airport |  | JP | 299 |
| 4 | Indira Gandhi International Airport |  | IN | 298 |
| 5 | Denver International Airport |  | US | 292 |
| 6 | La Aurora Airport |  | GT | 217 |
| 7 | Harry Reid International Airport |  | US | 216 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 213 |
| 9 | Frankfurt am Main International Airport |  | DE | 212 |
| 10 | Zurich Airport |  | CH | 199 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 177 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 174 |
| 13 | Guaymaral Airport |  | CO | 173 |
| 14 | Macau International Airport |  | MO | 165 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 164 |
| 16 | Bengaluru International Airport |  | IN | 159 |
| 17 | Charlotte/Douglas International Airport |  | US | 151 |
| 18 | Chicago O'Hare International Airport |  | US | 150 |
| 19 | Madrid Barajas International Airport |  | ES | 150 |
| 20 | Congonhas Airport |  | BR | 150 |
| 21 | Tenerife Norte Airport |  | ES | 146 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 142 |
| 23 | Ninoy Aquino International Airport |  | PH | 140 |
| 24 | Netaji Subhash Chandra Bose International Airport |  | IN | 136 |
| 25 | Kuala Lumpur International Airport |  | MY | 130 |
| 26 | Malpensa International Airport |  | IT | 127 |
| 27 | Reno/Tahoe International Airport |  | US | 127 |
| 28 | Daniel K Inouye International Airport |  | US | 125 |
| 29 | Salt Lake City International Airport |  | US | 125 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 123 |
| 31 | Charles de Gaulle International Airport |  | FR | 121 |
| 32 | Vitoria/Foronda Airport |  | ES | 119 |
| 33 | Barcelona International Airport |  | ES | 117 |
| 34 | George Bush Intcntl/Houston Airport |  | US | 112 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 109 |
| 36 | Pune Airport |  | IN | 109 |
| 37 | Miami International Airport |  | US | 108 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 106 |
| 39 | Austin-Bergstrom International Airport |  | US | 103 |
| 40 | Gimpo International Airport |  | KR | 101 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 74 | 14m | 114 km | 145.1 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 73 | 1h 8m | 706 km | 888.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 66 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 59 | 24m | 225 km | 228.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 57 | 29m | 304 km | 298.8 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 49 | 1h 45m | 1,156 km | 977.5 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 49 | 31m | - | - |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 47 | 1h 26m | 910 km | 737.5 t |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 45 | 26m | 152 km | 117.6 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 43 | 22m | 99 km | 73.7 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 40 | 16m | 206 km | 142.2 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 37 | 28m | 275 km | 175.3 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 36 | 19m | 165 km | 102.4 t |
| 14 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 35 | 53m | 556 km | 335.5 t |
| 16 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 34 | 1h 11m | 770 km | 451.7 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 34 | 30m | 369 km | 216.4 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 33 | 1h 54m | 1,304 km | 742.4 t |
| 19 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 31 | 23m | 252 km | 134.6 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 21 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 30 | 1h 43m | 1,423 km | 736.2 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 29 | 9m | - | - |
| 23 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 28 | 59m | 723 km | 349.1 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 28 | 13m | 99 km | 48.0 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 28 | 11m | 127 km | 61.3 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 27 | 46m | 452 km | 210.4 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 26 | 20m | 147 km | 65.8 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 25 | 16m | 183 km | 78.8 t |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 24 | 52m | 493 km | 204.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 24 | 1h 20m | 961 km | 397.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N298MC |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-04-04 17:40 UTC | 2026-04-04 18:10 UTC | 29m |
| LXJ433 | LXJ | Charleston Afb/International Airport (KCHS) | Witham Field (KSUA) | 2026-04-04 16:52 UTC | 2026-04-04 17:57 UTC | 1h 5m |
| TCN783 | TCN | Santa Barbara Municipal Airport (KSBA) | Bermuda Dunes Airport (KUDD) | 2026-04-04 17:18 UTC | 2026-04-04 17:52 UTC | 33m |
| N11024 |  | Livermore Municipal Airport (KLVK) | Livermore Municipal Airport (KLVK) | 2026-04-04 17:07 UTC | 2026-04-04 17:50 UTC | 42m |
| N411AP |  | Candy Lake Estate Airport (98OK) | Tulsa International Airport (KTUL) | 2026-04-04 17:10 UTC | 2026-04-04 17:48 UTC | 38m |
| TGRIO | TGR | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-04-04 17:22 UTC | 2026-04-04 17:46 UTC | 23m |
| AAL1219 | American Airlines | Miami International Airport (KMIA) | Denver International Airport (KDEN) | 2026-04-04 13:23 UTC | 2026-04-04 17:45 UTC | 4h 22m |
| WAH | WAH | Kenai Municipal Airport (PAEN) | Nikolai Creek Airport (9AK3) | 2026-04-04 17:30 UTC | 2026-04-04 17:45 UTC | 15m |
| SKW809E | SkyWest Airlines | San Francisco International Airport (KSFO) | Palm Springs International Airport (KPSP) | 2026-04-04 16:42 UTC | 2026-04-04 17:45 UTC | 1h 2m |
| N65501 |  | Phoenix Goodyear Airport (KGYR) | Lakeside Airpark (AZ05) | 2026-04-04 17:17 UTC | 2026-04-04 17:44 UTC | 26m |
| N153AE |  | Double Eagle Ii Airport (KAEG) | Albuquerque International Sunport Airport (KABQ) | 2026-04-04 17:32 UTC | 2026-04-04 17:43 UTC | 11m |
| CAP920 | CAP | Statesboro-Bulloch County Airport (KTBR) | 1GA4 (1GA4) | 2026-04-04 17:29 UTC | 2026-04-04 17:41 UTC | 12m |
| N168Y |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-04-04 17:34 UTC | 2026-04-04 17:38 UTC | 3m |
| WSN3 | WSN | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Gray Butte Field (04CA) | 2026-04-04 17:02 UTC | 2026-04-04 17:38 UTC | 35m |
| N5760 |  | Norman Y Mineta San Jose International Airport (KSJC) | Beryl Junction Airport (UT82) | 2026-04-04 16:26 UTC | 2026-04-04 17:37 UTC | 1h 10m |
| DLH3P | Lufthansa | Václav Havel Airport (LKPR) | Fulda-Jossa Airport (EDGF) | 2026-04-04 16:50 UTC | 2026-04-04 17:33 UTC | 42m |
| DLH875 | Lufthansa | Bergen Airport Flesland (ENBR) | Gelnhausen Airport (EDFG) | 2026-04-04 15:55 UTC | 2026-04-04 17:33 UTC | 1h 37m |
| BRG621 | BRG | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-04-04 16:44 UTC | 2026-04-04 17:29 UTC | 45m |
| TGCCC | TGC | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-04-04 17:03 UTC | 2026-04-04 17:27 UTC | 24m |
| N3026V |  | Ryan Field (KRYN) | Benson Municipal/Paul Kerchum Field (KE95) | 2026-04-04 16:54 UTC | 2026-04-04 17:24 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
