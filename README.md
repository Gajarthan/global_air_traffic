# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_22:31:48_UTC-green)

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

**Latest saved flight:** 2026-04-03 22:31:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-03 22:31:48 UTC

- **14,622** saved flights
- **8,019** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **14,622** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **180,917.5 tonnes** estimated CO2 emissions
- **10,487,970 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 653 |
| 2 | Ryanair | 564 |
| 3 | IndiGo | 404 |
| 4 | EJA | 294 |
| 5 | American Airlines | 279 |
| 6 | Southwest Airlines | 213 |
| 7 | Lufthansa | 210 |
| 8 | ENY | 190 |
| 9 | Vueling | 157 |
| 10 | LATAM Airlines | 154 |
| 11 | AXM | 142 |
| 12 | LXJ | 132 |
| 13 | QLK | 125 |
| 14 | All Nippon Airways | 123 |
| 15 | Delta Air Lines | 117 |
| 16 | AZU | 114 |
| 17 | Swiss International | 111 |
| 18 | VIV | 108 |
| 19 | United Airlines | 97 |
| 20 | WIF | 97 |
| 21 | Alaska Airlines | 96 |
| 22 | EDV | 92 |
| 23 | easyJet | 90 |
| 24 | AXB | 89 |
| 25 | Japan Airlines | 89 |
| 26 | AEE | 88 |
| 27 | Avianca | 87 |
| 28 | EJU | 87 |
| 29 | BRC | 86 |
| 30 | Cathay Pacific | 85 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 11904 |
| 2 | 🇮🇳 IN | 1230 |
| 3 | 🇪🇸 ES | 1110 |
| 4 | 🇦🇺 AU | 1098 |
| 5 | 🇧🇷 BR | 856 |
| 6 | 🇩🇪 DE | 757 |
| 7 | 🇯🇵 JP | 729 |
| 8 | 🇨🇴 CO | 726 |
| 9 | 🇨🇦 CA | 675 |
| 10 | 🇮🇹 IT | 628 |
| 11 | 🇬🇧 GB | 560 |
| 12 | 🇲🇽 MX | 511 |
| 13 | 🇫🇷 FR | 503 |
| 14 | 🇬🇷 GR | 391 |
| 15 | 🇨🇭 CH | 374 |
| 16 | 🇳🇿 NZ | 351 |
| 17 | 🇲🇾 MY | 319 |
| 18 | 🇳🇴 NO | 313 |
| 19 | 🇿🇦 ZA | 299 |
| 20 | 🇹🇷 TR | 269 |
| 21 | 🇬🇹 GT | 266 |
| 22 | 🇵🇭 PH | 265 |
| 23 | 🇰🇷 KR | 237 |
| 24 | 🇵🇱 PL | 202 |
| 25 | 🇹🇭 TH | 186 |
| 26 | 🇲🇦 MA | 179 |
| 27 | 🇮🇩 ID | 166 |
| 28 | 🇲🇴 MO | 157 |
| 29 | 🇧🇸 BS | 157 |
| 30 | 🇲🇪 ME | 150 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 365 |
| 2 | El Dorado International Airport |  | CO | 270 |
| 3 | Denver International Airport |  | US | 269 |
| 4 | Indira Gandhi International Airport |  | IN | 261 |
| 5 | Tokyo International Airport |  | JP | 253 |
| 6 | Harry Reid International Airport |  | US | 200 |
| 7 | Frankfurt am Main International Airport |  | DE | 196 |
| 8 | La Aurora Airport |  | GT | 186 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 182 |
| 10 | Zurich Airport |  | CH | 175 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 163 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 161 |
| 13 | Macau International Airport |  | MO | 157 |
| 14 | Guaymaral Airport |  | CO | 157 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 149 |
| 16 | Chicago O'Hare International Airport |  | US | 144 |
| 17 | Bengaluru International Airport |  | IN | 140 |
| 18 | Charlotte/Douglas International Airport |  | US | 138 |
| 19 | Congonhas Airport |  | BR | 133 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 131 |
| 21 | Madrid Barajas International Airport |  | ES | 127 |
| 22 | Ninoy Aquino International Airport |  | PH | 121 |
| 23 | Kuala Lumpur International Airport |  | MY | 117 |
| 24 | Salt Lake City International Airport |  | US | 115 |
| 25 | Tenerife Norte Airport |  | ES | 114 |
| 26 | Reno/Tahoe International Airport |  | US | 113 |
| 27 | Vitoria/Foronda Airport |  | ES | 111 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 111 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 110 |
| 30 | Daniel K Inouye International Airport |  | US | 107 |
| 31 | Charles de Gaulle International Airport |  | FR | 104 |
| 32 | Malpensa International Airport |  | IT | 103 |
| 33 | George Bush Intcntl/Houston Airport |  | US | 102 |
| 34 | Austin-Bergstrom International Airport |  | US | 99 |
| 35 | Pune Airport |  | IN | 99 |
| 36 | Barcelona International Airport |  | ES | 97 |
| 37 | Seattle-Tacoma International Airport |  | US | 96 |
| 38 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 96 |
| 39 | Miami International Airport |  | US | 94 |
| 40 | John Paul II International Airport Kraków-Balice Airport |  | PL | 91 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 67 | 14m | 114 km | 131.4 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 61 | 1h 7m | 706 km | 742.7 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 51 | 24m | 225 km | 197.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 46 | 29m | 304 km | 241.1 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 43 | 1h 46m | 1,156 km | 857.8 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 41 | 31m | - | - |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 37 | 22m | 99 km | 63.4 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 36 | 1h 26m | 910 km | 564.9 t |
| 10 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 35 | 27m | 152 km | 91.5 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 34 | 15m | 206 km | 120.9 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 34 | 28m | 275 km | 161.1 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 34 | 20m | 165 km | 96.7 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 32 | 53m | 556 km | 306.7 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 17 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 31 | 1h 54m | 1,304 km | 697.4 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 30 | 30m | 369 km | 191.0 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 27 | 1h 43m | 1,423 km | 662.6 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 27 | 1h 10m | 770 km | 358.7 t |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 26 | 59m | 723 km | 324.1 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 26 | 9m | - | - |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 25 | 20m | 147 km | 63.3 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 24 | 23m | 252 km | 104.2 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 24 | 11m | 127 km | 52.5 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 23 | 13m | 99 km | 39.4 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 22 | 44m | 452 km | 171.5 t |
| 28 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 21 | 1h 15m | 924 km | 334.9 t |
| 29 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 21 | 16m | 183 km | 66.2 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 20 | 12m | 15 km | 5.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| KHV | KHV | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-04-03 22:19 UTC | 2026-04-03 22:31 UTC | 12m |
| BULET47 | BUL | San Clemente Island Nalf Airport (KNUC) | San Clemente Island Nalf Airport (KNUC) | 2026-04-03 22:05 UTC | 2026-04-03 22:29 UTC | 24m |
| N404SH |  | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-04-03 21:16 UTC | 2026-04-03 22:18 UTC | 1h 2m |
| N69228 |  | Denton Enterprise Airport (KDTO) | Gainesville Municipal Airport (KGLE) | 2026-04-03 21:34 UTC | 2026-04-03 22:16 UTC | 41m |
| N224LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Van Nuys Airport (KVNY) | 2026-04-03 20:24 UTC | 2026-04-03 22:12 UTC | 1h 48m |
| BB055 |  | Zoltak Landing Airport (50FL) | Resort Airport (0AL1) | 2026-04-03 21:30 UTC | 2026-04-03 22:11 UTC | 41m |
| BRCAT09 | BRC | Jenkins Airport (NM87) | 81NM (81NM) | 2026-04-03 21:34 UTC | 2026-04-03 22:07 UTC | 33m |
| SH124 |  | Northwest Florida Beaches International Airport (KECP) | South Alabama Regional At Bill Benton Field (K79J) | 2026-04-03 21:29 UTC | 2026-04-03 22:05 UTC | 35m |
| N289KC |  | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-04-03 21:40 UTC | 2026-04-03 22:03 UTC | 22m |
| N631TS |  | Marina Municipal Airport (KOAR) | Garberville Airport (KO16) | 2026-04-03 21:12 UTC | 2026-04-03 22:01 UTC | 49m |
| N959BZ |  | Sun Valley Estates Airport (UT28) | Reno/Tahoe International Airport (KRNO) | 2026-04-03 21:00 UTC | 2026-04-03 21:55 UTC | 54m |
| N172KW |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-04-03 21:10 UTC | 2026-04-03 21:54 UTC | 44m |
| N773SP |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-04-03 21:07 UTC | 2026-04-03 21:53 UTC | 46m |
| EDV5185 | EDV | Hartsfield/Jackson Atlanta International Airport (KATL) | MS34 (MS34) | 2026-04-03 20:55 UTC | 2026-04-03 21:49 UTC | 54m |
| SCU51 | SCU | Ragwing Acres Airport (2OK4) | Jirik Field (OL23) | 2026-04-03 21:44 UTC | 2026-04-03 21:46 UTC | 2m |
| CAP424 | CAP | Livermore Municipal Airport (KLVK) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-03 21:34 UTC | 2026-04-03 21:46 UTC | 11m |
| N500TD |  | Bald Mountain Airport (OG45) | OG04 (OG04) | 2026-04-03 21:15 UTC | 2026-04-03 21:43 UTC | 28m |
| N567DF |  | San Bernardino International Airport (KSBD) | San Bernardino International Airport (KSBD) | 2026-04-03 21:28 UTC | 2026-04-03 21:42 UTC | 13m |
| N5778T |  | Bloomsburg Municipal Airport (KN13) | Numidia Airport (8PA0) | 2026-04-03 21:33 UTC | 2026-04-03 21:40 UTC | 7m |
| N122JM |  | Palo Alto Airport (KPAO) | Truckee-Tahoe Airport (KTRK) | 2026-04-03 21:03 UTC | 2026-04-03 21:40 UTC | 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
