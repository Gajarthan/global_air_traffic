# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_21:26:42_UTC-green)

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

**Latest saved flight:** 2026-08-17 21:26:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 21:26:42 UTC

- **210,091** saved flights
- **66,885** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **210,091** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,525,941.3 tonnes** estimated CO2 emissions
- **146,431,380 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8319 |
| 2 | SkyWest Airlines | 7560 |
| 3 | EJA | 4102 |
| 4 | IndiGo | 3575 |
| 5 | American Airlines | 3515 |
| 6 | Southwest Airlines | 3376 |
| 7 | Delta Air Lines | 2716 |
| 8 | ENY | 2617 |
| 9 | LATAM Airlines | 1980 |
| 10 | AZU | 1904 |
| 11 | Lufthansa | 1769 |
| 12 | Vueling | 1750 |
| 13 | WIF | 1691 |
| 14 | LXJ | 1661 |
| 15 | easyJet | 1459 |
| 16 | Swiss International | 1403 |
| 17 | AXM | 1363 |
| 18 | United Airlines | 1334 |
| 19 | QLK | 1293 |
| 20 | Alaska Airlines | 1292 |
| 21 | EJU | 1285 |
| 22 | All Nippon Airways | 1265 |
| 23 | VIV | 1156 |
| 24 | GLO | 1137 |
| 25 | Air France | 1133 |
| 26 | PGT | 1123 |
| 27 | JetBlue | 1075 |
| 28 | AEE | 1068 |
| 29 | WMT | 1067 |
| 30 | Wizz Air | 1044 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 178113 |
| 2 | 🇪🇸 ES | 13448 |
| 3 | 🇧🇷 BR | 12054 |
| 4 | 🇦🇺 AU | 11751 |
| 5 | 🇨🇦 CA | 11619 |
| 6 | 🇮🇳 IN | 11156 |
| 7 | 🇮🇹 IT | 10995 |
| 8 | 🇩🇪 DE | 10375 |
| 9 | 🇬🇧 GB | 9808 |
| 10 | 🇯🇵 JP | 8645 |
| 11 | 🇨🇴 CO | 8423 |
| 12 | 🇫🇷 FR | 8350 |
| 13 | 🇬🇷 GR | 6178 |
| 14 | 🇹🇷 TR | 5987 |
| 15 | 🇲🇽 MX | 5901 |
| 16 | 🇨🇭 CH | 5585 |
| 17 | 🇳🇴 NO | 5236 |
| 18 | 🇲🇾 MY | 3594 |
| 19 | 🇿🇦 ZA | 3517 |
| 20 | 🇵🇱 PL | 3475 |
| 21 | 🇹🇭 TH | 3354 |
| 22 | 🇳🇿 NZ | 2893 |
| 23 | 🇵🇭 PH | 2776 |
| 24 | 🇬🇹 GT | 2696 |
| 25 | 🇰🇷 KR | 2545 |
| 26 | 🇭🇷 HR | 2262 |
| 27 | 🇲🇦 MA | 2121 |
| 28 | 🇳🇱 NL | 1872 |
| 29 | 🇲🇪 ME | 1788 |
| 30 | 🇮🇩 ID | 1725 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4418 |
| 2 | Denver International Airport |  | US | 3436 |
| 3 | Tokyo International Airport |  | JP | 2599 |
| 4 | Indira Gandhi International Airport |  | IN | 2539 |
| 5 | Guaymaral Airport |  | CO | 2530 |
| 6 | Harry Reid International Airport |  | US | 2361 |
| 7 | Zurich Airport |  | CH | 2190 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2181 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2176 |
| 10 | La Aurora Airport |  | GT | 2050 |
| 11 | Chicago O'Hare International Airport |  | US | 1947 |
| 12 | El Dorado International Airport |  | CO | 1918 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1871 |
| 14 | Salt Lake City International Airport |  | US | 1863 |
| 15 | Congonhas Airport |  | BR | 1755 |
| 16 | Frankfurt am Main International Airport |  | DE | 1722 |
| 17 | Madrid Barajas International Airport |  | ES | 1643 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1592 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1591 |
| 20 | Capua Airport |  | IT | 1584 |
| 21 | Macau International Airport |  | MO | 1547 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1530 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1469 |
| 24 | Malpensa International Airport |  | IT | 1455 |
| 25 | Charles de Gaulle International Airport |  | FR | 1445 |
| 26 | Charlotte/Douglas International Airport |  | US | 1423 |
| 27 | Kuala Lumpur International Airport |  | MY | 1327 |
| 28 | Ninoy Aquino International Airport |  | PH | 1315 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1299 |
| 30 | Bengaluru International Airport |  | IN | 1289 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1274 |
| 32 | Barcelona International Airport |  | ES | 1261 |
| 33 | Seattle-Tacoma International Airport |  | US | 1248 |
| 34 | Viracopos International Airport |  | BR | 1220 |
| 35 | Calgary International Airport |  | CA | 1191 |
| 36 | Oslo Gardermoen Airport |  | NO | 1161 |
| 37 | Vitoria/Foronda Airport |  | ES | 1160 |
| 38 | Reno/Tahoe International Airport |  | US | 1149 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1132 |
| 40 | Daniel K Inouye International Airport |  | US | 1114 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1038 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 740 | 21m | 244 km | 3,115.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 514 | 1h 7m | 770 km | 6,828.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 486 | 24m | 225 km | 1,885.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 477 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 426 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 350 | 27m | 275 km | 1,658.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 346 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 308 | 44m | 241 km | 1,279.4 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 307 | 1h 49m | 1,423 km | 7,534.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 289 | 22m | 55 km | 274.7 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 270 | 21m | 250 km | 1,166.2 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 263 | 19m | 99 km | 450.5 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 257 | 27m | 215 km | 951.8 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 250 | 1h 37m | 1,156 km | 4,987.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 249 | 1h 14m | 961 km | 4,127.3 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 248 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 241 | 19m | 144 km | 599.5 t |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 239 | 31m | 369 km | 1,521.3 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 229 | 28m | 152 km | 598.5 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 225 | 1h 49m | 1,304 km | 5,061.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N945RF |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-17 20:34 UTC | 2026-08-17 21:26 UTC | 52m |
| N733JA |  | Cable Airport (KCCB) | Brackett Field (KPOC) | 2026-08-17 19:59 UTC | 2026-08-17 21:16 UTC | 1h 16m |
| N739ZH |  | Flying W Airport (KN14) | Flying W Airport (KN14) | 2026-08-17 20:44 UTC | 2026-08-17 21:15 UTC | 31m |
| N33RK |  | Peter O Knight Airport (KTPF) | Orlando Executive Airport (KORL) | 2026-08-17 20:44 UTC | 2026-08-17 21:15 UTC | 30m |
| N676CB |  | Elizabeth City Cg Air Station/Regional Airport (KECG) | Currituck County Regional Airport (KONX) | 2026-08-17 20:22 UTC | 2026-08-17 21:14 UTC | 52m |
| BCS4515 | BCS | Mollis Airport (LSZM) | Malpensa International Airport (LIMC) | 2026-08-17 20:36 UTC | 2026-08-17 21:09 UTC | 32m |
| N5620B |  | Minden-Tahoe Airport (KMEV) | Minden-Tahoe Airport (KMEV) | 2026-08-17 20:46 UTC | 2026-08-17 21:06 UTC | 19m |
| CXK160 | CXK | Essex County Airport (KCDW) | Northeast Philadelphia Airport (KPNE) | 2026-08-17 20:24 UTC | 2026-08-17 21:05 UTC | 40m |
| BLINR17 | BLI | Travis Afb Airport (KSUU) | Travis Afb Airport (KSUU) | 2026-08-17 20:40 UTC | 2026-08-17 21:05 UTC | 24m |
| MNL99 | MNL | Yolo County Airport (KDWA) | Truckee-Tahoe Airport (KTRK) | 2026-08-17 20:36 UTC | 2026-08-17 20:58 UTC | 22m |
| WAKE13 | WAK | Albuquerque International Sunport Airport (KABQ) | Albuquerque International Sunport Airport (KABQ) | 2026-08-17 20:48 UTC | 2026-08-17 20:54 UTC | 6m |
| VLG6XB | Vueling | Palma De Mallorca Airport (LEPA) | Barcelona International Airport (LEBL) | 2026-08-17 20:15 UTC | 2026-08-17 20:54 UTC | 39m |
| N1926F |  | San Carlos Airport (KSQL) | Tracy Municipal Airport (KTCY) | 2026-08-17 19:59 UTC | 2026-08-17 20:53 UTC | 54m |
| N82305 |  | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-08-17 20:44 UTC | 2026-08-17 20:53 UTC | 8m |
| AAL133 | American Airlines | Dublin Airport (EIDW) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-17 11:52 UTC | 2026-08-17 20:50 UTC | 8h 58m |
| N680H |  | Wausau Downtown Airport (KAUW) | Central Wisconsin Airport (KCWA) | 2026-08-17 20:37 UTC | 2026-08-17 20:49 UTC | 12m |
| N414UH |  | UT08 (UT08) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-08-17 20:31 UTC | 2026-08-17 20:47 UTC | 15m |
| N4603W |  | Rio Vista Municipal Airport (KO88) | Rio Vista Municipal Airport (KO88) | 2026-08-17 20:33 UTC | 2026-08-17 20:44 UTC | 11m |
| CGSWV | CGS | Vancouver International Airport (CYVR) | Princeton Airport (CYDC) | 2026-08-17 19:57 UTC | 2026-08-17 20:44 UTC | 47m |
| N16BT |  | Austin-Bergstrom International Airport (KAUS) | Addison Airport (KADS) | 2026-08-17 19:14 UTC | 2026-08-17 20:44 UTC | 1h 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
