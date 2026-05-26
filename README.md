# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_06:20:53_UTC-green)

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

**Latest saved flight:** 2026-05-26 06:20:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-26 06:20:53 UTC

- **94,827** saved flights
- **33,442** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **94,827** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,166,104.3 tonnes** estimated CO2 emissions
- **67,600,249 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4002 |
| 2 | SkyWest Airlines | 3525 |
| 3 | IndiGo | 1965 |
| 4 | EJA | 1795 |
| 5 | American Airlines | 1441 |
| 6 | Southwest Airlines | 1378 |
| 7 | ENY | 1173 |
| 8 | Lufthansa | 1139 |
| 9 | Delta Air Lines | 1039 |
| 10 | Vueling | 906 |
| 11 | LATAM Airlines | 851 |
| 12 | AXM | 839 |
| 13 | WIF | 829 |
| 14 | AZU | 759 |
| 15 | LXJ | 717 |
| 16 | Swiss International | 709 |
| 17 | All Nippon Airways | 699 |
| 18 | QLK | 660 |
| 19 | Alaska Airlines | 659 |
| 20 | easyJet | 622 |
| 21 | EJU | 609 |
| 22 | Cathay Pacific | 582 |
| 23 | AEE | 572 |
| 24 | VIV | 562 |
| 25 | Air France | 559 |
| 26 | CXK | 506 |
| 27 | MXY | 504 |
| 28 | Japan Airlines | 490 |
| 29 | AXB | 479 |
| 30 | AIQ | 457 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 78369 |
| 2 | 🇪🇸 ES | 6650 |
| 3 | 🇮🇳 IN | 6201 |
| 4 | 🇦🇺 AU | 5808 |
| 5 | 🇩🇪 DE | 5206 |
| 6 | 🇧🇷 BR | 5199 |
| 7 | 🇮🇹 IT | 5151 |
| 8 | 🇨🇦 CA | 4810 |
| 9 | 🇯🇵 JP | 4535 |
| 10 | 🇬🇧 GB | 4050 |
| 11 | 🇫🇷 FR | 3833 |
| 12 | 🇨🇴 CO | 3284 |
| 13 | 🇲🇽 MX | 2916 |
| 14 | 🇬🇷 GR | 2728 |
| 15 | 🇳🇴 NO | 2641 |
| 16 | 🇨🇭 CH | 2490 |
| 17 | 🇲🇾 MY | 2122 |
| 18 | 🇹🇷 TR | 1755 |
| 19 | 🇿🇦 ZA | 1711 |
| 20 | 🇳🇿 NZ | 1610 |
| 21 | 🇹🇭 TH | 1606 |
| 22 | 🇵🇱 PL | 1554 |
| 23 | 🇰🇷 KR | 1543 |
| 24 | 🇵🇭 PH | 1428 |
| 25 | 🇬🇹 GT | 1423 |
| 26 | 🇲🇦 MA | 1084 |
| 27 | 🇲🇴 MO | 1038 |
| 28 | 🇳🇱 NL | 954 |
| 29 | 🇲🇪 ME | 941 |
| 30 | 🇭🇷 HR | 864 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2049 |
| 2 | Denver International Airport |  | US | 1607 |
| 3 | Tokyo International Airport |  | JP | 1507 |
| 4 | Indira Gandhi International Airport |  | IN | 1347 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1253 |
| 6 | Harry Reid International Airport |  | US | 1222 |
| 7 | Frankfurt am Main International Airport |  | DE | 1154 |
| 8 | Guaymaral Airport |  | CO | 1151 |
| 9 | Zurich Airport |  | CH | 1108 |
| 10 | La Aurora Airport |  | GT | 1089 |
| 11 | Macau International Airport |  | MO | 1038 |
| 12 | El Dorado International Airport |  | CO | 1030 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1029 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 948 |
| 15 | Chicago O'Hare International Airport |  | US | 918 |
| 16 | Madrid Barajas International Airport |  | ES | 844 |
| 17 | Kuala Lumpur International Airport |  | MY | 842 |
| 18 | Salt Lake City International Airport |  | US | 801 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 799 |
| 20 | Capua Airport |  | IT | 787 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 756 |
| 22 | Malpensa International Airport |  | IT | 749 |
| 23 | Bengaluru International Airport |  | IN | 742 |
| 24 | Charles de Gaulle International Airport |  | FR | 741 |
| 25 | Charlotte/Douglas International Airport |  | US | 722 |
| 26 | Congonhas Airport |  | BR | 722 |
| 27 | Daniel K Inouye International Airport |  | US | 678 |
| 28 | Tenerife Norte Airport |  | ES | 675 |
| 29 | Ninoy Aquino International Airport |  | PH | 651 |
| 30 | Barcelona International Airport |  | ES | 640 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 638 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 616 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 608 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 601 |
| 35 | Amsterdam Airport Schiphol |  | NL | 589 |
| 36 | Don Mueang International Airport |  | TH | 588 |
| 37 | Vitoria/Foronda Airport |  | ES | 588 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 568 |
| 39 | Calgary International Airport |  | CA | 562 |
| 40 | O. R. Tambo International Airport |  | ZA | 543 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 472 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 349 | 21m | 244 km | 1,469.5 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 255 | 24m | 225 km | 989.3 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 252 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 242 | 14m | 114 km | 474.6 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 241 | 1h 26m | 910 km | 3,781.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 238 | 28m | 304 km | 1,247.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 217 | 1h 10m | 770 km | 2,882.7 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 205 | 19m | 165 km | 583.1 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 190 | 26m | 275 km | 900.3 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 143 | 27m | 215 km | 529.6 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 141 | 44m | 452 km | 1,098.9 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 141 | 14m | 154 km | 373.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 138 | 22m | 55 km | 131.2 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 136 | 27m | 152 km | 355.4 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 129 | 20m | 250 km | 557.2 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 123 | 1h 1m | 695 km | 1,474.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 122 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 122 | 18m | 144 km | 303.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 119 | 1h 39m | 1,156 km | 2,374.0 t |
| 26 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 114 | 1h 52m | 1,304 km | 2,564.7 t |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 113 | 1h 18m | 961 km | 1,873.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UAL946 | United Airlines | Washington Dulles International Airport (KIAD) | Amsterdam Airport Schiphol (EHAM) | 2026-05-25 23:25 UTC | 2026-05-26 06:20 UTC | 6h 55m |
| CTV641 | CTV | Halim Perdanakusuma International Airport (WIHH) | Halim Perdanakusuma International Airport (WIHH) | 2026-05-26 05:59 UTC | 2026-05-26 06:10 UTC | 11m |
| JFL463 | JFL | Vilnius International Airport (EYVI) | Khrabrovo Airport (UMKK) | 2026-05-26 05:37 UTC | 2026-05-26 06:10 UTC | 32m |
| KAL2148 | Korean Air | Gwangju Airport (RKJJ) | Incheon International Airport (RKSI) | 2026-05-26 05:34 UTC | 2026-05-26 06:05 UTC | 30m |
| N700JV |  | Aurillac Airport (LFLW) | Lyon-Bron Airport (LFLY) | 2026-05-26 05:24 UTC | 2026-05-26 05:59 UTC | 34m |
| ISR563 | ISR | Ben Gurion International Airport (LLBG) | Queen Alia International Airport (OJAI) | 2026-05-26 05:34 UTC | 2026-05-26 05:56 UTC | 22m |
| BEL8HQ | Brussels Airlines | Melsbroek Air Base (EBMB) | Zurich Airport (LSZH) | 2026-05-26 04:56 UTC | 2026-05-26 05:50 UTC | 54m |
| AFL900 | AFL | Sivas Airport (LTAR) | Queen Alia International Airport (OJAI) | 2026-05-26 04:46 UTC | 2026-05-26 05:49 UTC | 1h 3m |
| N502GV |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-05-26 05:10 UTC | 2026-05-26 05:37 UTC | 26m |
| AE974 |  | Sydney Bankstown Airport (YSBK) | Mudgee Airport (YMDG) | 2026-05-26 05:10 UTC | 2026-05-26 05:36 UTC | 26m |
| DLH1MM | Lufthansa | Frankfurt am Main International Airport (EDDF) | Stuttgart Airport (EDDS) | 2026-05-26 05:14 UTC | 2026-05-26 05:35 UTC | 21m |
| AFL1872 | AFL | Sheremetyevo International Airport (UUEE) | Bezymyanka Airfield (UWWG) | 2026-05-26 04:27 UTC | 2026-05-26 05:32 UTC | 1h 5m |
| TWB720 | TWB | G 710 Airport (RK6D) | Gimpo International Airport (RKSS) | 2026-05-26 04:58 UTC | 2026-05-26 05:28 UTC | 29m |
| FD629 |  | Perth Jandakot Airport (YPJT) | Kellerberrin Airport (YKEB) | 2026-05-26 04:58 UTC | 2026-05-26 05:26 UTC | 28m |
| RYR3GD | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Capua Airport (LIAU) | 2026-05-26 04:33 UTC | 2026-05-26 05:25 UTC | 52m |
| N800KM |  | John Wayne/Orange County Airport (KSNA) | Sacramento Mather Airport (KMHR) | 2026-05-26 04:17 UTC | 2026-05-26 05:23 UTC | 1h 5m |
| NYT921 | NYT | Tribhuvan International Airport (VNKT) | Suketar Airport (VNTJ) | 2026-05-26 04:59 UTC | 2026-05-26 05:22 UTC | 23m |
| AEE348 | AEE | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-05-26 05:00 UTC | 2026-05-26 05:20 UTC | 19m |
| ASL57F | ASL | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 2026-05-26 04:44 UTC | 2026-05-26 05:15 UTC | 31m |
| IGO479 | IndiGo | Sardar Vallabhbhai Patel International Airport (VAAH) | Mysore Airport (VOMY) | 2026-05-26 01:39 UTC | 2026-05-26 05:14 UTC | 3h 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
