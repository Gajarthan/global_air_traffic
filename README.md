# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_07:59:37_UTC-green)

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

**Latest saved flight:** 2026-04-05 07:59:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 07:59:37 UTC

- **17,455** saved flights
- **9,081** unique routes
- **114** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **17,455** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **219,361.9 tonnes** estimated CO2 emissions
- **12,716,634 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 769 |
| 2 | Ryanair | 699 |
| 3 | IndiGo | 496 |
| 4 | EJA | 328 |
| 5 | American Airlines | 322 |
| 6 | Southwest Airlines | 247 |
| 7 | Lufthansa | 246 |
| 8 | ENY | 234 |
| 9 | Vueling | 195 |
| 10 | LATAM Airlines | 184 |
| 11 | AXM | 171 |
| 12 | QLK | 152 |
| 13 | All Nippon Airways | 150 |
| 14 | Delta Air Lines | 150 |
| 15 | LXJ | 149 |
| 16 | AZU | 131 |
| 17 | VIV | 131 |
| 18 | Swiss International | 126 |
| 19 | Alaska Airlines | 123 |
| 20 | Japan Airlines | 117 |
| 21 | United Airlines | 116 |
| 22 | Avianca | 113 |
| 23 | EJU | 110 |
| 24 | AEE | 108 |
| 25 | EDV | 108 |
| 26 | easyJet | 107 |
| 27 | AXB | 106 |
| 28 | WIF | 102 |
| 29 | BRC | 101 |
| 30 | Cathay Pacific | 99 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 13903 |
| 2 | 🇮🇳 IN | 1513 |
| 3 | 🇪🇸 ES | 1432 |
| 4 | 🇦🇺 AU | 1288 |
| 5 | 🇧🇷 BR | 1000 |
| 6 | 🇯🇵 JP | 928 |
| 7 | 🇨🇴 CO | 905 |
| 8 | 🇩🇪 DE | 899 |
| 9 | 🇮🇹 IT | 799 |
| 10 | 🇨🇦 CA | 780 |
| 11 | 🇬🇧 GB | 665 |
| 12 | 🇫🇷 FR | 619 |
| 13 | 🇲🇽 MX | 608 |
| 14 | 🇬🇷 GR | 471 |
| 15 | 🇨🇭 CH | 450 |
| 16 | 🇳🇿 NZ | 394 |
| 17 | 🇲🇾 MY | 392 |
| 18 | 🇿🇦 ZA | 359 |
| 19 | 🇳🇴 NO | 341 |
| 20 | 🇵🇭 PH | 340 |
| 21 | 🇬🇹 GT | 337 |
| 22 | 🇹🇷 TR | 319 |
| 23 | 🇰🇷 KR | 309 |
| 24 | 🇹🇭 TH | 246 |
| 25 | 🇵🇱 PL | 240 |
| 26 | 🇲🇦 MA | 211 |
| 27 | 🇮🇩 ID | 194 |
| 28 | 🇧🇸 BS | 191 |
| 29 | 🇲🇴 MO | 183 |
| 30 | 🇲🇪 ME | 177 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 419 |
| 2 | El Dorado International Airport |  | CO | 343 |
| 3 | Denver International Airport |  | US | 327 |
| 4 | Tokyo International Airport |  | JP | 320 |
| 5 | Indira Gandhi International Airport |  | IN | 316 |
| 6 | La Aurora Airport |  | GT | 237 |
| 7 | Harry Reid International Airport |  | US | 232 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 221 |
| 9 | Frankfurt am Main International Airport |  | DE | 219 |
| 10 | Zurich Airport |  | CH | 207 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 189 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 189 |
| 13 | Macau International Airport |  | MO | 183 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 182 |
| 15 | Guaymaral Airport |  | CO | 182 |
| 16 | Chicago O'Hare International Airport |  | US | 172 |
| 17 | Bengaluru International Airport |  | IN | 169 |
| 18 | Charlotte/Douglas International Airport |  | US | 165 |
| 19 | Madrid Barajas International Airport |  | ES | 165 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 157 |
| 21 | Ninoy Aquino International Airport |  | PH | 155 |
| 22 | Congonhas Airport |  | BR | 154 |
| 23 | Tenerife Norte Airport |  | ES | 150 |
| 24 | Daniel K Inouye International Airport |  | US | 144 |
| 25 | Salt Lake City International Airport |  | US | 142 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 137 |
| 27 | Kuala Lumpur International Airport |  | MY | 136 |
| 28 | Reno/Tahoe International Airport |  | US | 135 |
| 29 | Malpensa International Airport |  | IT | 134 |
| 30 | Vitoria/Foronda Airport |  | ES | 131 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 129 |
| 32 | Charles de Gaulle International Airport |  | FR | 124 |
| 33 | Miami International Airport |  | US | 123 |
| 34 | Barcelona International Airport |  | ES | 122 |
| 35 | George Bush Intcntl/Houston Airport |  | US | 117 |
| 36 | Pune Airport |  | IN | 116 |
| 37 | Seattle-Tacoma International Airport |  | US | 114 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 112 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 111 |
| 40 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 110 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 79 | 1h 8m | 706 km | 961.8 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 79 | 14m | 114 km | 154.9 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 69 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 67 | 24m | 225 km | 259.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 60 | 29m | 304 km | 314.5 t |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 53 | 27m | 152 km | 138.5 t |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 51 | 1h 45m | 1,156 km | 1,017.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 51 | 31m | - | - |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 50 | 1h 27m | 910 km | 784.6 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 49 | 16m | 206 km | 174.2 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 46 | 22m | 99 km | 78.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 43 | 28m | 275 km | 203.8 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 39 | 19m | 165 km | 110.9 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 38 | 1h 11m | 770 km | 504.8 t |
| 15 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 38 | 1h 54m | 1,304 km | 854.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 37 | 30m | 369 km | 235.5 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 37 | 52m | 556 km | 354.7 t |
| 18 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 35 | 54m | 546 km | 329.5 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 33 | 1h 43m | 1,423 km | 809.9 t |
| 21 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 31 | 23m | 252 km | 134.6 t |
| 22 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 31 | 58m | 723 km | 386.5 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 30 | 46m | 452 km | 233.8 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 30 | 13m | 99 km | 51.4 t |
| 25 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 30 | 9m | - | - |
| 26 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 29 | 11m | 127 km | 63.5 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 27 | 20m | 147 km | 68.3 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 26 | 1h 23m | 961 km | 431.0 t |
| 29 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 25 | 16m | 183 km | 78.8 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 24 | 12m | 15 km | 6.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DRAGO74 | DRA | Sallanches Airport (LFHZ) | Sallanches Airport (LFHZ) | 2026-04-05 07:36 UTC | 2026-04-05 07:59 UTC | 23m |
| OEFDN | OEF | Rothenburg o. d. T. Airport (EDFR) | Rothenburg o. d. T. Airport (EDFR) | 2026-04-05 07:31 UTC | 2026-04-05 07:55 UTC | 24m |
| AUA205 | Austrian Airlines | Vienna International Airport (LOWW) | Frankfurt am Main International Airport (EDDF) | 2026-04-05 06:53 UTC | 2026-04-05 07:54 UTC | 1h 1m |
| CFG1RT | CFG | Munich International Airport (EDDM) | Frankfurt am Main International Airport (EDDF) | 2026-04-05 07:18 UTC | 2026-04-05 07:53 UTC | 34m |
| TRP7 | TRP | St Mary's County Regional Airport (K2W6) | Ronald Reagan Washington Ntl Airport (KDCA) | 2026-04-05 07:28 UTC | 2026-04-05 07:48 UTC | 20m |
| HBXDI | HBX | Courchevel Airport (LFLJ) | Courchevel Airport (LFLJ) | 2026-04-05 06:24 UTC | 2026-04-05 07:36 UTC | 1h 12m |
| AXM5305 | AXM | Kota Kinabalu International Airport (WBKK) | Seletar Airport (WSSL) | 2026-04-05 05:32 UTC | 2026-04-05 07:24 UTC | 1h 51m |
| QLK11D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Orange Airport (YORG) | 2026-04-05 06:56 UTC | 2026-04-05 07:21 UTC | 24m |
| SAS1641 | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Hamburg Airport (EDDH) | 2026-04-05 06:41 UTC | 2026-04-05 07:17 UTC | 35m |
| STW135 | STW | Antalya International Airport (LTAI) | Smolensk North Airport (XUBS) | 2026-04-05 04:28 UTC | 2026-04-05 07:16 UTC | 2h 48m |
| ANA1622 | All Nippon Airways | Naha Airport (ROAH) | Takamatsu Airport (RJOT) | 2026-04-05 05:56 UTC | 2026-04-05 07:13 UTC | 1h 16m |
| DLH491 | Lufthansa | Seattle-Tacoma International Airport (KSEA) | Reichelsheim Airport (EDFB) | 2026-04-04 21:29 UTC | 2026-04-05 07:09 UTC | 9h 40m |
| DLH4W | Lufthansa | Charlotte/Douglas International Airport (KCLT) | Dinkelsbuhl-Sinbronn Airport (EDND) | 2026-04-04 23:10 UTC | 2026-04-05 07:09 UTC | 7h 59m |
| AM222 |  | Sydney Kingsford Smith International Airport (YSSY) | Wellington Airport (YWEL) | 2026-04-05 06:34 UTC | 2026-04-05 07:08 UTC | 33m |
| DLH753 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Giebelstadt Airport (EDQG) | 2026-04-04 11:32 UTC | 2026-04-05 07:07 UTC | 19h 35m |
| RYR721U | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Gioia Del Colle Airport (LIBV) | 2026-04-05 06:03 UTC | 2026-04-05 07:06 UTC | 1h 3m |
| POLICER | POL | LIVD (LIVD) | Innsbruck Airport (LOWI) | 2026-04-05 06:55 UTC | 2026-04-05 07:06 UTC | 10m |
| SNJ95 | SNJ | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 2026-04-05 05:55 UTC | 2026-04-05 07:05 UTC | 1h 9m |
| HSEFS | HSE | Bang Pra Airport (VTBT) | Bang Pra Airport (VTBT) | 2026-04-05 05:58 UTC | 2026-04-05 07:05 UTC | 1h 7m |
| VLG59SX | Vueling | Paris-Orly Airport (LFPO) | Castellón De La Plana Airport (LECN) | 2026-04-05 05:36 UTC | 2026-04-05 06:59 UTC | 1h 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
