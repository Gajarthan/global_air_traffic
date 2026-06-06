# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_22:38:06_UTC-green)

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

**Latest saved flight:** 2026-06-06 22:38:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-06 22:38:06 UTC

- **104,853** saved flights
- **36,946** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **104,853** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,282,401.9 tonnes** estimated CO2 emissions
- **74,342,138 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4312 |
| 2 | SkyWest Airlines | 3956 |
| 3 | IndiGo | 2089 |
| 4 | EJA | 2004 |
| 5 | American Airlines | 1688 |
| 6 | Southwest Airlines | 1589 |
| 7 | ENY | 1316 |
| 8 | Delta Air Lines | 1243 |
| 9 | Lufthansa | 1202 |
| 10 | Vueling | 965 |
| 11 | LATAM Airlines | 927 |
| 12 | WIF | 914 |
| 13 | AXM | 897 |
| 14 | AZU | 840 |
| 15 | LXJ | 791 |
| 16 | Swiss International | 755 |
| 17 | All Nippon Airways | 734 |
| 18 | Alaska Airlines | 729 |
| 19 | QLK | 698 |
| 20 | easyJet | 682 |
| 21 | EJU | 659 |
| 22 | Cathay Pacific | 627 |
| 23 | AEE | 606 |
| 24 | VIV | 603 |
| 25 | Air France | 602 |
| 26 | United Airlines | 585 |
| 27 | MXY | 569 |
| 28 | CXK | 554 |
| 29 | Japan Airlines | 522 |
| 30 | AXB | 515 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 88316 |
| 2 | 🇪🇸 ES | 7218 |
| 3 | 🇮🇳 IN | 6597 |
| 4 | 🇦🇺 AU | 6317 |
| 5 | 🇧🇷 BR | 5719 |
| 6 | 🇩🇪 DE | 5627 |
| 7 | 🇮🇹 IT | 5575 |
| 8 | 🇨🇦 CA | 5455 |
| 9 | 🇯🇵 JP | 4819 |
| 10 | 🇬🇧 GB | 4429 |
| 11 | 🇫🇷 FR | 4154 |
| 12 | 🇨🇴 CO | 3632 |
| 13 | 🇲🇽 MX | 3143 |
| 14 | 🇬🇷 GR | 2987 |
| 15 | 🇳🇴 NO | 2903 |
| 16 | 🇨🇭 CH | 2673 |
| 17 | 🇲🇾 MY | 2296 |
| 18 | 🇹🇷 TR | 2005 |
| 19 | 🇿🇦 ZA | 1804 |
| 20 | 🇳🇿 NZ | 1752 |
| 21 | 🇰🇷 KR | 1724 |
| 22 | 🇹🇭 TH | 1723 |
| 23 | 🇵🇱 PL | 1695 |
| 24 | 🇵🇭 PH | 1537 |
| 25 | 🇬🇹 GT | 1523 |
| 26 | 🇲🇦 MA | 1160 |
| 27 | 🇲🇴 MO | 1102 |
| 28 | 🇳🇱 NL | 1029 |
| 29 | 🇲🇪 ME | 997 |
| 30 | 🇭🇷 HR | 916 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2284 |
| 2 | Denver International Airport |  | US | 1799 |
| 3 | Tokyo International Airport |  | JP | 1599 |
| 4 | Indira Gandhi International Airport |  | IN | 1433 |
| 5 | Harry Reid International Airport |  | US | 1343 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1330 |
| 7 | Guaymaral Airport |  | CO | 1323 |
| 8 | Frankfurt am Main International Airport |  | DE | 1198 |
| 9 | Zurich Airport |  | CH | 1185 |
| 10 | La Aurora Airport |  | GT | 1171 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1132 |
| 12 | El Dorado International Airport |  | CO | 1107 |
| 13 | Macau International Airport |  | MO | 1102 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1061 |
| 15 | Chicago O'Hare International Airport |  | US | 1056 |
| 16 | Madrid Barajas International Airport |  | ES | 916 |
| 17 | Kuala Lumpur International Airport |  | MY | 900 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 898 |
| 19 | Salt Lake City International Airport |  | US | 896 |
| 20 | Capua Airport |  | IT | 883 |
| 21 | Charlotte/Douglas International Airport |  | US | 815 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 803 |
| 23 | Charles de Gaulle International Airport |  | FR | 799 |
| 24 | Congonhas Airport |  | BR | 794 |
| 25 | Bengaluru International Airport |  | IN | 792 |
| 26 | Malpensa International Airport |  | IT | 786 |
| 27 | Daniel K Inouye International Airport |  | US | 718 |
| 28 | Tenerife Norte Airport |  | ES | 716 |
| 29 | Ninoy Aquino International Airport |  | PH | 703 |
| 30 | Barcelona International Airport |  | ES | 687 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 682 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 678 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 673 |
| 34 | Amsterdam Airport Schiphol |  | NL | 637 |
| 35 | Don Mueang International Airport |  | TH | 630 |
| 36 | Vitoria/Foronda Airport |  | ES | 630 |
| 37 | Calgary International Airport |  | CA | 621 |
| 38 | Seattle-Tacoma International Airport |  | US | 611 |
| 39 | Netaji Subhash Chandra Bose International Airport |  | IN | 603 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 599 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 546 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 386 | 21m | 244 km | 1,625.3 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 280 | 1h 7m | 706 km | 3,409.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 276 | 24m | 225 km | 1,070.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 275 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 266 | 14m | 114 km | 521.7 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 257 | 1h 25m | 910 km | 4,032.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 256 | 28m | 304 km | 1,342.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 241 | 1h 10m | 770 km | 3,201.5 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 216 | 19m | 165 km | 614.4 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 209 | 26m | 275 km | 990.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 161 | 20m | 99 km | 275.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 152 | 27m | 215 km | 562.9 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 145 | 31m | 369 km | 923.0 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 144 | 44m | 452 km | 1,122.3 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 144 | 27m | 152 km | 376.3 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 139 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 136 | 18m | 144 km | 338.3 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 128 | 1h 1m | 695 km | 1,534.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 122 | 1h 43m | 1,423 km | 2,994.1 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |
| 29 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 119 | 44m | 241 km | 494.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AIH954 | AIH | Gia Lam Air Base (VVGL) | Zhuhai Airport (ZGSD) | 2026-06-06 21:36 UTC | 2026-06-06 22:38 UTC | 1h 2m |
| CPA300 | Cathay Pacific | Munich International Airport (EDDM) | Zhuhai Airport (ZGSD) | 2026-06-06 11:59 UTC | 2026-06-06 22:30 UTC | 10h 31m |
| N100BW |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-06 22:06 UTC | 2026-06-06 22:26 UTC | 20m |
| CKS273 | CKS | Ben Gurion International Airport (LLBG) | Macau International Airport (VMMC) | 2026-06-06 12:58 UTC | 2026-06-06 22:24 UTC | 9h 25m |
| THY170 | Turkish Airlines | Istanbul Airport (LTFM) | Zhuhai Airport (ZGSD) | 2026-06-06 13:07 UTC | 2026-06-06 22:23 UTC | 9h 15m |
| N1784Q |  | Warrenton/Fauquier Airport (KHWY) | Culpeper Regional Airport (KCJR) | 2026-06-06 21:59 UTC | 2026-06-06 22:21 UTC | 22m |
| AUC | AUC | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-06-06 21:30 UTC | 2026-06-06 22:19 UTC | 48m |
| N550PL |  | Nice-Cote d'Azur Airport (LFMN) | Macau International Airport (VMMC) | 2026-06-06 10:01 UTC | 2026-06-06 22:16 UTC | 12h 14m |
| N125KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-06 21:41 UTC | 2026-06-06 22:13 UTC | 31m |
| N247TC |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-06-06 22:07 UTC | 2026-06-06 22:12 UTC | 5m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-06-06 10:55 UTC | 2026-06-06 22:11 UTC | 11h 15m |
| N157CL |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-06-06 22:02 UTC | 2026-06-06 22:09 UTC | 7m |
| CPA395 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-06-06 14:56 UTC | 2026-06-06 22:07 UTC | 7h 10m |
| N73KG |  | Phoenix Deer Valley Airport (KDVT) | 2AZ7 (2AZ7) | 2026-06-06 22:03 UTC | 2026-06-06 22:07 UTC | 3m |
| N303RH |  | Palo Alto Airport (KPAO) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-06-06 21:33 UTC | 2026-06-06 22:05 UTC | 31m |
| QLK1250 | QLK | Melbourne International Airport (YMML) | Brisbane International Airport (YBBN) | 2026-06-06 20:06 UTC | 2026-06-06 22:05 UTC | 1h 58m |
| UAL15 | United Airlines | London Heathrow Airport (EGLL) | Newark Liberty International Airport (KEWR) | 2026-06-06 14:37 UTC | 2026-06-06 22:03 UTC | 7h 26m |
| N911BT |  | Donalsonville Municipal Airport (K17J) | Donalsonville Municipal Airport (K17J) | 2026-06-06 21:37 UTC | 2026-06-06 22:02 UTC | 25m |
| CPA640 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Zhuhai Airport (ZGSD) | 2026-06-06 11:43 UTC | 2026-06-06 22:00 UTC | 10h 16m |
| N88EP |  | San Luis Obispo County Regional Airport (KSBP) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-06-06 21:34 UTC | 2026-06-06 21:59 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
