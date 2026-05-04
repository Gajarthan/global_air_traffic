# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_14:58:03_UTC-green)

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

**Latest saved flight:** 2026-05-04 14:58:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-04 14:58:03 UTC

- **67,694** saved flights
- **25,449** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **67,694** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **832,142.5 tonnes** estimated CO2 emissions
- **48,240,144 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2906 |
| 2 | SkyWest Airlines | 2489 |
| 3 | IndiGo | 1573 |
| 4 | EJA | 1205 |
| 5 | American Airlines | 1047 |
| 6 | Southwest Airlines | 949 |
| 7 | Lufthansa | 871 |
| 8 | ENY | 829 |
| 9 | Vueling | 665 |
| 10 | AXM | 658 |
| 11 | LATAM Airlines | 631 |
| 12 | All Nippon Airways | 579 |
| 13 | WIF | 567 |
| 14 | Delta Air Lines | 564 |
| 15 | AZU | 547 |
| 16 | Swiss International | 525 |
| 17 | QLK | 523 |
| 18 | LXJ | 489 |
| 19 | Alaska Airlines | 458 |
| 20 | easyJet | 452 |
| 21 | AEE | 450 |
| 22 | EJU | 438 |
| 23 | VIV | 421 |
| 24 | Cathay Pacific | 410 |
| 25 | Japan Airlines | 399 |
| 26 | Air France | 398 |
| 27 | AXB | 384 |
| 28 | AIQ | 346 |
| 29 | CXK | 345 |
| 30 | JetBlue | 328 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 53364 |
| 2 | 🇪🇸 ES | 4959 |
| 3 | 🇮🇳 IN | 4958 |
| 4 | 🇦🇺 AU | 4497 |
| 5 | 🇧🇷 BR | 3801 |
| 6 | 🇩🇪 DE | 3793 |
| 7 | 🇮🇹 IT | 3713 |
| 8 | 🇯🇵 JP | 3667 |
| 9 | 🇨🇦 CA | 3320 |
| 10 | 🇬🇧 GB | 2944 |
| 11 | 🇫🇷 FR | 2692 |
| 12 | 🇨🇴 CO | 2655 |
| 13 | 🇲🇽 MX | 2148 |
| 14 | 🇬🇷 GR | 2048 |
| 15 | 🇨🇭 CH | 1893 |
| 16 | 🇳🇴 NO | 1844 |
| 17 | 🇲🇾 MY | 1632 |
| 18 | 🇿🇦 ZA | 1367 |
| 19 | 🇳🇿 NZ | 1264 |
| 20 | 🇹🇭 TH | 1237 |
| 21 | 🇹🇷 TR | 1214 |
| 22 | 🇵🇭 PH | 1137 |
| 23 | 🇵🇱 PL | 1109 |
| 24 | 🇬🇹 GT | 1097 |
| 25 | 🇰🇷 KR | 1089 |
| 26 | 🇲🇦 MA | 828 |
| 27 | 🇲🇴 MO | 767 |
| 28 | 🇲🇪 ME | 734 |
| 29 | 🇳🇱 NL | 713 |
| 30 | 🇮🇩 ID | 582 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1485 |
| 2 | Tokyo International Airport |  | JP | 1235 |
| 3 | Denver International Airport |  | US | 1109 |
| 4 | Indira Gandhi International Airport |  | IN | 1036 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 999 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Frankfurt am Main International Airport |  | DE | 875 |
| 8 | Guaymaral Airport |  | CO | 850 |
| 9 | Harry Reid International Airport |  | US | 841 |
| 10 | La Aurora Airport |  | GT | 814 |
| 11 | Zurich Airport |  | CH | 807 |
| 12 | Macau International Airport |  | MO | 767 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 663 |
| 14 | Kuala Lumpur International Airport |  | MY | 654 |
| 15 | Madrid Barajas International Airport |  | ES | 647 |
| 16 | Chicago O'Hare International Airport |  | US | 646 |
| 17 | Bengaluru International Airport |  | IN | 602 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 601 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 591 |
| 20 | Malpensa International Airport |  | IT | 589 |
| 21 | Congonhas Airport |  | BR | 545 |
| 22 | Salt Lake City International Airport |  | US | 536 |
| 23 | Tenerife Norte Airport |  | ES | 535 |
| 24 | Charles de Gaulle International Airport |  | FR | 533 |
| 25 | Charlotte/Douglas International Airport |  | US | 531 |
| 26 | Ninoy Aquino International Airport |  | PH | 517 |
| 27 | Capua Airport |  | IT | 515 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 499 |
| 29 | Daniel K Inouye International Airport |  | US | 490 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 476 |
| 31 | Barcelona International Airport |  | ES | 468 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 457 |
| 33 | Vitoria/Foronda Airport |  | ES | 449 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 448 |
| 35 | Don Mueang International Airport |  | TH | 433 |
| 36 | O. R. Tambo International Airport |  | ZA | 432 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 425 |
| 38 | Amsterdam Airport Schiphol |  | NL | 420 |
| 39 | Reno/Tahoe International Airport |  | US | 405 |
| 40 | Calgary International Airport |  | CA | 397 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 351 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 261 | 1h 7m | 706 km | 3,177.7 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 229 | 21m | 244 km | 964.3 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 208 | 24m | 225 km | 806.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 194 | 28m | 304 km | 1,017.0 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 194 | 1h 27m | 910 km | 3,044.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 171 | 20m | 165 km | 486.4 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 168 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 162 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 151 | 26m | 275 km | 715.5 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 151 | 1h 12m | 770 km | 2,005.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 129 | 21m | 99 km | 221.0 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 124 | 44m | 452 km | 966.4 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 114 | 27m | 152 km | 297.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 113 | 31m | 369 km | 719.3 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 108 | 20m | 250 km | 466.5 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 103 | 27m | 215 km | 381.5 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 102 | 20m | 147 km | 258.1 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 97 | 1h 41m | 1,156 km | 1,935.1 t |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 96 | 58m | 493 km | 816.7 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 95 | 14m | 154 km | 251.7 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 2m | 695 km | 1,114.8 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 92 | 1h 53m | 1,304 km | 2,069.8 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 91 | 1h 43m | 1,423 km | 2,233.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 91 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 91 | 52m | 556 km | 872.3 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 86 | 1h 19m | 961 km | 1,425.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HUE12P | HUE | Zurich Airport (LSZH) | Lausanne-la Blecherette Airport (LSGL) | 2026-05-04 14:28 UTC | 2026-05-04 14:58 UTC | 29m |
| N730CA |  | Orlando Sanford International Airport (KSFB) | Orlando Sanford International Airport (KSFB) | 2026-05-04 14:46 UTC | 2026-05-04 14:57 UTC | 11m |
| N78183 |  | Denton Enterprise Airport (KDTO) | Bridgeport Municipal Airport (KXBP) | 2026-05-04 14:30 UTC | 2026-05-04 14:55 UTC | 24m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-05-04 14:38 UTC | 2026-05-04 14:49 UTC | 10m |
| DHXCD | DHX | Straubing Airport (EDMS) | Straubing Airport (EDMS) | 2026-05-04 14:36 UTC | 2026-05-04 14:49 UTC | 12m |
| LTHL239 | LTH | Kingsville Nas Airport (KNQI) | Kleberg County Airport (KIKG) | 2026-05-04 14:24 UTC | 2026-05-04 14:44 UTC | 19m |
| N778JA |  | CA40 (CA40) | San Gabriel Valley Airport (KEMT) | 2026-05-04 14:05 UTC | 2026-05-04 14:43 UTC | 38m |
| WIF3LA | WIF | Oslo Gardermoen Airport (ENGM) | Bringeland Airport (ENBL) | 2026-05-04 13:33 UTC | 2026-05-04 14:36 UTC | 1h 3m |
| N422LS |  | Purdue University Airport (KLAF) | Purdue University Airport (KLAF) | 2026-05-04 14:30 UTC | 2026-05-04 14:35 UTC | 4m |
| CWA922 | CWA | Calgary International Airport (CYYC) | Bow Island Airport (CEF3) | 2026-05-04 14:08 UTC | 2026-05-04 14:35 UTC | 26m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-05-04 13:33 UTC | 2026-05-04 14:35 UTC | 1h 2m |
| N936EA |  | Lynchburg Regional/Preston Glenn Field (KLYH) | Norfolk International Airport (KORF) | 2026-05-04 13:59 UTC | 2026-05-04 14:27 UTC | 28m |
| EJA400 | EJA | Hampton Roads Executive Airport (KPVG) | Bear Pen Airport (NC43) | 2026-05-04 13:52 UTC | 2026-05-04 14:24 UTC | 31m |
| N6538W |  | St Elmo Airport (K2R5) | St Elmo Airport (K2R5) | 2026-05-04 14:23 UTC | 2026-05-04 14:23 UTC | 0m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-05-04 13:55 UTC | 2026-05-04 14:22 UTC | 26m |
| SAS740 | Scandinavian Airlines | Stockholm-Arlanda Airport (ESSA) | Vilnius International Airport (EYVI) | 2026-05-04 13:19 UTC | 2026-05-04 14:21 UTC | 1h 1m |
| N8116B |  | Phyllis Field (6IL2) | De Kalb Taylor Municipal Airport (KDKB) | 2026-05-04 13:56 UTC | 2026-05-04 14:19 UTC | 22m |
| N224JV |  | Wilkes County Airport (KUKF) | Bear Pen Airport (NC43) | 2026-05-04 13:52 UTC | 2026-05-04 14:17 UTC | 25m |
| XBKYV | XBK | Ingeniero Juan Guillermo Villasana Airport (MMPC) | Tlaxcala Airport (MMTA) | 2026-05-04 14:01 UTC | 2026-05-04 14:15 UTC | 14m |
| FOXX755 | FOX | Beaufort Mcas (Merritt Field) Airport (KNBC) | Macdill Afb Airport (KMCF) | 2026-05-04 12:45 UTC | 2026-05-04 14:15 UTC | 1h 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
