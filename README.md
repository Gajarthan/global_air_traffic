# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_22:48:10_UTC-green)

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

**Latest saved flight:** 2026-04-09 22:48:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-09 22:48:10 UTC

- **26,088** saved flights
- **12,455** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **26,088** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **321,530.1 tonnes** estimated CO2 emissions
- **18,639,424 km** total distance flown
- **850 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1077 |
| 2 | Ryanair | 1072 |
| 3 | IndiGo | 702 |
| 4 | EJA | 469 |
| 5 | American Airlines | 467 |
| 6 | Southwest Airlines | 376 |
| 7 | ENY | 343 |
| 8 | Lufthansa | 338 |
| 9 | Vueling | 266 |
| 10 | AXM | 260 |
| 11 | LATAM Airlines | 259 |
| 12 | All Nippon Airways | 231 |
| 13 | QLK | 231 |
| 14 | Delta Air Lines | 218 |
| 15 | LXJ | 210 |
| 16 | AZU | 207 |
| 17 | Swiss International | 181 |
| 18 | Alaska Airlines | 180 |
| 19 | VIV | 175 |
| 20 | Japan Airlines | 171 |
| 21 | EJU | 169 |
| 22 | easyJet | 169 |
| 23 | WIF | 165 |
| 24 | AEE | 164 |
| 25 | United Airlines | 157 |
| 26 | EDV | 153 |
| 27 | Avianca | 150 |
| 28 | AXB | 144 |
| 29 | Cathay Pacific | 136 |
| 30 | JetBlue | 136 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 20625 |
| 2 | 🇮🇳 IN | 2152 |
| 3 | 🇪🇸 ES | 1944 |
| 4 | 🇦🇺 AU | 1884 |
| 5 | 🇧🇷 BR | 1472 |
| 6 | 🇯🇵 JP | 1436 |
| 7 | 🇩🇪 DE | 1342 |
| 8 | 🇮🇹 IT | 1326 |
| 9 | 🇨🇴 CO | 1315 |
| 10 | 🇨🇦 CA | 1233 |
| 11 | 🇬🇧 GB | 1046 |
| 12 | 🇫🇷 FR | 963 |
| 13 | 🇲🇽 MX | 844 |
| 14 | 🇬🇷 GR | 743 |
| 15 | 🇨🇭 CH | 716 |
| 16 | 🇲🇾 MY | 624 |
| 17 | 🇳🇿 NZ | 568 |
| 18 | 🇳🇴 NO | 559 |
| 19 | 🇿🇦 ZA | 532 |
| 20 | 🇹🇷 TR | 492 |
| 21 | 🇬🇹 GT | 489 |
| 22 | 🇵🇭 PH | 480 |
| 23 | 🇰🇷 KR | 448 |
| 24 | 🇹🇭 TH | 433 |
| 25 | 🇵🇱 PL | 385 |
| 26 | 🇲🇦 MA | 320 |
| 27 | 🇧🇸 BS | 271 |
| 28 | 🇲🇪 ME | 260 |
| 29 | 🇲🇴 MO | 259 |
| 30 | 🇮🇩 ID | 258 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 615 |
| 2 | El Dorado International Airport |  | CO | 488 |
| 3 | Tokyo International Airport |  | JP | 481 |
| 4 | Denver International Airport |  | US | 446 |
| 5 | Indira Gandhi International Airport |  | IN | 444 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 361 |
| 7 | La Aurora Airport |  | GT | 339 |
| 8 | Harry Reid International Airport |  | US | 338 |
| 9 | Zurich Airport |  | CH | 306 |
| 10 | Frankfurt am Main International Airport |  | DE | 283 |
| 11 | Guaymaral Airport |  | CO | 276 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 272 |
| 13 | Chicago O'Hare International Airport |  | US | 268 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 266 |
| 15 | Macau International Airport |  | MO | 259 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 256 |
| 17 | Charlotte/Douglas International Airport |  | US | 241 |
| 18 | Bengaluru International Airport |  | IN | 235 |
| 19 | Kuala Lumpur International Airport |  | MY | 231 |
| 20 | Tenerife Norte Airport |  | ES | 228 |
| 21 | Ninoy Aquino International Airport |  | PH | 223 |
| 22 | Madrid Barajas International Airport |  | ES | 222 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 206 |
| 24 | Malpensa International Airport |  | IT | 205 |
| 25 | Congonhas Airport |  | BR | 204 |
| 26 | Salt Lake City International Airport |  | US | 203 |
| 27 | Daniel K Inouye International Airport |  | US | 200 |
| 28 | Reno/Tahoe International Airport |  | US | 193 |
| 29 | Charles de Gaulle International Airport |  | FR | 185 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 184 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 180 |
| 32 | Miami International Airport |  | US | 177 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 173 |
| 34 | Seattle-Tacoma International Airport |  | US | 168 |
| 35 | Barcelona International Airport |  | ES | 168 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 168 |
| 37 | O. R. Tambo International Airport |  | ZA | 168 |
| 38 | Vitoria/Foronda Airport |  | ES | 163 |
| 39 | Capua Airport |  | IT | 161 |
| 40 | Pune Airport |  | IN | 160 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 123 | 1h 8m | 706 km | 1,497.5 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 107 | 14m | 114 km | 209.9 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 103 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 95 | 24m | 225 km | 368.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 86 | 28m | 304 km | 450.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 74 | 1h 27m | 910 km | 1,161.2 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 71 | 21m | 99 km | 121.6 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 68 | 27m | 152 km | 177.7 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 65 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 64 | 19m | 165 km | 182.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 59 | 1h 12m | 770 km | 783.8 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 54 | 55m | 546 km | 508.4 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 53 | 27m | 275 km | 251.1 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 51 | 31m | 369 km | 324.6 t |
| 17 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 47 | 45m | 452 km | 366.3 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 47 | 52m | 556 km | 450.5 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 46 | 20m | 250 km | 198.7 t |
| 21 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 45 | 9m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 43 | 13m | 99 km | 73.7 t |
| 25 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 43 | 4m | - | - |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 38 | 21m | 147 km | 96.2 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 38 | 12m | 15 km | 10.0 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 36 | 1h 21m | 961 km | 596.7 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 36 | 15m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N97ML |  | Oakland County International Airport (KPTK) | St Clair County International Airport (KPHN) | 2026-04-09 22:17 UTC | 2026-04-09 22:48 UTC | 30m |
| GRYHK12 | GRY | Miramar Mcas (Joe Foss Field) Airport (KNKX) | Camp Pendleton Mcas (Munn Field) Airport (KNFG) | 2026-04-09 22:03 UTC | 2026-04-09 22:39 UTC | 36m |
| MPH9441 | MPH | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-04-09 11:35 UTC | 2026-04-09 22:37 UTC | 11h 1m |
| DUKE81 | DUK | 75OK (75OK) | Tulsa International Airport (KTUL) | 2026-04-09 22:02 UTC | 2026-04-09 22:34 UTC | 32m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-04-09 11:55 UTC | 2026-04-09 22:34 UTC | 10h 38m |
| FLC71 | FLC | Grant County International Airport (KMWH) | Fairchild Afb Airport (KSKA) | 2026-04-09 20:58 UTC | 2026-04-09 22:32 UTC | 1h 34m |
| CPA318 | Cathay Pacific | Barcelona International Airport (LEBL) | Macau International Airport (VMMC) | 2026-04-09 11:12 UTC | 2026-04-09 22:30 UTC | 11h 17m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Macau International Airport (VMMC) | 2026-04-09 10:37 UTC | 2026-04-09 22:29 UTC | 11h 52m |
| N225TF |  | Corona Municipal Airport (KAJO) | Hemet-Ryan Airport (KHMT) | 2026-04-09 22:01 UTC | 2026-04-09 22:27 UTC | 25m |
| LS26 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-04-09 20:44 UTC | 2026-04-09 22:26 UTC | 1h 41m |
| N686RH |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-04-09 16:18 UTC | 2026-04-09 22:22 UTC | 6h 3m |
| CPA300 | Cathay Pacific | Munich International Airport (EDDM) | Macau International Airport (VMMC) | 2026-04-09 11:58 UTC | 2026-04-09 22:21 UTC | 10h 22m |
| TWY235 | TWY | Miami-Opa Locka Executive Airport (KOPF) | Witham Field (KSUA) | 2026-04-09 21:48 UTC | 2026-04-09 22:18 UTC | 30m |
| CPA2047 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-09 10:39 UTC | 2026-04-09 22:18 UTC | 11h 38m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-09 22:06 UTC | 2026-04-09 22:17 UTC | 11m |
| EJA665 | EJA | Salt Lake City International Airport (KSLC) | Provo Municipal Airport (KPVU) | 2026-04-09 21:58 UTC | 2026-04-09 22:17 UTC | 18m |
| N77ME |  | Clark Regional Airport (KJVY) | Aiken Regional Airport (KAIK) | 2026-04-09 21:00 UTC | 2026-04-09 22:16 UTC | 1h 16m |
| LXJ405 | LXJ | Westchester County Airport (KHPN) | General Edward Lawrence Logan International Airport (KBOS) | 2026-04-09 21:26 UTC | 2026-04-09 22:12 UTC | 46m |
| N73784 |  | Denton Enterprise Airport (KDTO) | Dreamland Airport (XA48) | 2026-04-09 21:38 UTC | 2026-04-09 22:12 UTC | 33m |
| N225MK |  | North Exuma Airport (85FA) | Orlando Executive Airport (KORL) | 2026-04-09 21:58 UTC | 2026-04-09 22:12 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
