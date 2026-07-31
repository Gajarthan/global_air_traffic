# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_16:13:37_UTC-green)

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

**Latest saved flight:** 2026-07-31 16:13:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-31 16:13:37 UTC

- **162,669** saved flights
- **53,611** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **162,669** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,951,239.4 tonnes** estimated CO2 emissions
- **113,115,325 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6493 |
| 2 | SkyWest Airlines | 5918 |
| 3 | EJA | 3219 |
| 4 | IndiGo | 2857 |
| 5 | American Airlines | 2565 |
| 6 | Southwest Airlines | 2541 |
| 7 | ENY | 2020 |
| 8 | Delta Air Lines | 1933 |
| 9 | Lufthansa | 1528 |
| 10 | LATAM Airlines | 1527 |
| 11 | AZU | 1428 |
| 12 | WIF | 1372 |
| 13 | Vueling | 1350 |
| 14 | LXJ | 1264 |
| 15 | AXM | 1131 |
| 16 | Swiss International | 1122 |
| 17 | easyJet | 1070 |
| 18 | Alaska Airlines | 1007 |
| 19 | QLK | 1003 |
| 20 | EJU | 1000 |
| 21 | All Nippon Airways | 999 |
| 22 | VIV | 896 |
| 23 | CXK | 868 |
| 24 | Cathay Pacific | 857 |
| 25 | United Airlines | 856 |
| 26 | GLO | 853 |
| 27 | AEE | 851 |
| 28 | Air France | 841 |
| 29 | MXY | 841 |
| 30 | JetBlue | 828 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 140380 |
| 2 | 🇪🇸 ES | 10426 |
| 3 | 🇧🇷 BR | 9293 |
| 4 | 🇦🇺 AU | 9200 |
| 5 | 🇮🇳 IN | 8980 |
| 6 | 🇨🇦 CA | 8843 |
| 7 | 🇮🇹 IT | 8382 |
| 8 | 🇩🇪 DE | 8196 |
| 9 | 🇬🇧 GB | 7481 |
| 10 | 🇯🇵 JP | 6587 |
| 11 | 🇫🇷 FR | 6436 |
| 12 | 🇨🇴 CO | 5799 |
| 13 | 🇬🇷 GR | 4670 |
| 14 | 🇲🇽 MX | 4662 |
| 15 | 🇳🇴 NO | 4293 |
| 16 | 🇨🇭 CH | 4282 |
| 17 | 🇹🇷 TR | 3888 |
| 18 | 🇲🇾 MY | 2938 |
| 19 | 🇵🇱 PL | 2767 |
| 20 | 🇿🇦 ZA | 2647 |
| 21 | 🇳🇿 NZ | 2383 |
| 22 | 🇹🇭 TH | 2316 |
| 23 | 🇵🇭 PH | 2134 |
| 24 | 🇰🇷 KR | 2119 |
| 25 | 🇬🇹 GT | 2090 |
| 26 | 🇲🇦 MA | 1637 |
| 27 | 🇲🇪 ME | 1533 |
| 28 | 🇭🇷 HR | 1526 |
| 29 | 🇳🇱 NL | 1485 |
| 30 | 🇲🇴 MO | 1361 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3315 |
| 2 | Denver International Airport |  | US | 2701 |
| 3 | Tokyo International Airport |  | JP | 2076 |
| 4 | Guaymaral Airport |  | CO | 2049 |
| 5 | Indira Gandhi International Airport |  | IN | 1994 |
| 6 | Harry Reid International Airport |  | US | 1971 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1793 |
| 8 | Zurich Airport |  | CH | 1741 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1709 |
| 10 | La Aurora Airport |  | GT | 1621 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1509 |
| 12 | El Dorado International Airport |  | CO | 1487 |
| 13 | Frankfurt am Main International Airport |  | DE | 1483 |
| 14 | Chicago O'Hare International Airport |  | US | 1468 |
| 15 | Salt Lake City International Airport |  | US | 1458 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1363 |
| 17 | Macau International Airport |  | MO | 1361 |
| 18 | Congonhas Airport |  | BR | 1348 |
| 19 | Madrid Barajas International Airport |  | ES | 1283 |
| 20 | Capua Airport |  | IT | 1276 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1241 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1157 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1153 |
| 24 | Charlotte/Douglas International Airport |  | US | 1141 |
| 25 | Kuala Lumpur International Airport |  | MY | 1118 |
| 26 | Charles de Gaulle International Airport |  | FR | 1109 |
| 27 | Malpensa International Airport |  | IT | 1075 |
| 28 | Bengaluru International Airport |  | IN | 1065 |
| 29 | Ninoy Aquino International Airport |  | PH | 1002 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 996 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 986 |
| 32 | Barcelona International Airport |  | ES | 963 |
| 33 | Daniel K Inouye International Airport |  | US | 953 |
| 34 | Seattle-Tacoma International Airport |  | US | 942 |
| 35 | Calgary International Airport |  | CA | 928 |
| 36 | Viracopos International Airport |  | BR | 926 |
| 37 | Tenerife Norte Airport |  | ES | 912 |
| 38 | Scottsdale Airport |  | US | 911 |
| 39 | Oslo Gardermoen Airport |  | NO | 908 |
| 40 | Reno/Tahoe International Airport |  | US | 890 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 859 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 591 | 21m | 244 km | 2,488.5 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 388 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 387 | 24m | 225 km | 1,501.4 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 373 | 1h 9m | 770 km | 4,955.0 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 302 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 284 | 27m | 275 km | 1,345.8 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 240 | 19m | 165 km | 682.7 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 240 | 22m | 55 km | 228.1 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 236 | 44m | 241 km | 980.3 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 223 | 1h 47m | 1,423 km | 5,472.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 213 | 26m | 215 km | 788.9 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 206 | 13m | - | - |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 206 | 20m | 250 km | 889.8 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 206 | 20m | 99 km | 352.9 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 198 | 30m | 49 km | 167.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 194 | 1h 15m | 961 km | 3,215.7 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 194 | 28m | 152 km | 507.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 191 | 18m | 144 km | 475.1 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 190 | 31m | 369 km | 1,209.4 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 187 | 50m | 556 km | 1,792.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 182 | 1h 39m | 1,156 km | 3,630.8 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 181 | 1h 1m | 695 km | 2,169.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 179 | 44m | 452 km | 1,395.0 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 174 | 1h 49m | 1,304 km | 3,914.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6367Q |  | Tracy Municipal Airport (KTCY) | Tracy Municipal Airport (KTCY) | 2026-07-31 15:33 UTC | 2026-07-31 16:13 UTC | 40m |
| N140UD |  | Salisbury-Ocean City Wicomico Regional Airport (KSBY) | Salisbury-Ocean City Wicomico Regional Airport (KSBY) | 2026-07-31 15:33 UTC | 2026-07-31 16:12 UTC | 39m |
| RVP953 | RVP | Cascais Airport (LPCS) | Portimão Airport (LPPM) | 2026-07-31 15:34 UTC | 2026-07-31 16:12 UTC | 38m |
| DELSL | DEL | Frankfurt-Egelsbach Airport (EDFE) | Baden-Oos Airport (EDTB) | 2026-07-31 15:36 UTC | 2026-07-31 16:12 UTC | 36m |
| SHINR29 | SHI | Austin-Bergstrom International Airport (KAUS) | Giddings-Lee County Airport (KGYB) | 2026-07-31 15:35 UTC | 2026-07-31 16:12 UTC | 36m |
| ECOCE | ECO | Torrejon Airport (LETO) | Torrejon Airport (LETO) | 2026-07-31 15:49 UTC | 2026-07-31 16:02 UTC | 12m |
| N734M |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-07-31 15:27 UTC | 2026-07-31 16:01 UTC | 34m |
| N750VX |  | K3A1 (K3A1) | K3A1 (K3A1) | 2026-07-31 15:38 UTC | 2026-07-31 15:59 UTC | 21m |
| HBZVX | HBZ | Locarno Airport (LSZL) | Locarno Airport (LSZL) | 2026-07-31 15:32 UTC | 2026-07-31 15:56 UTC | 24m |
| N65716 |  | Central Jersey Regional Airport (K47N) | Solberg/Hunterdon Airport (KN51) | 2026-07-31 15:40 UTC | 2026-07-31 15:53 UTC | 13m |
| HLF9816 | HLF | Charles de Gaulle International Airport (LFPG) | Pushkin Airport (ULLP) | 2026-07-29 11:05 UTC | 2026-07-31 15:52 UTC | 52h 46m |
| N58AY |  | Doylestown Airport (KDYL) | Lehigh Valley International Airport (KABE) | 2026-07-31 14:56 UTC | 2026-07-31 15:49 UTC | 52m |
| N1031V |  | Durango-La Plata County Airport (KDRO) | Navajo Lake Airport (K1V0) | 2026-07-31 15:11 UTC | 2026-07-31 15:47 UTC | 35m |
| EFC52H | EFC | Al Maktoum International Airport (OMDW) | Ras Al Khaimah International Airport (OMRK) | 2026-07-31 15:05 UTC | 2026-07-31 15:46 UTC | 41m |
| CAP3139 | CAP | Riveredge Airpark (19NK) | Oswego County Airport (KFZY) | 2026-07-31 15:23 UTC | 2026-07-31 15:44 UTC | 21m |
| N910DP |  | Phoenix Sky Harbor International Airport (KPHX) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-07-31 14:19 UTC | 2026-07-31 15:40 UTC | 1h 20m |
| PXT680 | PXT | Oakland San Francisco Bay Airport (KOAK) | Buchanan Field (KCCR) | 2026-07-31 15:28 UTC | 2026-07-31 15:40 UTC | 11m |
| N396FS |  | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-07-31 15:15 UTC | 2026-07-31 15:40 UTC | 24m |
| N219RB |  | Cottonwood Farm Airport (87VA) | Atlanta Municipal Airport (KY93) | 2026-07-31 14:21 UTC | 2026-07-31 15:36 UTC | 1h 14m |
| CGJDI | CGJ | Saint John Airport (CYSJ) | St-Quentin Airport (CDC4) | 2026-07-31 15:02 UTC | 2026-07-31 15:34 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
