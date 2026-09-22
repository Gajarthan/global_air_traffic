# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_23:38:23_UTC-green)

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

**Latest saved flight:** 2026-09-21 23:38:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-21 23:38:23 UTC

- **265,925** saved flights
- **78,297** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **265,925** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,224,443.0 tonnes** estimated CO2 emissions
- **186,924,230 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10521 |
| 2 | SkyWest Airlines | 9258 |
| 3 | EJA | 5171 |
| 4 | IndiGo | 4463 |
| 5 | American Airlines | 4151 |
| 6 | Southwest Airlines | 3917 |
| 7 | Delta Air Lines | 3310 |
| 8 | ENY | 3130 |
| 9 | LATAM Airlines | 2562 |
| 10 | AZU | 2502 |
| 11 | Vueling | 2233 |
| 12 | WIF | 2150 |
| 13 | LXJ | 2089 |
| 14 | Lufthansa | 2039 |
| 15 | easyJet | 1788 |
| 16 | Swiss International | 1752 |
| 17 | QLK | 1716 |
| 18 | EJU | 1677 |
| 19 | AXM | 1664 |
| 20 | United Airlines | 1633 |
| 21 | Alaska Airlines | 1571 |
| 22 | All Nippon Airways | 1530 |
| 23 | PGT | 1495 |
| 24 | WMT | 1493 |
| 25 | GLO | 1483 |
| 26 | Air France | 1460 |
| 27 | VIV | 1456 |
| 28 | Wizz Air | 1447 |
| 29 | CXK | 1290 |
| 30 | AEE | 1284 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 221080 |
| 2 | 🇪🇸 ES | 16715 |
| 3 | 🇧🇷 BR | 15559 |
| 4 | 🇦🇺 AU | 15216 |
| 5 | 🇨🇦 CA | 14815 |
| 6 | 🇮🇹 IT | 14470 |
| 7 | 🇮🇳 IN | 14111 |
| 8 | 🇩🇪 DE | 12807 |
| 9 | 🇬🇧 GB | 12337 |
| 10 | 🇨🇴 CO | 12128 |
| 11 | 🇫🇷 FR | 10612 |
| 12 | 🇯🇵 JP | 10244 |
| 13 | 🇹🇷 TR | 8050 |
| 14 | 🇬🇷 GR | 7702 |
| 15 | 🇲🇽 MX | 7333 |
| 16 | 🇨🇭 CH | 7088 |
| 17 | 🇳🇴 NO | 6568 |
| 18 | 🇹🇭 TH | 4768 |
| 19 | 🇲🇾 MY | 4487 |
| 20 | 🇿🇦 ZA | 4466 |
| 21 | 🇵🇱 PL | 4371 |
| 22 | 🇳🇿 NZ | 3697 |
| 23 | 🇵🇭 PH | 3529 |
| 24 | 🇬🇹 GT | 3378 |
| 25 | 🇭🇷 HR | 3030 |
| 26 | 🇰🇷 KR | 3014 |
| 27 | 🇲🇦 MA | 2656 |
| 28 | 🇲🇪 ME | 2491 |
| 29 | 🇳🇱 NL | 2380 |
| 30 | 🇮🇩 ID | 2222 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5422 |
| 2 | Denver International Airport |  | US | 4320 |
| 3 | Indira Gandhi International Airport |  | IN | 3191 |
| 4 | Tokyo International Airport |  | JP | 3062 |
| 5 | El Dorado International Airport |  | CO | 2852 |
| 6 | Harry Reid International Airport |  | US | 2843 |
| 7 | Guaymaral Airport |  | CO | 2793 |
| 8 | Zurich Airport |  | CH | 2763 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2671 |
| 10 | La Aurora Airport |  | GT | 2566 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2565 |
| 12 | Salt Lake City International Airport |  | US | 2350 |
| 13 | Chicago O'Hare International Airport |  | US | 2285 |
| 14 | Congonhas Airport |  | BR | 2267 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2175 |
| 16 | Capua Airport |  | IT | 2083 |
| 17 | Madrid Barajas International Airport |  | ES | 2049 |
| 18 | Frankfurt am Main International Airport |  | DE | 2025 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2011 |
| 20 | Malpensa International Airport |  | IT | 1921 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1900 |
| 22 | Charles de Gaulle International Airport |  | FR | 1884 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1869 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1863 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1810 |
| 26 | Macau International Airport |  | MO | 1769 |
| 27 | Ninoy Aquino International Airport |  | PH | 1733 |
| 28 | Barcelona International Airport |  | ES | 1661 |
| 29 | Charlotte/Douglas International Airport |  | US | 1660 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1643 |
| 31 | Viracopos International Airport |  | BR | 1614 |
| 32 | Kuala Lumpur International Airport |  | MY | 1609 |
| 33 | Seattle-Tacoma International Airport |  | US | 1559 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1554 |
| 35 | Calgary International Airport |  | CA | 1518 |
| 36 | Don Mueang International Airport |  | TH | 1513 |
| 37 | Bengaluru International Airport |  | IN | 1502 |
| 38 | Oslo Gardermoen Airport |  | NO | 1496 |
| 39 | Vancouver International Airport |  | CA | 1487 |
| 40 | Antalya International Airport |  | TR | 1424 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1115 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 993 | 21m | 244 km | 4,181.2 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 735 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 667 | 1h 6m | 770 km | 8,860.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 661 | 24m | 225 km | 2,564.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 592 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 438 | 44m | 555 km | 4,194.1 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 426 | 27m | 275 km | 2,018.6 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 420 | 1h 50m | 1,423 km | 10,307.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 405 | 44m | 241 km | 1,682.3 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 381 | 24m | 218 km | 1,435.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 361 | 21m | 250 km | 1,559.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 352 | 23m | 55 km | 334.6 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 340 | 12m | - | - |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 336 | 19m | 99 km | 575.5 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 335 | 1h 6m | 706 km | 4,078.6 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 332 | 13m | - | - |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 330 | 26m | 215 km | 1,222.2 t |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 309 | 19m | 144 km | 768.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 288 | 42m | 535 km | 2,659.9 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 283 | 28m | 152 km | 739.6 t |
| 28 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 277 | 18m | 14 km | 69.3 t |
| 29 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N77NG |  | Montgomery-Gibbs Executive Airport (KMYF) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-09-21 23:08 UTC | 2026-09-21 23:38 UTC | 29m |
| UAL2297 | United Airlines | General Edward Lawrence Logan International Airport (KBOS) | Denver International Airport (KDEN) | 2026-09-21 19:28 UTC | 2026-09-21 23:27 UTC | 3h 59m |
| CPA252 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-09-21 11:56 UTC | 2026-09-21 23:27 UTC | 11h 31m |
| N739AJ |  | Laurel Municipal Airport (K6S8) | Laurel Municipal Airport (K6S8) | 2026-09-21 23:15 UTC | 2026-09-21 23:26 UTC | 10m |
| UAL336 | United Airlines | San Francisco International Airport (KSFO) | Washington Dulles International Airport (KIAD) | 2026-09-21 18:54 UTC | 2026-09-21 23:26 UTC | 4h 31m |
| LS18 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-21 21:40 UTC | 2026-09-21 23:23 UTC | 1h 42m |
| N97SU |  | UT80 (UT80) | UT80 (UT80) | 2026-09-21 23:06 UTC | 2026-09-21 23:18 UTC | 11m |
| ZKHZM | ZKH | Christchurch International Airport (NZCH) | West Melton Aerodrome (NZWL) | 2026-09-21 22:59 UTC | 2026-09-21 23:17 UTC | 18m |
| FFY309 | FFY | St Augustine Airport (KSGJ) | New Smyrna Beach Municipal (Jack Bolt Field) Airport (KEVB) | 2026-09-21 22:34 UTC | 2026-09-21 23:14 UTC | 40m |
| MMY57 | MMY | Redding Regional Airport (KRDD) | Red Bluff Municipal Airport (KRBL) | 2026-09-21 22:33 UTC | 2026-09-21 23:10 UTC | 36m |
| N499XX |  | Twentynine Palms Self Airport (KNXP) | Twentynine Palms Self Airport (KNXP) | 2026-09-21 22:54 UTC | 2026-09-21 23:09 UTC | 14m |
| KNG52 | KNG | RNZAF Base Ohakea (NZOH) | Murchison Airport (NZMR) | 2026-09-21 22:13 UTC | 2026-09-21 23:08 UTC | 55m |
| N630KB |  | Hayward Executive Airport (KHWD) | Mineta San Jose International Airport (KSJC) | 2026-09-21 22:05 UTC | 2026-09-21 23:02 UTC | 57m |
| N230DC |  | Brigham City Regional Airport (KBMC) | Malad City Airport (KMLD) | 2026-09-21 22:39 UTC | 2026-09-21 23:02 UTC | 23m |
| PTLUE | PTL | Hector International Airport (KFAR) | Vancouver International Airport (CYVR) | 2026-09-21 20:21 UTC | 2026-09-21 23:01 UTC | 2h 39m |
| N96AE |  | Capital City Airport (KFFT) | Blue Grass Airport (KLEX) | 2026-09-21 22:45 UTC | 2026-09-21 23:00 UTC | 14m |
| CFASA | CFA | Calgary / Springbank Airport (CYBW) | Calgary / Springbank Airport (CYBW) | 2026-09-21 22:34 UTC | 2026-09-21 22:57 UTC | 23m |
| N118PA |  | Point Mugu Nas (Naval Base Ventura Co) Airport (KNTD) | Kelso Valley Airport (CN37) | 2026-09-21 22:24 UTC | 2026-09-21 22:55 UTC | 30m |
| JSX775 | JSX | Hollywood Burbank Airport (KBUR) | K4SD (K4SD) | 2026-09-21 21:57 UTC | 2026-09-21 22:55 UTC | 57m |
| PNC0250 | PNC | El Dorado International Airport (SKBO) | Tolemaida Air Base (SKTI) | 2026-09-21 22:42 UTC | 2026-09-21 22:53 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
