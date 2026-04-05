# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_13:54:27_UTC-green)

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

**Latest saved flight:** 2026-04-05 13:54:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 13:54:27 UTC

- **17,980** saved flights
- **9,241** unique routes
- **114** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **17,980** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **228,221.9 tonnes** estimated CO2 emissions
- **13,230,257 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 769 |
| 2 | Ryanair | 731 |
| 3 | IndiGo | 523 |
| 4 | EJA | 328 |
| 5 | American Airlines | 325 |
| 6 | Lufthansa | 253 |
| 7 | Southwest Airlines | 248 |
| 8 | ENY | 235 |
| 9 | Vueling | 201 |
| 10 | LATAM Airlines | 191 |
| 11 | AXM | 189 |
| 12 | All Nippon Airways | 161 |
| 13 | QLK | 154 |
| 14 | Delta Air Lines | 151 |
| 15 | LXJ | 150 |
| 16 | AZU | 136 |
| 17 | Swiss International | 135 |
| 18 | VIV | 133 |
| 19 | Japan Airlines | 124 |
| 20 | Alaska Airlines | 123 |
| 21 | easyJet | 119 |
| 22 | Avianca | 117 |
| 23 | United Airlines | 117 |
| 24 | AEE | 115 |
| 25 | AXB | 112 |
| 26 | EJU | 112 |
| 27 | EDV | 108 |
| 28 | WIF | 106 |
| 29 | Cathay Pacific | 104 |
| 30 | BRC | 101 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 13972 |
| 2 | 🇮🇳 IN | 1596 |
| 3 | 🇪🇸 ES | 1494 |
| 4 | 🇦🇺 AU | 1310 |
| 5 | 🇧🇷 BR | 1033 |
| 6 | 🇯🇵 JP | 993 |
| 7 | 🇨🇴 CO | 936 |
| 8 | 🇩🇪 DE | 934 |
| 9 | 🇮🇹 IT | 841 |
| 10 | 🇨🇦 CA | 781 |
| 11 | 🇬🇧 GB | 709 |
| 12 | 🇫🇷 FR | 655 |
| 13 | 🇲🇽 MX | 613 |
| 14 | 🇬🇷 GR | 510 |
| 15 | 🇨🇭 CH | 481 |
| 16 | 🇲🇾 MY | 434 |
| 17 | 🇿🇦 ZA | 401 |
| 18 | 🇳🇿 NZ | 396 |
| 19 | 🇳🇴 NO | 355 |
| 20 | 🇵🇭 PH | 350 |
| 21 | 🇬🇹 GT | 348 |
| 22 | 🇹🇷 TR | 341 |
| 23 | 🇰🇷 KR | 325 |
| 24 | 🇹🇭 TH | 267 |
| 25 | 🇵🇱 PL | 260 |
| 26 | 🇲🇦 MA | 224 |
| 27 | 🇮🇩 ID | 203 |
| 28 | 🇲🇴 MO | 196 |
| 29 | 🇧🇸 BS | 195 |
| 30 | 🇲🇪 ME | 190 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 421 |
| 2 | El Dorado International Airport |  | CO | 357 |
| 3 | Tokyo International Airport |  | JP | 339 |
| 4 | Indira Gandhi International Airport |  | IN | 333 |
| 5 | Denver International Airport |  | US | 327 |
| 6 | La Aurora Airport |  | GT | 243 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 239 |
| 8 | Harry Reid International Airport |  | US | 232 |
| 9 | Frankfurt am Main International Airport |  | DE | 225 |
| 10 | Zurich Airport |  | CH | 220 |
| 11 | Macau International Airport |  | MO | 196 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 191 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 189 |
| 14 | Guaymaral Airport |  | CO | 185 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 182 |
| 16 | Bengaluru International Airport |  | IN | 175 |
| 17 | Chicago O'Hare International Airport |  | US | 173 |
| 18 | Madrid Barajas International Airport |  | ES | 172 |
| 19 | Charlotte/Douglas International Airport |  | US | 167 |
| 20 | Tenerife Norte Airport |  | ES | 161 |
| 21 | Ninoy Aquino International Airport |  | PH | 160 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 159 |
| 23 | Congonhas Airport |  | BR | 155 |
| 24 | Kuala Lumpur International Airport |  | MY | 154 |
| 25 | Daniel K Inouye International Airport |  | US | 145 |
| 26 | Salt Lake City International Airport |  | US | 143 |
| 27 | Vitoria/Foronda Airport |  | ES | 140 |
| 28 | Malpensa International Airport |  | IT | 138 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 138 |
| 30 | Reno/Tahoe International Airport |  | US | 136 |
| 31 | Charles de Gaulle International Airport |  | FR | 136 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 135 |
| 33 | Barcelona International Airport |  | ES | 125 |
| 34 | Miami International Airport |  | US | 124 |
| 35 | Pune Airport |  | IN | 123 |
| 36 | O. R. Tambo International Airport |  | ZA | 123 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 120 |
| 38 | George Bush Intcntl/Houston Airport |  | US | 117 |
| 39 | Seattle-Tacoma International Airport |  | US | 115 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 114 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 85 | 1h 7m | 706 km | 1,034.9 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 79 | 14m | 114 km | 154.9 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 70 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 68 | 24m | 225 km | 263.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 64 | 28m | 304 km | 335.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 54 | 1h 27m | 910 km | 847.4 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 54 | 31m | - | - |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 54 | 27m | 152 km | 141.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 53 | 1h 44m | 1,156 km | 1,057.3 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 50 | 16m | 206 km | 177.8 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 48 | 22m | 99 km | 82.2 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 46 | 27m | 275 km | 218.0 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 45 | 19m | 165 km | 128.0 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 40 | 1h 11m | 770 km | 531.4 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 40 | 30m | 369 km | 254.6 t |
| 16 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 38 | 1h 54m | 1,304 km | 854.9 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 37 | 54m | 546 km | 348.4 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 37 | 52m | 556 km | 354.7 t |
| 19 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 35 | 23m | 252 km | 152.0 t |
| 21 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 34 | 1h 43m | 1,423 km | 834.4 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 33 | 46m | 452 km | 257.2 t |
| 23 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 32 | 58m | 723 km | 398.9 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 32 | 13m | 99 km | 54.9 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 32 | 11m | 127 km | 70.0 t |
| 26 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 30 | 9m | - | - |
| 27 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 29 | 17m | 183 km | 91.4 t |
| 28 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 29 | 20m | 250 km | 125.3 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 27 | 20m | 147 km | 68.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 26 | 1h 23m | 961 km | 431.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DKKSV | DKK | Sisteron - Theze Airport (LFNS) | Mont-Dauphin - St-Crepin Airport (LFNC) | 2026-04-05 10:58 UTC | 2026-04-05 13:54 UTC | 2h 55m |
| N1910R |  | Coban Airport (MGCB) | La Aurora Airport (MGGT) | 2026-04-05 13:23 UTC | 2026-04-05 13:49 UTC | 26m |
| HK3544G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-05 13:14 UTC | 2026-04-05 13:40 UTC | 25m |
| N816CC |  | 76TX (76TX) | Bfs Airport (TE70) | 2026-04-05 13:20 UTC | 2026-04-05 13:33 UTC | 12m |
| N5089G |  | Addington Field (KEKX) | Addington Field (KEKX) | 2026-04-05 13:20 UTC | 2026-04-05 13:32 UTC | 12m |
| CTN344 | CTN | Busevec Velika Glider Airport (LDZB) | Visoko Sport Airfield (LQVI) | 2026-04-05 13:05 UTC | 2026-04-05 13:32 UTC | 26m |
| E7SBA |  | Banja Luka International Airport (LQBK) | Graz Airport (LOWG) | 2026-04-05 12:53 UTC | 2026-04-05 13:30 UTC | 36m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-05 12:41 UTC | 2026-04-05 13:21 UTC | 39m |
| UAE380 | Emirates | Dubai International Airport (OMDB) | Macau International Airport (VMMC) | 2026-04-05 07:07 UTC | 2026-04-05 13:20 UTC | 6h 12m |
| EJC1116 | EJC | El Dorado International Airport (SKBO) | Tolemaida Air Base (SKTI) | 2026-04-05 13:05 UTC | 2026-04-05 13:19 UTC | 14m |
| HBZVU | HBZ | Reichenbach Air Base (LSGR) | Muenster Aero Airport (LSPU) | 2026-04-05 12:42 UTC | 2026-04-05 13:19 UTC | 36m |
| BPX213 | BPX | Daytona Beach International Airport (KDAB) | KXFL (KXFL) | 2026-04-05 13:03 UTC | 2026-04-05 13:18 UTC | 15m |
| AXM6046 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-05 12:59 UTC | 2026-04-05 13:17 UTC | 18m |
| AAL2475 | American Airlines | Charlotte/Douglas International Airport (KCLT) | St Louis Lambert International Airport (KSTL) | 2026-04-05 11:39 UTC | 2026-04-05 13:14 UTC | 1h 34m |
| VIV7332 | VIV | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 2026-04-05 12:10 UTC | 2026-04-05 13:11 UTC | 1h 1m |
| RYR2428 | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Visoko Sport Airfield (LQVI) | 2026-04-05 12:16 UTC | 2026-04-05 13:11 UTC | 55m |
| FD456 |  | Toowoomba Airport (YTWB) | Dalby Airport (YDAY) | 2026-04-05 12:52 UTC | 2026-04-05 13:06 UTC | 14m |
| LAE2524 | LAE | El Dorado International Airport (SKBO) | Los Angeles International Airport (KLAX) | 2026-04-05 03:07 UTC | 2026-04-05 13:05 UTC | 9h 58m |
| VIV5030 | VIV | General Abelardo L. Rodriguez International Airport (MMTJ) | Atizapan De Zaragoza Airport (MMJC) | 2026-04-05 08:42 UTC | 2026-04-05 13:05 UTC | 4h 23m |
| TCAFM | TCA | Balikesir Korfez Airport (LTFD) | Adnan Menderes International Airport (LTBJ) | 2026-04-05 12:46 UTC | 2026-04-05 13:05 UTC | 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
