# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--01_23:27:57_UTC-green)

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

**Latest saved flight:** 2026-10-01 23:27:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-10-01 23:27:57 UTC

- **274,162** saved flights
- **79,996** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **274,162** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,318,088.3 tonnes** estimated CO2 emissions
- **192,352,944 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10763 |
| 2 | SkyWest Airlines | 9541 |
| 3 | EJA | 5372 |
| 4 | IndiGo | 4567 |
| 5 | American Airlines | 4247 |
| 6 | Southwest Airlines | 4028 |
| 7 | Delta Air Lines | 3403 |
| 8 | ENY | 3210 |
| 9 | LATAM Airlines | 2650 |
| 10 | AZU | 2581 |
| 11 | Vueling | 2275 |
| 12 | WIF | 2231 |
| 13 | LXJ | 2164 |
| 14 | Lufthansa | 2068 |
| 15 | easyJet | 1823 |
| 16 | Swiss International | 1793 |
| 17 | QLK | 1772 |
| 18 | EJU | 1708 |
| 19 | AXM | 1683 |
| 20 | United Airlines | 1673 |
| 21 | Alaska Airlines | 1615 |
| 22 | All Nippon Airways | 1565 |
| 23 | PGT | 1543 |
| 24 | GLO | 1533 |
| 25 | WMT | 1528 |
| 26 | Air France | 1505 |
| 27 | VIV | 1503 |
| 28 | Wizz Air | 1484 |
| 29 | CXK | 1355 |
| 30 | AEE | 1308 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 228685 |
| 2 | 🇪🇸 ES | 17142 |
| 3 | 🇧🇷 BR | 16108 |
| 4 | 🇦🇺 AU | 15831 |
| 5 | 🇨🇦 CA | 15297 |
| 6 | 🇮🇹 IT | 14790 |
| 7 | 🇮🇳 IN | 14455 |
| 8 | 🇩🇪 DE | 13130 |
| 9 | 🇨🇴 CO | 12702 |
| 10 | 🇬🇧 GB | 12628 |
| 11 | 🇫🇷 FR | 10852 |
| 12 | 🇯🇵 JP | 10454 |
| 13 | 🇹🇷 TR | 8291 |
| 14 | 🇬🇷 GR | 7884 |
| 15 | 🇲🇽 MX | 7577 |
| 16 | 🇨🇭 CH | 7271 |
| 17 | 🇳🇴 NO | 6762 |
| 18 | 🇹🇭 TH | 4900 |
| 19 | 🇲🇾 MY | 4559 |
| 20 | 🇿🇦 ZA | 4553 |
| 21 | 🇵🇱 PL | 4476 |
| 22 | 🇳🇿 NZ | 3875 |
| 23 | 🇵🇭 PH | 3616 |
| 24 | 🇬🇹 GT | 3436 |
| 25 | 🇭🇷 HR | 3119 |
| 26 | 🇰🇷 KR | 3084 |
| 27 | 🇲🇦 MA | 2711 |
| 28 | 🇲🇪 ME | 2572 |
| 29 | 🇳🇱 NL | 2454 |
| 30 | 🇮🇩 ID | 2268 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5566 |
| 2 | Denver International Airport |  | US | 4473 |
| 3 | Indira Gandhi International Airport |  | IN | 3270 |
| 4 | Tokyo International Airport |  | JP | 3134 |
| 5 | El Dorado International Airport |  | CO | 3020 |
| 6 | Harry Reid International Airport |  | US | 2950 |
| 7 | Guaymaral Airport |  | CO | 2845 |
| 8 | Zurich Airport |  | CH | 2843 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2743 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2624 |
| 11 | La Aurora Airport |  | GT | 2612 |
| 12 | Salt Lake City International Airport |  | US | 2434 |
| 13 | Congonhas Airport |  | BR | 2342 |
| 14 | Chicago O'Hare International Airport |  | US | 2321 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2243 |
| 16 | Capua Airport |  | IT | 2128 |
| 17 | Madrid Barajas International Airport |  | ES | 2108 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2086 |
| 19 | Frankfurt am Main International Airport |  | DE | 2064 |
| 20 | Enrique Olaya Herrera Airport |  | CO | 1959 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1946 |
| 22 | Malpensa International Airport |  | IT | 1943 |
| 23 | Charles de Gaulle International Airport |  | FR | 1941 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1928 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1834 |
| 26 | Macau International Airport |  | MO | 1789 |
| 27 | Ninoy Aquino International Airport |  | PH | 1777 |
| 28 | Charlotte/Douglas International Airport |  | US | 1715 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1701 |
| 30 | Barcelona International Airport |  | ES | 1693 |
| 31 | Viracopos International Airport |  | BR | 1644 |
| 32 | Kuala Lumpur International Airport |  | MY | 1632 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1611 |
| 34 | Seattle-Tacoma International Airport |  | US | 1606 |
| 35 | Calgary International Airport |  | CA | 1560 |
| 36 | Don Mueang International Airport |  | TH | 1547 |
| 37 | Vancouver International Airport |  | CA | 1537 |
| 38 | Oslo Gardermoen Airport |  | NO | 1534 |
| 39 | Bengaluru International Airport |  | IN | 1533 |
| 40 | Reno/Tahoe International Airport |  | US | 1482 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1132 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1032 | 21m | 244 km | 4,345.5 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 767 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 693 | 1h 6m | 770 km | 9,206.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 688 | 24m | 225 km | 2,669.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 605 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 458 | 44m | 555 km | 4,385.6 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 441 | 27m | 275 km | 2,089.7 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 433 | 1h 50m | 1,423 km | 10,626.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 421 | 44m | 241 km | 1,748.7 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 392 | 24m | 218 km | 1,476.8 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 382 | 35m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 372 | 23m | 55 km | 353.6 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 370 | 21m | 250 km | 1,598.2 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 352 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 347 | 12m | - | - |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 342 | 26m | 215 km | 1,266.6 t |
| 18 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 342 | 1h 6m | 706 km | 4,163.9 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 342 | 19m | 99 km | 585.8 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 318 | 19m | 144 km | 791.0 t |
| 22 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 314 | 18m | 14 km | 78.5 t |
| 23 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 311 | 1h 14m | 961 km | 5,155.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 303 | 42m | 535 km | 2,798.4 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 296 | 1h 50m | 1,304 km | 6,659.2 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 271 | 44m | 431 km | 2,016.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UPS5012 | UPS | Chicago/Rockford International Airport (KRFD) | General Edward Lawrence Logan International Airport (KBOS) | 2026-10-01 21:39 UTC | 2026-10-01 23:27 UTC | 1h 48m |
| BT704 |  | North Island Nas (Halsey Field) Airport (KNZY) | CA84 (CA84) | 2026-10-01 22:11 UTC | 2026-10-01 23:24 UTC | 1h 12m |
| N9824V |  | Olympia Regional Airport (KOLM) | Olympia Regional Airport (KOLM) | 2026-10-01 22:33 UTC | 2026-10-01 23:20 UTC | 46m |
| LTA814 | LTA | Indianapolis International Airport (KIND) | K4I7 (K4I7) | 2026-10-01 23:01 UTC | 2026-10-01 23:19 UTC | 17m |
| N78Q |  | Monterey Regional Airport (KMRY) | Santa Barbara Municipal Airport (KSBA) | 2026-10-01 22:21 UTC | 2026-10-01 23:14 UTC | 52m |
| VKG505 | VKG | Antalya International Airport (LTAI) | Leszno Strzyzewi Airport (EPLS) | 2026-10-01 20:35 UTC | 2026-10-01 23:13 UTC | 2h 37m |
| LS09 |  | North Island Nas (Halsey Field) Airport (KNZY) | Imperial Beach Nolf (Ream Field) Airport (KNRS) | 2026-10-01 22:46 UTC | 2026-10-01 23:11 UTC | 24m |
| N784SP |  | Livermore Municipal Airport (KLVK) | Livermore Municipal Airport (KLVK) | 2026-10-01 22:55 UTC | 2026-10-01 23:07 UTC | 12m |
| N707KA |  | Boeing Field/King County International Airport (KBFI) | Boeing Field/King County International Airport (KBFI) | 2026-10-01 22:45 UTC | 2026-10-01 23:06 UTC | 21m |
| CFR430 | CFR | Mammoth Yosemite Airport (KMMH) | 6CL6 (6CL6) | 2026-10-01 22:53 UTC | 2026-10-01 22:58 UTC | 4m |
| RANGR41 | RAN | Lake Havasu City Airport (KHII) | Massey Farm Airport (AZ34) | 2026-10-01 22:39 UTC | 2026-10-01 22:58 UTC | 18m |
| N769FG |  | Trenton Mercer Airport (KTTN) | Sky Manor Airport (KN40) | 2026-10-01 22:16 UTC | 2026-10-01 22:56 UTC | 40m |
| N41HX |  | 6CL4 (6CL4) | 6CL4 (6CL4) | 2026-10-01 22:27 UTC | 2026-10-01 22:54 UTC | 27m |
| N84DL |  | Oakland San Francisco Bay Airport (KOAK) | Modesto City-County-Harry Sham Field (KMOD) | 2026-10-01 22:13 UTC | 2026-10-01 22:54 UTC | 41m |
| NTR224 | NTR | Faa'a International Airport (NTAA) | Tikehau Airport (NTGC) | 2026-10-01 22:12 UTC | 2026-10-01 22:54 UTC | 41m |
| STT11 | STT | Weiser Municipal Airport (KS87) | Weiser Municipal Airport (KS87) | 2026-10-01 22:36 UTC | 2026-10-01 22:49 UTC | 13m |
| N793US |  | Provo Municipal Airport (KPVU) | K36U (K36U) | 2026-10-01 22:18 UTC | 2026-10-01 22:48 UTC | 29m |
| N108UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-10-01 21:34 UTC | 2026-10-01 22:45 UTC | 1h 11m |
| RYR6743 | Ryanair | Ibn Batouta Airport (GMTT) | Angads Airport (GMFO) | 2026-10-01 22:13 UTC | 2026-10-01 22:45 UTC | 31m |
| ARCAS24 | ARC | Danaher Airport (7TX0) | Flying B Ranch Airstrip (35TX) | 2026-10-01 22:27 UTC | 2026-10-01 22:44 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
