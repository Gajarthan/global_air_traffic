# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_20:04:04_UTC-green)

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

**Latest saved flight:** 2026-04-11 20:04:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-11 20:04:04 UTC

- **29,530** saved flights
- **13,642** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **29,530** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **359,210.8 tonnes** estimated CO2 emissions
- **20,823,815 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1219 |
| 2 | SkyWest Airlines | 1202 |
| 3 | IndiGo | 767 |
| 4 | EJA | 509 |
| 5 | American Airlines | 508 |
| 6 | Southwest Airlines | 423 |
| 7 | ENY | 396 |
| 8 | Lufthansa | 358 |
| 9 | AXM | 314 |
| 10 | Vueling | 304 |
| 11 | LATAM Airlines | 288 |
| 12 | All Nippon Airways | 263 |
| 13 | AZU | 257 |
| 14 | QLK | 254 |
| 15 | Delta Air Lines | 245 |
| 16 | LXJ | 238 |
| 17 | Swiss International | 217 |
| 18 | Alaska Airlines | 195 |
| 19 | EJU | 192 |
| 20 | easyJet | 192 |
| 21 | VIV | 191 |
| 22 | Japan Airlines | 190 |
| 23 | WIF | 187 |
| 24 | AEE | 186 |
| 25 | United Airlines | 178 |
| 26 | EDV | 173 |
| 27 | Avianca | 164 |
| 28 | JetBlue | 156 |
| 29 | Air France | 154 |
| 30 | GLO | 154 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 23345 |
| 2 | 🇮🇳 IN | 2357 |
| 3 | 🇪🇸 ES | 2197 |
| 4 | 🇦🇺 AU | 2088 |
| 5 | 🇧🇷 BR | 1697 |
| 6 | 🇯🇵 JP | 1608 |
| 7 | 🇮🇹 IT | 1521 |
| 8 | 🇩🇪 DE | 1487 |
| 9 | 🇨🇴 CO | 1483 |
| 10 | 🇨🇦 CA | 1448 |
| 11 | 🇬🇧 GB | 1193 |
| 12 | 🇫🇷 FR | 1093 |
| 13 | 🇲🇽 MX | 943 |
| 14 | 🇬🇷 GR | 843 |
| 15 | 🇨🇭 CH | 840 |
| 16 | 🇲🇾 MY | 751 |
| 17 | 🇳🇿 NZ | 636 |
| 18 | 🇳🇴 NO | 630 |
| 19 | 🇿🇦 ZA | 609 |
| 20 | 🇵🇭 PH | 547 |
| 21 | 🇬🇹 GT | 545 |
| 22 | 🇹🇷 TR | 535 |
| 23 | 🇹🇭 TH | 532 |
| 24 | 🇰🇷 KR | 497 |
| 25 | 🇵🇱 PL | 447 |
| 26 | 🇲🇦 MA | 371 |
| 27 | 🇧🇸 BS | 314 |
| 28 | 🇲🇪 ME | 296 |
| 29 | 🇳🇱 NL | 285 |
| 30 | 🇮🇩 ID | 278 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 699 |
| 2 | Tokyo International Airport |  | JP | 540 |
| 3 | El Dorado International Airport |  | CO | 527 |
| 4 | Denver International Airport |  | US | 495 |
| 5 | Indira Gandhi International Airport |  | IN | 491 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 412 |
| 7 | La Aurora Airport |  | GT | 389 |
| 8 | Harry Reid International Airport |  | US | 379 |
| 9 | Zurich Airport |  | CH | 358 |
| 10 | Guaymaral Airport |  | CO | 352 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 307 |
| 12 | Chicago O'Hare International Airport |  | US | 306 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 305 |
| 14 | Frankfurt am Main International Airport |  | DE | 299 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 289 |
| 16 | Kuala Lumpur International Airport |  | MY | 282 |
| 17 | Macau International Airport |  | MO | 270 |
| 18 | Bengaluru International Airport |  | IN | 268 |
| 19 | Charlotte/Douglas International Airport |  | US | 266 |
| 20 | Madrid Barajas International Airport |  | ES | 262 |
| 21 | Tenerife Norte Airport |  | ES | 257 |
| 22 | Ninoy Aquino International Airport |  | PH | 251 |
| 23 | Congonhas Airport |  | BR | 249 |
| 24 | Malpensa International Airport |  | IT | 235 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 229 |
| 26 | Salt Lake City International Airport |  | US | 227 |
| 27 | Daniel K Inouye International Airport |  | US | 225 |
| 28 | Reno/Tahoe International Airport |  | US | 220 |
| 29 | Charles de Gaulle International Airport |  | FR | 210 |
| 30 | Capua Airport |  | IT | 204 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 203 |
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
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 137 | 26m | - | - |
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
| 20 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 50 | 21m | 244 km | 210.5 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 50 | 20m | 250 km | 216.0 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 47 | 13m | 99 km | 80.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 46 | 1h 42m | 1,423 km | 1,128.9 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 45 | 20m | 147 km | 113.9 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 41 | 1h 19m | 961 km | 679.6 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 40 | 12m | 15 km | 10.6 t |
| 30 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 39 | 26m | 215 km | 144.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N692PD |  | Kansas City Downtown/Wheeler Field (KMKC) | Kansas City Downtown/Wheeler Field (KMKC) | 2026-04-11 19:41 UTC | 2026-04-11 20:04 UTC | 22m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-11 19:33 UTC | 2026-04-11 19:55 UTC | 21m |
| N734ND |  | Fort Lauderdale Executive Airport (KFXE) | Pompano Beach Airpark (KPMP) | 2026-04-11 18:45 UTC | 2026-04-11 19:49 UTC | 1h 4m |
| N777WY |  | Gleim Field (FD81) | Lazy S Farm Airport (7FL7) | 2026-04-11 19:19 UTC | 2026-04-11 19:42 UTC | 22m |
| UAE9841 | Emirates | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-11 00:53 UTC | 2026-04-11 19:39 UTC | 18h 45m |
| N28220 |  | Santa Monica Municipal Airport (KSMO) | Santa Monica Municipal Airport (KSMO) | 2026-04-11 18:20 UTC | 2026-04-11 19:37 UTC | 1h 17m |
| N945RF |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-04-11 18:27 UTC | 2026-04-11 19:32 UTC | 1h 5m |
| N25995 |  | Denton Enterprise Airport (KDTO) | 5TS4 (5TS4) | 2026-04-11 19:10 UTC | 2026-04-11 19:31 UTC | 21m |
| EJM304 | EJM | Scottsdale Airport (KSDL) | Buffalo Niagara International Airport (KBUF) | 2026-04-11 15:49 UTC | 2026-04-11 19:30 UTC | 3h 41m |
| BRG3621 | BRG | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-04-11 18:38 UTC | 2026-04-11 19:30 UTC | 51m |
| ICY88 | ICY | Elmendorf Afb Airport (PAED) | Highland Airport (47AK) | 2026-04-11 18:31 UTC | 2026-04-11 19:25 UTC | 54m |
| ASP814 | ASP | Hartsfield/Jackson Atlanta International Airport (KATL) | Toronto Pearson International Airport (CYYZ) | 2026-04-11 17:37 UTC | 2026-04-11 19:25 UTC | 1h 47m |
| KSF44 | KSF | Kent State University Airport (K1G3) | Portage County Airport (KPOV) | 2026-04-11 19:17 UTC | 2026-04-11 19:23 UTC | 6m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-11 18:58 UTC | 2026-04-11 19:23 UTC | 25m |
| N9652F |  | Ashland County Airport (K3G4) | Ashland County Airport (K3G4) | 2026-04-11 19:08 UTC | 2026-04-11 19:22 UTC | 13m |
| N468AK |  | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-04-11 18:50 UTC | 2026-04-11 19:21 UTC | 31m |
| SDE561 | SDE | Scottsdale Airport (KSDL) | Weyburn Airport (CJE3) | 2026-04-11 17:01 UTC | 2026-04-11 19:20 UTC | 2h 18m |
| N169BA |  | Bb Airpark (TE88) | Garrett Ranch Airport (77XS) | 2026-04-11 19:09 UTC | 2026-04-11 19:17 UTC | 7m |
| XBONC | XBO | Ingeniero Juan Guillermo Villasana Airport (MMPC) | Hermanos Serdan International Airport (MMPB) | 2026-04-11 18:41 UTC | 2026-04-11 19:17 UTC | 35m |
| N523AB |  | Erie Municipal Airport (KEIK) | Erie Municipal Airport (KEIK) | 2026-04-11 18:35 UTC | 2026-04-11 19:13 UTC | 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
