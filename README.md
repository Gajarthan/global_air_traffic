# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--23_00:56:42_UTC-green)

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

**Latest saved flight:** 2026-07-23 00:56:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-23 00:56:42 UTC

- **145,041** saved flights
- **48,556** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **145,041** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,738,197.5 tonnes** estimated CO2 emissions
- **100,765,072 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5889 |
| 2 | SkyWest Airlines | 5316 |
| 3 | EJA | 2861 |
| 4 | IndiGo | 2624 |
| 5 | American Airlines | 2321 |
| 6 | Southwest Airlines | 2193 |
| 7 | ENY | 1808 |
| 8 | Delta Air Lines | 1720 |
| 9 | Lufthansa | 1444 |
| 10 | LATAM Airlines | 1338 |
| 11 | AZU | 1250 |
| 12 | WIF | 1237 |
| 13 | Vueling | 1236 |
| 14 | LXJ | 1117 |
| 15 | AXM | 1063 |
| 16 | Swiss International | 1029 |
| 17 | easyJet | 942 |
| 18 | All Nippon Airways | 924 |
| 19 | Alaska Airlines | 914 |
| 20 | QLK | 910 |
| 21 | EJU | 886 |
| 22 | VIV | 808 |
| 23 | CXK | 777 |
| 24 | AEE | 766 |
| 25 | JetBlue | 766 |
| 26 | Air France | 764 |
| 27 | MXY | 760 |
| 28 | Cathay Pacific | 757 |
| 29 | United Airlines | 754 |
| 30 | GLO | 744 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 125089 |
| 2 | 🇪🇸 ES | 9393 |
| 3 | 🇦🇺 AU | 8287 |
| 4 | 🇮🇳 IN | 8219 |
| 5 | 🇧🇷 BR | 8193 |
| 6 | 🇨🇦 CA | 7709 |
| 7 | 🇮🇹 IT | 7540 |
| 8 | 🇩🇪 DE | 7468 |
| 9 | 🇬🇧 GB | 6605 |
| 10 | 🇯🇵 JP | 6053 |
| 11 | 🇫🇷 FR | 5756 |
| 12 | 🇨🇴 CO | 4741 |
| 13 | 🇲🇽 MX | 4227 |
| 14 | 🇬🇷 GR | 4100 |
| 15 | 🇳🇴 NO | 3869 |
| 16 | 🇨🇭 CH | 3753 |
| 17 | 🇹🇷 TR | 3402 |
| 18 | 🇲🇾 MY | 2776 |
| 19 | 🇵🇱 PL | 2441 |
| 20 | 🇿🇦 ZA | 2350 |
| 21 | 🇳🇿 NZ | 2218 |
| 22 | 🇹🇭 TH | 2130 |
| 23 | 🇰🇷 KR | 2042 |
| 24 | 🇵🇭 PH | 1935 |
| 25 | 🇬🇹 GT | 1887 |
| 26 | 🇲🇦 MA | 1503 |
| 27 | 🇲🇪 ME | 1440 |
| 28 | 🇳🇱 NL | 1357 |
| 29 | 🇭🇷 HR | 1320 |
| 30 | 🇲🇴 MO | 1212 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2999 |
| 2 | Denver International Airport |  | US | 2430 |
| 3 | Tokyo International Airport |  | JP | 1945 |
| 4 | Indira Gandhi International Airport |  | IN | 1824 |
| 5 | Harry Reid International Airport |  | US | 1821 |
| 6 | Guaymaral Airport |  | CO | 1777 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1644 |
| 8 | Zurich Airport |  | CH | 1601 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1523 |
| 10 | La Aurora Airport |  | GT | 1462 |
| 11 | Frankfurt am Main International Airport |  | DE | 1392 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1370 |
| 13 | Chicago O'Hare International Airport |  | US | 1350 |
| 14 | Salt Lake City International Airport |  | US | 1304 |
| 15 | El Dorado International Airport |  | CO | 1296 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1262 |
| 17 | Macau International Airport |  | MO | 1212 |
| 18 | Capua Airport |  | IT | 1179 |
| 19 | Congonhas Airport |  | BR | 1166 |
| 20 | Madrid Barajas International Airport |  | ES | 1155 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1145 |
| 22 | Kuala Lumpur International Airport |  | MY | 1072 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1049 |
| 24 | Charlotte/Douglas International Airport |  | US | 1041 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1014 |
| 26 | Charles de Gaulle International Airport |  | FR | 1009 |
| 27 | Bengaluru International Airport |  | IN | 981 |
| 28 | Malpensa International Airport |  | IT | 936 |
| 29 | Ninoy Aquino International Airport |  | PH | 904 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 889 |
| 31 | Barcelona International Airport |  | ES | 880 |
| 32 | Daniel K Inouye International Airport |  | US | 878 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 863 |
| 34 | Tenerife Norte Airport |  | ES | 829 |
| 35 | Seattle-Tacoma International Airport |  | US | 826 |
| 36 | Viracopos International Airport |  | BR | 825 |
| 37 | Calgary International Airport |  | CA | 824 |
| 38 | Scottsdale Airport |  | US | 823 |
| 39 | Amsterdam Airport Schiphol |  | NL | 817 |
| 40 | Oslo Gardermoen Airport |  | NO | 795 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 749 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 527 | 21m | 244 km | 2,219.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 351 | 24m | 225 km | 1,361.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 351 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 340 | 1h 9m | 770 km | 4,516.6 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 261 | 26m | 275 km | 1,236.8 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 257 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 217 | 22m | 55 km | 206.3 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 194 | 26m | 215 km | 718.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 193 | 1h 46m | 1,423 km | 4,736.5 t |
| 16 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 193 | 44m | 241 km | 801.7 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 192 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 179 | 20m | 250 km | 773.2 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 179 | 28m | 152 km | 467.8 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 173 | 18m | 144 km | 430.3 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 168 | 44m | 452 km | 1,309.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 168 | 1h 16m | 961 km | 2,784.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 166 | 1h 1m | 695 km | 1,989.8 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 165 | 1h 39m | 1,156 km | 3,291.7 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 165 | 13m | - | - |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZKHZM | ZKH | Christchurch International Airport (NZCH) | West Melton Aerodrome (NZWL) | 2026-07-23 00:30 UTC | 2026-07-23 00:56 UTC | 25m |
| SHWK769 | SHW | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-07-23 00:37 UTC | 2026-07-23 00:51 UTC | 14m |
| N724LU |  | Lynchburg Regional/Preston Glenn Field (KLYH) | 94VA (94VA) | 2026-07-23 00:40 UTC | 2026-07-23 00:51 UTC | 11m |
| N8478R |  | Lovell Field (KCHA) | K3M3 (K3M3) | 2026-07-23 00:02 UTC | 2026-07-23 00:51 UTC | 48m |
| PFA333 | PFA | Broocke Air Patch Airport (FL95) | Space Coast Regional Airport (KTIX) | 2026-07-23 00:05 UTC | 2026-07-23 00:50 UTC | 44m |
| N5184L |  | Custer Airport (KTTF) | Fulton County Airport (KUSE) | 2026-07-23 00:25 UTC | 2026-07-23 00:48 UTC | 22m |
| TOGO42 | TOG | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-07-23 00:27 UTC | 2026-07-23 00:46 UTC | 19m |
| LVW202 | LVW | Victoria International Airport (CYYJ) | Vancouver International Airport (CYVR) | 2026-07-23 00:18 UTC | 2026-07-23 00:45 UTC | 26m |
| EJM325 | EJM | Washington Dulles International Airport (KIAD) | St Pete-Clearwater International Airport (KPIE) | 2026-07-22 22:48 UTC | 2026-07-23 00:40 UTC | 1h 52m |
| YGN | YGN | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-07-23 00:02 UTC | 2026-07-23 00:38 UTC | 36m |
| DTCHMN42 | DTC | Bob Maxwell Memorial Airfield (KOKB) | San Clemente Island Nalf Airport (KNUC) | 2026-07-22 22:30 UTC | 2026-07-23 00:34 UTC | 2h 3m |
| CFJSJ | CFJ | Oshawa Airport (CYOO) | Oshawa Airport (CYOO) | 2026-07-23 00:04 UTC | 2026-07-23 00:33 UTC | 29m |
| YHJ | YHJ | RAAF Williams Point Cook Base (YMPC) | Melbourne Moorabbin Airport (YMMB) | 2026-07-23 00:15 UTC | 2026-07-23 00:30 UTC | 15m |
| N52219 |  | Oakland/Troy Airport (KVLL) | Lenawee County Airport (KADG) | 2026-07-22 23:27 UTC | 2026-07-23 00:29 UTC | 1h 2m |
| HHC | HHC | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-07-23 00:22 UTC | 2026-07-23 00:26 UTC | 4m |
| N202WG |  | Indiana County/Jimmy Stewart Field (KIDI) | Indiana County/Jimmy Stewart Field (KIDI) | 2026-07-23 00:21 UTC | 2026-07-23 00:26 UTC | 4m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-07-23 00:16 UTC | 2026-07-23 00:22 UTC | 6m |
| N121BZ |  | 3TE6 (3TE6) | Lundin Airport (SD94) | 2026-07-22 22:54 UTC | 2026-07-23 00:14 UTC | 1h 19m |
| FGD551 | FGD | Prince George Airport (CYXS) | Beaverley Airport (CBA8) | 2026-07-23 00:04 UTC | 2026-07-23 00:11 UTC | 7m |
| N16046 |  | Lenawee County Airport (KADG) | Lenawee County Airport (KADG) | 2026-07-22 23:38 UTC | 2026-07-23 00:09 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
