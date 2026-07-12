# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--12_06:28:31_UTC-green)

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

**Latest saved flight:** 2026-07-12 06:28:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-12 06:28:31 UTC

- **138,308** saved flights
- **46,628** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **138,308** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,661,740.9 tonnes** estimated CO2 emissions
- **96,332,805 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5626 |
| 2 | SkyWest Airlines | 5076 |
| 3 | EJA | 2714 |
| 4 | IndiGo | 2542 |
| 5 | American Airlines | 2183 |
| 6 | Southwest Airlines | 2088 |
| 7 | ENY | 1736 |
| 8 | Delta Air Lines | 1645 |
| 9 | Lufthansa | 1410 |
| 10 | LATAM Airlines | 1271 |
| 11 | Vueling | 1195 |
| 12 | WIF | 1190 |
| 13 | AZU | 1187 |
| 14 | LXJ | 1061 |
| 15 | AXM | 1035 |
| 16 | Swiss International | 984 |
| 17 | easyJet | 895 |
| 18 | All Nippon Airways | 891 |
| 19 | Alaska Airlines | 874 |
| 20 | QLK | 863 |
| 21 | EJU | 848 |
| 22 | VIV | 760 |
| 23 | AEE | 747 |
| 24 | CXK | 740 |
| 25 | Air France | 738 |
| 26 | United Airlines | 729 |
| 27 | Cathay Pacific | 727 |
| 28 | JetBlue | 727 |
| 29 | MXY | 721 |
| 30 | GLO | 708 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 118867 |
| 2 | 🇪🇸 ES | 9087 |
| 3 | 🇮🇳 IN | 7971 |
| 4 | 🇦🇺 AU | 7906 |
| 5 | 🇧🇷 BR | 7800 |
| 6 | 🇨🇦 CA | 7280 |
| 7 | 🇮🇹 IT | 7220 |
| 8 | 🇩🇪 DE | 7213 |
| 9 | 🇬🇧 GB | 6263 |
| 10 | 🇯🇵 JP | 5835 |
| 11 | 🇫🇷 FR | 5496 |
| 12 | 🇨🇴 CO | 4371 |
| 13 | 🇲🇽 MX | 4013 |
| 14 | 🇬🇷 GR | 3945 |
| 15 | 🇳🇴 NO | 3723 |
| 16 | 🇨🇭 CH | 3580 |
| 17 | 🇹🇷 TR | 3235 |
| 18 | 🇲🇾 MY | 2692 |
| 19 | 🇵🇱 PL | 2318 |
| 20 | 🇿🇦 ZA | 2264 |
| 21 | 🇳🇿 NZ | 2132 |
| 22 | 🇹🇭 TH | 2094 |
| 23 | 🇰🇷 KR | 2000 |
| 24 | 🇵🇭 PH | 1885 |
| 25 | 🇬🇹 GT | 1839 |
| 26 | 🇲🇦 MA | 1455 |
| 27 | 🇲🇪 ME | 1371 |
| 28 | 🇳🇱 NL | 1290 |
| 29 | 🇭🇷 HR | 1254 |
| 30 | 🇲🇴 MO | 1188 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2870 |
| 2 | Denver International Airport |  | US | 2321 |
| 3 | Tokyo International Airport |  | JP | 1899 |
| 4 | Indira Gandhi International Airport |  | IN | 1761 |
| 5 | Harry Reid International Airport |  | US | 1728 |
| 6 | Guaymaral Airport |  | CO | 1684 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1603 |
| 8 | Zurich Airport |  | CH | 1534 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1458 |
| 10 | La Aurora Airport |  | GT | 1421 |
| 11 | Frankfurt am Main International Airport |  | DE | 1367 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1326 |
| 13 | Chicago O'Hare International Airport |  | US | 1306 |
| 14 | El Dorado International Airport |  | CO | 1231 |
| 15 | Salt Lake City International Airport |  | US | 1227 |
| 16 | Macau International Airport |  | MO | 1188 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1187 |
| 18 | Capua Airport |  | IT | 1136 |
| 19 | Madrid Barajas International Airport |  | ES | 1125 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1117 |
| 21 | Congonhas Airport |  | BR | 1113 |
| 22 | Kuala Lumpur International Airport |  | MY | 1043 |
| 23 | Charlotte/Douglas International Airport |  | US | 1013 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 996 |
| 25 | Charles de Gaulle International Airport |  | FR | 982 |
| 26 | Bengaluru International Airport |  | IN | 959 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 953 |
| 28 | Malpensa International Airport |  | IT | 903 |
| 29 | Ninoy Aquino International Airport |  | PH | 877 |
| 30 | Daniel K Inouye International Airport |  | US | 851 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 842 |
| 32 | Barcelona International Airport |  | ES | 840 |
| 33 | Tenerife Norte Airport |  | ES | 812 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 811 |
| 35 | Calgary International Airport |  | CA | 801 |
| 36 | Viracopos International Airport |  | BR | 791 |
| 37 | Scottsdale Airport |  | US | 791 |
| 38 | Seattle-Tacoma International Airport |  | US | 788 |
| 39 | Vitoria/Foronda Airport |  | ES | 775 |
| 40 | Amsterdam Airport Schiphol |  | NL | 775 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 709 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 501 | 21m | 244 km | 2,109.6 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 340 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 339 | 24m | 225 km | 1,315.2 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 330 | 1h 9m | 770 km | 4,383.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 297 | 14m | 114 km | 582.5 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 258 | 26m | 275 km | 1,222.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 251 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 206 | 22m | 55 km | 195.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 189 | 26m | 215 km | 700.0 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 189 | 44m | 241 km | 785.1 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 187 | 1h 46m | 1,423 km | 4,589.3 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 185 | 20m | 99 km | 316.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 182 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 173 | 20m | 250 km | 747.3 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 169 | 31m | 369 km | 1,075.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 166 | 18m | 144 km | 412.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 163 | 44m | 452 km | 1,270.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 161 | 1h 16m | 961 km | 2,668.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 159 | 1h 1m | 695 km | 1,905.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 156 | 1h 38m | 1,156 km | 3,112.1 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 152 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DLH796 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Zhuhai Airport (ZGSD) | 2026-07-11 20:07 UTC | 2026-07-12 06:28 UTC | 10h 20m |
| MAS788 | Malaysia Airlines | Kuala Lumpur International Airport (WMKK) | Khok Kathiam Airport (VTBL) | 2026-07-12 04:31 UTC | 2026-07-12 06:19 UTC | 1h 47m |
| CFL04 | CFL | Palmerston North Airport (NZPM) | Palmerston North Airport (NZPM) | 2026-07-12 06:14 UTC | 2026-07-12 06:15 UTC | 1m |
| UBG201 | UBG | VGZR (VGZR) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-07-12 05:28 UTC | 2026-07-12 06:14 UTC | 45m |
|  |  | Philadelphia International Airport (KPHL) | Philadelphia International Airport (KPHL) | 2026-07-12 01:22 UTC | 2026-07-12 06:02 UTC | 4h 39m |
| FJIRZ | FJI | Toulouse-Lasbordes Airport (LFCL) | Toulouse-Lasbordes Airport (LFCL) | 2026-07-12 05:33 UTC | 2026-07-12 06:01 UTC | 28m |
| SWR3ZC | Swiss International | Geneva Cointrin International Airport (LSGG) | Zurich Airport (LSZH) | 2026-07-12 05:26 UTC | 2026-07-12 06:00 UTC | 33m |
| RYR399Y | Ryanair | Copenhagen Kastrup Airport (EKCH) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-07-12 04:42 UTC | 2026-07-12 05:58 UTC | 1h 16m |
| KLM64F | KLM Royal Dutch | Warsaw Chopin Airport (EPWA) | Amsterdam Airport Schiphol (EHAM) | 2026-07-12 04:12 UTC | 2026-07-12 05:46 UTC | 1h 34m |
| AEW1049 | AEW | Eleftherios Venizelos International Airport (LGAV) | Adnan Menderes International Airport (LTBJ) | 2026-07-12 05:20 UTC | 2026-07-12 05:45 UTC | 25m |
| RYR33ZW | Ryanair | Nuremberg Airport (EDDN) | Sofia Airport (LBSF) | 2026-07-12 04:13 UTC | 2026-07-12 05:42 UTC | 1h 29m |
| RXA2125 | RXA | Perth International Airport (YPPH) | Frankland Airport (YFRK) | 2026-07-12 04:51 UTC | 2026-07-12 05:39 UTC | 48m |
| RYR3GD | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Capua Airport (LIAU) | 2026-07-12 04:48 UTC | 2026-07-12 05:34 UTC | 46m |
| VAA010 | VAA | Mukhrani Airport (UGMM) | UGMS (UGMS) | 2026-07-12 04:59 UTC | 2026-07-12 05:29 UTC | 30m |
| DLA54M | DLA | Graz Airport (LOWG) | Frankfurt am Main International Airport (EDDF) | 2026-07-12 04:09 UTC | 2026-07-12 05:29 UTC | 1h 19m |
| WZZ5AN | Wizz Air | Belgrade Nikola Tesla Airport (LYBE) | Khrabrovo Airport (UMKK) | 2026-07-12 03:55 UTC | 2026-07-12 05:28 UTC | 1h 32m |
|  |  | Coventry Airport (EGBE) | Chichester/Goodwood Airport (EGHR) | 2026-07-12 05:15 UTC | 2026-07-12 05:28 UTC | 12m |
| QLK171D | QLK | Brisbane International Airport (YBBN) | Port Macquarie Airport (YPMQ) | 2026-07-12 04:25 UTC | 2026-07-12 05:20 UTC | 54m |
| RYR53RZ | Ryanair | Václav Havel Airport (LKPR) | Otocac Airport (LDRO) | 2026-07-12 04:26 UTC | 2026-07-12 05:17 UTC | 51m |
| AXM6490 | AXM | Kota Kinabalu International Airport (WBKK) | Ranau Airport (WBKR) | 2026-07-12 05:05 UTC | 2026-07-12 05:16 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
