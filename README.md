# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_03:07:35_UTC-green)

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

**Latest saved flight:** 2026-04-09 03:07:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-09 03:07:35 UTC

- **24,471** saved flights
- **11,809** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **24,471** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **302,191.6 tonnes** estimated CO2 emissions
- **17,518,356 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1021 |
| 2 | Ryanair | 1000 |
| 3 | IndiGo | 672 |
| 4 | American Airlines | 448 |
| 5 | EJA | 446 |
| 6 | Southwest Airlines | 353 |
| 7 | ENY | 324 |
| 8 | Lufthansa | 308 |
| 9 | Vueling | 250 |
| 10 | AXM | 246 |
| 11 | LATAM Airlines | 244 |
| 12 | QLK | 223 |
| 13 | All Nippon Airways | 220 |
| 14 | Delta Air Lines | 208 |
| 15 | LXJ | 198 |
| 16 | AZU | 193 |
| 17 | Swiss International | 174 |
| 18 | Alaska Airlines | 171 |
| 19 | VIV | 165 |
| 20 | Japan Airlines | 163 |
| 21 | easyJet | 161 |
| 22 | EJU | 156 |
| 23 | AEE | 151 |
| 24 | WIF | 150 |
| 25 | United Airlines | 149 |
| 26 | Avianca | 145 |
| 27 | EDV | 144 |
| 28 | AXB | 139 |
| 29 | ANZ | 127 |
| 30 | GLO | 127 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 19290 |
| 2 | 🇮🇳 IN | 2050 |
| 3 | 🇪🇸 ES | 1831 |
| 4 | 🇦🇺 AU | 1817 |
| 5 | 🇧🇷 BR | 1371 |
| 6 | 🇯🇵 JP | 1369 |
| 7 | 🇨🇴 CO | 1255 |
| 8 | 🇩🇪 DE | 1237 |
| 9 | 🇮🇹 IT | 1231 |
| 10 | 🇨🇦 CA | 1143 |
| 11 | 🇬🇧 GB | 982 |
| 12 | 🇫🇷 FR | 891 |
| 13 | 🇲🇽 MX | 789 |
| 14 | 🇬🇷 GR | 690 |
| 15 | 🇨🇭 CH | 664 |
| 16 | 🇲🇾 MY | 581 |
| 17 | 🇳🇿 NZ | 538 |
| 18 | 🇳🇴 NO | 517 |
| 19 | 🇿🇦 ZA | 516 |
| 20 | 🇬🇹 GT | 480 |
| 21 | 🇹🇷 TR | 466 |
| 22 | 🇵🇭 PH | 462 |
| 23 | 🇰🇷 KR | 434 |
| 24 | 🇹🇭 TH | 397 |
| 25 | 🇵🇱 PL | 357 |
| 26 | 🇲🇦 MA | 295 |
| 27 | 🇮🇩 ID | 253 |
| 28 | 🇧🇸 BS | 251 |
| 29 | 🇲🇪 ME | 250 |
| 30 | 🇲🇴 MO | 241 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 584 |
| 2 | El Dorado International Airport |  | CO | 466 |
| 3 | Tokyo International Airport |  | JP | 455 |
| 4 | Denver International Airport |  | US | 433 |
| 5 | Indira Gandhi International Airport |  | IN | 423 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 336 |
| 7 | La Aurora Airport |  | GT | 331 |
| 8 | Harry Reid International Airport |  | US | 324 |
| 9 | Zurich Airport |  | CH | 287 |
| 10 | Frankfurt am Main International Airport |  | DE | 263 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 259 |
| 12 | Guaymaral Airport |  | CO | 259 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 255 |
| 14 | Chicago O'Hare International Airport |  | US | 253 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 250 |
| 16 | Macau International Airport |  | MO | 241 |
| 17 | Charlotte/Douglas International Airport |  | US | 230 |
| 18 | Bengaluru International Airport |  | IN | 229 |
| 19 | Ninoy Aquino International Airport |  | PH | 214 |
| 20 | Kuala Lumpur International Airport |  | MY | 213 |
| 21 | Madrid Barajas International Airport |  | ES | 211 |
| 22 | Tenerife Norte Airport |  | ES | 209 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 199 |
| 24 | Malpensa International Airport |  | IT | 196 |
| 25 | Congonhas Airport |  | BR | 196 |
| 26 | Salt Lake City International Airport |  | US | 194 |
| 27 | Daniel K Inouye International Airport |  | US | 189 |
| 28 | Reno/Tahoe International Airport |  | US | 184 |
| 29 | Charles de Gaulle International Airport |  | FR | 175 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 173 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 171 |
| 32 | Miami International Airport |  | US | 165 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 164 |
| 34 | O. R. Tambo International Airport |  | ZA | 161 |
| 35 | Seattle-Tacoma International Airport |  | US | 160 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 160 |
| 37 | Pune Airport |  | IN | 160 |
| 38 | Barcelona International Airport |  | ES | 155 |
| 39 | Vitoria/Foronda Airport |  | ES | 154 |
| 40 | Calgary International Airport |  | CA | 146 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 116 | 1h 8m | 706 km | 1,412.3 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 102 | 14m | 114 km | 200.1 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 96 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 94 | 24m | 225 km | 364.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 85 | 28m | 304 km | 445.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 71 | 1h 27m | 910 km | 1,114.2 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 70 | 22m | 99 km | 119.9 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 67 | 27m | 152 km | 175.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 59 | 19m | 165 km | 167.8 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 53 | 1h 12m | 770 km | 704.1 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 52 | 55m | 546 km | 489.6 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 49 | 27m | 275 km | 232.2 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 47 | 31m | 369 km | 299.2 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 47 | 52m | 556 km | 450.5 t |
| 19 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 44 | 46m | 452 km | 342.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 44 | 20m | 250 km | 190.1 t |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 43 | 4m | - | - |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 43 | 9m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 41 | 1h 43m | 1,423 km | 1,006.2 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 40 | 13m | 99 km | 68.6 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 36 | 20m | 147 km | 91.1 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 36 | 12m | 15 km | 9.5 t |
| 29 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 34 | 1h 21m | 961 km | 563.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N225LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Van Nuys Airport (KVNY) | 2026-04-09 02:05 UTC | 2026-04-09 03:07 UTC | 1h 1m |
| RSCU511 | RSC | Toowoomba Airport (YTWB) | Watts Bridge Airport (YWSG) | 2026-04-09 02:36 UTC | 2026-04-09 03:06 UTC | 30m |
| N839SP |  | Roberts Field (KRDM) | OR02 (OR02) | 2026-04-09 02:48 UTC | 2026-04-09 03:06 UTC | 18m |
| 8BE |  | Holbrook Airport (YHBK) | Tamworth Airport (YSTW) | 2026-04-09 01:51 UTC | 2026-04-09 03:04 UTC | 1h 13m |
| ZKTTL | ZKT | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-04-09 02:35 UTC | 2026-04-09 02:55 UTC | 20m |
| VIR155M | Virgin Atlantic | London Heathrow Airport (EGLL) | Harry Reid International Airport (KLAS) | 2026-04-08 17:01 UTC | 2026-04-09 02:47 UTC | 9h 46m |
| LS26 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-04-09 02:13 UTC | 2026-04-09 02:41 UTC | 27m |
| N772CA |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-04-09 01:56 UTC | 2026-04-09 02:41 UTC | 44m |
| RANGR41 | RAN | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-04-09 02:16 UTC | 2026-04-09 02:37 UTC | 21m |
| UNV | UNV | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-04-09 01:38 UTC | 2026-04-09 02:33 UTC | 55m |
| CJT590 | CJT | Saskatoon John G. Diefenbaker International Airport (CYXE) | Regina Beach Airport (CKL9) | 2026-04-09 02:11 UTC | 2026-04-09 02:30 UTC | 19m |
| N7529U |  | Double Eagle Ii Airport (KAEG) | Skywagon Farm Airport (NM88) | 2026-04-09 01:52 UTC | 2026-04-09 02:28 UTC | 35m |
| EJA915 | EJA | Palm Beach International Airport (KPBI) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-04-09 00:30 UTC | 2026-04-09 02:25 UTC | 1h 55m |
| N109BG |  | Los Angeles International Airport (KLAX) | Ernst Field (86CL) | 2026-04-09 01:55 UTC | 2026-04-09 02:24 UTC | 28m |
| MGL297 | MGL | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-08 10:48 UTC | 2026-04-09 02:20 UTC | 15h 31m |
| CPA660 | Cathay Pacific | Chhatrapati Shivaji International Airport (VABB) | Macau International Airport (VMMC) | 2026-04-08 21:42 UTC | 2026-04-09 02:18 UTC | 4h 36m |
| CWA935 | CWA | Edmonton International Airport (CYEG) | Two Hills Airport (CEL6) | 2026-04-09 02:01 UTC | 2026-04-09 02:18 UTC | 17m |
| BTN701 | BTN | Suvarnabhumi Airport (VTBS) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-08 23:55 UTC | 2026-04-09 02:17 UTC | 2h 22m |
| ZKTTL | ZKT | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-04-09 01:53 UTC | 2026-04-09 02:16 UTC | 23m |
| UAE9836 | Emirates | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-08 07:05 UTC | 2026-04-09 02:14 UTC | 19h 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
