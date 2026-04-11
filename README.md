# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_13:20:32_UTC-green)

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

**Latest saved flight:** 2026-04-11 13:20:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-11 13:20:32 UTC

- **28,681** saved flights
- **13,347** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **28,681** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **349,108.5 tonnes** estimated CO2 emissions
- **20,238,171 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1176 |
| 2 | SkyWest Airlines | 1155 |
| 3 | IndiGo | 756 |
| 4 | EJA | 503 |
| 5 | American Airlines | 495 |
| 6 | Southwest Airlines | 406 |
| 7 | ENY | 382 |
| 8 | Lufthansa | 350 |
| 9 | AXM | 312 |
| 10 | Vueling | 293 |
| 11 | LATAM Airlines | 280 |
| 12 | All Nippon Airways | 263 |
| 13 | QLK | 254 |
| 14 | Delta Air Lines | 241 |
| 15 | AZU | 239 |
| 16 | LXJ | 232 |
| 17 | Swiss International | 210 |
| 18 | Alaska Airlines | 190 |
| 19 | Japan Airlines | 190 |
| 20 | WIF | 187 |
| 21 | easyJet | 186 |
| 22 | EJU | 185 |
| 23 | VIV | 184 |
| 24 | AEE | 180 |
| 25 | United Airlines | 174 |
| 26 | EDV | 166 |
| 27 | Avianca | 161 |
| 28 | AXB | 151 |
| 29 | JetBlue | 150 |
| 30 | Air France | 148 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 22505 |
| 2 | 🇮🇳 IN | 2330 |
| 3 | 🇪🇸 ES | 2117 |
| 4 | 🇦🇺 AU | 2088 |
| 5 | 🇧🇷 BR | 1625 |
| 6 | 🇯🇵 JP | 1606 |
| 7 | 🇮🇹 IT | 1464 |
| 8 | 🇩🇪 DE | 1449 |
| 9 | 🇨🇴 CO | 1429 |
| 10 | 🇨🇦 CA | 1395 |
| 11 | 🇬🇧 GB | 1159 |
| 12 | 🇫🇷 FR | 1064 |
| 13 | 🇲🇽 MX | 900 |
| 14 | 🇬🇷 GR | 824 |
| 15 | 🇨🇭 CH | 809 |
| 16 | 🇲🇾 MY | 747 |
| 17 | 🇳🇿 NZ | 634 |
| 18 | 🇳🇴 NO | 626 |
| 19 | 🇿🇦 ZA | 601 |
| 20 | 🇵🇭 PH | 545 |
| 21 | 🇹🇭 TH | 528 |
| 22 | 🇬🇹 GT | 525 |
| 23 | 🇹🇷 TR | 521 |
| 24 | 🇰🇷 KR | 497 |
| 25 | 🇵🇱 PL | 433 |
| 26 | 🇲🇦 MA | 352 |
| 27 | 🇧🇸 BS | 297 |
| 28 | 🇲🇪 ME | 288 |
| 29 | 🇳🇱 NL | 279 |
| 30 | 🇮🇩 ID | 278 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 676 |
| 2 | Tokyo International Airport |  | JP | 540 |
| 3 | El Dorado International Airport |  | CO | 516 |
| 4 | Indira Gandhi International Airport |  | IN | 486 |
| 5 | Denver International Airport |  | US | 478 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 403 |
| 7 | La Aurora Airport |  | GT | 370 |
| 8 | Harry Reid International Airport |  | US | 365 |
| 9 | Zurich Airport |  | CH | 346 |
| 10 | Guaymaral Airport |  | CO | 319 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 297 |
| 12 | Frankfurt am Main International Airport |  | DE | 295 |
| 13 | Chicago O'Hare International Airport |  | US | 294 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 290 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 289 |
| 16 | Kuala Lumpur International Airport |  | MY | 280 |
| 17 | Macau International Airport |  | MO | 263 |
| 18 | Bengaluru International Airport |  | IN | 261 |
| 19 | Charlotte/Douglas International Airport |  | US | 258 |
| 20 | Ninoy Aquino International Airport |  | PH | 250 |
| 21 | Madrid Barajas International Airport |  | ES | 249 |
| 22 | Tenerife Norte Airport |  | ES | 247 |
| 23 | Congonhas Airport |  | BR | 234 |
| 24 | Malpensa International Airport |  | IT | 225 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 221 |
| 26 | Salt Lake City International Airport |  | US | 220 |
| 27 | Daniel K Inouye International Airport |  | US | 219 |
| 28 | Reno/Tahoe International Airport |  | US | 210 |
| 29 | Charles de Gaulle International Airport |  | FR | 203 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 198 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 197 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 192 |
| 33 | Capua Airport |  | IT | 191 |
| 34 | O. R. Tambo International Airport |  | ZA | 190 |
| 35 | Miami International Airport |  | US | 189 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 188 |
| 37 | Seattle-Tacoma International Airport |  | US | 181 |
| 38 | Vitoria/Foronda Airport |  | ES | 179 |
| 39 | Barcelona International Airport |  | ES | 179 |
| 40 | Don Mueang International Airport |  | TH | 178 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 139 | 1h 8m | 706 km | 1,692.3 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 122 | 27m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 117 | 14m | 114 km | 229.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 109 | 24m | 225 km | 422.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 100 | 28m | 304 km | 524.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 86 | 1h 27m | 910 km | 1,349.5 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 74 | 21m | 99 km | 126.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 73 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 73 | 19m | 165 km | 207.7 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 65 | 55m | 546 km | 612.0 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 62 | 1h 12m | 770 km | 823.6 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 58 | 27m | 275 km | 274.8 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 56 | 31m | 369 km | 356.5 t |
| 17 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 55 | 9m | - | - |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 53 | 46m | 452 km | 413.1 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 51 | 52m | 556 km | 488.9 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 47 | 20m | 250 km | 203.0 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 46 | 1h 42m | 1,423 km | 1,128.9 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 46 | 13m | 99 km | 78.9 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 45 | 20m | 147 km | 113.9 t |
| 25 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 27 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 44 | 21m | 244 km | 185.3 t |
| 28 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 39 | 26m | 215 km | 144.4 t |
| 29 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 30 | Brisbane International Airport (YBBN) | Monduran Airport (YMUA) | 39 | 31m | 304 km | 204.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9545F |  | Clermont County Airport (KI69) | Clermont County Airport (KI69) | 2026-04-11 13:06 UTC | 2026-04-11 13:20 UTC | 14m |
| TCF625 | TCF | Melbourne Orlando International Airport (KMLB) | Valkaria Airport (KX59) | 2026-04-11 12:04 UTC | 2026-04-11 13:17 UTC | 1h 13m |
| HBZAX | HBZ | Ambri Airport (LSPM) | LSMF (LSMF) | 2026-04-11 12:57 UTC | 2026-04-11 13:17 UTC | 20m |
| G72468 |  | Las Cruces International Airport (KLRU) | Las Cruces International Airport (KLRU) | 2026-04-11 12:06 UTC | 2026-04-11 13:09 UTC | 1h 2m |
| QTR815 | Qatar Airways | Chek Lap Kok International Airport (VHHH) | Chanmyathazi Airport (VYCZ) | 2026-04-11 10:36 UTC | 2026-04-11 13:08 UTC | 2h 31m |
| HBKNS | HBK | Biella / Cerrione Airport (LILE) | Raron Airport (LSTA) | 2026-04-11 12:19 UTC | 2026-04-11 13:04 UTC | 45m |
| C2006 |  | St Paul Island Airport (PASN) | Elmendorf Afb Airport (PAED) | 2026-04-11 11:00 UTC | 2026-04-11 12:55 UTC | 1h 55m |
| DEARO | DEA | Lager Hammelburg Airport (EDFJ) | Wasserkuppe Airport (EDER) | 2026-04-11 12:36 UTC | 2026-04-11 12:50 UTC | 14m |
| N5315T |  | Taunton Municipal/King Field (KTAN) | Norwood Memorial Airport (KOWD) | 2026-04-11 12:28 UTC | 2026-04-11 12:47 UTC | 19m |
| HBZAX | HBZ | Ambri Airport (LSPM) | LSMF (LSMF) | 2026-04-11 12:25 UTC | 2026-04-11 12:42 UTC | 16m |
| HBLVC | HBL | Leutkirch-Unterzeil Airport (EDNL) | Friedrichshafen Airport (EDNY) | 2026-04-11 12:23 UTC | 2026-04-11 12:41 UTC | 18m |
| ANE61HB | ANE | Madrid Barajas International Airport (LEMD) | Federico Garcia Lorca Airport (LEGR) | 2026-04-11 11:59 UTC | 2026-04-11 12:39 UTC | 39m |
| WIF8GH | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-11 12:15 UTC | 2026-04-11 12:38 UTC | 22m |
| N383AA |  | Malin Airport (SOML) | Quiruvilca Airport (SPQR) | 2026-04-11 12:24 UTC | 2026-04-11 12:36 UTC | 12m |
| PSGLB | PSG | Campo de Marte Airport (SBMT) | Congonhas Airport (SBSP) | 2026-04-11 12:08 UTC | 2026-04-11 12:35 UTC | 27m |
| FGSAT | FGS | Verona / Boscomantico Airport (LIPN) | Verona / Boscomantico Airport (LIPN) | 2026-04-11 12:22 UTC | 2026-04-11 12:32 UTC | 9m |
| RYR6KF | Ryanair | Copernicus Wrocław Airport (EPWR) | Vlora Internationa Airport (LAVL) | 2026-04-11 11:08 UTC | 2026-04-11 12:32 UTC | 1h 23m |
| HK5309G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-11 12:03 UTC | 2026-04-11 12:30 UTC | 27m |
| CNS712 | CNS | Hancock County/Bar Harbor Airport (KBHB) | General Edward Lawrence Logan International Airport (KBOS) | 2026-04-11 11:51 UTC | 2026-04-11 12:30 UTC | 38m |
| N9226F |  | Lewis University Airport (KLOT) | Lewis University Airport (KLOT) | 2026-04-11 12:15 UTC | 2026-04-11 12:30 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
