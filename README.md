# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_20:15:04_UTC-green)

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

**Latest saved flight:** 2026-09-24 20:15:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-24 20:15:04 UTC

- **268,546** saved flights
- **78,815** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **268,546** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,256,801.3 tonnes** estimated CO2 emissions
- **188,800,075 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10592 |
| 2 | SkyWest Airlines | 9349 |
| 3 | EJA | 5232 |
| 4 | IndiGo | 4499 |
| 5 | American Airlines | 4180 |
| 6 | Southwest Airlines | 3946 |
| 7 | Delta Air Lines | 3340 |
| 8 | ENY | 3155 |
| 9 | LATAM Airlines | 2586 |
| 10 | AZU | 2515 |
| 11 | Vueling | 2243 |
| 12 | WIF | 2186 |
| 13 | LXJ | 2113 |
| 14 | Lufthansa | 2045 |
| 15 | easyJet | 1804 |
| 16 | Swiss International | 1761 |
| 17 | QLK | 1732 |
| 18 | EJU | 1687 |
| 19 | AXM | 1673 |
| 20 | United Airlines | 1646 |
| 21 | Alaska Airlines | 1587 |
| 22 | All Nippon Airways | 1546 |
| 23 | PGT | 1511 |
| 24 | WMT | 1502 |
| 25 | GLO | 1496 |
| 26 | Air France | 1477 |
| 27 | VIV | 1465 |
| 28 | Wizz Air | 1458 |
| 29 | CXK | 1315 |
| 30 | AEE | 1292 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 223449 |
| 2 | 🇪🇸 ES | 16847 |
| 3 | 🇧🇷 BR | 15691 |
| 4 | 🇦🇺 AU | 15445 |
| 5 | 🇨🇦 CA | 14976 |
| 6 | 🇮🇹 IT | 14556 |
| 7 | 🇮🇳 IN | 14228 |
| 8 | 🇩🇪 DE | 12898 |
| 9 | 🇬🇧 GB | 12441 |
| 10 | 🇨🇴 CO | 12287 |
| 11 | 🇫🇷 FR | 10690 |
| 12 | 🇯🇵 JP | 10332 |
| 13 | 🇹🇷 TR | 8134 |
| 14 | 🇬🇷 GR | 7769 |
| 15 | 🇲🇽 MX | 7405 |
| 16 | 🇨🇭 CH | 7144 |
| 17 | 🇳🇴 NO | 6651 |
| 18 | 🇹🇭 TH | 4805 |
| 19 | 🇲🇾 MY | 4518 |
| 20 | 🇿🇦 ZA | 4490 |
| 21 | 🇵🇱 PL | 4402 |
| 22 | 🇳🇿 NZ | 3749 |
| 23 | 🇵🇭 PH | 3558 |
| 24 | 🇬🇹 GT | 3400 |
| 25 | 🇭🇷 HR | 3060 |
| 26 | 🇰🇷 KR | 3041 |
| 27 | 🇲🇦 MA | 2681 |
| 28 | 🇲🇪 ME | 2517 |
| 29 | 🇳🇱 NL | 2403 |
| 30 | 🇮🇩 ID | 2239 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5470 |
| 2 | Denver International Airport |  | US | 4367 |
| 3 | Indira Gandhi International Airport |  | IN | 3218 |
| 4 | Tokyo International Airport |  | JP | 3091 |
| 5 | El Dorado International Airport |  | CO | 2905 |
| 6 | Harry Reid International Airport |  | US | 2875 |
| 7 | Guaymaral Airport |  | CO | 2808 |
| 8 | Zurich Airport |  | CH | 2784 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2699 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2590 |
| 11 | La Aurora Airport |  | GT | 2584 |
| 12 | Salt Lake City International Airport |  | US | 2366 |
| 13 | Chicago O'Hare International Airport |  | US | 2299 |
| 14 | Congonhas Airport |  | BR | 2288 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2195 |
| 16 | Capua Airport |  | IT | 2092 |
| 17 | Madrid Barajas International Airport |  | ES | 2069 |
| 18 | Frankfurt am Main International Airport |  | DE | 2037 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2029 |
| 20 | Malpensa International Airport |  | IT | 1926 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1916 |
| 22 | Charles de Gaulle International Airport |  | FR | 1907 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1883 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1879 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1818 |
| 26 | Macau International Airport |  | MO | 1786 |
| 27 | Ninoy Aquino International Airport |  | PH | 1746 |
| 28 | Charlotte/Douglas International Airport |  | US | 1678 |
| 29 | Barcelona International Airport |  | ES | 1671 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1661 |
| 31 | Viracopos International Airport |  | BR | 1622 |
| 32 | Kuala Lumpur International Airport |  | MY | 1617 |
| 33 | Seattle-Tacoma International Airport |  | US | 1572 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1569 |
| 35 | Calgary International Airport |  | CA | 1529 |
| 36 | Don Mueang International Airport |  | TH | 1522 |
| 37 | Bengaluru International Airport |  | IN | 1513 |
| 38 | Oslo Gardermoen Airport |  | NO | 1509 |
| 39 | Vancouver International Airport |  | CA | 1503 |
| 40 | Antalya International Airport |  | TR | 1431 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1120 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1007 | 21m | 244 km | 4,240.2 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 741 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 676 | 1h 6m | 770 km | 8,980.1 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 669 | 24m | 225 km | 2,595.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 598 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 442 | 44m | 555 km | 4,232.4 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 431 | 27m | 275 km | 2,042.3 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 425 | 1h 50m | 1,423 km | 10,430.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 410 | 44m | 241 km | 1,703.1 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 384 | 24m | 218 km | 1,446.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 364 | 21m | 250 km | 1,572.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 360 | 23m | 55 km | 342.2 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 342 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 342 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 339 | 1h 6m | 706 km | 4,127.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 337 | 19m | 99 km | 577.3 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 335 | 26m | 215 km | 1,240.7 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 313 | 19m | 144 km | 778.6 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 304 | 1h 14m | 961 km | 5,039.0 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 293 | 42m | 535 km | 2,706.0 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 27 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 286 | 18m | 14 km | 71.5 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 284 | 28m | 152 km | 742.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 272 | 15m | 154 km | 720.7 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N508TJ |  | Genesee County Airport (KGVQ) | 6NK1 (6NK1) | 2026-09-24 19:05 UTC | 2026-09-24 20:15 UTC | 1h 9m |
| N6573D |  | Northwest Alabama Regional Airport (KMSL) | Northwest Alabama Regional Airport (KMSL) | 2026-09-24 19:11 UTC | 2026-09-24 20:08 UTC | 57m |
| XBJOR | XBJ | Hermanos Serdan International Airport (MMPB) | Ingeniero Juan Guillermo Villasana Airport (MMPC) | 2026-09-24 19:26 UTC | 2026-09-24 20:06 UTC | 40m |
| N527LP |  | Jake Arner Memorial Airport (K22N) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-09-24 19:45 UTC | 2026-09-24 20:04 UTC | 19m |
| N610FA |  | Allentown Queen City Municipal Airport (KXLL) | Capital City Airport (KCXY) | 2026-09-24 19:25 UTC | 2026-09-24 20:04 UTC | 38m |
| CFR93 | CFR | Chico Regional Airport (KCIC) | Rogers Field (KO05) | 2026-09-24 19:29 UTC | 2026-09-24 20:03 UTC | 33m |
| N6515G |  | Tacoma Narrows Airport (KTIW) | Olympia Regional Airport (KOLM) | 2026-09-24 19:22 UTC | 2026-09-24 20:02 UTC | 40m |
| N38549 |  | Laconia Municipal Airport (KLCI) | Lebanon Municipal Airport (KLEB) | 2026-09-24 19:32 UTC | 2026-09-24 20:01 UTC | 29m |
| N78ZG |  | City Of Colorado Springs Municipal Airport (KCOS) | Pueblo Memorial Airport (KPUB) | 2026-09-24 19:34 UTC | 2026-09-24 20:01 UTC | 26m |
| DAL2125 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | San Diego International Airport (KSAN) | 2026-09-24 16:38 UTC | 2026-09-24 19:57 UTC | 3h 19m |
| TORA11 | TOR | 75OK (75OK) | Ramey 1 Airport (0OK8) | 2026-09-24 19:37 UTC | 2026-09-24 19:53 UTC | 15m |
| CREEP31 | CRE | Enix Airport (OK51) | Ramey 1 Airport (0OK8) | 2026-09-24 19:17 UTC | 2026-09-24 19:50 UTC | 33m |
| KANTO81 | KAN | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-09-24 18:51 UTC | 2026-09-24 19:46 UTC | 55m |
| WIF149 | WIF | Oslo Gardermoen Airport (ENGM) | Gol Airport (ENKL) | 2026-09-24 19:11 UTC | 2026-09-24 19:46 UTC | 35m |
| N408RW |  | Key West International Airport (KEYW) | Key West International Airport (KEYW) | 2026-09-24 19:41 UTC | 2026-09-24 19:45 UTC | 4m |
|  |  | 97CL (97CL) | 97CL (97CL) | 2026-09-24 19:44 UTC | 2026-09-24 19:44 UTC | 0m |
| N300GV |  | Westchester County Airport (KHPN) | Suntime Airport (8NK6) | 2026-09-24 19:21 UTC | 2026-09-24 19:43 UTC | 22m |
| PAT963 | PAT | Dallas Executive Airport (KRBD) | 7Up Ranch Airport (75KS) | 2026-09-24 18:14 UTC | 2026-09-24 19:43 UTC | 1h 28m |
| UPS4 | UPS | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-09-24 08:38 UTC | 2026-09-24 19:42 UTC | 11h 3m |
| CXK226 | CXK | Hayward Executive Airport (KHWD) | Hayward Executive Airport (KHWD) | 2026-09-24 19:30 UTC | 2026-09-24 19:41 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
