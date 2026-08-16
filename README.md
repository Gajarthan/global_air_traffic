# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_19:15:58_UTC-green)

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

**Latest saved flight:** 2026-08-16 19:15:58 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 19:15:58 UTC

- **205,833** saved flights
- **65,659** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **205,833** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,474,437.9 tonnes** estimated CO2 emissions
- **143,445,676 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8116 |
| 2 | SkyWest Airlines | 7390 |
| 3 | EJA | 3990 |
| 4 | IndiGo | 3521 |
| 5 | American Airlines | 3422 |
| 6 | Southwest Airlines | 3313 |
| 7 | Delta Air Lines | 2639 |
| 8 | ENY | 2568 |
| 9 | LATAM Airlines | 1932 |
| 10 | AZU | 1864 |
| 11 | Lufthansa | 1749 |
| 12 | Vueling | 1705 |
| 13 | WIF | 1656 |
| 14 | LXJ | 1625 |
| 15 | easyJet | 1422 |
| 16 | Swiss International | 1373 |
| 17 | AXM | 1339 |
| 18 | United Airlines | 1298 |
| 19 | Alaska Airlines | 1277 |
| 20 | QLK | 1261 |
| 21 | EJU | 1260 |
| 22 | All Nippon Airways | 1245 |
| 23 | VIV | 1130 |
| 24 | GLO | 1107 |
| 25 | Air France | 1101 |
| 26 | PGT | 1099 |
| 27 | JetBlue | 1055 |
| 28 | AEE | 1051 |
| 29 | WMT | 1037 |
| 30 | CXK | 1015 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 174881 |
| 2 | 🇪🇸 ES | 13159 |
| 3 | 🇧🇷 BR | 11785 |
| 4 | 🇦🇺 AU | 11483 |
| 5 | 🇨🇦 CA | 11355 |
| 6 | 🇮🇳 IN | 10986 |
| 7 | 🇮🇹 IT | 10738 |
| 8 | 🇩🇪 DE | 10194 |
| 9 | 🇬🇧 GB | 9599 |
| 10 | 🇯🇵 JP | 8453 |
| 11 | 🇫🇷 FR | 8157 |
| 12 | 🇨🇴 CO | 8152 |
| 13 | 🇬🇷 GR | 6061 |
| 14 | 🇹🇷 TR | 5834 |
| 15 | 🇲🇽 MX | 5783 |
| 16 | 🇨🇭 CH | 5507 |
| 17 | 🇳🇴 NO | 5130 |
| 18 | 🇲🇾 MY | 3529 |
| 19 | 🇿🇦 ZA | 3454 |
| 20 | 🇵🇱 PL | 3396 |
| 21 | 🇹🇭 TH | 3246 |
| 22 | 🇳🇿 NZ | 2843 |
| 23 | 🇵🇭 PH | 2729 |
| 24 | 🇬🇹 GT | 2608 |
| 25 | 🇰🇷 KR | 2505 |
| 26 | 🇭🇷 HR | 2201 |
| 27 | 🇲🇦 MA | 2078 |
| 28 | 🇳🇱 NL | 1836 |
| 29 | 🇲🇪 ME | 1730 |
| 30 | 🇮🇩 ID | 1686 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4322 |
| 2 | Denver International Airport |  | US | 3359 |
| 3 | Tokyo International Airport |  | JP | 2550 |
| 4 | Indira Gandhi International Airport |  | IN | 2492 |
| 5 | Guaymaral Airport |  | CO | 2490 |
| 6 | Harry Reid International Airport |  | US | 2326 |
| 7 | Zurich Airport |  | CH | 2150 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2149 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2135 |
| 10 | La Aurora Airport |  | GT | 1990 |
| 11 | Chicago O'Hare International Airport |  | US | 1908 |
| 12 | El Dorado International Airport |  | CO | 1875 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1837 |
| 14 | Salt Lake City International Airport |  | US | 1821 |
| 15 | Congonhas Airport |  | BR | 1715 |
| 16 | Frankfurt am Main International Airport |  | DE | 1706 |
| 17 | Madrid Barajas International Airport |  | ES | 1615 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1572 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1565 |
| 20 | Capua Airport |  | IT | 1563 |
| 21 | Macau International Airport |  | MO | 1542 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1489 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1436 |
| 24 | Malpensa International Airport |  | IT | 1419 |
| 25 | Charles de Gaulle International Airport |  | FR | 1412 |
| 26 | Charlotte/Douglas International Airport |  | US | 1403 |
| 27 | Kuala Lumpur International Airport |  | MY | 1309 |
| 28 | Ninoy Aquino International Airport |  | PH | 1293 |
| 29 | Bengaluru International Airport |  | IN | 1276 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1269 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1238 |
| 32 | Barcelona International Airport |  | ES | 1225 |
| 33 | Seattle-Tacoma International Airport |  | US | 1220 |
| 34 | Viracopos International Airport |  | BR | 1193 |
| 35 | Calgary International Airport |  | CA | 1163 |
| 36 | Reno/Tahoe International Airport |  | US | 1139 |
| 37 | Oslo Gardermoen Airport |  | NO | 1137 |
| 38 | Vitoria/Foronda Airport |  | ES | 1135 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1106 |
| 40 | Daniel K Inouye International Airport |  | US | 1103 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1025 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 500 | 1h 7m | 770 km | 6,642.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 478 | 24m | 225 km | 1,854.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 469 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 395 | 8m | - | - |
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
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 256 | 24m | 218 km | 964.5 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 250 | 27m | 215 km | 925.9 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 248 | 19m | 99 km | 424.8 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 247 | 1h 14m | 961 km | 4,094.2 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 242 | 1h 37m | 1,156 km | 4,827.8 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 236 | 19m | 144 km | 587.0 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 233 | 31m | 369 km | 1,483.1 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 222 | 1h 49m | 1,304 km | 4,994.4 t |
| 29 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 220 | 28m | 152 km | 574.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UAL1149 | United Airlines | San Francisco International Airport (KSFO) | Newark Liberty International Airport (KEWR) | 2026-08-16 14:25 UTC | 2026-08-16 19:15 UTC | 4h 50m |
| CGRQH | CGR | Prince George Airport (CYXS) | Prince George Airport (CYXS) | 2026-08-16 19:01 UTC | 2026-08-16 19:13 UTC | 11m |
| N89PS |  | Gary/Chicago International Airport (KGYY) | Chicago Midway International Airport (KMDW) | 2026-08-16 19:01 UTC | 2026-08-16 19:08 UTC | 7m |
| BOE962 | BOE | Boeing Field/King County International Airport (KBFI) | Warden Airport (K2S4) | 2026-08-16 17:48 UTC | 2026-08-16 19:06 UTC | 1h 18m |
| AUA26Z | Austrian Airlines | Berlin Brandenburg Airport (EDDB) | Vienna International Airport (LOWW) | 2026-08-16 18:09 UTC | 2026-08-16 19:00 UTC | 51m |
| N29GB |  | Double Eagle Ii Airport (KAEG) | Double Eagle Ii Airport (KAEG) | 2026-08-16 18:58 UTC | 2026-08-16 18:59 UTC | 1m |
| N44SN |  | Central Florida Airpark (2FA6) | Leeward Air Ranch Airport (FD04) | 2026-08-16 18:43 UTC | 2026-08-16 18:59 UTC | 15m |
| CGNSS | CGN | Tumbler Ridge Airport (CBX7) | Tumbler Ridge Airport (CBX7) | 2026-08-16 18:45 UTC | 2026-08-16 18:57 UTC | 12m |
| N246SF |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-08-16 18:00 UTC | 2026-08-16 18:57 UTC | 57m |
| EJM393 | EJM | Ohio State University Airport (KOSU) | Bellingham International Airport (KBLI) | 2026-08-16 13:59 UTC | 2026-08-16 18:57 UTC | 4h 57m |
| AAL2088 | American Airlines | Laguardia Airport (KLGA) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-16 15:55 UTC | 2026-08-16 18:57 UTC | 3h 1m |
| SVX46 | SVX | Ted Stevens Anchorage International Airport (PANC) | Grebe Lake Airport (AK45) | 2026-08-16 17:00 UTC | 2026-08-16 18:56 UTC | 1h 55m |
| XBNLT | XBN | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-08-16 18:31 UTC | 2026-08-16 18:55 UTC | 24m |
| N748RM |  | Graham Municipal Airport (KRPH) | Dallas Love Field (KDAL) | 2026-08-16 18:29 UTC | 2026-08-16 18:54 UTC | 25m |
| N737HJ |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-08-16 18:05 UTC | 2026-08-16 18:54 UTC | 48m |
| CNS2041 | CNS | Charles M Schulz/Sonoma County Airport (KSTS) | Telluride Regional Airport (KTEX) | 2026-08-16 17:08 UTC | 2026-08-16 18:53 UTC | 1h 45m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-08-16 18:37 UTC | 2026-08-16 18:52 UTC | 14m |
| N330V |  | Kintail Farm Airport (GA00) | Cy Nunnally Memorial Airport (KD73) | 2026-08-16 18:04 UTC | 2026-08-16 18:49 UTC | 45m |
| LOT3825 | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Gdańsk Lech Wałęsa Airport (EPGD) | 2026-08-16 18:13 UTC | 2026-08-16 18:46 UTC | 32m |
| N4958A |  | Montgomery-Gibbs Executive Airport (KMYF) | Santa Monica Municipal Airport (KSMO) | 2026-08-16 17:33 UTC | 2026-08-16 18:45 UTC | 1h 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
