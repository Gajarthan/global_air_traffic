# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_20:31:52_UTC-green)

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

**Latest saved flight:** 2026-04-11 20:31:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-11 20:31:52 UTC

- **29,597** saved flights
- **13,664** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **29,597** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **360,494.5 tonnes** estimated CO2 emissions
- **20,898,232 km** total distance flown
- **842 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1224 |
| 2 | SkyWest Airlines | 1206 |
| 3 | IndiGo | 767 |
| 4 | EJA | 514 |
| 5 | American Airlines | 510 |
| 6 | Southwest Airlines | 426 |
| 7 | ENY | 396 |
| 8 | Lufthansa | 358 |
| 9 | AXM | 314 |
| 10 | Vueling | 305 |
| 11 | LATAM Airlines | 289 |
| 12 | All Nippon Airways | 263 |
| 13 | AZU | 258 |
| 14 | QLK | 254 |
| 15 | Delta Air Lines | 245 |
| 16 | LXJ | 238 |
| 17 | Swiss International | 217 |
| 18 | Alaska Airlines | 196 |
| 19 | easyJet | 193 |
| 20 | EJU | 192 |
| 21 | VIV | 191 |
| 22 | Japan Airlines | 190 |
| 23 | WIF | 187 |
| 24 | AEE | 186 |
| 25 | United Airlines | 179 |
| 26 | EDV | 173 |
| 27 | Avianca | 164 |
| 28 | JetBlue | 156 |
| 29 | GLO | 155 |
| 30 | Air France | 154 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 23406 |
| 2 | 🇮🇳 IN | 2357 |
| 3 | 🇪🇸 ES | 2206 |
| 4 | 🇦🇺 AU | 2088 |
| 5 | 🇧🇷 BR | 1702 |
| 6 | 🇯🇵 JP | 1608 |
| 7 | 🇮🇹 IT | 1525 |
| 8 | 🇨🇴 CO | 1491 |
| 9 | 🇩🇪 DE | 1488 |
| 10 | 🇨🇦 CA | 1453 |
| 11 | 🇬🇧 GB | 1198 |
| 12 | 🇫🇷 FR | 1096 |
| 13 | 🇲🇽 MX | 946 |
| 14 | 🇬🇷 GR | 843 |
| 15 | 🇨🇭 CH | 840 |
| 16 | 🇲🇾 MY | 751 |
| 17 | 🇳🇿 NZ | 636 |
| 18 | 🇳🇴 NO | 630 |
| 19 | 🇿🇦 ZA | 609 |
| 20 | 🇬🇹 GT | 547 |
| 21 | 🇵🇭 PH | 547 |
| 22 | 🇹🇷 TR | 537 |
| 23 | 🇹🇭 TH | 532 |
| 24 | 🇰🇷 KR | 497 |
| 25 | 🇵🇱 PL | 449 |
| 26 | 🇲🇦 MA | 372 |
| 27 | 🇧🇸 BS | 316 |
| 28 | 🇲🇪 ME | 297 |
| 29 | 🇳🇱 NL | 285 |
| 30 | 🇮🇩 ID | 278 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 701 |
| 2 | Tokyo International Airport |  | JP | 540 |
| 3 | El Dorado International Airport |  | CO | 530 |
| 4 | Denver International Airport |  | US | 501 |
| 5 | Indira Gandhi International Airport |  | IN | 491 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 412 |
| 7 | La Aurora Airport |  | GT | 390 |
| 8 | Harry Reid International Airport |  | US | 380 |
| 9 | Zurich Airport |  | CH | 358 |
| 10 | Guaymaral Airport |  | CO | 355 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 307 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 306 |
| 13 | Chicago O'Hare International Airport |  | US | 306 |
| 14 | Frankfurt am Main International Airport |  | DE | 300 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 289 |
| 16 | Kuala Lumpur International Airport |  | MY | 282 |
| 17 | Macau International Airport |  | MO | 272 |
| 18 | Bengaluru International Airport |  | IN | 268 |
| 19 | Charlotte/Douglas International Airport |  | US | 267 |
| 20 | Madrid Barajas International Airport |  | ES | 263 |
| 21 | Tenerife Norte Airport |  | ES | 261 |
| 22 | Ninoy Aquino International Airport |  | PH | 251 |
| 23 | Congonhas Airport |  | BR | 249 |
| 24 | Malpensa International Airport |  | IT | 236 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 229 |
| 26 | Daniel K Inouye International Airport |  | US | 227 |
| 27 | Salt Lake City International Airport |  | US | 227 |
| 28 | Reno/Tahoe International Airport |  | US | 222 |
| 29 | Charles de Gaulle International Airport |  | FR | 211 |
| 30 | Capua Airport |  | IT | 205 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 204 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 200 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 199 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 198 |
| 35 | Miami International Airport |  | US | 195 |
| 36 | O. R. Tambo International Airport |  | ZA | 194 |
| 37 | Vitoria/Foronda Airport |  | ES | 192 |
| 38 | Barcelona International Airport |  | ES | 188 |
| 39 | Seattle-Tacoma International Airport |  | US | 185 |
| 40 | Viracopos International Airport |  | BR | 180 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 139 | 1h 8m | 706 km | 1,692.3 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 138 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 123 | 14m | 114 km | 241.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 109 | 24m | 225 km | 422.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 100 | 28m | 304 km | 524.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 86 | 1h 27m | 910 km | 1,349.5 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 74 | 19m | 165 km | 210.5 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 74 | 21m | 99 km | 126.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 73 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 65 | 55m | 546 km | 612.0 t |
| 13 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 64 | 9m | - | - |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 63 | 27m | 275 km | 298.5 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 62 | 1h 12m | 770 km | 823.6 t |
| 16 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 56 | 31m | 369 km | 356.5 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 54 | 52m | 556 km | 517.6 t |
| 19 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 53 | 46m | 452 km | 413.1 t |
| 20 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 52 | 21m | 244 km | 219.0 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 50 | 20m | 250 km | 216.0 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 48 | 13m | 99 km | 82.3 t |
| 23 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 46 | 1h 42m | 1,423 km | 1,128.9 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 45 | 20m | 147 km | 113.9 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 41 | 12m | 15 km | 10.8 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 41 | 1h 19m | 961 km | 679.6 t |
| 30 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 39 | 26m | 215 km | 144.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-04-11 06:08 UTC | 2026-04-11 20:31 UTC | 14h 23m |
| N862YB |  | Albuquerque International Sunport Airport (KABQ) | Los Alamos Airport (KLAM) | 2026-04-11 20:11 UTC | 2026-04-11 20:31 UTC | 19m |
| HKC6652 | HKC | VGZR (VGZR) | Zhuhai Airport (ZGSD) | 2026-04-11 14:55 UTC | 2026-04-11 20:29 UTC | 5h 33m |
| TGW156 | TGW | Changi Air Base (WSAC) | VV02 (VV02) | 2026-04-11 19:02 UTC | 2026-04-11 20:25 UTC | 1h 22m |
| N758KC |  | Lake In The Hills Airport (K3CK) | 0IL8 (0IL8) | 2026-04-11 19:38 UTC | 2026-04-11 20:22 UTC | 43m |
| N443BG |  | Wood County Airport (K1G0) | Findlay Airport (KFDY) | 2026-04-11 19:36 UTC | 2026-04-11 20:19 UTC | 43m |
| EJA310 | EJA | Harry Reid International Airport (KLAS) | Rocky Mountain Metro Airport (KBJC) | 2026-04-11 18:53 UTC | 2026-04-11 20:18 UTC | 1h 25m |
| CXK1070 | CXK | Long Beach (Daugherty Field) Airport (KLGB) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-04-11 19:06 UTC | 2026-04-11 20:17 UTC | 1h 11m |
| UPS22 | UPS | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-04-11 09:00 UTC | 2026-04-11 20:17 UTC | 11h 17m |
| XBVFS | XBV | Licenciado Benito Juarez International Airport (MMMX) | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | 2026-04-11 19:42 UTC | 2026-04-11 20:15 UTC | 33m |
| N22PP |  | Walters Airport (0MD6) | Ronald Reagan Washington Ntl Airport (KDCA) | 2026-04-11 19:54 UTC | 2026-04-11 20:12 UTC | 18m |
| N118RK |  | 1AR8 (1AR8) | Brickey Airport (AR43) | 2026-04-11 20:00 UTC | 2026-04-11 20:11 UTC | 10m |
|  |  | Stanton Airport (KI50) | Stanton Airport (KI50) | 2026-04-11 20:01 UTC | 2026-04-11 20:06 UTC | 4m |
| N12834 |  | Ferrell Field (00PN) | Grove City Airport (K29D) | 2026-04-11 19:56 UTC | 2026-04-11 20:04 UTC | 8m |
| N692PD |  | Kansas City Downtown/Wheeler Field (KMKC) | Kansas City Downtown/Wheeler Field (KMKC) | 2026-04-11 19:41 UTC | 2026-04-11 20:04 UTC | 22m |
| HK5431G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-11 19:36 UTC | 2026-04-11 19:59 UTC | 22m |
| N15C |  | Northwest Arkansas Ntl Airport (KXNA) | 9TA2 (9TA2) | 2026-04-11 18:45 UTC | 2026-04-11 19:58 UTC | 1h 12m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-11 19:33 UTC | 2026-04-11 19:55 UTC | 21m |
| N734ND |  | Fort Lauderdale Executive Airport (KFXE) | Pompano Beach Airpark (KPMP) | 2026-04-11 18:45 UTC | 2026-04-11 19:49 UTC | 1h 4m |
| GPD954 | GPD | Luis Munoz Marin International Airport (TJSJ) | Cyril E King Airport (TIST) | 2026-04-11 19:32 UTC | 2026-04-11 19:48 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
