# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_03:18:46_UTC-green)

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

**Latest saved flight:** 2026-06-21 03:18:46 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-21 03:18:46 UTC

- **115,922** saved flights
- **40,146** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **115,922** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,409,445.7 tonnes** estimated CO2 emissions
- **81,706,995 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4777 |
| 2 | SkyWest Airlines | 4309 |
| 3 | EJA | 2246 |
| 4 | IndiGo | 2239 |
| 5 | American Airlines | 1812 |
| 6 | Southwest Airlines | 1726 |
| 7 | ENY | 1445 |
| 8 | Delta Air Lines | 1369 |
| 9 | Lufthansa | 1283 |
| 10 | Vueling | 1045 |
| 11 | WIF | 1024 |
| 12 | LATAM Airlines | 1019 |
| 13 | AZU | 966 |
| 14 | AXM | 955 |
| 15 | LXJ | 882 |
| 16 | Swiss International | 817 |
| 17 | All Nippon Airways | 794 |
| 18 | Alaska Airlines | 778 |
| 19 | QLK | 751 |
| 20 | easyJet | 742 |
| 21 | EJU | 728 |
| 22 | Cathay Pacific | 672 |
| 23 | AEE | 650 |
| 24 | VIV | 643 |
| 25 | United Airlines | 642 |
| 26 | Air France | 635 |
| 27 | CXK | 619 |
| 28 | MXY | 613 |
| 29 | AXB | 570 |
| 30 | GLO | 566 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 97951 |
| 2 | 🇪🇸 ES | 7895 |
| 3 | 🇮🇳 IN | 7057 |
| 4 | 🇦🇺 AU | 6880 |
| 5 | 🇧🇷 BR | 6384 |
| 6 | 🇮🇹 IT | 6197 |
| 7 | 🇩🇪 DE | 6176 |
| 8 | 🇨🇦 CA | 6090 |
| 9 | 🇯🇵 JP | 5203 |
| 10 | 🇬🇧 GB | 5039 |
| 11 | 🇫🇷 FR | 4599 |
| 12 | 🇨🇴 CO | 3985 |
| 13 | 🇲🇽 MX | 3418 |
| 14 | 🇬🇷 GR | 3306 |
| 15 | 🇳🇴 NO | 3186 |
| 16 | 🇨🇭 CH | 2956 |
| 17 | 🇲🇾 MY | 2475 |
| 18 | 🇹🇷 TR | 2346 |
| 19 | 🇿🇦 ZA | 1948 |
| 20 | 🇳🇿 NZ | 1903 |
| 21 | 🇵🇱 PL | 1901 |
| 22 | 🇰🇷 KR | 1883 |
| 23 | 🇹🇭 TH | 1882 |
| 24 | 🇵🇭 PH | 1690 |
| 25 | 🇬🇹 GT | 1637 |
| 26 | 🇲🇦 MA | 1259 |
| 27 | 🇲🇴 MO | 1169 |
| 28 | 🇲🇪 ME | 1141 |
| 29 | 🇳🇱 NL | 1118 |
| 30 | 🇭🇷 HR | 1005 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2448 |
| 2 | Denver International Airport |  | US | 1954 |
| 3 | Tokyo International Airport |  | JP | 1724 |
| 4 | Indira Gandhi International Airport |  | IN | 1547 |
| 5 | Guaymaral Airport |  | CO | 1475 |
| 6 | Harry Reid International Airport |  | US | 1453 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1419 |
| 8 | Zurich Airport |  | CH | 1289 |
| 9 | La Aurora Airport |  | GT | 1264 |
| 10 | Frankfurt am Main International Airport |  | DE | 1254 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1239 |
| 12 | El Dorado International Airport |  | CO | 1171 |
| 13 | Macau International Airport |  | MO | 1169 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1156 |
| 15 | Chicago O'Hare International Airport |  | US | 1140 |
| 16 | Capua Airport |  | IT | 1009 |
| 17 | Salt Lake City International Airport |  | US | 996 |
| 18 | Madrid Barajas International Airport |  | ES | 985 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 968 |
| 20 | Kuala Lumpur International Airport |  | MY | 955 |
| 21 | Congonhas Airport |  | BR | 887 |
| 22 | Charlotte/Douglas International Airport |  | US | 887 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 865 |
| 24 | Bengaluru International Airport |  | IN | 855 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 853 |
| 26 | Charles de Gaulle International Airport |  | FR | 848 |
| 27 | Malpensa International Airport |  | IT | 825 |
| 28 | Ninoy Aquino International Airport |  | PH | 780 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 758 |
| 30 | Daniel K Inouye International Airport |  | US | 757 |
| 31 | Tenerife Norte Airport |  | ES | 752 |
| 32 | Barcelona International Airport |  | ES | 739 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 731 |
| 34 | Vitoria/Foronda Airport |  | ES | 684 |
| 35 | Don Mueang International Airport |  | TH | 683 |
| 36 | Calgary International Airport |  | CA | 680 |
| 37 | Amsterdam Airport Schiphol |  | NL | 679 |
| 38 | Seattle-Tacoma International Airport |  | US | 667 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 660 |
| 40 | Scottsdale Airport |  | US | 659 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 612 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 422 | 21m | 244 km | 1,776.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 311 | 24m | 225 km | 1,206.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 299 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 284 | 1h 25m | 910 km | 4,456.6 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 276 | 1h 10m | 770 km | 3,666.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 231 | 26m | 275 km | 1,094.6 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 228 | 19m | 165 km | 648.6 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 216 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 174 | 22m | 55 km | 165.4 t |
| 14 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 168 | 20m | 99 km | 287.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 167 | 26m | 215 km | 618.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 157 | 27m | 152 km | 410.3 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 154 | 31m | 369 km | 980.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 152 | 44m | 452 km | 1,184.6 t |
| 21 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 152 | 44m | 241 km | 631.4 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 147 | 20m | 250 km | 635.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 142 | 1h 44m | 1,423 km | 3,484.9 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 139 | 1h 1m | 695 km | 1,666.2 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 135 | 1h 39m | 1,156 km | 2,693.2 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 132 | 1h 17m | 961 km | 2,188.0 t |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 129 | 24m | 223 km | 496.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-06-21 03:01 UTC | 2026-06-21 03:18 UTC | 17m |
| N1213S |  | Cortes Island (Hansen Airfield) Airport (CCI9) | Boeing Field/King County International Airport (KBFI) | 2026-06-21 02:15 UTC | 2026-06-21 03:18 UTC | 1h 3m |
| DTCHMN41 | DTC | Imperial Beach Nolf (Ream Field) Airport (KNRS) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-06-21 01:08 UTC | 2026-06-21 02:55 UTC | 1h 47m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-06-21 02:33 UTC | 2026-06-21 02:50 UTC | 16m |
| EJA469 | EJA | Eppley Airfield (KOMA) | Santa Fe Regional Airport (KSAF) | 2026-06-21 00:53 UTC | 2026-06-21 02:50 UTC | 1h 56m |
| 8GL |  | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-06-21 01:41 UTC | 2026-06-21 02:43 UTC | 1h 2m |
| LLR821 | LLR | Indira Gandhi International Airport (VIDP) | Kalka Airport (VI71) | 2026-06-21 02:10 UTC | 2026-06-21 02:43 UTC | 32m |
| AXM6415 | AXM | Taiping (Tekah) Airport (WMBI) | Batu Pahat Airport (WMAB) | 2026-06-21 02:08 UTC | 2026-06-21 02:42 UTC | 33m |
| A07 |  | Doha International Airport (OTBD) | Doha International Airport (OTBD) | 2026-06-21 02:15 UTC | 2026-06-21 02:34 UTC | 18m |
| ANA1262 | All Nippon Airways | New Chitose Airport (RJCC) | Mt. Fuji Shizuoka Airport (RJNS) | 2026-06-21 01:16 UTC | 2026-06-21 02:31 UTC | 1h 15m |
| AM320 |  | Melbourne Essendon Airport (YMEN) | Sale Airport (YSLT) | 2026-06-21 01:58 UTC | 2026-06-21 02:26 UTC | 27m |
| VAR512 | VAR | Phoenix Goodyear Airport (KGYR) | Julian Hinds Pump Plant Airstrip (73CL) | 2026-06-21 01:08 UTC | 2026-06-21 02:25 UTC | 1h 16m |
| SRQ6129 | SRQ | Diosdado Macapagal International Airport (RPLC) | Bulan Airport (RPUU) | 2026-06-21 01:31 UTC | 2026-06-21 02:18 UTC | 46m |
| ANZ268L | ANZ | Auckland International Airport (NZAA) | Whangarei Airport (NZWR) | 2026-06-21 01:53 UTC | 2026-06-21 02:17 UTC | 24m |
| AIQ3201 | AIQ | Don Mueang International Airport (VTBD) | Kengtung Airport (VYKG) | 2026-06-21 01:29 UTC | 2026-06-21 02:17 UTC | 48m |
| QLK322D | QLK | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-06-21 01:43 UTC | 2026-06-21 02:16 UTC | 33m |
| SNJ33 | SNJ | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 2026-06-21 00:50 UTC | 2026-06-21 02:16 UTC | 1h 25m |
| RXA6123 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Cooma/Polo Flat (Unlic) Airport (YPFT) | 2026-06-21 01:33 UTC | 2026-06-21 02:15 UTC | 41m |
| BHA951 | BHA | Tribhuvan International Airport (VNKT) | Bhojpur Airport (VNBJ) | 2026-06-21 01:48 UTC | 2026-06-21 02:11 UTC | 22m |
| N1076K |  | Las Cruces International Airport (KLRU) | Mystic Bluffs Airport (NM56) | 2026-06-21 01:09 UTC | 2026-06-21 02:08 UTC | 58m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
