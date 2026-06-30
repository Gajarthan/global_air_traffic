# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--30_23:26:20_UTC-green)

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

**Latest saved flight:** 2026-06-30 23:26:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-30 23:26:20 UTC

- **124,937** saved flights
- **42,742** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **124,937** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,508,458.1 tonnes** estimated CO2 emissions
- **87,446,846 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5084 |
| 2 | SkyWest Airlines | 4635 |
| 3 | EJA | 2448 |
| 4 | IndiGo | 2370 |
| 5 | American Airlines | 1934 |
| 6 | Southwest Airlines | 1877 |
| 7 | ENY | 1569 |
| 8 | Delta Air Lines | 1489 |
| 9 | Lufthansa | 1338 |
| 10 | LATAM Airlines | 1125 |
| 11 | Vueling | 1108 |
| 12 | WIF | 1104 |
| 13 | AZU | 1057 |
| 14 | AXM | 992 |
| 15 | LXJ | 969 |
| 16 | Swiss International | 875 |
| 17 | All Nippon Airways | 840 |
| 18 | Alaska Airlines | 819 |
| 19 | easyJet | 795 |
| 20 | QLK | 781 |
| 21 | EJU | 777 |
| 22 | Cathay Pacific | 694 |
| 23 | AEE | 690 |
| 24 | VIV | 683 |
| 25 | Air France | 678 |
| 26 | United Airlines | 669 |
| 27 | CXK | 665 |
| 28 | MXY | 652 |
| 29 | JetBlue | 640 |
| 30 | GLO | 629 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 106726 |
| 2 | 🇪🇸 ES | 8359 |
| 3 | 🇮🇳 IN | 7434 |
| 4 | 🇦🇺 AU | 7288 |
| 5 | 🇧🇷 BR | 6957 |
| 6 | 🇩🇪 DE | 6609 |
| 7 | 🇮🇹 IT | 6591 |
| 8 | 🇨🇦 CA | 6566 |
| 9 | 🇬🇧 GB | 5506 |
| 10 | 🇯🇵 JP | 5481 |
| 11 | 🇫🇷 FR | 4932 |
| 12 | 🇨🇴 CO | 4032 |
| 13 | 🇲🇽 MX | 3633 |
| 14 | 🇬🇷 GR | 3560 |
| 15 | 🇳🇴 NO | 3429 |
| 16 | 🇨🇭 CH | 3192 |
| 17 | 🇹🇷 TR | 2622 |
| 18 | 🇲🇾 MY | 2568 |
| 19 | 🇿🇦 ZA | 2051 |
| 20 | 🇵🇱 PL | 2045 |
| 21 | 🇳🇿 NZ | 2021 |
| 22 | 🇹🇭 TH | 1955 |
| 23 | 🇰🇷 KR | 1939 |
| 24 | 🇵🇭 PH | 1772 |
| 25 | 🇬🇹 GT | 1731 |
| 26 | 🇲🇦 MA | 1343 |
| 27 | 🇲🇪 ME | 1241 |
| 28 | 🇳🇱 NL | 1178 |
| 29 | 🇲🇴 MO | 1178 |
| 30 | 🇧🇸 BS | 1081 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2621 |
| 2 | Denver International Airport |  | US | 2111 |
| 3 | Tokyo International Airport |  | JP | 1811 |
| 4 | Indira Gandhi International Airport |  | IN | 1637 |
| 5 | Harry Reid International Airport |  | US | 1563 |
| 6 | Guaymaral Airport |  | CO | 1520 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1498 |
| 8 | Zurich Airport |  | CH | 1382 |
| 9 | La Aurora Airport |  | GT | 1337 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1334 |
| 11 | Frankfurt am Main International Airport |  | DE | 1291 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1229 |
| 13 | Chicago O'Hare International Airport |  | US | 1210 |
| 14 | Macau International Airport |  | MO | 1178 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1101 |
| 17 | Capua Airport |  | IT | 1061 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1040 |
| 19 | Madrid Barajas International Airport |  | ES | 1035 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1013 |
| 21 | Kuala Lumpur International Airport |  | MY | 999 |
| 22 | Congonhas Airport |  | BR | 975 |
| 23 | Charlotte/Douglas International Airport |  | US | 944 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 916 |
| 25 | Charles de Gaulle International Airport |  | FR | 907 |
| 26 | Bengaluru International Airport |  | IN | 896 |
| 27 | Malpensa International Airport |  | IT | 861 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 829 |
| 29 | Ninoy Aquino International Airport |  | PH | 822 |
| 30 | Daniel K Inouye International Airport |  | US | 800 |
| 31 | Barcelona International Airport |  | ES | 781 |
| 32 | Tenerife Norte Airport |  | ES | 768 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 764 |
| 34 | Calgary International Airport |  | CA | 736 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 731 |
| 36 | Seattle-Tacoma International Airport |  | US | 723 |
| 37 | Vitoria/Foronda Airport |  | ES | 720 |
| 38 | Scottsdale Airport |  | US | 720 |
| 39 | Amsterdam Airport Schiphol |  | NL | 715 |
| 40 | Viracopos International Airport |  | BR | 711 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 633 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 456 | 21m | 244 km | 1,920.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 324 | 24m | 225 km | 1,257.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 315 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 299 | 1h 10m | 770 km | 3,972.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 298 | 1h 25m | 910 km | 4,676.3 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 242 | 26m | 275 km | 1,146.7 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 231 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 186 | 22m | 55 km | 176.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 179 | 26m | 215 km | 662.9 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 177 | 20m | 99 km | 303.2 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 174 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 173 | 44m | 241 km | 718.6 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 171 | 27m | 152 km | 446.9 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 159 | 1h 44m | 1,423 km | 3,902.1 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 159 | 31m | 369 km | 1,012.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 157 | 18m | 144 km | 390.5 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 155 | 44m | 452 km | 1,208.0 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 153 | 20m | 250 km | 660.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 146 | 1h 38m | 1,156 km | 2,912.6 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 146 | 1h 1m | 695 km | 1,750.1 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 143 | 1h 17m | 961 km | 2,370.3 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |
| 29 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 140 | 30m | 49 km | 118.3 t |
| 30 | Calgary International Airport (CYYC) | Moose Jaw Municipal Airport (CJS4) | 136 | 1h 1m | 611 km | 1,434.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BRG622 | BRG | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-06-30 22:42 UTC | 2026-06-30 23:26 UTC | 43m |
| VEGA21 | VEG | 75OK (75OK) | Ramey 1 Airport (0OK8) | 2026-06-30 23:04 UTC | 2026-06-30 23:26 UTC | 21m |
| N429EP |  | Middle Georgia Regional Airport (KMCN) | Cochran Airport (K48A) | 2026-06-30 22:20 UTC | 2026-06-30 23:24 UTC | 1h 3m |
| N814SS |  | Kenai Municipal Airport (PAEN) | Ted Stevens Anchorage International Airport (PANC) | 2026-06-30 22:59 UTC | 2026-06-30 23:23 UTC | 24m |
| N2113J |  | Taylor Airport (3WA0) | Auburn Municipal Airport (KS50) | 2026-06-30 22:55 UTC | 2026-06-30 23:20 UTC | 24m |
| N993CB |  | Livermore Municipal Airport (KLVK) | Mc Clellan Airfield (KMCC) | 2026-06-30 22:52 UTC | 2026-06-30 23:11 UTC | 18m |
| N9767F |  | Brookhaven Airport (KHWV) | Talmage Field (03NY) | 2026-06-30 22:23 UTC | 2026-06-30 23:10 UTC | 46m |
| TIH | TIH | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-06-30 23:06 UTC | 2026-06-30 23:06 UTC | 0m |
| UAL484 | United Airlines | George Bush Intcntl/Houston Airport (KIAH) | Trego Wakeeney Airport (K0H1) | 2026-06-30 21:41 UTC | 2026-06-30 23:05 UTC | 1h 23m |
| TKR107 | TKR | Animas Air Park (K00C) | Animas Air Park (K00C) | 2026-06-30 22:43 UTC | 2026-06-30 23:04 UTC | 20m |
| YGA | YGA | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-06-30 22:16 UTC | 2026-06-30 23:02 UTC | 45m |
| EJA889 | EJA | Sugar Land Regional Airport (KSGR) | Habersham County Airport (KAJR) | 2026-06-30 21:27 UTC | 2026-06-30 23:01 UTC | 1h 34m |
| CASTL26 | CAS | Atlantic City International Airport (KACY) | New Castle Airport (KILG) | 2026-06-30 22:01 UTC | 2026-06-30 23:00 UTC | 58m |
| N748DC |  | North Las Vegas Airport (KVGT) | Carson City Airport (KCXP) | 2026-06-30 21:15 UTC | 2026-06-30 22:58 UTC | 1h 43m |
| N416NH |  | Wolford's Airport (IL01) | The Valley Airport (61AR) | 2026-06-30 21:52 UTC | 2026-06-30 22:56 UTC | 1h 4m |
| TKR101 | TKR | Animas Air Park (K00C) | Animas Air Park (K00C) | 2026-06-30 22:31 UTC | 2026-06-30 22:54 UTC | 23m |
| N612RM |  | Ankeny Regional Airport (KIKV) | Jesse Viertel Memorial Airport (KVER) | 2026-06-30 22:20 UTC | 2026-06-30 22:52 UTC | 32m |
| PBR675 | PBR | Victoria International Airport (CYYJ) | Boundary Bay Airport (CZBB) | 2026-06-30 22:36 UTC | 2026-06-30 22:51 UTC | 15m |
| ERU2 | ERU | AZ86 (AZ86) | Payson Airport (KPAN) | 2026-06-30 22:04 UTC | 2026-06-30 22:50 UTC | 46m |
| JRE823 | JRE | Dallas Love Field (KDAL) | Santa Fe Regional Airport (KSAF) | 2026-06-30 21:23 UTC | 2026-06-30 22:50 UTC | 1h 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
