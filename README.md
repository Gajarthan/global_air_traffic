# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_10:56:01_UTC-green)

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

**Latest saved flight:** 2026-04-12 10:56:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-12 10:56:01 UTC

- **30,287** saved flights
- **13,862** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **30,287** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **371,514.8 tonnes** estimated CO2 emissions
- **21,537,091 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1247 |
| 2 | SkyWest Airlines | 1230 |
| 3 | IndiGo | 793 |
| 4 | American Airlines | 524 |
| 5 | EJA | 523 |
| 6 | Southwest Airlines | 436 |
| 7 | ENY | 408 |
| 8 | Lufthansa | 364 |
| 9 | AXM | 330 |
| 10 | Vueling | 311 |
| 11 | LATAM Airlines | 295 |
| 12 | All Nippon Airways | 284 |
| 13 | AZU | 262 |
| 14 | QLK | 259 |
| 15 | Delta Air Lines | 247 |
| 16 | LXJ | 240 |
| 17 | Swiss International | 221 |
| 18 | Alaska Airlines | 201 |
| 19 | easyJet | 200 |
| 20 | EJU | 197 |
| 21 | Japan Airlines | 197 |
| 22 | VIV | 196 |
| 23 | AEE | 192 |
| 24 | WIF | 190 |
| 25 | United Airlines | 179 |
| 26 | EDV | 178 |
| 27 | Avianca | 167 |
| 28 | AIQ | 160 |
| 29 | GLO | 160 |
| 30 | JetBlue | 159 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 23815 |
| 2 | 🇮🇳 IN | 2428 |
| 3 | 🇪🇸 ES | 2245 |
| 4 | 🇦🇺 AU | 2164 |
| 5 | 🇧🇷 BR | 1733 |
| 6 | 🇯🇵 JP | 1702 |
| 7 | 🇮🇹 IT | 1563 |
| 8 | 🇩🇪 DE | 1520 |
| 9 | 🇨🇴 CO | 1518 |
| 10 | 🇨🇦 CA | 1478 |
| 11 | 🇬🇧 GB | 1225 |
| 12 | 🇫🇷 FR | 1111 |
| 13 | 🇲🇽 MX | 975 |
| 14 | 🇬🇷 GR | 865 |
| 15 | 🇨🇭 CH | 848 |
| 16 | 🇲🇾 MY | 789 |
| 17 | 🇳🇿 NZ | 665 |
| 18 | 🇳🇴 NO | 641 |
| 19 | 🇿🇦 ZA | 624 |
| 20 | 🇵🇭 PH | 571 |
| 21 | 🇹🇭 TH | 563 |
| 22 | 🇬🇹 GT | 553 |
| 23 | 🇹🇷 TR | 550 |
| 24 | 🇰🇷 KR | 527 |
| 25 | 🇵🇱 PL | 457 |
| 26 | 🇲🇦 MA | 383 |
| 27 | 🇧🇸 BS | 318 |
| 28 | 🇲🇪 ME | 305 |
| 29 | 🇳🇱 NL | 291 |
| 30 | 🇲🇴 MO | 288 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 720 |
| 2 | Tokyo International Airport |  | JP | 571 |
| 3 | El Dorado International Airport |  | CO | 541 |
| 4 | Denver International Airport |  | US | 512 |
| 5 | Indira Gandhi International Airport |  | IN | 511 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 424 |
| 7 | La Aurora Airport |  | GT | 394 |
| 8 | Harry Reid International Airport |  | US | 392 |
| 9 | Zurich Airport |  | CH | 363 |
| 10 | Guaymaral Airport |  | CO | 359 |
| 11 | Chicago O'Hare International Airport |  | US | 314 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 313 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 311 |
| 14 | Frankfurt am Main International Airport |  | DE | 306 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 300 |
| 16 | Kuala Lumpur International Airport |  | MY | 298 |
| 17 | Macau International Airport |  | MO | 288 |
| 18 | Bengaluru International Airport |  | IN | 274 |
| 19 | Charlotte/Douglas International Airport |  | US | 271 |
| 20 | Tenerife Norte Airport |  | ES | 266 |
| 21 | Madrid Barajas International Airport |  | ES | 265 |
| 22 | Ninoy Aquino International Airport |  | PH | 262 |
| 23 | Congonhas Airport |  | BR | 253 |
| 24 | Malpensa International Airport |  | IT | 242 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 234 |
| 26 | Daniel K Inouye International Airport |  | US | 231 |
| 27 | Reno/Tahoe International Airport |  | US | 230 |
| 28 | Salt Lake City International Airport |  | US | 230 |
| 29 | Charles de Gaulle International Airport |  | FR | 216 |
| 30 | Capua Airport |  | IT | 209 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 209 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 207 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 206 |
| 34 | Miami International Airport |  | US | 202 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 201 |
| 36 | O. R. Tambo International Airport |  | ZA | 199 |
| 37 | Vitoria/Foronda Airport |  | ES | 197 |
| 38 | Seattle-Tacoma International Airport |  | US | 192 |
| 39 | Barcelona International Airport |  | ES | 192 |
| 40 | Don Mueang International Airport |  | TH | 190 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 145 | 1h 8m | 706 km | 1,765.4 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 139 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 126 | 14m | 114 km | 247.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 112 | 24m | 225 km | 434.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 103 | 28m | 304 km | 540.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 90 | 1h 27m | 910 km | 1,412.3 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 78 | 19m | 165 km | 221.9 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 76 | 21m | 99 km | 130.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 75 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 69 | 55m | 546 km | 649.6 t |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 12 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 65 | 1h 12m | 770 km | 863.5 t |
| 14 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 65 | 9m | - | - |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 64 | 27m | 275 km | 303.3 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 60 | 31m | 369 km | 381.9 t |
| 17 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 57 | 45m | 452 km | 444.2 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 57 | 52m | 556 km | 546.4 t |
| 20 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 54 | 21m | 244 km | 227.4 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 51 | 20m | 250 km | 220.3 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 50 | 13m | 99 km | 85.7 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 47 | 20m | 147 km | 118.9 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 46 | 1h 42m | 1,423 km | 1,128.9 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 42 | 1h 19m | 961 km | 696.2 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 41 | 12m | 15 km | 10.8 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 41 | 14m | 154 km | 108.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CSC9606 | CSC | Melsbroek Air Base (EBMB) | Borisoglebskoye Airport (UWKG) | 2026-04-12 07:10 UTC | 2026-04-12 10:56 UTC | 3h 45m |
| N340GK |  | Searchlight Airport (K1L3) | Harry Reid International Airport (KLAS) | 2026-04-12 10:10 UTC | 2026-04-12 10:51 UTC | 40m |
| JA07DR |  | Shimofusa Airport (RJTL) | Shimofusa Airport (RJTL) | 2026-04-12 09:02 UTC | 2026-04-12 10:39 UTC | 1h 37m |
| CPA805 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-04-11 20:01 UTC | 2026-04-12 10:28 UTC | 14h 26m |
| JST17 | JST | Melbourne International Airport (YMML) | Perth International Airport (YPPH) | 2026-04-12 05:24 UTC | 2026-04-12 10:26 UTC | 5h 2m |
| RYR6GM | Ryanair | Memmingen Allgau Airport (EDJA) | Visoko Sport Airfield (LQVI) | 2026-04-12 09:22 UTC | 2026-04-12 10:19 UTC | 57m |
| RUK1711 | RUK | Manchester Airport (EGCC) | Ifrane Airport (GMFI) | 2026-04-12 07:27 UTC | 2026-04-12 10:19 UTC | 2h 52m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-11 19:14 UTC | 2026-04-12 10:15 UTC | 15h 1m |
| AZE514 | AZE | Palma De Mallorca Airport (LEPA) | Dusseldorf International Airport (EDDL) | 2026-04-12 08:14 UTC | 2026-04-12 10:12 UTC | 1h 57m |
| BBC437 | BBC | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-04-12 09:39 UTC | 2026-04-12 10:08 UTC | 28m |
| AXM5194 | AXM | Kuala Lumpur International Airport (WMKK) | Telupid Airport (WBKE) | 2026-04-12 07:55 UTC | 2026-04-12 10:08 UTC | 2h 12m |
| EZY86ZC | easyJet | London Gatwick Airport (EGKK) | Tivat Airport (LYTV) | 2026-04-12 07:59 UTC | 2026-04-12 10:07 UTC | 2h 8m |
| RYR59PZ | Ryanair | Dublin Airport (EIDW) | Calaf-Sallavinera Airport (LECF) | 2026-04-12 08:06 UTC | 2026-04-12 10:04 UTC | 1h 58m |
| RYR61NG | Ryanair | Barcelona International Airport (LEBL) | Lusse Airport (EDOJ) | 2026-04-12 08:00 UTC | 2026-04-12 10:04 UTC | 2h 4m |
| IGO295C | IndiGo | Indira Gandhi International Airport (VIDP) | VIBN (VIBN) | 2026-04-12 09:18 UTC | 2026-04-12 10:04 UTC | 45m |
| ICE30R | ICE | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 2026-04-12 09:41 UTC | 2026-04-12 10:03 UTC | 21m |
| AXM6130 | AXM | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 2026-04-12 09:49 UTC | 2026-04-12 10:03 UTC | 13m |
| ANA407 | All Nippon Airways | Tokyo International Airport (RJTT) | Yamagata Airport (RJSC) | 2026-04-12 09:35 UTC | 2026-04-12 10:02 UTC | 27m |
| NOZ372 | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Bardufoss Airport (ENDU) | 2026-04-12 08:43 UTC | 2026-04-12 10:02 UTC | 1h 19m |
| EWG9JL | EWG | Dusseldorf International Airport (EDDL) | Vlora Internationa Airport (LAVL) | 2026-04-12 08:04 UTC | 2026-04-12 10:02 UTC | 1h 58m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
