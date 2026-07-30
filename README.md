# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30_05:56:00_UTC-green)

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

**Latest saved flight:** 2026-07-30 05:56:00 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-30 05:56:00 UTC

- **159,860** saved flights
- **52,904** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **159,860** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,918,711.2 tonnes** estimated CO2 emissions
- **111,229,637 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6404 |
| 2 | SkyWest Airlines | 5837 |
| 3 | EJA | 3175 |
| 4 | IndiGo | 2814 |
| 5 | American Airlines | 2530 |
| 6 | Southwest Airlines | 2511 |
| 7 | ENY | 1994 |
| 8 | Delta Air Lines | 1903 |
| 9 | Lufthansa | 1516 |
| 10 | LATAM Airlines | 1502 |
| 11 | AZU | 1409 |
| 12 | WIF | 1352 |
| 13 | Vueling | 1336 |
| 14 | LXJ | 1233 |
| 15 | AXM | 1115 |
| 16 | Swiss International | 1099 |
| 17 | easyJet | 1044 |
| 18 | Alaska Airlines | 1001 |
| 19 | QLK | 989 |
| 20 | All Nippon Airways | 988 |
| 21 | EJU | 976 |
| 22 | VIV | 877 |
| 23 | CXK | 847 |
| 24 | United Airlines | 847 |
| 25 | Cathay Pacific | 843 |
| 26 | GLO | 842 |
| 27 | AEE | 839 |
| 28 | MXY | 832 |
| 29 | Air France | 829 |
| 30 | JetBlue | 820 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 138081 |
| 2 | 🇪🇸 ES | 10244 |
| 3 | 🇧🇷 BR | 9148 |
| 4 | 🇦🇺 AU | 9038 |
| 5 | 🇮🇳 IN | 8845 |
| 6 | 🇨🇦 CA | 8697 |
| 7 | 🇮🇹 IT | 8248 |
| 8 | 🇩🇪 DE | 8073 |
| 9 | 🇬🇧 GB | 7314 |
| 10 | 🇯🇵 JP | 6511 |
| 11 | 🇫🇷 FR | 6307 |
| 12 | 🇨🇴 CO | 5636 |
| 13 | 🇲🇽 MX | 4589 |
| 14 | 🇬🇷 GR | 4578 |
| 15 | 🇳🇴 NO | 4224 |
| 16 | 🇨🇭 CH | 4173 |
| 17 | 🇹🇷 TR | 3814 |
| 18 | 🇲🇾 MY | 2899 |
| 19 | 🇵🇱 PL | 2710 |
| 20 | 🇿🇦 ZA | 2573 |
| 21 | 🇳🇿 NZ | 2362 |
| 22 | 🇹🇭 TH | 2286 |
| 23 | 🇵🇭 PH | 2108 |
| 24 | 🇰🇷 KR | 2104 |
| 25 | 🇬🇹 GT | 2040 |
| 26 | 🇲🇦 MA | 1620 |
| 27 | 🇲🇪 ME | 1524 |
| 28 | 🇭🇷 HR | 1480 |
| 29 | 🇳🇱 NL | 1459 |
| 30 | 🇲🇴 MO | 1328 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3270 |
| 2 | Denver International Airport |  | US | 2663 |
| 3 | Tokyo International Airport |  | JP | 2057 |
| 4 | Guaymaral Airport |  | CO | 2006 |
| 5 | Indira Gandhi International Airport |  | IN | 1969 |
| 6 | Harry Reid International Airport |  | US | 1948 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1770 |
| 8 | Zurich Airport |  | CH | 1706 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1682 |
| 10 | La Aurora Airport |  | GT | 1583 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1493 |
| 12 | El Dorado International Airport |  | CO | 1465 |
| 13 | Frankfurt am Main International Airport |  | DE | 1464 |
| 14 | Chicago O'Hare International Airport |  | US | 1449 |
| 15 | Salt Lake City International Airport |  | US | 1440 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1335 |
| 17 | Macau International Airport |  | MO | 1328 |
| 18 | Congonhas Airport |  | BR | 1327 |
| 19 | Madrid Barajas International Airport |  | ES | 1264 |
| 20 | Capua Airport |  | IT | 1258 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1229 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1143 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1137 |
| 24 | Charlotte/Douglas International Airport |  | US | 1122 |
| 25 | Kuala Lumpur International Airport |  | MY | 1107 |
| 26 | Charles de Gaulle International Airport |  | FR | 1094 |
| 27 | Malpensa International Airport |  | IT | 1055 |
| 28 | Bengaluru International Airport |  | IN | 1055 |
| 29 | Ninoy Aquino International Airport |  | PH | 988 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 977 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 974 |
| 32 | Barcelona International Airport |  | ES | 953 |
| 33 | Daniel K Inouye International Airport |  | US | 943 |
| 34 | Seattle-Tacoma International Airport |  | US | 935 |
| 35 | Calgary International Airport |  | CA | 921 |
| 36 | Viracopos International Airport |  | BR | 915 |
| 37 | Scottsdale Airport |  | US | 904 |
| 38 | Tenerife Norte Airport |  | ES | 897 |
| 39 | Oslo Gardermoen Airport |  | NO | 886 |
| 40 | Amsterdam Airport Schiphol |  | NL | 877 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 842 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 582 | 21m | 244 km | 2,450.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 382 | 24m | 225 km | 1,482.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 379 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 367 | 1h 9m | 770 km | 4,875.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 294 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 280 | 27m | 275 km | 1,326.8 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 237 | 19m | 165 km | 674.2 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 233 | 22m | 55 km | 221.5 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 226 | 44m | 241 km | 938.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 217 | 1h 47m | 1,423 km | 5,325.5 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 210 | 26m | 215 km | 777.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 206 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 200 | 20m | 250 km | 863.9 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 192 | 30m | 49 km | 162.3 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 191 | 1h 15m | 961 km | 3,165.9 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 189 | 27m | 152 km | 493.9 t |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 188 | 31m | 369 km | 1,196.7 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 188 | 18m | 144 km | 467.6 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 184 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 182 | 50m | 556 km | 1,744.6 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 179 | 1h 39m | 1,156 km | 3,571.0 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 177 | 1h 1m | 695 km | 2,121.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 177 | 44m | 452 km | 1,379.5 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 170 | 23m | 218 km | 640.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BBX403 | BBX | Esbjerg Airport (EKEB) | Lemvig Airport (EKLV) | 2026-07-30 05:30 UTC | 2026-07-30 05:56 UTC | 25m |
| N43AE |  | 2TX2 (2TX2) | Granbury Regional Airport (KGDJ) | 2026-07-30 05:39 UTC | 2026-07-30 05:54 UTC | 14m |
| G20132 |  | Mcnary Field (KSLE) | Mcnary Field (KSLE) | 2026-07-30 04:18 UTC | 2026-07-30 05:40 UTC | 1h 22m |
| A7GQB |  | Persian Gulf International Airport (OIBP) | Persian Gulf International Airport (OIBP) | 2026-07-30 04:36 UTC | 2026-07-30 05:31 UTC | 55m |
| CHP51 | CHP | Fullerton Municipal Airport (KFUL) | 8CL0 (8CL0) | 2026-07-30 05:07 UTC | 2026-07-30 05:28 UTC | 21m |
| ZKIDH | ZKI | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-07-30 05:13 UTC | 2026-07-30 05:26 UTC | 13m |
| RYB | RYB | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-07-30 05:13 UTC | 2026-07-30 05:26 UTC | 12m |
| N185YY |  | Ugashik Narrows Airport (AA05) | Wasilla Airport (PAWS) | 2026-07-30 05:18 UTC | 2026-07-30 05:25 UTC | 7m |
| N491LP |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-07-30 04:46 UTC | 2026-07-30 05:21 UTC | 34m |
| JNX15 | JNX | Mesa Gateway Airport (KIWA) | Western Sky Airpark (0AZ2) | 2026-07-30 04:29 UTC | 2026-07-30 05:17 UTC | 48m |
| RXA6133 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-07-30 04:34 UTC | 2026-07-30 05:16 UTC | 42m |
| OAL098 | OAL | Limnos Airport (LGLM) | Ikaria Airport (LGIK) | 2026-07-30 04:39 UTC | 2026-07-30 05:10 UTC | 31m |
| SWR12K | Swiss International | Václav Havel Airport (LKPR) | Zurich Airport (LSZH) | 2026-07-30 04:08 UTC | 2026-07-30 05:10 UTC | 1h 1m |
| NPN | NPN | Kyneton Airport (YKTN) | Melbourne Essendon Airport (YMEN) | 2026-07-30 04:42 UTC | 2026-07-30 05:08 UTC | 26m |
| N5192A |  | 0CL6 (0CL6) | Van Nuys Airport (KVNY) | 2026-07-30 04:48 UTC | 2026-07-30 05:05 UTC | 17m |
| WZZ9445 | Wizz Air | Larnaca International Airport (LCLK) | Gyumri Shirak Airport (UDSG) | 2026-07-30 03:26 UTC | 2026-07-30 04:58 UTC | 1h 32m |
| JMA8662 | JMA | HKSA (HKSA) | Nakuru Airport (HKNK) | 2026-07-30 04:40 UTC | 2026-07-30 04:56 UTC | 15m |
| CPA250 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-07-29 17:35 UTC | 2026-07-30 04:53 UTC | 11h 18m |
| FDX1807 | FDX | Portland International Airport (KPDX) | NV13 (NV13) | 2026-07-30 03:45 UTC | 2026-07-30 04:50 UTC | 1h 5m |
| IGO5268 | IndiGo | Juhu Aerodrome (VAJJ) | Patiala Airport (VIPL) | 2026-07-30 03:11 UTC | 2026-07-30 04:50 UTC | 1h 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
