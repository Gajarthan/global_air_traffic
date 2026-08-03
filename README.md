# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_15:56:53_UTC-green)

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

**Latest saved flight:** 2026-08-03 15:56:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-03 15:56:53 UTC

- **168,718** saved flights
- **55,093** unique routes
- **139** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **168,718** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,033,978.1 tonnes** estimated CO2 emissions
- **117,911,772 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6731 |
| 2 | SkyWest Airlines | 6155 |
| 3 | EJA | 3353 |
| 4 | IndiGo | 2978 |
| 5 | American Airlines | 2661 |
| 6 | Southwest Airlines | 2655 |
| 7 | ENY | 2103 |
| 8 | Delta Air Lines | 2010 |
| 9 | LATAM Airlines | 1565 |
| 10 | Lufthansa | 1553 |
| 11 | AZU | 1484 |
| 12 | WIF | 1413 |
| 13 | Vueling | 1391 |
| 14 | LXJ | 1320 |
| 15 | AXM | 1166 |
| 16 | Swiss International | 1156 |
| 17 | easyJet | 1138 |
| 18 | EJU | 1036 |
| 19 | Alaska Airlines | 1031 |
| 20 | QLK | 1028 |
| 21 | All Nippon Airways | 1023 |
| 22 | VIV | 929 |
| 23 | Cathay Pacific | 901 |
| 24 | CXK | 895 |
| 25 | United Airlines | 889 |
| 26 | GLO | 884 |
| 27 | AEE | 883 |
| 28 | Air France | 871 |
| 29 | MXY | 864 |
| 30 | JetBlue | 850 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 145355 |
| 2 | 🇪🇸 ES | 10816 |
| 3 | 🇧🇷 BR | 9596 |
| 4 | 🇦🇺 AU | 9409 |
| 5 | 🇮🇳 IN | 9325 |
| 6 | 🇨🇦 CA | 9135 |
| 7 | 🇮🇹 IT | 8715 |
| 8 | 🇩🇪 DE | 8428 |
| 9 | 🇬🇧 GB | 7854 |
| 10 | 🇯🇵 JP | 6788 |
| 11 | 🇫🇷 FR | 6693 |
| 12 | 🇨🇴 CO | 6093 |
| 13 | 🇬🇷 GR | 4902 |
| 14 | 🇲🇽 MX | 4823 |
| 15 | 🇨🇭 CH | 4454 |
| 16 | 🇳🇴 NO | 4415 |
| 17 | 🇹🇷 TR | 4092 |
| 18 | 🇲🇾 MY | 3035 |
| 19 | 🇵🇱 PL | 2849 |
| 20 | 🇿🇦 ZA | 2743 |
| 21 | 🇹🇭 TH | 2458 |
| 22 | 🇳🇿 NZ | 2448 |
| 23 | 🇵🇭 PH | 2235 |
| 24 | 🇬🇹 GT | 2184 |
| 25 | 🇰🇷 KR | 2151 |
| 26 | 🇲🇦 MA | 1706 |
| 27 | 🇭🇷 HR | 1624 |
| 28 | 🇲🇪 ME | 1563 |
| 29 | 🇳🇱 NL | 1540 |
| 30 | 🇲🇴 MO | 1433 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3465 |
| 2 | Denver International Airport |  | US | 2801 |
| 3 | Tokyo International Airport |  | JP | 2132 |
| 4 | Guaymaral Airport |  | CO | 2103 |
| 5 | Indira Gandhi International Airport |  | IN | 2066 |
| 6 | Harry Reid International Airport |  | US | 2029 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1848 |
| 8 | Zurich Airport |  | CH | 1794 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1776 |
| 10 | La Aurora Airport |  | GT | 1685 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1554 |
| 12 | El Dorado International Airport |  | CO | 1529 |
| 13 | Chicago O'Hare International Airport |  | US | 1528 |
| 14 | Frankfurt am Main International Airport |  | DE | 1515 |
| 15 | Salt Lake City International Airport |  | US | 1508 |
| 16 | Macau International Airport |  | MO | 1433 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1395 |
| 18 | Congonhas Airport |  | BR | 1382 |
| 19 | Madrid Barajas International Airport |  | ES | 1329 |
| 20 | Capua Airport |  | IT | 1313 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1279 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1192 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1184 |
| 24 | Charlotte/Douglas International Airport |  | US | 1173 |
| 25 | Charles de Gaulle International Airport |  | FR | 1150 |
| 26 | Kuala Lumpur International Airport |  | MY | 1144 |
| 27 | Malpensa International Airport |  | IT | 1136 |
| 28 | Bengaluru International Airport |  | IN | 1108 |
| 29 | Ninoy Aquino International Airport |  | PH | 1051 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1041 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1036 |
| 32 | Barcelona International Airport |  | ES | 1000 |
| 33 | Daniel K Inouye International Airport |  | US | 981 |
| 34 | Seattle-Tacoma International Airport |  | US | 978 |
| 35 | Viracopos International Airport |  | BR | 962 |
| 36 | Calgary International Airport |  | CA | 952 |
| 37 | Oslo Gardermoen Airport |  | NO | 939 |
| 38 | Tenerife Norte Airport |  | ES | 939 |
| 39 | Reno/Tahoe International Airport |  | US | 936 |
| 40 | Scottsdale Airport |  | US | 934 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 874 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 614 | 21m | 244 km | 2,585.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 403 | 24m | 225 km | 1,563.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 402 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 382 | 1h 9m | 770 km | 5,074.6 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 317 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 289 | 27m | 275 km | 1,369.4 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 249 | 44m | 241 km | 1,034.3 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 246 | 19m | 165 km | 699.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 232 | 1h 47m | 1,423 km | 5,693.6 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 223 | 20m | 250 km | 963.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 219 | 26m | 215 km | 811.1 t |
| 18 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 211 | 20m | 99 km | 361.4 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 210 | 13m | - | - |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 200 | 19m | 144 km | 497.5 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 198 | 1h 15m | 961 km | 3,282.0 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 197 | 31m | 369 km | 1,254.0 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 197 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 196 | 50m | 556 km | 1,878.8 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 189 | 1h 38m | 1,156 km | 3,770.5 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 186 | 24m | 218 km | 700.7 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 185 | 1h 1m | 695 km | 2,217.6 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 182 | 44m | 452 km | 1,418.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N503MA |  | Akron Fulton International Airport (KAKR) | Wayne County Airport (KBJJ) | 2026-08-03 15:28 UTC | 2026-08-03 15:56 UTC | 28m |
| N28PK |  | Dubuque Regional Airport (KDBQ) | Dubuque Regional Airport (KDBQ) | 2026-08-03 15:42 UTC | 2026-08-03 15:55 UTC | 13m |
| N779US |  | Provo Municipal Airport (KPVU) | UT99 (UT99) | 2026-08-03 15:07 UTC | 2026-08-03 15:47 UTC | 39m |
| N829AF |  | Conroe/North Houston Regional Airport (KCXO) | Brenham Municipal Airport (K11R) | 2026-08-03 14:49 UTC | 2026-08-03 15:42 UTC | 53m |
| N5437J |  | Mckinney Ntl Airport (KTKI) | Casey Field (TE06) | 2026-08-03 15:24 UTC | 2026-08-03 15:34 UTC | 10m |
| SXS8BU | SXS | Stuttgart Airport (EDDS) | Adnan Menderes International Airport (LTBJ) | 2026-08-03 13:16 UTC | 2026-08-03 15:33 UTC | 2h 17m |
| N39688 |  | Provo Municipal Airport (KPVU) | K36U (K36U) | 2026-08-03 15:24 UTC | 2026-08-03 15:32 UTC | 7m |
| N444CU |  | Gulf Shores International/Jack Edwards Field (KJKA) | Craig Field (KSEM) | 2026-08-03 15:07 UTC | 2026-08-03 15:32 UTC | 25m |
| OYFFK | OYF | Copenhagen Roskilde Airport (EKRK) | EKSL (EKSL) | 2026-08-03 15:15 UTC | 2026-08-03 15:28 UTC | 12m |
| HBKZG | HBK | St Gallen Altenrhein Airport (LSZR) | Friedrichshafen Airport (EDNY) | 2026-08-03 14:59 UTC | 2026-08-03 15:26 UTC | 26m |
| N18NR |  | Santa Monica Municipal Airport (KSMO) | Meadows Field (KBFL) | 2026-08-03 14:46 UTC | 2026-08-03 15:24 UTC | 38m |
| AIZ419 | AIZ | Ben Gurion International Airport (LLBG) | Sivas Airport (LTAR) | 2026-08-03 14:06 UTC | 2026-08-03 15:24 UTC | 1h 17m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-08-03 14:44 UTC | 2026-08-03 15:23 UTC | 38m |
| HBKVP | HBK | Wangen-Lachen Airport (LSPV) | Wangen-Lachen Airport (LSPV) | 2026-08-03 15:04 UTC | 2026-08-03 15:22 UTC | 18m |
| N7ZT |  | San Luis Obispo County Regional Airport (KSBP) | Palm Springs International Airport (KPSP) | 2026-08-03 14:25 UTC | 2026-08-03 15:20 UTC | 55m |
| N155SL |  | William P Hobby Airport (KHOU) | True Grit South Airport (CO95) | 2026-08-03 13:21 UTC | 2026-08-03 15:20 UTC | 1h 58m |
| EJA376 | EJA | San Diego International Airport (KSAN) | Robin Airport (59AZ) | 2026-08-03 14:33 UTC | 2026-08-03 15:19 UTC | 45m |
| N423AC |  | Appleton International Airport (KATW) | 1MI9 (1MI9) | 2026-08-03 13:24 UTC | 2026-08-03 15:18 UTC | 1h 53m |
| MNTNA42 | MNT | Kubecka Aviation Airport (3XS1) | TE77 (TE77) | 2026-08-03 14:47 UTC | 2026-08-03 15:16 UTC | 29m |
| AAL1361 | American Airlines | NV13 (NV13) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-03 12:34 UTC | 2026-08-03 15:15 UTC | 2h 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
