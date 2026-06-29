# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_19:54:45_UTC-green)

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

**Latest saved flight:** 2026-06-29 19:54:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-29 19:54:45 UTC

- **124,012** saved flights
- **42,494** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **124,012** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,499,309.2 tonnes** estimated CO2 emissions
- **86,916,473 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5065 |
| 2 | SkyWest Airlines | 4593 |
| 3 | EJA | 2427 |
| 4 | IndiGo | 2364 |
| 5 | American Airlines | 1917 |
| 6 | Southwest Airlines | 1857 |
| 7 | ENY | 1557 |
| 8 | Delta Air Lines | 1475 |
| 9 | Lufthansa | 1334 |
| 10 | LATAM Airlines | 1117 |
| 11 | Vueling | 1104 |
| 12 | WIF | 1097 |
| 13 | AZU | 1042 |
| 14 | AXM | 990 |
| 15 | LXJ | 963 |
| 16 | Swiss International | 873 |
| 17 | All Nippon Airways | 836 |
| 18 | Alaska Airlines | 813 |
| 19 | easyJet | 792 |
| 20 | QLK | 779 |
| 21 | EJU | 776 |
| 22 | Cathay Pacific | 693 |
| 23 | AEE | 684 |
| 24 | Air France | 675 |
| 25 | VIV | 675 |
| 26 | United Airlines | 664 |
| 27 | CXK | 656 |
| 28 | MXY | 648 |
| 29 | JetBlue | 629 |
| 30 | GLO | 621 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 105612 |
| 2 | 🇪🇸 ES | 8340 |
| 3 | 🇮🇳 IN | 7419 |
| 4 | 🇦🇺 AU | 7229 |
| 5 | 🇧🇷 BR | 6893 |
| 6 | 🇩🇪 DE | 6600 |
| 7 | 🇮🇹 IT | 6576 |
| 8 | 🇨🇦 CA | 6496 |
| 9 | 🇬🇧 GB | 5479 |
| 10 | 🇯🇵 JP | 5459 |
| 11 | 🇫🇷 FR | 4918 |
| 12 | 🇨🇴 CO | 4031 |
| 13 | 🇲🇽 MX | 3607 |
| 14 | 🇬🇷 GR | 3537 |
| 15 | 🇳🇴 NO | 3416 |
| 16 | 🇨🇭 CH | 3181 |
| 17 | 🇹🇷 TR | 2609 |
| 18 | 🇲🇾 MY | 2563 |
| 19 | 🇿🇦 ZA | 2047 |
| 20 | 🇵🇱 PL | 2035 |
| 21 | 🇳🇿 NZ | 1998 |
| 22 | 🇹🇭 TH | 1940 |
| 23 | 🇰🇷 KR | 1932 |
| 24 | 🇵🇭 PH | 1762 |
| 25 | 🇬🇹 GT | 1710 |
| 26 | 🇲🇦 MA | 1331 |
| 27 | 🇲🇪 ME | 1237 |
| 28 | 🇳🇱 NL | 1178 |
| 29 | 🇲🇴 MO | 1177 |
| 30 | 🇧🇸 BS | 1076 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2606 |
| 2 | Denver International Airport |  | US | 2088 |
| 3 | Tokyo International Airport |  | JP | 1804 |
| 4 | Indira Gandhi International Airport |  | IN | 1633 |
| 5 | Harry Reid International Airport |  | US | 1547 |
| 6 | Guaymaral Airport |  | CO | 1519 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1492 |
| 8 | Zurich Airport |  | CH | 1377 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1323 |
| 10 | La Aurora Airport |  | GT | 1321 |
| 11 | Frankfurt am Main International Airport |  | DE | 1287 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1222 |
| 13 | Chicago O'Hare International Airport |  | US | 1201 |
| 14 | Macau International Airport |  | MO | 1177 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1089 |
| 17 | Capua Airport |  | IT | 1058 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1034 |
| 19 | Madrid Barajas International Airport |  | ES | 1032 |
| 20 | Kuala Lumpur International Airport |  | MY | 996 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 993 |
| 22 | Congonhas Airport |  | BR | 969 |
| 23 | Charlotte/Douglas International Airport |  | US | 934 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 910 |
| 25 | Charles de Gaulle International Airport |  | FR | 904 |
| 26 | Bengaluru International Airport |  | IN | 893 |
| 27 | Malpensa International Airport |  | IT | 858 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 819 |
| 29 | Ninoy Aquino International Airport |  | PH | 817 |
| 30 | Daniel K Inouye International Airport |  | US | 795 |
| 31 | Barcelona International Airport |  | ES | 777 |
| 32 | Tenerife Norte Airport |  | ES | 765 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 755 |
| 34 | Calgary International Airport |  | CA | 726 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 721 |
| 36 | Vitoria/Foronda Airport |  | ES | 719 |
| 37 | Seattle-Tacoma International Airport |  | US | 716 |
| 38 | Amsterdam Airport Schiphol |  | NL | 715 |
| 39 | Scottsdale Airport |  | US | 711 |
| 40 | Don Mueang International Airport |  | TH | 702 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 633 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 451 | 21m | 244 km | 1,899.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 322 | 24m | 225 km | 1,249.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 311 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 297 | 1h 10m | 770 km | 3,945.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 297 | 1h 25m | 910 km | 4,660.6 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 242 | 26m | 275 km | 1,146.7 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 231 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 180 | 22m | 55 km | 171.1 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 179 | 26m | 215 km | 662.9 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 175 | 20m | 99 km | 299.8 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 173 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 171 | 44m | 241 km | 710.3 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 168 | 27m | 152 km | 439.0 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 158 | 1h 44m | 1,423 km | 3,877.6 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 158 | 31m | 369 km | 1,005.7 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 156 | 18m | 144 km | 388.0 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 155 | 44m | 452 km | 1,208.0 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 152 | 20m | 250 km | 656.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 144 | 1h 38m | 1,156 km | 2,872.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 142 | 1h 1m | 695 km | 1,702.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 141 | 1h 17m | 961 km | 2,337.1 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 140 | 13m | - | - |
| 29 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 139 | 30m | 49 km | 117.5 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 136 | 54m | 136 km | 318.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BYF19 | BYF | San Carlos Airport (KSQL) | Palo Alto Airport (KPAO) | 2026-06-29 18:59 UTC | 2026-06-29 19:54 UTC | 54m |
| N2521W |  | Finger Lakes Regional Airport (K0G7) | Oswego County Airport (KFZY) | 2026-06-29 19:34 UTC | 2026-06-29 19:51 UTC | 16m |
| RAM803L | Royal Air Maroc | London Gatwick Airport (EGKK) | Mohammed V International Airport (GMMN) | 2026-06-29 17:14 UTC | 2026-06-29 19:45 UTC | 2h 30m |
| CXK1046 | CXK | Georgetown Executive Airport (KGTU) | Fayette Regional Air Center Airport (K3T5) | 2026-06-29 19:11 UTC | 2026-06-29 19:45 UTC | 33m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-06-29 19:23 UTC | 2026-06-29 19:40 UTC | 17m |
| N978AP |  | Gillespie Field (KSEE) | Hemet-Ryan Airport (KHMT) | 2026-06-29 18:17 UTC | 2026-06-29 19:34 UTC | 1h 16m |
| N115PJ |  | Essex County Airport (KCDW) | Laguardia Airport (KLGA) | 2026-06-29 18:17 UTC | 2026-06-29 19:29 UTC | 1h 12m |
| N717AF |  | Los Banos Municipal Airport (KLSN) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-06-29 19:09 UTC | 2026-06-29 19:27 UTC | 18m |
| CXK477 | CXK | Robinson Field (8IN2) | Columbus Municipal Airport (KBAK) | 2026-06-29 18:17 UTC | 2026-06-29 19:21 UTC | 1h 4m |
| N453PT |  | Essex County Airport (KCDW) | Essex County Airport (KCDW) | 2026-06-29 18:47 UTC | 2026-06-29 19:20 UTC | 33m |
| N13715 |  | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-06-29 19:14 UTC | 2026-06-29 19:19 UTC | 4m |
| RYR719 | Ryanair | Paris Beauvais Tille Airport (LFOB) | Birmingham International Airport (EGBB) | 2026-06-29 18:38 UTC | 2026-06-29 19:17 UTC | 39m |
| N6599D |  | Tampa Executive Airport (KVDF) | Palm Beach County Park Airport (KLNA) | 2026-06-29 17:38 UTC | 2026-06-29 19:17 UTC | 1h 38m |
| TKR160 | TKR | Animas Air Park (K00C) | Blanding Municipal Airport (KBDG) | 2026-06-29 18:59 UTC | 2026-06-29 19:15 UTC | 16m |
| N4CC |  | Lykens Valley Flying Assoc Airport (34PA) | Karlindo Airport (3PN2) | 2026-06-29 19:00 UTC | 2026-06-29 19:14 UTC | 13m |
| AAH444 | AAH | Daniel K Inouye International Airport (PHNL) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-06-29 18:41 UTC | 2026-06-29 19:13 UTC | 31m |
| TKR169 | TKR | Animas Air Park (K00C) | Blanding Municipal Airport (KBDG) | 2026-06-29 18:54 UTC | 2026-06-29 19:12 UTC | 18m |
| BNOG | BNO | Sandnessjoen Airport Stokka (ENST) | Bardufoss Airport (ENDU) | 2026-06-29 18:21 UTC | 2026-06-29 19:11 UTC | 50m |
| N76JF |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-06-29 18:33 UTC | 2026-06-29 19:09 UTC | 36m |
| N106RF |  | Chloride Airport (NM51) | Chloride Airport (NM51) | 2026-06-29 18:38 UTC | 2026-06-29 19:09 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
