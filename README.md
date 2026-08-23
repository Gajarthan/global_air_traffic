# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_14:36:59_UTC-green)

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

**Latest saved flight:** 2026-08-23 14:36:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 14:36:59 UTC

- **228,699** saved flights
- **70,733** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **228,699** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,758,504.8 tonnes** estimated CO2 emissions
- **159,913,321 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9187 |
| 2 | SkyWest Airlines | 8106 |
| 3 | EJA | 4397 |
| 4 | IndiGo | 3873 |
| 5 | American Airlines | 3743 |
| 6 | Southwest Airlines | 3549 |
| 7 | Delta Air Lines | 2925 |
| 8 | ENY | 2792 |
| 9 | LATAM Airlines | 2195 |
| 10 | AZU | 2124 |
| 11 | Vueling | 1943 |
| 12 | Lufthansa | 1870 |
| 13 | WIF | 1803 |
| 14 | LXJ | 1790 |
| 15 | easyJet | 1597 |
| 16 | Swiss International | 1526 |
| 17 | AXM | 1520 |
| 18 | EJU | 1455 |
| 19 | QLK | 1448 |
| 20 | United Airlines | 1447 |
| 21 | Alaska Airlines | 1385 |
| 22 | All Nippon Airways | 1372 |
| 23 | GLO | 1270 |
| 24 | VIV | 1254 |
| 25 | PGT | 1252 |
| 26 | WMT | 1249 |
| 27 | Air France | 1243 |
| 28 | Wizz Air | 1193 |
| 29 | JetBlue | 1142 |
| 30 | AEE | 1140 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 190821 |
| 2 | 🇪🇸 ES | 14686 |
| 3 | 🇧🇷 BR | 13351 |
| 4 | 🇦🇺 AU | 12961 |
| 5 | 🇨🇦 CA | 12626 |
| 6 | 🇮🇹 IT | 12360 |
| 7 | 🇮🇳 IN | 12068 |
| 8 | 🇩🇪 DE | 11259 |
| 9 | 🇬🇧 GB | 10770 |
| 10 | 🇨🇴 CO | 9404 |
| 11 | 🇯🇵 JP | 9312 |
| 12 | 🇫🇷 FR | 9168 |
| 13 | 🇹🇷 TR | 6741 |
| 14 | 🇬🇷 GR | 6720 |
| 15 | 🇲🇽 MX | 6360 |
| 16 | 🇨🇭 CH | 6077 |
| 17 | 🇳🇴 NO | 5623 |
| 18 | 🇲🇾 MY | 4061 |
| 19 | 🇹🇭 TH | 3994 |
| 20 | 🇿🇦 ZA | 3989 |
| 21 | 🇵🇱 PL | 3807 |
| 22 | 🇳🇿 NZ | 3169 |
| 23 | 🇵🇭 PH | 3142 |
| 24 | 🇬🇹 GT | 2875 |
| 25 | 🇰🇷 KR | 2705 |
| 26 | 🇭🇷 HR | 2609 |
| 27 | 🇲🇦 MA | 2317 |
| 28 | 🇲🇪 ME | 2085 |
| 29 | 🇳🇱 NL | 2049 |
| 30 | 🇮🇩 ID | 1976 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4772 |
| 2 | Denver International Airport |  | US | 3714 |
| 3 | Indira Gandhi International Airport |  | IN | 2791 |
| 4 | Tokyo International Airport |  | JP | 2781 |
| 5 | Guaymaral Airport |  | CO | 2648 |
| 6 | Harry Reid International Airport |  | US | 2475 |
| 7 | Zurich Airport |  | CH | 2381 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2336 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2306 |
| 10 | La Aurora Airport |  | GT | 2190 |
| 11 | El Dorado International Airport |  | CO | 2085 |
| 12 | Chicago O'Hare International Airport |  | US | 2071 |
| 13 | Salt Lake City International Airport |  | US | 2010 |
| 14 | Congonhas Airport |  | BR | 1946 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1938 |
| 16 | Frankfurt am Main International Airport |  | DE | 1835 |
| 17 | Madrid Barajas International Airport |  | ES | 1789 |
| 18 | Capua Airport |  | IT | 1780 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1713 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1700 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1649 |
| 22 | Malpensa International Airport |  | IT | 1633 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1612 |
| 24 | Macau International Airport |  | MO | 1596 |
| 25 | Charles de Gaulle International Airport |  | FR | 1584 |
| 26 | Ninoy Aquino International Airport |  | PH | 1508 |
| 27 | Charlotte/Douglas International Airport |  | US | 1494 |
| 28 | Kuala Lumpur International Airport |  | MY | 1471 |
| 29 | Barcelona International Airport |  | ES | 1433 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1385 |
| 31 | Viracopos International Airport |  | BR | 1358 |
| 32 | Enrique Olaya Herrera Airport |  | CO | 1355 |
| 33 | Bengaluru International Airport |  | IN | 1355 |
| 34 | Seattle-Tacoma International Airport |  | US | 1348 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1345 |
| 36 | Don Mueang International Airport |  | TH | 1307 |
| 37 | Calgary International Airport |  | CA | 1299 |
| 38 | Oslo Gardermoen Airport |  | NO | 1269 |
| 39 | Vitoria/Foronda Airport |  | ES | 1247 |
| 40 | O. R. Tambo International Airport |  | ZA | 1238 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1075 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 833 | 21m | 244 km | 3,507.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 575 | 1h 6m | 770 km | 7,638.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 567 | 24m | 225 km | 2,199.7 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 549 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 514 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 350 | 1h 50m | 1,423 km | 8,589.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 316 | 21m | 250 km | 1,364.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 315 | 1h 7m | 706 km | 3,835.1 t |
| 13 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 14 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 310 | 44m | 555 km | 2,968.4 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 305 | 22m | 55 km | 289.9 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 293 | 24m | 218 km | 1,103.8 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 293 | 1h 38m | 1,156 km | 5,845.2 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 285 | 19m | 99 km | 488.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 278 | 27m | 215 km | 1,029.6 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 267 | 1h 14m | 961 km | 4,425.7 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 266 | 12m | - | - |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 261 | 19m | 144 km | 649.2 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 245 | 1h 50m | 1,304 km | 5,511.9 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 241 | 15m | 154 km | 638.6 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 239 | 28m | 152 km | 624.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N961LA |  | Long Beach (Daugherty Field) Airport (KLGB) | Fullerton Municipal Airport (KFUL) | 2026-08-23 13:11 UTC | 2026-08-23 14:36 UTC | 1h 25m |
|  |  | North Texas Regional/Perrin Field (KGYI) | Jones Field (KF00) | 2026-08-23 14:16 UTC | 2026-08-23 14:33 UTC | 17m |
| RGA10 | RGA | Bern Belp Airport (LSZB) | Reichenbach Air Base (LSGR) | 2026-08-23 14:16 UTC | 2026-08-23 14:32 UTC | 15m |
| CCA908 | Air China | Madrid Barajas International Airport (LEMD) | Smolensk North Airport (XUBS) | 2026-08-23 11:39 UTC | 2026-08-23 14:31 UTC | 2h 52m |
| HBZVU | HBZ | Reichenbach Air Base (LSGR) | Raron Airport (LSTA) | 2026-08-23 14:10 UTC | 2026-08-23 14:30 UTC | 20m |
| PHJVZ | PHJ | Seppe Airport (EHSE) | Rotterdam Airport (EHRD) | 2026-08-23 13:42 UTC | 2026-08-23 14:27 UTC | 45m |
| PH1483 |  | Teuge Airport (EHTE) | Teuge Airport (EHTE) | 2026-08-23 14:10 UTC | 2026-08-23 14:24 UTC | 13m |
| N4117H |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-23 13:43 UTC | 2026-08-23 14:22 UTC | 38m |
| LTA533 | LTA | Scholes International At Galveston Airport (KGLS) | Underline Ok Airport (93XS) | 2026-08-23 13:56 UTC | 2026-08-23 14:17 UTC | 20m |
| N63PC |  | Coeur D'Alene Airport (KCOE) | Ephrata Municipal Airport (KEPH) | 2026-08-23 13:48 UTC | 2026-08-23 14:13 UTC | 25m |
| FHPCJ | FHP | Marennes Le Bournet Airport (LFJI) | Rochefort-Saint-Agnant (BA 721) Airport (LFDN) | 2026-08-23 14:00 UTC | 2026-08-23 14:10 UTC | 10m |
| SWR2KT | Swiss International | Malaga Airport (LEMG) | Zurich Airport (LSZH) | 2026-08-23 12:05 UTC | 2026-08-23 14:05 UTC | 1h 59m |
| THY7XK | Turkish Airlines | Zurich Airport (LSZH) | Tekirdag Corlu Airport (LTBU) | 2026-08-23 12:01 UTC | 2026-08-23 14:04 UTC | 2h 2m |
| N750XX |  | Harry Reid International Airport (KLAS) | Van Nuys Airport (KVNY) | 2026-08-23 13:25 UTC | 2026-08-23 14:03 UTC | 38m |
| N257EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-08-23 12:59 UTC | 2026-08-23 14:01 UTC | 1h 1m |
| N35542 |  | Rock Hill/York County/Bryant Field (KUZA) | Rock Hill/York County/Bryant Field (KUZA) | 2026-08-23 13:58 UTC | 2026-08-23 14:00 UTC | 2m |
| N750AY |  | CARK (CARK) | CARK (CARK) | 2026-08-23 13:38 UTC | 2026-08-23 13:59 UTC | 21m |
| LKF45 | LKF | Kenosha Regional Airport (KENW) | Ernie's Field (1MI4) | 2026-08-23 13:24 UTC | 2026-08-23 13:58 UTC | 34m |
| HB2414 |  | Sisteron - Theze Airport (LFNS) | Mont-Dauphin - St-Crepin Airport (LFNC) | 2026-08-23 12:29 UTC | 2026-08-23 13:58 UTC | 1h 28m |
| AFL273 | AFL | Suvarnabhumi Airport (VTBS) | Bezymyanka Airfield (UWWG) | 2026-08-23 06:30 UTC | 2026-08-23 13:57 UTC | 7h 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
