# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_19:33:39_UTC-green)

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

**Latest saved flight:** 2026-04-20 19:33:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-20 19:33:39 UTC

- **45,694** saved flights
- **18,856** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **45,694** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **551,219.3 tonnes** estimated CO2 emissions
- **31,954,744 km** total distance flown
- **839 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1943 |
| 2 | SkyWest Airlines | 1767 |
| 3 | IndiGo | 1092 |
| 4 | EJA | 789 |
| 5 | American Airlines | 752 |
| 6 | Southwest Airlines | 653 |
| 7 | ENY | 593 |
| 8 | Lufthansa | 474 |
| 9 | Vueling | 461 |
| 10 | AXM | 458 |
| 11 | LATAM Airlines | 451 |
| 12 | All Nippon Airways | 406 |
| 13 | AZU | 395 |
| 14 | Delta Air Lines | 384 |
| 15 | QLK | 366 |
| 16 | WIF | 362 |
| 17 | LXJ | 358 |
| 18 | Swiss International | 353 |
| 19 | AEE | 313 |
| 20 | Alaska Airlines | 311 |
| 21 | EJU | 306 |
| 22 | VIV | 294 |
| 23 | easyJet | 291 |
| 24 | Japan Airlines | 276 |
| 25 | Air France | 263 |
| 26 | JetBlue | 243 |
| 27 | United Airlines | 243 |
| 28 | AXB | 240 |
| 29 | Cathay Pacific | 236 |
| 30 | GLO | 236 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 36183 |
| 2 | 🇮🇳 IN | 3383 |
| 3 | 🇪🇸 ES | 3364 |
| 4 | 🇦🇺 AU | 3131 |
| 5 | 🇧🇷 BR | 2693 |
| 6 | 🇯🇵 JP | 2489 |
| 7 | 🇮🇹 IT | 2475 |
| 8 | 🇩🇪 DE | 2360 |
| 9 | 🇨🇦 CA | 2211 |
| 10 | 🇨🇴 CO | 2109 |
| 11 | 🇬🇧 GB | 1879 |
| 12 | 🇫🇷 FR | 1745 |
| 13 | 🇲🇽 MX | 1427 |
| 14 | 🇬🇷 GR | 1401 |
| 15 | 🇨🇭 CH | 1251 |
| 16 | 🇳🇴 NO | 1152 |
| 17 | 🇲🇾 MY | 1124 |
| 18 | 🇿🇦 ZA | 954 |
| 19 | 🇳🇿 NZ | 897 |
| 20 | 🇹🇭 TH | 817 |
| 21 | 🇵🇭 PH | 811 |
| 22 | 🇹🇷 TR | 810 |
| 23 | 🇰🇷 KR | 747 |
| 24 | 🇬🇹 GT | 733 |
| 25 | 🇵🇱 PL | 730 |
| 26 | 🇲🇦 MA | 567 |
| 27 | 🇲🇪 ME | 482 |
| 28 | 🇳🇱 NL | 466 |
| 29 | 🇲🇴 MO | 424 |
| 30 | 🇧🇸 BS | 418 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1071 |
| 2 | Tokyo International Airport |  | JP | 849 |
| 3 | Denver International Airport |  | US | 757 |
| 4 | El Dorado International Airport |  | CO | 735 |
| 5 | Indira Gandhi International Airport |  | IN | 730 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 696 |
| 7 | Harry Reid International Airport |  | US | 587 |
| 8 | Guaymaral Airport |  | CO | 579 |
| 9 | Zurich Airport |  | CH | 546 |
| 10 | La Aurora Airport |  | GT | 541 |
| 11 | Chicago O'Hare International Airport |  | US | 452 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 450 |
| 13 | Kuala Lumpur International Airport |  | MY | 449 |
| 14 | Frankfurt am Main International Airport |  | DE | 447 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 437 |
| 16 | Macau International Airport |  | MO | 424 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 421 |
| 18 | Madrid Barajas International Airport |  | ES | 410 |
| 19 | Bengaluru International Airport |  | IN | 405 |
| 20 | Charlotte/Douglas International Airport |  | US | 395 |
| 21 | Tenerife Norte Airport |  | ES | 395 |
| 22 | Malpensa International Airport |  | IT | 393 |
| 23 | Congonhas Airport |  | BR | 384 |
| 24 | Ninoy Aquino International Airport |  | PH | 376 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 347 |
| 26 | Salt Lake City International Airport |  | US | 340 |
| 27 | Charles de Gaulle International Airport |  | FR | 340 |
| 28 | Daniel K Inouye International Airport |  | US | 339 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 339 |
| 30 | Capua Airport |  | IT | 330 |
| 31 | Reno/Tahoe International Airport |  | US | 317 |
| 32 | Vitoria/Foronda Airport |  | ES | 316 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 315 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 314 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 310 |
| 36 | O. R. Tambo International Airport |  | ZA | 306 |
| 37 | Barcelona International Airport |  | ES | 300 |
| 38 | Calgary International Airport |  | CA | 277 |
| 39 | Viracopos International Airport |  | BR | 275 |
| 40 | Don Mueang International Airport |  | TH | 275 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 233 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 213 | 1h 7m | 706 km | 2,593.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 170 | 14m | 114 km | 333.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 163 | 24m | 225 km | 632.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 137 | 28m | 304 km | 718.2 t |
| 6 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 130 | 21m | 244 km | 547.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 129 | 1h 27m | 910 km | 2,024.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 123 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 123 | 19m | 165 km | 349.9 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 110 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 108 | 26m | 275 km | 511.8 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 98 | 54m | 546 km | 922.7 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 93 | 44m | 452 km | 724.8 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 92 | 20m | 99 km | 157.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 85 | 1h 11m | 770 km | 1,129.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 80 | 31m | 369 km | 509.2 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 77 | 20m | 250 km | 332.6 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 74 | 52m | 556 km | 709.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 73 | 20m | 147 km | 184.7 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 71 | 26m | 215 km | 263.0 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 67 | 13m | 99 km | 114.9 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 64 | 1h 41m | 1,423 km | 1,570.7 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 64 | 1h 52m | 1,304 km | 1,439.8 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 64 | 1h 0m | 695 km | 767.2 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 63 | 58m | 493 km | 536.0 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 62 | 1h 20m | 961 km | 1,027.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N31926 |  | Bolingbrook's Clow International Airport (K1C5) | Schaumburg Regional Airport (K06C) | 2026-04-20 19:22 UTC | 2026-04-20 19:33 UTC | 11m |
| N4627F |  | Lake In The Hills Airport (K3CK) | Watertown Municipal Airport (KRYV) | 2026-04-20 18:38 UTC | 2026-04-20 19:22 UTC | 44m |
| N753GJ |  | Houma-Terrebonne Airport (KHUM) | Lakefront Airport (KNEW) | 2026-04-20 18:59 UTC | 2026-04-20 19:19 UTC | 19m |
| N507AF |  | Addison Airport (KADS) | Mesquite Metro Airport (KHQZ) | 2026-04-20 18:54 UTC | 2026-04-20 19:18 UTC | 23m |
| XBMHJ | XBM | General Mariano Matamoros Airport (MMCB) | Chilpancingo Airport (MMCH) | 2026-04-20 18:46 UTC | 2026-04-20 19:15 UTC | 28m |
| CFR89 | CFR | Sequoia Ranch Airport (CA44) | Porter Ranch Airport (68CN) | 2026-04-20 19:09 UTC | 2026-04-20 19:14 UTC | 5m |
| N25117 |  | Caddo Mills Municipal Airport (K7F3) | Commerce Municipal Airport (K2F7) | 2026-04-20 17:54 UTC | 2026-04-20 19:14 UTC | 1h 19m |
| N70846 |  | Ramona Airport (KRNM) | Desert Wings Sky Ranch Airport (04CL) | 2026-04-20 18:59 UTC | 2026-04-20 19:13 UTC | 14m |
| ERU64 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | 42AZ (42AZ) | 2026-04-20 18:53 UTC | 2026-04-20 19:12 UTC | 19m |
| WARBEVR7 | WAR | Borrego Valley Airport (KL08) | Borrego Valley Airport (KL08) | 2026-04-20 18:47 UTC | 2026-04-20 19:10 UTC | 23m |
| N910MC |  | Roberts Field (KRDM) | Sacramento Executive Airport (KSAC) | 2026-04-20 17:27 UTC | 2026-04-20 19:04 UTC | 1h 37m |
| N5253X |  | Dupage Airport (KDPA) | Colonial Acres Airport (4LL8) | 2026-04-20 18:15 UTC | 2026-04-20 19:04 UTC | 48m |
| SNAKE91 | SNA | OK79 (OK79) | Halliburton Field (KDUC) | 2026-04-20 18:35 UTC | 2026-04-20 19:03 UTC | 27m |
| N228PK |  | Mc Clellan-Palomar Airport (KCRQ) | Henderson Executive Airport (KHND) | 2026-04-20 18:22 UTC | 2026-04-20 19:01 UTC | 39m |
| BURNY11 | BUR | Wildlife/Stroud Airport (TS80) | Smiley Johnson Municipal/Bass Field (KE34) | 2026-04-20 18:43 UTC | 2026-04-20 19:00 UTC | 16m |
| N91DA |  | MY25 (MY25) | Wetenkamp Airport (29MN) | 2026-04-20 18:21 UTC | 2026-04-20 18:59 UTC | 37m |
| JRE701 | JRE | Venice Municipal Airport (KVNC) | Orlando Executive Airport (KORL) | 2026-04-20 18:31 UTC | 2026-04-20 18:59 UTC | 27m |
| E7SMS |  | Banja Luka International Airport (LQBK) | Belgrade Nikola Tesla Airport (LYBE) | 2026-04-20 18:30 UTC | 2026-04-20 18:58 UTC | 28m |
| N221MF |  | Denton Enterprise Airport (KDTO) | Xwind Farm Airport (09TA) | 2026-04-20 18:19 UTC | 2026-04-20 18:58 UTC | 38m |
| WIF1DJ | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-20 18:42 UTC | 2026-04-20 18:56 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
