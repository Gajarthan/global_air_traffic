# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_05:36:33_UTC-green)

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

**Latest saved flight:** 2026-05-09 05:36:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-09 05:36:33 UTC

- **74,862** saved flights
- **27,634** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **74,862** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **921,241.2 tonnes** estimated CO2 emissions
- **53,405,289 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3206 |
| 2 | SkyWest Airlines | 2787 |
| 3 | IndiGo | 1676 |
| 4 | EJA | 1387 |
| 5 | American Airlines | 1169 |
| 6 | Southwest Airlines | 1088 |
| 7 | Lufthansa | 965 |
| 8 | ENY | 937 |
| 9 | Vueling | 725 |
| 10 | AXM | 703 |
| 11 | Delta Air Lines | 697 |
| 12 | LATAM Airlines | 693 |
| 13 | WIF | 649 |
| 14 | All Nippon Airways | 608 |
| 15 | AZU | 603 |
| 16 | QLK | 579 |
| 17 | Swiss International | 568 |
| 18 | LXJ | 554 |
| 19 | Alaska Airlines | 530 |
| 20 | easyJet | 490 |
| 21 | AEE | 479 |
| 22 | EJU | 479 |
| 23 | Cathay Pacific | 470 |
| 24 | VIV | 454 |
| 25 | Japan Airlines | 437 |
| 26 | Air France | 431 |
| 27 | AXB | 414 |
| 28 | CXK | 384 |
| 29 | AIQ | 368 |
| 30 | MXY | 363 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 60408 |
| 2 | 🇪🇸 ES | 5376 |
| 3 | 🇮🇳 IN | 5262 |
| 4 | 🇦🇺 AU | 4943 |
| 5 | 🇧🇷 BR | 4201 |
| 6 | 🇩🇪 DE | 4175 |
| 7 | 🇮🇹 IT | 4066 |
| 8 | 🇯🇵 JP | 3901 |
| 9 | 🇨🇦 CA | 3741 |
| 10 | 🇬🇧 GB | 3198 |
| 11 | 🇫🇷 FR | 2942 |
| 12 | 🇨🇴 CO | 2690 |
| 13 | 🇲🇽 MX | 2325 |
| 14 | 🇬🇷 GR | 2202 |
| 15 | 🇳🇴 NO | 2076 |
| 16 | 🇨🇭 CH | 2020 |
| 17 | 🇲🇾 MY | 1754 |
| 18 | 🇿🇦 ZA | 1445 |
| 19 | 🇳🇿 NZ | 1364 |
| 20 | 🇹🇷 TR | 1334 |
| 21 | 🇹🇭 TH | 1321 |
| 22 | 🇵🇱 PL | 1246 |
| 23 | 🇵🇭 PH | 1212 |
| 24 | 🇬🇹 GT | 1184 |
| 25 | 🇰🇷 KR | 1172 |
| 26 | 🇲🇦 MA | 885 |
| 27 | 🇲🇴 MO | 865 |
| 28 | 🇲🇪 ME | 798 |
| 29 | 🇳🇱 NL | 775 |
| 30 | 🇧🇸 BS | 627 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1664 |
| 2 | Tokyo International Airport |  | JP | 1310 |
| 3 | Denver International Airport |  | US | 1258 |
| 4 | Indira Gandhi International Airport |  | IN | 1109 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1079 |
| 6 | Frankfurt am Main International Airport |  | DE | 964 |
| 7 | Harry Reid International Airport |  | US | 934 |
| 8 | La Aurora Airport |  | GT | 888 |
| 9 | Guaymaral Airport |  | CO | 885 |
| 10 | El Dorado International Airport |  | CO | 878 |
| 11 | Zurich Airport |  | CH | 878 |
| 12 | Macau International Airport |  | MO | 865 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 753 |
| 14 | Chicago O'Hare International Airport |  | US | 728 |
| 15 | Kuala Lumpur International Airport |  | MY | 704 |
| 16 | Madrid Barajas International Airport |  | ES | 700 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 664 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 650 |
| 19 | Bengaluru International Airport |  | IN | 649 |
| 20 | Malpensa International Airport |  | IT | 644 |
| 21 | Salt Lake City International Airport |  | US | 617 |
| 22 | Congonhas Airport |  | BR | 596 |
| 23 | Charlotte/Douglas International Airport |  | US | 590 |
| 24 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 577 |
| 25 | Charles de Gaulle International Airport |  | FR | 577 |
| 26 | Capua Airport |  | IT | 575 |
| 27 | Tenerife Norte Airport |  | ES | 559 |
| 28 | Ninoy Aquino International Airport |  | PH | 550 |
| 29 | Daniel K Inouye International Airport |  | US | 549 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 536 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 518 |
| 32 | Barcelona International Airport |  | ES | 512 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 503 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 498 |
| 35 | Vitoria/Foronda Airport |  | ES | 480 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 470 |
| 37 | Amsterdam Airport Schiphol |  | NL | 467 |
| 38 | Don Mueang International Airport |  | TH | 465 |
| 39 | O. R. Tambo International Airport |  | ZA | 454 |
| 40 | Calgary International Airport |  | CA | 448 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 368 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 270 | 1h 8m | 706 km | 3,287.3 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 266 | 21m | 244 km | 1,120.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 219 | 24m | 225 km | 849.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 210 | 28m | 304 km | 1,100.9 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 205 | 1h 27m | 910 km | 3,216.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 192 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 181 | 19m | 165 km | 514.9 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 176 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 163 | 26m | 275 km | 772.4 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 162 | 1h 12m | 770 km | 2,152.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 137 | 21m | 99 km | 234.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 133 | 44m | 452 km | 1,036.5 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 121 | 31m | 369 km | 770.2 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 117 | 27m | 152 km | 305.8 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 112 | 27m | 215 km | 414.8 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 111 | 20m | 147 km | 280.9 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 111 | 20m | 250 km | 479.5 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 109 | 14m | 154 km | 288.8 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 102 | 1h 2m | 695 km | 1,222.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 101 | 1h 42m | 1,423 km | 2,478.7 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 100 | 58m | 493 km | 850.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 99 | 23m | 55 km | 94.1 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 96 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 93 | 52m | 556 km | 891.5 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 92 | 1h 19m | 961 km | 1,524.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BBC371 | BBC | VGZR (VGZR) | Tribhuvan International Airport (VNKT) | 2026-05-09 04:20 UTC | 2026-05-09 05:36 UTC | 1h 16m |
| SWR12K | Swiss International | Václav Havel Airport (LKPR) | Zurich Airport (LSZH) | 2026-05-09 04:34 UTC | 2026-05-09 05:35 UTC | 1h 0m |
| EZS46NT | EZS | Geneva Cointrin International Airport (LSGG) | Bordeaux-Merignac (BA 106) Airport (LFBD) | 2026-05-09 04:26 UTC | 2026-05-09 05:22 UTC | 55m |
| CPA250 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-05-08 17:38 UTC | 2026-05-09 05:20 UTC | 11h 41m |
| GLO1468 | GLO | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | Fazenda Cedro Airport (SWCE) | 2026-05-09 03:29 UTC | 2026-05-09 05:16 UTC | 1h 47m |
| AIQ3209 | AIQ | Don Mueang International Airport (VTBD) | VLXL (VLXL) | 2026-05-09 04:21 UTC | 2026-05-09 05:12 UTC | 50m |
| ASL57F | ASL | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 2026-05-09 04:50 UTC | 2026-05-09 05:11 UTC | 21m |
| SWR104C | Swiss International | Geneva Cointrin International Airport (LSGG) | Frankfurt am Main International Airport (EDDF) | 2026-05-09 04:19 UTC | 2026-05-09 05:10 UTC | 50m |
| DAL2245 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 04:58 UTC | 2026-05-09 05:08 UTC | 10m |
| VAR493 | VAR | Phoenix Goodyear Airport (KGYR) | Lake Havasu City Airport (KHII) | 2026-05-09 03:49 UTC | 2026-05-09 05:07 UTC | 1h 18m |
| LNI | LNI | Jurien Bay Airport (YJNB) | Jurien Bay Airport (YJNB) | 2026-05-09 05:00 UTC | 2026-05-09 05:07 UTC | 7m |
| STA603 | STA | Tribhuvan International Airport (VNKT) | Tribhuvan International Airport (VNKT) | 2026-05-09 05:02 UTC | 2026-05-09 05:07 UTC | 4m |
| JJP801 | JJP | Narita International Airport (RJAA) | Asahikawa Airport (RJEC) | 2026-05-09 03:55 UTC | 2026-05-09 05:03 UTC | 1h 7m |
| RYR196A | Ryanair | Luqa Airport (LMML) | Stanke Dimitrov Highway Strip (LB37) | 2026-05-09 03:46 UTC | 2026-05-09 05:02 UTC | 1h 16m |
| RYR46YA | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Tortoli' / Arbatax Airport (LIET) | 2026-05-09 04:10 UTC | 2026-05-09 05:02 UTC | 52m |
| APG225 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-05-09 04:37 UTC | 2026-05-09 05:01 UTC | 24m |
| AXM6490 | AXM | Kota Kinabalu International Airport (WBKK) | Telupid Airport (WBKE) | 2026-05-09 04:47 UTC | 2026-05-09 05:01 UTC | 13m |
| ASA1102 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-05-09 04:36 UTC | 2026-05-09 04:57 UTC | 21m |
| DLH3KV | Lufthansa | Dresden Airport (EDDC) | Frankfurt am Main International Airport (EDDF) | 2026-05-09 04:09 UTC | 2026-05-09 04:54 UTC | 45m |
| IGO183E | IndiGo | Bengaluru International Airport (VOBL) | Daltonganj Airport (VE54) | 2026-05-09 03:15 UTC | 2026-05-09 04:54 UTC | 1h 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
