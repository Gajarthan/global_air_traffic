# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_22:23:48_UTC-green)

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

**Latest saved flight:** 2026-05-04 22:23:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-04 22:23:48 UTC

- **68,575** saved flights
- **25,737** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **68,575** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **842,944.9 tonnes** estimated CO2 emissions
- **48,866,373 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2948 |
| 2 | SkyWest Airlines | 2544 |
| 3 | IndiGo | 1581 |
| 4 | EJA | 1239 |
| 5 | American Airlines | 1064 |
| 6 | Southwest Airlines | 969 |
| 7 | Lufthansa | 880 |
| 8 | ENY | 844 |
| 9 | Vueling | 675 |
| 10 | AXM | 658 |
| 11 | LATAM Airlines | 637 |
| 12 | All Nippon Airways | 579 |
| 13 | WIF | 579 |
| 14 | Delta Air Lines | 577 |
| 15 | AZU | 558 |
| 16 | Swiss International | 529 |
| 17 | QLK | 523 |
| 18 | LXJ | 495 |
| 19 | Alaska Airlines | 467 |
| 20 | easyJet | 455 |
| 21 | AEE | 451 |
| 22 | EJU | 447 |
| 23 | VIV | 427 |
| 24 | Cathay Pacific | 413 |
| 25 | Air France | 404 |
| 26 | Japan Airlines | 399 |
| 27 | AXB | 387 |
| 28 | CXK | 348 |
| 29 | AIQ | 346 |
| 30 | MXY | 333 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 54367 |
| 2 | 🇪🇸 ES | 5024 |
| 3 | 🇮🇳 IN | 4981 |
| 4 | 🇦🇺 AU | 4503 |
| 5 | 🇧🇷 BR | 3854 |
| 6 | 🇩🇪 DE | 3833 |
| 7 | 🇮🇹 IT | 3763 |
| 8 | 🇯🇵 JP | 3667 |
| 9 | 🇨🇦 CA | 3377 |
| 10 | 🇬🇧 GB | 2977 |
| 11 | 🇫🇷 FR | 2722 |
| 12 | 🇨🇴 CO | 2657 |
| 13 | 🇲🇽 MX | 2182 |
| 14 | 🇬🇷 GR | 2060 |
| 15 | 🇨🇭 CH | 1903 |
| 16 | 🇳🇴 NO | 1871 |
| 17 | 🇲🇾 MY | 1635 |
| 18 | 🇿🇦 ZA | 1371 |
| 19 | 🇳🇿 NZ | 1270 |
| 20 | 🇹🇭 TH | 1237 |
| 21 | 🇹🇷 TR | 1226 |
| 22 | 🇵🇭 PH | 1141 |
| 23 | 🇵🇱 PL | 1125 |
| 24 | 🇬🇹 GT | 1111 |
| 25 | 🇰🇷 KR | 1091 |
| 26 | 🇲🇦 MA | 835 |
| 27 | 🇲🇴 MO | 777 |
| 28 | 🇲🇪 ME | 742 |
| 29 | 🇳🇱 NL | 713 |
| 30 | 🇮🇩 ID | 582 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1512 |
| 2 | Tokyo International Airport |  | JP | 1235 |
| 3 | Denver International Airport |  | US | 1125 |
| 4 | Indira Gandhi International Airport |  | IN | 1043 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1006 |
| 6 | Frankfurt am Main International Airport |  | DE | 881 |
| 7 | El Dorado International Airport |  | CO | 878 |
| 8 | Harry Reid International Airport |  | US | 853 |
| 9 | Guaymaral Airport |  | CO | 852 |
| 10 | La Aurora Airport |  | GT | 827 |
| 11 | Zurich Airport |  | CH | 814 |
| 12 | Macau International Airport |  | MO | 777 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 674 |
| 14 | Chicago O'Hare International Airport |  | US | 659 |
| 15 | Kuala Lumpur International Airport |  | MY | 656 |
| 16 | Madrid Barajas International Airport |  | ES | 654 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 612 |
| 18 | Bengaluru International Airport |  | IN | 603 |
| 19 | Malpensa International Airport |  | IT | 599 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 591 |
| 21 | Congonhas Airport |  | BR | 551 |
| 22 | Salt Lake City International Airport |  | US | 546 |
| 23 | Charlotte/Douglas International Airport |  | US | 541 |
| 24 | Tenerife Norte Airport |  | ES | 540 |
| 25 | Charles de Gaulle International Airport |  | FR | 539 |
| 26 | Capua Airport |  | IT | 528 |
| 27 | Ninoy Aquino International Airport |  | PH | 519 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 502 |
| 29 | Daniel K Inouye International Airport |  | US | 498 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 483 |
| 31 | Barcelona International Airport |  | ES | 476 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 463 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 457 |
| 34 | Vitoria/Foronda Airport |  | ES | 455 |
| 35 | O. R. Tambo International Airport |  | ZA | 434 |
| 36 | Don Mueang International Airport |  | TH | 433 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 428 |
| 38 | Amsterdam Airport Schiphol |  | NL | 420 |
| 39 | Reno/Tahoe International Airport |  | US | 410 |
| 40 | Calgary International Airport |  | CA | 405 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 352 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 261 | 1h 7m | 706 km | 3,177.7 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 234 | 21m | 244 km | 985.3 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 208 | 24m | 225 km | 806.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 194 | 28m | 304 km | 1,017.0 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 194 | 1h 27m | 910 km | 3,044.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 171 | 20m | 165 km | 486.4 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 171 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 162 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 154 | 26m | 275 km | 729.7 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 151 | 1h 12m | 770 km | 2,005.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 130 | 21m | 99 km | 222.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 124 | 44m | 452 km | 966.4 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 115 | 31m | 369 km | 732.0 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 108 | 20m | 250 km | 466.5 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 105 | 27m | 215 km | 388.9 t |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 104 | 20m | 147 km | 263.2 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 96 | 58m | 493 km | 816.7 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 96 | 14m | 154 km | 254.4 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 95 | 1h 2m | 695 km | 1,138.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 93 | 1h 43m | 1,423 km | 2,282.4 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 91 | 12m | - | - |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 87 | 1h 19m | 961 km | 1,442.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| KAL432 | Korean Air | Incheon International Airport (RKSI) | Incheon International Airport (RKSI) | 2026-05-04 07:27 UTC | 2026-05-04 22:23 UTC | 14h 56m |
| CPA300 | Cathay Pacific | Munich International Airport (EDDM) | Macau International Airport (VMMC) | 2026-05-04 11:54 UTC | 2026-05-04 22:19 UTC | 10h 25m |
| AUB1350 | AUB | Auburn University Regional Airport (KAUO) | Columbus Airport (KCSG) | 2026-05-04 21:35 UTC | 2026-05-04 22:07 UTC | 32m |
| CPA395 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-05-04 14:31 UTC | 2026-05-04 22:06 UTC | 7h 35m |
| EXCEL11 | EXC | Fort Clark Springs Airport (74TX) | Flying J Ranch Airport (7TE4) | 2026-05-04 21:43 UTC | 2026-05-04 22:05 UTC | 21m |
| N850ZM |  | Camarillo Airport (KCMA) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-05-04 20:55 UTC | 2026-05-04 22:02 UTC | 1h 6m |
| N450EA |  | Gwinnett County/Briscoe Field (KLZU) | Cy Nunnally Memorial Airport (KD73) | 2026-05-04 21:42 UTC | 2026-05-04 21:59 UTC | 16m |
| N137RJ |  | Brackett Field (KPOC) | Brackett Field (KPOC) | 2026-05-04 21:45 UTC | 2026-05-04 21:58 UTC | 13m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-05-04 10:44 UTC | 2026-05-04 21:56 UTC | 11h 11m |
| N96FA |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-05-04 21:30 UTC | 2026-05-04 21:56 UTC | 26m |
| LS31 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-05-04 20:28 UTC | 2026-05-04 21:56 UTC | 1h 27m |
| HKC9484 | HKC | Ataturk International Airport (LTBA) | Macau International Airport (VMMC) | 2026-05-04 09:26 UTC | 2026-05-04 21:54 UTC | 12h 27m |
| N77ZR |  | Creve Coeur Airport (K1H0) | Blackhawk Airport (6MO0) | 2026-05-04 21:41 UTC | 2026-05-04 21:51 UTC | 10m |
| N69F |  | John F Kennedy International Airport (KJFK) | John F Kennedy International Airport (KJFK) | 2026-05-04 21:26 UTC | 2026-05-04 21:50 UTC | 24m |
| CRK081 | CRK | Vancouver International Airport (CYVR) | Macau International Airport (VMMC) | 2026-05-04 08:48 UTC | 2026-05-04 21:49 UTC | 13h 0m |
| N716AT |  | Robert/Bob/Curtis Memorial Airport (PFNO) | Kivalina Airport (PAVL) | 2026-05-04 21:03 UTC | 2026-05-04 21:47 UTC | 44m |
| KENT31 | KEN | Danaher Airport (7TX0) | Joseph Of Cupertino Stolport Airport (TS20) | 2026-05-04 21:32 UTC | 2026-05-04 21:44 UTC | 11m |
| AIC314 | Air India | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-05-04 17:21 UTC | 2026-05-04 21:40 UTC | 4h 19m |
| N65956 |  | Addison Airport (KADS) | Mid-Way Regional Airport (KJWY) | 2026-05-04 20:57 UTC | 2026-05-04 21:40 UTC | 42m |
| N516JR |  | Slobovia Outernational Airport (MS71) | Cuba Farm Airport (LA33) | 2026-05-04 21:13 UTC | 2026-05-04 21:38 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
