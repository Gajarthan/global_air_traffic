# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--01_17:13:27_UTC-green)

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

**Latest saved flight:** 2026-09-01 17:13:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-01 17:13:27 UTC

- **243,775** saved flights
- **73,827** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **243,775** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,936,185.2 tonnes** estimated CO2 emissions
- **170,213,635 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9791 |
| 2 | SkyWest Airlines | 8536 |
| 3 | EJA | 4707 |
| 4 | IndiGo | 4094 |
| 5 | American Airlines | 3919 |
| 6 | Southwest Airlines | 3660 |
| 7 | Delta Air Lines | 3106 |
| 8 | ENY | 2933 |
| 9 | LATAM Airlines | 2336 |
| 10 | AZU | 2264 |
| 11 | Vueling | 2090 |
| 12 | Lufthansa | 1956 |
| 13 | WIF | 1941 |
| 14 | LXJ | 1883 |
| 15 | easyJet | 1698 |
| 16 | Swiss International | 1643 |
| 17 | AXM | 1609 |
| 18 | EJU | 1569 |
| 19 | QLK | 1556 |
| 20 | United Airlines | 1532 |
| 21 | Alaska Airlines | 1455 |
| 22 | All Nippon Airways | 1438 |
| 23 | WMT | 1371 |
| 24 | GLO | 1363 |
| 25 | VIV | 1334 |
| 26 | Air France | 1333 |
| 27 | PGT | 1331 |
| 28 | Wizz Air | 1324 |
| 29 | AEE | 1205 |
| 30 | JetBlue | 1204 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 201895 |
| 2 | 🇪🇸 ES | 15673 |
| 3 | 🇧🇷 BR | 14203 |
| 4 | 🇦🇺 AU | 13832 |
| 5 | 🇨🇦 CA | 13554 |
| 6 | 🇮🇹 IT | 13358 |
| 7 | 🇮🇳 IN | 12753 |
| 8 | 🇩🇪 DE | 12032 |
| 9 | 🇬🇧 GB | 11512 |
| 10 | 🇨🇴 CO | 10532 |
| 11 | 🇫🇷 FR | 9845 |
| 12 | 🇯🇵 JP | 9735 |
| 13 | 🇹🇷 TR | 7249 |
| 14 | 🇬🇷 GR | 7199 |
| 15 | 🇲🇽 MX | 6720 |
| 16 | 🇨🇭 CH | 6561 |
| 17 | 🇳🇴 NO | 6040 |
| 18 | 🇹🇭 TH | 4408 |
| 19 | 🇲🇾 MY | 4317 |
| 20 | 🇿🇦 ZA | 4247 |
| 21 | 🇵🇱 PL | 4103 |
| 22 | 🇳🇿 NZ | 3347 |
| 23 | 🇵🇭 PH | 3340 |
| 24 | 🇬🇹 GT | 3066 |
| 25 | 🇰🇷 KR | 2866 |
| 26 | 🇭🇷 HR | 2811 |
| 27 | 🇲🇦 MA | 2467 |
| 28 | 🇲🇪 ME | 2282 |
| 29 | 🇳🇱 NL | 2207 |
| 30 | 🇮🇩 ID | 2126 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5028 |
| 2 | Denver International Airport |  | US | 3919 |
| 3 | Indira Gandhi International Airport |  | IN | 2973 |
| 4 | Tokyo International Airport |  | JP | 2900 |
| 5 | Guaymaral Airport |  | CO | 2710 |
| 6 | Harry Reid International Airport |  | US | 2593 |
| 7 | Zurich Airport |  | CH | 2563 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2486 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2432 |
| 10 | El Dorado International Airport |  | CO | 2393 |
| 11 | La Aurora Airport |  | GT | 2332 |
| 12 | Salt Lake City International Airport |  | US | 2156 |
| 13 | Chicago O'Hare International Airport |  | US | 2152 |
| 14 | Congonhas Airport |  | BR | 2082 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2019 |
| 16 | Frankfurt am Main International Airport |  | DE | 1927 |
| 17 | Capua Airport |  | IT | 1918 |
| 18 | Madrid Barajas International Airport |  | ES | 1917 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1829 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1794 |
| 21 | Malpensa International Airport |  | IT | 1745 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1720 |
| 23 | Charles de Gaulle International Airport |  | FR | 1714 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1708 |
| 25 | Ninoy Aquino International Airport |  | PH | 1625 |
| 26 | Macau International Airport |  | MO | 1624 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1561 |
| 28 | Charlotte/Douglas International Airport |  | US | 1556 |
| 29 | Kuala Lumpur International Airport |  | MY | 1555 |
| 30 | Barcelona International Airport |  | ES | 1546 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1474 |
| 32 | Viracopos International Airport |  | BR | 1445 |
| 33 | Seattle-Tacoma International Airport |  | US | 1426 |
| 34 | Don Mueang International Airport |  | TH | 1420 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1412 |
| 36 | Bengaluru International Airport |  | IN | 1412 |
| 37 | Calgary International Airport |  | CA | 1397 |
| 38 | Oslo Gardermoen Airport |  | NO | 1373 |
| 39 | Vancouver International Airport |  | CA | 1354 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1332 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1098 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 899 | 21m | 244 km | 3,785.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 629 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 621 | 24m | 225 km | 2,409.2 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 615 | 1h 6m | 770 km | 8,169.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 548 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 401 | 27m | 275 km | 1,900.2 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 385 | 1h 50m | 1,423 km | 9,448.5 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 373 | 44m | 555 km | 3,571.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 357 | 44m | 241 km | 1,482.9 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 347 | 21m | 250 km | 1,498.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 335 | 24m | 218 km | 1,262.1 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 325 | 1h 39m | 1,156 km | 6,483.6 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 324 | 22m | 55 km | 308.0 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 322 | 1h 6m | 706 km | 3,920.4 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 302 | 19m | 99 km | 517.3 t |
| 19 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 297 | 26m | 215 km | 1,100.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 287 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 283 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 280 | 1h 14m | 961 km | 4,641.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 276 | 19m | 144 km | 686.5 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 262 | 1h 50m | 1,304 km | 5,894.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 251 | 28m | 152 km | 656.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N315AK |  | Merrill Field (PAMR) | Wasilla Airport (PAWS) | 2026-09-01 17:00 UTC | 2026-09-01 17:13 UTC | 13m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-09-01 16:59 UTC | 2026-09-01 17:12 UTC | 12m |
| N673MA |  | Lewis University Airport (KLOT) | 12IL (12IL) | 2026-09-01 16:30 UTC | 2026-09-01 17:09 UTC | 39m |
| N359RC |  | Oakland/Troy Airport (KVLL) | Oakland/Troy Airport (KVLL) | 2026-09-01 16:56 UTC | 2026-09-01 17:09 UTC | 13m |
| N765KA |  | Wilding Farm Airport (6WA5) | 1WA9 (1WA9) | 2026-09-01 17:03 UTC | 2026-09-01 17:04 UTC | 0m |
| N55169 |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-09-01 15:56 UTC | 2026-09-01 17:01 UTC | 1h 5m |
| N6492H |  | Merrill Field (PAMR) | Fire Island Airport (6AK5) | 2026-09-01 16:50 UTC | 2026-09-01 16:57 UTC | 7m |
| N743TW |  | KU42 (KU42) | Wendover Airport (KENV) | 2026-09-01 16:09 UTC | 2026-09-01 16:57 UTC | 47m |
| N418PJ |  | San Rafael Airport (CA35) | San Rafael Airport (CA35) | 2026-09-01 16:35 UTC | 2026-09-01 16:56 UTC | 21m |
| N565DS |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-09-01 16:35 UTC | 2026-09-01 16:55 UTC | 20m |
| N5367H |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-09-01 16:09 UTC | 2026-09-01 16:53 UTC | 44m |
| ARCAS03 | ARC | 4TA5 (4TA5) | 54TS (54TS) | 2026-09-01 16:36 UTC | 2026-09-01 16:53 UTC | 16m |
| N4054H |  | KE80 (KE80) | Biplane Ranch Airport (NM02) | 2026-09-01 16:37 UTC | 2026-09-01 16:52 UTC | 14m |
| SINNER1 | SIN | 4XA5 (4XA5) | Anadarko Municipal Airport (KF68) | 2026-09-01 16:40 UTC | 2026-09-01 16:48 UTC | 8m |
| N15027 |  | OI99 (OI99) | Grimes Field (KI74) | 2026-09-01 16:15 UTC | 2026-09-01 16:46 UTC | 30m |
| N436CA |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-09-01 16:03 UTC | 2026-09-01 16:45 UTC | 42m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-09-01 16:31 UTC | 2026-09-01 16:44 UTC | 12m |
| N9425H |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-09-01 16:03 UTC | 2026-09-01 16:43 UTC | 39m |
| RMY3092 | RMY | Chek Lap Kok International Airport (VHHH) | Chek Lap Kok International Airport (VHHH) | 2026-09-01 16:43 UTC | 2026-09-01 16:43 UTC | 0m |
| PHJBG | PHJ | Twenthe Airport (EHTW) | Twenthe Airport (EHTW) | 2026-09-01 16:32 UTC | 2026-09-01 16:42 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
