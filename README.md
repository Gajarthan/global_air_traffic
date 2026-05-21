# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_14:17:20_UTC-green)

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

**Latest saved flight:** 2026-05-21 14:17:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-21 14:17:20 UTC

- **90,049** saved flights
- **32,055** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **90,049** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,113,297.6 tonnes** estimated CO2 emissions
- **64,538,988 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3858 |
| 2 | SkyWest Airlines | 3333 |
| 3 | IndiGo | 1896 |
| 4 | EJA | 1697 |
| 5 | American Airlines | 1369 |
| 6 | Southwest Airlines | 1300 |
| 7 | Lufthansa | 1118 |
| 8 | ENY | 1107 |
| 9 | Delta Air Lines | 988 |
| 10 | Vueling | 857 |
| 11 | LATAM Airlines | 814 |
| 12 | AXM | 800 |
| 13 | WIF | 788 |
| 14 | AZU | 716 |
| 15 | Swiss International | 688 |
| 16 | All Nippon Airways | 679 |
| 17 | LXJ | 668 |
| 18 | Alaska Airlines | 639 |
| 19 | QLK | 639 |
| 20 | easyJet | 592 |
| 21 | Cathay Pacific | 579 |
| 22 | EJU | 579 |
| 23 | AEE | 554 |
| 24 | VIV | 535 |
| 25 | Air France | 526 |
| 26 | Japan Airlines | 482 |
| 27 | CXK | 473 |
| 28 | AXB | 462 |
| 29 | MXY | 458 |
| 30 | AIQ | 437 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 74015 |
| 2 | 🇪🇸 ES | 6390 |
| 3 | 🇮🇳 IN | 5957 |
| 4 | 🇦🇺 AU | 5615 |
| 5 | 🇩🇪 DE | 4978 |
| 6 | 🇮🇹 IT | 4970 |
| 7 | 🇧🇷 BR | 4948 |
| 8 | 🇨🇦 CA | 4507 |
| 9 | 🇯🇵 JP | 4400 |
| 10 | 🇬🇧 GB | 3856 |
| 11 | 🇫🇷 FR | 3619 |
| 12 | 🇨🇴 CO | 3091 |
| 13 | 🇲🇽 MX | 2778 |
| 14 | 🇬🇷 GR | 2595 |
| 15 | 🇳🇴 NO | 2519 |
| 16 | 🇨🇭 CH | 2371 |
| 17 | 🇲🇾 MY | 2011 |
| 18 | 🇿🇦 ZA | 1645 |
| 19 | 🇹🇷 TR | 1639 |
| 20 | 🇳🇿 NZ | 1555 |
| 21 | 🇹🇭 TH | 1537 |
| 22 | 🇵🇱 PL | 1486 |
| 23 | 🇰🇷 KR | 1417 |
| 24 | 🇵🇭 PH | 1387 |
| 25 | 🇬🇹 GT | 1348 |
| 26 | 🇲🇦 MA | 1038 |
| 27 | 🇲🇴 MO | 1035 |
| 28 | 🇲🇪 ME | 919 |
| 29 | 🇳🇱 NL | 916 |
| 30 | 🇭🇷 HR | 819 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1964 |
| 2 | Denver International Airport |  | US | 1507 |
| 3 | Tokyo International Airport |  | JP | 1468 |
| 4 | Indira Gandhi International Airport |  | IN | 1292 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1221 |
| 6 | Harry Reid International Airport |  | US | 1152 |
| 7 | Frankfurt am Main International Airport |  | DE | 1127 |
| 8 | Zurich Airport |  | CH | 1067 |
| 9 | Guaymaral Airport |  | CO | 1057 |
| 10 | Macau International Airport |  | MO | 1035 |
| 11 | La Aurora Airport |  | GT | 1028 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 993 |
| 13 | El Dorado International Airport |  | CO | 981 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 913 |
| 15 | Chicago O'Hare International Airport |  | US | 868 |
| 16 | Madrid Barajas International Airport |  | ES | 819 |
| 17 | Kuala Lumpur International Airport |  | MY | 796 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 771 |
| 19 | Capua Airport |  | IT | 761 |
| 20 | Salt Lake City International Airport |  | US | 756 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 732 |
| 22 | Malpensa International Airport |  | IT | 727 |
| 23 | Bengaluru International Airport |  | IN | 716 |
| 24 | Charles de Gaulle International Airport |  | FR | 702 |
| 25 | Congonhas Airport |  | BR | 692 |
| 26 | Charlotte/Douglas International Airport |  | US | 689 |
| 27 | Daniel K Inouye International Airport |  | US | 658 |
| 28 | Tenerife Norte Airport |  | ES | 658 |
| 29 | Ninoy Aquino International Airport |  | PH | 637 |
| 30 | Barcelona International Airport |  | ES | 605 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 600 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 591 |
| 34 | Vitoria/Foronda Airport |  | ES | 571 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 569 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 37 | Don Mueang International Airport |  | TH | 564 |
| 38 | Amsterdam Airport Schiphol |  | NL | 562 |
| 39 | Calgary International Airport |  | CA | 533 |
| 40 | O. R. Tambo International Airport |  | ZA | 520 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 432 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 334 | 21m | 244 km | 1,406.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 249 | 24m | 225 km | 966.0 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 235 | 14m | 114 km | 460.9 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 233 | 9m | - | - |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 232 | 1h 26m | 910 km | 3,640.6 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 231 | 28m | 304 km | 1,211.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 208 | 1h 10m | 770 km | 2,763.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 201 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 196 | 19m | 165 km | 557.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 186 | 26m | 275 km | 881.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 148 | 21m | 99 km | 253.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 138 | 31m | 369 km | 878.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 134 | 27m | 215 km | 496.3 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 133 | 23m | 55 km | 126.4 t |
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
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 110 | 1h 18m | 961 km | 1,823.3 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 109 | 1h 40m | 1,156 km | 2,174.5 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 109 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CGPZT | CGP | Burlington Executive (CZBA) | Burlington Executive (CZBA) | 2026-05-21 13:40 UTC | 2026-05-21 14:17 UTC | 36m |
| N863SP |  | Marv Skie-Lincoln County Airport (KY14) | Oakleaf Airport (9SD8) | 2026-05-21 13:52 UTC | 2026-05-21 14:12 UTC | 20m |
| TGPEM | TGP | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-05-21 13:58 UTC | 2026-05-21 14:10 UTC | 12m |
| N72NG |  | Montgomery-Gibbs Executive Airport (KMYF) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-05-21 13:39 UTC | 2026-05-21 14:09 UTC | 29m |
| N307TL |  | Midland Airpark (KMDD) | Austin-Bergstrom International Airport (KAUS) | 2026-05-21 13:07 UTC | 2026-05-21 14:07 UTC | 1h 0m |
| FDB2RG | flydubai | Henri Coanda International Airport (LROP) | Queen Alia International Airport (OJAI) | 2026-05-21 12:18 UTC | 2026-05-21 14:05 UTC | 1h 46m |
| HBZWD | HBZ | Bern Belp Airport (LSZB) | Raron Airport (LSTA) | 2026-05-21 12:38 UTC | 2026-05-21 13:57 UTC | 1h 18m |
| N626GH |  | Deerfield Airport (8MD7) | Ocean City Municipal Airport (KOXB) | 2026-05-21 13:11 UTC | 2026-05-21 13:56 UTC | 44m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-05-21 13:06 UTC | 2026-05-21 13:56 UTC | 49m |
| TAM3313 | LATAM Airlines | Bacabal Airport (SNBI) | Fazenda Recanto Feliz Airport (SDRF) | 2026-05-21 07:59 UTC | 2026-05-21 13:55 UTC | 5h 55m |
| UFX62 | UFX | Humberside Airport (EGNJ) | Wickenby Aerodrome (EGNW) | 2026-05-21 13:15 UTC | 2026-05-21 13:54 UTC | 39m |
| N246R |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-05-21 13:10 UTC | 2026-05-21 13:53 UTC | 43m |
| DEAPR | DEA | Lubeck Blankensee Airport (EDHL) | Lubeck Blankensee Airport (EDHL) | 2026-05-21 13:52 UTC | 2026-05-21 13:52 UTC | 0m |
| CYP107 | CYP | Queen Alia International Airport (OJAI) | Queen Alia International Airport (OJAI) | 2026-05-21 13:50 UTC | 2026-05-21 13:52 UTC | 1m |
| AXY126G | AXY | Antalya International Airport (LTAI) | Queen Alia International Airport (OJAI) | 2026-05-21 13:05 UTC | 2026-05-21 13:52 UTC | 46m |
| ISR515 | ISR | Ben Gurion International Airport (LLBG) | Queen Alia International Airport (OJAI) | 2026-05-21 13:28 UTC | 2026-05-21 13:52 UTC | 23m |
| UAE5M | Emirates | Queen Alia International Airport (OJAI) | Queen Alia International Airport (OJAI) | 2026-05-21 13:31 UTC | 2026-05-21 13:52 UTC | 20m |
| ECLHI | ECL | Viseu Airport (LPVZ) | Viseu Airport (LPVZ) | 2026-05-21 13:50 UTC | 2026-05-21 13:51 UTC | 0m |
| N870ST |  | Wilkes-Barre/Scranton International Airport (KAVP) | Lehigh Valley International Airport (KABE) | 2026-05-21 13:31 UTC | 2026-05-21 13:50 UTC | 19m |
| SAVER40 | SAV | Snåsa Airfield Gronora (ENGS) | Trondheim Airport Vaernes (ENVA) | 2026-05-21 12:50 UTC | 2026-05-21 13:37 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
