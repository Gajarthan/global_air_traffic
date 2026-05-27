# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_19:26:51_UTC-green)

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

**Latest saved flight:** 2026-05-27 19:26:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-27 19:26:51 UTC

- **95,580** saved flights
- **33,645** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **95,580** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,173,909.4 tonnes** estimated CO2 emissions
- **68,052,721 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4024 |
| 2 | SkyWest Airlines | 3557 |
| 3 | IndiGo | 1983 |
| 4 | EJA | 1806 |
| 5 | American Airlines | 1449 |
| 6 | Southwest Airlines | 1389 |
| 7 | ENY | 1178 |
| 8 | Lufthansa | 1148 |
| 9 | Delta Air Lines | 1046 |
| 10 | Vueling | 909 |
| 11 | LATAM Airlines | 860 |
| 12 | AXM | 848 |
| 13 | WIF | 842 |
| 14 | AZU | 765 |
| 15 | LXJ | 725 |
| 16 | Swiss International | 713 |
| 17 | All Nippon Airways | 709 |
| 18 | Alaska Airlines | 664 |
| 19 | QLK | 663 |
| 20 | easyJet | 627 |
| 21 | EJU | 610 |
| 22 | Cathay Pacific | 582 |
| 23 | AEE | 577 |
| 24 | Air France | 565 |
| 25 | VIV | 564 |
| 26 | CXK | 509 |
| 27 | MXY | 506 |
| 28 | Japan Airlines | 493 |
| 29 | AXB | 484 |
| 30 | AIQ | 462 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 78915 |
| 2 | 🇪🇸 ES | 6688 |
| 3 | 🇮🇳 IN | 6257 |
| 4 | 🇦🇺 AU | 5876 |
| 5 | 🇧🇷 BR | 5245 |
| 6 | 🇩🇪 DE | 5243 |
| 7 | 🇮🇹 IT | 5182 |
| 8 | 🇨🇦 CA | 4839 |
| 9 | 🇯🇵 JP | 4584 |
| 10 | 🇬🇧 GB | 4092 |
| 11 | 🇫🇷 FR | 3883 |
| 12 | 🇨🇴 CO | 3304 |
| 13 | 🇲🇽 MX | 2932 |
| 14 | 🇬🇷 GR | 2760 |
| 15 | 🇳🇴 NO | 2676 |
| 16 | 🇨🇭 CH | 2511 |
| 17 | 🇲🇾 MY | 2152 |
| 18 | 🇹🇷 TR | 1769 |
| 19 | 🇿🇦 ZA | 1717 |
| 20 | 🇳🇿 NZ | 1632 |
| 21 | 🇹🇭 TH | 1625 |
| 22 | 🇰🇷 KR | 1580 |
| 23 | 🇵🇱 PL | 1565 |
| 24 | 🇵🇭 PH | 1444 |
| 25 | 🇬🇹 GT | 1426 |
| 26 | 🇲🇦 MA | 1090 |
| 27 | 🇲🇴 MO | 1038 |
| 28 | 🇳🇱 NL | 965 |
| 29 | 🇲🇪 ME | 945 |
| 30 | 🇭🇷 HR | 870 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2066 |
| 2 | Denver International Airport |  | US | 1621 |
| 3 | Tokyo International Airport |  | JP | 1521 |
| 4 | Indira Gandhi International Airport |  | IN | 1356 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1266 |
| 6 | Harry Reid International Airport |  | US | 1234 |
| 7 | Guaymaral Airport |  | CO | 1160 |
| 8 | Frankfurt am Main International Airport |  | DE | 1158 |
| 9 | Zurich Airport |  | CH | 1117 |
| 10 | La Aurora Airport |  | GT | 1092 |
| 11 | Macau International Airport |  | MO | 1038 |
| 12 | El Dorado International Airport |  | CO | 1034 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1032 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 956 |
| 15 | Chicago O'Hare International Airport |  | US | 920 |
| 16 | Kuala Lumpur International Airport |  | MY | 853 |
| 17 | Madrid Barajas International Airport |  | ES | 846 |
| 18 | Salt Lake City International Airport |  | US | 808 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 804 |
| 20 | Capua Airport |  | IT | 793 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 762 |
| 22 | Malpensa International Airport |  | IT | 752 |
| 23 | Bengaluru International Airport |  | IN | 749 |
| 24 | Charles de Gaulle International Airport |  | FR | 747 |
| 25 | Congonhas Airport |  | BR | 727 |
| 26 | Charlotte/Douglas International Airport |  | US | 723 |
| 27 | Daniel K Inouye International Airport |  | US | 683 |
| 28 | Tenerife Norte Airport |  | ES | 680 |
| 29 | Ninoy Aquino International Airport |  | PH | 659 |
| 30 | Barcelona International Airport |  | ES | 642 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 640 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 620 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 613 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 601 |
| 35 | Don Mueang International Airport |  | TH | 593 |
| 36 | Amsterdam Airport Schiphol |  | NL | 593 |
| 37 | Vitoria/Foronda Airport |  | ES | 592 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 569 |
| 39 | Calgary International Airport |  | CA | 564 |
| 40 | O. R. Tambo International Airport |  | ZA | 545 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 476 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 353 | 21m | 244 km | 1,486.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 260 | 24m | 225 km | 1,008.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 253 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 243 | 14m | 114 km | 476.6 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 242 | 1h 26m | 910 km | 3,797.5 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 240 | 28m | 304 km | 1,258.1 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 221 | 1h 10m | 770 km | 2,935.8 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 208 | 19m | 165 km | 591.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 191 | 26m | 275 km | 905.1 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 144 | 27m | 215 km | 533.3 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 142 | 44m | 452 km | 1,106.7 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 138 | 22m | 55 km | 131.2 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 136 | 27m | 152 km | 355.4 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 129 | 20m | 250 km | 557.2 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 125 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 123 | 1h 1m | 695 km | 1,474.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 123 | 18m | 144 km | 306.0 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 121 | 1h 39m | 1,156 km | 2,413.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 115 | 1h 52m | 1,304 km | 2,587.2 t |
| 27 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 113 | 1h 18m | 961 km | 1,873.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N69F |  | Laguardia Airport (KLGA) | John F Kennedy International Airport (KJFK) | 2026-05-27 18:52 UTC | 2026-05-27 19:26 UTC | 33m |
| N3003Q |  | Clearwater Executive Airport (KCLW) | Clearwater Executive Airport (KCLW) | 2026-05-27 18:59 UTC | 2026-05-27 19:24 UTC | 25m |
| N74737 |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Tracy Municipal Airport (KTCY) | 2026-05-27 18:43 UTC | 2026-05-27 19:19 UTC | 35m |
| CXK214 | CXK | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-05-27 18:58 UTC | 2026-05-27 19:14 UTC | 15m |
| LHX3VX | LHX | Munich International Airport (EDDM) | Papa Airport (LHPA) | 2026-05-27 18:36 UTC | 2026-05-27 19:10 UTC | 33m |
| N786MM |  | Long Beach (Daugherty Field) Airport (KLGB) | Bob Hope Airport (KBUR) | 2026-05-27 18:54 UTC | 2026-05-27 19:09 UTC | 15m |
| N844MK |  | Trenton Mercer Airport (KTTN) | Laguardia Airport (KLGA) | 2026-05-27 18:45 UTC | 2026-05-27 19:06 UTC | 21m |
| N707KA |  | 1WA9 (1WA9) | Boeing Field/King County International Airport (KBFI) | 2026-05-27 18:32 UTC | 2026-05-27 19:05 UTC | 32m |
| BCS71R | BCS | Vilnius International Airport (EYVI) | Alytus Airport (EYAL) | 2026-05-27 18:50 UTC | 2026-05-27 19:01 UTC | 10m |
| TVF30ZJ | TVF | Paris-Orly Airport (LFPO) | Toulon-Hyeres Airport (LFTH) | 2026-05-27 17:59 UTC | 2026-05-27 19:00 UTC | 1h 1m |
| CGLII | CGL | Edmonton / Cooking Lake Airport (CEZ3) | Edmonton / Goyer Field (CGF2) | 2026-05-27 18:56 UTC | 2026-05-27 18:59 UTC | 3m |
| PAT115 | PAT | Beaufort Mcas (Merritt Field) Airport (KNBC) | Camp Davis Mcolf Airport (14NC) | 2026-05-27 18:04 UTC | 2026-05-27 18:55 UTC | 51m |
| N441CJ |  | Mc Clellan Airfield (KMCC) | Boonville Airport (KD83) | 2026-05-27 18:06 UTC | 2026-05-27 18:53 UTC | 47m |
| N508XX |  | XS61 (XS61) | 12TE (12TE) | 2026-05-27 18:42 UTC | 2026-05-27 18:52 UTC | 10m |
| N833JB |  | Van Nuys Airport (KVNY) | Sequoia Field (KD86) | 2026-05-27 18:27 UTC | 2026-05-27 18:51 UTC | 24m |
| PJC60 | PJC | John Glenn Columbus International Airport (KCMH) | Curtis L Brown Jr Field (KEYF) | 2026-05-27 17:47 UTC | 2026-05-27 18:50 UTC | 1h 2m |
| N5551K |  | Watertown Municipal Airport (KRYV) | Al's Airway Airport (WS74) | 2026-05-27 18:41 UTC | 2026-05-27 18:49 UTC | 7m |
| LOST77 | LOS | Norman Y Mineta San Jose International Airport (KSJC) | El Peco Ranch Airport (49CL) | 2026-05-27 18:21 UTC | 2026-05-27 18:49 UTC | 27m |
| AAL3325 | American Airlines | Phoenix Sky Harbor International Airport (KPHX) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-05-27 17:09 UTC | 2026-05-27 18:45 UTC | 1h 36m |
| RYR9RJ | Ryanair | Brussels South Charleroi Airport (EBCI) | Plasy Rybnice Airport (LKPS) | 2026-05-27 17:36 UTC | 2026-05-27 18:44 UTC | 1h 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
