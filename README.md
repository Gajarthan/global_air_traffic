# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_14:47:04_UTC-green)

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

**Latest saved flight:** 2026-04-06 14:47:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-06 14:47:04 UTC

- **20,013** saved flights
- **10,030** unique routes
- **116** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **20,013** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **252,004.2 tonnes** estimated CO2 emissions
- **14,608,938 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 856 |
| 2 | Ryanair | 828 |
| 3 | IndiGo | 573 |
| 4 | American Airlines | 380 |
| 5 | EJA | 368 |
| 6 | Southwest Airlines | 283 |
| 7 | ENY | 267 |
| 8 | Lufthansa | 263 |
| 9 | Vueling | 218 |
| 10 | LATAM Airlines | 212 |
| 11 | AXM | 197 |
| 12 | Delta Air Lines | 177 |
| 13 | All Nippon Airways | 176 |
| 14 | LXJ | 172 |
| 15 | QLK | 164 |
| 16 | AZU | 154 |
| 17 | VIV | 151 |
| 18 | Swiss International | 150 |
| 19 | easyJet | 137 |
| 20 | Japan Airlines | 134 |
| 21 | United Airlines | 134 |
| 22 | Alaska Airlines | 132 |
| 23 | Avianca | 131 |
| 24 | EJU | 130 |
| 25 | AEE | 125 |
| 26 | WIF | 121 |
| 27 | EDV | 119 |
| 28 | AXB | 115 |
| 29 | Air France | 110 |
| 30 | Cathay Pacific | 105 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 15531 |
| 2 | 🇮🇳 IN | 1744 |
| 3 | 🇪🇸 ES | 1615 |
| 4 | 🇦🇺 AU | 1407 |
| 5 | 🇧🇷 BR | 1152 |
| 6 | 🇯🇵 JP | 1090 |
| 7 | 🇨🇴 CO | 1088 |
| 8 | 🇩🇪 DE | 1009 |
| 9 | 🇮🇹 IT | 985 |
| 10 | 🇨🇦 CA | 869 |
| 11 | 🇬🇧 GB | 796 |
| 12 | 🇫🇷 FR | 740 |
| 13 | 🇲🇽 MX | 687 |
| 14 | 🇬🇷 GR | 570 |
| 15 | 🇨🇭 CH | 543 |
| 16 | 🇲🇾 MY | 463 |
| 17 | 🇬🇹 GT | 460 |
| 18 | 🇿🇦 ZA | 453 |
| 19 | 🇳🇴 NO | 418 |
| 20 | 🇳🇿 NZ | 416 |
| 21 | 🇹🇷 TR | 393 |
| 22 | 🇵🇭 PH | 380 |
| 23 | 🇰🇷 KR | 351 |
| 24 | 🇹🇭 TH | 306 |
| 25 | 🇵🇱 PL | 289 |
| 26 | 🇲🇦 MA | 249 |
| 27 | 🇧🇸 BS | 220 |
| 28 | 🇮🇩 ID | 214 |
| 29 | 🇲🇪 ME | 210 |
| 30 | 🇳🇱 NL | 204 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 484 |
| 2 | El Dorado International Airport |  | CO | 415 |
| 3 | Tokyo International Airport |  | JP | 377 |
| 4 | Denver International Airport |  | US | 363 |
| 5 | Indira Gandhi International Airport |  | IN | 362 |
| 6 | La Aurora Airport |  | GT | 316 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 268 |
| 8 | Harry Reid International Airport |  | US | 260 |
| 9 | Zurich Airport |  | CH | 244 |
| 10 | Frankfurt am Main International Airport |  | DE | 235 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 217 |
| 12 | Chicago O'Hare International Airport |  | US | 211 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 211 |
| 14 | Guaymaral Airport |  | CO | 211 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 204 |
| 16 | Macau International Airport |  | MO | 200 |
| 17 | Bengaluru International Airport |  | IN | 195 |
| 18 | Charlotte/Douglas International Airport |  | US | 192 |
| 19 | Madrid Barajas International Airport |  | ES | 188 |
| 20 | Tenerife Norte Airport |  | ES | 184 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 181 |
| 22 | Ninoy Aquino International Airport |  | PH | 172 |
| 23 | Congonhas Airport |  | BR | 172 |
| 24 | Kuala Lumpur International Airport |  | MY | 160 |
| 25 | Salt Lake City International Airport |  | US | 157 |
| 26 | Reno/Tahoe International Airport |  | US | 156 |
| 27 | Daniel K Inouye International Airport |  | US | 154 |
| 28 | Malpensa International Airport |  | IT | 151 |
| 29 | Charles de Gaulle International Airport |  | FR | 150 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 150 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 147 |
| 32 | Vitoria/Foronda Airport |  | ES | 145 |
| 33 | O. R. Tambo International Airport |  | ZA | 141 |
| 34 | Miami International Airport |  | US | 140 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 140 |
| 36 | Pune Airport |  | IN | 135 |
| 37 | Barcelona International Airport |  | ES | 135 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 132 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 131 |
| 40 | Seattle-Tacoma International Airport |  | US | 127 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 95 | 1h 8m | 706 km | 1,156.6 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 89 | 14m | 114 km | 174.6 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 77 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 74 | 24m | 225 km | 287.1 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 69 | 28m | 304 km | 361.7 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 60 | 1h 27m | 910 km | 941.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 57 | 1h 43m | 1,156 km | 1,137.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 57 | 31m | - | - |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 55 | 16m | 206 km | 195.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 46 | 19m | 165 km | 130.8 t |
| 14 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 15 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 44 | 23m | 252 km | 191.0 t |
| 16 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 44 | 1h 12m | 770 km | 584.5 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 42 | 55m | 546 km | 395.4 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 41 | 30m | 369 km | 261.0 t |
| 19 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 40 | 10m | - | - |
| 20 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 39 | 4m | - | - |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 39 | 52m | 556 km | 373.8 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 37 | 13m | 99 km | 63.4 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 37 | 20m | 250 km | 159.8 t |
| 25 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 36 | 46m | 452 km | 280.6 t |
| 26 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 27 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 35 | 58m | 723 km | 436.3 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 32 | 12m | 15 km | 8.4 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 31 | 20m | 147 km | 78.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6896H |  | 0IL8 (0IL8) | 95LL (95LL) | 2026-04-06 14:14 UTC | 2026-04-06 14:47 UTC | 32m |
| N821SS |  | Francis S Gabreski Airport (KFOK) | Laguardia Airport (KLGA) | 2026-04-06 14:00 UTC | 2026-04-06 14:46 UTC | 45m |
| N66SC |  | Parker Field (SC47) | Aiken Regional Airport (KAIK) | 2026-04-06 13:38 UTC | 2026-04-06 14:44 UTC | 1h 6m |
| TCF639 | TCF | Melbourne Orlando International Airport (KMLB) | Valkaria Airport (KX59) | 2026-04-06 13:51 UTC | 2026-04-06 14:43 UTC | 51m |
| N773MG |  | Double Eagle Ii Airport (KAEG) | NM74 (NM74) | 2026-04-06 14:26 UTC | 2026-04-06 14:40 UTC | 14m |
| HK5178G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-06 14:21 UTC | 2026-04-06 14:35 UTC | 13m |
| CFLDD | CFL | Calgary International Airport (CYYC) | Saskatoon John G. Diefenbaker International Airport (CYXE) | 2026-04-06 13:42 UTC | 2026-04-06 14:30 UTC | 48m |
| NDU54 | NDU | ND24 (ND24) | ND24 (ND24) | 2026-04-06 14:28 UTC | 2026-04-06 14:28 UTC | 0m |
| N16069 |  | Perot Field/Fort Worth Alliance Airport (KAFW) | Kenneth Copeland Airport (K4T2) | 2026-04-06 13:42 UTC | 2026-04-06 14:28 UTC | 46m |
| SCU59 | SCU | 2OL2 (2OL2) | Cherokee Ranch Airport (OK25) | 2026-04-06 13:53 UTC | 2026-04-06 14:25 UTC | 32m |
| N78183 |  | Addington Field (4TX8) | Allison Farm Airport (XA34) | 2026-04-06 14:07 UTC | 2026-04-06 14:23 UTC | 16m |
| PSATN | PSA | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | Congonhas Airport (SBSP) | 2026-04-06 14:17 UTC | 2026-04-06 14:23 UTC | 6m |
| VJH792 | VJH | Bremen Airport (EDDW) | Sondrio Caiolo Airport (LILO) | 2026-04-06 13:18 UTC | 2026-04-06 14:18 UTC | 1h 0m |
| D0381 |  | Schwabach-Heidenberg Airport (EDPH) | Schwabach-Heidenberg Airport (EDPH) | 2026-04-06 13:26 UTC | 2026-04-06 14:18 UTC | 51m |
| ERU35 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | 42AZ (42AZ) | 2026-04-06 14:00 UTC | 2026-04-06 14:17 UTC | 16m |
| N172JA |  | Hicks Airfield (KT67) | Bridgeport Municipal Airport (KXBP) | 2026-04-06 14:00 UTC | 2026-04-06 14:17 UTC | 17m |
| N831MT |  | Boise Air Trml/Gowen Field (KBOI) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-06 12:50 UTC | 2026-04-06 14:17 UTC | 1h 26m |
| N72NG |  | Montgomery-Gibbs Executive Airport (KMYF) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-04-06 13:45 UTC | 2026-04-06 14:14 UTC | 28m |
| N542CJ |  | Mountain Hide-Away Airport (3PS4) | Lazy J Aerodrome (00WV) | 2026-04-06 13:45 UTC | 2026-04-06 14:14 UTC | 28m |
| CXK475 | CXK | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-04-06 12:36 UTC | 2026-04-06 14:13 UTC | 1h 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
