# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--24_18:10:17_UTC-green)

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

**Latest saved flight:** 2026-05-24 18:10:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-24 18:10:17 UTC

- **93,987** saved flights
- **33,194** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **93,987** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,156,320.1 tonnes** estimated CO2 emissions
- **67,033,052 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3971 |
| 2 | SkyWest Airlines | 3479 |
| 3 | IndiGo | 1952 |
| 4 | EJA | 1774 |
| 5 | American Airlines | 1428 |
| 6 | Southwest Airlines | 1362 |
| 7 | ENY | 1162 |
| 8 | Lufthansa | 1135 |
| 9 | Delta Air Lines | 1028 |
| 10 | Vueling | 892 |
| 11 | LATAM Airlines | 844 |
| 12 | AXM | 835 |
| 13 | WIF | 817 |
| 14 | AZU | 749 |
| 15 | LXJ | 708 |
| 16 | Swiss International | 706 |
| 17 | All Nippon Airways | 698 |
| 18 | Alaska Airlines | 653 |
| 19 | QLK | 650 |
| 20 | easyJet | 613 |
| 21 | EJU | 606 |
| 22 | Cathay Pacific | 582 |
| 23 | AEE | 567 |
| 24 | Air France | 557 |
| 25 | VIV | 556 |
| 26 | CXK | 502 |
| 27 | MXY | 496 |
| 28 | Japan Airlines | 489 |
| 29 | AXB | 479 |
| 30 | AIQ | 455 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 77586 |
| 2 | 🇪🇸 ES | 6593 |
| 3 | 🇮🇳 IN | 6166 |
| 4 | 🇦🇺 AU | 5748 |
| 5 | 🇩🇪 DE | 5182 |
| 6 | 🇧🇷 BR | 5158 |
| 7 | 🇮🇹 IT | 5101 |
| 8 | 🇨🇦 CA | 4758 |
| 9 | 🇯🇵 JP | 4524 |
| 10 | 🇬🇧 GB | 4013 |
| 11 | 🇫🇷 FR | 3800 |
| 12 | 🇨🇴 CO | 3262 |
| 13 | 🇲🇽 MX | 2886 |
| 14 | 🇬🇷 GR | 2703 |
| 15 | 🇳🇴 NO | 2610 |
| 16 | 🇨🇭 CH | 2476 |
| 17 | 🇲🇾 MY | 2110 |
| 18 | 🇹🇷 TR | 1737 |
| 19 | 🇿🇦 ZA | 1701 |
| 20 | 🇹🇭 TH | 1595 |
| 21 | 🇳🇿 NZ | 1594 |
| 22 | 🇵🇱 PL | 1547 |
| 23 | 🇰🇷 KR | 1515 |
| 24 | 🇵🇭 PH | 1420 |
| 25 | 🇬🇹 GT | 1413 |
| 26 | 🇲🇦 MA | 1078 |
| 27 | 🇲🇴 MO | 1038 |
| 28 | 🇳🇱 NL | 944 |
| 29 | 🇲🇪 ME | 936 |
| 30 | 🇭🇷 HR | 856 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2036 |
| 2 | Denver International Airport |  | US | 1580 |
| 3 | Tokyo International Airport |  | JP | 1505 |
| 4 | Indira Gandhi International Airport |  | IN | 1342 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1247 |
| 6 | Harry Reid International Airport |  | US | 1206 |
| 7 | Frankfurt am Main International Airport |  | DE | 1150 |
| 8 | Guaymaral Airport |  | CO | 1136 |
| 9 | Zurich Airport |  | CH | 1101 |
| 10 | La Aurora Airport |  | GT | 1080 |
| 11 | Macau International Airport |  | MO | 1038 |
| 12 | El Dorado International Airport |  | CO | 1026 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1024 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 937 |
| 15 | Chicago O'Hare International Airport |  | US | 895 |
| 16 | Madrid Barajas International Airport |  | ES | 840 |
| 17 | Kuala Lumpur International Airport |  | MY | 837 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 792 |
| 19 | Salt Lake City International Airport |  | US | 788 |
| 20 | Capua Airport |  | IT | 779 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 747 |
| 22 | Malpensa International Airport |  | IT | 743 |
| 23 | Bengaluru International Airport |  | IN | 739 |
| 24 | Charles de Gaulle International Airport |  | FR | 738 |
| 25 | Charlotte/Douglas International Airport |  | US | 716 |
| 26 | Congonhas Airport |  | BR | 714 |
| 27 | Daniel K Inouye International Airport |  | US | 674 |
| 28 | Tenerife Norte Airport |  | ES | 667 |
| 29 | Ninoy Aquino International Airport |  | PH | 649 |
| 30 | Barcelona International Airport |  | ES | 630 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 629 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 612 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 602 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 599 |
| 35 | Vitoria/Foronda Airport |  | ES | 586 |
| 36 | Don Mueang International Airport |  | TH | 584 |
| 37 | Amsterdam Airport Schiphol |  | NL | 581 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 567 |
| 39 | Calgary International Airport |  | CA | 559 |
| 40 | O. R. Tambo International Airport |  | ZA | 539 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 466 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 345 | 21m | 244 km | 1,452.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 253 | 24m | 225 km | 981.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 249 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 242 | 14m | 114 km | 474.6 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 241 | 1h 26m | 910 km | 3,781.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 237 | 28m | 304 km | 1,242.4 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 216 | 1h 10m | 770 km | 2,869.4 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 205 | 19m | 165 km | 583.1 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 189 | 26m | 275 km | 895.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 141 | 44m | 452 km | 1,098.9 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 140 | 27m | 215 km | 518.5 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 139 | 14m | 154 km | 368.3 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 136 | 22m | 55 km | 129.3 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 135 | 27m | 152 km | 352.8 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 129 | 20m | 250 km | 557.2 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 121 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 120 | 1h 1m | 695 km | 1,438.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 120 | 18m | 144 km | 298.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 116 | 1h 40m | 1,156 km | 2,314.2 t |
| 26 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 112 | 1h 18m | 961 km | 1,856.5 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 111 | 1h 52m | 1,304 km | 2,497.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| 504HW |  | Riego Flight Strip (38CL) | Riego Flight Strip (38CL) | 2026-05-24 17:52 UTC | 2026-05-24 18:10 UTC | 17m |
| N523DL |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-05-24 17:43 UTC | 2026-05-24 18:03 UTC | 20m |
| N818LW |  | Henderson Executive Airport (KHND) | Twentynine Palms Airport (KTNP) | 2026-05-24 17:39 UTC | 2026-05-24 18:02 UTC | 23m |
| N739BZ |  | Cheyenne Regional/Jerry Olson Field (KCYS) | Laramie Regional Airport (KLAR) | 2026-05-24 17:34 UTC | 2026-05-24 17:57 UTC | 23m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-05-24 17:41 UTC | 2026-05-24 17:56 UTC | 15m |
| N141SM |  | Nashville International Airport (KBNA) | SC60 (SC60) | 2026-05-24 16:34 UTC | 2026-05-24 17:55 UTC | 1h 20m |
| EPI394 | EPI | North Texas Regional/Perrin Field (KGYI) | Gainesville Municipal Airport (KGLE) | 2026-05-24 16:58 UTC | 2026-05-24 17:54 UTC | 56m |
|  |  | Murfreesboro Municipal Airport (KMBT) | Rachel's Landing Airport (8TN6) | 2026-05-24 17:47 UTC | 2026-05-24 17:48 UTC | 1m |
| VAR476 | VAR | Needles Airport (KEED) | Lake Havasu City Airport (KHII) | 2026-05-24 17:30 UTC | 2026-05-24 17:46 UTC | 15m |
| RYR2ZM | Ryanair | Copernicus Wrocław Airport (EPWR) | Palermo / Bocca Di Falco Airport (LICP) | 2026-05-24 15:53 UTC | 2026-05-24 17:43 UTC | 1h 49m |
| N231NH |  | Pope Valley Airport (05CL) | Yolo County Airport (KDWA) | 2026-05-24 17:27 UTC | 2026-05-24 17:43 UTC | 15m |
| VOI760 | VOI | Licenciado Benito Juarez International Airport (MMMX) | Denver International Airport (KDEN) | 2026-05-24 14:38 UTC | 2026-05-24 17:41 UTC | 3h 3m |
| RYR56GA | Ryanair | Ciampino Airport (LIRA) | Ohrid St. Paul the Apostle Airport (LWOH) | 2026-05-24 16:47 UTC | 2026-05-24 17:37 UTC | 50m |
| N129NB |  | Skwentna Airport (PASW) | Talaheim Airport (1AK8) | 2026-05-24 17:18 UTC | 2026-05-24 17:36 UTC | 18m |
| AFR1082 | Air France | Charles de Gaulle International Airport (LFPG) | Václav Havel Airport (LKPR) | 2026-05-24 16:08 UTC | 2026-05-24 17:32 UTC | 1h 23m |
| XE1180 |  | Harry Reid International Airport (KLAS) | Santa Monica Municipal Airport (KSMO) | 2026-05-24 16:33 UTC | 2026-05-24 17:32 UTC | 59m |
| VLG3BL | Vueling | Paris-Orly Airport (LFPO) | San Sebastian Airport (LESO) | 2026-05-24 16:33 UTC | 2026-05-24 17:31 UTC | 58m |
| ENY3384 | ENY | Dallas-Fort Worth International Airport (KDFW) | 5TA4 (5TA4) | 2026-05-24 16:52 UTC | 2026-05-24 17:29 UTC | 37m |
| IGO543J | IndiGo | Bengaluru International Airport (VOBL) | Salem Airport (VOSM) | 2026-05-24 12:08 UTC | 2026-05-24 17:29 UTC | 5h 20m |
| RYR8N | Ryanair | Copernicus Wrocław Airport (EPWR) | Grudziądz-Lisie Kąty Airport  (EPGI) | 2026-05-24 17:01 UTC | 2026-05-24 17:29 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
