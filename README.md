# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--31_19:56:49_UTC-green)

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

**Latest saved flight:** 2026-08-31 19:56:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-31 19:56:49 UTC

- **243,022** saved flights
- **73,670** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **243,022** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,925,081.3 tonnes** estimated CO2 emissions
- **169,569,932 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9764 |
| 2 | SkyWest Airlines | 8523 |
| 3 | EJA | 4699 |
| 4 | IndiGo | 4082 |
| 5 | American Airlines | 3915 |
| 6 | Southwest Airlines | 3652 |
| 7 | Delta Air Lines | 3101 |
| 8 | ENY | 2929 |
| 9 | LATAM Airlines | 2331 |
| 10 | AZU | 2258 |
| 11 | Vueling | 2083 |
| 12 | Lufthansa | 1951 |
| 13 | WIF | 1930 |
| 14 | LXJ | 1881 |
| 15 | easyJet | 1696 |
| 16 | Swiss International | 1638 |
| 17 | AXM | 1602 |
| 18 | EJU | 1561 |
| 19 | QLK | 1550 |
| 20 | United Airlines | 1529 |
| 21 | Alaska Airlines | 1452 |
| 22 | All Nippon Airways | 1434 |
| 23 | WMT | 1369 |
| 24 | GLO | 1358 |
| 25 | VIV | 1331 |
| 26 | PGT | 1330 |
| 27 | Air France | 1326 |
| 28 | Wizz Air | 1317 |
| 29 | AEE | 1201 |
| 30 | JetBlue | 1201 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 201366 |
| 2 | 🇪🇸 ES | 15623 |
| 3 | 🇧🇷 BR | 14167 |
| 4 | 🇦🇺 AU | 13785 |
| 5 | 🇨🇦 CA | 13513 |
| 6 | 🇮🇹 IT | 13315 |
| 7 | 🇮🇳 IN | 12710 |
| 8 | 🇩🇪 DE | 11993 |
| 9 | 🇬🇧 GB | 11480 |
| 10 | 🇨🇴 CO | 10495 |
| 11 | 🇫🇷 FR | 9800 |
| 12 | 🇯🇵 JP | 9717 |
| 13 | 🇹🇷 TR | 7227 |
| 14 | 🇬🇷 GR | 7169 |
| 15 | 🇲🇽 MX | 6700 |
| 16 | 🇨🇭 CH | 6541 |
| 17 | 🇳🇴 NO | 6010 |
| 18 | 🇹🇭 TH | 4397 |
| 19 | 🇲🇾 MY | 4297 |
| 20 | 🇿🇦 ZA | 4233 |
| 21 | 🇵🇱 PL | 4088 |
| 22 | 🇳🇿 NZ | 3340 |
| 23 | 🇵🇭 PH | 3326 |
| 24 | 🇬🇹 GT | 3059 |
| 25 | 🇰🇷 KR | 2860 |
| 26 | 🇭🇷 HR | 2804 |
| 27 | 🇲🇦 MA | 2462 |
| 28 | 🇲🇪 ME | 2270 |
| 29 | 🇳🇱 NL | 2198 |
| 30 | 🇮🇩 ID | 2118 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5017 |
| 2 | Denver International Airport |  | US | 3917 |
| 3 | Indira Gandhi International Airport |  | IN | 2960 |
| 4 | Tokyo International Airport |  | JP | 2892 |
| 5 | Guaymaral Airport |  | CO | 2707 |
| 6 | Harry Reid International Airport |  | US | 2580 |
| 7 | Zurich Airport |  | CH | 2552 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2483 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2426 |
| 10 | El Dorado International Airport |  | CO | 2381 |
| 11 | La Aurora Airport |  | GT | 2328 |
| 12 | Chicago O'Hare International Airport |  | US | 2151 |
| 13 | Salt Lake City International Airport |  | US | 2150 |
| 14 | Congonhas Airport |  | BR | 2074 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2014 |
| 16 | Frankfurt am Main International Airport |  | DE | 1920 |
| 17 | Capua Airport |  | IT | 1914 |
| 18 | Madrid Barajas International Airport |  | ES | 1909 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1823 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1788 |
| 21 | Malpensa International Airport |  | IT | 1736 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1718 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1703 |
| 24 | Charles de Gaulle International Airport |  | FR | 1701 |
| 25 | Macau International Airport |  | MO | 1619 |
| 26 | Ninoy Aquino International Airport |  | PH | 1617 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1556 |
| 28 | Charlotte/Douglas International Airport |  | US | 1554 |
| 29 | Kuala Lumpur International Airport |  | MY | 1549 |
| 30 | Barcelona International Airport |  | ES | 1544 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1470 |
| 32 | Viracopos International Airport |  | BR | 1444 |
| 33 | Seattle-Tacoma International Airport |  | US | 1423 |
| 34 | Don Mueang International Airport |  | TH | 1416 |
| 35 | Bengaluru International Airport |  | IN | 1410 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1409 |
| 37 | Calgary International Airport |  | CA | 1394 |
| 38 | Oslo Gardermoen Airport |  | NO | 1366 |
| 39 | Vancouver International Airport |  | CA | 1346 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1327 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1097 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 896 | 21m | 244 km | 3,772.8 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 627 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 617 | 24m | 225 km | 2,393.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 614 | 1h 6m | 770 km | 8,156.5 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 548 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 400 | 27m | 275 km | 1,895.4 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 382 | 1h 50m | 1,423 km | 9,374.9 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 371 | 44m | 555 km | 3,552.5 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 354 | 44m | 241 km | 1,470.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 347 | 21m | 250 km | 1,498.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 334 | 24m | 218 km | 1,258.3 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 322 | 1h 40m | 1,156 km | 6,423.8 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 322 | 22m | 55 km | 306.1 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 302 | 19m | 99 km | 517.3 t |
| 19 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 296 | 26m | 215 km | 1,096.3 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 286 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 282 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 279 | 1h 14m | 961 km | 4,624.6 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 274 | 19m | 144 km | 681.6 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 265 | 15m | 154 km | 702.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 262 | 1h 50m | 1,304 km | 5,894.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 251 | 28m | 152 km | 656.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LS09 |  | Gillespie Field (KSEE) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-31 19:44 UTC | 2026-08-31 19:56 UTC | 11m |
| N364RC |  | Dawson Municipal Airport (K16J) | Dawson Municipal Airport (K16J) | 2026-08-31 18:54 UTC | 2026-08-31 19:56 UTC | 1h 2m |
| CPA875 | Cathay Pacific | Dallas-Fort Worth International Airport (KDFW) | Chek Lap Kok International Airport (VHHH) | 2026-08-31 04:15 UTC | 2026-08-31 19:53 UTC | 15h 38m |
| BLINR17 | BLI | Samsarg Field (KN58) | Travis Afb Airport (KSUU) | 2026-08-31 19:14 UTC | 2026-08-31 19:53 UTC | 38m |
| LAE2873 | LAE | Los Angeles International Airport (KLAX) | El Dorado International Airport (SKBO) | 2026-08-31 13:08 UTC | 2026-08-31 19:51 UTC | 6h 43m |
| XSR362 | XSR | Colonel James Jabara Airport (KAAO) | Colonel James Jabara Airport (KAAO) | 2026-08-31 19:15 UTC | 2026-08-31 19:51 UTC | 35m |
| N91MF |  | Beaver Municipal Airport (KK44) | Higginsville Industrial Municipal Airport (KHIG) | 2026-08-31 18:33 UTC | 2026-08-31 19:46 UTC | 1h 13m |
| LCO3601 | LCO | Miami International Airport (KMIA) | Brussels Airport (EBBR) | 2026-08-31 11:22 UTC | 2026-08-31 19:43 UTC | 8h 20m |
| N9522S |  | Jim & Julie's Airport (96WA) | Jim & Julie's Airport (96WA) | 2026-08-31 19:29 UTC | 2026-08-31 19:41 UTC | 11m |
| N71AA |  | Easton State Airport (KESW) | Easton State Airport (KESW) | 2026-08-31 19:24 UTC | 2026-08-31 19:39 UTC | 15m |
| N118UV |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-08-31 18:41 UTC | 2026-08-31 19:33 UTC | 52m |
| N5314X |  | Felts Field (KSFF) | Boyle R & D Airport (63WA) | 2026-08-31 18:52 UTC | 2026-08-31 19:28 UTC | 36m |
| N478BC |  | Centennial Airport (KAPA) | Aero Bear Field (CD23) | 2026-08-31 18:37 UTC | 2026-08-31 19:26 UTC | 48m |
| LJY47 | LJY | West Virginia International Yeager Airport (KCRW) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-08-31 18:56 UTC | 2026-08-31 19:21 UTC | 24m |
| EJA835 | EJA | Martin State Airport (KMTN) | Key West International Airport (KEYW) | 2026-08-31 17:03 UTC | 2026-08-31 19:20 UTC | 2h 17m |
| N381SB |  | Lubbock Preston Smith International Airport (KLBB) | Fertile Municipal Airport (KD14) | 2026-08-31 16:25 UTC | 2026-08-31 19:20 UTC | 2h 55m |
| N484BW |  | Long Beach (Daugherty Field) Airport (KLGB) | Palm Springs International Airport (KPSP) | 2026-08-31 18:53 UTC | 2026-08-31 19:20 UTC | 26m |
| N661JM |  | Santa Barbara Municipal Airport (KSBA) | Telluride Regional Airport (KTEX) | 2026-08-31 17:50 UTC | 2026-08-31 19:19 UTC | 1h 28m |
| N25XM |  | North Las Vegas Airport (KVGT) | K36U (K36U) | 2026-08-31 18:02 UTC | 2026-08-31 19:18 UTC | 1h 16m |
| WIF42G | WIF | Brønnøysund Airport (ENBN) | Trondheim Airport Vaernes (ENVA) | 2026-08-31 18:39 UTC | 2026-08-31 19:15 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
