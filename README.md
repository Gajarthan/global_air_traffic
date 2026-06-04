# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_08:54:18_UTC-green)

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

**Latest saved flight:** 2026-06-04 08:54:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-04 08:54:18 UTC

- **101,895** saved flights
- **36,101** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **101,895** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,245,980.0 tonnes** estimated CO2 emissions
- **72,230,726 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4201 |
| 2 | SkyWest Airlines | 3824 |
| 3 | IndiGo | 2040 |
| 4 | EJA | 1945 |
| 5 | American Airlines | 1646 |
| 6 | Southwest Airlines | 1543 |
| 7 | ENY | 1264 |
| 8 | Delta Air Lines | 1198 |
| 9 | Lufthansa | 1189 |
| 10 | Vueling | 947 |
| 11 | LATAM Airlines | 901 |
| 12 | WIF | 893 |
| 13 | AXM | 881 |
| 14 | AZU | 822 |
| 15 | LXJ | 765 |
| 16 | Swiss International | 739 |
| 17 | All Nippon Airways | 720 |
| 18 | Alaska Airlines | 714 |
| 19 | QLK | 685 |
| 20 | easyJet | 665 |
| 21 | EJU | 642 |
| 22 | Cathay Pacific | 615 |
| 23 | AEE | 592 |
| 24 | Air France | 587 |
| 25 | VIV | 587 |
| 26 | United Airlines | 568 |
| 27 | MXY | 549 |
| 28 | CXK | 545 |
| 29 | Japan Airlines | 509 |
| 30 | AXB | 503 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 85515 |
| 2 | 🇪🇸 ES | 7040 |
| 3 | 🇮🇳 IN | 6460 |
| 4 | 🇦🇺 AU | 6198 |
| 5 | 🇧🇷 BR | 5567 |
| 6 | 🇩🇪 DE | 5499 |
| 7 | 🇮🇹 IT | 5418 |
| 8 | 🇨🇦 CA | 5280 |
| 9 | 🇯🇵 JP | 4709 |
| 10 | 🇬🇧 GB | 4321 |
| 11 | 🇫🇷 FR | 4053 |
| 12 | 🇨🇴 CO | 3512 |
| 13 | 🇲🇽 MX | 3078 |
| 14 | 🇬🇷 GR | 2904 |
| 15 | 🇳🇴 NO | 2830 |
| 16 | 🇨🇭 CH | 2625 |
| 17 | 🇲🇾 MY | 2246 |
| 18 | 🇹🇷 TR | 1929 |
| 19 | 🇿🇦 ZA | 1771 |
| 20 | 🇳🇿 NZ | 1717 |
| 21 | 🇹🇭 TH | 1695 |
| 22 | 🇰🇷 KR | 1658 |
| 23 | 🇵🇱 PL | 1634 |
| 24 | 🇬🇹 GT | 1501 |
| 25 | 🇵🇭 PH | 1495 |
| 26 | 🇲🇦 MA | 1135 |
| 27 | 🇲🇴 MO | 1074 |
| 28 | 🇳🇱 NL | 1010 |
| 29 | 🇲🇪 ME | 963 |
| 30 | 🇭🇷 HR | 901 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2210 |
| 2 | Denver International Airport |  | US | 1743 |
| 3 | Tokyo International Airport |  | JP | 1560 |
| 4 | Indira Gandhi International Airport |  | IN | 1404 |
| 5 | Harry Reid International Airport |  | US | 1308 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1304 |
| 7 | Guaymaral Airport |  | CO | 1268 |
| 8 | Frankfurt am Main International Airport |  | DE | 1189 |
| 9 | Zurich Airport |  | CH | 1167 |
| 10 | La Aurora Airport |  | GT | 1154 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1100 |
| 12 | El Dorado International Airport |  | CO | 1077 |
| 13 | Macau International Airport |  | MO | 1074 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1034 |
| 15 | Chicago O'Hare International Airport |  | US | 1019 |
| 16 | Madrid Barajas International Airport |  | ES | 890 |
| 17 | Kuala Lumpur International Airport |  | MY | 887 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 876 |
| 19 | Salt Lake City International Airport |  | US | 860 |
| 20 | Capua Airport |  | IT | 848 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 794 |
| 22 | Charlotte/Douglas International Airport |  | US | 788 |
| 23 | Charles de Gaulle International Airport |  | FR | 780 |
| 24 | Malpensa International Airport |  | IT | 772 |
| 25 | Bengaluru International Airport |  | IN | 771 |
| 26 | Congonhas Airport |  | BR | 771 |
| 27 | Daniel K Inouye International Airport |  | US | 706 |
| 28 | Tenerife Norte Airport |  | ES | 700 |
| 29 | Ninoy Aquino International Airport |  | PH | 683 |
| 30 | Barcelona International Airport |  | ES | 672 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 663 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 661 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 649 |
| 34 | Amsterdam Airport Schiphol |  | NL | 624 |
| 35 | Don Mueang International Airport |  | TH | 620 |
| 36 | Vitoria/Foronda Airport |  | ES | 618 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 38 | Calgary International Airport |  | CA | 599 |
| 39 | Seattle-Tacoma International Airport |  | US | 590 |
| 40 | John Paul II International Airport Kraków-Balice Airport |  | PL | 575 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 522 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 374 | 21m | 244 km | 1,574.8 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 271 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 269 | 24m | 225 km | 1,043.6 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 256 | 14m | 114 km | 502.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 249 | 1h 26m | 910 km | 3,907.4 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 247 | 28m | 304 km | 1,294.8 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 233 | 1h 10m | 770 km | 3,095.2 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 215 | 19m | 165 km | 611.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 202 | 26m | 275 km | 957.2 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 159 | 20m | 99 km | 272.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 153 | 22m | 55 km | 145.4 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 150 | 27m | 215 km | 555.5 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 143 | 31m | 369 km | 910.2 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 141 | 27m | 152 km | 368.5 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 136 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 132 | 18m | 144 km | 328.3 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 131 | 20m | 147 km | 331.5 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 128 | 1h 39m | 1,156 km | 2,553.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 127 | 1h 1m | 695 km | 1,522.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 120 | 1h 43m | 1,423 km | 2,945.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 117 | 12m | - | - |
| 30 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IGO1157 | IndiGo | Juhu Aerodrome (VAJJ) | Simara Airport (VNSI) | 2026-06-04 06:03 UTC | 2026-06-04 08:54 UTC | 2h 50m |
| GHAZA | GHA | Kaunas International Airport (EYKA) | Siauliai International Airport (EYSA) | 2026-06-04 07:34 UTC | 2026-06-04 08:39 UTC | 1h 4m |
| OKACL | OKA | Bubovice Airport (LKBU) | Mlada Boleslav Airport (LKMB) | 2026-06-04 08:10 UTC | 2026-06-04 08:36 UTC | 25m |
| OEGFB | OEG | Salzburg Airport (LOWS) | Cologne Bonn Airport (EDDK) | 2026-06-04 07:10 UTC | 2026-06-04 08:20 UTC | 1h 10m |
| HBZVU | HBZ | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-06-04 08:11 UTC | 2026-06-04 08:17 UTC | 6m |
| N661LF |  | HI13 (HI13) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-06-04 08:03 UTC | 2026-06-04 08:14 UTC | 10m |
| KAL408 | Korean Air | Brisbane International Airport (YBBN) | Incheon International Airport (RKSI) | 2026-06-03 22:59 UTC | 2026-06-04 08:13 UTC | 9h 13m |
| FD628J |  | Perth Jandakot Airport (YPJT) | Dumbleyung Airport (YDUM) | 2026-06-04 07:35 UTC | 2026-06-04 08:10 UTC | 35m |
| HAKAR | HAK | Graz Airport (LOWG) | Pristina International Airport (BKPR) | 2026-06-04 06:59 UTC | 2026-06-04 08:06 UTC | 1h 6m |
| DHK368 | DHK | East Midlands Airport (EGNX) | John F Kennedy International Airport (KJFK) | 2026-06-04 00:58 UTC | 2026-06-04 08:06 UTC | 7h 7m |
| AGV08 | AGV | Reichenbach Air Base (LSGR) | Raron Airport (LSTA) | 2026-06-04 06:30 UTC | 2026-06-04 08:05 UTC | 1h 35m |
| WZZ912 | Wizz Air | M. R. Stefanik Airport (LZIB) | Berane Airport (LYBR) | 2026-06-04 07:15 UTC | 2026-06-04 08:05 UTC | 49m |
| HBLZC | HBL | Grenchen Airport (LSZG) | Bern Belp Airport (LSZB) | 2026-06-04 07:20 UTC | 2026-06-04 08:02 UTC | 41m |
| AUA541 | Austrian Airlines | Vienna International Airport (LOWW) | Venezia / Tessera -  Marco Polo Airport (LIPZ) | 2026-06-04 07:14 UTC | 2026-06-04 08:01 UTC | 47m |
| OAL082 | OAL | Thessaloniki Macedonia International Airport (LGTS) | Samos Airport (LGSM) | 2026-06-04 06:50 UTC | 2026-06-04 07:59 UTC | 1h 9m |
| RYR57YU | Ryanair | Dublin Airport (EIDW) | Bristol International Airport (EGGD) | 2026-06-04 07:15 UTC | 2026-06-04 07:58 UTC | 42m |
| YOI | YOI | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-06-04 07:29 UTC | 2026-06-04 07:57 UTC | 27m |
| APG6312 | APG | Godofredo P. Ramos Airport (RPVE) | Ninoy Aquino International Airport (RPLL) | 2026-06-04 07:07 UTC | 2026-06-04 07:56 UTC | 49m |
| AEE4SR | AEE | Eleftherios Venizelos International Airport (LGAV) | Mikonos Airport (LGMK) | 2026-06-04 07:35 UTC | 2026-06-04 07:53 UTC | 18m |
| FMA | FMA | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-06-04 07:36 UTC | 2026-06-04 07:53 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
