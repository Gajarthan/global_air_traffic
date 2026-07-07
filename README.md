# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--07_16:00:12_UTC-green)

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

**Latest saved flight:** 2026-07-07 16:00:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-07 16:00:12 UTC

- **132,209** saved flights
- **44,879** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **132,209** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,593,190.3 tonnes** estimated CO2 emissions
- **92,358,858 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5383 |
| 2 | SkyWest Airlines | 4888 |
| 3 | EJA | 2594 |
| 4 | IndiGo | 2467 |
| 5 | American Airlines | 2058 |
| 6 | Southwest Airlines | 1986 |
| 7 | ENY | 1662 |
| 8 | Delta Air Lines | 1583 |
| 9 | Lufthansa | 1377 |
| 10 | LATAM Airlines | 1216 |
| 11 | Vueling | 1161 |
| 12 | WIF | 1154 |
| 13 | AZU | 1122 |
| 14 | LXJ | 1019 |
| 15 | AXM | 1017 |
| 16 | Swiss International | 938 |
| 17 | All Nippon Airways | 868 |
| 18 | easyJet | 844 |
| 19 | Alaska Airlines | 842 |
| 20 | QLK | 825 |
| 21 | EJU | 813 |
| 22 | VIV | 730 |
| 23 | AEE | 717 |
| 24 | Air France | 717 |
| 25 | Cathay Pacific | 716 |
| 26 | CXK | 709 |
| 27 | United Airlines | 702 |
| 28 | JetBlue | 694 |
| 29 | MXY | 686 |
| 30 | GLO | 680 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 113266 |
| 2 | 🇪🇸 ES | 8804 |
| 3 | 🇮🇳 IN | 7736 |
| 4 | 🇦🇺 AU | 7608 |
| 5 | 🇧🇷 BR | 7461 |
| 6 | 🇨🇦 CA | 6984 |
| 7 | 🇩🇪 DE | 6919 |
| 8 | 🇮🇹 IT | 6895 |
| 9 | 🇬🇧 GB | 5912 |
| 10 | 🇯🇵 JP | 5685 |
| 11 | 🇫🇷 FR | 5259 |
| 12 | 🇨🇴 CO | 4151 |
| 13 | 🇲🇽 MX | 3854 |
| 14 | 🇬🇷 GR | 3785 |
| 15 | 🇳🇴 NO | 3584 |
| 16 | 🇨🇭 CH | 3420 |
| 17 | 🇹🇷 TR | 2945 |
| 18 | 🇲🇾 MY | 2634 |
| 19 | 🇵🇱 PL | 2185 |
| 20 | 🇿🇦 ZA | 2179 |
| 21 | 🇳🇿 NZ | 2091 |
| 22 | 🇹🇭 TH | 2039 |
| 23 | 🇰🇷 KR | 1968 |
| 24 | 🇵🇭 PH | 1817 |
| 25 | 🇬🇹 GT | 1800 |
| 26 | 🇲🇦 MA | 1403 |
| 27 | 🇲🇪 ME | 1311 |
| 28 | 🇳🇱 NL | 1246 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1167 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2763 |
| 2 | Denver International Airport |  | US | 2245 |
| 3 | Tokyo International Airport |  | JP | 1865 |
| 4 | Indira Gandhi International Airport |  | IN | 1710 |
| 5 | Harry Reid International Airport |  | US | 1645 |
| 6 | Guaymaral Airport |  | CO | 1613 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1555 |
| 8 | Zurich Airport |  | CH | 1471 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1407 |
| 10 | La Aurora Airport |  | GT | 1390 |
| 11 | Frankfurt am Main International Airport |  | DE | 1333 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1271 |
| 13 | Chicago O'Hare International Airport |  | US | 1270 |
| 14 | Macau International Airport |  | MO | 1186 |
| 15 | El Dorado International Airport |  | CO | 1181 |
| 16 | Salt Lake City International Airport |  | US | 1175 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1140 |
| 18 | Madrid Barajas International Airport |  | ES | 1085 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1082 |
| 20 | Capua Airport |  | IT | 1078 |
| 21 | Congonhas Airport |  | BR | 1055 |
| 22 | Kuala Lumpur International Airport |  | MY | 1023 |
| 23 | Charlotte/Douglas International Airport |  | US | 982 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 957 |
| 25 | Charles de Gaulle International Airport |  | FR | 956 |
| 26 | Bengaluru International Airport |  | IN | 933 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 908 |
| 28 | Malpensa International Airport |  | IT | 881 |
| 29 | Ninoy Aquino International Airport |  | PH | 843 |
| 30 | Daniel K Inouye International Airport |  | US | 825 |
| 31 | Barcelona International Airport |  | ES | 816 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 808 |
| 33 | Tenerife Norte Airport |  | ES | 796 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 778 |
| 35 | Calgary International Airport |  | CA | 770 |
| 36 | Seattle-Tacoma International Airport |  | US | 760 |
| 37 | Scottsdale Airport |  | US | 759 |
| 38 | Vitoria/Foronda Airport |  | ES | 755 |
| 39 | Viracopos International Airport |  | BR | 754 |
| 40 | Amsterdam Airport Schiphol |  | NL | 748 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 677 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 478 | 21m | 244 km | 2,012.7 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 331 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 329 | 24m | 225 km | 1,276.4 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 321 | 1h 10m | 770 km | 4,264.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 283 | 14m | 114 km | 555.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 250 | 26m | 275 km | 1,184.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 241 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 193 | 22m | 55 km | 183.4 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 185 | 44m | 241 km | 768.5 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 184 | 26m | 215 km | 681.5 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 183 | 20m | 99 km | 313.5 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 178 | 13m | - | - |
| 18 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 177 | 1h 46m | 1,423 km | 4,343.9 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 165 | 31m | 369 km | 1,050.3 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 162 | 18m | 144 km | 403.0 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 161 | 20m | 250 km | 695.4 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 159 | 44m | 452 km | 1,239.2 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 159 | 30m | 49 km | 134.4 t |
| 25 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 155 | 1h 1m | 695 km | 1,858.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 154 | 1h 16m | 961 km | 2,552.6 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 150 | 1h 38m | 1,156 km | 2,992.4 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 148 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N118GM |  | Logan-Cache Airport (KLGU) | Cavok Ranch Airport (UT90) | 2026-07-07 15:33 UTC | 2026-07-07 16:00 UTC | 26m |
| ABK355 | ABK | Montréal (Mirabel) Airport (CYMX) | Montréal (Mirabel) Airport (CYMX) | 2026-07-07 13:50 UTC | 2026-07-07 15:54 UTC | 2h 3m |
| FIRE04 | FIR | Vila Real Airport (LPVR) | Braga Municipal Aerodrome (LPBR) | 2026-07-07 15:02 UTC | 2026-07-07 15:53 UTC | 51m |
| EJA505 | EJA | Westchester County Airport (KHPN) | KHTO (KHTO) | 2026-07-07 15:32 UTC | 2026-07-07 15:51 UTC | 19m |
|  |  | 19TE (19TE) | TA43 (TA43) | 2026-07-07 15:38 UTC | 2026-07-07 15:51 UTC | 12m |
| AAL1227 | American Airlines | Miami International Airport (KMIA) | Dallas-Fort Worth International Airport (KDFW) | 2026-07-07 13:16 UTC | 2026-07-07 15:48 UTC | 2h 31m |
| RNGR774 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Ingleside Regional Airport (KTFP) | 2026-07-07 15:21 UTC | 2026-07-07 15:47 UTC | 26m |
| OAL048 | OAL | Eleftherios Venizelos International Airport (LGAV) | Skiros Airport (LGSY) | 2026-07-07 15:19 UTC | 2026-07-07 15:45 UTC | 26m |
| N984GC |  | Seward Municipal Airport (KSWT) | 41NE (41NE) | 2026-07-07 15:25 UTC | 2026-07-07 15:44 UTC | 19m |
| AIB707 | AIB | Cardiff International Airport (EGFF) | Cardiff International Airport (EGFF) | 2026-07-07 15:06 UTC | 2026-07-07 15:38 UTC | 31m |
| JUMP14 | JUM | Bertani Ranch Airport (23TS) | Creekside Airport (03XS) | 2026-07-07 15:23 UTC | 2026-07-07 15:37 UTC | 14m |
| N686JA |  | Orlando Apopka Airport (KX04) | Orlando Apopka Airport (KX04) | 2026-07-07 15:32 UTC | 2026-07-07 15:36 UTC | 3m |
| N7232W |  | 19TE (19TE) | Flying Hare Field (34XS) | 2026-07-07 15:21 UTC | 2026-07-07 15:35 UTC | 14m |
| N3504P |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-07-07 15:22 UTC | 2026-07-07 15:35 UTC | 12m |
| ERU4 | ERU | Bagdad Airport (KE51) | Lake Havasu City Airport (KHII) | 2026-07-07 14:48 UTC | 2026-07-07 15:34 UTC | 45m |
| N383CJ |  | Wilmington International Airport (KILM) | Frederick Municipal Airport (KFDK) | 2026-07-07 14:30 UTC | 2026-07-07 15:31 UTC | 1h 0m |
| N77ZR |  | Creve Coeur Airport (K1H0) | Blackhawk Airport (6MO0) | 2026-07-07 15:13 UTC | 2026-07-07 15:24 UTC | 11m |
| N434DD |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-07-07 15:10 UTC | 2026-07-07 15:23 UTC | 12m |
| SCU33 | SCU | Jones Memorial Airport (K3F7) | Haskell Airport (K2K9) | 2026-07-07 14:09 UTC | 2026-07-07 15:21 UTC | 1h 11m |
| N735Z |  | Elizabeth City Cg Air Station/Regional Airport (KECG) | Atlantic City International Airport (KACY) | 2026-07-07 14:39 UTC | 2026-07-07 15:21 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
