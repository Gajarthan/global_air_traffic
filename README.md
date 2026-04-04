# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_08:26:32_UTC-green)

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

**Latest saved flight:** 2026-04-04 08:26:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 08:26:32 UTC

- **15,200** saved flights
- **8,217** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **15,200** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **188,292.0 tonnes** estimated CO2 emissions
- **10,915,480 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 672 |
| 2 | Ryanair | 581 |
| 3 | IndiGo | 432 |
| 4 | EJA | 302 |
| 5 | American Airlines | 282 |
| 6 | Southwest Airlines | 226 |
| 7 | Lufthansa | 215 |
| 8 | ENY | 196 |
| 9 | LATAM Airlines | 161 |
| 10 | Vueling | 161 |
| 11 | AXM | 151 |
| 12 | QLK | 137 |
| 13 | LXJ | 134 |
| 14 | All Nippon Airways | 132 |
| 15 | Delta Air Lines | 125 |
| 16 | AZU | 115 |
| 17 | Swiss International | 114 |
| 18 | VIV | 111 |
| 19 | Alaska Airlines | 104 |
| 20 | Japan Airlines | 102 |
| 21 | United Airlines | 98 |
| 22 | WIF | 97 |
| 23 | AEE | 95 |
| 24 | Avianca | 95 |
| 25 | AXB | 95 |
| 26 | EJU | 95 |
| 27 | EDV | 93 |
| 28 | easyJet | 90 |
| 29 | Cathay Pacific | 88 |
| 30 | BRC | 87 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 12258 |
| 2 | 🇮🇳 IN | 1317 |
| 3 | 🇦🇺 AU | 1197 |
| 4 | 🇪🇸 ES | 1152 |
| 5 | 🇧🇷 BR | 873 |
| 6 | 🇯🇵 JP | 806 |
| 7 | 🇩🇪 DE | 774 |
| 8 | 🇨🇴 CO | 754 |
| 9 | 🇨🇦 CA | 696 |
| 10 | 🇮🇹 IT | 658 |
| 11 | 🇬🇧 GB | 574 |
| 12 | 🇲🇽 MX | 523 |
| 13 | 🇫🇷 FR | 518 |
| 14 | 🇬🇷 GR | 424 |
| 15 | 🇨🇭 CH | 391 |
| 16 | 🇳🇿 NZ | 379 |
| 17 | 🇲🇾 MY | 339 |
| 18 | 🇳🇴 NO | 315 |
| 19 | 🇿🇦 ZA | 312 |
| 20 | 🇵🇭 PH | 293 |
| 21 | 🇹🇷 TR | 281 |
| 22 | 🇰🇷 KR | 267 |
| 23 | 🇬🇹 GT | 267 |
| 24 | 🇵🇱 PL | 207 |
| 25 | 🇹🇭 TH | 204 |
| 26 | 🇲🇦 MA | 181 |
| 27 | 🇮🇩 ID | 169 |
| 28 | 🇧🇸 BS | 159 |
| 29 | 🇲🇴 MO | 158 |
| 30 | 🇲🇪 ME | 154 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 375 |
| 2 | El Dorado International Airport |  | CO | 284 |
| 3 | Tokyo International Airport |  | JP | 281 |
| 4 | Denver International Airport |  | US | 280 |
| 5 | Indira Gandhi International Airport |  | IN | 278 |
| 6 | Harry Reid International Airport |  | US | 213 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 200 |
| 8 | Frankfurt am Main International Airport |  | DE | 199 |
| 9 | La Aurora Airport |  | GT | 187 |
| 10 | Zurich Airport |  | CH | 180 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 177 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 166 |
| 13 | Macau International Airport |  | MO | 158 |
| 14 | Guaymaral Airport |  | CO | 157 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 153 |
| 16 | Chicago O'Hare International Airport |  | US | 147 |
| 17 | Bengaluru International Airport |  | IN | 147 |
| 18 | Charlotte/Douglas International Airport |  | US | 142 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 135 |
| 20 | Madrid Barajas International Airport |  | ES | 135 |
| 21 | Congonhas Airport |  | BR | 135 |
| 22 | Ninoy Aquino International Airport |  | PH | 134 |
| 23 | Netaji Subhash Chandra Bose International Airport |  | IN | 123 |
| 24 | Reno/Tahoe International Airport |  | US | 122 |
| 25 | Salt Lake City International Airport |  | US | 121 |
| 26 | Kuala Lumpur International Airport |  | MY | 121 |
| 27 | Daniel K Inouye International Airport |  | US | 119 |
| 28 | Tenerife Norte Airport |  | ES | 118 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 117 |
| 30 | Vitoria/Foronda Airport |  | ES | 113 |
| 31 | Malpensa International Airport |  | IT | 109 |
| 32 | Charles de Gaulle International Airport |  | FR | 108 |
| 33 | George Bush Intcntl/Houston Airport |  | US | 104 |
| 34 | Austin-Bergstrom International Airport |  | US | 103 |
| 35 | Pune Airport |  | IN | 102 |
| 36 | Barcelona International Airport |  | ES | 102 |
| 37 | Seattle-Tacoma International Airport |  | US | 98 |
| 38 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 98 |
| 39 | Miami International Airport |  | US | 96 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 95 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 70 | 14m | 114 km | 137.3 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 69 | 1h 7m | 706 km | 840.1 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 58 | 24m | 225 km | 225.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 52 | 29m | 304 km | 272.6 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 44 | 1h 46m | 1,156 km | 877.8 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 44 | 31m | - | - |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 43 | 1h 26m | 910 km | 674.8 t |
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
| 19 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 30 | 1h 10m | 770 km | 398.5 t |
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
| RESQ21 | RES | Nordholz-Spieka Airport (EDXN) | Grube Airport (EDHB) | 2026-04-04 07:55 UTC | 2026-04-04 08:26 UTC | 31m |
| IHFRT | IHF | Linate Airport (LIML) | Milano / Bresso Airport (LIMB) | 2026-04-04 07:59 UTC | 2026-04-04 08:22 UTC | 22m |
| FGSAT | FGS | Verona / Boscomantico Airport (LIPN) | Verona / Boscomantico Airport (LIPN) | 2026-04-04 07:57 UTC | 2026-04-04 08:09 UTC | 12m |
| C18 |  | Spitzerberg Airport (LOAS) | LHFP (LHFP) | 2026-04-04 08:00 UTC | 2026-04-04 08:08 UTC | 8m |
| AFR38SN | Air France | Charles de Gaulle International Airport (LFPG) | Zurich Airport (LSZH) | 2026-04-04 07:15 UTC | 2026-04-04 08:03 UTC | 47m |
| HBXPY | HBX | Buttwil Airport (LSZU) | Buttwil Airport (LSZU) | 2026-04-04 07:10 UTC | 2026-04-04 08:02 UTC | 51m |
| BFS06H | BFS | Aerodrom dels Pirineus-Alt Urgell Airport (LESU) | San Sebastian Airport (LESO) | 2026-04-04 06:40 UTC | 2026-04-04 08:01 UTC | 1h 21m |
| HBZUW | HBZ | Bex Airport (LSGB) | Sion Airport (LSGS) | 2026-04-04 07:39 UTC | 2026-04-04 08:01 UTC | 22m |
| PSQ | PSQ | Hillman Farm Airport (YHLM) | Hillman Farm Airport (YHLM) | 2026-04-04 07:42 UTC | 2026-04-04 07:56 UTC | 13m |
| ANA785 | All Nippon Airways | Osaka International Airport (RJOO) | Saga Airport (RJFS) | 2026-04-04 06:45 UTC | 2026-04-04 07:52 UTC | 1h 7m |
| AXM6037 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-04 07:35 UTC | 2026-04-04 07:49 UTC | 13m |
| RYR161N | Ryanair | Barcelona International Airport (LEBL) | Malpensa International Airport (LIMC) | 2026-04-04 06:20 UTC | 2026-04-04 07:45 UTC | 1h 25m |
| HSEFS | HSE | Bang Pra Airport (VTBT) | Bang Pra Airport (VTBT) | 2026-04-04 07:37 UTC | 2026-04-04 07:44 UTC | 6m |
| FGSAT | FGS | Verona / Boscomantico Airport (LIPN) | Verona / Boscomantico Airport (LIPN) | 2026-04-04 07:29 UTC | 2026-04-04 07:43 UTC | 13m |
| ANA397 | All Nippon Airways | Tokyo International Airport (RJTT) | Yamagata Airport (RJSC) | 2026-04-04 07:17 UTC | 2026-04-04 07:43 UTC | 26m |
| SEH400 | SEH | Eleftherios Venizelos International Airport (LGAV) | Naxos Airport (LGNX) | 2026-04-04 07:23 UTC | 2026-04-04 07:43 UTC | 20m |
| N661MS |  | Tyler Pounds Regional Airport (KTYR) | Austin-Bergstrom International Airport (KAUS) | 2026-04-04 07:10 UTC | 2026-04-04 07:43 UTC | 33m |
| SEH2ZT | SEH | Eleftherios Venizelos International Airport (LGAV) | Andravida Airport (LGAD) | 2026-04-04 07:06 UTC | 2026-04-04 07:39 UTC | 32m |
| EJU4787 | EJU | Nantes Atlantique Airport (LFRS) | Bassatine Airport (GMFM) | 2026-04-04 05:40 UTC | 2026-04-04 07:38 UTC | 1h 58m |
| RUK3DN | RUK | London Stansted Airport (EGSS) | Glasgow International Airport (EGPF) | 2026-04-04 06:39 UTC | 2026-04-04 07:37 UTC | 57m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
