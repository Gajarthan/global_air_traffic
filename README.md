# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_10:10:33_UTC-green)

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

**Latest saved flight:** 2026-04-17 10:10:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-17 10:10:33 UTC

- **38,746** saved flights
- **16,654** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **38,746** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **468,198.5 tonnes** estimated CO2 emissions
- **27,141,944 km** total distance flown
- **840 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1622 |
| 2 | SkyWest Airlines | 1511 |
| 3 | IndiGo | 957 |
| 4 | EJA | 667 |
| 5 | American Airlines | 646 |
| 6 | Southwest Airlines | 534 |
| 7 | ENY | 500 |
| 8 | AXM | 410 |
| 9 | Vueling | 390 |
| 10 | LATAM Airlines | 386 |
| 11 | Lufthansa | 385 |
| 12 | All Nippon Airways | 348 |
| 13 | AZU | 343 |
| 14 | QLK | 327 |
| 15 | Delta Air Lines | 326 |
| 16 | LXJ | 309 |
| 17 | WIF | 296 |
| 18 | Swiss International | 293 |
| 19 | AEE | 258 |
| 20 | Alaska Airlines | 258 |
| 21 | easyJet | 253 |
| 22 | EJU | 251 |
| 23 | VIV | 245 |
| 24 | Japan Airlines | 237 |
| 25 | Air France | 217 |
| 26 | EDV | 212 |
| 27 | United Airlines | 211 |
| 28 | AIQ | 201 |
| 29 | GLO | 200 |
| 30 | JetBlue | 199 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 30453 |
| 2 | 🇮🇳 IN | 2928 |
| 3 | 🇪🇸 ES | 2880 |
| 4 | 🇦🇺 AU | 2777 |
| 5 | 🇧🇷 BR | 2265 |
| 6 | 🇯🇵 JP | 2112 |
| 7 | 🇮🇹 IT | 2034 |
| 8 | 🇩🇪 DE | 1972 |
| 9 | 🇨🇦 CA | 1905 |
| 10 | 🇨🇴 CO | 1899 |
| 11 | 🇬🇧 GB | 1587 |
| 12 | 🇫🇷 FR | 1464 |
| 13 | 🇲🇽 MX | 1217 |
| 14 | 🇬🇷 GR | 1171 |
| 15 | 🇨🇭 CH | 1061 |
| 16 | 🇲🇾 MY | 993 |
| 17 | 🇳🇴 NO | 950 |
| 18 | 🇳🇿 NZ | 809 |
| 19 | 🇿🇦 ZA | 805 |
| 20 | 🇵🇭 PH | 718 |
| 21 | 🇹🇭 TH | 711 |
| 22 | 🇹🇷 TR | 690 |
| 23 | 🇬🇹 GT | 654 |
| 24 | 🇰🇷 KR | 641 |
| 25 | 🇵🇱 PL | 603 |
| 26 | 🇲🇦 MA | 481 |
| 27 | 🇳🇱 NL | 390 |
| 28 | 🇲🇪 ME | 384 |
| 29 | 🇧🇸 BS | 373 |
| 30 | 🇮🇩 ID | 361 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 902 |
| 2 | Tokyo International Airport |  | JP | 721 |
| 3 | El Dorado International Airport |  | CO | 670 |
| 4 | Denver International Airport |  | US | 648 |
| 5 | Indira Gandhi International Airport |  | IN | 632 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 581 |
| 7 | Harry Reid International Airport |  | US | 507 |
| 8 | Guaymaral Airport |  | CO | 494 |
| 9 | La Aurora Airport |  | GT | 481 |
| 10 | Zurich Airport |  | CH | 468 |
| 11 | Kuala Lumpur International Airport |  | MY | 389 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 383 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 380 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 378 |
| 15 | Chicago O'Hare International Airport |  | US | 373 |
| 16 | Macau International Airport |  | MO | 355 |
| 17 | Madrid Barajas International Airport |  | ES | 352 |
| 18 | Tenerife Norte Airport |  | ES | 349 |
| 19 | Frankfurt am Main International Airport |  | DE | 347 |
| 20 | Charlotte/Douglas International Airport |  | US | 343 |
| 21 | Bengaluru International Airport |  | IN | 338 |
| 22 | Congonhas Airport |  | BR | 334 |
| 23 | Ninoy Aquino International Airport |  | PH | 333 |
| 24 | Malpensa International Airport |  | IT | 313 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 301 |
| 26 | Salt Lake City International Airport |  | US | 293 |
| 27 | Daniel K Inouye International Airport |  | US | 288 |
| 28 | Charles de Gaulle International Airport |  | FR | 284 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 280 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 271 |
| 31 | Vitoria/Foronda Airport |  | ES | 264 |
| 32 | Capua Airport |  | IT | 262 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 258 |
| 34 | O. R. Tambo International Airport |  | ZA | 257 |
| 35 | Reno/Tahoe International Airport |  | US | 257 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 252 |
| 37 | Barcelona International Airport |  | ES | 251 |
| 38 | Don Mueang International Airport |  | TH | 239 |
| 39 | Viracopos International Airport |  | BR | 236 |
| 40 | Seattle-Tacoma International Airport |  | US | 233 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 197 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 181 | 1h 8m | 706 km | 2,203.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 157 | 14m | 114 km | 307.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 141 | 24m | 225 km | 547.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 114 | 28m | 304 km | 597.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 111 | 1h 27m | 910 km | 1,741.8 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 103 | 19m | 165 km | 293.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 99 | 31m | - | - |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 98 | 21m | 244 km | 412.7 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 95 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 89 | 26m | 275 km | 421.7 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 86 | 54m | 546 km | 809.7 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 82 | 21m | 99 km | 140.5 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 79 | 1h 11m | 770 km | 1,049.5 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 76 | 45m | 452 km | 592.3 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 71 | 31m | 369 km | 451.9 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 62 | 20m | 147 km | 156.9 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 61 | 52m | 556 km | 584.7 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 59 | 1h 41m | 1,423 km | 1,448.0 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 59 | 13m | 99 km | 101.2 t |
| 24 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 25 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 57 | 26m | 215 km | 211.1 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 56 | 16m | 162 km | 157.0 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 56 | 13m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 55 | 1h 53m | 1,304 km | 1,237.4 t |
| 30 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BNOB | BNO | Bodø Airport (ENBO) | Røst Airport (ENRS) | 2026-04-17 09:57 UTC | 2026-04-17 10:10 UTC | 13m |
| ABY684 | ABY | Sharjah International Airport (OMSJ) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-17 04:39 UTC | 2026-04-17 10:02 UTC | 5h 22m |
| LIFTR71 | LIF | Wunstorf Airport (ETNW) | Wunstorf Airport (ETNW) | 2026-04-17 09:42 UTC | 2026-04-17 09:55 UTC | 12m |
| PSJJA | PSJ | Limeira Airport (SDYM) | Campo Fontenelle Airport (SBYS) | 2026-04-17 09:30 UTC | 2026-04-17 09:40 UTC | 10m |
| RYR280W | Ryanair | Gdańsk Lech Wałęsa Airport (EPGD) | Gdańsk Lech Wałęsa Airport (EPGD) | 2026-04-17 04:05 UTC | 2026-04-17 09:39 UTC | 5h 33m |
| IHACF | IHA | LIVD (LIVD) | LIVD (LIVD) | 2026-04-17 09:12 UTC | 2026-04-17 09:35 UTC | 23m |
| RYR2KK | Ryanair | Pisa / San Giusto - Galileo Galilei International Airport (LIRP) | Eindhoven Airport (EHEH) | 2026-04-17 08:07 UTC | 2026-04-17 09:35 UTC | 1h 27m |
| NSZ38K | NSZ | Lulea Airport (ESPA) | Stockholm-Arlanda Airport (ESSA) | 2026-04-17 08:23 UTC | 2026-04-17 09:31 UTC | 1h 8m |
| IBB27XK | IBB | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 2026-04-17 09:20 UTC | 2026-04-17 09:30 UTC | 10m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Bringeland Airport (ENBL) | 2026-04-17 09:08 UTC | 2026-04-17 09:30 UTC | 21m |
| NHZ31 | NHZ | Blackpool International Airport (EGNH) | RAF Woodvale (EGOW) | 2026-04-17 09:17 UTC | 2026-04-17 09:30 UTC | 12m |
| N452JG |  | Schwabisch Hall-Weckrieden Airport (EDTX) | Schwabisch Hall-Weckrieden Airport (EDTX) | 2026-04-17 09:23 UTC | 2026-04-17 09:27 UTC | 4m |
| AFR28UD | Air France | Charles de Gaulle International Airport (LFPG) | Geneva Cointrin International Airport (LSGG) | 2026-04-17 08:36 UTC | 2026-04-17 09:26 UTC | 50m |
| LIFTR71 | LIF | Wunstorf Airport (ETNW) | Wunstorf Airport (ETNW) | 2026-04-17 07:15 UTC | 2026-04-17 09:26 UTC | 2h 11m |
| TAY1MN | TAY | Lisbon Portela Airport (LPPT) | Mohammed V International Airport (GMMN) | 2026-04-17 08:33 UTC | 2026-04-17 09:23 UTC | 49m |
| SWR7AK | Swiss International | Nice-Cote d'Azur Airport (LFMN) | Zurich Airport (LSZH) | 2026-04-17 08:26 UTC | 2026-04-17 09:23 UTC | 56m |
| IGO502F | IndiGo | Indira Gandhi International Airport (VIDP) | Ambala Air Force Station (VIAM) | 2026-04-17 08:56 UTC | 2026-04-17 09:21 UTC | 25m |
| UAE9846 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-04-17 03:07 UTC | 2026-04-17 09:21 UTC | 6h 14m |
| NAY31XL | NAY | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 2026-04-17 09:08 UTC | 2026-04-17 09:21 UTC | 12m |
| AEE253 | AEE | Mytilene International Airport (LGMT) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-17 08:23 UTC | 2026-04-17 09:21 UTC | 57m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
