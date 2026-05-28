# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--28_16:11:50_UTC-green)

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

**Latest saved flight:** 2026-05-28 16:11:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-28 16:11:50 UTC

- **95,791** saved flights
- **33,712** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **95,791** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,175,520.8 tonnes** estimated CO2 emissions
- **68,146,133 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4029 |
| 2 | SkyWest Airlines | 3560 |
| 3 | IndiGo | 1988 |
| 4 | EJA | 1809 |
| 5 | American Airlines | 1450 |
| 6 | Southwest Airlines | 1393 |
| 7 | ENY | 1179 |
| 8 | Lufthansa | 1150 |
| 9 | Delta Air Lines | 1049 |
| 10 | Vueling | 909 |
| 11 | LATAM Airlines | 861 |
| 12 | AXM | 848 |
| 13 | WIF | 845 |
| 14 | AZU | 767 |
| 15 | LXJ | 727 |
| 16 | Swiss International | 715 |
| 17 | All Nippon Airways | 709 |
| 18 | Alaska Airlines | 664 |
| 19 | QLK | 663 |
| 20 | easyJet | 627 |
| 21 | EJU | 611 |
| 22 | Cathay Pacific | 582 |
| 23 | AEE | 579 |
| 24 | Air France | 565 |
| 25 | VIV | 564 |
| 26 | CXK | 511 |
| 27 | MXY | 506 |
| 28 | Japan Airlines | 493 |
| 29 | AXB | 485 |
| 30 | AIQ | 462 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 79104 |
| 2 | 🇪🇸 ES | 6702 |
| 3 | 🇮🇳 IN | 6271 |
| 4 | 🇦🇺 AU | 5880 |
| 5 | 🇧🇷 BR | 5261 |
| 6 | 🇩🇪 DE | 5258 |
| 7 | 🇮🇹 IT | 5193 |
| 8 | 🇨🇦 CA | 4849 |
| 9 | 🇯🇵 JP | 4584 |
| 10 | 🇬🇧 GB | 4104 |
| 11 | 🇫🇷 FR | 3895 |
| 12 | 🇨🇴 CO | 3314 |
| 13 | 🇲🇽 MX | 2936 |
| 14 | 🇬🇷 GR | 2766 |
| 15 | 🇳🇴 NO | 2689 |
| 16 | 🇨🇭 CH | 2520 |
| 17 | 🇲🇾 MY | 2152 |
| 18 | 🇹🇷 TR | 1774 |
| 19 | 🇿🇦 ZA | 1721 |
| 20 | 🇳🇿 NZ | 1634 |
| 21 | 🇹🇭 TH | 1625 |
| 22 | 🇰🇷 KR | 1580 |
| 23 | 🇵🇱 PL | 1566 |
| 24 | 🇵🇭 PH | 1444 |
| 25 | 🇬🇹 GT | 1431 |
| 26 | 🇲🇦 MA | 1090 |
| 27 | 🇲🇴 MO | 1038 |
| 28 | 🇳🇱 NL | 967 |
| 29 | 🇲🇪 ME | 946 |
| 30 | 🇭🇷 HR | 871 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2069 |
| 2 | Denver International Airport |  | US | 1623 |
| 3 | Tokyo International Airport |  | JP | 1521 |
| 4 | Indira Gandhi International Airport |  | IN | 1357 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1269 |
| 6 | Harry Reid International Airport |  | US | 1236 |
| 7 | Guaymaral Airport |  | CO | 1168 |
| 8 | Frankfurt am Main International Airport |  | DE | 1160 |
| 9 | Zurich Airport |  | CH | 1119 |
| 10 | La Aurora Airport |  | GT | 1097 |
| 11 | Macau International Airport |  | MO | 1038 |
| 12 | El Dorado International Airport |  | CO | 1035 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1034 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 957 |
| 15 | Chicago O'Hare International Airport |  | US | 921 |
| 16 | Kuala Lumpur International Airport |  | MY | 853 |
| 17 | Madrid Barajas International Airport |  | ES | 848 |
| 18 | Salt Lake City International Airport |  | US | 810 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 806 |
| 20 | Capua Airport |  | IT | 794 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 763 |
| 22 | Malpensa International Airport |  | IT | 752 |
| 23 | Bengaluru International Airport |  | IN | 752 |
| 24 | Charles de Gaulle International Airport |  | FR | 747 |
| 25 | Congonhas Airport |  | BR | 730 |
| 26 | Charlotte/Douglas International Airport |  | US | 725 |
| 27 | Daniel K Inouye International Airport |  | US | 684 |
| 28 | Tenerife Norte Airport |  | ES | 681 |
| 29 | Ninoy Aquino International Airport |  | PH | 659 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 642 |
| 31 | Barcelona International Airport |  | ES | 642 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 621 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 614 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 601 |
| 35 | Amsterdam Airport Schiphol |  | NL | 595 |
| 36 | Don Mueang International Airport |  | TH | 593 |
| 37 | Vitoria/Foronda Airport |  | ES | 593 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 569 |
| 39 | Calgary International Airport |  | CA | 565 |
| 40 | O. R. Tambo International Airport |  | ZA | 547 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 480 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 354 | 21m | 244 km | 1,490.6 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 260 | 24m | 225 km | 1,008.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 254 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 243 | 14m | 114 km | 476.6 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 242 | 1h 26m | 910 km | 3,797.5 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 240 | 28m | 304 km | 1,258.1 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 221 | 1h 10m | 770 km | 2,935.8 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 208 | 19m | 165 km | 591.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 192 | 26m | 275 km | 909.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 144 | 27m | 215 km | 533.3 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 142 | 44m | 452 km | 1,106.7 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 138 | 22m | 55 km | 131.2 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 138 | 27m | 152 km | 360.6 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 130 | 20m | 250 km | 561.5 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 129 | 20m | 147 km | 326.4 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 125 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 123 | 1h 1m | 695 km | 1,474.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 123 | 18m | 144 km | 306.0 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 121 | 1h 39m | 1,156 km | 2,413.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 115 | 1h 52m | 1,304 km | 2,587.2 t |
| 27 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 113 | 1h 18m | 961 km | 1,873.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N4423Q |  | Colonial Air Park (01TN) | Pegasus Field (7TN4) | 2026-05-28 15:43 UTC | 2026-05-28 16:11 UTC | 28m |
| WAH | WAH | Kenai Municipal Airport (PAEN) | Trading Bay Production Airport (5AK0) | 2026-05-28 15:56 UTC | 2026-05-28 16:09 UTC | 13m |
| FHRIV | FHR | Rennes-Saint-Jacques Airport (LFRN) | Rennes-Saint-Jacques Airport (LFRN) | 2026-05-28 15:48 UTC | 2026-05-28 16:03 UTC | 15m |
| DKKSU | DKK | Courchevel Airport (LFLJ) | Ambri Airport (LSPM) | 2026-05-28 13:48 UTC | 2026-05-28 16:02 UTC | 2h 14m |
| FLC90 | FLC | Centennial Airport (KAPA) | Spring Canyon Airport (CO94) | 2026-05-28 15:11 UTC | 2026-05-28 15:58 UTC | 47m |
| N472AT |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-05-28 15:23 UTC | 2026-05-28 15:57 UTC | 34m |
| PEA301 | PEA | Geneva Cointrin International Airport (LSGG) | Nice-Cote d'Azur Airport (LFMN) | 2026-05-28 15:08 UTC | 2026-05-28 15:53 UTC | 45m |
|  |  | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-05-28 15:37 UTC | 2026-05-28 15:50 UTC | 12m |
| ZKIDU | ZKI | Balclutha Aerodrome (NZBA) | Taieri Airport (NZTI) | 2026-05-28 15:35 UTC | 2026-05-28 15:49 UTC | 13m |
| N125AP |  | Austin Executive Airport (KEDC) | Austin Executive Airport (KEDC) | 2026-05-28 15:34 UTC | 2026-05-28 15:48 UTC | 14m |
| FAC5767 | FAC | El Dorado International Airport (SKBO) | Velasquez Airport (SKVL) | 2026-05-28 15:15 UTC | 2026-05-28 15:46 UTC | 31m |
| N401AA |  | Kissimmee Gateway Airport (KISM) | Orlando Sanford International Airport (KSFB) | 2026-05-28 15:09 UTC | 2026-05-28 15:46 UTC | 37m |
| ERU42 | ERU | AZ86 (AZ86) | 42AZ (42AZ) | 2026-05-28 15:05 UTC | 2026-05-28 15:37 UTC | 31m |
| PSVTS | PSV | Campo de Marte Airport (SBMT) | Ubatuba Airport (SDUB) | 2026-05-28 15:16 UTC | 2026-05-28 15:37 UTC | 21m |
| N213JD |  | Vowers Ranch Airport (WY29) | Laramie Regional Airport (KLAR) | 2026-05-28 15:15 UTC | 2026-05-28 15:36 UTC | 21m |
| ROAR11 | ROA | Ball Airport (5MS8) | MS52 (MS52) | 2026-05-28 15:23 UTC | 2026-05-28 15:36 UTC | 12m |
| FIN7EN | Finnair | Helsinki Vantaa Airport (EFHK) | Pyhoselka Airport (EFPH) | 2026-05-28 14:44 UTC | 2026-05-28 15:35 UTC | 51m |
| N738BJ |  | Erie Municipal Airport (KEIK) | Erie Municipal Airport (KEIK) | 2026-05-28 15:29 UTC | 2026-05-28 15:34 UTC | 4m |
| JNX1 | JNX | Roswell Air Center Airport (KROW) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-05-28 14:22 UTC | 2026-05-28 15:34 UTC | 1h 11m |
| KEN46 | KEN | Boeing Field/King County International Airport (KBFI) | William R Fairchild International Airport (KCLM) | 2026-05-28 15:12 UTC | 2026-05-28 15:33 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
