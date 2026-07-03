# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--03_16:45:02_UTC-green)

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

**Latest saved flight:** 2026-07-03 16:45:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-03 16:45:02 UTC

- **127,546** saved flights
- **43,513** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **127,546** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,538,827.0 tonnes** estimated CO2 emissions
- **89,207,361 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5173 |
| 2 | SkyWest Airlines | 4707 |
| 3 | EJA | 2506 |
| 4 | IndiGo | 2412 |
| 5 | American Airlines | 1959 |
| 6 | Southwest Airlines | 1913 |
| 7 | ENY | 1600 |
| 8 | Delta Air Lines | 1518 |
| 9 | Lufthansa | 1354 |
| 10 | LATAM Airlines | 1159 |
| 11 | Vueling | 1127 |
| 12 | WIF | 1124 |
| 13 | AZU | 1077 |
| 14 | AXM | 1002 |
| 15 | LXJ | 992 |
| 16 | Swiss International | 885 |
| 17 | All Nippon Airways | 853 |
| 18 | Alaska Airlines | 825 |
| 19 | easyJet | 814 |
| 20 | QLK | 803 |
| 21 | EJU | 788 |
| 22 | Cathay Pacific | 708 |
| 23 | VIV | 701 |
| 24 | AEE | 698 |
| 25 | Air France | 695 |
| 26 | CXK | 686 |
| 27 | United Airlines | 675 |
| 28 | MXY | 664 |
| 29 | JetBlue | 654 |
| 30 | GLO | 644 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 109073 |
| 2 | 🇪🇸 ES | 8489 |
| 3 | 🇮🇳 IN | 7558 |
| 4 | 🇦🇺 AU | 7447 |
| 5 | 🇧🇷 BR | 7131 |
| 6 | 🇩🇪 DE | 6729 |
| 7 | 🇨🇦 CA | 6706 |
| 8 | 🇮🇹 IT | 6693 |
| 9 | 🇬🇧 GB | 5633 |
| 10 | 🇯🇵 JP | 5567 |
| 11 | 🇫🇷 FR | 5047 |
| 12 | 🇨🇴 CO | 4062 |
| 13 | 🇲🇽 MX | 3708 |
| 14 | 🇬🇷 GR | 3625 |
| 15 | 🇳🇴 NO | 3489 |
| 16 | 🇨🇭 CH | 3245 |
| 17 | 🇹🇷 TR | 2715 |
| 18 | 🇲🇾 MY | 2597 |
| 19 | 🇿🇦 ZA | 2118 |
| 20 | 🇵🇱 PL | 2084 |
| 21 | 🇳🇿 NZ | 2059 |
| 22 | 🇹🇭 TH | 1990 |
| 23 | 🇰🇷 KR | 1958 |
| 24 | 🇵🇭 PH | 1804 |
| 25 | 🇬🇹 GT | 1751 |
| 26 | 🇲🇦 MA | 1366 |
| 27 | 🇲🇪 ME | 1260 |
| 28 | 🇳🇱 NL | 1203 |
| 29 | 🇲🇴 MO | 1184 |
| 30 | 🇧🇸 BS | 1101 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2661 |
| 2 | Denver International Airport |  | US | 2151 |
| 3 | Tokyo International Airport |  | JP | 1835 |
| 4 | Indira Gandhi International Airport |  | IN | 1662 |
| 5 | Harry Reid International Airport |  | US | 1593 |
| 6 | Guaymaral Airport |  | CO | 1549 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1513 |
| 8 | Zurich Airport |  | CH | 1401 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1355 |
| 10 | La Aurora Airport |  | GT | 1355 |
| 11 | Frankfurt am Main International Airport |  | DE | 1312 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1245 |
| 13 | Chicago O'Hare International Airport |  | US | 1233 |
| 14 | Macau International Airport |  | MO | 1184 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1124 |
| 17 | Capua Airport |  | IT | 1067 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1056 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1053 |
| 20 | Madrid Barajas International Airport |  | ES | 1045 |
| 21 | Kuala Lumpur International Airport |  | MY | 1010 |
| 22 | Congonhas Airport |  | BR | 1001 |
| 23 | Charlotte/Douglas International Airport |  | US | 956 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 935 |
| 25 | Charles de Gaulle International Airport |  | FR | 926 |
| 26 | Bengaluru International Airport |  | IN | 916 |
| 27 | Malpensa International Airport |  | IT | 871 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 856 |
| 29 | Ninoy Aquino International Airport |  | PH | 836 |
| 30 | Daniel K Inouye International Airport |  | US | 807 |
| 31 | Barcelona International Airport |  | ES | 792 |
| 32 | Tenerife Norte Airport |  | ES | 777 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 775 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 746 |
| 35 | Calgary International Airport |  | CA | 744 |
| 36 | Scottsdale Airport |  | US | 738 |
| 37 | Seattle-Tacoma International Airport |  | US | 734 |
| 38 | Vitoria/Foronda Airport |  | ES | 734 |
| 39 | Viracopos International Airport |  | BR | 726 |
| 40 | Amsterdam Airport Schiphol |  | NL | 725 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 647 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 462 | 21m | 244 km | 1,945.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 328 | 24m | 225 km | 1,272.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 322 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 309 | 1h 10m | 770 km | 4,104.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 244 | 26m | 275 km | 1,156.2 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 236 | 31m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 187 | 22m | 55 km | 177.7 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 181 | 26m | 215 km | 670.3 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 178 | 44m | 241 km | 739.4 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 177 | 20m | 99 km | 303.2 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 172 | 27m | 152 km | 449.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 164 | 1h 45m | 1,423 km | 4,024.8 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 162 | 31m | 369 km | 1,031.2 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 157 | 18m | 144 km | 390.5 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 156 | 44m | 452 km | 1,215.8 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 155 | 20m | 250 km | 669.5 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 152 | 30m | 49 km | 128.5 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 150 | 1h 1m | 695 km | 1,798.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 147 | 1h 17m | 961 km | 2,436.6 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 146 | 54m | 136 km | 342.3 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N404PH |  | Fair Weather Field (TX42) | William P Hobby Airport (KHOU) | 2026-07-03 16:27 UTC | 2026-07-03 16:45 UTC | 17m |
| N477XP |  | P K Airpark (K5W4) | P K Airpark (K5W4) | 2026-07-03 15:05 UTC | 2026-07-03 16:43 UTC | 1h 37m |
| DFALB | DFA | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-07-03 16:13 UTC | 2026-07-03 16:32 UTC | 18m |
| N467DC |  | Waukegan Ntl Airport (KUGN) | 3WI1 (3WI1) | 2026-07-03 16:15 UTC | 2026-07-03 16:29 UTC | 14m |
| N835FG |  | Trenton Mercer Airport (KTTN) | Flying W Airport (KN14) | 2026-07-03 16:06 UTC | 2026-07-03 16:28 UTC | 22m |
| MNB353 | MNB | Sharjah International Airport (OMSJ) | Zhuhai Airport (ZGSD) | 2026-07-03 09:05 UTC | 2026-07-03 16:22 UTC | 7h 16m |
| INTEL24 | INT | Chino Airport (KCNO) | Apple Valley Airport (KAPV) | 2026-07-03 16:03 UTC | 2026-07-03 16:18 UTC | 14m |
| WIF9BY | WIF | Bergen Airport Flesland (ENBR) | Bringeland Airport (ENBL) | 2026-07-03 15:59 UTC | 2026-07-03 16:17 UTC | 17m |
| N640SP |  | Mount Hawley Auxiliary Airport (K3MY) | Mount Hawley Auxiliary Airport (K3MY) | 2026-07-03 14:31 UTC | 2026-07-03 16:16 UTC | 1h 45m |
| N2JW |  | Marseille Provence Airport (LFML) | Bangor International Airport (KBGR) | 2026-07-03 09:09 UTC | 2026-07-03 16:15 UTC | 7h 5m |
| CPA336 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Zhuhai Airport (ZGSD) | 2026-07-03 08:51 UTC | 2026-07-03 16:13 UTC | 7h 22m |
| N110CC |  | KU42 (KU42) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-07-03 15:56 UTC | 2026-07-03 16:13 UTC | 16m |
| HAF405 | HAF | Elefsis Airport (LGEL) | Mikonos Airport (LGMK) | 2026-07-03 15:48 UTC | 2026-07-03 16:13 UTC | 24m |
| SWA1498 | Southwest Airlines | Denver International Airport (KDEN) | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | 2026-07-03 13:14 UTC | 2026-07-03 16:12 UTC | 2h 58m |
| N78US |  | Preston Airport (KU10) | Logan-Cache Airport (KLGU) | 2026-07-03 15:53 UTC | 2026-07-03 16:11 UTC | 17m |
| N403S |  | Jonesboro Airport (KF88) | Pensacola International Airport (KPNS) | 2026-07-03 14:17 UTC | 2026-07-03 16:09 UTC | 1h 51m |
| EIN145 | Aer Lingus | Shannon Airport (EINN) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-03 09:57 UTC | 2026-07-03 16:07 UTC | 6h 10m |
| XAVTY | XAV | Del Norte International Airport (MMAN) | Del Norte International Airport (MMAN) | 2026-07-03 15:59 UTC | 2026-07-03 16:07 UTC | 7m |
| ZKICU | ZKI | Invercargill Airport (NZNV) | Taieri Airport (NZTI) | 2026-07-03 15:15 UTC | 2026-07-03 16:04 UTC | 49m |
| VOE5VE | VOE | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Bordeaux-Merignac (BA 106) Airport (LFBD) | 2026-07-03 14:22 UTC | 2026-07-03 16:02 UTC | 1h 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
