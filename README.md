# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_18:25:04_UTC-green)

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

**Latest saved flight:** 2026-04-09 18:25:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-09 18:25:04 UTC

- **25,522** saved flights
- **12,210** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **25,522** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **315,455.6 tonnes** estimated CO2 emissions
- **18,287,283 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1056 |
| 2 | SkyWest Airlines | 1041 |
| 3 | IndiGo | 702 |
| 4 | American Airlines | 457 |
| 5 | EJA | 455 |
| 6 | Southwest Airlines | 363 |
| 7 | Lufthansa | 332 |
| 8 | ENY | 329 |
| 9 | Vueling | 265 |
| 10 | AXM | 260 |
| 11 | LATAM Airlines | 251 |
| 12 | All Nippon Airways | 231 |
| 13 | QLK | 230 |
| 14 | Delta Air Lines | 214 |
| 15 | LXJ | 204 |
| 16 | AZU | 199 |
| 17 | Swiss International | 181 |
| 18 | Alaska Airlines | 176 |
| 19 | Japan Airlines | 171 |
| 20 | VIV | 171 |
| 21 | EJU | 168 |
| 22 | easyJet | 168 |
| 23 | WIF | 162 |
| 24 | AEE | 161 |
| 25 | United Airlines | 152 |
| 26 | EDV | 149 |
| 27 | Avianca | 148 |
| 28 | AXB | 144 |
| 29 | Air France | 133 |
| 30 | BRC | 133 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 19918 |
| 2 | 🇮🇳 IN | 2151 |
| 3 | 🇪🇸 ES | 1927 |
| 4 | 🇦🇺 AU | 1880 |
| 5 | 🇯🇵 JP | 1434 |
| 6 | 🇧🇷 BR | 1426 |
| 7 | 🇩🇪 DE | 1327 |
| 8 | 🇮🇹 IT | 1310 |
| 9 | 🇨🇴 CO | 1290 |
| 10 | 🇨🇦 CA | 1187 |
| 11 | 🇬🇧 GB | 1037 |
| 12 | 🇫🇷 FR | 954 |
| 13 | 🇲🇽 MX | 825 |
| 14 | 🇬🇷 GR | 732 |
| 15 | 🇨🇭 CH | 713 |
| 16 | 🇲🇾 MY | 624 |
| 17 | 🇳🇴 NO | 550 |
| 18 | 🇳🇿 NZ | 550 |
| 19 | 🇿🇦 ZA | 532 |
| 20 | 🇹🇷 TR | 487 |
| 21 | 🇬🇹 GT | 483 |
| 22 | 🇵🇭 PH | 478 |
| 23 | 🇰🇷 KR | 447 |
| 24 | 🇹🇭 TH | 432 |
| 25 | 🇵🇱 PL | 382 |
| 26 | 🇲🇦 MA | 314 |
| 27 | 🇧🇸 BS | 265 |
| 28 | 🇮🇩 ID | 258 |
| 29 | 🇲🇪 ME | 258 |
| 30 | 🇳🇱 NL | 256 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 596 |
| 2 | Tokyo International Airport |  | JP | 480 |
| 3 | El Dorado International Airport |  | CO | 479 |
| 4 | Indira Gandhi International Airport |  | IN | 444 |
| 5 | Denver International Airport |  | US | 434 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 356 |
| 7 | La Aurora Airport |  | GT | 333 |
| 8 | Harry Reid International Airport |  | US | 331 |
| 9 | Zurich Airport |  | CH | 303 |
| 10 | Frankfurt am Main International Airport |  | DE | 278 |
| 11 | Guaymaral Airport |  | CO | 270 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 267 |
| 13 | Chicago O'Hare International Airport |  | US | 262 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 260 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 256 |
| 16 | Macau International Airport |  | MO | 253 |
| 17 | Charlotte/Douglas International Airport |  | US | 235 |
| 18 | Bengaluru International Airport |  | IN | 235 |
| 19 | Kuala Lumpur International Airport |  | MY | 231 |
| 20 | Tenerife Norte Airport |  | ES | 224 |
| 21 | Ninoy Aquino International Airport |  | PH | 222 |
| 22 | Madrid Barajas International Airport |  | ES | 219 |
| 23 | Malpensa International Airport |  | IT | 205 |
| 24 | Atizapan De Zaragoza Airport |  | MX | 204 |
| 25 | Congonhas Airport |  | BR | 201 |
| 26 | Daniel K Inouye International Airport |  | US | 196 |
| 27 | Salt Lake City International Airport |  | US | 196 |
| 28 | Reno/Tahoe International Airport |  | US | 187 |
| 29 | Charles de Gaulle International Airport |  | FR | 184 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 179 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 177 |
| 32 | Miami International Airport |  | US | 171 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 169 |
| 34 | O. R. Tambo International Airport |  | ZA | 168 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 167 |
| 36 | Barcelona International Airport |  | ES | 166 |
| 37 | Seattle-Tacoma International Airport |  | US | 163 |
| 38 | Vitoria/Foronda Airport |  | ES | 161 |
| 39 | Pune Airport |  | IN | 160 |
| 40 | Capua Airport |  | IT | 155 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 122 | 1h 8m | 706 km | 1,485.4 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 104 | 14m | 114 km | 204.0 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 101 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 95 | 24m | 225 km | 368.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 86 | 28m | 304 km | 450.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 74 | 1h 27m | 910 km | 1,161.2 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 71 | 21m | 99 km | 121.6 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 67 | 27m | 152 km | 175.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 65 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 64 | 19m | 165 km | 182.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 59 | 1h 12m | 770 km | 783.8 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 54 | 55m | 546 km | 508.4 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 52 | 27m | 275 km | 246.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 50 | 31m | 369 km | 318.3 t |
| 17 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 47 | 45m | 452 km | 366.3 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 47 | 52m | 556 km | 450.5 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 46 | 20m | 250 km | 198.7 t |
| 21 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 23 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 43 | 4m | - | - |
| 24 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 43 | 9m | - | - |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 42 | 13m | 99 km | 72.0 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 38 | 21m | 147 km | 96.2 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 37 | 12m | 15 km | 9.8 t |
| 29 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 35 | 1h 21m | 961 km | 580.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N664CA |  | Buchanan Field (KCCR) | Livermore Municipal Airport (KLVK) | 2026-04-09 17:48 UTC | 2026-04-09 18:25 UTC | 36m |
| CXK644 | CXK | Dupage Airport (KDPA) | Wade Airport (56LL) | 2026-04-09 17:38 UTC | 2026-04-09 18:21 UTC | 43m |
| N677TX |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-04-09 17:50 UTC | 2026-04-09 18:19 UTC | 29m |
| CARD11 | CAR | Flysooner Field (OK50) | Henderson Farm Airport (35OL) | 2026-04-09 17:54 UTC | 2026-04-09 18:17 UTC | 23m |
| N6812W |  | MI72 (MI72) | 84MI (84MI) | 2026-04-09 16:39 UTC | 2026-04-09 18:16 UTC | 1h 37m |
| N1536Y |  | Cross Keys Airport (K17N) | Millville Municipal Airport (KMIV) | 2026-04-09 17:39 UTC | 2026-04-09 18:14 UTC | 35m |
| CXK469 | CXK | Baton Rouge Metro, Ryan Field (KBTR) | False River Regional Airport (KHZR) | 2026-04-09 18:02 UTC | 2026-04-09 18:14 UTC | 11m |
| ARCAS32 | ARC | 4TA5 (4TA5) | TX20 (TX20) | 2026-04-09 17:54 UTC | 2026-04-09 18:10 UTC | 16m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-04-09 16:13 UTC | 2026-04-09 18:08 UTC | 1h 55m |
| BRG561 | BRG | Shungnak Airport (PAGH) | Ambler Airport (PAFM) | 2026-04-09 17:57 UTC | 2026-04-09 18:08 UTC | 11m |
| N944VB |  | Newport News/Williamsburg International Airport (KPHF) | Norfolk International Airport (KORF) | 2026-04-09 17:49 UTC | 2026-04-09 18:03 UTC | 13m |
| N227MF |  | Phoenix Deer Valley Airport (KDVT) | Telluride Regional Airport (KTEX) | 2026-04-09 16:21 UTC | 2026-04-09 18:01 UTC | 1h 39m |
| N584CC |  | NJ58 (NJ58) | NJ58 (NJ58) | 2026-04-09 17:58 UTC | 2026-04-09 18:00 UTC | 2m |
| N39JM |  | Terrell Municipal Airport (KTRL) | Grove Hill Airport (5TX2) | 2026-04-09 17:31 UTC | 2026-04-09 17:57 UTC | 25m |
| DRAFT81 | DRA | Bagdad Airport (KE51) | AZ00 (AZ00) | 2026-04-09 17:27 UTC | 2026-04-09 17:54 UTC | 26m |
| BGST02 | BGS | Corpus Christi Nas (Truax Field) Airport (KNGP) | Beech Factory Airport (KBEC) | 2026-04-09 15:26 UTC | 2026-04-09 17:53 UTC | 2h 26m |
| N73NY |  | Lake Havasu City Airport (KHII) | Laughlin/Bullhead International Airport (KIFP) | 2026-04-09 16:29 UTC | 2026-04-09 17:53 UTC | 1h 23m |
| MAFIA21 | MAF | Fort Clark Springs Airport (74TX) | Anacacho Ranch Airport (0XS7) | 2026-04-09 17:33 UTC | 2026-04-09 17:51 UTC | 17m |
| CFDYL | CFD | Vancouver International Airport (CYVR) | Pitt Meadows Airport (CYPK) | 2026-04-09 17:31 UTC | 2026-04-09 17:50 UTC | 18m |
| BRCAT05 | BRC | Jenkins Airport (NM87) | 81NM (81NM) | 2026-04-09 17:07 UTC | 2026-04-09 17:49 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
