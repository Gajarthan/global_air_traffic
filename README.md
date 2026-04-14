# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_12:31:10_UTC-green)

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

**Latest saved flight:** 2026-04-14 12:31:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-14 12:31:10 UTC

- **33,931** saved flights
- **15,054** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **33,931** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **417,790.2 tonnes** estimated CO2 emissions
- **24,219,720 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1453 |
| 2 | SkyWest Airlines | 1354 |
| 3 | IndiGo | 859 |
| 4 | American Airlines | 585 |
| 5 | EJA | 577 |
| 6 | Southwest Airlines | 487 |
| 7 | ENY | 449 |
| 8 | Lufthansa | 380 |
| 9 | AXM | 362 |
| 10 | Vueling | 347 |
| 11 | LATAM Airlines | 338 |
| 12 | All Nippon Airways | 309 |
| 13 | AZU | 300 |
| 14 | QLK | 289 |
| 15 | Delta Air Lines | 286 |
| 16 | LXJ | 271 |
| 17 | Swiss International | 261 |
| 18 | WIF | 239 |
| 19 | easyJet | 230 |
| 20 | Alaska Airlines | 228 |
| 21 | AEE | 225 |
| 22 | EJU | 225 |
| 23 | VIV | 219 |
| 24 | Japan Airlines | 216 |
| 25 | EDV | 195 |
| 26 | United Airlines | 193 |
| 27 | Air France | 185 |
| 28 | GLO | 184 |
| 29 | Avianca | 181 |
| 30 | JetBlue | 180 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 26484 |
| 2 | 🇮🇳 IN | 2635 |
| 3 | 🇪🇸 ES | 2555 |
| 4 | 🇦🇺 AU | 2416 |
| 5 | 🇧🇷 BR | 1989 |
| 6 | 🇯🇵 JP | 1872 |
| 7 | 🇮🇹 IT | 1828 |
| 8 | 🇩🇪 DE | 1721 |
| 9 | 🇨🇴 CO | 1682 |
| 10 | 🇨🇦 CA | 1648 |
| 11 | 🇬🇧 GB | 1398 |
| 12 | 🇫🇷 FR | 1258 |
| 13 | 🇲🇽 MX | 1076 |
| 14 | 🇬🇷 GR | 1001 |
| 15 | 🇨🇭 CH | 941 |
| 16 | 🇲🇾 MY | 875 |
| 17 | 🇳🇴 NO | 780 |
| 18 | 🇳🇿 NZ | 726 |
| 19 | 🇿🇦 ZA | 714 |
| 20 | 🇵🇭 PH | 652 |
| 21 | 🇹🇷 TR | 634 |
| 22 | 🇹🇭 TH | 621 |
| 23 | 🇬🇹 GT | 601 |
| 24 | 🇰🇷 KR | 584 |
| 25 | 🇵🇱 PL | 533 |
| 26 | 🇲🇦 MA | 432 |
| 27 | 🇧🇸 BS | 340 |
| 28 | 🇲🇪 ME | 338 |
| 29 | 🇳🇱 NL | 334 |
| 30 | 🇮🇩 ID | 326 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 803 |
| 2 | Tokyo International Airport |  | JP | 639 |
| 3 | El Dorado International Airport |  | CO | 602 |
| 4 | Denver International Airport |  | US | 570 |
| 5 | Indira Gandhi International Airport |  | IN | 561 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 489 |
| 7 | Harry Reid International Airport |  | US | 446 |
| 8 | La Aurora Airport |  | GT | 438 |
| 9 | Zurich Airport |  | CH | 423 |
| 10 | Guaymaral Airport |  | CO | 408 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 343 |
| 12 | Chicago O'Hare International Airport |  | US | 343 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 340 |
| 14 | Kuala Lumpur International Airport |  | MY | 336 |
| 15 | Frankfurt am Main International Airport |  | DE | 331 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 331 |
| 17 | Macau International Airport |  | MO | 320 |
| 18 | Madrid Barajas International Airport |  | ES | 310 |
| 19 | Charlotte/Douglas International Airport |  | US | 306 |
| 20 | Bengaluru International Airport |  | IN | 303 |
| 21 | Ninoy Aquino International Airport |  | PH | 301 |
| 22 | Tenerife Norte Airport |  | ES | 300 |
| 23 | Congonhas Airport |  | BR | 297 |
| 24 | Malpensa International Airport |  | IT | 281 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 259 |
| 26 | Daniel K Inouye International Airport |  | US | 259 |
| 27 | Salt Lake City International Airport |  | US | 255 |
| 28 | Capua Airport |  | IT | 250 |
| 29 | Charles de Gaulle International Airport |  | FR | 249 |
| 30 | Reno/Tahoe International Airport |  | US | 243 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 238 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 237 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 233 |
| 34 | O. R. Tambo International Airport |  | ZA | 231 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 228 |
| 36 | Vitoria/Foronda Airport |  | ES | 226 |
| 37 | Barcelona International Airport |  | ES | 221 |
| 38 | Miami International Airport |  | US | 214 |
| 39 | Seattle-Tacoma International Airport |  | US | 212 |
| 40 | Viracopos International Airport |  | BR | 208 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 161 | 1h 8m | 706 km | 1,960.2 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 158 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 139 | 14m | 114 km | 272.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 126 | 24m | 225 km | 488.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 100 | 1h 27m | 910 km | 1,569.2 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 90 | 19m | 165 km | 256.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 85 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 81 | 9m | - | - |
| 10 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 76 | 21m | 244 km | 320.0 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 74 | 27m | 275 km | 350.7 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 73 | 1h 12m | 770 km | 969.7 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 66 | 31m | 369 km | 420.1 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 63 | 45m | 452 km | 491.0 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 59 | 20m | 250 km | 254.8 t |
| 21 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 55 | 20m | 147 km | 139.2 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 53 | 1h 41m | 1,423 km | 1,300.7 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 52 | 13m | 99 km | 89.2 t |
| 25 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 51 | 23m | 252 km | 221.4 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 51 | 16m | 162 km | 143.0 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 48 | 12m | 15 km | 12.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 48 | 14m | 154 km | 127.2 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 47 | 1h 20m | 961 km | 779.0 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 47 | 1h 53m | 1,304 km | 1,057.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N609FA |  | Lazy J Ranch Airport (PS82) | Solberg/Hunterdon Airport (KN51) | 2026-04-14 11:56 UTC | 2026-04-14 12:31 UTC | 34m |
| N157ES |  | Stadtlohn-Vreden Airport (EDLS) | Twenthe Airport (EHTW) | 2026-04-14 12:10 UTC | 2026-04-14 12:26 UTC | 15m |
| N108HF |  | Long Island Mac Arthur Airport (KISP) | Long Island Mac Arthur Airport (KISP) | 2026-04-14 11:42 UTC | 2026-04-14 12:25 UTC | 42m |
| HBSGW | HBS | Lommis Airfield (LSZT) | Lommis Airfield (LSZT) | 2026-04-14 12:01 UTC | 2026-04-14 12:19 UTC | 17m |
| N278SP |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-04-14 11:09 UTC | 2026-04-14 12:10 UTC | 1h 1m |
| N5114Z |  | Westchester County Airport (KHPN) | Francis S Gabreski Airport (KFOK) | 2026-04-14 11:26 UTC | 2026-04-14 12:08 UTC | 41m |
| DEMON3 | DEM | Eindhoven Airport (EHEH) | Volkel Air Base (EHVK) | 2026-04-14 11:56 UTC | 2026-04-14 12:08 UTC | 11m |
| N53371 |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-04-14 11:43 UTC | 2026-04-14 12:07 UTC | 23m |
| HKS51 | HKS | Humberside Airport (EGNJ) | EGYO (EGYO) | 2026-04-14 11:47 UTC | 2026-04-14 12:06 UTC | 18m |
| HK5271G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-14 11:41 UTC | 2026-04-14 12:01 UTC | 20m |
| UNI135 | UNI | Cologne Bonn Airport (EDDK) | La Morgal Airport (LEMR) | 2026-04-14 10:15 UTC | 2026-04-14 12:01 UTC | 1h 45m |
| N22265 |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-04-14 11:28 UTC | 2026-04-14 12:01 UTC | 32m |
| N80EW |  | Teterboro Airport (KTEB) | Laguardia Airport (KLGA) | 2026-04-14 11:53 UTC | 2026-04-14 12:00 UTC | 7m |
| N4887G |  | Miami Homestead General Aviation Airport (KX51) | Miami Homestead General Aviation Airport (KX51) | 2026-04-14 11:42 UTC | 2026-04-14 11:59 UTC | 16m |
| HBSGT | HBS | Lommis Airfield (LSZT) | Lommis Airfield (LSZT) | 2026-04-14 11:40 UTC | 2026-04-14 11:57 UTC | 16m |
| N780LA |  | Northeast Philadelphia Airport (KPNE) | Lancaster Airport (KLNS) | 2026-04-14 11:11 UTC | 2026-04-14 11:52 UTC | 40m |
| N734VQ |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-04-14 11:20 UTC | 2026-04-14 11:49 UTC | 29m |
| IGO5EC | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Birsa Munda Airport (VERC) | 2026-04-14 11:04 UTC | 2026-04-14 11:48 UTC | 43m |
| DEKBC | DEK | Sun View Field (03PR) | Straubing Airport (EDMS) | 2026-04-14 11:44 UTC | 2026-04-14 11:45 UTC | 0m |
|  |  | Brookneal/Campbell County Airport (K0V4) | Brookneal/Campbell County Airport (K0V4) | 2026-04-14 11:42 UTC | 2026-04-14 11:43 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
