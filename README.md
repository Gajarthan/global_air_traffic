# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--11_10:51:56_UTC-green)

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

**Latest saved flight:** 2026-06-11 10:51:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-11 10:51:56 UTC

- **107,938** saved flights
- **37,791** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **107,938** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,319,650.4 tonnes** estimated CO2 emissions
- **76,501,475 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4454 |
| 2 | SkyWest Airlines | 4046 |
| 3 | IndiGo | 2140 |
| 4 | EJA | 2080 |
| 5 | American Airlines | 1715 |
| 6 | Southwest Airlines | 1621 |
| 7 | ENY | 1347 |
| 8 | Delta Air Lines | 1280 |
| 9 | Lufthansa | 1231 |
| 10 | Vueling | 987 |
| 11 | LATAM Airlines | 957 |
| 12 | WIF | 950 |
| 13 | AXM | 917 |
| 14 | AZU | 877 |
| 15 | LXJ | 813 |
| 16 | Swiss International | 788 |
| 17 | All Nippon Airways | 751 |
| 18 | Alaska Airlines | 740 |
| 19 | QLK | 717 |
| 20 | easyJet | 698 |
| 21 | EJU | 687 |
| 22 | Cathay Pacific | 648 |
| 23 | AEE | 616 |
| 24 | VIV | 614 |
| 25 | Air France | 610 |
| 26 | United Airlines | 594 |
| 27 | MXY | 580 |
| 28 | CXK | 569 |
| 29 | Japan Airlines | 534 |
| 30 | AXB | 531 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 90729 |
| 2 | 🇪🇸 ES | 7411 |
| 3 | 🇮🇳 IN | 6743 |
| 4 | 🇦🇺 AU | 6476 |
| 5 | 🇧🇷 BR | 5939 |
| 6 | 🇩🇪 DE | 5797 |
| 7 | 🇮🇹 IT | 5785 |
| 8 | 🇨🇦 CA | 5659 |
| 9 | 🇯🇵 JP | 4928 |
| 10 | 🇬🇧 GB | 4589 |
| 11 | 🇫🇷 FR | 4295 |
| 12 | 🇨🇴 CO | 3734 |
| 13 | 🇲🇽 MX | 3224 |
| 14 | 🇬🇷 GR | 3065 |
| 15 | 🇳🇴 NO | 2989 |
| 16 | 🇨🇭 CH | 2747 |
| 17 | 🇲🇾 MY | 2353 |
| 18 | 🇹🇷 TR | 2097 |
| 19 | 🇿🇦 ZA | 1849 |
| 20 | 🇰🇷 KR | 1794 |
| 21 | 🇳🇿 NZ | 1794 |
| 22 | 🇹🇭 TH | 1778 |
| 23 | 🇵🇱 PL | 1768 |
| 24 | 🇵🇭 PH | 1584 |
| 25 | 🇬🇹 GT | 1550 |
| 26 | 🇲🇦 MA | 1193 |
| 27 | 🇲🇴 MO | 1134 |
| 28 | 🇳🇱 NL | 1060 |
| 29 | 🇲🇪 ME | 1043 |
| 30 | 🇭🇷 HR | 944 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2328 |
| 2 | Denver International Airport |  | US | 1829 |
| 3 | Tokyo International Airport |  | JP | 1631 |
| 4 | Indira Gandhi International Airport |  | IN | 1467 |
| 5 | Harry Reid International Airport |  | US | 1374 |
| 6 | Guaymaral Airport |  | CO | 1373 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1354 |
| 8 | Zurich Airport |  | CH | 1226 |
| 9 | Frankfurt am Main International Airport |  | DE | 1214 |
| 10 | La Aurora Airport |  | GT | 1192 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1161 |
| 12 | Macau International Airport |  | MO | 1134 |
| 13 | El Dorado International Airport |  | CO | 1132 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1081 |
| 15 | Chicago O'Hare International Airport |  | US | 1075 |
| 16 | Madrid Barajas International Airport |  | ES | 940 |
| 17 | Capua Airport |  | IT | 926 |
| 18 | Kuala Lumpur International Airport |  | MY | 922 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 918 |
| 20 | Salt Lake City International Airport |  | US | 915 |
| 21 | Charlotte/Douglas International Airport |  | US | 833 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 823 |
| 23 | Congonhas Airport |  | BR | 822 |
| 24 | Charles de Gaulle International Airport |  | FR | 816 |
| 25 | Bengaluru International Airport |  | IN | 813 |
| 26 | Malpensa International Airport |  | IT | 799 |
| 27 | Daniel K Inouye International Airport |  | US | 728 |
| 28 | Ninoy Aquino International Airport |  | PH | 727 |
| 29 | Tenerife Norte Airport |  | ES | 723 |
| 30 | Barcelona International Airport |  | ES | 706 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 700 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 698 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 698 |
| 34 | Amsterdam Airport Schiphol |  | NL | 654 |
| 35 | Don Mueang International Airport |  | TH | 650 |
| 36 | Vitoria/Foronda Airport |  | ES | 645 |
| 37 | Calgary International Airport |  | CA | 636 |
| 38 | Seattle-Tacoma International Airport |  | US | 621 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 619 |
| 40 | Netaji Subhash Chandra Bose International Airport |  | IN | 610 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 568 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 396 | 21m | 244 km | 1,667.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 288 | 24m | 225 km | 1,117.3 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 283 | 1h 7m | 706 km | 3,445.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 279 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 263 | 1h 25m | 910 km | 4,127.1 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 259 | 28m | 304 km | 1,357.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 250 | 1h 10m | 770 km | 3,321.1 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 221 | 19m | 165 km | 628.6 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 217 | 26m | 275 km | 1,028.3 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 208 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 162 | 20m | 99 km | 277.5 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 158 | 27m | 215 km | 585.2 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 158 | 22m | 55 km | 150.2 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 152 | 14m | 154 km | 402.7 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 150 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 149 | 27m | 152 km | 389.4 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 147 | 31m | 369 km | 935.7 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 145 | 44m | 452 km | 1,130.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 140 | 18m | 144 km | 348.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 131 | 1h 1m | 695 km | 1,570.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 26 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 129 | 44m | 241 km | 535.8 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 128 | 1h 43m | 1,423 km | 3,141.3 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 122 | 1h 18m | 961 km | 2,022.2 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| QFY41T | QFY | Cuatro Vientos Airport (LECU) | Casarrubios Del Monte Airport (LEMT) | 2026-06-11 10:23 UTC | 2026-06-11 10:51 UTC | 28m |
| EDC096R | EDC | Oxford (Kidlington) Airport (EGTK) | Guernsey Airport (EGJB) | 2026-06-11 10:10 UTC | 2026-06-11 10:44 UTC | 34m |
| N313CF |  | Dekalb-Peachtree Airport (KPDK) | Savannah/Hilton Head International Airport (KSAV) | 2026-06-11 10:04 UTC | 2026-06-11 10:40 UTC | 35m |
| NHZ31 | NHZ | Blackpool International Airport (EGNH) | RAF Woodvale (EGOW) | 2026-06-11 10:04 UTC | 2026-06-11 10:32 UTC | 28m |
| RJA525 | Royal Jordanian | Queen Alia International Airport (OJAI) | HL60 (HL60) | 2026-06-11 08:19 UTC | 2026-06-11 10:28 UTC | 2h 9m |
| WZZ8EU | Wizz Air | Barcelona International Airport (LEBL) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-06-11 07:45 UTC | 2026-06-11 10:08 UTC | 2h 22m |
| ZKIDU | ZKI | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-06-11 09:32 UTC | 2026-06-11 10:06 UTC | 33m |
| LHX9931 | LHX | Eleftherios Venizelos International Airport (LGAV) | Zemunik Airport (LDZD) | 2026-06-11 08:39 UTC | 2026-06-11 10:05 UTC | 1h 25m |
| FIN9VM | Finnair | Helsinki Vantaa Airport (EFHK) | Vaasa Airport (EFVA) | 2026-06-11 09:20 UTC | 2026-06-11 10:05 UTC | 44m |
| RYR8NQ | Ryanair | Bari / Palese International Airport (LIBD) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-06-11 08:34 UTC | 2026-06-11 10:01 UTC | 1h 27m |
| RYR59SQ | Ryanair | Palma De Mallorca Airport (LEPA) | Munster Osnabruck Airport (EDDG) | 2026-06-11 07:34 UTC | 2026-06-11 10:01 UTC | 2h 26m |
| EZY42CA | easyJet | Belfast International Airport (EGAA) | Liverpool John Lennon Airport (EGGP) | 2026-06-11 09:29 UTC | 2026-06-11 09:59 UTC | 29m |
| PHAFW | PHA | De Kooy Airport (EHKD) | Texel Airport (EHTX) | 2026-06-11 09:31 UTC | 2026-06-11 09:58 UTC | 26m |
| RYR2LC | Ryanair | Barcelona International Airport (LEBL) | Ifrane Airport (GMFI) | 2026-06-11 08:44 UTC | 2026-06-11 09:55 UTC | 1h 10m |
| RYR62PM | Ryanair | London Stansted Airport (EGSS) | Burg Feuerstein Airport (EDQE) | 2026-06-11 08:39 UTC | 2026-06-11 09:52 UTC | 1h 12m |
| SFJ85 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-06-11 08:34 UTC | 2026-06-11 09:51 UTC | 1h 17m |
| RYR354V | Ryanair | Torino / Caselle International Airport (LIMF) | L'Aquila / Preturo Airport (LIAP) | 2026-06-11 08:46 UTC | 2026-06-11 09:51 UTC | 1h 4m |
| SVF680 | SVF | Malmen Air Base (ESCF) | EPKI (EPKI) | 2026-06-11 07:33 UTC | 2026-06-11 09:51 UTC | 2h 17m |
| RYR84LH | Ryanair | Madrid Barajas International Airport (LEMD) | Luqa Airport (LMML) | 2026-06-11 07:33 UTC | 2026-06-11 09:50 UTC | 2h 17m |
| VOE3705 | VOE | Burgos Airport (LEBG) | Menorca Airport (LEMH) | 2026-06-11 08:54 UTC | 2026-06-11 09:50 UTC | 55m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
