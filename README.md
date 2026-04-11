# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_14:48:00_UTC-green)

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

**Latest saved flight:** 2026-04-11 14:48:00 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-11 14:48:00 UTC

- **28,812** saved flights
- **13,390** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **28,812** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **350,635.9 tonnes** estimated CO2 emissions
- **20,326,720 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1184 |
| 2 | SkyWest Airlines | 1157 |
| 3 | IndiGo | 761 |
| 4 | EJA | 504 |
| 5 | American Airlines | 498 |
| 6 | Southwest Airlines | 407 |
| 7 | ENY | 383 |
| 8 | Lufthansa | 350 |
| 9 | AXM | 314 |
| 10 | Vueling | 296 |
| 11 | LATAM Airlines | 282 |
| 12 | All Nippon Airways | 263 |
| 13 | QLK | 254 |
| 14 | AZU | 249 |
| 15 | Delta Air Lines | 241 |
| 16 | LXJ | 232 |
| 17 | Swiss International | 211 |
| 18 | Alaska Airlines | 190 |
| 19 | Japan Airlines | 190 |
| 20 | VIV | 188 |
| 21 | WIF | 187 |
| 22 | EJU | 186 |
| 23 | easyJet | 186 |
| 24 | AEE | 180 |
| 25 | United Airlines | 174 |
| 26 | EDV | 166 |
| 27 | Avianca | 162 |
| 28 | AXB | 153 |
| 29 | JetBlue | 150 |
| 30 | Air France | 148 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 22587 |
| 2 | 🇮🇳 IN | 2344 |
| 3 | 🇪🇸 ES | 2133 |
| 4 | 🇦🇺 AU | 2088 |
| 5 | 🇧🇷 BR | 1650 |
| 6 | 🇯🇵 JP | 1606 |
| 7 | 🇮🇹 IT | 1472 |
| 8 | 🇩🇪 DE | 1456 |
| 9 | 🇨🇴 CO | 1439 |
| 10 | 🇨🇦 CA | 1408 |
| 11 | 🇬🇧 GB | 1166 |
| 12 | 🇫🇷 FR | 1067 |
| 13 | 🇲🇽 MX | 913 |
| 14 | 🇬🇷 GR | 824 |
| 15 | 🇨🇭 CH | 820 |
| 16 | 🇲🇾 MY | 751 |
| 17 | 🇳🇿 NZ | 636 |
| 18 | 🇳🇴 NO | 629 |
| 19 | 🇿🇦 ZA | 603 |
| 20 | 🇵🇭 PH | 545 |
| 21 | 🇹🇭 TH | 532 |
| 22 | 🇬🇹 GT | 531 |
| 23 | 🇹🇷 TR | 521 |
| 24 | 🇰🇷 KR | 497 |
| 25 | 🇵🇱 PL | 435 |
| 26 | 🇲🇦 MA | 354 |
| 27 | 🇧🇸 BS | 300 |
| 28 | 🇲🇪 ME | 289 |
| 29 | 🇳🇱 NL | 281 |
| 30 | 🇮🇩 ID | 278 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 679 |
| 2 | Tokyo International Airport |  | JP | 540 |
| 3 | El Dorado International Airport |  | CO | 517 |
| 4 | Indira Gandhi International Airport |  | IN | 487 |
| 5 | Denver International Airport |  | US | 478 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 403 |
| 7 | La Aurora Airport |  | GT | 376 |
| 8 | Harry Reid International Airport |  | US | 365 |
| 9 | Zurich Airport |  | CH | 347 |
| 10 | Guaymaral Airport |  | CO | 327 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 297 |
| 12 | Chicago O'Hare International Airport |  | US | 295 |
| 13 | Frankfurt am Main International Airport |  | DE | 295 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 290 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 289 |
| 16 | Kuala Lumpur International Airport |  | MY | 282 |
| 17 | Macau International Airport |  | MO | 265 |
| 18 | Bengaluru International Airport |  | IN | 265 |
| 19 | Charlotte/Douglas International Airport |  | US | 258 |
| 20 | Madrid Barajas International Airport |  | ES | 252 |
| 21 | Ninoy Aquino International Airport |  | PH | 250 |
| 22 | Tenerife Norte Airport |  | ES | 247 |
| 23 | Congonhas Airport |  | BR | 238 |
| 24 | Malpensa International Airport |  | IT | 226 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 224 |
| 26 | Salt Lake City International Airport |  | US | 221 |
| 27 | Daniel K Inouye International Airport |  | US | 220 |
| 28 | Reno/Tahoe International Airport |  | US | 210 |
| 29 | Charles de Gaulle International Airport |  | FR | 203 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 198 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 198 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 193 |
| 33 | Capua Airport |  | IT | 192 |
| 34 | O. R. Tambo International Airport |  | ZA | 191 |
| 35 | Miami International Airport |  | US | 190 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 188 |
| 37 | Vitoria/Foronda Airport |  | ES | 183 |
| 38 | Seattle-Tacoma International Airport |  | US | 181 |
| 39 | Barcelona International Airport |  | ES | 180 |
| 40 | Don Mueang International Airport |  | TH | 179 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 139 | 1h 8m | 706 km | 1,692.3 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 126 | 27m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 117 | 14m | 114 km | 229.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 109 | 24m | 225 km | 422.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 100 | 28m | 304 km | 524.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 86 | 1h 27m | 910 km | 1,349.5 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 74 | 19m | 165 km | 210.5 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 74 | 21m | 99 km | 126.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 73 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 65 | 55m | 546 km | 612.0 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 62 | 1h 12m | 770 km | 823.6 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 59 | 27m | 275 km | 279.6 t |
| 15 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 16 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 58 | 9m | - | - |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 56 | 31m | 369 km | 356.5 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 53 | 46m | 452 km | 413.1 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 51 | 52m | 556 km | 488.9 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 48 | 20m | 250 km | 207.3 t |
| 21 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 47 | 13m | 99 km | 80.6 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 46 | 1h 42m | 1,423 km | 1,128.9 t |
| 24 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 45 | 21m | 244 km | 189.5 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 45 | 20m | 147 km | 113.9 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 40 | 1h 20m | 961 km | 663.0 t |
| 29 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 39 | 26m | 215 km | 144.4 t |
| 30 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK644 | CXK | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-04-11 13:34 UTC | 2026-04-11 14:48 UTC | 1h 13m |
| CXK447 | CXK | Dupage Airport (KDPA) | Wade Airport (56LL) | 2026-04-11 13:44 UTC | 2026-04-11 14:38 UTC | 53m |
| N3030E |  | Burlington/Alamance Regional Airport (KBUY) | Burlington/Alamance Regional Airport (KBUY) | 2026-04-11 13:12 UTC | 2026-04-11 14:34 UTC | 1h 21m |
| TOPCLFE3 | TOP | RAF Topcliffe (EGXZ) | RAF Topcliffe (EGXZ) | 2026-04-11 12:53 UTC | 2026-04-11 14:24 UTC | 1h 31m |
| KENLEY | KEN | London Biggin Hill Airport (EGKB) | London Biggin Hill Airport (EGKB) | 2026-04-11 14:17 UTC | 2026-04-11 14:22 UTC | 5m |
| N67K |  | La Retama Southwest Airport (MM17) | Nuevo Dolores Airport (MM53) | 2026-04-11 13:40 UTC | 2026-04-11 14:20 UTC | 39m |
| WCP250 | WCP | Treasure Coast International Airport (KFPR) | Baggett Airport (FD57) | 2026-04-11 14:17 UTC | 2026-04-11 14:19 UTC | 2m |
| AAL2671 | American Airlines | Salt Lake City International Airport (KSLC) | Evanston-Uinta County Burns Field (KEVW) | 2026-04-11 14:03 UTC | 2026-04-11 14:17 UTC | 13m |
| DKKSY | DKK | Samedan Airport (LSZS) | Bad Ragaz Airport (LSZE) | 2026-04-11 13:00 UTC | 2026-04-11 14:16 UTC | 1h 16m |
|  |  | 94GA (94GA) | 94GA (94GA) | 2026-04-11 14:15 UTC | 2026-04-11 14:16 UTC | 0m |
| WMU83 | WMU | Battle Creek Executive At Kellogg Field (KBTL) | Kirsch Municipal Airport (KIRS) | 2026-04-11 13:25 UTC | 2026-04-11 14:16 UTC | 50m |
| N709LU |  | Brookneal/Campbell County Airport (K0V4) | Brookneal/Campbell County Airport (K0V4) | 2026-04-11 13:54 UTC | 2026-04-11 14:15 UTC | 20m |
|  |  | Fayetteville Municipal Airport (KFYM) | Fayetteville Municipal Airport (KFYM) | 2026-04-11 14:11 UTC | 2026-04-11 14:11 UTC | 0m |
| N433CA |  | French Valley Airport (KF70) | Blanding Municipal Airport (KBDG) | 2026-04-11 11:50 UTC | 2026-04-11 14:10 UTC | 2h 19m |
| N5426F |  | Asheboro Regional Airport (KHBI) | Wayne Executive Jetport Airport (KGWW) | 2026-04-11 13:18 UTC | 2026-04-11 14:10 UTC | 51m |
| CFBQP | CFB | Burlington Executive (CZBA) | Burlington Executive (CZBA) | 2026-04-11 14:04 UTC | 2026-04-11 14:08 UTC | 3m |
| BULET51 | BUL | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-04-11 13:45 UTC | 2026-04-11 14:08 UTC | 23m |
| DIFLD | DIF | Wangerooge Airport (EDWG) | Harle Airport (EDXP) | 2026-04-11 14:02 UTC | 2026-04-11 14:06 UTC | 3m |
| DMUHF | DMU | Hildesheim Airport (EDVM) | Hildesheim Airport (EDVM) | 2026-04-11 13:48 UTC | 2026-04-11 14:06 UTC | 18m |
| ZKIWG | ZKI | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-04-11 13:52 UTC | 2026-04-11 14:06 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
