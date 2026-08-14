# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_20:27:39_UTC-green)

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

**Latest saved flight:** 2026-08-14 20:27:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-14 20:27:39 UTC

- **196,566** saved flights
- **61,707** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **196,566** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,347,313.9 tonnes** estimated CO2 emissions
- **136,076,165 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7812 |
| 2 | SkyWest Airlines | 7067 |
| 3 | EJA | 3873 |
| 4 | IndiGo | 3387 |
| 5 | Southwest Airlines | 3048 |
| 6 | American Airlines | 3040 |
| 7 | ENY | 2429 |
| 8 | Delta Air Lines | 2321 |
| 9 | LATAM Airlines | 1841 |
| 10 | AZU | 1775 |
| 11 | Lufthansa | 1696 |
| 12 | Vueling | 1642 |
| 13 | WIF | 1628 |
| 14 | LXJ | 1558 |
| 15 | easyJet | 1352 |
| 16 | Swiss International | 1328 |
| 17 | AXM | 1277 |
| 18 | EJU | 1217 |
| 19 | QLK | 1208 |
| 20 | All Nippon Airways | 1184 |
| 21 | Alaska Airlines | 1163 |
| 22 | VIV | 1082 |
| 23 | GLO | 1057 |
| 24 | Air France | 1034 |
| 25 | PGT | 1024 |
| 26 | AEE | 1010 |
| 27 | CXK | 1005 |
| 28 | United Airlines | 1004 |
| 29 | WMT | 985 |
| 30 | Wizz Air | 974 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 167166 |
| 2 | 🇪🇸 ES | 12702 |
| 3 | 🇧🇷 BR | 11288 |
| 4 | 🇦🇺 AU | 11009 |
| 5 | 🇨🇦 CA | 10765 |
| 6 | 🇮🇳 IN | 10589 |
| 7 | 🇮🇹 IT | 10245 |
| 8 | 🇩🇪 DE | 9766 |
| 9 | 🇬🇧 GB | 9239 |
| 10 | 🇯🇵 JP | 7984 |
| 11 | 🇫🇷 FR | 7835 |
| 12 | 🇨🇴 CO | 7714 |
| 13 | 🇬🇷 GR | 5780 |
| 14 | 🇲🇽 MX | 5558 |
| 15 | 🇹🇷 TR | 5357 |
| 16 | 🇨🇭 CH | 5314 |
| 17 | 🇳🇴 NO | 5040 |
| 18 | 🇲🇾 MY | 3342 |
| 19 | 🇿🇦 ZA | 3320 |
| 20 | 🇵🇱 PL | 3246 |
| 21 | 🇹🇭 TH | 3032 |
| 22 | 🇳🇿 NZ | 2739 |
| 23 | 🇵🇭 PH | 2589 |
| 24 | 🇬🇹 GT | 2509 |
| 25 | 🇰🇷 KR | 2383 |
| 26 | 🇭🇷 HR | 2056 |
| 27 | 🇲🇦 MA | 1988 |
| 28 | 🇳🇱 NL | 1769 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1584 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4089 |
| 2 | Denver International Airport |  | US | 3208 |
| 3 | Tokyo International Airport |  | JP | 2449 |
| 4 | Guaymaral Airport |  | CO | 2438 |
| 5 | Indira Gandhi International Airport |  | IN | 2392 |
| 6 | Harry Reid International Airport |  | US | 2260 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2078 |
| 8 | Zurich Airport |  | CH | 2078 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2033 |
| 10 | La Aurora Airport |  | GT | 1923 |
| 11 | El Dorado International Airport |  | CO | 1794 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1757 |
| 13 | Salt Lake City International Airport |  | US | 1746 |
| 14 | Chicago O'Hare International Airport |  | US | 1716 |
| 15 | Frankfurt am Main International Airport |  | DE | 1662 |
| 16 | Congonhas Airport |  | BR | 1643 |
| 17 | Madrid Barajas International Airport |  | ES | 1547 |
| 18 | Macau International Airport |  | MO | 1531 |
| 19 | Capua Airport |  | IT | 1503 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1498 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1451 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1413 |
| 23 | Malpensa International Airport |  | IT | 1364 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1362 |
| 25 | Charles de Gaulle International Airport |  | FR | 1350 |
| 26 | Charlotte/Douglas International Airport |  | US | 1302 |
| 27 | Kuala Lumpur International Airport |  | MY | 1246 |
| 28 | Bengaluru International Airport |  | IN | 1244 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1227 |
| 30 | Ninoy Aquino International Airport |  | PH | 1224 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1203 |
| 32 | Barcelona International Airport |  | ES | 1181 |
| 33 | Viracopos International Airport |  | BR | 1141 |
| 34 | Seattle-Tacoma International Airport |  | US | 1127 |
| 35 | Calgary International Airport |  | CA | 1117 |
| 36 | Reno/Tahoe International Airport |  | US | 1113 |
| 37 | Oslo Gardermoen Airport |  | NO | 1109 |
| 38 | Daniel K Inouye International Airport |  | US | 1092 |
| 39 | Vitoria/Foronda Airport |  | ES | 1081 |
| 40 | Tenerife Norte Airport |  | ES | 1076 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1006 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 720 | 21m | 244 km | 3,031.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 474 | 1h 7m | 770 km | 6,296.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 458 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 453 | 24m | 225 km | 1,757.4 t |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 341 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 337 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 330 | 27m | 275 km | 1,563.7 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 304 | 1h 7m | 706 km | 3,701.2 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 297 | 44m | 241 km | 1,233.7 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 284 | 1h 49m | 1,423 km | 6,969.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 280 | 22m | 55 km | 266.1 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 261 | 21m | 250 km | 1,127.4 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 245 | 26m | 215 km | 907.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 242 | 24m | 218 km | 911.7 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 239 | 1h 15m | 961 km | 3,961.6 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 239 | 19m | 99 km | 409.4 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 237 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 232 | 1h 38m | 1,156 km | 4,628.3 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 231 | 19m | 144 km | 574.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 222 | 31m | 369 km | 1,413.1 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 214 | 28m | 152 km | 559.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 213 | 1h 3m | 695 km | 2,553.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TOM7WL | TOM | Palma De Mallorca Airport (LEPA) | London Gatwick Airport (EGKK) | 2026-08-14 18:33 UTC | 2026-08-14 20:27 UTC | 1h 54m |
| TKR103 | TKR | Chico Regional Airport (KCIC) | Hayfork Airport (KF62) | 2026-08-14 20:09 UTC | 2026-08-14 20:23 UTC | 13m |
| PAT820 | PAT | Sacramento Mather Airport (KMHR) | Reno/Tahoe International Airport (KRNO) | 2026-08-14 19:47 UTC | 2026-08-14 20:18 UTC | 30m |
| N11TE |  | Destin Executive Airport (KDTS) | Nashville International Airport (KBNA) | 2026-08-14 19:01 UTC | 2026-08-14 20:16 UTC | 1h 14m |
| N1882S |  | Van Nuys Airport (KVNY) | Riverside Airport (KRAL) | 2026-08-14 19:33 UTC | 2026-08-14 20:15 UTC | 42m |
| GFY1124 | GFY | Portland-Hillsboro Airport (KHIO) | Portland-Hillsboro Airport (KHIO) | 2026-08-14 19:25 UTC | 2026-08-14 20:15 UTC | 50m |
| IGO071 | IndiGo | Indira Gandhi International Airport (VIDP) | Shaibah Airport (OESB) | 2026-08-14 17:01 UTC | 2026-08-14 20:12 UTC | 3h 11m |
| N202SF |  | Moraine Air Park (KI73) | 2OH9 (2OH9) | 2026-08-14 20:03 UTC | 2026-08-14 20:11 UTC | 7m |
| IGO059 | IndiGo | Juhu Aerodrome (VAJJ) | Shaibah Airport (OESB) | 2026-08-14 17:41 UTC | 2026-08-14 20:09 UTC | 2h 27m |
| N587SL |  | Lancaster County-Mc Whirter Field (KLKR) | North Pickens Airport (K3M8) | 2026-08-14 19:12 UTC | 2026-08-14 20:07 UTC | 54m |
| N713LU |  | New London Airport (KW90) | VG27 (VG27) | 2026-08-14 19:16 UTC | 2026-08-14 20:06 UTC | 49m |
| AAL3215 | American Airlines | Chicago O'Hare International Airport (KORD) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-14 18:11 UTC | 2026-08-14 20:05 UTC | 1h 54m |
| N504RP |  | MS00 (MS00) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-08-14 18:15 UTC | 2026-08-14 20:03 UTC | 1h 47m |
| TALON35 | TAL | Greenville Spartanburg International Airport (KGSP) | Conway-Horry County Airport (KHYW) | 2026-08-14 19:30 UTC | 2026-08-14 20:02 UTC | 32m |
| N908FG |  | Trenton Mercer Airport (KTTN) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-08-14 19:24 UTC | 2026-08-14 20:01 UTC | 37m |
| CODE21 | COD | 75OK (75OK) | Good Life Ranch Airport (17OK) | 2026-08-14 19:25 UTC | 2026-08-14 20:01 UTC | 36m |
| TGCBC | TGC | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-08-14 19:51 UTC | 2026-08-14 20:00 UTC | 9m |
| VOE6GV | VOE | Brest Bretagne Airport (LFRB) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-14 18:08 UTC | 2026-08-14 20:00 UTC | 1h 51m |
| UAL316 | United Airlines | Dublin Airport (EIDW) | Newark Liberty International Airport (KEWR) | 2026-08-14 12:59 UTC | 2026-08-14 19:58 UTC | 6h 59m |
| N4549F |  | Dubois Regional Airport (KDUJ) | Punxsutawney Municipal Airport (KN35) | 2026-08-14 19:25 UTC | 2026-08-14 19:56 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
