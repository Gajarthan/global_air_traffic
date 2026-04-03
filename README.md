# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_19:16:53_UTC-green)

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

**Latest saved flight:** 2026-04-03 19:16:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-03 19:16:53 UTC

- **14,143** saved flights
- **7,802** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **14,143** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **175,086.8 tonnes** estimated CO2 emissions
- **10,149,960 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 604 |
| 2 | Ryanair | 540 |
| 3 | IndiGo | 402 |
| 4 | EJA | 282 |
| 5 | American Airlines | 260 |
| 6 | Lufthansa | 210 |
| 7 | Southwest Airlines | 204 |
| 8 | ENY | 182 |
| 9 | Vueling | 154 |
| 10 | LATAM Airlines | 145 |
| 11 | AXM | 142 |
| 12 | LXJ | 125 |
| 13 | All Nippon Airways | 123 |
| 14 | QLK | 123 |
| 15 | AZU | 113 |
| 16 | Delta Air Lines | 112 |
| 17 | Swiss International | 109 |
| 18 | VIV | 103 |
| 19 | WIF | 97 |
| 20 | Alaska Airlines | 91 |
| 21 | AXB | 89 |
| 22 | Japan Airlines | 89 |
| 23 | easyJet | 88 |
| 24 | United Airlines | 88 |
| 25 | EJU | 87 |
| 26 | AEE | 86 |
| 27 | EDV | 86 |
| 28 | Cathay Pacific | 85 |
| 29 | GLO | 83 |
| 30 | BRC | 80 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 11296 |
| 2 | 🇮🇳 IN | 1223 |
| 3 | 🇪🇸 ES | 1095 |
| 4 | 🇦🇺 AU | 1082 |
| 5 | 🇧🇷 BR | 829 |
| 6 | 🇩🇪 DE | 754 |
| 7 | 🇯🇵 JP | 727 |
| 8 | 🇨🇴 CO | 667 |
| 9 | 🇨🇦 CA | 651 |
| 10 | 🇮🇹 IT | 618 |
| 11 | 🇬🇧 GB | 545 |
| 12 | 🇫🇷 FR | 499 |
| 13 | 🇲🇽 MX | 494 |
| 14 | 🇬🇷 GR | 385 |
| 15 | 🇨🇭 CH | 372 |
| 16 | 🇳🇿 NZ | 325 |
| 17 | 🇲🇾 MY | 319 |
| 18 | 🇳🇴 NO | 313 |
| 19 | 🇿🇦 ZA | 297 |
| 20 | 🇵🇭 PH | 265 |
| 21 | 🇹🇷 TR | 263 |
| 22 | 🇬🇹 GT | 260 |
| 23 | 🇰🇷 KR | 237 |
| 24 | 🇵🇱 PL | 197 |
| 25 | 🇹🇭 TH | 186 |
| 26 | 🇲🇦 MA | 170 |
| 27 | 🇮🇩 ID | 166 |
| 28 | 🇲🇴 MO | 157 |
| 29 | 🇧🇸 BS | 152 |
| 30 | 🇲🇪 ME | 148 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 345 |
| 2 | Indira Gandhi International Airport |  | IN | 259 |
| 3 | Tokyo International Airport |  | JP | 253 |
| 4 | Denver International Airport |  | US | 249 |
| 5 | El Dorado International Airport |  | CO | 239 |
| 6 | Frankfurt am Main International Airport |  | DE | 196 |
| 7 | Harry Reid International Airport |  | US | 191 |
| 8 | La Aurora Airport |  | GT | 181 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 178 |
| 10 | Zurich Airport |  | CH | 173 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 159 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 158 |
| 13 | Macau International Airport |  | MO | 157 |
| 14 | Guaymaral Airport |  | CO | 155 |
| 15 | Bengaluru International Airport |  | IN | 139 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 137 |
| 17 | Chicago O'Hare International Airport |  | US | 134 |
| 18 | Congonhas Airport |  | BR | 129 |
| 19 | Charlotte/Douglas International Airport |  | US | 128 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 125 |
| 21 | Madrid Barajas International Airport |  | ES | 123 |
| 22 | Ninoy Aquino International Airport |  | PH | 121 |
| 23 | Kuala Lumpur International Airport |  | MY | 117 |
| 24 | Tenerife Norte Airport |  | ES | 114 |
| 25 | Vitoria/Foronda Airport |  | ES | 110 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 110 |
| 27 | Salt Lake City International Airport |  | US | 109 |
| 28 | Reno/Tahoe International Airport |  | US | 105 |
| 29 | Charles de Gaulle International Airport |  | FR | 104 |
| 30 | Daniel K Inouye International Airport |  | US | 103 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 103 |
| 32 | Malpensa International Airport |  | IT | 102 |
| 33 | Pune Airport |  | IN | 96 |
| 34 | Barcelona International Airport |  | ES | 96 |
| 35 | George Bush Intcntl/Houston Airport |  | US | 95 |
| 36 | Austin-Bergstrom International Airport |  | US | 93 |
| 37 | Seattle-Tacoma International Airport |  | US | 91 |
| 38 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 90 |
| 39 | General Edward Lawrence Logan International Airport |  | US | 88 |
| 40 | Miami International Airport |  | US | 87 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 65 | 14m | 114 km | 127.5 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 61 | 1h 7m | 706 km | 742.7 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 51 | 24m | 225 km | 197.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 46 | 29m | 304 km | 241.1 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 42 | 1h 46m | 1,156 km | 837.9 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 41 | 31m | - | - |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 36 | 1h 26m | 910 km | 564.9 t |
| 9 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 36 | 22m | 99 km | 61.7 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 34 | 15m | 206 km | 120.9 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 34 | 20m | 165 km | 96.7 t |
| 13 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 34 | 26m | 152 km | 88.9 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 33 | 28m | 275 km | 156.4 t |
| 15 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 30 | 30m | 369 km | 191.0 t |
| 17 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 30 | 1h 55m | 1,304 km | 674.9 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 30 | 53m | 556 km | 287.6 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 27 | 1h 43m | 1,423 km | 662.6 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 27 | 1h 10m | 770 km | 358.7 t |
| 21 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 26 | 9m | - | - |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 25 | 20m | 147 km | 63.3 t |
| 23 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 25 | 59m | 723 km | 311.7 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 24 | 23m | 252 km | 104.2 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 24 | 11m | 127 km | 52.5 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 22 | 44m | 452 km | 171.5 t |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 22 | 13m | 99 km | 37.7 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 21 | 16m | 183 km | 66.2 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 19 | 30m | 213 km | 69.8 t |
| 30 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 19 | 1h 16m | 924 km | 303.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CFR78 | CFR | Hemet-Ryan Airport (KHMT) | Hemet-Ryan Airport (KHMT) | 2026-04-03 18:25 UTC | 2026-04-03 19:16 UTC | 51m |
| N484BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-04-03 18:45 UTC | 2026-04-03 19:06 UTC | 20m |
| N5691R |  | Mckinney Ntl Airport (KTKI) | Casey Field (TE06) | 2026-04-03 18:32 UTC | 2026-04-03 19:06 UTC | 33m |
| N500TD |  | OG08 (OG08) | OG08 (OG08) | 2026-04-03 18:46 UTC | 2026-04-03 18:59 UTC | 12m |
| N481LP |  | Glendale Regional Airport (KGEU) | Bagdad Airport (KE51) | 2026-04-03 17:41 UTC | 2026-04-03 18:58 UTC | 1h 16m |
| NIT263 | NIT | Macon Downtown Airport (KMAC) | Monticello Sky Ranch Airport (GA06) | 2026-04-03 18:27 UTC | 2026-04-03 18:57 UTC | 29m |
| XCLMO | XCL | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-04-03 18:49 UTC | 2026-04-03 18:56 UTC | 6m |
| CGAQD | CGA | Abbotsford Airport (CYXX) | Chilliwack Airport (CYCW) | 2026-04-03 18:45 UTC | 2026-04-03 18:55 UTC | 10m |
| N253EA |  | Glendale Regional Airport (KGEU) | Bagdad Airport (KE51) | 2026-04-03 17:40 UTC | 2026-04-03 18:55 UTC | 1h 15m |
| N502FS |  | Porterville Municipal Airport (KPTV) | Porterville Municipal Airport (KPTV) | 2026-04-03 17:51 UTC | 2026-04-03 18:53 UTC | 1h 1m |
| SIL1705 | SIL | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-04-03 18:32 UTC | 2026-04-03 18:51 UTC | 18m |
| N12339 |  | Flying Cow Air Ranch Airport (FD39) | Flying Cow Air Ranch Airport (FD39) | 2026-04-03 18:45 UTC | 2026-04-03 18:46 UTC | 0m |
| TWY81 | TWY | Van Nuys Airport (KVNY) | Sequoia Field (KD86) | 2026-04-03 18:17 UTC | 2026-04-03 18:42 UTC | 24m |
| N707MA |  | Winter Haven Regional Airport (KGIF) | Winter Haven Regional Airport (KGIF) | 2026-04-03 17:30 UTC | 2026-04-03 18:42 UTC | 1h 11m |
| N86BJ |  | Denton Enterprise Airport (KDTO) | Gainesville Municipal Airport (KGLE) | 2026-04-03 18:05 UTC | 2026-04-03 18:35 UTC | 29m |
| AR2 |  | Miami-Opa Locka Executive Airport (KOPF) | Miami Executive Airport (KTMB) | 2026-04-03 18:15 UTC | 2026-04-03 18:35 UTC | 19m |
| N500TD |  | OG08 (OG08) | OG08 (OG08) | 2026-04-03 18:23 UTC | 2026-04-03 18:34 UTC | 11m |
| VIV7040 | VIV | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 2026-04-03 16:40 UTC | 2026-04-03 18:33 UTC | 1h 52m |
| N78RJ |  | Donaldson Field (KGYH) | Donaldson Field (KGYH) | 2026-04-03 18:26 UTC | 2026-04-03 18:31 UTC | 4m |
| N60603 |  | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-04-03 17:58 UTC | 2026-04-03 18:27 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
