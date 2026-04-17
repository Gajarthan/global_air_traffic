# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_19:06:17_UTC-green)

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

**Latest saved flight:** 2026-04-17 19:06:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-17 19:06:17 UTC

- **39,767** saved flights
- **17,027** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **39,767** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **478,994.4 tonnes** estimated CO2 emissions
- **27,767,792 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1668 |
| 2 | SkyWest Airlines | 1548 |
| 3 | IndiGo | 976 |
| 4 | EJA | 685 |
| 5 | American Airlines | 664 |
| 6 | Southwest Airlines | 556 |
| 7 | ENY | 512 |
| 8 | AXM | 413 |
| 9 | Vueling | 399 |
| 10 | LATAM Airlines | 393 |
| 11 | Lufthansa | 386 |
| 12 | AZU | 354 |
| 13 | All Nippon Airways | 351 |
| 14 | Delta Air Lines | 338 |
| 15 | QLK | 327 |
| 16 | LXJ | 316 |
| 17 | WIF | 314 |
| 18 | Swiss International | 306 |
| 19 | AEE | 265 |
| 20 | Alaska Airlines | 264 |
| 21 | easyJet | 260 |
| 22 | EJU | 259 |
| 23 | VIV | 252 |
| 24 | Japan Airlines | 238 |
| 25 | Air France | 227 |
| 26 | United Airlines | 216 |
| 27 | EDV | 214 |
| 28 | JetBlue | 211 |
| 29 | GLO | 207 |
| 30 | AIQ | 203 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 31409 |
| 2 | 🇮🇳 IN | 2978 |
| 3 | 🇪🇸 ES | 2954 |
| 4 | 🇦🇺 AU | 2785 |
| 5 | 🇧🇷 BR | 2349 |
| 6 | 🇯🇵 JP | 2131 |
| 7 | 🇮🇹 IT | 2077 |
| 8 | 🇩🇪 DE | 2016 |
| 9 | 🇨🇦 CA | 1953 |
| 10 | 🇨🇴 CO | 1923 |
| 11 | 🇬🇧 GB | 1627 |
| 12 | 🇫🇷 FR | 1522 |
| 13 | 🇲🇽 MX | 1248 |
| 14 | 🇬🇷 GR | 1199 |
| 15 | 🇨🇭 CH | 1099 |
| 16 | 🇲🇾 MY | 1003 |
| 17 | 🇳🇴 NO | 1000 |
| 18 | 🇿🇦 ZA | 827 |
| 19 | 🇳🇿 NZ | 811 |
| 20 | 🇵🇭 PH | 722 |
| 21 | 🇹🇭 TH | 716 |
| 22 | 🇹🇷 TR | 700 |
| 23 | 🇬🇹 GT | 680 |
| 24 | 🇰🇷 KR | 641 |
| 25 | 🇵🇱 PL | 618 |
| 26 | 🇲🇦 MA | 491 |
| 27 | 🇳🇱 NL | 404 |
| 28 | 🇲🇪 ME | 397 |
| 29 | 🇧🇸 BS | 387 |
| 30 | 🇮🇩 ID | 365 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 920 |
| 2 | Tokyo International Airport |  | JP | 728 |
| 3 | El Dorado International Airport |  | CO | 675 |
| 4 | Denver International Airport |  | US | 658 |
| 5 | Indira Gandhi International Airport |  | IN | 640 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 596 |
| 7 | Harry Reid International Airport |  | US | 515 |
| 8 | Guaymaral Airport |  | CO | 509 |
| 9 | La Aurora Airport |  | GT | 500 |
| 10 | Zurich Airport |  | CH | 484 |
| 11 | Kuala Lumpur International Airport |  | MY | 394 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 392 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 389 |
| 14 | Chicago O'Hare International Airport |  | US | 386 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 379 |
| 16 | Macau International Airport |  | MO | 363 |
| 17 | Madrid Barajas International Airport |  | ES | 358 |
| 18 | Tenerife Norte Airport |  | ES | 355 |
| 19 | Charlotte/Douglas International Airport |  | US | 354 |
| 20 | Frankfurt am Main International Airport |  | DE | 350 |
| 21 | Bengaluru International Airport |  | IN | 348 |
| 22 | Congonhas Airport |  | BR | 345 |
| 23 | Ninoy Aquino International Airport |  | PH | 335 |
| 24 | Malpensa International Airport |  | IT | 322 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 308 |
| 26 | Salt Lake City International Airport |  | US | 305 |
| 27 | Daniel K Inouye International Airport |  | US | 295 |
| 28 | Charles de Gaulle International Airport |  | FR | 294 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 286 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 274 |
| 31 | Vitoria/Foronda Airport |  | ES | 273 |
| 32 | Capua Airport |  | IT | 271 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 268 |
| 34 | Reno/Tahoe International Airport |  | US | 268 |
| 35 | O. R. Tambo International Airport |  | ZA | 265 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 264 |
| 37 | Barcelona International Airport |  | ES | 256 |
| 38 | Viracopos International Airport |  | BR | 243 |
| 39 | Don Mueang International Airport |  | TH | 240 |
| 40 | Calgary International Airport |  | CA | 237 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 204 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 183 | 1h 8m | 706 km | 2,228.0 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 158 | 14m | 114 km | 309.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 141 | 24m | 225 km | 547.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 114 | 28m | 304 km | 597.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 111 | 1h 27m | 910 km | 1,741.8 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 105 | 19m | 165 km | 298.7 t |
| 8 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 103 | 21m | 244 km | 433.7 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 101 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 100 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 91 | 26m | 275 km | 431.2 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 86 | 54m | 546 km | 809.7 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 85 | 21m | 99 km | 145.6 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 81 | 1h 11m | 770 km | 1,076.0 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 77 | 45m | 452 km | 600.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 73 | 27m | 152 km | 190.8 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 72 | 31m | 369 km | 458.3 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 63 | 52m | 556 km | 603.9 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 62 | 20m | 147 km | 156.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 62 | 20m | 250 km | 267.8 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 61 | 1h 41m | 1,423 km | 1,497.0 t |
| 23 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 61 | 16m | 162 km | 171.0 t |
| 24 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 60 | 26m | 215 km | 222.2 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 58 | 13m | - | - |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 56 | 1h 53m | 1,304 km | 1,259.9 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 55 | 1h 20m | 961 km | 911.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| NIT249 | NIT | Cochran Airport (K48A) | Chinaberry Ranch Airport (9GA8) | 2026-04-17 17:24 UTC | 2026-04-17 19:06 UTC | 1h 41m |
| DSU56 | DSU | Cleveland Municipal Airport (KRNV) | Cleveland Municipal Airport (KRNV) | 2026-04-17 18:53 UTC | 2026-04-17 19:03 UTC | 10m |
| NGF6968 | NGF | Merced Yosemite Regional Airport (KMCE) | San Carlos Airport (KSQL) | 2026-04-17 18:23 UTC | 2026-04-17 19:03 UTC | 40m |
| DSU59 | DSU | Cleveland Municipal Airport (KRNV) | Cleveland Municipal Airport (KRNV) | 2026-04-17 18:52 UTC | 2026-04-17 19:02 UTC | 10m |
| N626JS |  | Laurence G Hanscom Field (KBED) | Lebanon Municipal Airport (KLEB) | 2026-04-17 18:39 UTC | 2026-04-17 19:01 UTC | 22m |
| C6026 |  | Mobile Regional Airport (KMOB) | Mobile Regional Airport (KMOB) | 2026-04-17 17:59 UTC | 2026-04-17 18:59 UTC | 1h 0m |
| N942RM |  | Livingston County/Spencer J Hardy Airport (KOZW) | Livingston County/Spencer J Hardy Airport (KOZW) | 2026-04-17 18:20 UTC | 2026-04-17 18:56 UTC | 36m |
| MEOW01 | MEO | 75OK (75OK) | Flying E Ranch Airport (OK16) | 2026-04-17 18:28 UTC | 2026-04-17 18:56 UTC | 28m |
| N3619N |  | Lancaster Airport (KLNS) | Lancaster Airport (KLNS) | 2026-04-17 18:09 UTC | 2026-04-17 18:53 UTC | 44m |
| N9136B |  | Solberg/Hunterdon Airport (KN51) | Solberg/Hunterdon Airport (KN51) | 2026-04-17 18:33 UTC | 2026-04-17 18:50 UTC | 16m |
| ARCAS50 | ARC | 4TA5 (4TA5) | TX20 (TX20) | 2026-04-17 18:34 UTC | 2026-04-17 18:49 UTC | 15m |
| N891JS |  | Valdosta Regional Airport (KVLD) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-17 18:06 UTC | 2026-04-17 18:49 UTC | 43m |
| RDHK763 | RDH | Langley Afb Airport (KLFI) | Norfolk Ns (Chambers Field) Airport (KNGU) | 2026-04-17 18:44 UTC | 2026-04-17 18:49 UTC | 4m |
| N110CT |  | Capital City Airport (KCXY) | Capital City Airport (KCXY) | 2026-04-17 18:44 UTC | 2026-04-17 18:49 UTC | 4m |
| AMX484 | Aeromexico | Licenciado Benito Juarez International Airport (MMMX) | Harry Reid International Airport (KLAS) | 2026-04-17 15:13 UTC | 2026-04-17 18:45 UTC | 3h 31m |
| CFPCG | CFP | Vancouver International Airport (CYVR) | Quamichan Lake (Raven Field) Airport (CML2) | 2026-04-17 18:29 UTC | 2026-04-17 18:44 UTC | 15m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-04-17 18:30 UTC | 2026-04-17 18:43 UTC | 13m |
| N98EG |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-04-17 18:13 UTC | 2026-04-17 18:41 UTC | 28m |
| N9382W |  | City Of Colorado Springs Municipal Airport (KCOS) | Granite Mountain Lodge Airport (CO11) | 2026-04-17 17:38 UTC | 2026-04-17 18:40 UTC | 1h 1m |
| CGFHA | CGF | Vancouver International Airport (CYVR) | Pitt Meadows Airport (CYPK) | 2026-04-17 18:19 UTC | 2026-04-17 18:38 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
