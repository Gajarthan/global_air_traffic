# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_15:29:19_UTC-green)

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

**Latest saved flight:** 2026-04-11 15:29:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-11 15:29:19 UTC

- **28,917** saved flights
- **13,429** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **28,917** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **351,869.2 tonnes** estimated CO2 emissions
- **20,398,212 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1191 |
| 2 | SkyWest Airlines | 1157 |
| 3 | IndiGo | 764 |
| 4 | EJA | 504 |
| 5 | American Airlines | 499 |
| 6 | Southwest Airlines | 408 |
| 7 | ENY | 384 |
| 8 | Lufthansa | 352 |
| 9 | AXM | 314 |
| 10 | Vueling | 296 |
| 11 | LATAM Airlines | 283 |
| 12 | All Nippon Airways | 263 |
| 13 | QLK | 254 |
| 14 | AZU | 250 |
| 15 | Delta Air Lines | 243 |
| 16 | LXJ | 232 |
| 17 | Swiss International | 214 |
| 18 | Alaska Airlines | 190 |
| 19 | Japan Airlines | 190 |
| 20 | VIV | 188 |
| 21 | EJU | 187 |
| 22 | WIF | 187 |
| 23 | easyJet | 186 |
| 24 | AEE | 182 |
| 25 | United Airlines | 174 |
| 26 | EDV | 167 |
| 27 | Avianca | 163 |
| 28 | AXB | 153 |
| 29 | JetBlue | 153 |
| 30 | Air France | 149 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 22679 |
| 2 | 🇮🇳 IN | 2350 |
| 3 | 🇪🇸 ES | 2139 |
| 4 | 🇦🇺 AU | 2088 |
| 5 | 🇧🇷 BR | 1658 |
| 6 | 🇯🇵 JP | 1606 |
| 7 | 🇮🇹 IT | 1484 |
| 8 | 🇩🇪 DE | 1467 |
| 9 | 🇨🇴 CO | 1447 |
| 10 | 🇨🇦 CA | 1408 |
| 11 | 🇬🇧 GB | 1166 |
| 12 | 🇫🇷 FR | 1072 |
| 13 | 🇲🇽 MX | 917 |
| 14 | 🇬🇷 GR | 828 |
| 15 | 🇨🇭 CH | 825 |
| 16 | 🇲🇾 MY | 751 |
| 17 | 🇳🇿 NZ | 636 |
| 18 | 🇳🇴 NO | 630 |
| 19 | 🇿🇦 ZA | 605 |
| 20 | 🇵🇭 PH | 545 |
| 21 | 🇬🇹 GT | 533 |
| 22 | 🇹🇭 TH | 532 |
| 23 | 🇹🇷 TR | 522 |
| 24 | 🇰🇷 KR | 497 |
| 25 | 🇵🇱 PL | 439 |
| 26 | 🇲🇦 MA | 358 |
| 27 | 🇧🇸 BS | 302 |
| 28 | 🇲🇪 ME | 291 |
| 29 | 🇳🇱 NL | 283 |
| 30 | 🇮🇩 ID | 278 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 681 |
| 2 | Tokyo International Airport |  | JP | 540 |
| 3 | El Dorado International Airport |  | CO | 520 |
| 4 | Indira Gandhi International Airport |  | IN | 489 |
| 5 | Denver International Airport |  | US | 480 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 405 |
| 7 | La Aurora Airport |  | GT | 377 |
| 8 | Harry Reid International Airport |  | US | 366 |
| 9 | Zurich Airport |  | CH | 350 |
| 10 | Guaymaral Airport |  | CO | 329 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 299 |
| 12 | Frankfurt am Main International Airport |  | DE | 296 |
| 13 | Chicago O'Hare International Airport |  | US | 295 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 291 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 289 |
| 16 | Kuala Lumpur International Airport |  | MY | 282 |
| 17 | Macau International Airport |  | MO | 267 |
| 18 | Bengaluru International Airport |  | IN | 266 |
| 19 | Charlotte/Douglas International Airport |  | US | 260 |
| 20 | Madrid Barajas International Airport |  | ES | 254 |
| 21 | Ninoy Aquino International Airport |  | PH | 250 |
| 22 | Tenerife Norte Airport |  | ES | 249 |
| 23 | Congonhas Airport |  | BR | 240 |
| 24 | Malpensa International Airport |  | IT | 228 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 225 |
| 26 | Salt Lake City International Airport |  | US | 222 |
| 27 | Daniel K Inouye International Airport |  | US | 220 |
| 28 | Reno/Tahoe International Airport |  | US | 211 |
| 29 | Charles de Gaulle International Airport |  | FR | 204 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 199 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 199 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 195 |
| 33 | Capua Airport |  | IT | 194 |
| 34 | O. R. Tambo International Airport |  | ZA | 192 |
| 35 | Miami International Airport |  | US | 192 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 189 |
| 37 | Vitoria/Foronda Airport |  | ES | 184 |
| 38 | Seattle-Tacoma International Airport |  | US | 181 |
| 39 | Barcelona International Airport |  | ES | 181 |
| 40 | Don Mueang International Airport |  | TH | 179 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 139 | 1h 8m | 706 km | 1,692.3 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 126 | 27m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 119 | 14m | 114 km | 233.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 109 | 24m | 225 km | 422.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 100 | 28m | 304 km | 524.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 86 | 1h 27m | 910 km | 1,349.5 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 74 | 19m | 165 km | 210.5 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 74 | 21m | 99 km | 126.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 73 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 65 | 55m | 546 km | 612.0 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 62 | 1h 12m | 770 km | 823.6 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 60 | 27m | 275 km | 284.3 t |
| 15 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 16 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 58 | 9m | - | - |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 56 | 31m | 369 km | 356.5 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 53 | 46m | 452 km | 413.1 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 51 | 52m | 556 km | 488.9 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 49 | 20m | 250 km | 211.7 t |
| 21 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 47 | 13m | 99 km | 80.6 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 46 | 1h 42m | 1,423 km | 1,128.9 t |
| 24 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 45 | 21m | 244 km | 189.5 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 45 | 20m | 147 km | 113.9 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 40 | 1h 20m | 961 km | 663.0 t |
| 29 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 39 | 26m | 215 km | 144.4 t |
| 30 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N13524 |  | Fairfield County Airport (KLHQ) | Fairfield County Airport (KLHQ) | 2026-04-11 15:06 UTC | 2026-04-11 15:29 UTC | 23m |
| N339XA |  | Mesa Gateway Airport (KIWA) | Mesa Gateway Airport (KIWA) | 2026-04-11 14:55 UTC | 2026-04-11 15:28 UTC | 32m |
| N9042H |  | Albert Whitted Airport (KSPG) | Crews Homestead Ranch Airport (FL01) | 2026-04-11 14:45 UTC | 2026-04-11 15:26 UTC | 41m |
| N846AA |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-04-11 14:28 UTC | 2026-04-11 15:11 UTC | 42m |
| BOX500 | BOX | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-04-11 04:48 UTC | 2026-04-11 15:09 UTC | 10h 20m |
| OXF2978 | OXF | Falcon Field (KFFZ) | Falcon Field (KFFZ) | 2026-04-11 15:03 UTC | 2026-04-11 15:08 UTC | 5m |
| N524RD |  | Pocono Mountains Regional Airport (KMPO) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-04-11 14:40 UTC | 2026-04-11 15:08 UTC | 27m |
| N480LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-04-11 14:15 UTC | 2026-04-11 15:05 UTC | 50m |
| CONGO64 | CON | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-04-11 14:29 UTC | 2026-04-11 15:04 UTC | 34m |
| N208RF |  | Columbia Metro Airport (KCAE) | Strickland Field (89NC) | 2026-04-11 13:36 UTC | 2026-04-11 15:03 UTC | 1h 27m |
| TGBOP | TGB | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 2026-04-11 14:32 UTC | 2026-04-11 15:00 UTC | 27m |
| TAHOE51 | TAH | Easterwood Field (KCLL) | Jonesboro Airport (KF88) | 2026-04-11 14:14 UTC | 2026-04-11 15:00 UTC | 46m |
| N285ME |  | Witham Field (KSUA) | Tampa Executive Airport (KVDF) | 2026-04-11 14:14 UTC | 2026-04-11 15:00 UTC | 46m |
| HBKKC | HBK | Amlikon Glider Airport (LSPA) | Winterthur Airport (LSPH) | 2026-04-11 14:17 UTC | 2026-04-11 14:58 UTC | 41m |
| BCS694 | BCS | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-04-11 03:46 UTC | 2026-04-11 14:57 UTC | 11h 10m |
| NDU362 | NDU | Mesa Gateway Airport (KIWA) | Pinal Airpark (KMZJ) | 2026-04-11 14:25 UTC | 2026-04-11 14:57 UTC | 31m |
| N771DE |  | Piedmont Triad International Airport (KGSO) | NC20 (NC20) | 2026-04-11 14:26 UTC | 2026-04-11 14:50 UTC | 23m |
| AEE6SM | AEE | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-04-11 14:22 UTC | 2026-04-11 14:49 UTC | 27m |
| N410JA |  | Waukegan Ntl Airport (KUGN) | Kenosha Regional Airport (KENW) | 2026-04-11 14:38 UTC | 2026-04-11 14:49 UTC | 10m |
| CXK644 | CXK | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-04-11 13:34 UTC | 2026-04-11 14:48 UTC | 1h 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
