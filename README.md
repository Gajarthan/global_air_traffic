# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_20:25:34_UTC-green)

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

**Latest saved flight:** 2026-04-12 20:25:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-12 20:25:34 UTC

- **31,264** saved flights
- **14,209** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **31,264** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **383,847.3 tonnes** estimated CO2 emissions
- **22,252,015 km** total distance flown
- **849 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1306 |
| 2 | SkyWest Airlines | 1269 |
| 3 | IndiGo | 804 |
| 4 | American Airlines | 544 |
| 5 | EJA | 543 |
| 6 | Southwest Airlines | 454 |
| 7 | ENY | 423 |
| 8 | Lufthansa | 374 |
| 9 | AXM | 335 |
| 10 | Vueling | 320 |
| 11 | LATAM Airlines | 312 |
| 12 | All Nippon Airways | 287 |
| 13 | AZU | 273 |
| 14 | QLK | 260 |
| 15 | Delta Air Lines | 258 |
| 16 | LXJ | 245 |
| 17 | Swiss International | 232 |
| 18 | easyJet | 209 |
| 19 | Alaska Airlines | 208 |
| 20 | WIF | 206 |
| 21 | EJU | 204 |
| 22 | VIV | 201 |
| 23 | Japan Airlines | 197 |
| 24 | AEE | 196 |
| 25 | United Airlines | 184 |
| 26 | EDV | 183 |
| 27 | Avianca | 170 |
| 28 | Air France | 169 |
| 29 | GLO | 168 |
| 30 | JetBlue | 167 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 24624 |
| 2 | 🇮🇳 IN | 2468 |
| 3 | 🇪🇸 ES | 2332 |
| 4 | 🇦🇺 AU | 2173 |
| 5 | 🇧🇷 BR | 1831 |
| 6 | 🇯🇵 JP | 1713 |
| 7 | 🇮🇹 IT | 1637 |
| 8 | 🇩🇪 DE | 1588 |
| 9 | 🇨🇴 CO | 1567 |
| 10 | 🇨🇦 CA | 1502 |
| 11 | 🇬🇧 GB | 1269 |
| 12 | 🇫🇷 FR | 1156 |
| 13 | 🇲🇽 MX | 1001 |
| 14 | 🇬🇷 GR | 891 |
| 15 | 🇨🇭 CH | 878 |
| 16 | 🇲🇾 MY | 807 |
| 17 | 🇳🇴 NO | 693 |
| 18 | 🇳🇿 NZ | 667 |
| 19 | 🇿🇦 ZA | 646 |
| 20 | 🇬🇹 GT | 578 |
| 21 | 🇹🇷 TR | 576 |
| 22 | 🇵🇭 PH | 575 |
| 23 | 🇹🇭 TH | 569 |
| 24 | 🇰🇷 KR | 531 |
| 25 | 🇵🇱 PL | 477 |
| 26 | 🇲🇦 MA | 403 |
| 27 | 🇧🇸 BS | 329 |
| 28 | 🇲🇪 ME | 312 |
| 29 | 🇳🇱 NL | 300 |
| 30 | 🇮🇩 ID | 296 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 751 |
| 2 | Tokyo International Airport |  | JP | 576 |
| 3 | El Dorado International Airport |  | CO | 555 |
| 4 | Denver International Airport |  | US | 529 |
| 5 | Indira Gandhi International Airport |  | IN | 520 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 436 |
| 7 | La Aurora Airport |  | GT | 417 |
| 8 | Harry Reid International Airport |  | US | 406 |
| 9 | Zurich Airport |  | CH | 385 |
| 10 | Guaymaral Airport |  | CO | 382 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 323 |
| 12 | Chicago O'Hare International Airport |  | US | 323 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 321 |
| 14 | Frankfurt am Main International Airport |  | DE | 316 |
| 15 | Kuala Lumpur International Airport |  | MY | 306 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 302 |
| 17 | Macau International Airport |  | MO | 291 |
| 18 | Charlotte/Douglas International Airport |  | US | 282 |
| 19 | Tenerife Norte Airport |  | ES | 281 |
| 20 | Bengaluru International Airport |  | IN | 281 |
| 21 | Madrid Barajas International Airport |  | ES | 278 |
| 22 | Congonhas Airport |  | BR | 267 |
| 23 | Ninoy Aquino International Airport |  | PH | 264 |
| 24 | Malpensa International Airport |  | IT | 251 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 240 |
| 26 | Reno/Tahoe International Airport |  | US | 239 |
| 27 | Salt Lake City International Airport |  | US | 238 |
| 28 | Daniel K Inouye International Airport |  | US | 237 |
| 29 | Charles de Gaulle International Airport |  | FR | 229 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 222 |
| 31 | John Paul II International Airport Kraków-Balice Airport |  | PL | 216 |
| 32 | Capua Airport |  | IT | 216 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 215 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 211 |
| 35 | O. R. Tambo International Airport |  | ZA | 209 |
| 36 | Miami International Airport |  | US | 208 |
| 37 | Vitoria/Foronda Airport |  | ES | 206 |
| 38 | Seattle-Tacoma International Airport |  | US | 197 |
| 39 | Barcelona International Airport |  | ES | 197 |
| 40 | Don Mueang International Airport |  | TH | 192 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 149 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 145 | 1h 8m | 706 km | 1,765.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 130 | 14m | 114 km | 255.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 112 | 24m | 225 km | 434.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 104 | 28m | 304 km | 545.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 91 | 1h 28m | 910 km | 1,428.0 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 81 | 19m | 165 km | 230.4 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 76 | 21m | 99 km | 130.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 75 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 73 | 9m | - | - |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 71 | 27m | 152 km | 185.5 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 70 | 55m | 546 km | 659.1 t |
| 13 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 66 | 27m | 275 km | 312.7 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 66 | 1h 12m | 770 km | 876.8 t |
| 16 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 60 | 21m | 244 km | 252.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 60 | 31m | 369 km | 381.9 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 19 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 57 | 45m | 452 km | 444.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 54 | 20m | 250 km | 233.2 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 50 | 13m | 99 km | 85.7 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 48 | 20m | 147 km | 121.5 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 48 | 1h 42m | 1,423 km | 1,178.0 t |
| 25 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 44 | 1h 21m | 961 km | 729.3 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 43 | 12m | 15 km | 11.3 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 43 | 14m | 154 km | 113.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N66HC |  | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-04-12 19:30 UTC | 2026-04-12 20:25 UTC | 55m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-04-12 20:02 UTC | 2026-04-12 20:24 UTC | 21m |
| CPA085 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-12 05:10 UTC | 2026-04-12 20:23 UTC | 15h 12m |
| N55264 |  | Lehigh Valley International Airport (KABE) | Lancaster Airport (KLNS) | 2026-04-12 19:42 UTC | 2026-04-12 20:21 UTC | 39m |
| ANA968 | All Nippon Airways | Nagasaki Airport (RJFU) | Tokyo International Airport (RJTT) | 2026-04-12 19:09 UTC | 2026-04-12 20:19 UTC | 1h 10m |
| CXK532 | CXK | Long Island Mac Arthur Airport (KISP) | Westmoreland Airport (49NY) | 2026-04-12 18:38 UTC | 2026-04-12 20:13 UTC | 1h 34m |
| DLH5MR | Lufthansa | Munich International Airport (EDDM) | Frankfurt am Main International Airport (EDDF) | 2026-04-12 19:38 UTC | 2026-04-12 20:09 UTC | 31m |
| N424KT |  | Talkeetna Airport (PATK) | Mc Kinley Country Airport (81AK) | 2026-04-12 19:44 UTC | 2026-04-12 20:09 UTC | 25m |
| ANE88SC | ANE | Madrid Barajas International Airport (LEMD) | Frankfurt am Main International Airport (EDDF) | 2026-04-12 18:05 UTC | 2026-04-12 20:07 UTC | 2h 2m |
| N545GC |  | Lompoc Airport (KLPC) | Lompoc Airport (KLPC) | 2026-04-12 19:24 UTC | 2026-04-12 20:07 UTC | 42m |
| AAL9990 | American Airlines | John F Kennedy International Airport (KJFK) | ETIN (ETIN) | 2026-04-12 12:57 UTC | 2026-04-12 20:04 UTC | 7h 6m |
| AUA279 | Austrian Airlines | Vienna International Airport (LOWW) | Salzgitter-Schaferstuhl Airport (EDVJ) | 2026-04-12 18:42 UTC | 2026-04-12 20:04 UTC | 1h 21m |
| DLH1V | Lufthansa | Vienna International Airport (LOWW) | Ansbach-Petersdorf Airport (EDQF) | 2026-04-12 18:58 UTC | 2026-04-12 20:04 UTC | 1h 6m |
| DLH2LC | Lufthansa | Grazzanise Airport (LIRM) | Ingelfingen-Buhlhof Airport (EDGI) | 2026-04-12 18:28 UTC | 2026-04-12 20:04 UTC | 1h 36m |
| EWG1SP | EWG | Zurich Airport (LSZH) | Attendorn-Finnentrop Airport (EDKU) | 2026-04-12 18:55 UTC | 2026-04-12 20:04 UTC | 1h 9m |
| EWG3PL | EWG | Hamburg Airport (EDDH) | Osnabruck-Atterheide Airport (EDWO) | 2026-04-12 19:14 UTC | 2026-04-12 20:04 UTC | 49m |
| EWG5K | EWG | Zurich Airport (LSZH) | Elz Airport (EDFY) | 2026-04-12 19:01 UTC | 2026-04-12 20:04 UTC | 1h 3m |
| EWG8SY | EWG | Vienna International Airport (LOWW) | Meschede-Schuren Airport (EDKM) | 2026-04-12 18:38 UTC | 2026-04-12 20:04 UTC | 1h 25m |
| KLM53T | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Giesen-Lutzellinden Airport (EDFL) | 2026-04-12 19:06 UTC | 2026-04-12 20:04 UTC | 58m |
| LOT5NG | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Soest/Bad Sassendorf Airport (EDLZ) | 2026-04-12 18:20 UTC | 2026-04-12 20:04 UTC | 1h 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
