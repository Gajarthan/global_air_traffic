# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--09_21:05:58_UTC-green)

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

**Latest saved flight:** 2026-09-09 21:05:58 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-09 21:05:58 UTC

- **252,949** saved flights
- **75,726** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **252,949** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,047,600.2 tonnes** estimated CO2 emissions
- **176,672,476 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10117 |
| 2 | SkyWest Airlines | 8825 |
| 3 | EJA | 4886 |
| 4 | IndiGo | 4237 |
| 5 | American Airlines | 4030 |
| 6 | Southwest Airlines | 3740 |
| 7 | Delta Air Lines | 3190 |
| 8 | ENY | 3017 |
| 9 | LATAM Airlines | 2434 |
| 10 | AZU | 2351 |
| 11 | Vueling | 2152 |
| 12 | WIF | 2026 |
| 13 | Lufthansa | 1994 |
| 14 | LXJ | 1973 |
| 15 | easyJet | 1732 |
| 16 | Swiss International | 1699 |
| 17 | AXM | 1630 |
| 18 | QLK | 1622 |
| 19 | EJU | 1620 |
| 20 | United Airlines | 1575 |
| 21 | Alaska Airlines | 1508 |
| 22 | All Nippon Airways | 1478 |
| 23 | WMT | 1433 |
| 24 | GLO | 1406 |
| 25 | PGT | 1391 |
| 26 | VIV | 1382 |
| 27 | Air France | 1379 |
| 28 | Wizz Air | 1378 |
| 29 | JetBlue | 1235 |
| 30 | AEE | 1233 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 209925 |
| 2 | 🇪🇸 ES | 16146 |
| 3 | 🇧🇷 BR | 14751 |
| 4 | 🇦🇺 AU | 14381 |
| 5 | 🇨🇦 CA | 14060 |
| 6 | 🇮🇹 IT | 13858 |
| 7 | 🇮🇳 IN | 13251 |
| 8 | 🇩🇪 DE | 12392 |
| 9 | 🇬🇧 GB | 11835 |
| 10 | 🇨🇴 CO | 11191 |
| 11 | 🇫🇷 FR | 10172 |
| 12 | 🇯🇵 JP | 9922 |
| 13 | 🇹🇷 TR | 7570 |
| 14 | 🇬🇷 GR | 7410 |
| 15 | 🇲🇽 MX | 6970 |
| 16 | 🇨🇭 CH | 6811 |
| 17 | 🇳🇴 NO | 6259 |
| 18 | 🇹🇭 TH | 4549 |
| 19 | 🇲🇾 MY | 4385 |
| 20 | 🇿🇦 ZA | 4325 |
| 21 | 🇵🇱 PL | 4211 |
| 22 | 🇳🇿 NZ | 3450 |
| 23 | 🇵🇭 PH | 3428 |
| 24 | 🇬🇹 GT | 3146 |
| 25 | 🇰🇷 KR | 2914 |
| 26 | 🇭🇷 HR | 2907 |
| 27 | 🇲🇦 MA | 2555 |
| 28 | 🇲🇪 ME | 2379 |
| 29 | 🇳🇱 NL | 2280 |
| 30 | 🇮🇩 ID | 2162 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5211 |
| 2 | Denver International Airport |  | US | 4086 |
| 3 | Indira Gandhi International Airport |  | IN | 3068 |
| 4 | Tokyo International Airport |  | JP | 2960 |
| 5 | Guaymaral Airport |  | CO | 2747 |
| 6 | Harry Reid International Airport |  | US | 2686 |
| 7 | Zurich Airport |  | CH | 2648 |
| 8 | El Dorado International Airport |  | CO | 2587 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2561 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2491 |
| 11 | La Aurora Airport |  | GT | 2400 |
| 12 | Salt Lake City International Airport |  | US | 2230 |
| 13 | Chicago O'Hare International Airport |  | US | 2206 |
| 14 | Congonhas Airport |  | BR | 2165 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2076 |
| 16 | Capua Airport |  | IT | 1996 |
| 17 | Madrid Barajas International Airport |  | ES | 1986 |
| 18 | Frankfurt am Main International Airport |  | DE | 1963 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1892 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1839 |
| 21 | Malpensa International Airport |  | IT | 1819 |
| 22 | Charles de Gaulle International Airport |  | FR | 1773 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1772 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1760 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1692 |
| 26 | Ninoy Aquino International Airport |  | PH | 1675 |
| 27 | Macau International Airport |  | MO | 1667 |
| 28 | Barcelona International Airport |  | ES | 1592 |
| 29 | Charlotte/Douglas International Airport |  | US | 1591 |
| 30 | Kuala Lumpur International Airport |  | MY | 1579 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1555 |
| 32 | Viracopos International Airport |  | BR | 1509 |
| 33 | Seattle-Tacoma International Airport |  | US | 1490 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1464 |
| 35 | Calgary International Airport |  | CA | 1458 |
| 36 | Don Mueang International Airport |  | TH | 1456 |
| 37 | Bengaluru International Airport |  | IN | 1443 |
| 38 | Oslo Gardermoen Airport |  | NO | 1427 |
| 39 | Vancouver International Airport |  | CA | 1417 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1367 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 939 | 21m | 244 km | 3,953.9 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 676 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 637 | 24m | 225 km | 2,471.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 634 | 1h 6m | 770 km | 8,422.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 566 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 415 | 27m | 275 km | 1,966.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 403 | 1h 50m | 1,423 km | 9,890.3 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 398 | 44m | 555 km | 3,811.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 380 | 44m | 241 km | 1,578.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 372 | 35m | - | - |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 353 | 21m | 250 km | 1,524.7 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 352 | 24m | 218 km | 1,326.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 337 | 23m | 55 km | 320.3 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 312 | 26m | 215 km | 1,155.5 t |
| 18 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 306 | 19m | 99 km | 524.2 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 301 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 296 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 290 | 1h 14m | 961 km | 4,806.9 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 289 | 19m | 144 km | 718.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 274 | 1h 50m | 1,304 km | 6,164.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 262 | 41m | 535 km | 2,419.7 t |
| 29 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 258 | 28m | 152 km | 674.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N872SP |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-09-09 20:17 UTC | 2026-09-09 21:05 UTC | 48m |
| N5275S |  | Centennial Airport (KAPA) | Pueblo Memorial Airport (KPUB) | 2026-09-09 20:05 UTC | 2026-09-09 20:58 UTC | 52m |
| GIZMO31 | GIZ | 75OK (75OK) | Lariat Ranch Airport (OK42) | 2026-09-09 20:40 UTC | 2026-09-09 20:54 UTC | 13m |
| ROKT71 | ROK | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Bird Nest Airport (4MS5) | 2026-09-09 20:32 UTC | 2026-09-09 20:52 UTC | 20m |
| CXK102 | CXK | Harrisburg International Airport (KMDT) | Lancaster Airport (KLNS) | 2026-09-09 20:34 UTC | 2026-09-09 20:52 UTC | 18m |
| N8425F |  | Anniston Regional Airport (KANB) | Auburn University Regional Airport (KAUO) | 2026-09-09 20:04 UTC | 2026-09-09 20:50 UTC | 46m |
| ANVIL11 | ANV | Fairchild Afb Airport (KSKA) | Fairchild Afb Airport (KSKA) | 2026-09-09 19:06 UTC | 2026-09-09 20:47 UTC | 1h 41m |
| G72252 |  | Mcnary Field (KSLE) | Mcnary Field (KSLE) | 2026-09-09 19:19 UTC | 2026-09-09 20:45 UTC | 1h 26m |
| N204DR |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-09-09 20:17 UTC | 2026-09-09 20:43 UTC | 25m |
| TAHOE51 | TAH | Randolph Afb Airport (KRND) | Tee Pee Creek Airport (8TE0) | 2026-09-09 20:09 UTC | 2026-09-09 20:40 UTC | 30m |
| UAL1650 | United Airlines | Okc Will Rogers International Airport (KOKC) | Chicago O'Hare International Airport (KORD) | 2026-09-09 18:26 UTC | 2026-09-09 20:39 UTC | 2h 12m |
| LS21 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-09 19:05 UTC | 2026-09-09 20:39 UTC | 1h 33m |
| ETD206 | Etihad Airways | OM11 (OM11) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-09 18:19 UTC | 2026-09-09 20:36 UTC | 2h 17m |
| UAE248 | Emirates | Galeao - Antonio Carlos Jobim International Airport (SBGL) | Fujairah International Airport (OMFJ) | 2026-09-09 06:52 UTC | 2026-09-09 20:36 UTC | 13h 44m |
| N203DH |  | Ted Stevens Anchorage International Airport (PANC) | King Salmon Airport (PAKN) | 2026-09-09 18:51 UTC | 2026-09-09 20:34 UTC | 1h 42m |
| VILLN11 | VIL | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | Rancho San Simeon Airport (66CA) | 2026-09-09 19:54 UTC | 2026-09-09 20:33 UTC | 39m |
| BYF31 | BYF | San Carlos Airport (KSQL) | Buchanan Field (KCCR) | 2026-09-09 20:07 UTC | 2026-09-09 20:31 UTC | 23m |
| N312EH |  | Bentonville Municipal/Louise M Thaden Field (KVBT) | Lynch Field (44MU) | 2026-09-09 20:13 UTC | 2026-09-09 20:31 UTC | 17m |
| CFXEP | CFX | Montréal (Mirabel) Airport (CYMX) | Montréal (Mirabel) Airport (CYMX) | 2026-09-09 20:08 UTC | 2026-09-09 20:30 UTC | 21m |
| FAC5760 | FAC | Ernesto Cortissoz International Airport (SKBQ) | Alfonso Lopez Pumarejo Airport (SKVP) | 2026-09-09 20:11 UTC | 2026-09-09 20:29 UTC | 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
