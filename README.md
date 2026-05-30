# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_22:20:28_UTC-green)

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

**Latest saved flight:** 2026-05-30 22:20:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-30 22:20:28 UTC

- **98,089** saved flights
- **34,450** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **98,089** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,201,236.0 tonnes** estimated CO2 emissions
- **69,636,872 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4115 |
| 2 | SkyWest Airlines | 3667 |
| 3 | IndiGo | 2010 |
| 4 | EJA | 1859 |
| 5 | American Airlines | 1489 |
| 6 | Southwest Airlines | 1425 |
| 7 | ENY | 1205 |
| 8 | Lufthansa | 1172 |
| 9 | Delta Air Lines | 1077 |
| 10 | Vueling | 928 |
| 11 | LATAM Airlines | 877 |
| 12 | WIF | 866 |
| 13 | AXM | 854 |
| 14 | AZU | 797 |
| 15 | LXJ | 746 |
| 16 | Swiss International | 726 |
| 17 | All Nippon Airways | 710 |
| 18 | Alaska Airlines | 677 |
| 19 | QLK | 669 |
| 20 | easyJet | 645 |
| 21 | EJU | 623 |
| 22 | Cathay Pacific | 591 |
| 23 | AEE | 587 |
| 24 | VIV | 576 |
| 25 | Air France | 574 |
| 26 | CXK | 528 |
| 27 | MXY | 522 |
| 28 | Japan Airlines | 497 |
| 29 | AXB | 492 |
| 30 | GLO | 467 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 81358 |
| 2 | 🇪🇸 ES | 6874 |
| 3 | 🇮🇳 IN | 6350 |
| 4 | 🇦🇺 AU | 5930 |
| 5 | 🇧🇷 BR | 5409 |
| 6 | 🇩🇪 DE | 5393 |
| 7 | 🇮🇹 IT | 5294 |
| 8 | 🇨🇦 CA | 4987 |
| 9 | 🇯🇵 JP | 4604 |
| 10 | 🇬🇧 GB | 4211 |
| 11 | 🇫🇷 FR | 3963 |
| 12 | 🇨🇴 CO | 3440 |
| 13 | 🇲🇽 MX | 3007 |
| 14 | 🇬🇷 GR | 2841 |
| 15 | 🇳🇴 NO | 2746 |
| 16 | 🇨🇭 CH | 2568 |
| 17 | 🇲🇾 MY | 2172 |
| 18 | 🇹🇷 TR | 1849 |
| 19 | 🇿🇦 ZA | 1737 |
| 20 | 🇳🇿 NZ | 1651 |
| 21 | 🇹🇭 TH | 1640 |
| 22 | 🇵🇱 PL | 1594 |
| 23 | 🇰🇷 KR | 1590 |
| 24 | 🇬🇹 GT | 1469 |
| 25 | 🇵🇭 PH | 1458 |
| 26 | 🇲🇦 MA | 1110 |
| 27 | 🇲🇴 MO | 1046 |
| 28 | 🇳🇱 NL | 992 |
| 29 | 🇲🇪 ME | 956 |
| 30 | 🇭🇷 HR | 881 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2127 |
| 2 | Denver International Airport |  | US | 1664 |
| 3 | Tokyo International Airport |  | JP | 1525 |
| 4 | Indira Gandhi International Airport |  | IN | 1378 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1288 |
| 6 | Harry Reid International Airport |  | US | 1260 |
| 7 | Guaymaral Airport |  | CO | 1238 |
| 8 | Frankfurt am Main International Airport |  | DE | 1177 |
| 9 | Zurich Airport |  | CH | 1141 |
| 10 | La Aurora Airport |  | GT | 1129 |
| 11 | El Dorado International Airport |  | CO | 1060 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1054 |
| 13 | Macau International Airport |  | MO | 1046 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 989 |
| 15 | Chicago O'Hare International Airport |  | US | 941 |
| 16 | Madrid Barajas International Airport |  | ES | 867 |
| 17 | Kuala Lumpur International Airport |  | MY | 858 |
| 18 | Salt Lake City International Airport |  | US | 829 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 822 |
| 20 | Capua Airport |  | IT | 819 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 769 |
| 22 | Malpensa International Airport |  | IT | 764 |
| 23 | Bengaluru International Airport |  | IN | 761 |
| 24 | Charles de Gaulle International Airport |  | FR | 760 |
| 25 | Charlotte/Douglas International Airport |  | US | 750 |
| 26 | Congonhas Airport |  | BR | 748 |
| 27 | Daniel K Inouye International Airport |  | US | 690 |
| 28 | Tenerife Norte Airport |  | ES | 688 |
| 29 | Ninoy Aquino International Airport |  | PH | 665 |
| 30 | Barcelona International Airport |  | ES | 658 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 652 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 630 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 627 |
| 34 | Amsterdam Airport Schiphol |  | NL | 610 |
| 35 | Vitoria/Foronda Airport |  | ES | 606 |
| 36 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 37 | Don Mueang International Airport |  | TH | 601 |
| 38 | Calgary International Airport |  | CA | 580 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 572 |
| 40 | O. R. Tambo International Airport |  | ZA | 554 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 512 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 360 | 21m | 244 km | 1,515.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 265 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 263 | 24m | 225 km | 1,020.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 251 | 14m | 114 km | 492.3 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 243 | 1h 26m | 910 km | 3,813.2 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 242 | 28m | 304 km | 1,268.6 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 223 | 1h 10m | 770 km | 2,962.4 t |
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
| N584SF |  | Denton Enterprise Airport (KDTO) | Jim Sears Airport (3TA7) | 2026-05-30 21:40 UTC | 2026-05-30 22:20 UTC | 40m |
| CPA395 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-05-30 14:15 UTC | 2026-05-30 21:53 UTC | 7h 38m |
| N786FA |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-05-30 20:55 UTC | 2026-05-30 21:38 UTC | 43m |
| FIN6AK | Finnair | Chania International Airport (LGSA) | Pskov Airport (ULOO) | 2026-05-30 18:26 UTC | 2026-05-30 21:34 UTC | 3h 7m |
| N208JP |  | Maple Hurst Farms Airport (LL74) | 75IS (75IS) | 2026-05-30 21:19 UTC | 2026-05-30 21:32 UTC | 12m |
| N80616 |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-05-30 20:50 UTC | 2026-05-30 21:30 UTC | 40m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-05-30 21:13 UTC | 2026-05-30 21:27 UTC | 14m |
| N225AV |  | Muzquiz New Airport (MM42) | Quetzalcoatl International Airport (MMNL) | 2026-05-30 20:40 UTC | 2026-05-30 21:27 UTC | 46m |
| CXK357 | CXK | Sugar Land Regional Airport (KSGR) | Fayette Regional Air Center Airport (K3T5) | 2026-05-30 20:45 UTC | 2026-05-30 21:27 UTC | 41m |
| LVN | LVN | Shute Harbour/Whitsunday Airport (YSHR) | Whitsunday Island Airport (YWHI) | 2026-05-30 21:15 UTC | 2026-05-30 21:25 UTC | 10m |
| N577GA |  | Reykjavik Airport (BIRK) | BIPA (BIPA) | 2026-05-30 21:07 UTC | 2026-05-30 21:24 UTC | 16m |
| N786MM |  | Los Angeles International Airport (KLAX) | Harry Reid International Airport (KLAS) | 2026-05-30 20:38 UTC | 2026-05-30 21:23 UTC | 45m |
| N88765 |  | Helio Airport (2AK7) | Talkeetna Airport (PATK) | 2026-05-30 20:59 UTC | 2026-05-30 21:19 UTC | 20m |
| N121BZ |  | John Wayne/Orange County Airport (KSNA) | Benson Municipal/Paul Kerchum Field (KE95) | 2026-05-30 20:22 UTC | 2026-05-30 21:19 UTC | 56m |
| N194W |  | Miami International Airport (KMIA) | Witham Field (KSUA) | 2026-05-30 20:51 UTC | 2026-05-30 21:17 UTC | 25m |
| FFAB123 | FFA | Rota Naval Station Airport (LERT) | Rota Naval Station Airport (LERT) | 2026-05-30 20:48 UTC | 2026-05-30 21:15 UTC | 27m |
| RYR418Z | Ryanair | Valencia Airport (LEVC) | Ibiza Airport (LEIB) | 2026-05-30 20:46 UTC | 2026-05-30 21:14 UTC | 28m |
| N243EA |  | Glendale Regional Airport (KGEU) | Montezuma Airport (19AZ) | 2026-05-30 20:14 UTC | 2026-05-30 21:08 UTC | 54m |
| N305RP |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-05-30 20:44 UTC | 2026-05-30 21:08 UTC | 24m |
| VTE3694 | VTE | Dallas-Fort Worth International Airport (KDFW) | Vivian Airport (K3F4) | 2026-05-30 20:35 UTC | 2026-05-30 21:03 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
