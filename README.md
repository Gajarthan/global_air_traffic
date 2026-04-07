# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_22:44:32_UTC-green)

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

**Latest saved flight:** 2026-04-07 22:44:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-07 22:44:32 UTC

- **22,329** saved flights
- **11,009** unique routes
- **118** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **22,329** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **276,724.3 tonnes** estimated CO2 emissions
- **16,041,987 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 957 |
| 2 | Ryanair | 929 |
| 3 | IndiGo | 623 |
| 4 | American Airlines | 418 |
| 5 | EJA | 417 |
| 6 | Southwest Airlines | 323 |
| 7 | ENY | 296 |
| 8 | Lufthansa | 281 |
| 9 | Vueling | 233 |
| 10 | LATAM Airlines | 229 |
| 11 | AXM | 214 |
| 12 | Delta Air Lines | 194 |
| 13 | All Nippon Airways | 193 |
| 14 | LXJ | 189 |
| 15 | QLK | 186 |
| 16 | AZU | 176 |
| 17 | Swiss International | 162 |
| 18 | VIV | 159 |
| 19 | Alaska Airlines | 153 |
| 20 | easyJet | 149 |
| 21 | Japan Airlines | 148 |
| 22 | United Airlines | 146 |
| 23 | EJU | 143 |
| 24 | Avianca | 139 |
| 25 | AEE | 138 |
| 26 | WIF | 134 |
| 27 | EDV | 133 |
| 28 | AXB | 126 |
| 29 | Air France | 119 |
| 30 | JetBlue | 114 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 17686 |
| 2 | 🇮🇳 IN | 1901 |
| 3 | 🇪🇸 ES | 1739 |
| 4 | 🇦🇺 AU | 1570 |
| 5 | 🇧🇷 BR | 1268 |
| 6 | 🇯🇵 JP | 1214 |
| 7 | 🇨🇴 CO | 1179 |
| 8 | 🇮🇹 IT | 1128 |
| 9 | 🇩🇪 DE | 1109 |
| 10 | 🇨🇦 CA | 995 |
| 11 | 🇬🇧 GB | 882 |
| 12 | 🇫🇷 FR | 815 |
| 13 | 🇲🇽 MX | 737 |
| 14 | 🇬🇷 GR | 630 |
| 15 | 🇨🇭 CH | 604 |
| 16 | 🇲🇾 MY | 501 |
| 17 | 🇿🇦 ZA | 492 |
| 18 | 🇳🇴 NO | 467 |
| 19 | 🇬🇹 GT | 465 |
| 20 | 🇳🇿 NZ | 453 |
| 21 | 🇹🇷 TR | 429 |
| 22 | 🇵🇭 PH | 415 |
| 23 | 🇰🇷 KR | 389 |
| 24 | 🇹🇭 TH | 349 |
| 25 | 🇵🇱 PL | 321 |
| 26 | 🇲🇦 MA | 269 |
| 27 | 🇧🇸 BS | 242 |
| 28 | 🇮🇩 ID | 231 |
| 29 | 🇲🇪 ME | 231 |
| 30 | 🇳🇱 NL | 221 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 542 |
| 2 | El Dorado International Airport |  | CO | 442 |
| 3 | Tokyo International Airport |  | JP | 410 |
| 4 | Denver International Airport |  | US | 401 |
| 5 | Indira Gandhi International Airport |  | IN | 382 |
| 6 | La Aurora Airport |  | GT | 320 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 302 |
| 8 | Harry Reid International Airport |  | US | 298 |
| 9 | Zurich Airport |  | CH | 269 |
| 10 | Frankfurt am Main International Airport |  | DE | 248 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 238 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 236 |
| 13 | Chicago O'Hare International Airport |  | US | 235 |
| 14 | Guaymaral Airport |  | CO | 234 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 219 |
| 16 | Charlotte/Douglas International Airport |  | US | 214 |
| 17 | Bengaluru International Airport |  | IN | 214 |
| 18 | Macau International Airport |  | MO | 204 |
| 19 | Tenerife Norte Airport |  | ES | 202 |
| 20 | Madrid Barajas International Airport |  | ES | 200 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 192 |
| 22 | Ninoy Aquino International Airport |  | PH | 190 |
| 23 | Congonhas Airport |  | BR | 184 |
| 24 | Salt Lake City International Airport |  | US | 178 |
| 25 | Kuala Lumpur International Airport |  | MY | 178 |
| 26 | Malpensa International Airport |  | IT | 174 |
| 27 | Daniel K Inouye International Airport |  | US | 173 |
| 28 | Reno/Tahoe International Airport |  | US | 173 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 170 |
| 30 | Charles de Gaulle International Airport |  | FR | 163 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 162 |
| 32 | Miami International Airport |  | US | 154 |
| 33 | O. R. Tambo International Airport |  | ZA | 153 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 151 |
| 35 | Pune Airport |  | IN | 150 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 149 |
| 37 | Vitoria/Foronda Airport |  | ES | 147 |
| 38 | Barcelona International Airport |  | ES | 145 |
| 39 | Seattle-Tacoma International Airport |  | US | 144 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 140 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 103 | 1h 8m | 706 km | 1,254.0 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 95 | 14m | 114 km | 186.3 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 86 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 82 | 24m | 225 km | 318.1 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 77 | 28m | 304 km | 403.7 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 66 | 1h 28m | 910 km | 1,035.7 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 66 | 27m | 152 km | 172.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 61 | 1h 43m | 1,156 km | 1,216.9 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 51 | 19m | 165 km | 145.1 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 50 | 1h 13m | 770 km | 664.2 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 15 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 46 | 55m | 546 km | 433.1 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 45 | 31m | 369 km | 286.4 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 45 | 52m | 556 km | 431.4 t |
| 19 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 42 | 20m | 250 km | 181.4 t |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 41 | 4m | - | - |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 41 | 9m | - | - |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 39 | 46m | 452 km | 303.9 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 38 | 1h 1m | 723 km | 473.7 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 34 | 12m | 15 km | 9.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 33 | 1h 22m | 961 km | 547.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UGLY73 | UGL | Short Creek Airport (8TN7) | Campbell Army Air Field (Fort Campbell) Airport (KHOP) | 2026-04-07 22:07 UTC | 2026-04-07 22:44 UTC | 36m |
| EOV | EOV | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-04-07 21:52 UTC | 2026-04-07 22:39 UTC | 47m |
| N786VC |  | Bentonville Municipal/Louise M Thaden Field (KVBT) | Gravette Field (AR09) | 2026-04-07 22:04 UTC | 2026-04-07 22:37 UTC | 33m |
| TTF | TTF | Merton Airport (YMEO) | Melbourne Essendon Airport (YMEN) | 2026-04-07 22:03 UTC | 2026-04-07 22:35 UTC | 31m |
| TRW | TRW | Camden Airport (YSCN) | Yarrawonga Airport (YYWG) | 2026-04-07 21:13 UTC | 2026-04-07 22:32 UTC | 1h 18m |
| N139PS |  | KU42 (KU42) | KU77 (KU77) | 2026-04-07 21:56 UTC | 2026-04-07 22:31 UTC | 35m |
| N749KJ |  | Seattle Paine Field International Airport (KPAE) | Skagit Regional Airport (KBVS) | 2026-04-07 22:11 UTC | 2026-04-07 22:30 UTC | 18m |
| GH71 |  | Catalina Airport (KAVX) | Catalina Airport (KAVX) | 2026-04-07 21:44 UTC | 2026-04-07 22:28 UTC | 44m |
| TERRY52 | TER | 2XA0 (2XA0) | 2XA0 (2XA0) | 2026-04-07 22:09 UTC | 2026-04-07 22:25 UTC | 16m |
| N248FS |  | Santa Monica Municipal Airport (KSMO) | Riverside Airport (KRAL) | 2026-04-07 21:39 UTC | 2026-04-07 22:24 UTC | 45m |
| RFS713 | RFS | Boeing Field/King County International Airport (KBFI) | William R Fairchild International Airport (KCLM) | 2026-04-07 21:26 UTC | 2026-04-07 22:21 UTC | 54m |
| N532CP |  | Chino Airport (KCNO) | Meadows Field (KBFL) | 2026-04-07 21:53 UTC | 2026-04-07 22:19 UTC | 25m |
| KNIFE27 | KNI | Los Alamitos Army Air Field (KSLI) | San Bernardino International Airport (KSBD) | 2026-04-07 21:42 UTC | 2026-04-07 22:14 UTC | 32m |
| N770BK |  | K47A (K47A) | B Tree Farms Airport (97GA) | 2026-04-07 21:54 UTC | 2026-04-07 22:13 UTC | 19m |
| N96705 |  | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-04-07 21:58 UTC | 2026-04-07 22:12 UTC | 14m |
| THY6297 | Turkish Airlines | Juhu Aerodrome (VAJJ) | Macau International Airport (VMMC) | 2026-04-07 17:32 UTC | 2026-04-07 22:10 UTC | 4h 38m |
| CPA696 | Cathay Pacific | Chhatrapati Shivaji International Airport (VABB) | Macau International Airport (VMMC) | 2026-04-07 17:39 UTC | 2026-04-07 22:09 UTC | 4h 29m |
| CPA395 | Cathay Pacific | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-04-07 19:27 UTC | 2026-04-07 22:07 UTC | 2h 39m |
| KFB236 | KFB | Palm Beach International Airport (KPBI) | Lehigh Valley International Airport (KABE) | 2026-04-07 20:03 UTC | 2026-04-07 22:07 UTC | 2h 3m |
| N755PR |  | Oakland County International Airport (KPTK) | Prices Airport (K9G2) | 2026-04-07 21:53 UTC | 2026-04-07 22:05 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
