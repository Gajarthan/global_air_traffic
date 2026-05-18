# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--18_22:45:45_UTC-green)

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

**Latest saved flight:** 2026-05-18 22:45:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-18 22:45:45 UTC

- **87,732** saved flights
- **31,374** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **87,732** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,086,280.5 tonnes** estimated CO2 emissions
- **62,972,782 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3753 |
| 2 | SkyWest Airlines | 3259 |
| 3 | IndiGo | 1868 |
| 4 | EJA | 1664 |
| 5 | American Airlines | 1350 |
| 6 | Southwest Airlines | 1280 |
| 7 | Lufthansa | 1102 |
| 8 | ENY | 1091 |
| 9 | Delta Air Lines | 965 |
| 10 | Vueling | 837 |
| 11 | LATAM Airlines | 792 |
| 12 | AXM | 782 |
| 13 | WIF | 749 |
| 14 | AZU | 695 |
| 15 | Swiss International | 675 |
| 16 | All Nippon Airways | 667 |
| 17 | LXJ | 644 |
| 18 | QLK | 626 |
| 19 | Alaska Airlines | 624 |
| 20 | easyJet | 577 |
| 21 | EJU | 565 |
| 22 | Cathay Pacific | 561 |
| 23 | AEE | 547 |
| 24 | VIV | 528 |
| 25 | Air France | 511 |
| 26 | Japan Airlines | 479 |
| 27 | CXK | 462 |
| 28 | AXB | 457 |
| 29 | MXY | 450 |
| 30 | AIQ | 427 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 72070 |
| 2 | 🇪🇸 ES | 6216 |
| 3 | 🇮🇳 IN | 5854 |
| 4 | 🇦🇺 AU | 5492 |
| 5 | 🇩🇪 DE | 4867 |
| 6 | 🇮🇹 IT | 4860 |
| 7 | 🇧🇷 BR | 4826 |
| 8 | 🇨🇦 CA | 4388 |
| 9 | 🇯🇵 JP | 4325 |
| 10 | 🇬🇧 GB | 3738 |
| 11 | 🇫🇷 FR | 3500 |
| 12 | 🇨🇴 CO | 2979 |
| 13 | 🇲🇽 MX | 2737 |
| 14 | 🇬🇷 GR | 2546 |
| 15 | 🇳🇴 NO | 2421 |
| 16 | 🇨🇭 CH | 2317 |
| 17 | 🇲🇾 MY | 1965 |
| 18 | 🇿🇦 ZA | 1621 |
| 19 | 🇹🇷 TR | 1591 |
| 20 | 🇳🇿 NZ | 1523 |
| 21 | 🇹🇭 TH | 1504 |
| 22 | 🇵🇱 PL | 1455 |
| 23 | 🇰🇷 KR | 1360 |
| 24 | 🇵🇭 PH | 1354 |
| 25 | 🇬🇹 GT | 1323 |
| 26 | 🇲🇴 MO | 1017 |
| 27 | 🇲🇦 MA | 1016 |
| 28 | 🇲🇪 ME | 907 |
| 29 | 🇳🇱 NL | 892 |
| 30 | 🇭🇷 HR | 788 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1934 |
| 2 | Denver International Airport |  | US | 1472 |
| 3 | Tokyo International Airport |  | JP | 1445 |
| 4 | Indira Gandhi International Airport |  | IN | 1260 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1208 |
| 6 | Harry Reid International Airport |  | US | 1121 |
| 7 | Frankfurt am Main International Airport |  | DE | 1113 |
| 8 | Zurich Airport |  | CH | 1044 |
| 9 | Macau International Airport |  | MO | 1017 |
| 10 | Guaymaral Airport |  | CO | 1010 |
| 11 | La Aurora Airport |  | GT | 1004 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 975 |
| 13 | El Dorado International Airport |  | CO | 952 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 890 |
| 15 | Chicago O'Hare International Airport |  | US | 848 |
| 16 | Madrid Barajas International Airport |  | ES | 796 |
| 17 | Kuala Lumpur International Airport |  | MY | 780 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 756 |
| 19 | Capua Airport |  | IT | 742 |
| 20 | Salt Lake City International Airport |  | US | 733 |
| 21 | Malpensa International Airport |  | IT | 717 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 717 |
| 23 | Bengaluru International Airport |  | IN | 707 |
| 24 | Charles de Gaulle International Airport |  | FR | 681 |
| 25 | Charlotte/Douglas International Airport |  | US | 680 |
| 26 | Congonhas Airport |  | BR | 673 |
| 27 | Daniel K Inouye International Airport |  | US | 643 |
| 28 | Tenerife Norte Airport |  | ES | 642 |
| 29 | Ninoy Aquino International Airport |  | PH | 620 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 596 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 32 | Barcelona International Airport |  | ES | 591 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 582 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 562 |
| 35 | Vitoria/Foronda Airport |  | ES | 559 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 554 |
| 37 | Amsterdam Airport Schiphol |  | NL | 546 |
| 38 | Don Mueang International Airport |  | TH | 545 |
| 39 | Calgary International Airport |  | CA | 519 |
| 40 | O. R. Tambo International Airport |  | ZA | 510 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 414 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 327 | 21m | 244 km | 1,376.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 276 | 1h 8m | 706 km | 3,360.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 243 | 24m | 225 km | 942.7 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 230 | 1h 26m | 910 km | 3,609.2 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 227 | 28m | 304 km | 1,190.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 225 | 14m | 114 km | 441.3 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 223 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 201 | 1h 10m | 770 km | 2,670.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 193 | 19m | 165 km | 549.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 182 | 26m | 275 km | 862.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 148 | 21m | 99 km | 253.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 136 | 31m | 369 km | 865.7 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 127 | 20m | 147 km | 321.4 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 126 | 27m | 215 km | 466.7 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 124 | 14m | 154 km | 328.6 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 123 | 23m | 55 km | 116.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 121 | 20m | 250 km | 522.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 113 | 18m | 144 km | 281.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 111 | 1h 42m | 1,423 km | 2,724.1 t |
| 27 | Bodø Airport (ENBO) | ENEN (ENEN) | 111 | 13m | - | - |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 108 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 106 | 1h 41m | 1,156 km | 2,114.7 t |
| 30 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| C2004 |  | Kalaeloa (John Rodgers Field) Airport (PHJR) | Kalaeloa (John Rodgers Field) Airport (PHJR) | 2026-05-18 22:34 UTC | 2026-05-18 22:45 UTC | 11m |
| CXK393 | CXK | Morristown Municipal Airport (KMMU) | Lancaster Airport (KLNS) | 2026-05-18 21:38 UTC | 2026-05-18 22:41 UTC | 1h 2m |
| WAH | WAH | Ted Stevens Anchorage International Airport (PANC) | Nikolai Creek Airport (9AK3) | 2026-05-18 22:16 UTC | 2026-05-18 22:38 UTC | 21m |
| N55KC |  | Yuba County Airport (KMYV) | San Carlos Airport (KSQL) | 2026-05-18 21:58 UTC | 2026-05-18 22:37 UTC | 39m |
| N111BP |  | John Glenn Columbus International Airport (KCMH) | Auburn University Regional Airport (KAUO) | 2026-05-18 21:15 UTC | 2026-05-18 22:33 UTC | 1h 18m |
| CPA294 | Cathay Pacific | Melsbroek Air Base (EBMB) | Zhuhai Airport (ZGSD) | 2026-05-18 11:17 UTC | 2026-05-18 22:31 UTC | 11h 13m |
| VWA118 | VWA | Falcon Field (KFFZ) | Glendale Regional Airport (KGEU) | 2026-05-18 22:04 UTC | 2026-05-18 22:29 UTC | 25m |
| N563M |  | Gerald R Ford International Airport (KGRR) | 6MI0 (6MI0) | 2026-05-18 22:08 UTC | 2026-05-18 22:29 UTC | 20m |
| N367MS |  | North Las Vegas Airport (KVGT) | Creech Afb Airport (KINS) | 2026-05-18 21:53 UTC | 2026-05-18 22:24 UTC | 30m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Zhuhai Airport (ZGSD) | 2026-05-18 10:13 UTC | 2026-05-18 22:21 UTC | 12h 8m |
| HRD05 | HRD | Carr Airport (WV65) | Arnold Palmer Regional Airport (KLBE) | 2026-05-18 22:02 UTC | 2026-05-18 22:19 UTC | 17m |
| HAWK280 | HAW | Kingsville Nas Airport (KNQI) | Puesta Del Sol Airport (TA44) | 2026-05-18 21:32 UTC | 2026-05-18 22:19 UTC | 47m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-05-18 10:50 UTC | 2026-05-18 22:19 UTC | 11h 28m |
| N528SV |  | Trenton Mercer Airport (KTTN) | Eagle Crest-Hudson Airport (DE25) | 2026-05-18 20:59 UTC | 2026-05-18 22:16 UTC | 1h 16m |
| N737MH |  | Chino Airport (KCNO) | Big Bear City Airport (KL35) | 2026-05-18 21:41 UTC | 2026-05-18 22:13 UTC | 32m |
| AIC314 | Air India | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-05-18 17:54 UTC | 2026-05-18 22:13 UTC | 4h 18m |
| N7878S |  | Long Beach (Daugherty Field) Airport (KLGB) | Long Beach (Daugherty Field) Airport (KLGB) | 2026-05-18 21:29 UTC | 2026-05-18 22:11 UTC | 42m |
| N30JA |  | Aurora Municipal Airport (KARR) | Ruder Airport (59IL) | 2026-05-18 21:53 UTC | 2026-05-18 22:11 UTC | 17m |
| N900KP |  | Boise Air Trml/Gowen Field (KBOI) | Mc Clellan Airfield (KMCC) | 2026-05-18 21:01 UTC | 2026-05-18 22:08 UTC | 1h 6m |
| N5367H |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-05-18 21:53 UTC | 2026-05-18 22:08 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
