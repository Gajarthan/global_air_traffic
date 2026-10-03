# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_13:23:40_UTC-green)

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

**Latest saved flight:** 2026-10-03 13:23:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-10-03 13:23:40 UTC

- **275,285** saved flights
- **80,199** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **275,285** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,330,943.8 tonnes** estimated CO2 emissions
- **193,098,190 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10796 |
| 2 | SkyWest Airlines | 9572 |
| 3 | EJA | 5391 |
| 4 | IndiGo | 4593 |
| 5 | American Airlines | 4257 |
| 6 | Southwest Airlines | 4043 |
| 7 | Delta Air Lines | 3418 |
| 8 | ENY | 3220 |
| 9 | LATAM Airlines | 2668 |
| 10 | AZU | 2589 |
| 11 | Vueling | 2285 |
| 12 | WIF | 2242 |
| 13 | LXJ | 2173 |
| 14 | Lufthansa | 2071 |
| 15 | easyJet | 1830 |
| 16 | Swiss International | 1804 |
| 17 | QLK | 1775 |
| 18 | EJU | 1711 |
| 19 | AXM | 1689 |
| 20 | United Airlines | 1678 |
| 21 | Alaska Airlines | 1622 |
| 22 | All Nippon Airways | 1572 |
| 23 | PGT | 1548 |
| 24 | GLO | 1536 |
| 25 | WMT | 1531 |
| 26 | Air France | 1510 |
| 27 | VIV | 1509 |
| 28 | Wizz Air | 1488 |
| 29 | CXK | 1357 |
| 30 | AEE | 1309 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 229603 |
| 2 | 🇪🇸 ES | 17218 |
| 3 | 🇧🇷 BR | 16171 |
| 4 | 🇦🇺 AU | 15881 |
| 5 | 🇨🇦 CA | 15342 |
| 6 | 🇮🇹 IT | 14838 |
| 7 | 🇮🇳 IN | 14528 |
| 8 | 🇩🇪 DE | 13168 |
| 9 | 🇨🇴 CO | 12768 |
| 10 | 🇬🇧 GB | 12677 |
| 11 | 🇫🇷 FR | 10883 |
| 12 | 🇯🇵 JP | 10502 |
| 13 | 🇹🇷 TR | 8318 |
| 14 | 🇬🇷 GR | 7900 |
| 15 | 🇲🇽 MX | 7604 |
| 16 | 🇨🇭 CH | 7317 |
| 17 | 🇳🇴 NO | 6798 |
| 18 | 🇹🇭 TH | 4936 |
| 19 | 🇲🇾 MY | 4574 |
| 20 | 🇿🇦 ZA | 4562 |
| 21 | 🇵🇱 PL | 4500 |
| 22 | 🇳🇿 NZ | 3905 |
| 23 | 🇵🇭 PH | 3638 |
| 24 | 🇬🇹 GT | 3454 |
| 25 | 🇭🇷 HR | 3131 |
| 26 | 🇰🇷 KR | 3100 |
| 27 | 🇲🇦 MA | 2715 |
| 28 | 🇲🇪 ME | 2582 |
| 29 | 🇳🇱 NL | 2460 |
| 30 | 🇮🇩 ID | 2279 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5584 |
| 2 | Denver International Airport |  | US | 4490 |
| 3 | Indira Gandhi International Airport |  | IN | 3284 |
| 4 | Tokyo International Airport |  | JP | 3149 |
| 5 | El Dorado International Airport |  | CO | 3046 |
| 6 | Harry Reid International Airport |  | US | 2962 |
| 7 | Zurich Airport |  | CH | 2861 |
| 8 | Guaymaral Airport |  | CO | 2850 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2748 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2628 |
| 11 | La Aurora Airport |  | GT | 2626 |
| 12 | Salt Lake City International Airport |  | US | 2445 |
| 13 | Congonhas Airport |  | BR | 2352 |
| 14 | Chicago O'Hare International Airport |  | US | 2326 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2250 |
| 16 | Capua Airport |  | IT | 2137 |
| 17 | Madrid Barajas International Airport |  | ES | 2118 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2101 |
| 19 | Frankfurt am Main International Airport |  | DE | 2070 |
| 20 | Enrique Olaya Herrera Airport |  | CO | 1959 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1951 |
| 22 | Malpensa International Airport |  | IT | 1947 |
| 23 | Charles de Gaulle International Airport |  | FR | 1946 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1929 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1839 |
| 26 | Macau International Airport |  | MO | 1792 |
| 27 | Ninoy Aquino International Airport |  | PH | 1789 |
| 28 | Charlotte/Douglas International Airport |  | US | 1717 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1712 |
| 30 | Barcelona International Airport |  | ES | 1700 |
| 31 | Viracopos International Airport |  | BR | 1649 |
| 32 | Kuala Lumpur International Airport |  | MY | 1638 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1618 |
| 34 | Seattle-Tacoma International Airport |  | US | 1614 |
| 35 | Calgary International Airport |  | CA | 1563 |
| 36 | Don Mueang International Airport |  | TH | 1557 |
| 37 | Oslo Gardermoen Airport |  | NO | 1544 |
| 38 | Vancouver International Airport |  | CA | 1544 |
| 39 | Bengaluru International Airport |  | IN | 1541 |
| 40 | Reno/Tahoe International Airport |  | US | 1492 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1133 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1038 | 21m | 244 km | 4,370.7 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 767 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 696 | 1h 6m | 770 km | 9,245.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 694 | 24m | 225 km | 2,692.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 610 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 459 | 44m | 555 km | 4,395.1 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 443 | 27m | 275 km | 2,099.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 435 | 1h 50m | 1,423 km | 10,675.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 423 | 44m | 241 km | 1,757.1 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 393 | 24m | 218 km | 1,480.6 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 382 | 35m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 372 | 23m | 55 km | 353.6 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 370 | 21m | 250 km | 1,598.2 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 353 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 349 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 347 | 1h 6m | 706 km | 4,224.7 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 344 | 19m | 99 km | 589.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 342 | 26m | 215 km | 1,266.6 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 320 | 19m | 144 km | 796.0 t |
| 22 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 316 | 18m | 14 km | 79.0 t |
| 23 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 311 | 1h 14m | 961 km | 5,155.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 310 | 42m | 535 km | 2,863.1 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 298 | 1h 50m | 1,304 km | 6,704.2 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 273 | 44m | 431 km | 2,031.6 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N802RP |  | Patrick Leahy Burlington International Airport (KBTV) | Spencer Airport (VT09) | 2026-10-03 12:45 UTC | 2026-10-03 13:23 UTC | 38m |
| CXK526 | CXK | Columbus Municipal Airport (KBAK) | Columbus Municipal Airport (KBAK) | 2026-10-03 12:14 UTC | 2026-10-03 13:15 UTC | 1h 1m |
| THY6296 | Turkish Airlines | Queen Alia International Airport (OJAI) | Zhuhai Airport (ZGSD) | 2026-10-03 03:50 UTC | 2026-10-03 13:14 UTC | 9h 24m |
| SPMOC | SPM | Pobiednik Wielki Airport (EPKP) | Pobiednik Wielki Airport (EPKP) | 2026-10-03 12:20 UTC | 2026-10-03 13:14 UTC | 54m |
| HBZPV | HBZ | St Stephan Airport (LSTS) | Raron Airport (LSTA) | 2026-10-03 12:25 UTC | 2026-10-03 13:13 UTC | 48m |
| DFDEV | DFD | Zurich Airport (LSZH) | Bonn-Hangelar Airport (EDKB) | 2026-10-03 12:16 UTC | 2026-10-03 13:11 UTC | 55m |
| BAW43XP | British Airways | Amsterdam Airport Schiphol (EHAM) | London Heathrow Airport (EGLL) | 2026-10-03 12:32 UTC | 2026-10-03 13:11 UTC | 39m |
| ETD204 | Etihad Airways | Abu Dhabi International Airport (OMAA) | Chhatrapati Shivaji International Airport (VABB) | 2026-10-03 10:47 UTC | 2026-10-03 13:10 UTC | 2h 23m |
| LNPFG | LNP | Kjeller Airport (ENKJ) | Kjeller Airport (ENKJ) | 2026-10-03 11:42 UTC | 2026-10-03 13:07 UTC | 1h 24m |
| LFA534 | LFA | Orlando Sanford International Airport (KSFB) | Orlando Sanford International Airport (KSFB) | 2026-10-03 12:43 UTC | 2026-10-03 13:05 UTC | 21m |
| MCK202 | MCK | Halle-Oppin Airport (EDAQ) | Zurich Airport (LSZH) | 2026-10-03 11:51 UTC | 2026-10-03 12:45 UTC | 54m |
| N529WM |  | Cedar City Regional Airport (KCDC) | Mc Elroy Airfield (K20V) | 2026-10-03 11:19 UTC | 2026-10-03 12:41 UTC | 1h 21m |
| ECISV | ECI | Ampuriabrava Airport (LEAP) | Ampuriabrava Airport (LEAP) | 2026-10-03 12:07 UTC | 2026-10-03 12:41 UTC | 34m |
| AZU4177 | AZU | Viracopos International Airport (SBKP) | Clube de Marte Ibira de Para-Quedismo Airport (SWYV) | 2026-10-03 11:56 UTC | 2026-10-03 12:40 UTC | 44m |
| UPS5981 | UPS | Boeing Field/King County International Airport (KBFI) | Salt Lake City International Airport (KSLC) | 2026-10-03 11:12 UTC | 2026-10-03 12:39 UTC | 1h 27m |
| N383AA |  | Casa Grande Airport (SPCG) | Quiruvilca Airport (SPQR) | 2026-10-03 12:23 UTC | 2026-10-03 12:36 UTC | 12m |
| SRU3121 | SRU | Jorge Chavez International Airport (SPJC) | Casa Grande Airport (SPCG) | 2026-10-03 11:40 UTC | 2026-10-03 12:27 UTC | 47m |
| N11DT |  | Malin Airport (SOML) | Quiruvilca Airport (SPQR) | 2026-10-03 12:15 UTC | 2026-10-03 12:27 UTC | 11m |
| DLH686 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Herzliya Airport (LLHZ) | 2026-10-03 08:36 UTC | 2026-10-03 12:27 UTC | 3h 50m |
| 4XHPI |  | Haifa International Airport (LLHA) | LLTN (LLTN) | 2026-10-03 11:04 UTC | 2026-10-03 12:27 UTC | 1h 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
