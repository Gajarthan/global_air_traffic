# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_15:04:38_UTC-green)

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

**Latest saved flight:** 2026-06-21 15:04:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-21 15:04:38 UTC

- **116,334** saved flights
- **40,266** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **116,334** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,414,193.2 tonnes** estimated CO2 emissions
- **81,982,213 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4805 |
| 2 | SkyWest Airlines | 4312 |
| 3 | IndiGo | 2255 |
| 4 | EJA | 2247 |
| 5 | American Airlines | 1814 |
| 6 | Southwest Airlines | 1729 |
| 7 | ENY | 1448 |
| 8 | Delta Air Lines | 1370 |
| 9 | Lufthansa | 1289 |
| 10 | Vueling | 1048 |
| 11 | WIF | 1027 |
| 12 | LATAM Airlines | 1023 |
| 13 | AZU | 970 |
| 14 | AXM | 958 |
| 15 | LXJ | 882 |
| 16 | Swiss International | 821 |
| 17 | All Nippon Airways | 799 |
| 18 | Alaska Airlines | 779 |
| 19 | QLK | 751 |
| 20 | easyJet | 745 |
| 21 | EJU | 731 |
| 22 | Cathay Pacific | 673 |
| 23 | AEE | 654 |
| 24 | VIV | 643 |
| 25 | United Airlines | 642 |
| 26 | Air France | 640 |
| 27 | CXK | 623 |
| 28 | MXY | 615 |
| 29 | AXB | 577 |
| 30 | GLO | 570 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 98149 |
| 2 | 🇪🇸 ES | 7942 |
| 3 | 🇮🇳 IN | 7098 |
| 4 | 🇦🇺 AU | 6884 |
| 5 | 🇧🇷 BR | 6413 |
| 6 | 🇮🇹 IT | 6234 |
| 7 | 🇩🇪 DE | 6212 |
| 8 | 🇨🇦 CA | 6096 |
| 9 | 🇯🇵 JP | 5230 |
| 10 | 🇬🇧 GB | 5086 |
| 11 | 🇫🇷 FR | 4638 |
| 12 | 🇨🇴 CO | 3986 |
| 13 | 🇲🇽 MX | 3420 |
| 14 | 🇬🇷 GR | 3327 |
| 15 | 🇳🇴 NO | 3194 |
| 16 | 🇨🇭 CH | 2983 |
| 17 | 🇲🇾 MY | 2489 |
| 18 | 🇹🇷 TR | 2360 |
| 19 | 🇿🇦 ZA | 1962 |
| 20 | 🇵🇱 PL | 1913 |
| 21 | 🇳🇿 NZ | 1905 |
| 22 | 🇹🇭 TH | 1892 |
| 23 | 🇰🇷 KR | 1889 |
| 24 | 🇵🇭 PH | 1692 |
| 25 | 🇬🇹 GT | 1638 |
| 26 | 🇲🇦 MA | 1266 |
| 27 | 🇲🇴 MO | 1169 |
| 28 | 🇲🇪 ME | 1145 |
| 29 | 🇳🇱 NL | 1123 |
| 30 | 🇭🇷 HR | 1014 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2451 |
| 2 | Denver International Airport |  | US | 1956 |
| 3 | Tokyo International Airport |  | JP | 1733 |
| 4 | Indira Gandhi International Airport |  | IN | 1556 |
| 5 | Guaymaral Airport |  | CO | 1476 |
| 6 | Harry Reid International Airport |  | US | 1453 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1422 |
| 8 | Zurich Airport |  | CH | 1297 |
| 9 | La Aurora Airport |  | GT | 1265 |
| 10 | Frankfurt am Main International Airport |  | DE | 1259 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1239 |
| 12 | El Dorado International Airport |  | CO | 1171 |
| 13 | Macau International Airport |  | MO | 1169 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1156 |
| 15 | Chicago O'Hare International Airport |  | US | 1141 |
| 16 | Capua Airport |  | IT | 1014 |
| 17 | Salt Lake City International Airport |  | US | 997 |
| 18 | Madrid Barajas International Airport |  | ES | 988 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 971 |
| 20 | Kuala Lumpur International Airport |  | MY | 962 |
| 21 | Congonhas Airport |  | BR | 891 |
| 22 | Charlotte/Douglas International Airport |  | US | 887 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 865 |
| 24 | Bengaluru International Airport |  | IN | 859 |
| 25 | Charles de Gaulle International Airport |  | FR | 857 |
| 26 | General Edward Lawrence Logan International Airport |  | US | 856 |
| 27 | Malpensa International Airport |  | IT | 827 |
| 28 | Ninoy Aquino International Airport |  | PH | 781 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 761 |
| 30 | Daniel K Inouye International Airport |  | US | 758 |
| 31 | Tenerife Norte Airport |  | ES | 756 |
| 32 | Barcelona International Airport |  | ES | 741 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 731 |
| 34 | Don Mueang International Airport |  | TH | 685 |
| 35 | Vitoria/Foronda Airport |  | ES | 684 |
| 36 | Calgary International Airport |  | CA | 681 |
| 37 | Amsterdam Airport Schiphol |  | NL | 681 |
| 38 | Seattle-Tacoma International Airport |  | US | 667 |
| 39 | Viracopos International Airport |  | BR | 662 |
| 40 | Scottsdale Airport |  | US | 661 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 612 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 423 | 21m | 244 km | 1,781.1 t |
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
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 168 | 20m | 99 km | 287.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 167 | 26m | 215 km | 618.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 158 | 27m | 152 km | 412.9 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 154 | 31m | 369 km | 980.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 20 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 153 | 44m | 241 km | 635.5 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 152 | 44m | 452 km | 1,184.6 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 148 | 20m | 250 km | 639.3 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 143 | 1h 44m | 1,423 km | 3,509.4 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 139 | 1h 1m | 695 km | 1,666.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 136 | 1h 39m | 1,156 km | 2,713.1 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 132 | 1h 17m | 961 km | 2,188.0 t |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 129 | 24m | 223 km | 496.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N258EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-06-21 14:08 UTC | 2026-06-21 15:04 UTC | 55m |
| N491SF |  | Jim & Julie's Airport (96WA) | Jim & Julie's Airport (96WA) | 2026-06-21 14:07 UTC | 2026-06-21 15:01 UTC | 54m |
| N1311Z |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-06-21 14:12 UTC | 2026-06-21 14:59 UTC | 46m |
| N46JG |  | Flying Eagle Airport (PS21) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-06-21 14:38 UTC | 2026-06-21 14:56 UTC | 17m |
| N8065L |  | KM33 (KM33) | KM33 (KM33) | 2026-06-21 14:31 UTC | 2026-06-21 14:56 UTC | 25m |
| NWX580 | NWX | Aero Valley Airport (K52F) | Vance Field (TE76) | 2026-06-21 14:21 UTC | 2026-06-21 14:55 UTC | 34m |
| N10897 |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-06-21 14:21 UTC | 2026-06-21 14:51 UTC | 30m |
| N583CA |  | Dallas Executive Airport (KRBD) | Mid-Way Regional Airport (KJWY) | 2026-06-21 14:24 UTC | 2026-06-21 14:46 UTC | 21m |
| N417MK |  | Carson City Airport (KCXP) | Lake Tahoe Airport (KTVL) | 2026-06-21 14:37 UTC | 2026-06-21 14:45 UTC | 8m |
| N919FG |  | London Stansted Airport (EGSS) | Nice-Cote d'Azur Airport (LFMN) | 2026-06-21 13:04 UTC | 2026-06-21 14:43 UTC | 1h 39m |
| N223HF |  | Long Island Mac Arthur Airport (KISP) | Long Island Mac Arthur Airport (KISP) | 2026-06-21 14:23 UTC | 2026-06-21 14:42 UTC | 18m |
| N476LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-06-21 13:43 UTC | 2026-06-21 14:42 UTC | 58m |
| N62ZA |  | Essex County Airport (KCDW) | Francis S Gabreski Airport (KFOK) | 2026-06-21 13:44 UTC | 2026-06-21 14:37 UTC | 53m |
| N247JP |  | Boise Air Trml/Gowen Field (KBOI) | South Fork Ranch Airport (0ID0) | 2026-06-21 14:22 UTC | 2026-06-21 14:34 UTC | 12m |
| N513DS |  | Grand Junction Regional Airport (KGJT) | Westwater Airport (UT42) | 2026-06-21 14:13 UTC | 2026-06-21 14:33 UTC | 20m |
| N379NL |  | Delaware Coastal Airport (KGED) | Willaview Airport (2DE2) | 2026-06-21 14:22 UTC | 2026-06-21 14:31 UTC | 9m |
| N40NW |  | London Luton Airport (EGGW) | Ibiza Airport (LEIB) | 2026-06-21 12:31 UTC | 2026-06-21 14:31 UTC | 1h 59m |
| FCA2UA | FCA | London Biggin Hill Airport (EGKB) | Ossiacher See Airport (LOKF) | 2026-06-21 12:57 UTC | 2026-06-21 14:30 UTC | 1h 33m |
| N355ME |  | Double Eagle Ii Airport (KAEG) | Grants-Milan Municipal Airport (KGNT) | 2026-06-21 13:55 UTC | 2026-06-21 14:28 UTC | 33m |
| GLO1368 | GLO | Congonhas Airport (SBSP) | Clube de Marte Ibira de Para-Quedismo Airport (SWYV) | 2026-06-21 13:47 UTC | 2026-06-21 14:27 UTC | 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
