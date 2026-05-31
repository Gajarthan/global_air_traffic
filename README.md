# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_00:59:57_UTC-green)

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

**Latest saved flight:** 2026-05-31 00:59:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-31 00:59:57 UTC

- **98,940** saved flights
- **35,202** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **98,940** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,213,456.7 tonnes** estimated CO2 emissions
- **70,345,314 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4115 |
| 2 | SkyWest Airlines | 3694 |
| 3 | IndiGo | 2012 |
| 4 | EJA | 1874 |
| 5 | American Airlines | 1601 |
| 6 | Southwest Airlines | 1492 |
| 7 | ENY | 1221 |
| 8 | Lufthansa | 1172 |
| 9 | Delta Air Lines | 1163 |
| 10 | Vueling | 928 |
| 11 | LATAM Airlines | 878 |
| 12 | WIF | 866 |
| 13 | AXM | 856 |
| 14 | AZU | 799 |
| 15 | LXJ | 748 |
| 16 | Swiss International | 726 |
| 17 | All Nippon Airways | 710 |
| 18 | Alaska Airlines | 695 |
| 19 | QLK | 674 |
| 20 | easyJet | 646 |
| 21 | EJU | 623 |
| 22 | Cathay Pacific | 591 |
| 23 | AEE | 587 |
| 24 | VIV | 577 |
| 25 | Air France | 575 |
| 26 | United Airlines | 555 |
| 27 | CXK | 528 |
| 28 | MXY | 528 |
| 29 | Japan Airlines | 497 |
| 30 | AXB | 492 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 82598 |
| 2 | 🇪🇸 ES | 6878 |
| 3 | 🇮🇳 IN | 6356 |
| 4 | 🇦🇺 AU | 5982 |
| 5 | 🇧🇷 BR | 5419 |
| 6 | 🇩🇪 DE | 5396 |
| 7 | 🇮🇹 IT | 5294 |
| 8 | 🇨🇦 CA | 5073 |
| 9 | 🇯🇵 JP | 4613 |
| 10 | 🇬🇧 GB | 4221 |
| 11 | 🇫🇷 FR | 3966 |
| 12 | 🇨🇴 CO | 3441 |
| 13 | 🇲🇽 MX | 3023 |
| 14 | 🇬🇷 GR | 2848 |
| 15 | 🇳🇴 NO | 2746 |
| 16 | 🇨🇭 CH | 2568 |
| 17 | 🇲🇾 MY | 2177 |
| 18 | 🇹🇷 TR | 1870 |
| 19 | 🇿🇦 ZA | 1737 |
| 20 | 🇳🇿 NZ | 1667 |
| 21 | 🇹🇭 TH | 1640 |
| 22 | 🇵🇱 PL | 1597 |
| 23 | 🇰🇷 KR | 1594 |
| 24 | 🇬🇹 GT | 1470 |
| 25 | 🇵🇭 PH | 1459 |
| 26 | 🇲🇦 MA | 1110 |
| 27 | 🇲🇴 MO | 1046 |
| 28 | 🇳🇱 NL | 992 |
| 29 | 🇲🇪 ME | 956 |
| 30 | 🇭🇷 HR | 881 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2152 |
| 2 | Denver International Airport |  | US | 1692 |
| 3 | Tokyo International Airport |  | JP | 1528 |
| 4 | Indira Gandhi International Airport |  | IN | 1380 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1288 |
| 6 | Harry Reid International Airport |  | US | 1266 |
| 7 | Guaymaral Airport |  | CO | 1238 |
| 8 | Frankfurt am Main International Airport |  | DE | 1177 |
| 9 | Zurich Airport |  | CH | 1141 |
| 10 | La Aurora Airport |  | GT | 1130 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1068 |
| 12 | El Dorado International Airport |  | CO | 1060 |
| 13 | Macau International Airport |  | MO | 1046 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1005 |
| 15 | Chicago O'Hare International Airport |  | US | 989 |
| 16 | Madrid Barajas International Airport |  | ES | 868 |
| 17 | Kuala Lumpur International Airport |  | MY | 860 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 854 |
| 19 | Salt Lake City International Airport |  | US | 838 |
| 20 | Capua Airport |  | IT | 819 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 778 |
| 22 | Charlotte/Douglas International Airport |  | US | 765 |
| 23 | Malpensa International Airport |  | IT | 764 |
| 24 | Charles de Gaulle International Airport |  | FR | 763 |
| 25 | Bengaluru International Airport |  | IN | 761 |
| 26 | Congonhas Airport |  | BR | 749 |
| 27 | Daniel K Inouye International Airport |  | US | 690 |
| 28 | Tenerife Norte Airport |  | ES | 688 |
| 29 | Ninoy Aquino International Airport |  | PH | 666 |
| 30 | Barcelona International Airport |  | ES | 658 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 653 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 646 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 630 |
| 34 | Amsterdam Airport Schiphol |  | NL | 610 |
| 35 | Vitoria/Foronda Airport |  | ES | 606 |
| 36 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 37 | Don Mueang International Airport |  | TH | 601 |
| 38 | Calgary International Airport |  | CA | 582 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 572 |
| 40 | Seattle-Tacoma International Airport |  | US | 563 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 512 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 360 | 21m | 244 km | 1,515.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 265 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 263 | 24m | 225 km | 1,020.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 251 | 14m | 114 km | 492.3 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 244 | 1h 26m | 910 km | 3,828.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 242 | 28m | 304 km | 1,268.6 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 224 | 1h 10m | 770 km | 2,975.7 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 209 | 19m | 165 km | 594.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 195 | 26m | 275 km | 924.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 155 | 20m | 99 km | 265.5 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 146 | 27m | 215 km | 540.7 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 142 | 44m | 452 km | 1,106.7 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 141 | 22m | 55 km | 134.0 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 140 | 27m | 152 km | 365.9 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 129 | 20m | 147 km | 326.4 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 129 | 13m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 127 | 18m | 144 km | 315.9 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 124 | 1h 39m | 1,156 km | 2,473.8 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 124 | 1h 1m | 695 km | 1,486.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 117 | 1h 43m | 1,423 km | 2,871.4 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 115 | 1h 18m | 961 km | 1,906.2 t |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AAL1156 | American Airlines | Phoenix Sky Harbor International Airport (KPHX) | Coffeyville Municipal Airport (KCFV) | 2026-05-30 23:10 UTC | 2026-05-31 00:59 UTC | 1h 49m |
| AAL1682 | American Airlines | Dallas-Fort Worth International Airport (KDFW) | Cincinnati West Airport (KI67) | 2026-05-30 23:25 UTC | 2026-05-31 00:59 UTC | 1h 34m |
| AAL2469 | American Airlines | Dallas-Fort Worth International Airport (KDFW) | Humphreys County Airport (K0M5) | 2026-05-30 23:51 UTC | 2026-05-31 00:59 UTC | 1h 8m |
| AAL2496 | American Airlines | San Antonio International Airport (KSAT) | Horseshoe Landing Airport (16SC) | 2026-05-30 23:02 UTC | 2026-05-31 00:59 UTC | 1h 57m |
| AAL2662 | American Airlines | Charlotte/Douglas International Airport (KCLT) | Montvale Airpark (TN87) | 2026-05-31 00:36 UTC | 2026-05-31 00:59 UTC | 23m |
| AAL2804 | American Airlines | Dallas-Fort Worth International Airport (KDFW) | 4MO0 (4MO0) | 2026-05-31 00:07 UTC | 2026-05-31 00:59 UTC | 52m |
| AAL2806 | American Airlines | Dallas-Fort Worth International Airport (KDFW) | Sherman Army Air Field (KFLV) | 2026-05-31 00:04 UTC | 2026-05-31 00:59 UTC | 55m |
| AAL3005 | American Airlines | Philadelphia International Airport (KPHL) | Chanute Martin Johnson Airport (KCNU) | 2026-05-30 22:32 UTC | 2026-05-31 00:59 UTC | 2h 27m |
| AAL302 | American Airlines | John F Kennedy International Airport (KJFK) | Miami-Roberts County Airport (K3E0) | 2026-05-30 21:47 UTC | 2026-05-31 00:59 UTC | 3h 12m |
| AAL3042 | American Airlines | Philadelphia International Airport (KPHL) | D A Chandler Airport (OI42) | 2026-05-31 00:02 UTC | 2026-05-31 00:59 UTC | 57m |
| AAL3107 | American Airlines | Chicago O'Hare International Airport (KORD) | Chatham Kent Airport (CYCK) | 2026-05-31 00:25 UTC | 2026-05-31 00:59 UTC | 34m |
| AAL3166 | American Airlines | Philadelphia International Airport (KPHL) | Williamson Airport (OI73) | 2026-05-30 23:55 UTC | 2026-05-31 00:59 UTC | 1h 4m |
| AAL3259 | American Airlines | Philadelphia International Airport (KPHL) | Lake County Executive Airport (KLNN) | 2026-05-31 00:07 UTC | 2026-05-31 00:59 UTC | 52m |
| AAL368 | American Airlines | Miami International Airport (KMIA) | MYBO (MYBO) | 2026-05-31 00:47 UTC | 2026-05-31 00:59 UTC | 12m |
| AAL564 | American Airlines | Chicago O'Hare International Airport (KORD) | Rodney (New Glasgow) Airport (CPU3) | 2026-05-31 00:18 UTC | 2026-05-31 00:59 UTC | 41m |
| AAL650 | American Airlines | Cleveland-Hopkins International Airport (KCLE) | Ensminger Airport (74KS) | 2026-05-30 23:20 UTC | 2026-05-31 00:59 UTC | 1h 39m |
| AAL728 | American Airlines | Philadelphia International Airport (KPHL) | Fox Harbour Airport (CFH4) | 2026-05-30 23:37 UTC | 2026-05-31 00:59 UTC | 1h 22m |
| AAL822 | American Airlines | Norfolk International Airport (KORF) | Plymouth Municipal Airport (KPMZ) | 2026-05-31 00:47 UTC | 2026-05-31 00:59 UTC | 12m |
| AAR731 | AAR | Incheon International Airport (RKSI) | Hengchun Airport (RCKW) | 2026-05-30 22:48 UTC | 2026-05-31 00:59 UTC | 2h 11m |
| AAY2046 | AAY | Sarasota/Bradenton International Airport (KSRQ) | Paso Fino Farm Airport (0GA8) | 2026-05-31 00:25 UTC | 2026-05-31 00:59 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
