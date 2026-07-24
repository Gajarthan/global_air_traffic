# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--24_14:00:27_UTC-green)

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

**Latest saved flight:** 2026-07-24 14:00:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-24 14:00:27 UTC

- **147,651** saved flights
- **49,303** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **147,651** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,767,881.2 tonnes** estimated CO2 emissions
- **102,485,868 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5974 |
| 2 | SkyWest Airlines | 5403 |
| 3 | EJA | 2915 |
| 4 | IndiGo | 2659 |
| 5 | American Airlines | 2349 |
| 6 | Southwest Airlines | 2232 |
| 7 | ENY | 1833 |
| 8 | Delta Air Lines | 1747 |
| 9 | Lufthansa | 1451 |
| 10 | LATAM Airlines | 1359 |
| 11 | AZU | 1277 |
| 12 | WIF | 1257 |
| 13 | Vueling | 1250 |
| 14 | LXJ | 1134 |
| 15 | AXM | 1071 |
| 16 | Swiss International | 1047 |
| 17 | easyJet | 953 |
| 18 | All Nippon Airways | 937 |
| 19 | Alaska Airlines | 926 |
| 20 | QLK | 922 |
| 21 | EJU | 902 |
| 22 | VIV | 820 |
| 23 | CXK | 790 |
| 24 | AEE | 779 |
| 25 | Air France | 773 |
| 26 | Cathay Pacific | 773 |
| 27 | JetBlue | 773 |
| 28 | MXY | 771 |
| 29 | United Airlines | 766 |
| 30 | GLO | 764 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 127253 |
| 2 | 🇪🇸 ES | 9543 |
| 3 | 🇦🇺 AU | 8453 |
| 4 | 🇮🇳 IN | 8345 |
| 5 | 🇧🇷 BR | 8340 |
| 6 | 🇨🇦 CA | 7889 |
| 7 | 🇮🇹 IT | 7662 |
| 8 | 🇩🇪 DE | 7572 |
| 9 | 🇬🇧 GB | 6743 |
| 10 | 🇯🇵 JP | 6154 |
| 11 | 🇫🇷 FR | 5861 |
| 12 | 🇨🇴 CO | 4905 |
| 13 | 🇲🇽 MX | 4284 |
| 14 | 🇬🇷 GR | 4183 |
| 15 | 🇳🇴 NO | 3941 |
| 16 | 🇨🇭 CH | 3867 |
| 17 | 🇹🇷 TR | 3462 |
| 18 | 🇲🇾 MY | 2790 |
| 19 | 🇵🇱 PL | 2490 |
| 20 | 🇿🇦 ZA | 2388 |
| 21 | 🇳🇿 NZ | 2243 |
| 22 | 🇹🇭 TH | 2166 |
| 23 | 🇰🇷 KR | 2055 |
| 24 | 🇵🇭 PH | 1975 |
| 25 | 🇬🇹 GT | 1913 |
| 26 | 🇲🇦 MA | 1516 |
| 27 | 🇲🇪 ME | 1462 |
| 28 | 🇳🇱 NL | 1373 |
| 29 | 🇭🇷 HR | 1344 |
| 30 | 🇲🇴 MO | 1233 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3036 |
| 2 | Denver International Airport |  | US | 2470 |
| 3 | Tokyo International Airport |  | JP | 1972 |
| 4 | Indira Gandhi International Airport |  | IN | 1852 |
| 5 | Harry Reid International Airport |  | US | 1840 |
| 6 | Guaymaral Airport |  | CO | 1823 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1665 |
| 8 | Zurich Airport |  | CH | 1627 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1553 |
| 10 | La Aurora Airport |  | GT | 1483 |
| 11 | Frankfurt am Main International Airport |  | DE | 1402 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1388 |
| 13 | Chicago O'Hare International Airport |  | US | 1367 |
| 14 | Salt Lake City International Airport |  | US | 1329 |
| 15 | El Dorado International Airport |  | CO | 1323 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1275 |
| 17 | Macau International Airport |  | MO | 1233 |
| 18 | Capua Airport |  | IT | 1193 |
| 19 | Congonhas Airport |  | BR | 1189 |
| 20 | Madrid Barajas International Airport |  | ES | 1173 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1153 |
| 22 | Kuala Lumpur International Airport |  | MY | 1075 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1065 |
| 24 | Charlotte/Douglas International Airport |  | US | 1052 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1035 |
| 26 | Charles de Gaulle International Airport |  | FR | 1021 |
| 27 | Bengaluru International Airport |  | IN | 996 |
| 28 | Malpensa International Airport |  | IT | 955 |
| 29 | Ninoy Aquino International Airport |  | PH | 924 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 903 |
| 31 | Barcelona International Airport |  | ES | 891 |
| 32 | Daniel K Inouye International Airport |  | US | 886 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 884 |
| 34 | Seattle-Tacoma International Airport |  | US | 847 |
| 35 | Tenerife Norte Airport |  | ES | 845 |
| 36 | Calgary International Airport |  | CA | 844 |
| 37 | Viracopos International Airport |  | BR | 836 |
| 38 | Scottsdale Airport |  | US | 835 |
| 39 | Amsterdam Airport Schiphol |  | NL | 826 |
| 40 | Oslo Gardermoen Airport |  | NO | 815 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 769 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 535 | 21m | 244 km | 2,252.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 360 | 24m | 225 km | 1,396.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 357 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 346 | 1h 9m | 770 km | 4,596.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 266 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 265 | 27m | 275 km | 1,255.7 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 222 | 22m | 55 km | 211.0 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 200 | 44m | 241 km | 830.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 198 | 1h 46m | 1,423 km | 4,859.2 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 196 | 26m | 215 km | 725.9 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 195 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 191 | 20m | 99 km | 327.2 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 181 | 27m | 152 km | 473.0 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 180 | 20m | 250 km | 777.5 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 175 | 31m | 369 km | 1,113.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 174 | 18m | 144 km | 432.8 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 172 | 1h 16m | 961 km | 2,851.0 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 171 | 12m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 170 | 44m | 452 km | 1,324.9 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 168 | 1h 1m | 695 km | 2,013.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 167 | 1h 39m | 1,156 km | 3,331.6 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 161 | 55m | 136 km | 377.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N694SP |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-07-24 13:14 UTC | 2026-07-24 14:00 UTC | 46m |
| LYRE71 | LYR | Tee Pee Creek Airport (8TE0) | Tee Pee Creek Airport (8TE0) | 2026-07-24 13:39 UTC | 2026-07-24 13:58 UTC | 18m |
| SCA17 | SCA | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-07-24 13:25 UTC | 2026-07-24 13:58 UTC | 32m |
| N105RF |  | Miller-Herrold Airport (28MI) | Miller-Herrold Airport (28MI) | 2026-07-24 13:27 UTC | 2026-07-24 13:56 UTC | 29m |
| N688AA |  | Kissimmee Gateway Airport (KISM) | Lake Wales Municipal Airport (KX07) | 2026-07-24 13:38 UTC | 2026-07-24 13:55 UTC | 16m |
| N465BF |  | Aurora Municipal Airport (KARR) | Dunn Airport (LL54) | 2026-07-24 13:20 UTC | 2026-07-24 13:53 UTC | 33m |
| N22WL |  | Northern Colorado Regional Airport (KFNL) | Wirth Field (CO06) | 2026-07-24 13:27 UTC | 2026-07-24 13:50 UTC | 23m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-07-24 13:29 UTC | 2026-07-24 13:50 UTC | 20m |
| SWEEP32 | SWE | Bertani Ranch Airport (23TS) | Robertson Ranch Airport (0TE0) | 2026-07-24 13:30 UTC | 2026-07-24 13:44 UTC | 13m |
| N9666V |  | Carson City Airport (KCXP) | Lake Tahoe Airport (KTVL) | 2026-07-24 13:27 UTC | 2026-07-24 13:40 UTC | 13m |
| LVKLO | LVK | San Fernando Airport (SADF) | SAVO (SAVO) | 2026-07-24 13:22 UTC | 2026-07-24 13:40 UTC | 18m |
| LYRE71 | LYR | Randolph Afb Airport (KRND) | Tee Pee Creek Airport (8TE0) | 2026-07-24 13:11 UTC | 2026-07-24 13:39 UTC | 28m |
| N806SP |  | 12II (12II) | Richmond Municipal Airport (KRID) | 2026-07-24 13:08 UTC | 2026-07-24 13:38 UTC | 30m |
| OXF5147 | OXF | Falcon Field (KFFZ) | AZ86 (AZ86) | 2026-07-24 12:51 UTC | 2026-07-24 13:38 UTC | 46m |
| N916CE |  | Erie-Ottawa International Airport (KPCW) | Sandusky County Regional Airport (KS24) | 2026-07-24 13:01 UTC | 2026-07-24 13:26 UTC | 24m |
| RJA294 | Royal Jordanian | Dallas-Fort Worth International Airport (KDFW) | Amman-Marka International Airport (OJAM) | 2026-07-24 01:37 UTC | 2026-07-24 13:25 UTC | 11h 48m |
| T7MPS |  | Saanen Airport (LSGK) | St Gallen Altenrhein Airport (LSZR) | 2026-07-24 12:52 UTC | 2026-07-24 13:24 UTC | 32m |
| RGA06 | RGA | Locarno Airport (LSZL) | Locarno Airport (LSZL) | 2026-07-24 13:12 UTC | 2026-07-24 13:23 UTC | 11m |
| FGDTJ | FGD | Rennes-Saint-Jacques Airport (LFRN) | Rennes-Saint-Jacques Airport (LFRN) | 2026-07-24 13:12 UTC | 2026-07-24 13:22 UTC | 10m |
| HK2078G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-07-24 12:54 UTC | 2026-07-24 13:21 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
