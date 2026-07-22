# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--22_21:08:01_UTC-green)

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

**Latest saved flight:** 2026-07-22 21:08:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-22 21:08:01 UTC

- **144,625** saved flights
- **48,440** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **144,625** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,732,736.5 tonnes** estimated CO2 emissions
- **100,448,492 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5885 |
| 2 | SkyWest Airlines | 5292 |
| 3 | EJA | 2849 |
| 4 | IndiGo | 2623 |
| 5 | American Airlines | 2317 |
| 6 | Southwest Airlines | 2186 |
| 7 | ENY | 1798 |
| 8 | Delta Air Lines | 1718 |
| 9 | Lufthansa | 1444 |
| 10 | LATAM Airlines | 1326 |
| 11 | AZU | 1245 |
| 12 | WIF | 1237 |
| 13 | Vueling | 1236 |
| 14 | LXJ | 1113 |
| 15 | AXM | 1063 |
| 16 | Swiss International | 1029 |
| 17 | easyJet | 942 |
| 18 | All Nippon Airways | 922 |
| 19 | Alaska Airlines | 910 |
| 20 | QLK | 906 |
| 21 | EJU | 886 |
| 22 | VIV | 803 |
| 23 | CXK | 776 |
| 24 | AEE | 765 |
| 25 | JetBlue | 765 |
| 26 | Air France | 764 |
| 27 | MXY | 755 |
| 28 | United Airlines | 752 |
| 29 | Cathay Pacific | 748 |
| 30 | GLO | 740 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 124639 |
| 2 | 🇪🇸 ES | 9387 |
| 3 | 🇦🇺 AU | 8244 |
| 4 | 🇮🇳 IN | 8215 |
| 5 | 🇧🇷 BR | 8151 |
| 6 | 🇨🇦 CA | 7652 |
| 7 | 🇮🇹 IT | 7536 |
| 8 | 🇩🇪 DE | 7462 |
| 9 | 🇬🇧 GB | 6601 |
| 10 | 🇯🇵 JP | 6036 |
| 11 | 🇫🇷 FR | 5756 |
| 12 | 🇨🇴 CO | 4697 |
| 13 | 🇲🇽 MX | 4208 |
| 14 | 🇬🇷 GR | 4096 |
| 15 | 🇳🇴 NO | 3867 |
| 16 | 🇨🇭 CH | 3752 |
| 17 | 🇹🇷 TR | 3396 |
| 18 | 🇲🇾 MY | 2775 |
| 19 | 🇵🇱 PL | 2438 |
| 20 | 🇿🇦 ZA | 2350 |
| 21 | 🇳🇿 NZ | 2209 |
| 22 | 🇹🇭 TH | 2130 |
| 23 | 🇰🇷 KR | 2037 |
| 24 | 🇵🇭 PH | 1934 |
| 25 | 🇬🇹 GT | 1885 |
| 26 | 🇲🇦 MA | 1502 |
| 27 | 🇲🇪 ME | 1437 |
| 28 | 🇳🇱 NL | 1356 |
| 29 | 🇭🇷 HR | 1318 |
| 30 | 🇲🇴 MO | 1207 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2985 |
| 2 | Denver International Airport |  | US | 2427 |
| 3 | Tokyo International Airport |  | JP | 1942 |
| 4 | Indira Gandhi International Airport |  | IN | 1823 |
| 5 | Harry Reid International Airport |  | US | 1815 |
| 6 | Guaymaral Airport |  | CO | 1775 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1642 |
| 8 | Zurich Airport |  | CH | 1600 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1520 |
| 10 | La Aurora Airport |  | GT | 1460 |
| 11 | Frankfurt am Main International Airport |  | DE | 1391 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1367 |
| 13 | Chicago O'Hare International Airport |  | US | 1347 |
| 14 | Salt Lake City International Airport |  | US | 1297 |
| 15 | El Dorado International Airport |  | CO | 1283 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1262 |
| 17 | Macau International Airport |  | MO | 1207 |
| 18 | Capua Airport |  | IT | 1179 |
| 19 | Congonhas Airport |  | BR | 1157 |
| 20 | Madrid Barajas International Airport |  | ES | 1153 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1141 |
| 22 | Kuala Lumpur International Airport |  | MY | 1072 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1043 |
| 24 | Charlotte/Douglas International Airport |  | US | 1038 |
| 25 | Charles de Gaulle International Airport |  | FR | 1009 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1008 |
| 27 | Bengaluru International Airport |  | IN | 980 |
| 28 | Malpensa International Airport |  | IT | 936 |
| 29 | Ninoy Aquino International Airport |  | PH | 903 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 888 |
| 31 | Barcelona International Airport |  | ES | 879 |
| 32 | Daniel K Inouye International Airport |  | US | 876 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 862 |
| 34 | Tenerife Norte Airport |  | ES | 829 |
| 35 | Viracopos International Airport |  | BR | 822 |
| 36 | Seattle-Tacoma International Airport |  | US | 822 |
| 37 | Calgary International Airport |  | CA | 821 |
| 38 | Scottsdale Airport |  | US | 820 |
| 39 | Amsterdam Airport Schiphol |  | NL | 816 |
| 40 | Oslo Gardermoen Airport |  | NO | 795 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 748 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 525 | 21m | 244 km | 2,210.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 351 | 24m | 225 km | 1,361.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 350 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 340 | 1h 9m | 770 km | 4,516.6 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 261 | 26m | 275 km | 1,236.8 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 257 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 217 | 22m | 55 km | 206.3 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 194 | 26m | 215 km | 718.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 193 | 1h 46m | 1,423 km | 4,736.5 t |
| 16 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 193 | 44m | 241 km | 801.7 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 191 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 179 | 20m | 250 km | 773.2 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 179 | 28m | 152 km | 467.8 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 173 | 18m | 144 km | 430.3 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 168 | 44m | 452 km | 1,309.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 168 | 1h 16m | 961 km | 2,784.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 166 | 1h 1m | 695 km | 1,989.8 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 165 | 1h 39m | 1,156 km | 3,291.7 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 164 | 13m | - | - |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CUJAS25 | CUJ | Orleans-Bricy (BA 123) Air Base (LFOJ) | Orleans-Bricy (BA 123) Air Base (LFOJ) | 2026-07-22 20:46 UTC | 2026-07-22 21:08 UTC | 21m |
| MVK84 | MVK | Mankato Regional Airport (KMKT) | 6MN8 (6MN8) | 2026-07-22 20:49 UTC | 2026-07-22 21:07 UTC | 17m |
| N168BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-07-22 20:13 UTC | 2026-07-22 21:02 UTC | 49m |
| N814SS |  | Beluga Airport (PABG) | Kenai Municipal Airport (PAEN) | 2026-07-22 20:41 UTC | 2026-07-22 21:00 UTC | 19m |
| N844MK |  | Trenton Mercer Airport (KTTN) | Linden Airport (KLDJ) | 2026-07-22 20:04 UTC | 2026-07-22 20:59 UTC | 54m |
| N738XD |  | Chino Airport (KCNO) | Santa Barbara Municipal Airport (KSBA) | 2026-07-22 19:33 UTC | 2026-07-22 20:58 UTC | 1h 25m |
| N115GK |  | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-07-22 20:20 UTC | 2026-07-22 20:55 UTC | 35m |
| ENY3749 | ENY | Miami International Airport (KMIA) | FD82 (FD82) | 2026-07-22 19:41 UTC | 2026-07-22 20:53 UTC | 1h 12m |
| TKR132 | TKR | Coeur D'Alene/Pappy Boyington Field (KCOE) | Ferry County Airport (KR49) | 2026-07-22 20:25 UTC | 2026-07-22 20:48 UTC | 23m |
| CES214 | China Eastern | London Gatwick Airport (EGKK) | Kotlas Airport (ULKK) | 2026-07-22 17:21 UTC | 2026-07-22 20:45 UTC | 3h 23m |
| N7139D |  | Middleton Municipal/Morey Field (KC29) | Thiessen Field (34WI) | 2026-07-22 20:36 UTC | 2026-07-22 20:45 UTC | 8m |
| N347BG |  | Blevins Airport (7OI1) | Findlay Airport (KFDY) | 2026-07-22 20:05 UTC | 2026-07-22 20:43 UTC | 38m |
| N969YC |  | Laguardia Airport (KLGA) | Francis S Gabreski Airport (KFOK) | 2026-07-22 20:10 UTC | 2026-07-22 20:41 UTC | 31m |
| VAR450 | VAR | Phoenix Goodyear Airport (KGYR) | Bishop Airfield (1AZ0) | 2026-07-22 20:04 UTC | 2026-07-22 20:38 UTC | 33m |
| JIA5604 | JIA | Charlotte/Douglas International Airport (KCLT) | 93FD (93FD) | 2026-07-22 19:34 UTC | 2026-07-22 20:36 UTC | 1h 2m |
| N312PX |  | Chicago Executive Airport (KPWK) | Dubuque Regional Airport (KDBQ) | 2026-07-22 19:41 UTC | 2026-07-22 20:35 UTC | 53m |
| FXC44 | FXC | Bridgeport/Sikorsky Airport (KBDR) | Laguardia Airport (KLGA) | 2026-07-22 20:10 UTC | 2026-07-22 20:34 UTC | 24m |
| N5334D |  | Holmes County Airport (K10G) | Holmes County Airport (K10G) | 2026-07-22 19:47 UTC | 2026-07-22 20:32 UTC | 44m |
| N71FF |  | Montgomery-Gibbs Executive Airport (KMYF) | Gillespie Field (KSEE) | 2026-07-22 19:29 UTC | 2026-07-22 20:31 UTC | 1h 1m |
| N92KF |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-07-22 19:33 UTC | 2026-07-22 20:30 UTC | 56m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
