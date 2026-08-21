# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_02:44:24_UTC-green)

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

**Latest saved flight:** 2026-08-21 02:44:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 02:44:24 UTC

- **221,016** saved flights
- **69,318** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **221,016** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,659,749.9 tonnes** estimated CO2 emissions
- **154,188,397 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8846 |
| 2 | SkyWest Airlines | 7890 |
| 3 | EJA | 4289 |
| 4 | IndiGo | 3737 |
| 5 | American Airlines | 3667 |
| 6 | Southwest Airlines | 3489 |
| 7 | Delta Air Lines | 2848 |
| 8 | ENY | 2724 |
| 9 | LATAM Airlines | 2102 |
| 10 | AZU | 2030 |
| 11 | Vueling | 1858 |
| 12 | Lufthansa | 1830 |
| 13 | WIF | 1763 |
| 14 | LXJ | 1746 |
| 15 | easyJet | 1530 |
| 16 | Swiss International | 1466 |
| 17 | AXM | 1448 |
| 18 | United Airlines | 1390 |
| 19 | QLK | 1381 |
| 20 | EJU | 1374 |
| 21 | Alaska Airlines | 1347 |
| 22 | All Nippon Airways | 1321 |
| 23 | GLO | 1210 |
| 24 | VIV | 1206 |
| 25 | PGT | 1198 |
| 26 | Air France | 1197 |
| 27 | WMT | 1163 |
| 28 | Wizz Air | 1124 |
| 29 | JetBlue | 1119 |
| 30 | AEE | 1104 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 186154 |
| 2 | 🇪🇸 ES | 14139 |
| 3 | 🇧🇷 BR | 12782 |
| 4 | 🇦🇺 AU | 12498 |
| 5 | 🇨🇦 CA | 12214 |
| 6 | 🇮🇹 IT | 11742 |
| 7 | 🇮🇳 IN | 11652 |
| 8 | 🇩🇪 DE | 10894 |
| 9 | 🇬🇧 GB | 10365 |
| 10 | 🇨🇴 CO | 9097 |
| 11 | 🇯🇵 JP | 8977 |
| 12 | 🇫🇷 FR | 8786 |
| 13 | 🇬🇷 GR | 6437 |
| 14 | 🇹🇷 TR | 6361 |
| 15 | 🇲🇽 MX | 6149 |
| 16 | 🇨🇭 CH | 5829 |
| 17 | 🇳🇴 NO | 5481 |
| 18 | 🇲🇾 MY | 3834 |
| 19 | 🇿🇦 ZA | 3763 |
| 20 | 🇹🇭 TH | 3664 |
| 21 | 🇵🇱 PL | 3662 |
| 22 | 🇳🇿 NZ | 3070 |
| 23 | 🇵🇭 PH | 2977 |
| 24 | 🇬🇹 GT | 2790 |
| 25 | 🇰🇷 KR | 2638 |
| 26 | 🇭🇷 HR | 2447 |
| 27 | 🇲🇦 MA | 2220 |
| 28 | 🇳🇱 NL | 1962 |
| 29 | 🇲🇪 ME | 1950 |
| 30 | 🇮🇩 ID | 1879 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4647 |
| 2 | Denver International Airport |  | US | 3614 |
| 3 | Tokyo International Airport |  | JP | 2695 |
| 4 | Indira Gandhi International Airport |  | IN | 2675 |
| 5 | Guaymaral Airport |  | CO | 2606 |
| 6 | Harry Reid International Airport |  | US | 2439 |
| 7 | Zurich Airport |  | CH | 2288 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2274 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2240 |
| 10 | La Aurora Airport |  | GT | 2126 |
| 11 | El Dorado International Airport |  | CO | 2071 |
| 12 | Chicago O'Hare International Airport |  | US | 2024 |
| 13 | Salt Lake City International Airport |  | US | 1947 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1908 |
| 15 | Congonhas Airport |  | BR | 1869 |
| 16 | Frankfurt am Main International Airport |  | DE | 1797 |
| 17 | Madrid Barajas International Airport |  | ES | 1731 |
| 18 | Capua Airport |  | IT | 1685 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1661 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1629 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1625 |
| 22 | Macau International Airport |  | MO | 1583 |
| 23 | Malpensa International Airport |  | IT | 1548 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1548 |
| 25 | Charles de Gaulle International Airport |  | FR | 1519 |
| 26 | Charlotte/Douglas International Airport |  | US | 1470 |
| 27 | Ninoy Aquino International Airport |  | PH | 1416 |
| 28 | Kuala Lumpur International Airport |  | MY | 1404 |
| 29 | Barcelona International Airport |  | ES | 1354 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1343 |
| 31 | Bengaluru International Airport |  | IN | 1325 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1314 |
| 33 | Seattle-Tacoma International Airport |  | US | 1309 |
| 34 | Viracopos International Airport |  | BR | 1298 |
| 35 | Calgary International Airport |  | CA | 1252 |
| 36 | Enrique Olaya Herrera Airport |  | CO | 1235 |
| 37 | Vitoria/Foronda Airport |  | ES | 1225 |
| 38 | Oslo Gardermoen Airport |  | NO | 1224 |
| 39 | Don Mueang International Airport |  | TH | 1205 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1186 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1064 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 793 | 21m | 244 km | 3,339.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 547 | 1h 7m | 770 km | 7,266.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 528 | 24m | 225 km | 2,048.4 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 499 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 499 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 371 | 27m | 275 km | 1,758.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 326 | 1h 50m | 1,423 km | 8,000.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 324 | 44m | 241 km | 1,345.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 292 | 21m | 250 km | 1,261.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 276 | 1h 38m | 1,156 km | 5,506.1 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 274 | 24m | 218 km | 1,032.3 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 272 | 27m | 215 km | 1,007.4 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 261 | 1h 14m | 961 km | 4,326.2 t |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 252 | 12m | - | - |
| 26 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 251 | 44m | 555 km | 2,403.4 t |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 251 | 19m | 144 km | 624.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 239 | 1h 49m | 1,304 km | 5,376.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZKTTS | ZKT | RNZAF Base Auckland-Whenuapai (NZWP) | RNZAF Base Auckland-Whenuapai (NZWP) | 2026-08-21 02:24 UTC | 2026-08-21 02:44 UTC | 19m |
| PFT318 | PFT | Lake Tahoe Airport (KTVL) | Zamperini Field (KTOA) | 2026-08-21 01:13 UTC | 2026-08-21 02:32 UTC | 1h 19m |
| SKW5305 | SkyWest Airlines | Hayfork Airport (KF62) | San Francisco International Airport (KSFO) | 2026-08-21 01:38 UTC | 2026-08-21 02:29 UTC | 51m |
| 9MNAA |  | Sultan Abdul Aziz Shah International Airport (WMSA) | Ulu Bernam Airport (WMBF) | 2026-08-21 02:18 UTC | 2026-08-21 02:29 UTC | 10m |
| N111WH |  | Mobile Regional Airport (KMOB) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-08-21 02:06 UTC | 2026-08-21 02:29 UTC | 22m |
| N814SS |  | Beluga Airport (PABG) | Nikolai Creek Airport (9AK3) | 2026-08-21 02:17 UTC | 2026-08-21 02:28 UTC | 10m |
| HER12 | HER | Woodbourne Airport (NZWB) | Wellington International Airport (NZWN) | 2026-08-21 02:07 UTC | 2026-08-21 02:25 UTC | 18m |
| THY3006 | Turkish Airlines | Antalya International Airport (LTAI) | Smolensk North Airport (XUBS) | 2026-08-20 20:26 UTC | 2026-08-21 02:22 UTC | 5h 55m |
| N893AE |  | Des Moines International Airport (KDSM) | Teterboro Airport (KTEB) | 2026-08-21 00:23 UTC | 2026-08-21 02:21 UTC | 1h 58m |
| N61842 |  | Lenawee County Airport (KADG) | Lenawee County Airport (KADG) | 2026-08-21 01:50 UTC | 2026-08-21 02:19 UTC | 28m |
| N64464 |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-08-21 02:09 UTC | 2026-08-21 02:17 UTC | 7m |
| VOZ551 | Virgin Australia | Sydney Kingsford Smith International Airport (YSSY) | Perth International Airport (YPPH) | 2026-08-20 21:42 UTC | 2026-08-21 02:14 UTC | 4h 31m |
| AJAX19 | AJA | Goulburn Airport (YGLB) | Merimbula Airport (YMER) | 2026-08-21 01:54 UTC | 2026-08-21 02:12 UTC | 17m |
| N175EM |  | Tucson International Airport (KTUS) | Santa Fe Regional Airport (KSAF) | 2026-08-21 01:02 UTC | 2026-08-21 02:10 UTC | 1h 7m |
| N223SB |  | Bayview Farms Airport (WN51) | Lake Tahoe Airport (KTVL) | 2026-08-20 22:43 UTC | 2026-08-21 02:08 UTC | 3h 24m |
| FS200 |  | RAAF Base Richmond (YSRI) | Bunyan Airfield (YBUY) | 2026-08-21 00:56 UTC | 2026-08-21 02:06 UTC | 1h 10m |
| N598WC |  | Sacramento Mather Airport (KMHR) | Bangor International Airport (KBGR) | 2026-08-20 21:08 UTC | 2026-08-21 02:04 UTC | 4h 56m |
| SKW5786 | SkyWest Airlines | Los Angeles International Airport (KLAX) | Mesawood Airport (6CO2) | 2026-08-21 00:34 UTC | 2026-08-21 02:03 UTC | 1h 28m |
| N527BF |  | Tampa International Airport (KTPA) | Zephyrhills Municipal Airport (KZPH) | 2026-08-21 01:47 UTC | 2026-08-21 01:59 UTC | 11m |
| ZKHWM | ZKH | Gore3 Airport (NZGC) | Invercargill Airport (NZNV) | 2026-08-21 01:49 UTC | 2026-08-21 01:58 UTC | 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
