# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_17:33:03_UTC-green)

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

**Latest saved flight:** 2026-09-20 17:33:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-20 17:33:03 UTC

- **264,676** saved flights
- **78,078** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **264,676** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,207,916.0 tonnes** estimated CO2 emissions
- **185,966,143 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10474 |
| 2 | SkyWest Airlines | 9195 |
| 3 | EJA | 5144 |
| 4 | IndiGo | 4449 |
| 5 | American Airlines | 4134 |
| 6 | Southwest Airlines | 3892 |
| 7 | Delta Air Lines | 3296 |
| 8 | ENY | 3119 |
| 9 | LATAM Airlines | 2552 |
| 10 | AZU | 2490 |
| 11 | Vueling | 2223 |
| 12 | WIF | 2135 |
| 13 | LXJ | 2076 |
| 14 | Lufthansa | 2036 |
| 15 | easyJet | 1784 |
| 16 | Swiss International | 1745 |
| 17 | QLK | 1708 |
| 18 | EJU | 1671 |
| 19 | AXM | 1662 |
| 20 | United Airlines | 1622 |
| 21 | Alaska Airlines | 1567 |
| 22 | All Nippon Airways | 1525 |
| 23 | PGT | 1488 |
| 24 | WMT | 1488 |
| 25 | GLO | 1476 |
| 26 | Air France | 1451 |
| 27 | VIV | 1445 |
| 28 | Wizz Air | 1438 |
| 29 | CXK | 1282 |
| 30 | AEE | 1280 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 219882 |
| 2 | 🇪🇸 ES | 16668 |
| 3 | 🇧🇷 BR | 15495 |
| 4 | 🇦🇺 AU | 15145 |
| 5 | 🇨🇦 CA | 14725 |
| 6 | 🇮🇹 IT | 14415 |
| 7 | 🇮🇳 IN | 14072 |
| 8 | 🇩🇪 DE | 12780 |
| 9 | 🇬🇧 GB | 12281 |
| 10 | 🇨🇴 CO | 12021 |
| 11 | 🇫🇷 FR | 10575 |
| 12 | 🇯🇵 JP | 10226 |
| 13 | 🇹🇷 TR | 8023 |
| 14 | 🇬🇷 GR | 7676 |
| 15 | 🇲🇽 MX | 7277 |
| 16 | 🇨🇭 CH | 7066 |
| 17 | 🇳🇴 NO | 6533 |
| 18 | 🇹🇭 TH | 4749 |
| 19 | 🇲🇾 MY | 4480 |
| 20 | 🇿🇦 ZA | 4452 |
| 21 | 🇵🇱 PL | 4359 |
| 22 | 🇳🇿 NZ | 3678 |
| 23 | 🇵🇭 PH | 3521 |
| 24 | 🇬🇹 GT | 3375 |
| 25 | 🇭🇷 HR | 3019 |
| 26 | 🇰🇷 KR | 2999 |
| 27 | 🇲🇦 MA | 2651 |
| 28 | 🇲🇪 ME | 2482 |
| 29 | 🇳🇱 NL | 2375 |
| 30 | 🇮🇩 ID | 2220 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5406 |
| 2 | Denver International Airport |  | US | 4281 |
| 3 | Indira Gandhi International Airport |  | IN | 3183 |
| 4 | Tokyo International Airport |  | JP | 3055 |
| 5 | Harry Reid International Airport |  | US | 2817 |
| 6 | El Dorado International Airport |  | CO | 2816 |
| 7 | Guaymaral Airport |  | CO | 2786 |
| 8 | Zurich Airport |  | CH | 2754 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2658 |
| 10 | La Aurora Airport |  | GT | 2563 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2562 |
| 12 | Salt Lake City International Airport |  | US | 2332 |
| 13 | Chicago O'Hare International Airport |  | US | 2272 |
| 14 | Congonhas Airport |  | BR | 2257 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2161 |
| 16 | Capua Airport |  | IT | 2074 |
| 17 | Madrid Barajas International Airport |  | ES | 2044 |
| 18 | Frankfurt am Main International Airport |  | DE | 2022 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2000 |
| 20 | Malpensa International Airport |  | IT | 1915 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1893 |
| 22 | Charles de Gaulle International Airport |  | FR | 1872 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1862 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1841 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1806 |
| 26 | Macau International Airport |  | MO | 1761 |
| 27 | Ninoy Aquino International Airport |  | PH | 1729 |
| 28 | Barcelona International Airport |  | ES | 1654 |
| 29 | Charlotte/Douglas International Airport |  | US | 1649 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1626 |
| 31 | Viracopos International Airport |  | BR | 1606 |
| 32 | Kuala Lumpur International Airport |  | MY | 1606 |
| 33 | Seattle-Tacoma International Airport |  | US | 1552 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1541 |
| 35 | Calgary International Airport |  | CA | 1508 |
| 36 | Don Mueang International Airport |  | TH | 1506 |
| 37 | Bengaluru International Airport |  | IN | 1501 |
| 38 | Oslo Gardermoen Airport |  | NO | 1488 |
| 39 | Vancouver International Airport |  | CA | 1480 |
| 40 | Antalya International Airport |  | TR | 1419 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1113 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 989 | 21m | 244 km | 4,164.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 726 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 665 | 1h 6m | 770 km | 8,834.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 659 | 24m | 225 km | 2,556.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 592 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 432 | 44m | 555 km | 4,136.6 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 426 | 27m | 275 km | 2,018.6 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 420 | 1h 50m | 1,423 km | 10,307.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 402 | 44m | 241 km | 1,669.8 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 379 | 24m | 218 km | 1,427.8 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 361 | 21m | 250 km | 1,559.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 350 | 23m | 55 km | 332.7 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 338 | 12m | - | - |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 336 | 19m | 99 km | 575.5 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 18 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 333 | 1h 6m | 706 km | 4,054.3 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 328 | 26m | 215 km | 1,214.8 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 327 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 307 | 19m | 144 km | 763.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 286 | 42m | 535 km | 2,641.4 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 286 | 1h 50m | 1,304 km | 6,434.3 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 282 | 28m | 152 km | 737.0 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 268 | 18m | 14 km | 67.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JUMP13 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-09-20 17:15 UTC | 2026-09-20 17:33 UTC | 17m |
| N242EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-09-20 16:35 UTC | 2026-09-20 17:32 UTC | 57m |
| AWH18A | AWH | Malpensa International Airport (LIMC) | Leipzig Halle Airport (EDDP) | 2026-09-20 16:16 UTC | 2026-09-20 17:28 UTC | 1h 12m |
| N113FD |  | Mc Clellan Airfield (KMCC) | Van Vleck Airport (57CN) | 2026-09-20 16:56 UTC | 2026-09-20 17:23 UTC | 27m |
| AEE473 | AEE | Nuevo Aeropuerto Internacional Mariscal Sucre (SEQM) | Nuevo Aeropuerto Internacional Mariscal Sucre (SEQM) | 2026-09-20 17:12 UTC | 2026-09-20 17:23 UTC | 11m |
| N711FP |  | Easterwood Field (KCLL) | Addington Field (4TX8) | 2026-09-20 16:42 UTC | 2026-09-20 17:22 UTC | 40m |
| N71PW |  | Tri-Cities Airport (KTRI) | Sunrise Farms Airport (ME25) | 2026-09-20 14:04 UTC | 2026-09-20 17:22 UTC | 3h 17m |
| N125PM |  | Vance Brand Airport (KLMO) | Vance Brand Airport (KLMO) | 2026-09-20 17:00 UTC | 2026-09-20 17:21 UTC | 20m |
| XBFMS | XBF | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-09-20 16:21 UTC | 2026-09-20 17:19 UTC | 57m |
| N841AK |  | Grand Prairie Municipal Airport (KGPM) | Grand Prairie Municipal Airport (KGPM) | 2026-09-20 17:17 UTC | 2026-09-20 17:19 UTC | 1m |
| N4952G |  | Springfield Robertson County Airport (KM91) | Springfield Robertson County Airport (KM91) | 2026-09-20 16:48 UTC | 2026-09-20 17:18 UTC | 30m |
| SD1 |  | 52TA (52TA) | Tri-County Aerodrome (48TX) | 2026-09-20 16:30 UTC | 2026-09-20 17:18 UTC | 47m |
| N788RB |  | Rocky Mountain Metro Airport (KBJC) | High Plains Airport Airport (CD15) | 2026-09-20 16:53 UTC | 2026-09-20 17:17 UTC | 24m |
| N2603Y |  | Minden-Tahoe Airport (KMEV) | Lake Tahoe Airport (KTVL) | 2026-09-20 16:51 UTC | 2026-09-20 17:16 UTC | 25m |
| N44SW |  | South Bend International Airport (KSBN) | James G Whiting Memorial Field (KMEY) | 2026-09-20 15:55 UTC | 2026-09-20 17:14 UTC | 1h 19m |
| PVD426R | PVD | Frankfurt am Main International Airport (EDDF) | Munster Osnabruck Airport (EDDG) | 2026-09-20 16:39 UTC | 2026-09-20 17:13 UTC | 34m |
| AOJ69Y | AOJ | Graz Airport (LOWG) | Zurich Airport (LSZH) | 2026-09-20 16:05 UTC | 2026-09-20 17:11 UTC | 1h 6m |
| N79212 |  | Mc Clellan-Palomar Airport (KCRQ) | Mc Clellan-Palomar Airport (KCRQ) | 2026-09-20 16:45 UTC | 2026-09-20 17:11 UTC | 26m |
| HK3502G |  | Guaymaral Airport (SKGY) | Madrid Air Base (SKMA) | 2026-09-20 17:01 UTC | 2026-09-20 17:11 UTC | 10m |
| N243TS |  | San Gabriel Valley Airport (KEMT) | Riverside Airport (KRAL) | 2026-09-20 16:49 UTC | 2026-09-20 17:10 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
