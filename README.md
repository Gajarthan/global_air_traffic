# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_10:48:17_UTC-green)

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

**Latest saved flight:** 2026-04-11 10:48:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-11 10:48:17 UTC

- **28,477** saved flights
- **13,300** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **28,477** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **346,414.1 tonnes** estimated CO2 emissions
- **20,081,979 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1161 |
| 2 | SkyWest Airlines | 1155 |
| 3 | IndiGo | 750 |
| 4 | EJA | 502 |
| 5 | American Airlines | 495 |
| 6 | Southwest Airlines | 406 |
| 7 | ENY | 382 |
| 8 | Lufthansa | 346 |
| 9 | AXM | 305 |
| 10 | Vueling | 291 |
| 11 | LATAM Airlines | 275 |
| 12 | All Nippon Airways | 261 |
| 13 | QLK | 254 |
| 14 | Delta Air Lines | 240 |
| 15 | AZU | 236 |
| 16 | LXJ | 232 |
| 17 | Swiss International | 206 |
| 18 | Alaska Airlines | 190 |
| 19 | Japan Airlines | 187 |
| 20 | easyJet | 184 |
| 21 | EJU | 183 |
| 22 | VIV | 183 |
| 23 | WIF | 183 |
| 24 | AEE | 180 |
| 25 | United Airlines | 173 |
| 26 | EDV | 166 |
| 27 | Avianca | 159 |
| 28 | AXB | 150 |
| 29 | JetBlue | 150 |
| 30 | Air France | 145 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 22466 |
| 2 | 🇮🇳 IN | 2309 |
| 3 | 🇪🇸 ES | 2094 |
| 4 | 🇦🇺 AU | 2080 |
| 5 | 🇧🇷 BR | 1599 |
| 6 | 🇯🇵 JP | 1585 |
| 7 | 🇮🇹 IT | 1438 |
| 8 | 🇩🇪 DE | 1433 |
| 9 | 🇨🇴 CO | 1407 |
| 10 | 🇨🇦 CA | 1393 |
| 11 | 🇬🇧 GB | 1148 |
| 12 | 🇫🇷 FR | 1052 |
| 13 | 🇲🇽 MX | 898 |
| 14 | 🇬🇷 GR | 821 |
| 15 | 🇨🇭 CH | 790 |
| 16 | 🇲🇾 MY | 729 |
| 17 | 🇳🇿 NZ | 634 |
| 18 | 🇳🇴 NO | 617 |
| 19 | 🇿🇦 ZA | 585 |
| 20 | 🇵🇭 PH | 543 |
| 21 | 🇬🇹 GT | 525 |
| 22 | 🇹🇷 TR | 515 |
| 23 | 🇹🇭 TH | 509 |
| 24 | 🇰🇷 KR | 492 |
| 25 | 🇵🇱 PL | 426 |
| 26 | 🇲🇦 MA | 348 |
| 27 | 🇧🇸 BS | 296 |
| 28 | 🇲🇪 ME | 282 |
| 29 | 🇳🇱 NL | 275 |
| 30 | 🇮🇩 ID | 275 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 676 |
| 2 | Tokyo International Airport |  | JP | 533 |
| 3 | El Dorado International Airport |  | CO | 511 |
| 4 | Indira Gandhi International Airport |  | IN | 480 |
| 5 | Denver International Airport |  | US | 478 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 401 |
| 7 | La Aurora Airport |  | GT | 370 |
| 8 | Harry Reid International Airport |  | US | 365 |
| 9 | Zurich Airport |  | CH | 341 |
| 10 | Guaymaral Airport |  | CO | 312 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 297 |
| 12 | Chicago O'Hare International Airport |  | US | 294 |
| 13 | Frankfurt am Main International Airport |  | DE | 293 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 290 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 289 |
| 16 | Kuala Lumpur International Airport |  | MY | 272 |
| 17 | Macau International Airport |  | MO | 263 |
| 18 | Bengaluru International Airport |  | IN | 259 |
| 19 | Charlotte/Douglas International Airport |  | US | 257 |
| 20 | Ninoy Aquino International Airport |  | PH | 249 |
| 21 | Madrid Barajas International Airport |  | ES | 245 |
| 22 | Tenerife Norte Airport |  | ES | 242 |
| 23 | Congonhas Airport |  | BR | 228 |
| 24 | Malpensa International Airport |  | IT | 221 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 220 |
| 26 | Salt Lake City International Airport |  | US | 220 |
| 27 | Daniel K Inouye International Airport |  | US | 219 |
| 28 | Reno/Tahoe International Airport |  | US | 210 |
| 29 | Charles de Gaulle International Airport |  | FR | 200 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 195 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 194 |
| 32 | Miami International Airport |  | US | 189 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 188 |
| 34 | O. R. Tambo International Airport |  | ZA | 186 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 186 |
| 36 | Capua Airport |  | IT | 185 |
| 37 | Seattle-Tacoma International Airport |  | US | 180 |
| 38 | Vitoria/Foronda Airport |  | ES | 178 |
| 39 | Barcelona International Airport |  | ES | 178 |
| 40 | Don Mueang International Airport |  | TH | 173 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 137 | 1h 8m | 706 km | 1,668.0 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 119 | 27m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 115 | 14m | 114 km | 225.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 109 | 24m | 225 km | 422.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 99 | 28m | 304 km | 519.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 84 | 1h 27m | 910 km | 1,318.2 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 74 | 21m | 99 km | 126.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 72 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 71 | 19m | 165 km | 202.0 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 63 | 55m | 546 km | 593.1 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 62 | 1h 12m | 770 km | 823.6 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 58 | 27m | 275 km | 274.8 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 55 | 31m | 369 km | 350.1 t |
| 17 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 55 | 9m | - | - |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 52 | 46m | 452 km | 405.3 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 51 | 52m | 556 km | 488.9 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 47 | 20m | 250 km | 203.0 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 45 | 20m | 147 km | 113.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 45 | 1h 42m | 1,423 km | 1,104.4 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 45 | 13m | 99 km | 77.2 t |
| 25 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 27 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 44 | 21m | 244 km | 185.3 t |
| 28 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 29 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 38 | 26m | 215 km | 140.7 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 38 | 12m | 15 km | 10.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GUIDO | GUI | Redhill Aerodrome (EGKR) | Redhill Aerodrome (EGKR) | 2026-04-11 10:29 UTC | 2026-04-11 10:48 UTC | 18m |
| ANE1113 | ANE | Madrid Barajas International Airport (LEMD) | A Coruna Airport (LECO) | 2026-04-11 09:56 UTC | 2026-04-11 10:41 UTC | 45m |
| ANA860 | All Nippon Airways | Chek Lap Kok International Airport (VHHH) | Tokyo International Airport (RJTT) | 2026-04-11 06:48 UTC | 2026-04-11 10:33 UTC | 3h 45m |
| RTV2N | RTV | Viseu Airport (LPVZ) | Viseu Airport (LPVZ) | 2026-04-11 10:22 UTC | 2026-04-11 10:33 UTC | 10m |
| IE747 |  | Leutkirch-Unterzeil Airport (EDNL) | Leutkirch-Unterzeil Airport (EDNL) | 2026-04-11 10:18 UTC | 2026-04-11 10:24 UTC | 6m |
| LSI143 | LSI | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-04-10 23:26 UTC | 2026-04-11 10:21 UTC | 10h 55m |
| IGO295C | IndiGo | Indira Gandhi International Airport (VIDP) | VIBN (VIBN) | 2026-04-11 09:33 UTC | 2026-04-11 10:20 UTC | 46m |
| HBLVC | HBL | Zurich Airport (LSZH) | Friedrichshafen Airport (EDNY) | 2026-04-11 09:47 UTC | 2026-04-11 10:14 UTC | 27m |
| RYR7SY | Ryanair | Poznań-Ławica Airport (EPPO) | Otocac Airport (LDRO) | 2026-04-11 09:08 UTC | 2026-04-11 10:12 UTC | 1h 4m |
| CXK687 | CXK | Long Island Mac Arthur Airport (KISP) | Talmage Field (03NY) | 2026-04-11 09:57 UTC | 2026-04-11 10:12 UTC | 15m |
| HBZUR | HBZ | Wangen-Lachen Airport (LSPV) | Raron Airport (LSTA) | 2026-04-11 09:29 UTC | 2026-04-11 10:12 UTC | 42m |
| RTV2N | RTV | Vilar Da Luz Airport (LPVL) | Viseu Airport (LPVZ) | 2026-04-11 09:37 UTC | 2026-04-11 10:10 UTC | 32m |
| PSFPG | PSF | Calciolandia Airport (SIKK) | Congonhas Airport (SBSP) | 2026-04-11 09:20 UTC | 2026-04-11 10:08 UTC | 48m |
| AAY1897 | AAY | Harry Reid International Airport (KLAS) | Seattle Paine Field International Airport (KPAE) | 2026-04-11 07:26 UTC | 2026-04-11 10:05 UTC | 2h 39m |
| EVA055 | EVA Air | Chicago O'Hare International Airport (KORD) | Heineck Farm Airport (76WA) | 2026-04-11 05:49 UTC | 2026-04-11 10:05 UTC | 4h 16m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Sandane Airport Anda (ENSD) | 2026-04-11 09:40 UTC | 2026-04-11 10:05 UTC | 24m |
| KLM1799 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Goch-Asperden Airport (EDLG) | 2026-04-11 09:38 UTC | 2026-04-11 10:02 UTC | 24m |
| RYR35CB | Ryanair | Karlsruhe Baden-Baden Airport (EDSB) | Visoko Sport Airfield (LQVI) | 2026-04-11 08:51 UTC | 2026-04-11 10:01 UTC | 1h 10m |
| RYR1963 | Ryanair | Memmingen Allgau Airport (EDJA) | Losinj Island Airport (LDLO) | 2026-04-11 09:21 UTC | 2026-04-11 10:00 UTC | 39m |
| IE747 |  | Valencia Airport (LEVC) | Leutkirch-Unterzeil Airport (EDNL) | 2026-04-11 06:56 UTC | 2026-04-11 10:00 UTC | 3h 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
