# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_23:50:05_UTC-green)

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

**Latest saved flight:** 2026-04-18 23:50:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-18 23:50:05 UTC

- **42,244** saved flights
- **17,778** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **42,244** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **507,112.9 tonnes** estimated CO2 emissions
- **29,397,850 km** total distance flown
- **836 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1766 |
| 2 | SkyWest Airlines | 1652 |
| 3 | IndiGo | 1027 |
| 4 | EJA | 732 |
| 5 | American Airlines | 705 |
| 6 | Southwest Airlines | 598 |
| 7 | ENY | 555 |
| 8 | AXM | 434 |
| 9 | LATAM Airlines | 423 |
| 10 | Vueling | 422 |
| 11 | Lufthansa | 414 |
| 12 | All Nippon Airways | 377 |
| 13 | AZU | 377 |
| 14 | Delta Air Lines | 362 |
| 15 | QLK | 341 |
| 16 | LXJ | 333 |
| 17 | Swiss International | 324 |
| 18 | WIF | 324 |
| 19 | Alaska Airlines | 286 |
| 20 | AEE | 282 |
| 21 | EJU | 277 |
| 22 | easyJet | 272 |
| 23 | VIV | 270 |
| 24 | Japan Airlines | 257 |
| 25 | Air France | 236 |
| 26 | United Airlines | 230 |
| 27 | JetBlue | 228 |
| 28 | GLO | 224 |
| 29 | AXB | 220 |
| 30 | EDV | 219 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 33586 |
| 2 | 🇮🇳 IN | 3145 |
| 3 | 🇪🇸 ES | 3095 |
| 4 | 🇦🇺 AU | 2934 |
| 5 | 🇧🇷 BR | 2541 |
| 6 | 🇯🇵 JP | 2293 |
| 7 | 🇮🇹 IT | 2186 |
| 8 | 🇩🇪 DE | 2128 |
| 9 | 🇨🇦 CA | 2074 |
| 10 | 🇨🇴 CO | 1971 |
| 11 | 🇬🇧 GB | 1709 |
| 12 | 🇫🇷 FR | 1620 |
| 13 | 🇲🇽 MX | 1330 |
| 14 | 🇬🇷 GR | 1276 |
| 15 | 🇨🇭 CH | 1178 |
| 16 | 🇲🇾 MY | 1053 |
| 17 | 🇳🇴 NO | 1034 |
| 18 | 🇿🇦 ZA | 869 |
| 19 | 🇳🇿 NZ | 856 |
| 20 | 🇵🇭 PH | 760 |
| 21 | 🇹🇭 TH | 742 |
| 22 | 🇹🇷 TR | 733 |
| 23 | 🇬🇹 GT | 707 |
| 24 | 🇰🇷 KR | 693 |
| 25 | 🇵🇱 PL | 664 |
| 26 | 🇲🇦 MA | 522 |
| 27 | 🇳🇱 NL | 432 |
| 28 | 🇲🇪 ME | 429 |
| 29 | 🇧🇸 BS | 397 |
| 30 | 🇮🇩 ID | 382 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 992 |
| 2 | Tokyo International Airport |  | JP | 784 |
| 3 | Denver International Airport |  | US | 704 |
| 4 | El Dorado International Airport |  | CO | 689 |
| 5 | Indira Gandhi International Airport |  | IN | 678 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 632 |
| 7 | Harry Reid International Airport |  | US | 546 |
| 8 | Guaymaral Airport |  | CO | 533 |
| 9 | La Aurora Airport |  | GT | 522 |
| 10 | Zurich Airport |  | CH | 507 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 421 |
| 12 | Kuala Lumpur International Airport |  | MY | 415 |
| 13 | Chicago O'Hare International Airport |  | US | 414 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 410 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 395 |
| 16 | Frankfurt am Main International Airport |  | DE | 383 |
| 17 | Madrid Barajas International Airport |  | ES | 379 |
| 18 | Macau International Airport |  | MO | 377 |
| 19 | Charlotte/Douglas International Airport |  | US | 371 |
| 20 | Bengaluru International Airport |  | IN | 370 |
| 21 | Tenerife Norte Airport |  | ES | 368 |
| 22 | Congonhas Airport |  | BR | 366 |
| 23 | Ninoy Aquino International Airport |  | PH | 353 |
| 24 | Malpensa International Airport |  | IT | 341 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 327 |
| 26 | Salt Lake City International Airport |  | US | 324 |
| 27 | Daniel K Inouye International Airport |  | US | 314 |
| 28 | Charles de Gaulle International Airport |  | FR | 306 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 305 |
| 30 | Vitoria/Foronda Airport |  | ES | 299 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 297 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 293 |
| 33 | Reno/Tahoe International Airport |  | US | 292 |
| 34 | O. R. Tambo International Airport |  | ZA | 282 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 282 |
| 36 | Capua Airport |  | IT | 282 |
| 37 | Barcelona International Airport |  | ES | 268 |
| 38 | Viracopos International Airport |  | BR | 260 |
| 39 | Calgary International Airport |  | CA | 254 |
| 40 | Seattle-Tacoma International Airport |  | US | 250 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 214 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 197 | 1h 7m | 706 km | 2,398.5 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 152 | 24m | 225 km | 589.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 125 | 28m | 304 km | 655.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 121 | 1h 27m | 910 km | 1,898.8 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 115 | 21m | 244 km | 484.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 112 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 112 | 19m | 165 km | 318.6 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 106 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 99 | 26m | 275 km | 469.1 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 91 | 54m | 546 km | 856.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 88 | 21m | 99 km | 150.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 85 | 44m | 452 km | 662.5 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 82 | 1h 11m | 770 km | 1,089.3 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 76 | 27m | 152 km | 198.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 75 | 31m | 369 km | 477.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 70 | 20m | 250 km | 302.4 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 68 | 52m | 556 km | 651.8 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 66 | 20m | 147 km | 167.0 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 63 | 26m | 215 km | 233.3 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 60 | 1h 53m | 1,304 km | 1,349.8 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 59 | 12m | - | - |
| 28 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 58 | 1h 21m | 961 km | 961.4 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 58 | 1h 0m | 695 km | 695.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-18 23:35 UTC | 2026-04-18 23:50 UTC | 14m |
| UAL2209 | United Airlines | San Francisco International Airport (KSFO) | Newark Liberty International Airport (KEWR) | 2026-04-18 19:08 UTC | 2026-04-18 23:49 UTC | 4h 41m |
| N3517S |  | Rocky Mountain Metro Airport (KBJC) | City Of Las Animas - Bent County Airport (K7V9) | 2026-04-18 22:01 UTC | 2026-04-18 23:23 UTC | 1h 21m |
| N1968F |  | Lake Tahoe Airport (KTVL) | Dayton Valley Airpark (KA34) | 2026-04-18 22:43 UTC | 2026-04-18 23:19 UTC | 36m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-18 23:04 UTC | 2026-04-18 23:18 UTC | 14m |
| N40057 |  | Van Nuys Airport (KVNY) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-04-18 22:08 UTC | 2026-04-18 23:18 UTC | 1h 9m |
| N554CN |  | Wiley Post Airport (KPWA) | Mc Alester Regional Airport (KMLC) | 2026-04-18 22:54 UTC | 2026-04-18 23:15 UTC | 21m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-04-18 22:45 UTC | 2026-04-18 23:14 UTC | 29m |
| EJA567 | EJA | Santa Barbara Municipal Airport (KSBA) | Moffett Federal Airfield (KNUQ) | 2026-04-18 22:36 UTC | 2026-04-18 23:12 UTC | 36m |
| N479MM |  | Asheville Regional Airport (KAVL) | Hefner-Easley Airport (KH68) | 2026-04-18 21:12 UTC | 2026-04-18 23:10 UTC | 1h 58m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-18 22:14 UTC | 2026-04-18 23:10 UTC | 56m |
| N4014Z |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-04-18 23:05 UTC | 2026-04-18 23:09 UTC | 3m |
| CGEAM | CGE | Calgary / Springbank Airport (CYBW) | Banff Airport (CYBA) | 2026-04-18 22:46 UTC | 2026-04-18 23:07 UTC | 20m |
| ZKJCJ | ZKJ | Christchurch International Airport (NZCH) | Turangi Airport (NZTN) | 2026-04-18 22:13 UTC | 2026-04-18 23:06 UTC | 53m |
| N1967S |  | Fullerton Municipal Airport (KFUL) | Big Bear City Airport (KL35) | 2026-04-18 22:25 UTC | 2026-04-18 23:05 UTC | 40m |
| LWK | LWK | Perth Jandakot Airport (YPJT) | Three Springs Airport (YTHS) | 2026-04-18 22:20 UTC | 2026-04-18 23:04 UTC | 44m |
| N811ME |  | Gilbert Airport (73PA) | Lancaster Airport (KLNS) | 2026-04-18 22:48 UTC | 2026-04-18 23:03 UTC | 14m |
| ASA7004 | Alaska Airlines | Seattle-Tacoma International Airport (KSEA) | Prince Rupert Airport (CYPR) | 2026-04-18 21:51 UTC | 2026-04-18 23:02 UTC | 1h 11m |
| ZKRJZ | ZKR | Christchurch International Airport (NZCH) | Turangi Airport (NZTN) | 2026-04-18 22:03 UTC | 2026-04-18 23:01 UTC | 57m |
| N733ZK |  | Oakland San Francisco Bay Airport (KOAK) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-18 22:30 UTC | 2026-04-18 23:00 UTC | 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
