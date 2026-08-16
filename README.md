# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_22:24:38_UTC-green)

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

**Latest saved flight:** 2026-08-16 22:24:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 22:24:38 UTC

- **206,442** saved flights
- **65,833** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **206,442** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,483,048.6 tonnes** estimated CO2 emissions
- **143,944,847 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8146 |
| 2 | SkyWest Airlines | 7433 |
| 3 | EJA | 4019 |
| 4 | IndiGo | 3522 |
| 5 | American Airlines | 3443 |
| 6 | Southwest Airlines | 3319 |
| 7 | Delta Air Lines | 2656 |
| 8 | ENY | 2576 |
| 9 | LATAM Airlines | 1938 |
| 10 | AZU | 1868 |
| 11 | Lufthansa | 1749 |
| 12 | Vueling | 1709 |
| 13 | WIF | 1657 |
| 14 | LXJ | 1634 |
| 15 | easyJet | 1428 |
| 16 | Swiss International | 1376 |
| 17 | AXM | 1339 |
| 18 | United Airlines | 1303 |
| 19 | Alaska Airlines | 1279 |
| 20 | QLK | 1262 |
| 21 | EJU | 1260 |
| 22 | All Nippon Airways | 1245 |
| 23 | VIV | 1134 |
| 24 | GLO | 1117 |
| 25 | Air France | 1103 |
| 26 | PGT | 1101 |
| 27 | JetBlue | 1058 |
| 28 | AEE | 1052 |
| 29 | WMT | 1040 |
| 30 | CXK | 1017 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 175535 |
| 2 | 🇪🇸 ES | 13186 |
| 3 | 🇧🇷 BR | 11830 |
| 4 | 🇦🇺 AU | 11489 |
| 5 | 🇨🇦 CA | 11407 |
| 6 | 🇮🇳 IN | 10993 |
| 7 | 🇮🇹 IT | 10764 |
| 8 | 🇩🇪 DE | 10208 |
| 9 | 🇬🇧 GB | 9625 |
| 10 | 🇯🇵 JP | 8455 |
| 11 | 🇨🇴 CO | 8217 |
| 12 | 🇫🇷 FR | 8166 |
| 13 | 🇬🇷 GR | 6069 |
| 14 | 🇹🇷 TR | 5853 |
| 15 | 🇲🇽 MX | 5803 |
| 16 | 🇨🇭 CH | 5513 |
| 17 | 🇳🇴 NO | 5138 |
| 18 | 🇲🇾 MY | 3529 |
| 19 | 🇿🇦 ZA | 3454 |
| 20 | 🇵🇱 PL | 3403 |
| 21 | 🇹🇭 TH | 3247 |
| 22 | 🇳🇿 NZ | 2847 |
| 23 | 🇵🇭 PH | 2729 |
| 24 | 🇬🇹 GT | 2634 |
| 25 | 🇰🇷 KR | 2505 |
| 26 | 🇭🇷 HR | 2209 |
| 27 | 🇲🇦 MA | 2081 |
| 28 | 🇳🇱 NL | 1839 |
| 29 | 🇲🇪 ME | 1741 |
| 30 | 🇮🇩 ID | 1686 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4347 |
| 2 | Denver International Airport |  | US | 3381 |
| 3 | Tokyo International Airport |  | JP | 2550 |
| 4 | Guaymaral Airport |  | CO | 2494 |
| 5 | Indira Gandhi International Airport |  | IN | 2494 |
| 6 | Harry Reid International Airport |  | US | 2332 |
| 7 | Zurich Airport |  | CH | 2154 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2151 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2144 |
| 10 | La Aurora Airport |  | GT | 2007 |
| 11 | Chicago O'Hare International Airport |  | US | 1912 |
| 12 | El Dorado International Airport |  | CO | 1887 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1845 |
| 14 | Salt Lake City International Airport |  | US | 1829 |
| 15 | Congonhas Airport |  | BR | 1724 |
| 16 | Frankfurt am Main International Airport |  | DE | 1706 |
| 17 | Madrid Barajas International Airport |  | ES | 1618 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1574 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1570 |
| 20 | Capua Airport |  | IT | 1568 |
| 21 | Macau International Airport |  | MO | 1542 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1494 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1436 |
| 24 | Malpensa International Airport |  | IT | 1424 |
| 25 | Charles de Gaulle International Airport |  | FR | 1413 |
| 26 | Charlotte/Douglas International Airport |  | US | 1410 |
| 27 | Kuala Lumpur International Airport |  | MY | 1309 |
| 28 | Ninoy Aquino International Airport |  | PH | 1293 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1276 |
| 30 | Bengaluru International Airport |  | IN | 1276 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1249 |
| 32 | Barcelona International Airport |  | ES | 1229 |
| 33 | Seattle-Tacoma International Airport |  | US | 1227 |
| 34 | Viracopos International Airport |  | BR | 1197 |
| 35 | Calgary International Airport |  | CA | 1168 |
| 36 | Reno/Tahoe International Airport |  | US | 1141 |
| 37 | Oslo Gardermoen Airport |  | NO | 1139 |
| 38 | Vitoria/Foronda Airport |  | ES | 1136 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1107 |
| 40 | Tenerife Norte Airport |  | ES | 1105 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1026 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 500 | 1h 7m | 770 km | 6,642.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 478 | 24m | 225 km | 1,854.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 470 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 401 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 345 | 27m | 275 km | 1,634.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 303 | 44m | 241 km | 1,258.6 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 297 | 1h 49m | 1,423 km | 7,288.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 268 | 21m | 250 km | 1,157.6 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 257 | 24m | 218 km | 968.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 253 | 19m | 99 km | 433.4 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 250 | 27m | 215 km | 925.9 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 244 | 1h 37m | 1,156 km | 4,867.7 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 237 | 19m | 144 km | 589.5 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 233 | 31m | 369 km | 1,483.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 225 | 28m | 152 km | 588.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 222 | 1h 49m | 1,304 km | 4,994.4 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-16 22:08 UTC | 2026-08-16 22:24 UTC | 16m |
| CXK685 | CXK | Conroe/North Houston Regional Airport (KCXO) | Conroe/North Houston Regional Airport (KCXO) | 2026-08-16 21:12 UTC | 2026-08-16 22:15 UTC | 1h 3m |
| SCU28 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Ragwing Acres Airport (2OK4) | 2026-08-16 21:36 UTC | 2026-08-16 22:11 UTC | 35m |
| N69PJ |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-08-16 21:30 UTC | 2026-08-16 22:10 UTC | 40m |
| CAI9048 | CAI | Antalya International Airport (LTAI) | Bezymyanka Airfield (UWWG) | 2026-08-16 19:01 UTC | 2026-08-16 22:09 UTC | 3h 8m |
| N616F |  | Livermore Municipal Airport (KLVK) | Sacramento Executive Airport (KSAC) | 2026-08-16 21:33 UTC | 2026-08-16 22:04 UTC | 31m |
| N8351L |  | Double W Airport (3OK7) | Tulsa International Airport (KTUL) | 2026-08-16 21:56 UTC | 2026-08-16 21:58 UTC | 1m |
| FTO381 | FTO | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-08-16 21:17 UTC | 2026-08-16 21:56 UTC | 39m |
| N721AZ |  | John Wayne/Orange County Airport (KSNA) | Portland-Hillsboro Airport (KHIO) | 2026-08-16 20:06 UTC | 2026-08-16 21:54 UTC | 1h 47m |
| JZA804 | JZA | Vancouver International Airport (CYVR) | Thompson Airport (WA61) | 2026-08-16 21:15 UTC | 2026-08-16 21:52 UTC | 37m |
| DAL2419 | Delta Air Lines | Phoenix Sky Harbor International Airport (KPHX) | Seattle-Tacoma International Airport (KSEA) | 2026-08-16 19:15 UTC | 2026-08-16 21:51 UTC | 2h 36m |
| JA01TE |  | Matsumoto Airport (RJAF) | Matsumoto Airport (RJAF) | 2026-08-16 21:47 UTC | 2026-08-16 21:51 UTC | 4m |
| AAL757 | American Airlines | Dallas-Fort Worth International Airport (KDFW) | Seattle-Tacoma International Airport (KSEA) | 2026-08-16 18:09 UTC | 2026-08-16 21:49 UTC | 3h 39m |
| N734HX |  | Knox County Regional Airport (KRKD) | Matinicus Island Airport (35ME) | 2026-08-16 21:38 UTC | 2026-08-16 21:48 UTC | 9m |
| N42BW |  | Granbury Regional Airport (KGDJ) | Curtis Field (KBBD) | 2026-08-16 21:06 UTC | 2026-08-16 21:48 UTC | 41m |
| N13DC |  | Boise Air Trml/Gowen Field (KBOI) | Coyote Run Airport (0ID3) | 2026-08-16 21:29 UTC | 2026-08-16 21:46 UTC | 17m |
| SKW3735 | SkyWest Airlines | Roberts Field/Redmond Municipal Airport (KRDM) | Seattle-Tacoma International Airport (KSEA) | 2026-08-16 20:58 UTC | 2026-08-16 21:46 UTC | 48m |
| TKR829 | TKR | Lemons Field (2ID6) | 0ID5 (0ID5) | 2026-08-16 21:12 UTC | 2026-08-16 21:45 UTC | 32m |
| JUMP16 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-08-16 20:19 UTC | 2026-08-16 21:43 UTC | 1h 23m |
| N307TL |  | Kerrville Municipal/Louis Schreiner Field (KERV) | Gunnison-Crested Butte Regional Airport (KGUC) | 2026-08-16 19:18 UTC | 2026-08-16 21:41 UTC | 2h 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
