# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_23:24:19_UTC-green)

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

**Latest saved flight:** 2026-06-29 23:24:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-29 23:24:19 UTC

- **124,363** saved flights
- **42,594** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **124,363** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,503,246.9 tonnes** estimated CO2 emissions
- **87,144,750 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5074 |
| 2 | SkyWest Airlines | 4618 |
| 3 | EJA | 2436 |
| 4 | IndiGo | 2364 |
| 5 | American Airlines | 1927 |
| 6 | Southwest Airlines | 1865 |
| 7 | ENY | 1563 |
| 8 | Delta Air Lines | 1480 |
| 9 | Lufthansa | 1335 |
| 10 | LATAM Airlines | 1122 |
| 11 | Vueling | 1105 |
| 12 | WIF | 1099 |
| 13 | AZU | 1046 |
| 14 | AXM | 990 |
| 15 | LXJ | 965 |
| 16 | Swiss International | 875 |
| 17 | All Nippon Airways | 836 |
| 18 | Alaska Airlines | 815 |
| 19 | easyJet | 794 |
| 20 | QLK | 780 |
| 21 | EJU | 776 |
| 22 | Cathay Pacific | 694 |
| 23 | AEE | 686 |
| 24 | VIV | 677 |
| 25 | Air France | 676 |
| 26 | United Airlines | 666 |
| 27 | CXK | 662 |
| 28 | MXY | 649 |
| 29 | JetBlue | 634 |
| 30 | GLO | 623 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 106091 |
| 2 | 🇪🇸 ES | 8348 |
| 3 | 🇮🇳 IN | 7419 |
| 4 | 🇦🇺 AU | 7239 |
| 5 | 🇧🇷 BR | 6916 |
| 6 | 🇩🇪 DE | 6602 |
| 7 | 🇮🇹 IT | 6583 |
| 8 | 🇨🇦 CA | 6523 |
| 9 | 🇬🇧 GB | 5488 |
| 10 | 🇯🇵 JP | 5459 |
| 11 | 🇫🇷 FR | 4926 |
| 12 | 🇨🇴 CO | 4032 |
| 13 | 🇲🇽 MX | 3617 |
| 14 | 🇬🇷 GR | 3543 |
| 15 | 🇳🇴 NO | 3421 |
| 16 | 🇨🇭 CH | 3184 |
| 17 | 🇹🇷 TR | 2612 |
| 18 | 🇲🇾 MY | 2563 |
| 19 | 🇿🇦 ZA | 2047 |
| 20 | 🇵🇱 PL | 2042 |
| 21 | 🇳🇿 NZ | 2006 |
| 22 | 🇹🇭 TH | 1940 |
| 23 | 🇰🇷 KR | 1932 |
| 24 | 🇵🇭 PH | 1764 |
| 25 | 🇬🇹 GT | 1716 |
| 26 | 🇲🇦 MA | 1340 |
| 27 | 🇲🇪 ME | 1238 |
| 28 | 🇳🇱 NL | 1178 |
| 29 | 🇲🇴 MO | 1177 |
| 30 | 🇧🇸 BS | 1078 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2614 |
| 2 | Denver International Airport |  | US | 2099 |
| 3 | Tokyo International Airport |  | JP | 1804 |
| 4 | Indira Gandhi International Airport |  | IN | 1633 |
| 5 | Harry Reid International Airport |  | US | 1557 |
| 6 | Guaymaral Airport |  | CO | 1520 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1493 |
| 8 | Zurich Airport |  | CH | 1378 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1328 |
| 10 | La Aurora Airport |  | GT | 1325 |
| 11 | Frankfurt am Main International Airport |  | DE | 1288 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1225 |
| 13 | Chicago O'Hare International Airport |  | US | 1206 |
| 14 | Macau International Airport |  | MO | 1177 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1097 |
| 17 | Capua Airport |  | IT | 1060 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1040 |
| 19 | Madrid Barajas International Airport |  | ES | 1032 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1000 |
| 21 | Kuala Lumpur International Airport |  | MY | 996 |
| 22 | Congonhas Airport |  | BR | 971 |
| 23 | Charlotte/Douglas International Airport |  | US | 940 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 910 |
| 25 | Charles de Gaulle International Airport |  | FR | 905 |
| 26 | Bengaluru International Airport |  | IN | 893 |
| 27 | Malpensa International Airport |  | IT | 860 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 825 |
| 29 | Ninoy Aquino International Airport |  | PH | 818 |
| 30 | Daniel K Inouye International Airport |  | US | 796 |
| 31 | Barcelona International Airport |  | ES | 778 |
| 32 | Tenerife Norte Airport |  | ES | 767 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 758 |
| 34 | Calgary International Airport |  | CA | 732 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 728 |
| 36 | Seattle-Tacoma International Airport |  | US | 720 |
| 37 | Vitoria/Foronda Airport |  | ES | 719 |
| 38 | Amsterdam Airport Schiphol |  | NL | 715 |
| 39 | Scottsdale Airport |  | US | 715 |
| 40 | Viracopos International Airport |  | BR | 703 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 633 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 452 | 21m | 244 km | 1,903.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 322 | 24m | 225 km | 1,249.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 312 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 297 | 1h 10m | 770 km | 3,945.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 297 | 1h 25m | 910 km | 4,660.6 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 242 | 26m | 275 km | 1,146.7 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 231 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 183 | 22m | 55 km | 173.9 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 179 | 26m | 215 km | 662.9 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 175 | 20m | 99 km | 299.8 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 173 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 172 | 44m | 241 km | 714.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 168 | 27m | 152 km | 439.0 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 159 | 31m | 369 km | 1,012.1 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 158 | 1h 44m | 1,423 km | 3,877.6 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 156 | 18m | 144 km | 388.0 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 155 | 44m | 452 km | 1,208.0 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 152 | 20m | 250 km | 656.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 144 | 1h 38m | 1,156 km | 2,872.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 142 | 1h 1m | 695 km | 1,702.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 142 | 1h 17m | 961 km | 2,353.7 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |
| 29 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 139 | 30m | 49 km | 117.5 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 136 | 54m | 136 km | 318.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9421F |  | Cross Keys Airport (K17N) | Cross Keys Airport (K17N) | 2026-06-29 23:04 UTC | 2026-06-29 23:24 UTC | 19m |
| N88SM |  | Essex County Airport (KCDW) | Essex County Airport (KCDW) | 2026-06-29 22:07 UTC | 2026-06-29 23:23 UTC | 1h 15m |
| FD526 |  | Adelaide International Airport (YPAD) | Cleve Airport (YCEE) | 2026-06-29 22:40 UTC | 2026-06-29 23:22 UTC | 41m |
| N540M |  | Dupage Airport (KDPA) | Dane County Regional/Truax Field (KMSN) | 2026-06-29 22:55 UTC | 2026-06-29 23:20 UTC | 24m |
| N43JA |  | Lakewood Airport (KN12) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-06-29 22:15 UTC | 2026-06-29 22:56 UTC | 41m |
| UZX | UZX | Inverell Airport (YIVL) | Warkworth Airport (YWKW) | 2026-06-29 21:41 UTC | 2026-06-29 22:55 UTC | 1h 13m |
| JUMP13 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-06-29 21:51 UTC | 2026-06-29 22:48 UTC | 57m |
| TKR107 | TKR | Animas Air Park (K00C) | Blanding Municipal Airport (KBDG) | 2026-06-29 22:31 UTC | 2026-06-29 22:46 UTC | 14m |
| ABF9 | ABF | Reykjavik Airport (BIRK) | Tallinn Airport (EETN) | 2026-06-29 19:37 UTC | 2026-06-29 22:36 UTC | 2h 58m |
| N20543 |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-06-29 21:52 UTC | 2026-06-29 22:32 UTC | 39m |
| N552KM |  | Butler County Regional/Hogan Field (KHAO) | Middletown Regional/Hook Field (KMWO) | 2026-06-29 22:26 UTC | 2026-06-29 22:31 UTC | 5m |
| N102PG |  | Portland International Airport (KPDX) | King Salmon Airport (PAKN) | 2026-06-29 18:56 UTC | 2026-06-29 22:30 UTC | 3h 34m |
| CPA318 | Cathay Pacific | Barcelona International Airport (LEBL) | Zhuhai Airport (ZGSD) | 2026-06-29 11:32 UTC | 2026-06-29 22:29 UTC | 10h 57m |
| N78AB |  | Minden-Tahoe Airport (KMEV) | NV13 (NV13) | 2026-06-29 19:59 UTC | 2026-06-29 22:25 UTC | 2h 25m |
| AA1TB |  | Grand Junction Regional Airport (KGJT) | Blanding Municipal Airport (KBDG) | 2026-06-29 21:21 UTC | 2026-06-29 22:23 UTC | 1h 1m |
| AERT9 | AER | King Salmon Airport (PAKN) | Homer Airport (PAHO) | 2026-06-29 21:31 UTC | 2026-06-29 22:18 UTC | 47m |
| N202FF |  | Flying Cloud Airport (KFCM) | 0SD6 (0SD6) | 2026-06-29 20:27 UTC | 2026-06-29 22:17 UTC | 1h 49m |
| VTE5424 | VTE | Charlotte/Douglas International Airport (KCLT) | Mercer County Airport (KBLF) | 2026-06-29 21:54 UTC | 2026-06-29 22:17 UTC | 22m |
| N413AL |  | Fort Worth Meacham International Airport (KFTW) | Whatley Flying Service Airport (8TA1) | 2026-06-29 21:30 UTC | 2026-06-29 22:17 UTC | 47m |
| SCU48 | SCU | Gregg Airport (7OK1) | Gregg Airport (7OK1) | 2026-06-29 22:17 UTC | 2026-06-29 22:17 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
