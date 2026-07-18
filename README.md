# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--18_23:12:51_UTC-green)

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

**Latest saved flight:** 2026-07-18 23:12:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-18 23:12:51 UTC

- **142,495** saved flights
- **47,788** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **142,495** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,709,575.7 tonnes** estimated CO2 emissions
- **99,105,839 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5799 |
| 2 | SkyWest Airlines | 5204 |
| 3 | EJA | 2804 |
| 4 | IndiGo | 2599 |
| 5 | American Airlines | 2275 |
| 6 | Southwest Airlines | 2146 |
| 7 | ENY | 1765 |
| 8 | Delta Air Lines | 1686 |
| 9 | Lufthansa | 1435 |
| 10 | LATAM Airlines | 1313 |
| 11 | AZU | 1227 |
| 12 | Vueling | 1224 |
| 13 | WIF | 1219 |
| 14 | LXJ | 1094 |
| 15 | AXM | 1055 |
| 16 | Swiss International | 1014 |
| 17 | easyJet | 927 |
| 18 | All Nippon Airways | 913 |
| 19 | Alaska Airlines | 898 |
| 20 | QLK | 894 |
| 21 | EJU | 878 |
| 22 | VIV | 791 |
| 23 | AEE | 762 |
| 24 | CXK | 762 |
| 25 | JetBlue | 760 |
| 26 | Air France | 759 |
| 27 | United Airlines | 742 |
| 28 | MXY | 740 |
| 29 | Cathay Pacific | 736 |
| 30 | GLO | 730 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 122503 |
| 2 | 🇪🇸 ES | 9297 |
| 3 | 🇦🇺 AU | 8160 |
| 4 | 🇮🇳 IN | 8141 |
| 5 | 🇧🇷 BR | 8051 |
| 6 | 🇨🇦 CA | 7505 |
| 7 | 🇮🇹 IT | 7430 |
| 8 | 🇩🇪 DE | 7388 |
| 9 | 🇬🇧 GB | 6522 |
| 10 | 🇯🇵 JP | 5974 |
| 11 | 🇫🇷 FR | 5668 |
| 12 | 🇨🇴 CO | 4563 |
| 13 | 🇲🇽 MX | 4135 |
| 14 | 🇬🇷 GR | 4058 |
| 15 | 🇳🇴 NO | 3817 |
| 16 | 🇨🇭 CH | 3688 |
| 17 | 🇹🇷 TR | 3371 |
| 18 | 🇲🇾 MY | 2751 |
| 19 | 🇵🇱 PL | 2396 |
| 20 | 🇿🇦 ZA | 2326 |
| 21 | 🇳🇿 NZ | 2186 |
| 22 | 🇹🇭 TH | 2127 |
| 23 | 🇰🇷 KR | 2027 |
| 24 | 🇵🇭 PH | 1928 |
| 25 | 🇬🇹 GT | 1873 |
| 26 | 🇲🇦 MA | 1490 |
| 27 | 🇲🇪 ME | 1411 |
| 28 | 🇳🇱 NL | 1344 |
| 29 | 🇭🇷 HR | 1299 |
| 30 | 🇲🇴 MO | 1193 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2933 |
| 2 | Denver International Airport |  | US | 2382 |
| 3 | Tokyo International Airport |  | JP | 1928 |
| 4 | Indira Gandhi International Airport |  | IN | 1804 |
| 5 | Harry Reid International Airport |  | US | 1787 |
| 6 | Guaymaral Airport |  | CO | 1736 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1634 |
| 8 | Zurich Airport |  | CH | 1585 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1493 |
| 10 | La Aurora Airport |  | GT | 1449 |
| 11 | Frankfurt am Main International Airport |  | DE | 1385 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1349 |
| 13 | Chicago O'Hare International Airport |  | US | 1331 |
| 14 | Salt Lake City International Airport |  | US | 1274 |
| 15 | El Dorado International Airport |  | CO | 1260 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1255 |
| 17 | Macau International Airport |  | MO | 1193 |
| 18 | Capua Airport |  | IT | 1166 |
| 19 | Madrid Barajas International Airport |  | ES | 1146 |
| 20 | Congonhas Airport |  | BR | 1143 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1130 |
| 22 | Kuala Lumpur International Airport |  | MY | 1062 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1034 |
| 24 | Charlotte/Douglas International Airport |  | US | 1029 |
| 25 | Charles de Gaulle International Airport |  | FR | 1004 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 996 |
| 27 | Bengaluru International Airport |  | IN | 972 |
| 28 | Malpensa International Airport |  | IT | 921 |
| 29 | Ninoy Aquino International Airport |  | PH | 900 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 874 |
| 31 | Daniel K Inouye International Airport |  | US | 868 |
| 32 | Barcelona International Airport |  | ES | 868 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 841 |
| 34 | Tenerife Norte Airport |  | ES | 824 |
| 35 | Calgary International Airport |  | CA | 813 |
| 36 | Seattle-Tacoma International Airport |  | US | 810 |
| 37 | Viracopos International Airport |  | BR | 809 |
| 38 | Amsterdam Airport Schiphol |  | NL | 807 |
| 39 | Scottsdale Airport |  | US | 803 |
| 40 | Vitoria/Foronda Airport |  | ES | 784 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 731 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 518 | 21m | 244 km | 2,181.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 349 | 24m | 225 km | 1,354.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 346 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 338 | 1h 9m | 770 km | 4,490.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 259 | 26m | 275 km | 1,227.3 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 210 | 22m | 55 km | 199.6 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 192 | 1h 46m | 1,423 km | 4,712.0 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 191 | 26m | 215 km | 707.4 t |
| 16 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 190 | 44m | 241 km | 789.2 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 189 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 178 | 28m | 152 km | 465.2 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 177 | 20m | 250 km | 764.5 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 172 | 18m | 144 km | 427.8 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 167 | 44m | 452 km | 1,301.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 165 | 1h 1m | 695 km | 1,977.9 t |
| 26 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 164 | 1h 16m | 961 km | 2,718.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 163 | 1h 38m | 1,156 km | 3,251.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 162 | 13m | - | - |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 156 | 14m | 154 km | 413.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RSCU204 | RSC | Sydney Bankstown Airport (YSBK) | YSMB (YSMB) | 2026-07-18 22:28 UTC | 2026-07-18 23:12 UTC | 44m |
| QFA6132 | Qantas | Avalon Airport (YMAV) | Avalon Airport (YMAV) | 2026-07-18 22:54 UTC | 2026-07-18 23:06 UTC | 11m |
| N2666U |  | Decatur Municipal Airport (KLUD) | Vance Field (TE76) | 2026-07-18 22:25 UTC | 2026-07-18 22:56 UTC | 30m |
| SD1 |  | 52TA (52TA) | Tri-County Aerodrome (48TX) | 2026-07-18 22:33 UTC | 2026-07-18 22:48 UTC | 15m |
| JIA5030 | JIA | Charlotte/Douglas International Airport (KCLT) | Toronto Pearson International Airport (CYYZ) | 2026-07-18 20:57 UTC | 2026-07-18 22:45 UTC | 1h 48m |
| RFS729 | RFS | Boeing Field/King County International Airport (KBFI) | Renton Municipal Airport (KRNT) | 2026-07-18 22:07 UTC | 2026-07-18 22:42 UTC | 35m |
| TKR132 | TKR | Coeur D'Alene/Pappy Boyington Field (KCOE) | Coeur D'Alene/Pappy Boyington Field (KCOE) | 2026-07-18 21:50 UTC | 2026-07-18 22:39 UTC | 49m |
| JA139R |  | Shizuhama Airport (RJNY) | Mt. Fuji Shizuoka Airport (RJNS) | 2026-07-18 22:25 UTC | 2026-07-18 22:39 UTC | 13m |
| TKR103 | TKR | Rogue Valley International/Medford Airport (KMFR) | Southfork Airport (23ID) | 2026-07-18 21:37 UTC | 2026-07-18 22:37 UTC | 59m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-07-18 22:21 UTC | 2026-07-18 22:37 UTC | 15m |
| CFMPF | CFM | Prince George Airport (CYXS) | Boundary Bay Airport (CZBB) | 2026-07-18 18:54 UTC | 2026-07-18 22:35 UTC | 3h 40m |
| N625MC |  | Powell River Airport (CYPW) | Boeing Field/King County International Airport (KBFI) | 2026-07-18 21:52 UTC | 2026-07-18 22:34 UTC | 41m |
| TIBKY | TIB | Tambor Airport (MRTR) | Juan Santamaria International Airport (MROC) | 2026-07-18 22:05 UTC | 2026-07-18 22:32 UTC | 26m |
| EJA871 | EJA | Beverly Regional Airport (KBVY) | Lincoln Airport (KLNK) | 2026-07-18 19:31 UTC | 2026-07-18 22:32 UTC | 3h 1m |
| N211U |  | Waco Regional Airport (KACT) | Easterwood Field (KCLL) | 2026-07-18 21:29 UTC | 2026-07-18 22:31 UTC | 1h 1m |
| N835CB |  | Roberts Field (KRDM) | Santa Fe Regional Airport (KSAF) | 2026-07-18 19:58 UTC | 2026-07-18 22:28 UTC | 2h 30m |
| N251PA |  | Falcon Field (KFFZ) | 99AZ (99AZ) | 2026-07-18 21:24 UTC | 2026-07-18 22:26 UTC | 1h 2m |
| SKW344H | SkyWest Airlines | Denver International Airport (KDEN) | TX20 (TX20) | 2026-07-18 21:14 UTC | 2026-07-18 22:26 UTC | 1h 12m |
| AAL779 | American Airlines | Harry Reid International Airport (KLAS) | Philadelphia International Airport (KPHL) | 2026-07-18 17:43 UTC | 2026-07-18 22:26 UTC | 4h 43m |
| JZA7918 | JZA | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Scottsfield Airpark (CCF9) | 2026-07-18 21:44 UTC | 2026-07-18 22:24 UTC | 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
