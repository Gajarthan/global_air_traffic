# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_09:30:27_UTC-green)

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

**Latest saved flight:** 2026-04-09 09:30:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-09 09:30:27 UTC

- **24,770** saved flights
- **11,915** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **24,770** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **307,325.7 tonnes** estimated CO2 emissions
- **17,815,982 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1021 |
| 2 | Ryanair | 1019 |
| 3 | IndiGo | 684 |
| 4 | American Airlines | 448 |
| 5 | EJA | 447 |
| 6 | Southwest Airlines | 354 |
| 7 | ENY | 324 |
| 8 | Lufthansa | 323 |
| 9 | Vueling | 257 |
| 10 | AXM | 253 |
| 11 | LATAM Airlines | 244 |
| 12 | QLK | 230 |
| 13 | All Nippon Airways | 226 |
| 14 | Delta Air Lines | 209 |
| 15 | LXJ | 198 |
| 16 | AZU | 194 |
| 17 | Swiss International | 180 |
| 18 | Alaska Airlines | 175 |
| 19 | Japan Airlines | 168 |
| 20 | VIV | 165 |
| 21 | easyJet | 164 |
| 22 | EJU | 158 |
| 23 | WIF | 154 |
| 24 | AEE | 153 |
| 25 | United Airlines | 149 |
| 26 | Avianca | 145 |
| 27 | EDV | 145 |
| 28 | AXB | 141 |
| 29 | Cathay Pacific | 130 |
| 30 | ANZ | 128 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 19349 |
| 2 | 🇮🇳 IN | 2093 |
| 3 | 🇦🇺 AU | 1870 |
| 4 | 🇪🇸 ES | 1864 |
| 5 | 🇯🇵 JP | 1405 |
| 6 | 🇧🇷 BR | 1374 |
| 7 | 🇩🇪 DE | 1282 |
| 8 | 🇨🇴 CO | 1257 |
| 9 | 🇮🇹 IT | 1251 |
| 10 | 🇨🇦 CA | 1150 |
| 11 | 🇬🇧 GB | 1002 |
| 12 | 🇫🇷 FR | 902 |
| 13 | 🇲🇽 MX | 789 |
| 14 | 🇬🇷 GR | 699 |
| 15 | 🇨🇭 CH | 688 |
| 16 | 🇲🇾 MY | 604 |
| 17 | 🇳🇿 NZ | 550 |
| 18 | 🇳🇴 NO | 529 |
| 19 | 🇿🇦 ZA | 518 |
| 20 | 🇬🇹 GT | 482 |
| 21 | 🇹🇷 TR | 476 |
| 22 | 🇵🇭 PH | 472 |
| 23 | 🇰🇷 KR | 443 |
| 24 | 🇹🇭 TH | 411 |
| 25 | 🇵🇱 PL | 365 |
| 26 | 🇲🇦 MA | 302 |
| 27 | 🇮🇩 ID | 256 |
| 28 | 🇲🇴 MO | 251 |
| 29 | 🇧🇸 BS | 251 |
| 30 | 🇲🇪 ME | 251 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 585 |
| 2 | El Dorado International Airport |  | CO | 467 |
| 3 | Tokyo International Airport |  | JP | 467 |
| 4 | Denver International Airport |  | US | 433 |
| 5 | Indira Gandhi International Airport |  | IN | 432 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 339 |
| 7 | La Aurora Airport |  | GT | 332 |
| 8 | Harry Reid International Airport |  | US | 325 |
| 9 | Zurich Airport |  | CH | 295 |
| 10 | Frankfurt am Main International Airport |  | DE | 270 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 259 |
| 12 | Guaymaral Airport |  | CO | 259 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 256 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 255 |
| 15 | Chicago O'Hare International Airport |  | US | 253 |
| 16 | Macau International Airport |  | MO | 251 |
| 17 | Bengaluru International Airport |  | IN | 232 |
| 18 | Charlotte/Douglas International Airport |  | US | 230 |
| 19 | Kuala Lumpur International Airport |  | MY | 220 |
| 20 | Ninoy Aquino International Airport |  | PH | 219 |
| 21 | Madrid Barajas International Airport |  | ES | 214 |
| 22 | Tenerife Norte Airport |  | ES | 213 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 199 |
| 24 | Malpensa International Airport |  | IT | 197 |
| 25 | Congonhas Airport |  | BR | 196 |
| 26 | Salt Lake City International Airport |  | US | 194 |
| 27 | Daniel K Inouye International Airport |  | US | 193 |
| 28 | Reno/Tahoe International Airport |  | US | 184 |
| 29 | Charles de Gaulle International Airport |  | FR | 176 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 175 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 172 |
| 32 | Miami International Airport |  | US | 165 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 164 |
| 34 | Seattle-Tacoma International Airport |  | US | 162 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 162 |
| 36 | O. R. Tambo International Airport |  | ZA | 162 |
| 37 | Barcelona International Airport |  | ES | 160 |
| 38 | Pune Airport |  | IN | 160 |
| 39 | Vitoria/Foronda Airport |  | ES | 156 |
| 40 | Calgary International Airport |  | CA | 146 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 118 | 1h 8m | 706 km | 1,436.7 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 103 | 14m | 114 km | 202.0 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 96 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 95 | 24m | 225 km | 368.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 86 | 28m | 304 km | 450.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 73 | 1h 27m | 910 km | 1,145.5 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 71 | 21m | 99 km | 121.6 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 67 | 27m | 152 km | 175.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 64 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 60 | 19m | 165 km | 170.7 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 56 | 1h 12m | 770 km | 743.9 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 54 | 55m | 546 km | 508.4 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 50 | 27m | 275 km | 236.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 48 | 31m | 369 km | 305.5 t |
| 17 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 47 | 52m | 556 km | 450.5 t |
| 19 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 46 | 45m | 452 km | 358.5 t |
| 20 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 44 | 20m | 250 km | 190.1 t |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 43 | 4m | - | - |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 43 | 9m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 42 | 1h 42m | 1,423 km | 1,030.7 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 40 | 13m | 99 km | 68.6 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 36 | 20m | 147 km | 91.1 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 36 | 12m | 15 km | 9.5 t |
| 29 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 34 | 1h 21m | 961 km | 563.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BNI93 | BNI | Łódź Władysław Reymont Airport (EPLL) | Zielona Góra-Babimost Airport (EPZG) | 2026-04-09 08:13 UTC | 2026-04-09 09:30 UTC | 1h 16m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-04-09 08:29 UTC | 2026-04-09 09:21 UTC | 51m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-04-08 21:46 UTC | 2026-04-09 09:15 UTC | 11h 29m |
| MAS129 | Malaysia Airlines | Kuala Lumpur International Airport (WMKK) | Melbourne International Airport (YMML) | 2026-04-09 02:09 UTC | 2026-04-09 09:12 UTC | 7h 3m |
| AFR188 | Air France | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-04-08 22:01 UTC | 2026-04-09 09:03 UTC | 11h 1m |
| DAKAY | DAK | Munich International Airport (EDDM) | Stuttgart Airport (EDDS) | 2026-04-09 08:29 UTC | 2026-04-09 08:59 UTC | 29m |
| AEE374 | AEE | Eleftherios Venizelos International Airport (LGAV) | Mikonos Airport (LGMK) | 2026-04-09 08:40 UTC | 2026-04-09 08:57 UTC | 17m |
| BEL4QA | Brussels Airlines | Vienna International Airport (LOWW) | Brussels Airport (EBBR) | 2026-04-09 07:25 UTC | 2026-04-09 08:54 UTC | 1h 28m |
| ZKIWG | ZKI | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-04-09 08:41 UTC | 2026-04-09 08:53 UTC | 11m |
| DLH010 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hamburg Airport (EDDH) | 2026-04-09 07:58 UTC | 2026-04-09 08:47 UTC | 48m |
| DLH507 | Lufthansa | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | Frankfurt am Main International Airport (EDDF) | 2026-04-08 22:04 UTC | 2026-04-09 08:45 UTC | 10h 40m |
| SEH1SM | SEH | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-04-09 08:16 UTC | 2026-04-09 08:44 UTC | 27m |
| HBZYJ | HBZ | Bex Airport (LSGB) | Muenster Aero Airport (LSPU) | 2026-04-09 07:07 UTC | 2026-04-09 08:44 UTC | 1h 36m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Macau International Airport (VMMC) | 2026-04-08 21:44 UTC | 2026-04-09 08:42 UTC | 10h 57m |
| EWG68N | EWG | Vienna International Airport (LOWW) | Hamburg Airport (EDDH) | 2026-04-09 07:19 UTC | 2026-04-09 08:41 UTC | 1h 21m |
| HGO770 | HGO | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-07 23:11 UTC | 2026-04-09 08:39 UTC | 33h 27m |
| WZZ6260 | Wizz Air | Mollis Airport (LSZM) | Prijedor Urije Airport (LQPD) | 2026-04-09 07:33 UTC | 2026-04-09 08:39 UTC | 1h 5m |
| RYR76HY | Ryanair | Brussels South Charleroi Airport (EBCI) | Nador International Airport (GMMW) | 2026-04-09 06:08 UTC | 2026-04-09 08:38 UTC | 2h 30m |
| RYR6SW | Ryanair | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Tortoli' / Arbatax Airport (LIET) | 2026-04-09 07:45 UTC | 2026-04-09 08:38 UTC | 52m |
| RYR955M | Ryanair | Alicante International Airport (LEAL) | Hamburg Airport (EDDH) | 2026-04-09 05:57 UTC | 2026-04-09 08:37 UTC | 2h 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
