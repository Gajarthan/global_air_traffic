# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_21:57:20_UTC-green)

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

**Latest saved flight:** 2026-06-08 21:57:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-08 21:57:20 UTC

- **106,643** saved flights
- **37,458** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **106,643** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,304,170.1 tonnes** estimated CO2 emissions
- **75,604,066 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4396 |
| 2 | SkyWest Airlines | 4014 |
| 3 | IndiGo | 2111 |
| 4 | EJA | 2056 |
| 5 | American Airlines | 1708 |
| 6 | Southwest Airlines | 1610 |
| 7 | ENY | 1337 |
| 8 | Delta Air Lines | 1272 |
| 9 | Lufthansa | 1218 |
| 10 | Vueling | 980 |
| 11 | LATAM Airlines | 943 |
| 12 | WIF | 934 |
| 13 | AXM | 910 |
| 14 | AZU | 866 |
| 15 | LXJ | 803 |
| 16 | Swiss International | 775 |
| 17 | All Nippon Airways | 741 |
| 18 | Alaska Airlines | 737 |
| 19 | QLK | 711 |
| 20 | easyJet | 692 |
| 21 | EJU | 680 |
| 22 | Cathay Pacific | 637 |
| 23 | AEE | 613 |
| 24 | VIV | 611 |
| 25 | Air France | 608 |
| 26 | United Airlines | 588 |
| 27 | MXY | 579 |
| 28 | CXK | 560 |
| 29 | Japan Airlines | 526 |
| 30 | AXB | 522 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 89727 |
| 2 | 🇪🇸 ES | 7328 |
| 3 | 🇮🇳 IN | 6661 |
| 4 | 🇦🇺 AU | 6395 |
| 5 | 🇧🇷 BR | 5857 |
| 6 | 🇩🇪 DE | 5720 |
| 7 | 🇮🇹 IT | 5714 |
| 8 | 🇨🇦 CA | 5565 |
| 9 | 🇯🇵 JP | 4874 |
| 10 | 🇬🇧 GB | 4526 |
| 11 | 🇫🇷 FR | 4238 |
| 12 | 🇨🇴 CO | 3667 |
| 13 | 🇲🇽 MX | 3198 |
| 14 | 🇬🇷 GR | 3031 |
| 15 | 🇳🇴 NO | 2955 |
| 16 | 🇨🇭 CH | 2723 |
| 17 | 🇲🇾 MY | 2336 |
| 18 | 🇹🇷 TR | 2063 |
| 19 | 🇿🇦 ZA | 1836 |
| 20 | 🇰🇷 KR | 1773 |
| 21 | 🇳🇿 NZ | 1772 |
| 22 | 🇹🇭 TH | 1759 |
| 23 | 🇵🇱 PL | 1744 |
| 24 | 🇵🇭 PH | 1567 |
| 25 | 🇬🇹 GT | 1541 |
| 26 | 🇲🇦 MA | 1178 |
| 27 | 🇲🇴 MO | 1112 |
| 28 | 🇳🇱 NL | 1047 |
| 29 | 🇲🇪 ME | 1024 |
| 30 | 🇭🇷 HR | 928 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2312 |
| 2 | Denver International Airport |  | US | 1816 |
| 3 | Tokyo International Airport |  | JP | 1613 |
| 4 | Indira Gandhi International Airport |  | IN | 1449 |
| 5 | Harry Reid International Airport |  | US | 1363 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1341 |
| 7 | Guaymaral Airport |  | CO | 1335 |
| 8 | Zurich Airport |  | CH | 1210 |
| 9 | Frankfurt am Main International Airport |  | DE | 1207 |
| 10 | La Aurora Airport |  | GT | 1186 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1155 |
| 12 | El Dorado International Airport |  | CO | 1119 |
| 13 | Macau International Airport |  | MO | 1112 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1074 |
| 15 | Chicago O'Hare International Airport |  | US | 1071 |
| 16 | Madrid Barajas International Airport |  | ES | 930 |
| 17 | Kuala Lumpur International Airport |  | MY | 915 |
| 18 | Salt Lake City International Airport |  | US | 911 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 910 |
| 20 | Capua Airport |  | IT | 910 |
| 21 | Charlotte/Douglas International Airport |  | US | 828 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 814 |
| 23 | Congonhas Airport |  | BR | 811 |
| 24 | Charles de Gaulle International Airport |  | FR | 810 |
| 25 | Malpensa International Airport |  | IT | 797 |
| 26 | Bengaluru International Airport |  | IN | 797 |
| 27 | Daniel K Inouye International Airport |  | US | 724 |
| 28 | Ninoy Aquino International Airport |  | PH | 718 |
| 29 | Tenerife Norte Airport |  | ES | 718 |
| 30 | Barcelona International Airport |  | ES | 699 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 691 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 689 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 689 |
| 34 | Amsterdam Airport Schiphol |  | NL | 647 |
| 35 | Don Mueang International Airport |  | TH | 643 |
| 36 | Vitoria/Foronda Airport |  | ES | 637 |
| 37 | Calgary International Airport |  | CA | 629 |
| 38 | Seattle-Tacoma International Airport |  | US | 620 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 614 |
| 40 | Netaji Subhash Chandra Bose International Airport |  | IN | 607 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 551 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 392 | 21m | 244 km | 1,650.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 284 | 24m | 225 km | 1,101.8 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 281 | 1h 7m | 706 km | 3,421.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 278 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 270 | 14m | 114 km | 529.6 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 260 | 1h 25m | 910 km | 4,080.0 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 259 | 28m | 304 km | 1,357.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 245 | 1h 10m | 770 km | 3,254.6 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 220 | 19m | 165 km | 625.8 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 213 | 26m | 275 km | 1,009.3 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 205 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 161 | 20m | 99 km | 275.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 155 | 27m | 215 km | 574.1 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 150 | 14m | 154 km | 397.4 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 148 | 27m | 152 km | 386.8 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 147 | 31m | 369 km | 935.7 t |
| 19 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 145 | 44m | 452 km | 1,130.1 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 144 | 13m | - | - |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 140 | 18m | 144 km | 348.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 131 | 1h 1m | 695 km | 1,570.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 125 | 1h 43m | 1,423 km | 3,067.7 t |
| 27 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 125 | 44m | 241 km | 519.2 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 120 | 1h 18m | 961 km | 1,989.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA044 | Cathay Pacific | Juhu Aerodrome (VAJJ) | Macau International Airport (VMMC) | 2026-06-08 17:03 UTC | 2026-06-08 21:57 UTC | 4h 54m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-06-08 10:58 UTC | 2026-06-08 21:53 UTC | 10h 55m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-06-08 17:32 UTC | 2026-06-08 21:50 UTC | 4h 17m |
| N237TH |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-06-08 21:30 UTC | 2026-06-08 21:50 UTC | 19m |
| CPA234 | Cathay Pacific | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-06-08 11:13 UTC | 2026-06-08 21:49 UTC | 10h 35m |
| TEX10 | TEX | RNZAF Base Ohakea (NZOH) | Wanganui Airport (NZWU) | 2026-06-08 21:13 UTC | 2026-06-08 21:48 UTC | 34m |
| N258JS |  | Santa Monica Municipal Airport (KSMO) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-06-08 20:51 UTC | 2026-06-08 21:47 UTC | 56m |
| N612TT |  | Santa Monica Municipal Airport (KSMO) | Santa Barbara Municipal Airport (KSBA) | 2026-06-08 21:08 UTC | 2026-06-08 21:45 UTC | 36m |
| N438H |  | Bradley International Airport (KBDL) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-08 20:09 UTC | 2026-06-08 21:37 UTC | 1h 27m |
| CFAFR000 | CFA | Kelowna Airport (CYLW) | Penticton Airport (CYYF) | 2026-06-08 21:15 UTC | 2026-06-08 21:29 UTC | 14m |
| N6FE |  | Dallas Love Field (KDAL) | Austin-Bergstrom International Airport (KAUS) | 2026-06-08 20:49 UTC | 2026-06-08 21:23 UTC | 33m |
| N107UV |  | Provo Municipal Airport (KPVU) | UT99 (UT99) | 2026-06-08 21:06 UTC | 2026-06-08 21:19 UTC | 13m |
| N705BH |  | Kodiak Municipal Airport (PAKD) | Kodiak Municipal Airport (PAKD) | 2026-06-08 21:16 UTC | 2026-06-08 21:19 UTC | 2m |
| SWA297 | Southwest Airlines | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | Goosefair Airport (ME45) | 2026-06-08 20:18 UTC | 2026-06-08 21:18 UTC | 59m |
| CYO696 | CYO | Tampa International Airport (KTPA) | Pecos Municipal Airport (KPEQ) | 2026-06-08 18:17 UTC | 2026-06-08 21:16 UTC | 2h 58m |
| N529KG |  | Manchester Boston Regional Airport (KMHT) | 1MI8 (1MI8) | 2026-06-08 19:58 UTC | 2026-06-08 21:15 UTC | 1h 17m |
| N8138G |  | Pippen-York Ranch Airport (TX41) | Little Buttes Antique Airfield (1CL1) | 2026-06-08 13:31 UTC | 2026-06-08 21:14 UTC | 7h 42m |
| PVL8481 | PVL | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Buctouche Airport (CDT5) | 2026-06-08 16:33 UTC | 2026-06-08 21:08 UTC | 4h 35m |
| EJA963 | EJA | Los Angeles International Airport (KLAX) | Dorton Airport (03MO) | 2026-06-08 18:20 UTC | 2026-06-08 21:05 UTC | 2h 44m |
| AL4 |  | Sydney Bankstown Airport (YSBK) | Greenthorpe Airport (YGTP) | 2026-06-08 20:27 UTC | 2026-06-08 21:04 UTC | 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
