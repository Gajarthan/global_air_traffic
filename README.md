# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_11:09:42_UTC-green)

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

**Latest saved flight:** 2026-08-25 11:09:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 11:09:42 UTC

- **234,805** saved flights
- **71,903** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **234,805** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,829,260.5 tonnes** estimated CO2 emissions
- **164,015,102 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9409 |
| 2 | SkyWest Airlines | 8299 |
| 3 | EJA | 4553 |
| 4 | IndiGo | 3973 |
| 5 | American Airlines | 3815 |
| 6 | Southwest Airlines | 3599 |
| 7 | Delta Air Lines | 2991 |
| 8 | ENY | 2854 |
| 9 | LATAM Airlines | 2253 |
| 10 | AZU | 2185 |
| 11 | Vueling | 2011 |
| 12 | Lufthansa | 1911 |
| 13 | WIF | 1866 |
| 14 | LXJ | 1844 |
| 15 | easyJet | 1637 |
| 16 | Swiss International | 1576 |
| 17 | AXM | 1574 |
| 18 | EJU | 1502 |
| 19 | QLK | 1497 |
| 20 | United Airlines | 1484 |
| 21 | Alaska Airlines | 1417 |
| 22 | All Nippon Airways | 1401 |
| 23 | GLO | 1307 |
| 24 | WMT | 1305 |
| 25 | VIV | 1294 |
| 26 | PGT | 1280 |
| 27 | Air France | 1278 |
| 28 | Wizz Air | 1246 |
| 29 | AEE | 1167 |
| 30 | JetBlue | 1162 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 195118 |
| 2 | 🇪🇸 ES | 15091 |
| 3 | 🇧🇷 BR | 13690 |
| 4 | 🇦🇺 AU | 13332 |
| 5 | 🇨🇦 CA | 12982 |
| 6 | 🇮🇹 IT | 12766 |
| 7 | 🇮🇳 IN | 12368 |
| 8 | 🇩🇪 DE | 11570 |
| 9 | 🇬🇧 GB | 11066 |
| 10 | 🇨🇴 CO | 9856 |
| 11 | 🇯🇵 JP | 9541 |
| 12 | 🇫🇷 FR | 9405 |
| 13 | 🇹🇷 TR | 6960 |
| 14 | 🇬🇷 GR | 6915 |
| 15 | 🇲🇽 MX | 6528 |
| 16 | 🇨🇭 CH | 6264 |
| 17 | 🇳🇴 NO | 5801 |
| 18 | 🇲🇾 MY | 4215 |
| 19 | 🇹🇭 TH | 4197 |
| 20 | 🇿🇦 ZA | 4107 |
| 21 | 🇵🇱 PL | 3917 |
| 22 | 🇳🇿 NZ | 3247 |
| 23 | 🇵🇭 PH | 3235 |
| 24 | 🇬🇹 GT | 2935 |
| 25 | 🇰🇷 KR | 2755 |
| 26 | 🇭🇷 HR | 2698 |
| 27 | 🇲🇦 MA | 2380 |
| 28 | 🇲🇪 ME | 2173 |
| 29 | 🇳🇱 NL | 2105 |
| 30 | 🇮🇩 ID | 2052 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4874 |
| 2 | Denver International Airport |  | US | 3799 |
| 3 | Indira Gandhi International Airport |  | IN | 2867 |
| 4 | Tokyo International Airport |  | JP | 2840 |
| 5 | Guaymaral Airport |  | CO | 2677 |
| 6 | Harry Reid International Airport |  | US | 2518 |
| 7 | Zurich Airport |  | CH | 2457 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2396 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2353 |
| 10 | La Aurora Airport |  | GT | 2236 |
| 11 | El Dorado International Airport |  | CO | 2198 |
| 12 | Chicago O'Hare International Airport |  | US | 2117 |
| 13 | Salt Lake City International Airport |  | US | 2069 |
| 14 | Congonhas Airport |  | BR | 1998 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1973 |
| 16 | Frankfurt am Main International Airport |  | DE | 1869 |
| 17 | Capua Airport |  | IT | 1848 |
| 18 | Madrid Barajas International Airport |  | ES | 1846 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1765 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1732 |
| 21 | Malpensa International Airport |  | IT | 1682 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1664 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1649 |
| 24 | Charles de Gaulle International Airport |  | FR | 1634 |
| 25 | Macau International Airport |  | MO | 1608 |
| 26 | Ninoy Aquino International Airport |  | PH | 1562 |
| 27 | Kuala Lumpur International Airport |  | MY | 1524 |
| 28 | Charlotte/Douglas International Airport |  | US | 1515 |
| 29 | Barcelona International Airport |  | ES | 1484 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1443 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1420 |
| 32 | Viracopos International Airport |  | BR | 1396 |
| 33 | Bengaluru International Airport |  | IN | 1379 |
| 34 | Seattle-Tacoma International Airport |  | US | 1378 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1377 |
| 36 | Don Mueang International Airport |  | TH | 1364 |
| 37 | Calgary International Airport |  | CA | 1345 |
| 38 | Oslo Gardermoen Airport |  | NO | 1314 |
| 39 | Vancouver International Airport |  | CA | 1282 |
| 40 | O. R. Tambo International Airport |  | ZA | 1277 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1085 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 862 | 21m | 244 km | 3,629.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 596 | 1h 6m | 770 km | 7,917.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 595 | 24m | 225 km | 2,308.3 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 584 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 523 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 387 | 27m | 275 km | 1,833.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 363 | 1h 50m | 1,423 km | 8,908.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 361 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 341 | 44m | 555 km | 3,265.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 340 | 44m | 241 km | 1,412.3 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 330 | 21m | 250 km | 1,425.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 317 | 1h 7m | 706 km | 3,859.5 t |
| 14 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 314 | 24m | 218 km | 1,183.0 t |
| 15 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 308 | 1h 39m | 1,156 km | 6,144.5 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 290 | 19m | 99 km | 496.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 288 | 27m | 215 km | 1,066.6 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 273 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 272 | 1h 14m | 961 km | 4,508.5 t |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 267 | 29m | 304 km | 1,399.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 267 | 19m | 144 km | 664.1 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 261 | 15m | 154 km | 691.5 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 251 | 1h 50m | 1,304 km | 5,646.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ERU957 | ERU | Daytona Beach International Airport (KDAB) | Ormond Beach Municipal Airport (KOMN) | 2026-08-25 10:35 UTC | 2026-08-25 11:09 UTC | 33m |
| CFC2978 | CFC | Satenas Air Base (ESIB) | Khrabrovo Airport (UMKK) | 2026-08-25 09:56 UTC | 2026-08-25 11:05 UTC | 1h 9m |
| HBZPV | HBZ | Courchevel Airport (LFLJ) | Reichenbach Air Base (LSGR) | 2026-08-25 10:34 UTC | 2026-08-25 11:04 UTC | 30m |
| EFC39R | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-25 10:52 UTC | 2026-08-25 11:03 UTC | 11m |
| N627RG |  | Harford County Airport (K0W3) | Ocean City Municipal Airport (KOXB) | 2026-08-25 10:20 UTC | 2026-08-25 10:58 UTC | 37m |
| HBZZT | HBZ | Ambri Airport (LSPM) | Ambri Airport (LSPM) | 2026-08-25 10:54 UTC | 2026-08-25 10:56 UTC | 2m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | KXTA (KXTA) | 2026-08-25 10:40 UTC | 2026-08-25 10:54 UTC | 13m |
| BBC373 | BBC | VGZR (VGZR) | Tribhuvan International Airport (VNKT) | 2026-08-25 09:48 UTC | 2026-08-25 10:52 UTC | 1h 3m |
| KAL695 | Korean Air | Incheon International Airport (RKSI) | Simara Airport (VNSI) | 2026-08-25 05:16 UTC | 2026-08-25 10:51 UTC | 5h 34m |
| AIC219 | Air India | Indira Gandhi International Airport (VIDP) | Langtang Airport (VNLT) | 2026-08-25 09:29 UTC | 2026-08-25 10:49 UTC | 1h 19m |
| N400BC |  | Calais-Dunkerque Airport (LFAC) | Lyon Saint-Exupery Airport (LFLL) | 2026-08-25 09:54 UTC | 2026-08-25 10:48 UTC | 54m |
| N378EA |  | K00V (K00V) | Lone Tree Ranch Airport (35CO) | 2026-08-25 10:20 UTC | 2026-08-25 10:43 UTC | 23m |
| QLK1575 | QLK | Gold Coast Airport (YBCG) | Melbourne International Airport (YMML) | 2026-08-25 08:30 UTC | 2026-08-25 10:40 UTC | 2h 9m |
| CFE801 | CFE | Linate Airport (LIML) | London City Airport (EGLC) | 2026-08-25 09:03 UTC | 2026-08-25 10:40 UTC | 1h 36m |
| TDT12 | TDT | Cranfield Airport (EGTC) | Bournemouth Airport (EGHH) | 2026-08-25 10:00 UTC | 2026-08-25 10:39 UTC | 39m |
| SEH4JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-08-25 10:10 UTC | 2026-08-25 10:37 UTC | 27m |
| ADO87 | ADO | Tokyo International Airport (RJTT) | Asahikawa Airport (RJEC) | 2026-08-25 09:18 UTC | 2026-08-25 10:32 UTC | 1h 14m |
| HUE28P | HUE | Nice-Cote d'Azur Airport (LFMN) | Sondrio Caiolo Airport (LILO) | 2026-08-25 09:40 UTC | 2026-08-25 10:32 UTC | 52m |
| SPOSL | SPO | Lubin Airport (EPLU) | Jeżów Sudecki Airport (EPJS) | 2026-08-25 07:04 UTC | 2026-08-25 10:29 UTC | 3h 25m |
| JAF3NE | JAF | Malaga Airport (LEMG) | Brussels Airport (EBBR) | 2026-08-25 08:17 UTC | 2026-08-25 10:26 UTC | 2h 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
