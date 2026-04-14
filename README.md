# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_03:15:36_UTC-green)

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

**Latest saved flight:** 2026-04-14 03:15:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-14 03:15:36 UTC

- **33,399** saved flights
- **14,907** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **33,399** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **411,219.2 tonnes** estimated CO2 emissions
- **23,838,794 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1414 |
| 2 | SkyWest Airlines | 1354 |
| 3 | IndiGo | 842 |
| 4 | American Airlines | 583 |
| 5 | EJA | 577 |
| 6 | Southwest Airlines | 486 |
| 7 | ENY | 449 |
| 8 | Lufthansa | 377 |
| 9 | AXM | 348 |
| 10 | Vueling | 340 |
| 11 | LATAM Airlines | 335 |
| 12 | All Nippon Airways | 301 |
| 13 | AZU | 296 |
| 14 | Delta Air Lines | 283 |
| 15 | QLK | 276 |
| 16 | LXJ | 271 |
| 17 | Swiss International | 252 |
| 18 | Alaska Airlines | 227 |
| 19 | WIF | 225 |
| 20 | easyJet | 222 |
| 21 | EJU | 221 |
| 22 | VIV | 218 |
| 23 | AEE | 216 |
| 24 | Japan Airlines | 210 |
| 25 | EDV | 195 |
| 26 | United Airlines | 193 |
| 27 | GLO | 182 |
| 28 | Avianca | 181 |
| 29 | JetBlue | 180 |
| 30 | Air France | 178 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 26392 |
| 2 | 🇮🇳 IN | 2577 |
| 3 | 🇪🇸 ES | 2497 |
| 4 | 🇦🇺 AU | 2310 |
| 5 | 🇧🇷 BR | 1965 |
| 6 | 🇯🇵 JP | 1811 |
| 7 | 🇮🇹 IT | 1772 |
| 8 | 🇨🇴 CO | 1675 |
| 9 | 🇩🇪 DE | 1666 |
| 10 | 🇨🇦 CA | 1642 |
| 11 | 🇬🇧 GB | 1360 |
| 12 | 🇫🇷 FR | 1222 |
| 13 | 🇲🇽 MX | 1075 |
| 14 | 🇬🇷 GR | 969 |
| 15 | 🇨🇭 CH | 922 |
| 16 | 🇲🇾 MY | 841 |
| 17 | 🇳🇴 NO | 747 |
| 18 | 🇳🇿 NZ | 713 |
| 19 | 🇿🇦 ZA | 682 |
| 20 | 🇵🇭 PH | 631 |
| 21 | 🇹🇷 TR | 618 |
| 22 | 🇹🇭 TH | 601 |
| 23 | 🇬🇹 GT | 600 |
| 24 | 🇰🇷 KR | 568 |
| 25 | 🇵🇱 PL | 518 |
| 26 | 🇲🇦 MA | 425 |
| 27 | 🇧🇸 BS | 340 |
| 28 | 🇲🇪 ME | 330 |
| 29 | 🇳🇱 NL | 321 |
| 30 | 🇲🇴 MO | 317 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 802 |
| 2 | Tokyo International Airport |  | JP | 615 |
| 3 | El Dorado International Airport |  | CO | 599 |
| 4 | Denver International Airport |  | US | 569 |
| 5 | Indira Gandhi International Airport |  | IN | 545 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 473 |
| 7 | Harry Reid International Airport |  | US | 441 |
| 8 | La Aurora Airport |  | GT | 437 |
| 9 | Zurich Airport |  | CH | 413 |
| 10 | Guaymaral Airport |  | CO | 406 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 343 |
| 12 | Chicago O'Hare International Airport |  | US | 343 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 340 |
| 14 | Frankfurt am Main International Airport |  | DE | 326 |
| 15 | Kuala Lumpur International Airport |  | MY | 323 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 318 |
| 17 | Macau International Airport |  | MO | 317 |
| 18 | Charlotte/Douglas International Airport |  | US | 305 |
| 19 | Madrid Barajas International Airport |  | ES | 303 |
| 20 | Bengaluru International Airport |  | IN | 300 |
| 21 | Tenerife Norte Airport |  | ES | 294 |
| 22 | Congonhas Airport |  | BR | 292 |
| 23 | Ninoy Aquino International Airport |  | PH | 291 |
| 24 | Malpensa International Airport |  | IT | 272 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 258 |
| 26 | Daniel K Inouye International Airport |  | US | 256 |
| 27 | Salt Lake City International Airport |  | US | 253 |
| 28 | Reno/Tahoe International Airport |  | US | 243 |
| 29 | Charles de Gaulle International Airport |  | FR | 240 |
| 30 | Capua Airport |  | IT | 236 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 235 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 228 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 228 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 228 |
| 35 | O. R. Tambo International Airport |  | ZA | 223 |
| 36 | Vitoria/Foronda Airport |  | ES | 222 |
| 37 | Miami International Airport |  | US | 214 |
| 38 | Barcelona International Airport |  | ES | 214 |
| 39 | Seattle-Tacoma International Airport |  | US | 211 |
| 40 | Calgary International Airport |  | CA | 205 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 157 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 156 | 1h 8m | 706 km | 1,899.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 139 | 14m | 114 km | 272.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 122 | 24m | 225 km | 473.3 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 107 | 28m | 304 km | 560.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 94 | 1h 27m | 910 km | 1,475.1 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 85 | 19m | 165 km | 241.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 81 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 81 | 9m | - | - |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 75 | 54m | 546 km | 706.1 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 74 | 21m | 244 km | 311.6 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 73 | 27m | 275 km | 345.9 t |
| 14 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 69 | 1h 12m | 770 km | 916.6 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 65 | 31m | 369 km | 413.7 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 61 | 45m | 452 km | 475.4 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 20 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 57 | 20m | 250 km | 246.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 53 | 20m | 147 km | 134.1 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 52 | 1h 41m | 1,423 km | 1,276.2 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 52 | 13m | 99 km | 89.2 t |
| 25 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 49 | 16m | 162 km | 137.4 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 48 | 23m | 252 km | 208.4 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 48 | 12m | 15 km | 12.7 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 47 | 1h 20m | 961 km | 779.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 47 | 1h 53m | 1,304 km | 1,057.4 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 46 | 59m | 695 km | 551.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| J992KT |  | Adi Sutjipto International Airport (WARJ) | Adi Sutjipto International Airport (WARJ) | 2026-04-14 02:50 UTC | 2026-04-14 03:15 UTC | 24m |
| N79US |  | Logan-Cache Airport (KLGU) | Wendover Airport (KENV) | 2026-04-14 02:04 UTC | 2026-04-14 03:07 UTC | 1h 2m |
| ZFW | ZFW | RAAF Williams Point Cook Base (YMPC) | Melbourne Moorabbin Airport (YMMB) | 2026-04-14 02:33 UTC | 2026-04-14 02:47 UTC | 14m |
| MER1 | MER | Paraparaumu Airport (NZPP) | Molesworth Airport (NZML) | 2026-04-14 02:06 UTC | 2026-04-14 02:44 UTC | 38m |
| MXY609 | MXY | San Francisco International Airport (KSFO) | San Bernardino International Airport (KSBD) | 2026-04-14 01:45 UTC | 2026-04-14 02:43 UTC | 58m |
| XSR340 | XSR | Kelly Field (KSKF) | Jack Poore Airport (5KS8) | 2026-04-14 00:59 UTC | 2026-04-14 02:40 UTC | 1h 41m |
| N119AN |  | Miami Executive Airport (KTMB) | Lake Wales Municipal Airport (KX07) | 2026-04-14 01:38 UTC | 2026-04-14 02:40 UTC | 1h 2m |
| SWA3807 | Southwest Airlines | Oakland San Francisco Bay Airport (KOAK) | Santa Monica Municipal Airport (KSMO) | 2026-04-14 01:40 UTC | 2026-04-14 02:37 UTC | 57m |
| BURNY20 | BUR | Wichita Valley Airport (KF14) | 5TA4 (5TA4) | 2026-04-14 02:17 UTC | 2026-04-14 02:36 UTC | 19m |
| VHJKM | VHJ | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-04-14 02:22 UTC | 2026-04-14 02:33 UTC | 11m |
| N400EM |  | Albuquerque International Sunport Airport (KABQ) | Grants-Milan Municipal Airport (KGNT) | 2026-04-14 02:08 UTC | 2026-04-14 02:31 UTC | 22m |
| QLK40D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Wellington Airport (YWEL) | 2026-04-14 02:02 UTC | 2026-04-14 02:31 UTC | 29m |
| SLI871 | SLI | General Heriberto Jara International Airport (MMVR) | Atizapan De Zaragoza Airport (MMJC) | 2026-04-14 01:51 UTC | 2026-04-14 02:30 UTC | 39m |
| JAL2823 | Japan Airlines | Okadama Airport (RJCO) | Odate Noshiro Airport (RJSR) | 2026-04-14 01:47 UTC | 2026-04-14 02:30 UTC | 42m |
| CJT590 | CJT | Saskatoon John G. Diefenbaker International Airport (CYXE) | Regina Beach Airport (CKL9) | 2026-04-14 02:12 UTC | 2026-04-14 02:29 UTC | 16m |
| QLK1510 | QLK | Melbourne International Airport (YMML) | Sydney Kingsford Smith International Airport (YSSY) | 2026-04-14 01:14 UTC | 2026-04-14 02:29 UTC | 1h 14m |
| OUA39 | OUA | University Of Oklahoma Westheimer Airport (KOUN) | Haskell Airport (K2K9) | 2026-04-14 01:51 UTC | 2026-04-14 02:27 UTC | 35m |
| SWA2178 | Southwest Airlines | Harry Reid International Airport (KLAS) | Tampa International Airport (KTPA) | 2026-04-13 22:34 UTC | 2026-04-14 02:25 UTC | 3h 51m |
| BTR | BTR | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-04-14 02:01 UTC | 2026-04-14 02:25 UTC | 24m |
| IGO638Y | IndiGo | Indira Gandhi International Airport (VIDP) | Coimbatore Air Force Station (VOSX) | 2026-04-13 23:54 UTC | 2026-04-14 02:22 UTC | 2h 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
