# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--10_04:24:40_UTC-green)

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

**Latest saved flight:** 2026-06-10 04:24:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-10 04:24:40 UTC

- **107,210** saved flights
- **37,603** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **107,210** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,310,673.9 tonnes** estimated CO2 emissions
- **75,981,095 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4405 |
| 2 | SkyWest Airlines | 4031 |
| 3 | IndiGo | 2126 |
| 4 | EJA | 2069 |
| 5 | American Airlines | 1711 |
| 6 | Southwest Airlines | 1616 |
| 7 | ENY | 1341 |
| 8 | Delta Air Lines | 1274 |
| 9 | Lufthansa | 1223 |
| 10 | Vueling | 983 |
| 11 | LATAM Airlines | 952 |
| 12 | WIF | 939 |
| 13 | AXM | 912 |
| 14 | AZU | 874 |
| 15 | LXJ | 808 |
| 16 | Swiss International | 779 |
| 17 | All Nippon Airways | 745 |
| 18 | Alaska Airlines | 739 |
| 19 | QLK | 714 |
| 20 | easyJet | 692 |
| 21 | EJU | 682 |
| 22 | Cathay Pacific | 643 |
| 23 | AEE | 613 |
| 24 | VIV | 613 |
| 25 | Air France | 608 |
| 26 | United Airlines | 594 |
| 27 | MXY | 579 |
| 28 | CXK | 565 |
| 29 | Japan Airlines | 528 |
| 30 | AXB | 527 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 90256 |
| 2 | 🇪🇸 ES | 7354 |
| 3 | 🇮🇳 IN | 6702 |
| 4 | 🇦🇺 AU | 6428 |
| 5 | 🇧🇷 BR | 5909 |
| 6 | 🇩🇪 DE | 5745 |
| 7 | 🇮🇹 IT | 5741 |
| 8 | 🇨🇦 CA | 5610 |
| 9 | 🇯🇵 JP | 4888 |
| 10 | 🇬🇧 GB | 4550 |
| 11 | 🇫🇷 FR | 4259 |
| 12 | 🇨🇴 CO | 3715 |
| 13 | 🇲🇽 MX | 3213 |
| 14 | 🇬🇷 GR | 3045 |
| 15 | 🇳🇴 NO | 2964 |
| 16 | 🇨🇭 CH | 2734 |
| 17 | 🇲🇾 MY | 2340 |
| 18 | 🇹🇷 TR | 2074 |
| 19 | 🇿🇦 ZA | 1840 |
| 20 | 🇳🇿 NZ | 1783 |
| 21 | 🇰🇷 KR | 1781 |
| 22 | 🇹🇭 TH | 1761 |
| 23 | 🇵🇱 PL | 1746 |
| 24 | 🇵🇭 PH | 1570 |
| 25 | 🇬🇹 GT | 1550 |
| 26 | 🇲🇦 MA | 1182 |
| 27 | 🇲🇴 MO | 1120 |
| 28 | 🇳🇱 NL | 1049 |
| 29 | 🇲🇪 ME | 1026 |
| 30 | 🇭🇷 HR | 929 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2319 |
| 2 | Denver International Airport |  | US | 1823 |
| 3 | Tokyo International Airport |  | JP | 1618 |
| 4 | Indira Gandhi International Airport |  | IN | 1456 |
| 5 | Harry Reid International Airport |  | US | 1367 |
| 6 | Guaymaral Airport |  | CO | 1360 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1345 |
| 8 | Zurich Airport |  | CH | 1216 |
| 9 | Frankfurt am Main International Airport |  | DE | 1210 |
| 10 | La Aurora Airport |  | GT | 1192 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1159 |
| 12 | El Dorado International Airport |  | CO | 1129 |
| 13 | Macau International Airport |  | MO | 1120 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1079 |
| 15 | Chicago O'Hare International Airport |  | US | 1072 |
| 16 | Madrid Barajas International Airport |  | ES | 932 |
| 17 | Kuala Lumpur International Airport |  | MY | 917 |
| 18 | Capua Airport |  | IT | 916 |
| 19 | Salt Lake City International Airport |  | US | 913 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 913 |
| 21 | Charlotte/Douglas International Airport |  | US | 832 |
| 22 | Congonhas Airport |  | BR | 816 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 815 |
| 24 | Charles de Gaulle International Airport |  | FR | 812 |
| 25 | Bengaluru International Airport |  | IN | 808 |
| 26 | Malpensa International Airport |  | IT | 797 |
| 27 | Daniel K Inouye International Airport |  | US | 727 |
| 28 | Ninoy Aquino International Airport |  | PH | 720 |
| 29 | Tenerife Norte Airport |  | ES | 718 |
| 30 | Barcelona International Airport |  | ES | 701 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 697 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 697 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 697 |
| 34 | Amsterdam Airport Schiphol |  | NL | 649 |
| 35 | Don Mueang International Airport |  | TH | 644 |
| 36 | Vitoria/Foronda Airport |  | ES | 640 |
| 37 | Calgary International Airport |  | CA | 632 |
| 38 | Seattle-Tacoma International Airport |  | US | 621 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 617 |
| 40 | Netaji Subhash Chandra Bose International Airport |  | IN | 609 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 563 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 395 | 21m | 244 km | 1,663.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 285 | 24m | 225 km | 1,105.7 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 282 | 1h 7m | 706 km | 3,433.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 279 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 261 | 1h 25m | 910 km | 4,095.7 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 259 | 28m | 304 km | 1,357.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 246 | 1h 10m | 770 km | 3,267.9 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 220 | 19m | 165 km | 625.8 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 214 | 26m | 275 km | 1,014.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 205 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 162 | 20m | 99 km | 277.5 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 157 | 27m | 215 km | 581.5 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 150 | 14m | 154 km | 397.4 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 149 | 27m | 152 km | 389.4 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 147 | 31m | 369 km | 935.7 t |
| 19 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 145 | 44m | 452 km | 1,130.1 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 145 | 13m | - | - |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 140 | 18m | 144 km | 348.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 131 | 1h 1m | 695 km | 1,570.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 126 | 1h 43m | 1,423 km | 3,092.2 t |
| 27 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 126 | 44m | 241 km | 523.4 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 121 | 1h 18m | 961 km | 2,005.6 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9965P |  | Corpus Christi International Airport (KCRP) | Austin-Bergstrom International Airport (KAUS) | 2026-06-10 02:59 UTC | 2026-06-10 04:24 UTC | 1h 25m |
| EJA542 | EJA | Austin-Bergstrom International Airport (KAUS) | Henderson Executive Airport (KHND) | 2026-06-10 01:42 UTC | 2026-06-10 04:22 UTC | 2h 39m |
| N88765 |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-10 04:02 UTC | 2026-06-10 04:22 UTC | 19m |
| HPJ | HPJ | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-06-10 03:52 UTC | 2026-06-10 04:19 UTC | 27m |
| PKAR650 | PKA | Murray Field (YMUL) | Murray Field (YMUL) | 2026-06-10 04:10 UTC | 2026-06-10 04:11 UTC | 0m |
| N3939X |  | City Of Colorado Springs Municipal Airport (KCOS) | High Plains Airport Airport (CD15) | 2026-06-10 03:45 UTC | 2026-06-10 04:10 UTC | 24m |
| RDHK710 | RDH | Langley Afb Airport (KLFI) | Norfolk Ns (Chambers Field) Airport (KNGU) | 2026-06-10 03:57 UTC | 2026-06-10 04:07 UTC | 10m |
| BCS5959 | BCS | Leipzig Halle Airport (EDDP) | Pila Airport (EPPI) | 2026-06-10 03:30 UTC | 2026-06-10 04:01 UTC | 30m |
| MNB203 | MNB | Istanbul Airport (LTFM) | Macau International Airport (VMMC) | 2026-06-09 09:20 UTC | 2026-06-10 03:59 UTC | 18h 39m |
| N539SH |  | Gold King Creek Airport (PAAN) | Gold King Creek Airport (PAAN) | 2026-06-10 03:45 UTC | 2026-06-10 03:53 UTC | 8m |
| UNV | UNV | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-06-10 02:47 UTC | 2026-06-10 03:47 UTC | 1h 0m |
| SQS234 | SQS | Batujajar Airport (WI1B) | Margahayu Airport (WIAK) | 2026-06-10 03:15 UTC | 2026-06-10 03:45 UTC | 29m |
| FD247 |  | Sydney Bankstown Airport (YSBK) | Wellington Airport (YWEL) | 2026-06-10 03:03 UTC | 2026-06-10 03:40 UTC | 37m |
| N496AC |  | Salzburg Airport (LOWS) | Mc Elroy Airfield (K20V) | 2026-06-09 17:09 UTC | 2026-06-10 03:37 UTC | 10h 27m |
| KFN | KFN | Melbourne Moorabbin Airport (YMMB) | Warrnambool Airport (YWBL) | 2026-06-10 01:47 UTC | 2026-06-10 03:35 UTC | 1h 47m |
| N410W |  | Central Il Regional/Bloomington-Normal Airport (KBMI) | Frasca Field (KC16) | 2026-06-10 03:11 UTC | 2026-06-10 03:34 UTC | 23m |
| N21TQ |  | Lincoln Airport (KLNK) | Cherokee County Regional Airport (KCKP) | 2026-06-10 03:11 UTC | 2026-06-10 03:34 UTC | 22m |
| ASA1092 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-06-10 03:13 UTC | 2026-06-10 03:34 UTC | 20m |
| AIC1DJ | Air India | Indira Gandhi International Airport (VIDP) | VIBN (VIBN) | 2026-06-10 02:39 UTC | 2026-06-10 03:31 UTC | 52m |
| GUG702 | GUG | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-06-10 03:19 UTC | 2026-06-10 03:31 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
