# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_14:51:05_UTC-green)

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

**Latest saved flight:** 2026-08-18 14:51:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 14:51:05 UTC

- **212,106** saved flights
- **67,241** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **212,106** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,550,020.9 tonnes** estimated CO2 emissions
- **147,827,298 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8407 |
| 2 | SkyWest Airlines | 7602 |
| 3 | EJA | 4120 |
| 4 | IndiGo | 3631 |
| 5 | American Airlines | 3536 |
| 6 | Southwest Airlines | 3386 |
| 7 | Delta Air Lines | 2732 |
| 8 | ENY | 2625 |
| 9 | LATAM Airlines | 1999 |
| 10 | AZU | 1925 |
| 11 | Lufthansa | 1778 |
| 12 | Vueling | 1774 |
| 13 | WIF | 1706 |
| 14 | LXJ | 1673 |
| 15 | easyJet | 1471 |
| 16 | Swiss International | 1421 |
| 17 | AXM | 1390 |
| 18 | United Airlines | 1342 |
| 19 | QLK | 1320 |
| 20 | Alaska Airlines | 1303 |
| 21 | EJU | 1303 |
| 22 | All Nippon Airways | 1286 |
| 23 | VIV | 1166 |
| 24 | GLO | 1145 |
| 25 | Air France | 1144 |
| 26 | PGT | 1144 |
| 27 | WMT | 1086 |
| 28 | JetBlue | 1080 |
| 29 | AEE | 1072 |
| 30 | Wizz Air | 1056 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 179159 |
| 2 | 🇪🇸 ES | 13589 |
| 3 | 🇧🇷 BR | 12165 |
| 4 | 🇦🇺 AU | 11962 |
| 5 | 🇨🇦 CA | 11715 |
| 6 | 🇮🇳 IN | 11320 |
| 7 | 🇮🇹 IT | 11155 |
| 8 | 🇩🇪 DE | 10485 |
| 9 | 🇬🇧 GB | 9897 |
| 10 | 🇯🇵 JP | 8782 |
| 11 | 🇨🇴 CO | 8531 |
| 12 | 🇫🇷 FR | 8425 |
| 13 | 🇬🇷 GR | 6210 |
| 14 | 🇹🇷 TR | 6074 |
| 15 | 🇲🇽 MX | 5938 |
| 16 | 🇨🇭 CH | 5635 |
| 17 | 🇳🇴 NO | 5288 |
| 18 | 🇲🇾 MY | 3673 |
| 19 | 🇿🇦 ZA | 3582 |
| 20 | 🇵🇱 PL | 3504 |
| 21 | 🇹🇭 TH | 3447 |
| 22 | 🇳🇿 NZ | 2945 |
| 23 | 🇵🇭 PH | 2829 |
| 24 | 🇬🇹 GT | 2711 |
| 25 | 🇰🇷 KR | 2583 |
| 26 | 🇭🇷 HR | 2303 |
| 27 | 🇲🇦 MA | 2138 |
| 28 | 🇳🇱 NL | 1890 |
| 29 | 🇲🇪 ME | 1824 |
| 30 | 🇮🇩 ID | 1771 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4450 |
| 2 | Denver International Airport |  | US | 3458 |
| 3 | Tokyo International Airport |  | JP | 2633 |
| 4 | Indira Gandhi International Airport |  | IN | 2584 |
| 5 | Guaymaral Airport |  | CO | 2534 |
| 6 | Harry Reid International Airport |  | US | 2377 |
| 7 | Zurich Airport |  | CH | 2213 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2186 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2183 |
| 10 | La Aurora Airport |  | GT | 2061 |
| 11 | Chicago O'Hare International Airport |  | US | 1957 |
| 12 | El Dorado International Airport |  | CO | 1949 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1875 |
| 14 | Salt Lake City International Airport |  | US | 1874 |
| 15 | Congonhas Airport |  | BR | 1768 |
| 16 | Frankfurt am Main International Airport |  | DE | 1733 |
| 17 | Madrid Barajas International Airport |  | ES | 1662 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1600 |
| 19 | Capua Airport |  | IT | 1597 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1596 |
| 21 | Macau International Airport |  | MO | 1554 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1550 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1490 |
| 24 | Malpensa International Airport |  | IT | 1471 |
| 25 | Charles de Gaulle International Airport |  | FR | 1457 |
| 26 | Charlotte/Douglas International Airport |  | US | 1427 |
| 27 | Kuala Lumpur International Airport |  | MY | 1354 |
| 28 | Ninoy Aquino International Airport |  | PH | 1341 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1308 |
| 30 | Bengaluru International Airport |  | IN | 1301 |
| 31 | Barcelona International Airport |  | ES | 1285 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1282 |
| 33 | Seattle-Tacoma International Airport |  | US | 1263 |
| 34 | Viracopos International Airport |  | BR | 1233 |
| 35 | Calgary International Airport |  | CA | 1202 |
| 36 | Oslo Gardermoen Airport |  | NO | 1176 |
| 37 | Vitoria/Foronda Airport |  | ES | 1170 |
| 38 | Reno/Tahoe International Airport |  | US | 1152 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1144 |
| 40 | Don Mueang International Airport |  | TH | 1138 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1039 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 753 | 21m | 244 km | 3,170.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 525 | 1h 7m | 770 km | 6,974.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 493 | 24m | 225 km | 1,912.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 479 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 437 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 352 | 27m | 275 km | 1,668.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 348 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 311 | 1h 49m | 1,423 km | 7,632.4 t |
| 10 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 311 | 14m | 114 km | 610.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 311 | 44m | 241 km | 1,291.8 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 291 | 22m | 55 km | 276.6 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 275 | 21m | 250 km | 1,187.8 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 265 | 19m | 99 km | 453.9 t |
| 18 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 262 | 1h 38m | 1,156 km | 5,226.8 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 259 | 27m | 215 km | 959.2 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 251 | 19m | 165 km | 714.0 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 251 | 1h 14m | 961 km | 4,160.5 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 249 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 244 | 31m | 369 km | 1,553.1 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 243 | 19m | 144 km | 604.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 228 | 1h 49m | 1,304 km | 5,129.4 t |
| 30 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 223 | 44m | 555 km | 2,135.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N748CB |  | Trenton Mercer Airport (KTTN) | Mar Bar L Farms Airport (NJ46) | 2026-08-18 13:17 UTC | 2026-08-18 14:51 UTC | 1h 33m |
| SFY207 | SFY | Wee Bee Sky Ranch Airport (70FA) | Fly In Ranches Airport (FD25) | 2026-08-18 14:13 UTC | 2026-08-18 14:47 UTC | 34m |
| N2268W |  | Chorman Airport (KD74) | Townsend A Airport (DE34) | 2026-08-18 14:14 UTC | 2026-08-18 14:44 UTC | 29m |
| RYR85ZZ | Ryanair | Decimomannu Airport (LIED) | Palma De Mallorca Airport (LEPA) | 2026-08-18 13:44 UTC | 2026-08-18 14:36 UTC | 52m |
| CGVFG | CGV | Calgary / Springbank Airport (CYBW) | Calgary / Springbank Airport (CYBW) | 2026-08-18 13:54 UTC | 2026-08-18 14:36 UTC | 41m |
| N85JA |  | John C Tune Airport (KJWN) | Springfield Robertson County Airport (KM91) | 2026-08-18 13:38 UTC | 2026-08-18 14:36 UTC | 58m |
| N4022W |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-08-18 14:01 UTC | 2026-08-18 14:36 UTC | 34m |
| N1759F |  | Tulsa International Airport (KTUL) | Dog Iron Ranch Airport (OK37) | 2026-08-18 14:04 UTC | 2026-08-18 14:35 UTC | 31m |
| AGV08 | AGV | Meiringen Airport (LSMM) | Meiringen Airport (LSMM) | 2026-08-18 14:22 UTC | 2026-08-18 14:32 UTC | 10m |
| N474AK |  | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-08-18 13:54 UTC | 2026-08-18 14:28 UTC | 33m |
| N79001 |  | St George Regional Airport (KSGU) | General Dick Stout Field (K1L8) | 2026-08-18 14:17 UTC | 2026-08-18 14:26 UTC | 9m |
| N6516Z |  | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-08-18 13:31 UTC | 2026-08-18 14:24 UTC | 52m |
| N234WL |  | Tweed/New Haven Airport (KHVN) | Laguardia Airport (KLGA) | 2026-08-18 13:55 UTC | 2026-08-18 14:23 UTC | 27m |
| N920CF |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-08-18 13:54 UTC | 2026-08-18 14:23 UTC | 28m |
| CXK168 | CXK | North Las Vegas Airport (KVGT) | Twentynine Palms Airport (KTNP) | 2026-08-18 12:51 UTC | 2026-08-18 14:23 UTC | 1h 31m |
| N9421E |  | Leesburg Executive Airport (KJYO) | Leesburg Executive Airport (KJYO) | 2026-08-18 13:50 UTC | 2026-08-18 14:22 UTC | 32m |
| N831MT |  | Boise Air Trml/Gowen Field (KBOI) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-18 12:50 UTC | 2026-08-18 14:20 UTC | 1h 30m |
| C6025 |  | St Pete-Clearwater International Airport (KPIE) | St Pete-Clearwater International Airport (KPIE) | 2026-08-18 14:02 UTC | 2026-08-18 14:18 UTC | 16m |
| PROVA85 | PRO | Salida/Harriett Alexander Field (KANK) | Central Colorado Regional Airport (KAEJ) | 2026-08-18 13:52 UTC | 2026-08-18 14:13 UTC | 20m |
| N1910R |  | Coban Airport (MGCB) | La Aurora Airport (MGGT) | 2026-08-18 13:56 UTC | 2026-08-18 14:12 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
