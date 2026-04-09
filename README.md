# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_23:45:28_UTC-green)

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

**Latest saved flight:** 2026-04-08 23:45:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-08 23:45:28 UTC

- **24,361** saved flights
- **11,786** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **24,361** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **301,116.8 tonnes** estimated CO2 emissions
- **17,456,044 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1020 |
| 2 | Ryanair | 1000 |
| 3 | IndiGo | 669 |
| 4 | American Airlines | 447 |
| 5 | EJA | 444 |
| 6 | Southwest Airlines | 352 |
| 7 | ENY | 324 |
| 8 | Lufthansa | 308 |
| 9 | Vueling | 250 |
| 10 | AXM | 244 |
| 11 | LATAM Airlines | 244 |
| 12 | QLK | 222 |
| 13 | All Nippon Airways | 218 |
| 14 | Delta Air Lines | 208 |
| 15 | LXJ | 197 |
| 16 | AZU | 192 |
| 17 | Swiss International | 174 |
| 18 | Alaska Airlines | 167 |
| 19 | VIV | 163 |
| 20 | Japan Airlines | 162 |
| 21 | easyJet | 161 |
| 22 | EJU | 156 |
| 23 | AEE | 151 |
| 24 | WIF | 150 |
| 25 | United Airlines | 149 |
| 26 | Avianca | 144 |
| 27 | EDV | 144 |
| 28 | AXB | 138 |
| 29 | ANZ | 126 |
| 30 | GLO | 126 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 19208 |
| 2 | 🇮🇳 IN | 2037 |
| 3 | 🇪🇸 ES | 1831 |
| 4 | 🇦🇺 AU | 1800 |
| 5 | 🇧🇷 BR | 1367 |
| 6 | 🇯🇵 JP | 1357 |
| 7 | 🇨🇴 CO | 1245 |
| 8 | 🇩🇪 DE | 1236 |
| 9 | 🇮🇹 IT | 1231 |
| 10 | 🇨🇦 CA | 1125 |
| 11 | 🇬🇧 GB | 981 |
| 12 | 🇫🇷 FR | 891 |
| 13 | 🇲🇽 MX | 781 |
| 14 | 🇬🇷 GR | 690 |
| 15 | 🇨🇭 CH | 664 |
| 16 | 🇲🇾 MY | 577 |
| 17 | 🇳🇿 NZ | 525 |
| 18 | 🇳🇴 NO | 517 |
| 19 | 🇿🇦 ZA | 516 |
| 20 | 🇬🇹 GT | 480 |
| 21 | 🇹🇷 TR | 465 |
| 22 | 🇵🇭 PH | 457 |
| 23 | 🇰🇷 KR | 434 |
| 24 | 🇹🇭 TH | 390 |
| 25 | 🇵🇱 PL | 357 |
| 26 | 🇲🇦 MA | 295 |
| 27 | 🇮🇩 ID | 251 |
| 28 | 🇧🇸 BS | 251 |
| 29 | 🇲🇪 ME | 250 |
| 30 | 🇳🇱 NL | 239 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 584 |
| 2 | El Dorado International Airport |  | CO | 462 |
| 3 | Tokyo International Airport |  | JP | 450 |
| 4 | Denver International Airport |  | US | 432 |
| 5 | Indira Gandhi International Airport |  | IN | 420 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 336 |
| 7 | La Aurora Airport |  | GT | 331 |
| 8 | Harry Reid International Airport |  | US | 321 |
| 9 | Zurich Airport |  | CH | 287 |
| 10 | Frankfurt am Main International Airport |  | DE | 263 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 259 |
| 12 | Guaymaral Airport |  | CO | 257 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 253 |
| 14 | Chicago O'Hare International Airport |  | US | 253 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 248 |
| 16 | Macau International Airport |  | MO | 236 |
| 17 | Charlotte/Douglas International Airport |  | US | 230 |
| 18 | Bengaluru International Airport |  | IN | 228 |
| 19 | Ninoy Aquino International Airport |  | PH | 211 |
| 20 | Madrid Barajas International Airport |  | ES | 211 |
| 21 | Kuala Lumpur International Airport |  | MY | 211 |
| 22 | Tenerife Norte Airport |  | ES | 209 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 197 |
| 24 | Malpensa International Airport |  | IT | 196 |
| 25 | Congonhas Airport |  | BR | 196 |
| 26 | Salt Lake City International Airport |  | US | 194 |
| 27 | Daniel K Inouye International Airport |  | US | 185 |
| 28 | Reno/Tahoe International Airport |  | US | 184 |
| 29 | Charles de Gaulle International Airport |  | FR | 175 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 171 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 171 |
| 32 | Miami International Airport |  | US | 165 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 164 |
| 34 | O. R. Tambo International Airport |  | ZA | 161 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 160 |
| 36 | Pune Airport |  | IN | 160 |
| 37 | Seattle-Tacoma International Airport |  | US | 157 |
| 38 | Barcelona International Airport |  | ES | 155 |
| 39 | Vitoria/Foronda Airport |  | ES | 154 |
| 40 | Calgary International Airport |  | CA | 143 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 115 | 1h 8m | 706 km | 1,400.1 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 101 | 14m | 114 km | 198.1 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 95 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 93 | 24m | 225 km | 360.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 85 | 28m | 304 km | 445.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 70 | 1h 27m | 910 km | 1,098.5 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 70 | 22m | 99 km | 119.9 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 67 | 27m | 152 km | 175.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 58 | 19m | 165 km | 165.0 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 52 | 55m | 546 km | 489.6 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 52 | 1h 13m | 770 km | 690.8 t |
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
| NPN | NPN | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-04-08 23:28 UTC | 2026-04-08 23:45 UTC | 16m |
| N947EL |  | Centennial Airport (KAPA) | Austin-Bergstrom International Airport (KAUS) | 2026-04-08 21:58 UTC | 2026-04-08 23:33 UTC | 1h 34m |
| N6338F |  | Princeton Airport (K39N) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-04-08 22:51 UTC | 2026-04-08 23:32 UTC | 40m |
| N302JD |  | Stillwater Regional Airport (KSWO) | Stillwater Regional Airport (KSWO) | 2026-04-08 23:31 UTC | 2026-04-08 23:31 UTC | 0m |
| UAL475 | United Airlines | Edmonton / Gartner Airport (CFQ7) | Denver International Airport (KDEN) | 2026-04-08 21:16 UTC | 2026-04-08 23:30 UTC | 2h 13m |
| N734PU |  | Mckinney Ntl Airport (KTKI) | Casey Field (TE06) | 2026-04-08 22:49 UTC | 2026-04-08 23:28 UTC | 38m |
| FFAB123 | FFA | Norfolk Ns (Chambers Field) Airport (KNGU) | Norfolk Ns (Chambers Field) Airport (KNGU) | 2026-04-08 22:37 UTC | 2026-04-08 23:26 UTC | 49m |
| XABNT | XAB | Licenciado Benito Juarez International Airport (MMMX) | Licenciado Benito Juarez International Airport (MMMX) | 2026-04-08 23:12 UTC | 2026-04-08 23:24 UTC | 11m |
| N738AH |  | Jonesboro Municipal Airport (KJBR) | Jonesboro Municipal Airport (KJBR) | 2026-04-08 22:57 UTC | 2026-04-08 23:19 UTC | 22m |
| N8888X |  | Saline County Regional Airport (KSUZ) | Saline County Regional Airport (KSUZ) | 2026-04-08 23:06 UTC | 2026-04-08 23:16 UTC | 10m |
| QLK9D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-04-08 22:54 UTC | 2026-04-08 23:16 UTC | 21m |
| N36PJ |  | Denver International Airport (KDEN) | Music Mountain Air Ranch Airport (68AZ) | 2026-04-08 21:06 UTC | 2026-04-08 23:14 UTC | 2h 7m |
| LKC | LKC | Perth Jandakot Airport (YPJT) | Ballidu Airport (YBIU) | 2026-04-08 22:07 UTC | 2026-04-08 23:06 UTC | 59m |
| SKW389T | SkyWest Airlines | Denver International Airport (KDEN) | K2K3 (K2K3) | 2026-04-08 22:33 UTC | 2026-04-08 23:06 UTC | 32m |
| N63663 |  | Murfreesboro Municipal Airport (KMBT) | Rachel's Landing Airport (8TN6) | 2026-04-08 22:56 UTC | 2026-04-08 23:04 UTC | 7m |
| NJM888 | NJM | Aiken Regional Airport (KAIK) | Orlando Executive Airport (KORL) | 2026-04-08 21:59 UTC | 2026-04-08 23:03 UTC | 1h 3m |
| N911LL |  | Gaines County Airport (KGNC) | Gaines County Airport (KGNC) | 2026-04-08 23:02 UTC | 2026-04-08 23:03 UTC | 1m |
| LIFELN2 | LIF | City Of Colorado Springs Municipal Airport (KCOS) | 1CO7 (1CO7) | 2026-04-08 22:33 UTC | 2026-04-08 23:01 UTC | 28m |
| N76SN |  | Gerald R Ford International Airport (KGRR) | Boire Field (KASH) | 2026-04-08 21:27 UTC | 2026-04-08 23:01 UTC | 1h 33m |
| OBE | OBE | Perth Jandakot Airport (YPJT) | Merredin Airport (YMDN) | 2026-04-08 22:06 UTC | 2026-04-08 23:00 UTC | 54m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
