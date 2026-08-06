# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--06_03:26:36_UTC-green)

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

**Latest saved flight:** 2026-08-06 03:26:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-06 03:26:36 UTC

- **173,603** saved flights
- **56,282** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **173,603** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,090,735.6 tonnes** estimated CO2 emissions
- **121,202,063 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6887 |
| 2 | SkyWest Airlines | 6369 |
| 3 | EJA | 3451 |
| 4 | IndiGo | 3034 |
| 5 | Southwest Airlines | 2742 |
| 6 | American Airlines | 2731 |
| 7 | ENY | 2166 |
| 8 | Delta Air Lines | 2061 |
| 9 | LATAM Airlines | 1605 |
| 10 | Lufthansa | 1574 |
| 11 | AZU | 1534 |
| 12 | WIF | 1448 |
| 13 | Vueling | 1428 |
| 14 | LXJ | 1361 |
| 15 | AXM | 1186 |
| 16 | Swiss International | 1178 |
| 17 | easyJet | 1175 |
| 18 | QLK | 1060 |
| 19 | EJU | 1059 |
| 20 | Alaska Airlines | 1057 |
| 21 | All Nippon Airways | 1048 |
| 22 | VIV | 954 |
| 23 | Cathay Pacific | 939 |
| 24 | CXK | 924 |
| 25 | GLO | 914 |
| 26 | United Airlines | 904 |
| 27 | AEE | 903 |
| 28 | Air France | 888 |
| 29 | MXY | 880 |
| 30 | JetBlue | 867 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 149770 |
| 2 | 🇪🇸 ES | 11095 |
| 3 | 🇧🇷 BR | 9885 |
| 4 | 🇦🇺 AU | 9699 |
| 5 | 🇮🇳 IN | 9518 |
| 6 | 🇨🇦 CA | 9512 |
| 7 | 🇮🇹 IT | 8946 |
| 8 | 🇩🇪 DE | 8586 |
| 9 | 🇬🇧 GB | 8029 |
| 10 | 🇯🇵 JP | 6958 |
| 11 | 🇫🇷 FR | 6870 |
| 12 | 🇨🇴 CO | 6401 |
| 13 | 🇬🇷 GR | 5030 |
| 14 | 🇲🇽 MX | 4971 |
| 15 | 🇨🇭 CH | 4566 |
| 16 | 🇳🇴 NO | 4507 |
| 17 | 🇹🇷 TR | 4251 |
| 18 | 🇲🇾 MY | 3084 |
| 19 | 🇵🇱 PL | 2896 |
| 20 | 🇿🇦 ZA | 2782 |
| 21 | 🇹🇭 TH | 2542 |
| 22 | 🇳🇿 NZ | 2514 |
| 23 | 🇵🇭 PH | 2288 |
| 24 | 🇬🇹 GT | 2213 |
| 25 | 🇰🇷 KR | 2175 |
| 26 | 🇲🇦 MA | 1742 |
| 27 | 🇭🇷 HR | 1673 |
| 28 | 🇲🇪 ME | 1586 |
| 29 | 🇳🇱 NL | 1564 |
| 30 | 🇲🇴 MO | 1500 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3595 |
| 2 | Denver International Airport |  | US | 2880 |
| 3 | Tokyo International Airport |  | JP | 2177 |
| 4 | Guaymaral Airport |  | CO | 2163 |
| 5 | Indira Gandhi International Airport |  | IN | 2121 |
| 6 | Harry Reid International Airport |  | US | 2081 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1883 |
| 8 | Zurich Airport |  | CH | 1832 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1824 |
| 10 | La Aurora Airport |  | GT | 1707 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1602 |
| 12 | El Dorado International Airport |  | CO | 1581 |
| 13 | Chicago O'Hare International Airport |  | US | 1572 |
| 14 | Salt Lake City International Airport |  | US | 1561 |
| 15 | Frankfurt am Main International Airport |  | DE | 1536 |
| 16 | Macau International Airport |  | MO | 1500 |
| 17 | Congonhas Airport |  | BR | 1430 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1419 |
| 19 | Capua Airport |  | IT | 1351 |
| 20 | Madrid Barajas International Airport |  | ES | 1350 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1305 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1221 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1208 |
| 24 | Charlotte/Douglas International Airport |  | US | 1199 |
| 25 | Charles de Gaulle International Airport |  | FR | 1175 |
| 26 | Malpensa International Airport |  | IT | 1174 |
| 27 | Kuala Lumpur International Airport |  | MY | 1163 |
| 28 | Bengaluru International Airport |  | IN | 1130 |
| 29 | Norman Y Mineta San Jose International Airport |  | US | 1080 |
| 30 | Ninoy Aquino International Airport |  | PH | 1077 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1070 |
| 32 | Barcelona International Airport |  | ES | 1025 |
| 33 | Seattle-Tacoma International Airport |  | US | 1003 |
| 34 | Daniel K Inouye International Airport |  | US | 1002 |
| 35 | Calgary International Airport |  | CA | 989 |
| 36 | Reno/Tahoe International Airport |  | US | 987 |
| 37 | Viracopos International Airport |  | BR | 986 |
| 38 | Oslo Gardermoen Airport |  | NO | 963 |
| 39 | Tenerife Norte Airport |  | ES | 960 |
| 40 | Scottsdale Airport |  | US | 946 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 634 | 21m | 244 km | 2,669.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 409 | 24m | 225 km | 1,586.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 407 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 393 | 1h 8m | 770 km | 5,220.7 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 320 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 293 | 27m | 275 km | 1,388.4 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 262 | 22m | 55 km | 249.0 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 260 | 44m | 241 km | 1,080.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 238 | 1h 48m | 1,423 km | 5,840.9 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 224 | 20m | 250 km | 967.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 223 | 26m | 215 km | 825.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 221 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 212 | 20m | 99 km | 363.1 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 209 | 50m | 556 km | 2,003.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 207 | 1h 15m | 961 km | 3,431.1 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 205 | 19m | 144 km | 509.9 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 202 | 12m | - | - |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 201 | 1h 38m | 1,156 km | 4,009.9 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 201 | 31m | 369 km | 1,279.4 t |
| 27 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 200 | 8m | - | - |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 193 | 24m | 218 km | 727.1 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 189 | 43m | 452 km | 1,473.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N559SC |  | Ogden-Hinckley Airport (KOGD) | Nephi Municipal Airport (KU14) | 2026-08-06 02:20 UTC | 2026-08-06 03:26 UTC | 1h 5m |
| N805AT |  | Arlington Municipal Airport (KGKY) | Austin-Bergstrom International Airport (KAUS) | 2026-08-06 01:54 UTC | 2026-08-06 03:20 UTC | 1h 25m |
| N76BH |  | Mc Clellan-Palomar Airport (KCRQ) | Hemet-Ryan Airport (KHMT) | 2026-08-06 02:56 UTC | 2026-08-06 03:17 UTC | 21m |
| FJQ | FJQ | Sydney Bankstown Airport (YSBK) | Tamworth Airport (YSTW) | 2026-08-06 01:48 UTC | 2026-08-06 03:14 UTC | 1h 26m |
| NPS | NPS | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-08-06 02:40 UTC | 2026-08-06 03:11 UTC | 31m |
| CPA372 | Cathay Pacific | Madrid Barajas International Airport (LEMD) | Zhuhai Airport (ZGSD) | 2026-08-05 15:38 UTC | 2026-08-06 03:11 UTC | 11h 32m |
| WXQ | WXQ | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-08-06 02:57 UTC | 2026-08-06 03:10 UTC | 13m |
| N5477T |  | Merrill Field (PAMR) | Birchwood Airport (PABV) | 2026-08-06 01:45 UTC | 2026-08-06 03:00 UTC | 1h 14m |
| XSR717 | XSR | K42V (K42V) | Colonel James Jabara Airport (KAAO) | 2026-08-06 02:18 UTC | 2026-08-06 02:55 UTC | 37m |
| ZKPDZ | ZKP | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-08-06 02:39 UTC | 2026-08-06 02:50 UTC | 10m |
| N559SH |  | Gold King Creek Airport (PAAN) | Healy River Airport (PAHV) | 2026-08-06 02:40 UTC | 2026-08-06 02:43 UTC | 3m |
| QLK40D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Wellington Airport (YWEL) | 2026-08-06 02:13 UTC | 2026-08-06 02:42 UTC | 28m |
| N24144 |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-08-06 02:13 UTC | 2026-08-06 02:39 UTC | 26m |
| TEXGLD | TEX | RNZAF Base Ohakea (NZOH) | Wanganui Airport (NZWU) | 2026-08-06 02:19 UTC | 2026-08-06 02:38 UTC | 19m |
| ETD595 | Etihad Airways | Al Bateen Executive Airport (OMAD) | Ben Gurion International Airport (LLBG) | 2026-08-06 00:01 UTC | 2026-08-06 02:37 UTC | 2h 36m |
| DAL1277 | Delta Air Lines | John Wayne/Orange County Airport (KSNA) | Salt Lake City International Airport (KSLC) | 2026-08-06 01:14 UTC | 2026-08-06 02:37 UTC | 1h 22m |
| LFA322 | LFA | Brunswick Golden Isles Airport (KBQK) | Jacksonville Executive At Craig Airport (KCRG) | 2026-08-06 00:33 UTC | 2026-08-06 02:35 UTC | 2h 2m |
| VIQ | VIQ | Sydney Bankstown Airport (YSBK) | Orange Airport (YORG) | 2026-08-06 01:40 UTC | 2026-08-06 02:35 UTC | 55m |
| N10EH |  | Salt Lake City International Airport (KSLC) | 2WY3 (2WY3) | 2026-08-06 02:12 UTC | 2026-08-06 02:35 UTC | 23m |
| YNR | YNR | Adelaide Parafield Airport (YPPF) | Adelaide Parafield Airport (YPPF) | 2026-08-06 02:01 UTC | 2026-08-06 02:33 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
