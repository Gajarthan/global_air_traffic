# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_17:53:43_UTC-green)

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

**Latest saved flight:** 2026-06-08 17:53:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-08 17:53:43 UTC

- **106,291** saved flights
- **37,349** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **106,291** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,299,780.1 tonnes** estimated CO2 emissions
- **75,349,570 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4386 |
| 2 | SkyWest Airlines | 3994 |
| 3 | IndiGo | 2111 |
| 4 | EJA | 2038 |
| 5 | American Airlines | 1700 |
| 6 | Southwest Airlines | 1602 |
| 7 | ENY | 1332 |
| 8 | Delta Air Lines | 1263 |
| 9 | Lufthansa | 1217 |
| 10 | Vueling | 977 |
| 11 | LATAM Airlines | 941 |
| 12 | WIF | 930 |
| 13 | AXM | 910 |
| 14 | AZU | 861 |
| 15 | LXJ | 801 |
| 16 | Swiss International | 775 |
| 17 | All Nippon Airways | 741 |
| 18 | Alaska Airlines | 733 |
| 19 | QLK | 710 |
| 20 | easyJet | 689 |
| 21 | EJU | 680 |
| 22 | Cathay Pacific | 633 |
| 23 | AEE | 612 |
| 24 | Air France | 608 |
| 25 | VIV | 607 |
| 26 | United Airlines | 587 |
| 27 | MXY | 578 |
| 28 | CXK | 560 |
| 29 | Japan Airlines | 526 |
| 30 | AXB | 522 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 89322 |
| 2 | 🇪🇸 ES | 7314 |
| 3 | 🇮🇳 IN | 6659 |
| 4 | 🇦🇺 AU | 6389 |
| 5 | 🇧🇷 BR | 5829 |
| 6 | 🇩🇪 DE | 5716 |
| 7 | 🇮🇹 IT | 5705 |
| 8 | 🇨🇦 CA | 5531 |
| 9 | 🇯🇵 JP | 4874 |
| 10 | 🇬🇧 GB | 4505 |
| 11 | 🇫🇷 FR | 4230 |
| 12 | 🇨🇴 CO | 3655 |
| 13 | 🇲🇽 MX | 3175 |
| 14 | 🇬🇷 GR | 3020 |
| 15 | 🇳🇴 NO | 2945 |
| 16 | 🇨🇭 CH | 2722 |
| 17 | 🇲🇾 MY | 2336 |
| 18 | 🇹🇷 TR | 2051 |
| 19 | 🇿🇦 ZA | 1836 |
| 20 | 🇰🇷 KR | 1773 |
| 21 | 🇳🇿 NZ | 1766 |
| 22 | 🇹🇭 TH | 1759 |
| 23 | 🇵🇱 PL | 1738 |
| 24 | 🇵🇭 PH | 1567 |
| 25 | 🇬🇹 GT | 1533 |
| 26 | 🇲🇦 MA | 1175 |
| 27 | 🇲🇴 MO | 1108 |
| 28 | 🇳🇱 NL | 1045 |
| 29 | 🇲🇪 ME | 1023 |
| 30 | 🇭🇷 HR | 927 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2303 |
| 2 | Denver International Airport |  | US | 1810 |
| 3 | Tokyo International Airport |  | JP | 1613 |
| 4 | Indira Gandhi International Airport |  | IN | 1448 |
| 5 | Harry Reid International Airport |  | US | 1356 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1338 |
| 7 | Guaymaral Airport |  | CO | 1334 |
| 8 | Zurich Airport |  | CH | 1209 |
| 9 | Frankfurt am Main International Airport |  | DE | 1205 |
| 10 | La Aurora Airport |  | GT | 1180 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1149 |
| 12 | El Dorado International Airport |  | CO | 1113 |
| 13 | Macau International Airport |  | MO | 1108 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1069 |
| 15 | Chicago O'Hare International Airport |  | US | 1068 |
| 16 | Madrid Barajas International Airport |  | ES | 929 |
| 17 | Kuala Lumpur International Airport |  | MY | 915 |
| 18 | Salt Lake City International Airport |  | US | 910 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 909 |
| 20 | Capua Airport |  | IT | 907 |
| 21 | Charlotte/Douglas International Airport |  | US | 825 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 814 |
| 23 | Charles de Gaulle International Airport |  | FR | 808 |
| 24 | Congonhas Airport |  | BR | 806 |
| 25 | Bengaluru International Airport |  | IN | 797 |
| 26 | Malpensa International Airport |  | IT | 796 |
| 27 | Daniel K Inouye International Airport |  | US | 722 |
| 28 | Ninoy Aquino International Airport |  | PH | 718 |
| 29 | Tenerife Norte Airport |  | ES | 718 |
| 30 | Barcelona International Airport |  | ES | 698 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 687 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 686 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 683 |
| 34 | Amsterdam Airport Schiphol |  | NL | 647 |
| 35 | Don Mueang International Airport |  | TH | 643 |
| 36 | Vitoria/Foronda Airport |  | ES | 636 |
| 37 | Calgary International Airport |  | CA | 626 |
| 38 | Seattle-Tacoma International Airport |  | US | 616 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 609 |
| 40 | Netaji Subhash Chandra Bose International Airport |  | IN | 607 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 551 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 390 | 21m | 244 km | 1,642.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 284 | 24m | 225 km | 1,101.8 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 281 | 1h 7m | 706 km | 3,421.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 276 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 268 | 14m | 114 km | 525.6 t |
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
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 143 | 13m | - | - |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 139 | 18m | 144 km | 345.8 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 130 | 1h 1m | 695 km | 1,558.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 125 | 1h 43m | 1,423 km | 3,067.7 t |
| 27 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 124 | 44m | 241 km | 515.1 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 119 | 1h 18m | 961 km | 1,972.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N475LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-06-08 17:05 UTC | 2026-06-08 17:53 UTC | 48m |
| SWEEP11 | SWE | Lewis Private Airport (4TE2) | Pinon Ranch Airport (1XS8) | 2026-06-08 17:40 UTC | 2026-06-08 17:52 UTC | 11m |
| N250CR |  | XA65 (XA65) | Baylie Airport (66XS) | 2026-06-08 17:38 UTC | 2026-06-08 17:48 UTC | 10m |
| AUB158 | AUB | Montgomery Regional (Dannelly Field) Airport (KMGM) | Dothan Regional Airport (KDHN) | 2026-06-08 17:07 UTC | 2026-06-08 17:47 UTC | 39m |
| N1507X |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-06-08 17:19 UTC | 2026-06-08 17:45 UTC | 26m |
| N2315B |  | Venice Municipal Airport (KVNC) | Venice Municipal Airport (KVNC) | 2026-06-08 17:09 UTC | 2026-06-08 17:42 UTC | 32m |
| TKJ8UC | TKJ | Sabiha Gokcen International Airport (LTFJ) | Gaziemir Airport (LTBK) | 2026-06-08 17:05 UTC | 2026-06-08 17:41 UTC | 36m |
|  |  | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-06-08 17:37 UTC | 2026-06-08 17:40 UTC | 2m |
| N911PF |  | Addison Airport (KADS) | Casey Field (TE06) | 2026-06-08 17:20 UTC | 2026-06-08 17:39 UTC | 19m |
| N26CF |  | Nikolai Creek Airport (9AK3) | Ted Stevens Anchorage International Airport (PANC) | 2026-06-08 17:10 UTC | 2026-06-08 17:38 UTC | 27m |
| EJA503 | EJA | John Wayne/Orange County Airport (KSNA) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-06-08 17:02 UTC | 2026-06-08 17:36 UTC | 33m |
| N7383L |  | KFTG (KFTG) | Limon Municipal Airport (KLIC) | 2026-06-08 16:44 UTC | 2026-06-08 17:27 UTC | 42m |
| WMU86 | WMU | East Lake Airport (66MI) | Kalamazoo/Battle Creek International Airport (KAZO) | 2026-06-08 17:14 UTC | 2026-06-08 17:26 UTC | 11m |
| N530JL |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-06-08 15:55 UTC | 2026-06-08 17:24 UTC | 1h 29m |
| PREY21 | PRE | Randolph Afb Airport (KRND) | Bailey Airport (2TS8) | 2026-06-08 16:46 UTC | 2026-06-08 17:24 UTC | 38m |
| N20HT |  | K5T6 (K5T6) | Deming Municipal Airport (KDMN) | 2026-06-08 16:42 UTC | 2026-06-08 17:22 UTC | 40m |
| N303RR |  | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Faulkton Municipal Airport (K3FU) | 2026-06-08 16:06 UTC | 2026-06-08 17:21 UTC | 1h 15m |
| DAL2446 | Delta Air Lines | 0ND7 (0ND7) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-06-08 16:28 UTC | 2026-06-08 17:21 UTC | 53m |
| BL68E |  | Baswell Airport (57AL) | Bay Minette Municipal Airport (K1R8) | 2026-06-08 16:56 UTC | 2026-06-08 17:21 UTC | 25m |
| N560BE |  | Wilcox Airport (1MT9) | Mertens Airport (3CO2) | 2026-06-08 16:26 UTC | 2026-06-08 17:20 UTC | 54m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
