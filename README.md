# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_23:57:02_UTC-green)

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

**Latest saved flight:** 2026-08-02 23:57:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-02 23:57:02 UTC

- **168,068** saved flights
- **54,935** unique routes
- **139** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **168,068** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **2,026,340.9 tonnes** estimated CO2 emissions
- **117,469,038 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6701 |
| 2 | SkyWest Airlines | 6146 |
| 3 | EJA | 3346 |
| 4 | IndiGo | 2952 |
| 5 | American Airlines | 2654 |
| 6 | Southwest Airlines | 2648 |
| 7 | ENY | 2099 |
| 8 | Delta Air Lines | 2008 |
| 9 | LATAM Airlines | 1560 |
| 10 | Lufthansa | 1543 |
| 11 | AZU | 1481 |
| 12 | WIF | 1401 |
| 13 | Vueling | 1383 |
| 14 | LXJ | 1318 |
| 15 | AXM | 1156 |
| 16 | Swiss International | 1151 |
| 17 | easyJet | 1130 |
| 18 | EJU | 1033 |
| 19 | Alaska Airlines | 1029 |
| 20 | QLK | 1022 |
| 21 | All Nippon Airways | 1018 |
| 22 | VIV | 925 |
| 23 | Cathay Pacific | 897 |
| 24 | CXK | 892 |
| 25 | United Airlines | 889 |
| 26 | GLO | 882 |
| 27 | AEE | 880 |
| 28 | Air France | 865 |
| 29 | MXY | 864 |
| 30 | JetBlue | 849 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 145044 |
| 2 | 🇪🇸 ES | 10763 |
| 3 | 🇧🇷 BR | 9577 |
| 4 | 🇦🇺 AU | 9370 |
| 5 | 🇮🇳 IN | 9256 |
| 6 | 🇨🇦 CA | 9114 |
| 7 | 🇮🇹 IT | 8675 |
| 8 | 🇩🇪 DE | 8369 |
| 9 | 🇬🇧 GB | 7805 |
| 10 | 🇯🇵 JP | 6747 |
| 11 | 🇫🇷 FR | 6660 |
| 12 | 🇨🇴 CO | 6058 |
| 13 | 🇬🇷 GR | 4881 |
| 14 | 🇲🇽 MX | 4808 |
| 15 | 🇨🇭 CH | 4417 |
| 16 | 🇳🇴 NO | 4385 |
| 17 | 🇹🇷 TR | 4061 |
| 18 | 🇲🇾 MY | 3013 |
| 19 | 🇵🇱 PL | 2831 |
| 20 | 🇿🇦 ZA | 2723 |
| 21 | 🇳🇿 NZ | 2446 |
| 22 | 🇹🇭 TH | 2424 |
| 23 | 🇵🇭 PH | 2225 |
| 24 | 🇬🇹 GT | 2176 |
| 25 | 🇰🇷 KR | 2149 |
| 26 | 🇲🇦 MA | 1703 |
| 27 | 🇭🇷 HR | 1608 |
| 28 | 🇲🇪 ME | 1553 |
| 29 | 🇳🇱 NL | 1527 |
| 30 | 🇲🇴 MO | 1426 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3457 |
| 2 | Denver International Airport |  | US | 2799 |
| 3 | Tokyo International Airport |  | JP | 2120 |
| 4 | Guaymaral Airport |  | CO | 2094 |
| 5 | Indira Gandhi International Airport |  | IN | 2050 |
| 6 | Harry Reid International Airport |  | US | 2025 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1841 |
| 8 | Zurich Airport |  | CH | 1786 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1769 |
| 10 | La Aurora Airport |  | GT | 1681 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1551 |
| 12 | Chicago O'Hare International Airport |  | US | 1525 |
| 13 | El Dorado International Airport |  | CO | 1524 |
| 14 | Frankfurt am Main International Airport |  | DE | 1511 |
| 15 | Salt Lake City International Airport |  | US | 1506 |
| 16 | Macau International Airport |  | MO | 1426 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1393 |
| 18 | Congonhas Airport |  | BR | 1380 |
| 19 | Madrid Barajas International Airport |  | ES | 1325 |
| 20 | Capua Airport |  | IT | 1307 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1279 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1187 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1177 |
| 24 | Charlotte/Douglas International Airport |  | US | 1171 |
| 25 | Charles de Gaulle International Airport |  | FR | 1144 |
| 26 | Kuala Lumpur International Airport |  | MY | 1137 |
| 27 | Malpensa International Airport |  | IT | 1129 |
| 28 | Bengaluru International Airport |  | IN | 1096 |
| 29 | Ninoy Aquino International Airport |  | PH | 1046 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1039 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1032 |
| 32 | Barcelona International Airport |  | ES | 991 |
| 33 | Daniel K Inouye International Airport |  | US | 978 |
| 34 | Seattle-Tacoma International Airport |  | US | 977 |
| 35 | Viracopos International Airport |  | BR | 960 |
| 36 | Calgary International Airport |  | CA | 952 |
| 37 | Tenerife Norte Airport |  | ES | 938 |
| 38 | Reno/Tahoe International Airport |  | US | 935 |
| 39 | Oslo Gardermoen Airport |  | NO | 932 |
| 40 | Scottsdale Airport |  | US | 932 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 871 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 611 | 21m | 244 km | 2,572.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 402 | 24m | 225 km | 1,559.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 402 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 381 | 1h 9m | 770 km | 5,061.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 316 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 288 | 27m | 275 km | 1,364.7 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 245 | 19m | 165 km | 696.9 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 244 | 44m | 241 km | 1,013.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 231 | 1h 47m | 1,423 km | 5,669.1 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 221 | 20m | 250 km | 954.6 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 218 | 26m | 215 km | 807.4 t |
| 18 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 215 | 31m | 49 km | 181.7 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 211 | 20m | 99 km | 361.4 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 210 | 13m | - | - |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 199 | 19m | 144 km | 495.0 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 198 | 1h 15m | 961 km | 3,282.0 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 196 | 31m | 369 km | 1,247.6 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 196 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 195 | 50m | 556 km | 1,869.2 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 187 | 1h 38m | 1,156 km | 3,730.6 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 184 | 24m | 218 km | 693.2 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 183 | 1h 1m | 695 km | 2,193.6 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 182 | 44m | 452 km | 1,418.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UAL2437 | United Airlines | Chicago O'Hare International Airport (KORD) | Washington Dulles International Airport (KIAD) | 2026-08-02 22:33 UTC | 2026-08-02 23:57 UTC | 1h 23m |
| UAL925 | United Airlines | London Heathrow Airport (EGLL) | Washington Dulles International Airport (KIAD) | 2026-08-02 16:25 UTC | 2026-08-02 23:56 UTC | 7h 30m |
| N915CM |  | Hayward Executive Airport (KHWD) | Hayward Executive Airport (KHWD) | 2026-08-02 23:06 UTC | 2026-08-02 23:53 UTC | 46m |
| N814SS |  | Beluga Airport (PABG) | Kenai Municipal Airport (PAEN) | 2026-08-02 23:27 UTC | 2026-08-02 23:51 UTC | 24m |
| N212AE |  | Kodiak Airport (PADQ) | Kodiak Municipal Airport (PAKD) | 2026-08-02 23:39 UTC | 2026-08-02 23:43 UTC | 3m |
| NYV | NYV | RAAF Williams Point Cook Base (YMPC) | Melbourne Moorabbin Airport (YMMB) | 2026-08-02 23:27 UTC | 2026-08-02 23:41 UTC | 13m |
| N359DG |  | Visalia Municipal Airport (KVIS) | Lake Tahoe Airport (KTVL) | 2026-08-02 23:06 UTC | 2026-08-02 23:41 UTC | 34m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-02 23:26 UTC | 2026-08-02 23:40 UTC | 13m |
| CATS73 | CAT | Osan Air Base (RKSO) | Osan Air Base (RKSO) | 2026-08-02 23:24 UTC | 2026-08-02 23:39 UTC | 15m |
| NVD | NVD | RAAF Williams Point Cook Base (YMPC) | Melbourne Moorabbin Airport (YMMB) | 2026-08-02 23:24 UTC | 2026-08-02 23:38 UTC | 14m |
| TIBGC | TIB | Juan Santamaria International Airport (MROC) | Quepos Managua Airport (MRQP) | 2026-08-02 23:22 UTC | 2026-08-02 23:37 UTC | 14m |
| N651PA |  | Purdue University Airport (KLAF) | De Ford Airport (4II0) | 2026-08-02 22:34 UTC | 2026-08-02 23:35 UTC | 1h 1m |
| RQM | RQM | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-08-02 23:02 UTC | 2026-08-02 23:33 UTC | 31m |
| TKR15 | TKR | Hill Afb Airport (KHIF) | Nephi Municipal Airport (KU14) | 2026-08-02 23:10 UTC | 2026-08-02 23:30 UTC | 20m |
| N251SF |  | Dupage Airport (KDPA) | Aero Lake Estates Airport (30IS) | 2026-08-02 23:06 UTC | 2026-08-02 23:29 UTC | 23m |
| N378TP |  | Bob Hope Airport (KBUR) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-08-02 19:54 UTC | 2026-08-02 23:29 UTC | 3h 34m |
| N166SA |  | Parker Field (AL18) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-02 22:01 UTC | 2026-08-02 23:27 UTC | 1h 25m |
| N829CB |  | Gaines County Airport (KGNC) | Central Colorado Regional Airport (KAEJ) | 2026-08-02 22:04 UTC | 2026-08-02 23:20 UTC | 1h 16m |
| N928JJ |  | Napa County Airport (KAPC) | Truckee-Tahoe Airport (KTRK) | 2026-08-02 22:57 UTC | 2026-08-02 23:19 UTC | 21m |
| N345RF |  | Watertown Municipal Airport (KRYV) | Kalkaska City Airport (KY89) | 2026-08-02 22:27 UTC | 2026-08-02 23:13 UTC | 45m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
