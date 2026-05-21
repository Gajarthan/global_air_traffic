# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_11:22:32_UTC-green)

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

**Latest saved flight:** 2026-05-21 11:22:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-21 11:22:32 UTC

- **89,876** saved flights
- **32,011** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **89,876** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,111,535.8 tonnes** estimated CO2 emissions
- **64,436,857 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3852 |
| 2 | SkyWest Airlines | 3333 |
| 3 | IndiGo | 1894 |
| 4 | EJA | 1696 |
| 5 | American Airlines | 1369 |
| 6 | Southwest Airlines | 1300 |
| 7 | Lufthansa | 1116 |
| 8 | ENY | 1106 |
| 9 | Delta Air Lines | 987 |
| 10 | Vueling | 856 |
| 11 | LATAM Airlines | 808 |
| 12 | AXM | 799 |
| 13 | WIF | 781 |
| 14 | AZU | 714 |
| 15 | Swiss International | 688 |
| 16 | All Nippon Airways | 679 |
| 17 | LXJ | 668 |
| 18 | Alaska Airlines | 639 |
| 19 | QLK | 639 |
| 20 | easyJet | 592 |
| 21 | Cathay Pacific | 579 |
| 22 | EJU | 579 |
| 23 | AEE | 553 |
| 24 | VIV | 535 |
| 25 | Air France | 525 |
| 26 | Japan Airlines | 482 |
| 27 | CXK | 470 |
| 28 | AXB | 462 |
| 29 | MXY | 457 |
| 30 | AIQ | 436 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 73912 |
| 2 | 🇪🇸 ES | 6380 |
| 3 | 🇮🇳 IN | 5950 |
| 4 | 🇦🇺 AU | 5612 |
| 5 | 🇩🇪 DE | 4966 |
| 6 | 🇮🇹 IT | 4966 |
| 7 | 🇧🇷 BR | 4926 |
| 8 | 🇨🇦 CA | 4498 |
| 9 | 🇯🇵 JP | 4400 |
| 10 | 🇬🇧 GB | 3843 |
| 11 | 🇫🇷 FR | 3604 |
| 12 | 🇨🇴 CO | 3079 |
| 13 | 🇲🇽 MX | 2778 |
| 14 | 🇬🇷 GR | 2592 |
| 15 | 🇳🇴 NO | 2499 |
| 16 | 🇨🇭 CH | 2362 |
| 17 | 🇲🇾 MY | 2009 |
| 18 | 🇿🇦 ZA | 1645 |
| 19 | 🇹🇷 TR | 1637 |
| 20 | 🇳🇿 NZ | 1555 |
| 21 | 🇹🇭 TH | 1534 |
| 22 | 🇵🇱 PL | 1486 |
| 23 | 🇰🇷 KR | 1417 |
| 24 | 🇵🇭 PH | 1387 |
| 25 | 🇬🇹 GT | 1339 |
| 26 | 🇲🇦 MA | 1037 |
| 27 | 🇲🇴 MO | 1035 |
| 28 | 🇲🇪 ME | 918 |
| 29 | 🇳🇱 NL | 916 |
| 30 | 🇭🇷 HR | 814 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1964 |
| 2 | Denver International Airport |  | US | 1507 |
| 3 | Tokyo International Airport |  | JP | 1468 |
| 4 | Indira Gandhi International Airport |  | IN | 1290 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1220 |
| 6 | Harry Reid International Airport |  | US | 1150 |
| 7 | Frankfurt am Main International Airport |  | DE | 1126 |
| 8 | Zurich Airport |  | CH | 1066 |
| 9 | Guaymaral Airport |  | CO | 1049 |
| 10 | Macau International Airport |  | MO | 1035 |
| 11 | La Aurora Airport |  | GT | 1019 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 992 |
| 13 | El Dorado International Airport |  | CO | 980 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 913 |
| 15 | Chicago O'Hare International Airport |  | US | 868 |
| 16 | Madrid Barajas International Airport |  | ES | 819 |
| 17 | Kuala Lumpur International Airport |  | MY | 795 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 770 |
| 19 | Capua Airport |  | IT | 761 |
| 20 | Salt Lake City International Airport |  | US | 756 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 732 |
| 22 | Malpensa International Airport |  | IT | 727 |
| 23 | Bengaluru International Airport |  | IN | 715 |
| 24 | Charles de Gaulle International Airport |  | FR | 700 |
| 25 | Congonhas Airport |  | BR | 691 |
| 26 | Charlotte/Douglas International Airport |  | US | 689 |
| 27 | Daniel K Inouye International Airport |  | US | 658 |
| 28 | Tenerife Norte Airport |  | ES | 657 |
| 29 | Ninoy Aquino International Airport |  | PH | 637 |
| 30 | Barcelona International Airport |  | ES | 604 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 600 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 589 |
| 34 | Vitoria/Foronda Airport |  | ES | 570 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 567 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 37 | Don Mueang International Airport |  | TH | 562 |
| 38 | Amsterdam Airport Schiphol |  | NL | 562 |
| 39 | Calgary International Airport |  | CA | 533 |
| 40 | O. R. Tambo International Airport |  | ZA | 520 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 429 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 334 | 21m | 244 km | 1,406.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 249 | 24m | 225 km | 966.0 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 235 | 14m | 114 km | 460.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 232 | 1h 26m | 910 km | 3,640.6 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 231 | 28m | 304 km | 1,211.0 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 229 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 208 | 1h 10m | 770 km | 2,763.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 201 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 196 | 19m | 165 km | 557.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 186 | 26m | 275 km | 881.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 148 | 21m | 99 km | 253.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 138 | 31m | 369 km | 878.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 132 | 27m | 215 km | 488.9 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 132 | 22m | 55 km | 125.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 129 | 14m | 154 km | 341.8 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 123 | 20m | 250 km | 531.3 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 116 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 116 | 18m | 144 km | 288.5 t |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 109 | 1h 18m | 961 km | 1,806.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 109 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 108 | 1h 40m | 1,156 km | 2,154.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N769FG |  | Trenton Mercer Airport (KTTN) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-05-21 10:39 UTC | 2026-05-21 11:22 UTC | 42m |
| BHA508 | BHA | Langtang Airport (VNLT) | Tribhuvan International Airport (VNKT) | 2026-05-21 11:14 UTC | 2026-05-21 11:15 UTC | 1m |
| CITT85 | CIT | Wichita Dwight D Eisenhower Ntl Airport (KICT) | Kinsley Municipal Airport (K33K) | 2026-05-21 10:42 UTC | 2026-05-21 11:12 UTC | 29m |
| HYD164 | HYD | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Rouyn-Noranda Airport (CYUY) | 2026-05-21 10:11 UTC | 2026-05-21 11:05 UTC | 54m |
| MRS1315 | MRS | Cherif Al Idrissi Airport (GMTA) | Fes Sefrou Airport (GMFU) | 2026-05-21 10:47 UTC | 2026-05-21 11:01 UTC | 13m |
| WWIND222 | WWI | Anglesey Airport (EGOV) | Caernarfon Airport (EGCK) | 2026-05-21 10:05 UTC | 2026-05-21 10:53 UTC | 48m |
| AIC219 | Air India | Indira Gandhi International Airport (VIDP) | Langtang Airport (VNLT) | 2026-05-21 09:33 UTC | 2026-05-21 10:51 UTC | 1h 17m |
| WIF77P | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-05-21 09:58 UTC | 2026-05-21 10:45 UTC | 47m |
| FJO64J | FJO | Ljubljana Joze Pucnik Airport (LJLJ) | Southampton Airport (EGHI) | 2026-05-21 08:39 UTC | 2026-05-21 10:44 UTC | 2h 4m |
| CUCO502 | CUC | LE83 (LE83) | Valladolid Airport (LEVD) | 2026-05-21 10:28 UTC | 2026-05-21 10:43 UTC | 15m |
| MOLOCH63 | MOL | Cognac-Chateaubernard (BA 709) Air Base (LFBG) | St Jean D'angely Airport (LFIY) | 2026-05-21 10:10 UTC | 2026-05-21 10:41 UTC | 30m |
| TMN1 | TMN | Auckland International Airport (NZAA) | Sydney Kingsford Smith International Airport (YSSY) | 2026-05-21 07:52 UTC | 2026-05-21 10:40 UTC | 2h 48m |
| DHEAL | DHE | Bonn-Hangelar Airport (EDKB) | Bonn-Hangelar Airport (EDKB) | 2026-05-21 09:28 UTC | 2026-05-21 10:40 UTC | 1h 11m |
| N357EA |  | Cottonwood Airport (KP52) | Glendale Regional Airport (KGEU) | 2026-05-21 09:29 UTC | 2026-05-21 10:37 UTC | 1h 8m |
| GDERH | GDE | Sherburn-In-Elmet Airfield (EGCJ) | Sherburn-In-Elmet Airfield (EGCJ) | 2026-05-21 10:34 UTC | 2026-05-21 10:36 UTC | 2m |
| ANE1121 | ANE | Madrid Barajas International Airport (LEMD) | La Morgal Airport (LEMR) | 2026-05-21 10:00 UTC | 2026-05-21 10:36 UTC | 36m |
| RYR2SM | Ryanair | Dublin Airport (EIDW) | Liverpool John Lennon Airport (EGGP) | 2026-05-21 10:02 UTC | 2026-05-21 10:36 UTC | 33m |
| SEH4JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-05-21 10:09 UTC | 2026-05-21 10:36 UTC | 26m |
| AEE242 | AEE | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-05-21 09:59 UTC | 2026-05-21 10:31 UTC | 32m |
| EZY45JX | easyJet | Glasgow International Airport (EGPF) | Václav Havel Airport (LKPR) | 2026-05-21 08:31 UTC | 2026-05-21 10:31 UTC | 1h 59m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
