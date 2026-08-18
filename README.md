# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_13:35:33_UTC-green)

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

**Latest saved flight:** 2026-08-18 13:35:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 13:35:33 UTC

- **211,887** saved flights
- **67,202** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **211,887** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,547,692.4 tonnes** estimated CO2 emissions
- **147,692,315 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8397 |
| 2 | SkyWest Airlines | 7600 |
| 3 | EJA | 4113 |
| 4 | IndiGo | 3626 |
| 5 | American Airlines | 3534 |
| 6 | Southwest Airlines | 3386 |
| 7 | Delta Air Lines | 2731 |
| 8 | ENY | 2625 |
| 9 | LATAM Airlines | 1995 |
| 10 | AZU | 1920 |
| 11 | Lufthansa | 1778 |
| 12 | Vueling | 1772 |
| 13 | WIF | 1705 |
| 14 | LXJ | 1670 |
| 15 | easyJet | 1469 |
| 16 | Swiss International | 1420 |
| 17 | AXM | 1389 |
| 18 | United Airlines | 1341 |
| 19 | QLK | 1320 |
| 20 | Alaska Airlines | 1303 |
| 21 | EJU | 1302 |
| 22 | All Nippon Airways | 1286 |
| 23 | VIV | 1164 |
| 24 | Air France | 1143 |
| 25 | PGT | 1143 |
| 26 | GLO | 1142 |
| 27 | WMT | 1082 |
| 28 | JetBlue | 1080 |
| 29 | AEE | 1072 |
| 30 | Wizz Air | 1055 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 178988 |
| 2 | 🇪🇸 ES | 13581 |
| 3 | 🇧🇷 BR | 12138 |
| 4 | 🇦🇺 AU | 11958 |
| 5 | 🇨🇦 CA | 11699 |
| 6 | 🇮🇳 IN | 11308 |
| 7 | 🇮🇹 IT | 11132 |
| 8 | 🇩🇪 DE | 10477 |
| 9 | 🇬🇧 GB | 9887 |
| 10 | 🇯🇵 JP | 8782 |
| 11 | 🇨🇴 CO | 8515 |
| 12 | 🇫🇷 FR | 8417 |
| 13 | 🇬🇷 GR | 6209 |
| 14 | 🇹🇷 TR | 6065 |
| 15 | 🇲🇽 MX | 5932 |
| 16 | 🇨🇭 CH | 5626 |
| 17 | 🇳🇴 NO | 5279 |
| 18 | 🇲🇾 MY | 3671 |
| 19 | 🇿🇦 ZA | 3578 |
| 20 | 🇵🇱 PL | 3500 |
| 21 | 🇹🇭 TH | 3435 |
| 22 | 🇳🇿 NZ | 2945 |
| 23 | 🇵🇭 PH | 2829 |
| 24 | 🇬🇹 GT | 2705 |
| 25 | 🇰🇷 KR | 2583 |
| 26 | 🇭🇷 HR | 2296 |
| 27 | 🇲🇦 MA | 2136 |
| 28 | 🇳🇱 NL | 1888 |
| 29 | 🇲🇪 ME | 1821 |
| 30 | 🇮🇩 ID | 1769 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4448 |
| 2 | Denver International Airport |  | US | 3457 |
| 3 | Tokyo International Airport |  | JP | 2633 |
| 4 | Indira Gandhi International Airport |  | IN | 2582 |
| 5 | Guaymaral Airport |  | CO | 2534 |
| 6 | Harry Reid International Airport |  | US | 2376 |
| 7 | Zurich Airport |  | CH | 2212 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2186 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2183 |
| 10 | La Aurora Airport |  | GT | 2058 |
| 11 | Chicago O'Hare International Airport |  | US | 1956 |
| 12 | El Dorado International Airport |  | CO | 1945 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1875 |
| 14 | Salt Lake City International Airport |  | US | 1874 |
| 15 | Congonhas Airport |  | BR | 1764 |
| 16 | Frankfurt am Main International Airport |  | DE | 1732 |
| 17 | Madrid Barajas International Airport |  | ES | 1661 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1599 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1596 |
| 20 | Capua Airport |  | IT | 1596 |
| 21 | Macau International Airport |  | MO | 1554 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1547 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1489 |
| 24 | Malpensa International Airport |  | IT | 1470 |
| 25 | Charles de Gaulle International Airport |  | FR | 1456 |
| 26 | Charlotte/Douglas International Airport |  | US | 1426 |
| 27 | Kuala Lumpur International Airport |  | MY | 1353 |
| 28 | Ninoy Aquino International Airport |  | PH | 1341 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1306 |
| 30 | Bengaluru International Airport |  | IN | 1298 |
| 31 | Barcelona International Airport |  | ES | 1282 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1281 |
| 33 | Seattle-Tacoma International Airport |  | US | 1263 |
| 34 | Viracopos International Airport |  | BR | 1229 |
| 35 | Calgary International Airport |  | CA | 1201 |
| 36 | Oslo Gardermoen Airport |  | NO | 1173 |
| 37 | Vitoria/Foronda Airport |  | ES | 1170 |
| 38 | Reno/Tahoe International Airport |  | US | 1150 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1143 |
| 40 | Don Mueang International Airport |  | TH | 1136 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1039 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 753 | 21m | 244 km | 3,170.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 525 | 1h 7m | 770 km | 6,974.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 493 | 24m | 225 km | 1,912.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 479 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 435 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 352 | 27m | 275 km | 1,668.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 348 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 311 | 1h 49m | 1,423 km | 7,632.4 t |
| 10 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 311 | 14m | 114 km | 610.0 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 310 | 44m | 241 km | 1,287.7 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 290 | 22m | 55 km | 275.6 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 274 | 21m | 250 km | 1,183.5 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 263 | 19m | 99 km | 450.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 261 | 1h 38m | 1,156 km | 5,206.9 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 259 | 27m | 215 km | 959.2 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 250 | 19m | 165 km | 711.1 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 250 | 1h 14m | 961 km | 4,143.9 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 249 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 244 | 31m | 369 km | 1,553.1 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 243 | 19m | 144 km | 604.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 227 | 1h 49m | 1,304 km | 5,106.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N846AA |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-08-18 12:46 UTC | 2026-08-18 13:35 UTC | 48m |
| HBLSR | HBL | Grenchen Airport (LSZG) | Mollis Airport (LSZM) | 2026-08-18 13:13 UTC | 2026-08-18 13:31 UTC | 18m |
| SLICK92 | SLI | Larew Airport (WV53) | Lynn Airport (18WV) | 2026-08-18 13:11 UTC | 2026-08-18 13:30 UTC | 18m |
| TRF526 | TRF | 11TX (11TX) | Jones Field (KF00) | 2026-08-18 12:36 UTC | 2026-08-18 13:29 UTC | 52m |
| CXK284 | CXK | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-08-18 12:59 UTC | 2026-08-18 13:24 UTC | 25m |
| CFDBJ | CFD | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Eugene F Kranz Toledo Express Airport (KTOL) | 2026-08-18 11:46 UTC | 2026-08-18 13:22 UTC | 1h 36m |
| N4002S |  | Easton/Valley View Airport (K11V) | Easton/Valley View Airport (K11V) | 2026-08-18 12:50 UTC | 2026-08-18 13:18 UTC | 28m |
| PHJVZ | PHJ | Seppe Airport (EHSE) | Antwerp International Airport (Deurne) (EBAW) | 2026-08-18 12:56 UTC | 2026-08-18 13:17 UTC | 21m |
| N102CQ |  | Savannah/Hilton Head International Airport (KSAV) | Hunter Army Air Field (KSVN) | 2026-08-18 13:10 UTC | 2026-08-18 13:16 UTC | 6m |
| N318RL |  | Camarillo Airport (KCMA) | Camarillo Airport (KCMA) | 2026-08-18 13:02 UTC | 2026-08-18 13:15 UTC | 13m |
| CAN10 | CAN | Calcinate Del Pesce Airport (LILC) | Calcinate Del Pesce Airport (LILC) | 2026-08-18 13:12 UTC | 2026-08-18 13:14 UTC | 1m |
| FXC33 | FXC | Bridgeport/Sikorsky Airport (KBDR) | Monmouth Executive Airport (KBLM) | 2026-08-18 12:28 UTC | 2026-08-18 13:12 UTC | 44m |
| LFA548 | LFA | Orlando Sanford International Airport (KSFB) | Orlando Executive Airport (KORL) | 2026-08-18 12:56 UTC | 2026-08-18 13:12 UTC | 15m |
| TEK63 | TEK | Lancaster Airport (KLNS) | Trenton Mercer Airport (KTTN) | 2026-08-18 12:46 UTC | 2026-08-18 13:11 UTC | 24m |
| THNDR12 | THN | 8NC3 (8NC3) | 8NC3 (8NC3) | 2026-08-18 12:55 UTC | 2026-08-18 13:11 UTC | 15m |
| SPIN252 | SPI | Kingsville Nas Airport (KNQI) | Kingsville Nas Airport (KNQI) | 2026-08-18 12:55 UTC | 2026-08-18 13:08 UTC | 13m |
| BOMR701 | BOM | Corpus Christi Nas (Truax Field) Airport (KNGP) | Waldron Field Nolf Airport (KNWL) | 2026-08-18 12:52 UTC | 2026-08-18 13:08 UTC | 16m |
| AIC219 | Air India | Tribhuvan International Airport (VNKT) | Langtang Airport (VNLT) | 2026-08-18 12:57 UTC | 2026-08-18 13:08 UTC | 11m |
| OYCKP | OYC | Reykjavik Airport (BIRK) | Thorisos Airport (BITO) | 2026-08-18 11:44 UTC | 2026-08-18 13:07 UTC | 1h 23m |
| HDB1 | HDB | Al Minhad Air Base (OMDM) | Al Minhad Air Base (OMDM) | 2026-08-18 12:29 UTC | 2026-08-18 13:07 UTC | 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
