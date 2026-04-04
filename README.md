# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_21:35:17_UTC-green)

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

**Latest saved flight:** 2026-04-04 21:35:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 21:35:17 UTC

- **16,912** saved flights
- **8,901** unique routes
- **113** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **16,912** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **211,170.5 tonnes** estimated CO2 emissions
- **12,241,767 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 744 |
| 2 | Ryanair | 685 |
| 3 | IndiGo | 481 |
| 4 | EJA | 322 |
| 5 | American Airlines | 311 |
| 6 | Southwest Airlines | 239 |
| 7 | Lufthansa | 238 |
| 8 | ENY | 226 |
| 9 | Vueling | 189 |
| 10 | LATAM Airlines | 182 |
| 11 | AXM | 161 |
| 12 | LXJ | 146 |
| 13 | Delta Air Lines | 144 |
| 14 | All Nippon Airways | 141 |
| 15 | QLK | 137 |
| 16 | AZU | 129 |
| 17 | VIV | 126 |
| 18 | Swiss International | 124 |
| 19 | Alaska Airlines | 113 |
| 20 | United Airlines | 112 |
| 21 | EJU | 109 |
| 22 | Avianca | 108 |
| 23 | Japan Airlines | 107 |
| 24 | easyJet | 106 |
| 25 | AEE | 105 |
| 26 | AXB | 105 |
| 27 | EDV | 104 |
| 28 | WIF | 102 |
| 29 | BRC | 101 |
| 30 | GLO | 97 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 13523 |
| 2 | 🇮🇳 IN | 1466 |
| 3 | 🇪🇸 ES | 1398 |
| 4 | 🇦🇺 AU | 1211 |
| 5 | 🇧🇷 BR | 986 |
| 6 | 🇨🇴 CO | 872 |
| 7 | 🇩🇪 DE | 872 |
| 8 | 🇯🇵 JP | 862 |
| 9 | 🇮🇹 IT | 784 |
| 10 | 🇨🇦 CA | 755 |
| 11 | 🇬🇧 GB | 659 |
| 12 | 🇫🇷 FR | 608 |
| 13 | 🇲🇽 MX | 579 |
| 14 | 🇬🇷 GR | 459 |
| 15 | 🇨🇭 CH | 444 |
| 16 | 🇳🇿 NZ | 381 |
| 17 | 🇲🇾 MY | 369 |
| 18 | 🇿🇦 ZA | 350 |
| 19 | 🇳🇴 NO | 339 |
| 20 | 🇬🇹 GT | 327 |
| 21 | 🇹🇷 TR | 308 |
| 22 | 🇵🇭 PH | 305 |
| 23 | 🇰🇷 KR | 292 |
| 24 | 🇵🇱 PL | 239 |
| 25 | 🇹🇭 TH | 232 |
| 26 | 🇲🇦 MA | 206 |
| 27 | 🇧🇸 BS | 190 |
| 28 | 🇮🇩 ID | 178 |
| 29 | 🇲🇪 ME | 173 |
| 30 | 🇲🇴 MO | 169 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 408 |
| 2 | El Dorado International Airport |  | CO | 327 |
| 3 | Denver International Airport |  | US | 315 |
| 4 | Indira Gandhi International Airport |  | IN | 303 |
| 5 | Tokyo International Airport |  | JP | 299 |
| 6 | La Aurora Airport |  | GT | 230 |
| 7 | Harry Reid International Airport |  | US | 224 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 215 |
| 9 | Frankfurt am Main International Airport |  | DE | 212 |
| 10 | Zurich Airport |  | CH | 203 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 183 |
| 12 | Guaymaral Airport |  | CO | 180 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 177 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 176 |
| 15 | Macau International Airport |  | MO | 169 |
| 16 | Chicago O'Hare International Airport |  | US | 165 |
| 17 | Bengaluru International Airport |  | IN | 162 |
| 18 | Charlotte/Douglas International Airport |  | US | 158 |
| 19 | Madrid Barajas International Airport |  | ES | 156 |
| 20 | Congonhas Airport |  | BR | 153 |
| 21 | Tenerife Norte Airport |  | ES | 150 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 149 |
| 23 | Ninoy Aquino International Airport |  | PH | 140 |
| 24 | Netaji Subhash Chandra Bose International Airport |  | IN | 136 |
| 25 | Salt Lake City International Airport |  | US | 136 |
| 26 | Malpensa International Airport |  | IT | 133 |
| 27 | Daniel K Inouye International Airport |  | US | 132 |
| 28 | Reno/Tahoe International Airport |  | US | 132 |
| 29 | Kuala Lumpur International Airport |  | MY | 131 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 128 |
| 31 | Vitoria/Foronda Airport |  | ES | 125 |
| 32 | Charles de Gaulle International Airport |  | FR | 123 |
| 33 | Miami International Airport |  | US | 119 |
| 34 | Barcelona International Airport |  | ES | 119 |
| 35 | Pune Airport |  | IN | 116 |
| 36 | George Bush Intcntl/Houston Airport |  | US | 115 |
| 37 | General Edward Lawrence Logan International Airport |  | US | 110 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 110 |
| 39 | Seattle-Tacoma International Airport |  | US | 108 |
| 40 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 106 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 77 | 14m | 114 km | 151.0 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 73 | 1h 8m | 706 km | 888.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 68 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 59 | 24m | 225 km | 228.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 57 | 29m | 304 km | 298.8 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 51 | 1h 45m | 1,156 km | 1,017.4 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 49 | 31m | - | - |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 49 | 27m | 152 km | 128.1 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 47 | 1h 26m | 910 km | 737.5 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 44 | 22m | 99 km | 75.4 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 43 | 16m | 206 km | 152.9 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 40 | 28m | 275 km | 189.5 t |
| 13 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 37 | 52m | 556 km | 354.7 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 36 | 19m | 165 km | 102.4 t |
| 15 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 16 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 35 | 1h 54m | 1,304 km | 787.4 t |
| 17 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 34 | 1h 11m | 770 km | 451.7 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 34 | 30m | 369 km | 216.4 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 32 | 1h 43m | 1,423 km | 785.3 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 31 | 23m | 252 km | 134.6 t |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 31 | 58m | 723 km | 386.5 t |
| 22 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 30 | 13m | 99 km | 51.4 t |
| 24 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 30 | 9m | - | - |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 28 | 11m | 127 km | 61.3 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 27 | 20m | 147 km | 68.3 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 27 | 46m | 452 km | 210.4 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 25 | 16m | 183 km | 78.8 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 25 | 1h 24m | 961 km | 414.4 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 24 | 12m | 15 km | 6.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N734LQ |  | Jim & Julie's Airport (96WA) | Jim & Julie's Airport (96WA) | 2026-04-04 20:56 UTC | 2026-04-04 21:35 UTC | 38m |
| N7089R |  | Pittsburgh/Butler Regional Airport (KBTP) | Pittsburgh/Butler Regional Airport (KBTP) | 2026-04-04 21:03 UTC | 2026-04-04 21:25 UTC | 21m |
| BCS696 | BCS | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2026-04-04 10:10 UTC | 2026-04-04 21:20 UTC | 11h 10m |
| N164ER |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-04-04 20:52 UTC | 2026-04-04 21:19 UTC | 26m |
| N404SH |  | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-04-04 20:24 UTC | 2026-04-04 21:18 UTC | 53m |
| N412AG |  | Eagle Soaring Airport (1CD4) | Mesa 1 Airport (81CO) | 2026-04-04 20:53 UTC | 2026-04-04 21:17 UTC | 24m |
| N60244 |  | North Las Vegas Airport (KVGT) | Creech Afb Airport (KINS) | 2026-04-04 20:54 UTC | 2026-04-04 21:16 UTC | 21m |
| N850TV |  | Mckinney Ntl Airport (KTKI) | Mc Alester Regional Airport (KMLC) | 2026-04-04 19:47 UTC | 2026-04-04 21:14 UTC | 1h 26m |
| HAF403 | HAF | Limnos Airport (LGLM) | Ikaria Airport (LGIK) | 2026-04-04 20:34 UTC | 2026-04-04 21:11 UTC | 36m |
| N6SP |  | Summit Airport (KEVY) | Summit Airport (KEVY) | 2026-04-04 21:07 UTC | 2026-04-04 21:09 UTC | 2m |
| N2896Q |  | Perot Field/Fort Worth Alliance Airport (KAFW) | Cross Wind Airport (08TX) | 2026-04-04 20:37 UTC | 2026-04-04 21:08 UTC | 31m |
| N743TW |  | Wendover Airport (KENV) | Logan-Cache Airport (KLGU) | 2026-04-04 19:41 UTC | 2026-04-04 20:57 UTC | 1h 15m |
| BRCAT14 | BRC | Roswell Air Center Airport (KROW) | 81NM (81NM) | 2026-04-04 19:54 UTC | 2026-04-04 20:53 UTC | 59m |
| N9454B |  | Byron Airport (KC83) | Byron Airport (KC83) | 2026-04-04 20:11 UTC | 2026-04-04 20:53 UTC | 41m |
| N350BV |  | Meadows Field (KBFL) | Mahogany Mtn Airport (1JY2) | 2026-04-04 19:34 UTC | 2026-04-04 20:51 UTC | 1h 16m |
| BRG530 | BRG | Ralph Wien Memorial Airport (PAOT) | Selawik Airport (PASK) | 2026-04-04 20:21 UTC | 2026-04-04 20:50 UTC | 29m |
| N934FP |  | Mc Ghee Tyson Airport (KTYS) | Crossville Memorial-Whitson Field (KCSV) | 2026-04-04 20:33 UTC | 2026-04-04 20:50 UTC | 16m |
| N229LJ |  | E E Lane Airport (3MS6) | Walls Airport (1AR1) | 2026-04-04 20:29 UTC | 2026-04-04 20:48 UTC | 19m |
| N491LG |  | Tall Timber Airport (CD28) | Athanasiou Valley Airport (CO07) | 2026-04-04 20:32 UTC | 2026-04-04 20:47 UTC | 15m |
| N3288 |  | Livermore Municipal Airport (KLVK) | Livermore Municipal Airport (KLVK) | 2026-04-04 20:46 UTC | 2026-04-04 20:47 UTC | 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
