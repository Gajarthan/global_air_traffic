# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_22:09:13_UTC-green)

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

**Latest saved flight:** 2026-09-29 22:09:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-29 22:09:13 UTC

- **272,618** saved flights
- **79,664** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **272,618** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,302,605.8 tonnes** estimated CO2 emissions
- **191,455,409 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10720 |
| 2 | SkyWest Airlines | 9497 |
| 3 | EJA | 5338 |
| 4 | IndiGo | 4551 |
| 5 | American Airlines | 4233 |
| 6 | Southwest Airlines | 4012 |
| 7 | Delta Air Lines | 3389 |
| 8 | ENY | 3201 |
| 9 | LATAM Airlines | 2631 |
| 10 | AZU | 2562 |
| 11 | Vueling | 2266 |
| 12 | WIF | 2217 |
| 13 | LXJ | 2147 |
| 14 | Lufthansa | 2060 |
| 15 | easyJet | 1820 |
| 16 | Swiss International | 1783 |
| 17 | QLK | 1757 |
| 18 | EJU | 1702 |
| 19 | AXM | 1679 |
| 20 | United Airlines | 1667 |
| 21 | Alaska Airlines | 1608 |
| 22 | All Nippon Airways | 1561 |
| 23 | PGT | 1538 |
| 24 | GLO | 1522 |
| 25 | WMT | 1517 |
| 26 | Air France | 1499 |
| 27 | VIV | 1494 |
| 28 | Wizz Air | 1480 |
| 29 | CXK | 1347 |
| 30 | AEE | 1304 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 227268 |
| 2 | 🇪🇸 ES | 17058 |
| 3 | 🇧🇷 BR | 15999 |
| 4 | 🇦🇺 AU | 15698 |
| 5 | 🇨🇦 CA | 15191 |
| 6 | 🇮🇹 IT | 14720 |
| 7 | 🇮🇳 IN | 14401 |
| 8 | 🇩🇪 DE | 13060 |
| 9 | 🇬🇧 GB | 12582 |
| 10 | 🇨🇴 CO | 12574 |
| 11 | 🇫🇷 FR | 10819 |
| 12 | 🇯🇵 JP | 10420 |
| 13 | 🇹🇷 TR | 8260 |
| 14 | 🇬🇷 GR | 7854 |
| 15 | 🇲🇽 MX | 7538 |
| 16 | 🇨🇭 CH | 7242 |
| 17 | 🇳🇴 NO | 6728 |
| 18 | 🇹🇭 TH | 4879 |
| 19 | 🇲🇾 MY | 4549 |
| 20 | 🇿🇦 ZA | 4537 |
| 21 | 🇵🇱 PL | 4464 |
| 22 | 🇳🇿 NZ | 3847 |
| 23 | 🇵🇭 PH | 3597 |
| 24 | 🇬🇹 GT | 3428 |
| 25 | 🇭🇷 HR | 3104 |
| 26 | 🇰🇷 KR | 3074 |
| 27 | 🇲🇦 MA | 2700 |
| 28 | 🇲🇪 ME | 2555 |
| 29 | 🇳🇱 NL | 2445 |
| 30 | 🇮🇩 ID | 2264 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5554 |
| 2 | Denver International Airport |  | US | 4444 |
| 3 | Indira Gandhi International Airport |  | IN | 3254 |
| 4 | Tokyo International Airport |  | JP | 3121 |
| 5 | El Dorado International Airport |  | CO | 2991 |
| 6 | Harry Reid International Airport |  | US | 2929 |
| 7 | Guaymaral Airport |  | CO | 2831 |
| 8 | Zurich Airport |  | CH | 2826 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2734 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2615 |
| 11 | La Aurora Airport |  | GT | 2605 |
| 12 | Salt Lake City International Airport |  | US | 2416 |
| 13 | Congonhas Airport |  | BR | 2328 |
| 14 | Chicago O'Hare International Airport |  | US | 2316 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2231 |
| 16 | Capua Airport |  | IT | 2108 |
| 17 | Madrid Barajas International Airport |  | ES | 2099 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2067 |
| 19 | Frankfurt am Main International Airport |  | DE | 2056 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1936 |
| 21 | Malpensa International Airport |  | IT | 1935 |
| 22 | Charles de Gaulle International Airport |  | FR | 1935 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1932 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1906 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1829 |
| 26 | Macau International Airport |  | MO | 1789 |
| 27 | Ninoy Aquino International Airport |  | PH | 1767 |
| 28 | Charlotte/Douglas International Airport |  | US | 1707 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1699 |
| 30 | Barcelona International Airport |  | ES | 1688 |
| 31 | Viracopos International Airport |  | BR | 1640 |
| 32 | Kuala Lumpur International Airport |  | MY | 1630 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1599 |
| 34 | Seattle-Tacoma International Airport |  | US | 1598 |
| 35 | Calgary International Airport |  | CA | 1548 |
| 36 | Don Mueang International Airport |  | TH | 1543 |
| 37 | Bengaluru International Airport |  | IN | 1530 |
| 38 | Oslo Gardermoen Airport |  | NO | 1527 |
| 39 | Vancouver International Airport |  | CA | 1523 |
| 40 | Reno/Tahoe International Airport |  | US | 1465 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1126 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1023 | 21m | 244 km | 4,307.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 758 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 686 | 1h 6m | 770 km | 9,113.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 682 | 24m | 225 km | 2,645.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 602 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 456 | 44m | 555 km | 4,366.4 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 438 | 27m | 275 km | 2,075.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 431 | 1h 50m | 1,423 km | 10,577.4 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 418 | 44m | 241 km | 1,736.3 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 391 | 24m | 218 km | 1,473.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 379 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 369 | 21m | 250 km | 1,593.9 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 366 | 23m | 55 km | 347.9 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 349 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 345 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 342 | 1h 6m | 706 km | 4,163.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 341 | 19m | 99 km | 584.1 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 337 | 26m | 215 km | 1,248.1 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 317 | 19m | 144 km | 788.5 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 309 | 1h 14m | 961 km | 5,121.8 t |
| 24 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 305 | 18m | 14 km | 76.3 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 302 | 42m | 535 km | 2,789.2 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 295 | 1h 50m | 1,304 km | 6,636.7 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N805FA |  | Camarillo Airport (KCMA) | Santa Monica Municipal Airport (KSMO) | 2026-09-29 21:07 UTC | 2026-09-29 22:09 UTC | 1h 1m |
| N2129J |  | Trenton Mercer Airport (KTTN) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-09-29 21:15 UTC | 2026-09-29 21:59 UTC | 43m |
| PNTHR71 | PNT | Laughlin Afb Aux Nr 1 Airport (KT70) | Dunbar Ranch Airport (0XS8) | 2026-09-29 21:38 UTC | 2026-09-29 21:54 UTC | 16m |
| N447BL |  | Harnett Regional Jetport Airport (KHRJ) | Harnett Regional Jetport Airport (KHRJ) | 2026-09-29 21:31 UTC | 2026-09-29 21:53 UTC | 22m |
| N397AM |  | KU77 (KU77) | Wendover Airport (KENV) | 2026-09-29 20:58 UTC | 2026-09-29 21:53 UTC | 55m |
| N700JL |  | Stottlemyer Airport (2II3) | Purdue University Airport (KLAF) | 2026-09-29 21:31 UTC | 2026-09-29 21:52 UTC | 20m |
| N4583R |  | Savannah/Hilton Head International Airport (KSAV) | Hunter Army Air Field (KSVN) | 2026-09-29 21:40 UTC | 2026-09-29 21:51 UTC | 10m |
| PSDOR | PSD | Congonhas Airport (SBSP) | Clube do Ceu Airport (SDIN) | 2026-09-29 21:15 UTC | 2026-09-29 21:47 UTC | 31m |
| JUPITER | JUP | El Dorado International Airport (SKBO) | Velasquez Airport (SKVL) | 2026-09-29 20:56 UTC | 2026-09-29 21:43 UTC | 46m |
| SH12 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-29 21:30 UTC | 2026-09-29 21:42 UTC | 12m |
| ARCAS10 | ARC | Kickapoo Downtown Airport (KCWC) | 54TS (54TS) | 2026-09-29 21:26 UTC | 2026-09-29 21:42 UTC | 15m |
| N300KL |  | Arkansas International Airport (KBYH) | Jackson County/Reynolds Field (KJXN) | 2026-09-29 19:53 UTC | 2026-09-29 21:41 UTC | 1h 48m |
| N222HN |  | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-09-29 21:37 UTC | 2026-09-29 21:40 UTC | 2m |
| JANET27 | JAN | Harry Reid International Airport (KLAS) | NV11 (NV11) | 2026-09-29 21:22 UTC | 2026-09-29 21:37 UTC | 14m |
| N4411X |  | Montgomery-Gibbs Executive Airport (KMYF) | CL35 (CL35) | 2026-09-29 21:09 UTC | 2026-09-29 21:35 UTC | 26m |
| N817SS |  | Rust Field (8XS9) | West Houston Airport (KIWS) | 2026-09-29 20:20 UTC | 2026-09-29 21:35 UTC | 1h 14m |
| N235CD |  | Iberlin Strip (WY23) | Iberlin Strip (WY23) | 2026-09-29 21:20 UTC | 2026-09-29 21:34 UTC | 14m |
|  |  | Greenville Municipal Airport (K6D6) | Greenville Municipal Airport (K6D6) | 2026-09-29 21:28 UTC | 2026-09-29 21:33 UTC | 4m |
| EFY7838 | EFY | El Dorado International Airport (SKBO) | La Nubia Airport (SKMZ) | 2026-09-29 21:03 UTC | 2026-09-29 21:33 UTC | 29m |
| HER13 | HER | RNZAF Base Auckland-Whenuapai (NZWP) | Wellington International Airport (NZWN) | 2026-09-29 20:28 UTC | 2026-09-29 21:32 UTC | 1h 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
