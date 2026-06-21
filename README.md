# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_16:46:24_UTC-green)

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

**Latest saved flight:** 2026-06-21 16:46:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-21 16:46:24 UTC

- **116,546** saved flights
- **40,318** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **116,546** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,416,125.5 tonnes** estimated CO2 emissions
- **82,094,231 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4814 |
| 2 | SkyWest Airlines | 4323 |
| 3 | IndiGo | 2258 |
| 4 | EJA | 2255 |
| 5 | American Airlines | 1819 |
| 6 | Southwest Airlines | 1732 |
| 7 | ENY | 1452 |
| 8 | Delta Air Lines | 1372 |
| 9 | Lufthansa | 1290 |
| 10 | Vueling | 1049 |
| 11 | WIF | 1031 |
| 12 | LATAM Airlines | 1026 |
| 13 | AZU | 970 |
| 14 | AXM | 958 |
| 15 | LXJ | 884 |
| 16 | Swiss International | 825 |
| 17 | All Nippon Airways | 799 |
| 18 | Alaska Airlines | 780 |
| 19 | QLK | 751 |
| 20 | easyJet | 746 |
| 21 | EJU | 731 |
| 22 | Cathay Pacific | 673 |
| 23 | AEE | 657 |
| 24 | VIV | 643 |
| 25 | Air France | 642 |
| 26 | United Airlines | 642 |
| 27 | CXK | 625 |
| 28 | MXY | 617 |
| 29 | AXB | 578 |
| 30 | GLO | 570 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 98362 |
| 2 | 🇪🇸 ES | 7954 |
| 3 | 🇮🇳 IN | 7107 |
| 4 | 🇦🇺 AU | 6884 |
| 5 | 🇧🇷 BR | 6420 |
| 6 | 🇮🇹 IT | 6242 |
| 7 | 🇩🇪 DE | 6217 |
| 8 | 🇨🇦 CA | 6105 |
| 9 | 🇯🇵 JP | 5230 |
| 10 | 🇬🇧 GB | 5096 |
| 11 | 🇫🇷 FR | 4652 |
| 12 | 🇨🇴 CO | 3988 |
| 13 | 🇲🇽 MX | 3423 |
| 14 | 🇬🇷 GR | 3336 |
| 15 | 🇳🇴 NO | 3203 |
| 16 | 🇨🇭 CH | 2992 |
| 17 | 🇲🇾 MY | 2489 |
| 18 | 🇹🇷 TR | 2369 |
| 19 | 🇿🇦 ZA | 1972 |
| 20 | 🇵🇱 PL | 1918 |
| 21 | 🇳🇿 NZ | 1905 |
| 22 | 🇹🇭 TH | 1892 |
| 23 | 🇰🇷 KR | 1889 |
| 24 | 🇵🇭 PH | 1692 |
| 25 | 🇬🇹 GT | 1641 |
| 26 | 🇲🇦 MA | 1270 |
| 27 | 🇲🇴 MO | 1169 |
| 28 | 🇲🇪 ME | 1146 |
| 29 | 🇳🇱 NL | 1125 |
| 30 | 🇭🇷 HR | 1015 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2457 |
| 2 | Denver International Airport |  | US | 1962 |
| 3 | Tokyo International Airport |  | JP | 1733 |
| 4 | Indira Gandhi International Airport |  | IN | 1558 |
| 5 | Guaymaral Airport |  | CO | 1478 |
| 6 | Harry Reid International Airport |  | US | 1455 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1427 |
| 8 | Zurich Airport |  | CH | 1302 |
| 9 | La Aurora Airport |  | GT | 1267 |
| 10 | Frankfurt am Main International Airport |  | DE | 1260 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1240 |
| 12 | El Dorado International Airport |  | CO | 1171 |
| 13 | Macau International Airport |  | MO | 1169 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1157 |
| 15 | Chicago O'Hare International Airport |  | US | 1144 |
| 16 | Capua Airport |  | IT | 1015 |
| 17 | Salt Lake City International Airport |  | US | 998 |
| 18 | Madrid Barajas International Airport |  | ES | 988 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 971 |
| 20 | Kuala Lumpur International Airport |  | MY | 962 |
| 21 | Congonhas Airport |  | BR | 894 |
| 22 | Charlotte/Douglas International Airport |  | US | 888 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 865 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 860 |
| 25 | Charles de Gaulle International Airport |  | FR | 860 |
| 26 | Bengaluru International Airport |  | IN | 860 |
| 27 | Malpensa International Airport |  | IT | 828 |
| 28 | Ninoy Aquino International Airport |  | PH | 781 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 761 |
| 30 | Daniel K Inouye International Airport |  | US | 760 |
| 31 | Tenerife Norte Airport |  | ES | 757 |
| 32 | Barcelona International Airport |  | ES | 742 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 732 |
| 34 | Don Mueang International Airport |  | TH | 685 |
| 35 | Vitoria/Foronda Airport |  | ES | 685 |
| 36 | Calgary International Airport |  | CA | 684 |
| 37 | Amsterdam Airport Schiphol |  | NL | 682 |
| 38 | Seattle-Tacoma International Airport |  | US | 669 |
| 39 | Viracopos International Airport |  | BR | 662 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 661 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 613 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 424 | 21m | 244 km | 1,785.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 311 | 24m | 225 km | 1,206.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 299 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 285 | 1h 25m | 910 km | 4,472.3 t |
| 7 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 281 | 1h 10m | 770 km | 3,732.9 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 261 | 28m | 304 km | 1,368.2 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 231 | 26m | 275 km | 1,094.6 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 230 | 19m | 165 km | 654.2 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 217 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 174 | 22m | 55 km | 165.4 t |
| 14 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 168 | 26m | 215 km | 622.2 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 168 | 20m | 99 km | 287.8 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 158 | 27m | 152 km | 412.9 t |
| 18 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 155 | 44m | 241 km | 643.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 154 | 31m | 369 km | 980.2 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 152 | 44m | 452 km | 1,184.6 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 148 | 20m | 250 km | 639.3 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 143 | 1h 44m | 1,423 km | 3,509.4 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 139 | 1h 1m | 695 km | 1,666.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 136 | 1h 39m | 1,156 km | 2,713.1 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 133 | 1h 17m | 961 km | 2,204.5 t |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 129 | 24m | 223 km | 496.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JUMP13 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-06-21 16:21 UTC | 2026-06-21 16:46 UTC | 24m |
| N967JB |  | Rocky Mountain Metro Airport (KBJC) | Pueblo Memorial Airport (KPUB) | 2026-06-21 16:14 UTC | 2026-06-21 16:42 UTC | 28m |
| N2YV |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-06-21 16:19 UTC | 2026-06-21 16:40 UTC | 20m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-06-21 16:19 UTC | 2026-06-21 16:36 UTC | 16m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-06-21 16:16 UTC | 2026-06-21 16:31 UTC | 15m |
| JBU892 | JetBlue | Tampa International Airport (KTPA) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-21 13:56 UTC | 2026-06-21 16:27 UTC | 2h 31m |
| N115AH |  | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-06-21 15:48 UTC | 2026-06-21 16:26 UTC | 38m |
| ECIDM | ECI | Sabadell Airport (LELL) | Sabadell Airport (LELL) | 2026-06-21 15:09 UTC | 2026-06-21 16:26 UTC | 1h 16m |
| TKR855 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-06-21 15:50 UTC | 2026-06-21 16:25 UTC | 35m |
| CXK500 | CXK | Jacksonville Executive At Craig Airport (KCRG) | K55J (K55J) | 2026-06-21 16:05 UTC | 2026-06-21 16:24 UTC | 19m |
| OPN86 | OPN | Montgomery County Airpark (KGAI) | II49 (II49) | 2026-06-21 14:20 UTC | 2026-06-21 16:23 UTC | 2h 3m |
| N220BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-06-21 15:20 UTC | 2026-06-21 16:22 UTC | 1h 2m |
| FGOBR | FGO | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | 2026-06-21 16:06 UTC | 2026-06-21 16:19 UTC | 13m |
| N782ND |  | Trenton Mercer Airport (KTTN) | Lehigh Valley International Airport (KABE) | 2026-06-21 15:19 UTC | 2026-06-21 16:18 UTC | 59m |
| TGKME | TGK | Coban Airport (MGCB) | La Aurora Airport (MGGT) | 2026-06-21 15:54 UTC | 2026-06-21 16:17 UTC | 23m |
| AIC4WS | Air India | Indira Gandhi International Airport (VIDP) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-06-21 14:22 UTC | 2026-06-21 16:16 UTC | 1h 53m |
| GPMMC | GPM | EGYO (EGYO) | Norwich International Airport (EGSH) | 2026-06-21 15:36 UTC | 2026-06-21 16:15 UTC | 39m |
| EJA591 | EJA | MA72 (MA72) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-21 15:51 UTC | 2026-06-21 16:13 UTC | 21m |
| N929SS |  | North Little Rock Municipal Airport (KORK) | Poplar Bluff Regional Business Airport (KPOF) | 2026-06-21 15:51 UTC | 2026-06-21 16:12 UTC | 21m |
| HK5463X |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-06-21 15:53 UTC | 2026-06-21 16:11 UTC | 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
