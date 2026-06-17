# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--17_17:21:22_UTC-green)

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

**Latest saved flight:** 2026-06-17 17:21:22 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-17 17:21:22 UTC

- **113,295** saved flights
- **39,369** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **113,295** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,380,672.9 tonnes** estimated CO2 emissions
- **80,039,011 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4666 |
| 2 | SkyWest Airlines | 4213 |
| 3 | EJA | 2198 |
| 4 | IndiGo | 2197 |
| 5 | American Airlines | 1785 |
| 6 | Southwest Airlines | 1686 |
| 7 | ENY | 1412 |
| 8 | Delta Air Lines | 1339 |
| 9 | Lufthansa | 1270 |
| 10 | Vueling | 1032 |
| 11 | WIF | 1003 |
| 12 | LATAM Airlines | 999 |
| 13 | AZU | 947 |
| 14 | AXM | 945 |
| 15 | LXJ | 862 |
| 16 | Swiss International | 809 |
| 17 | All Nippon Airways | 786 |
| 18 | Alaska Airlines | 766 |
| 19 | QLK | 739 |
| 20 | easyJet | 730 |
| 21 | EJU | 716 |
| 22 | Cathay Pacific | 665 |
| 23 | AEE | 635 |
| 24 | Air France | 629 |
| 25 | VIV | 629 |
| 26 | United Airlines | 627 |
| 27 | CXK | 600 |
| 28 | MXY | 600 |
| 29 | GLO | 557 |
| 30 | AXB | 556 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 95505 |
| 2 | 🇪🇸 ES | 7744 |
| 3 | 🇮🇳 IN | 6936 |
| 4 | 🇦🇺 AU | 6722 |
| 5 | 🇧🇷 BR | 6272 |
| 6 | 🇮🇹 IT | 6083 |
| 7 | 🇩🇪 DE | 6065 |
| 8 | 🇨🇦 CA | 5953 |
| 9 | 🇯🇵 JP | 5112 |
| 10 | 🇬🇧 GB | 4894 |
| 11 | 🇫🇷 FR | 4514 |
| 12 | 🇨🇴 CO | 3842 |
| 13 | 🇲🇽 MX | 3351 |
| 14 | 🇬🇷 GR | 3221 |
| 15 | 🇳🇴 NO | 3133 |
| 16 | 🇨🇭 CH | 2899 |
| 17 | 🇲🇾 MY | 2443 |
| 18 | 🇹🇷 TR | 2270 |
| 19 | 🇿🇦 ZA | 1923 |
| 20 | 🇰🇷 KR | 1868 |
| 21 | 🇳🇿 NZ | 1856 |
| 22 | 🇵🇱 PL | 1848 |
| 23 | 🇹🇭 TH | 1843 |
| 24 | 🇵🇭 PH | 1651 |
| 25 | 🇬🇹 GT | 1616 |
| 26 | 🇲🇦 MA | 1242 |
| 27 | 🇲🇴 MO | 1161 |
| 28 | 🇲🇪 ME | 1109 |
| 29 | 🇳🇱 NL | 1099 |
| 30 | 🇭🇷 HR | 986 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2412 |
| 2 | Denver International Airport |  | US | 1914 |
| 3 | Tokyo International Airport |  | JP | 1697 |
| 4 | Indira Gandhi International Airport |  | IN | 1511 |
| 5 | Guaymaral Airport |  | CO | 1425 |
| 6 | Harry Reid International Airport |  | US | 1420 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1393 |
| 8 | Zurich Airport |  | CH | 1273 |
| 9 | La Aurora Airport |  | GT | 1245 |
| 10 | Frankfurt am Main International Airport |  | DE | 1239 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1220 |
| 12 | Macau International Airport |  | MO | 1161 |
| 13 | El Dorado International Airport |  | CO | 1149 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1132 |
| 15 | Chicago O'Hare International Airport |  | US | 1122 |
| 16 | Capua Airport |  | IT | 984 |
| 17 | Madrid Barajas International Airport |  | ES | 979 |
| 18 | Salt Lake City International Airport |  | US | 958 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 951 |
| 20 | Kuala Lumpur International Airport |  | MY | 947 |
| 21 | Charlotte/Douglas International Airport |  | US | 880 |
| 22 | Congonhas Airport |  | BR | 872 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 845 |
| 24 | Charles de Gaulle International Airport |  | FR | 841 |
| 25 | Bengaluru International Airport |  | IN | 839 |
| 26 | Malpensa International Airport |  | IT | 817 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 792 |
| 28 | Ninoy Aquino International Airport |  | PH | 761 |
| 29 | Daniel K Inouye International Airport |  | US | 745 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 744 |
| 31 | Tenerife Norte Airport |  | ES | 740 |
| 32 | Barcelona International Airport |  | ES | 733 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 715 |
| 34 | Don Mueang International Airport |  | TH | 672 |
| 35 | Amsterdam Airport Schiphol |  | NL | 672 |
| 36 | Vitoria/Foronda Airport |  | ES | 671 |
| 37 | Calgary International Airport |  | CA | 667 |
| 38 | Seattle-Tacoma International Airport |  | US | 651 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 648 |
| 40 | Viracopos International Airport |  | BR | 647 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 591 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 411 | 21m | 244 km | 1,730.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 301 | 24m | 225 km | 1,167.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 294 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 284 | 1h 7m | 706 km | 3,457.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 277 | 1h 25m | 910 km | 4,346.8 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 276 | 14m | 114 km | 541.3 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 270 | 1h 10m | 770 km | 3,586.7 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 227 | 26m | 275 km | 1,075.7 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 225 | 19m | 165 km | 640.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 211 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 168 | 20m | 99 km | 287.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 166 | 26m | 215 km | 614.8 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 164 | 22m | 55 km | 155.9 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 162 | 13m | - | - |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 155 | 27m | 152 km | 405.1 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 153 | 31m | 369 km | 973.9 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 150 | 44m | 452 km | 1,169.0 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 22 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 146 | 44m | 241 km | 606.5 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 144 | 20m | 250 km | 622.0 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 136 | 1h 1m | 695 km | 1,630.2 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 133 | 1h 43m | 1,423 km | 3,264.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 133 | 1h 39m | 1,156 km | 2,653.3 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 127 | 1h 17m | 961 km | 2,105.1 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 127 | 12m | - | - |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 126 | 24m | 223 km | 484.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HUE12P | HUE | Zurich Airport (LSZH) | Friedrichshafen Airport (EDNY) | 2026-06-17 16:52 UTC | 2026-06-17 17:21 UTC | 29m |
| N636KT |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-06-17 16:37 UTC | 2026-06-17 17:19 UTC | 42m |
| N1577S |  | Bill Pugh Field (KM22) | Bill Pugh Field (KM22) | 2026-06-17 17:00 UTC | 2026-06-17 17:15 UTC | 14m |
| N642RG |  | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-06-17 16:31 UTC | 2026-06-17 17:12 UTC | 41m |
| N940LH |  | Dallas Executive Airport (KRBD) | Mid-Way Regional Airport (KJWY) | 2026-06-17 16:58 UTC | 2026-06-17 17:12 UTC | 14m |
| ARCAS11 | ARC | Danaher Airport (7TX0) | TX20 (TX20) | 2026-06-17 16:55 UTC | 2026-06-17 17:10 UTC | 15m |
| N734HX |  | Knox County Regional Airport (KRKD) | Vinalhaven Airport (ME55) | 2026-06-17 16:57 UTC | 2026-06-17 17:06 UTC | 8m |
| JYRJK | JYR | Amman-Marka International Airport (OJAM) | Queen Alia International Airport (OJAI) | 2026-06-17 16:41 UTC | 2026-06-17 17:06 UTC | 25m |
| N691HS |  | Quonset State Airport (KOQU) | Block Island State Airport (KBID) | 2026-06-17 16:47 UTC | 2026-06-17 17:05 UTC | 18m |
| JEDI33 | JED | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Shade Tree Field (MS82) | 2026-06-17 16:37 UTC | 2026-06-17 17:05 UTC | 27m |
| CGFHA | CGF | Vancouver International Airport (CYVR) | Pitt Meadows Airport (CYPK) | 2026-06-17 16:47 UTC | 2026-06-17 17:04 UTC | 17m |
| N1118Q |  | Skypark Airport (KBTF) | Nephi Municipal Airport (KU14) | 2026-06-17 16:27 UTC | 2026-06-17 17:04 UTC | 36m |
| N287BG |  | Leesburg International Airport (KLEE) | Leesburg International Airport (KLEE) | 2026-06-17 16:59 UTC | 2026-06-17 17:03 UTC | 4m |
| N15190 |  | Groton-New London Airport (KGON) | New Bedford Regional Airport (KEWB) | 2026-06-17 16:33 UTC | 2026-06-17 17:02 UTC | 28m |
| C6040 |  | San Diego International Airport (KSAN) | San Diego International Airport (KSAN) | 2026-06-17 15:36 UTC | 2026-06-17 17:01 UTC | 1h 25m |
| CXK669 | CXK | Raleigh-Durham International Airport (KRDU) | Triangle North Executive Airport (KLHZ) | 2026-06-17 16:19 UTC | 2026-06-17 17:01 UTC | 42m |
| C2703 |  | Mc Clellan Airfield (KMCC) | Bear Valley Airport (73CA) | 2026-06-17 16:35 UTC | 2026-06-17 16:58 UTC | 23m |
| SWR98G | Swiss International | Henri Coanda International Airport (LROP) | Zurich Airport (LSZH) | 2026-06-17 13:48 UTC | 2026-06-17 16:57 UTC | 3h 8m |
| N260RD |  | Madrid Air Base (SKMA) | Guaymaral Airport (SKGY) | 2026-06-17 16:42 UTC | 2026-06-17 16:55 UTC | 12m |
| N8116N |  | CL24 (CL24) | Lake Tahoe Airport (KTVL) | 2026-06-17 16:24 UTC | 2026-06-17 16:50 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
