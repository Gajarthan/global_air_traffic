# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_18:54:30_UTC-green)

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

**Latest saved flight:** 2026-08-08 18:54:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 18:54:30 UTC

- **179,261** saved flights
- **57,526** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **179,261** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,154,175.5 tonnes** estimated CO2 emissions
- **124,879,741 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7110 |
| 2 | SkyWest Airlines | 6528 |
| 3 | EJA | 3530 |
| 4 | IndiGo | 3144 |
| 5 | Southwest Airlines | 2819 |
| 6 | American Airlines | 2790 |
| 7 | ENY | 2235 |
| 8 | Delta Air Lines | 2122 |
| 9 | LATAM Airlines | 1669 |
| 10 | AZU | 1602 |
| 11 | Lufthansa | 1600 |
| 12 | WIF | 1493 |
| 13 | Vueling | 1481 |
| 14 | LXJ | 1404 |
| 15 | Swiss International | 1224 |
| 16 | easyJet | 1219 |
| 17 | AXM | 1211 |
| 18 | EJU | 1093 |
| 19 | QLK | 1093 |
| 20 | All Nippon Airways | 1088 |
| 21 | Alaska Airlines | 1083 |
| 22 | VIV | 985 |
| 23 | GLO | 953 |
| 24 | Cathay Pacific | 946 |
| 25 | CXK | 945 |
| 26 | AEE | 933 |
| 27 | Air France | 922 |
| 28 | United Airlines | 920 |
| 29 | MXY | 899 |
| 30 | PGT | 889 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 153721 |
| 2 | 🇪🇸 ES | 11507 |
| 3 | 🇧🇷 BR | 10273 |
| 4 | 🇦🇺 AU | 10071 |
| 5 | 🇮🇳 IN | 9856 |
| 6 | 🇨🇦 CA | 9774 |
| 7 | 🇮🇹 IT | 9261 |
| 8 | 🇩🇪 DE | 8886 |
| 9 | 🇬🇧 GB | 8278 |
| 10 | 🇯🇵 JP | 7227 |
| 11 | 🇫🇷 FR | 7143 |
| 12 | 🇨🇴 CO | 6625 |
| 13 | 🇬🇷 GR | 5230 |
| 14 | 🇲🇽 MX | 5130 |
| 15 | 🇨🇭 CH | 4785 |
| 16 | 🇳🇴 NO | 4642 |
| 17 | 🇹🇷 TR | 4539 |
| 18 | 🇲🇾 MY | 3160 |
| 19 | 🇵🇱 PL | 2994 |
| 20 | 🇿🇦 ZA | 2922 |
| 21 | 🇹🇭 TH | 2718 |
| 22 | 🇳🇿 NZ | 2582 |
| 23 | 🇵🇭 PH | 2358 |
| 24 | 🇬🇹 GT | 2287 |
| 25 | 🇰🇷 KR | 2240 |
| 26 | 🇲🇦 MA | 1813 |
| 27 | 🇭🇷 HR | 1783 |
| 28 | 🇲🇪 ME | 1634 |
| 29 | 🇳🇱 NL | 1614 |
| 30 | 🇲🇴 MO | 1510 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3700 |
| 2 | Denver International Airport |  | US | 2962 |
| 3 | Tokyo International Airport |  | JP | 2245 |
| 4 | Guaymaral Airport |  | CO | 2207 |
| 5 | Indira Gandhi International Airport |  | IN | 2195 |
| 6 | Harry Reid International Airport |  | US | 2118 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1930 |
| 8 | Zurich Airport |  | CH | 1908 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1867 |
| 10 | La Aurora Airport |  | GT | 1758 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1637 |
| 12 | Chicago O'Hare International Airport |  | US | 1616 |
| 13 | Salt Lake City International Airport |  | US | 1601 |
| 14 | El Dorado International Airport |  | CO | 1596 |
| 15 | Frankfurt am Main International Airport |  | DE | 1563 |
| 16 | Macau International Airport |  | MO | 1510 |
| 17 | Congonhas Airport |  | BR | 1488 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1433 |
| 19 | Madrid Barajas International Airport |  | ES | 1401 |
| 20 | Capua Airport |  | IT | 1401 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1336 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1276 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1248 |
| 24 | Malpensa International Airport |  | IT | 1231 |
| 25 | Charlotte/Douglas International Airport |  | US | 1220 |
| 26 | Charles de Gaulle International Airport |  | FR | 1214 |
| 27 | Kuala Lumpur International Airport |  | MY | 1191 |
| 28 | Bengaluru International Airport |  | IN | 1175 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1114 |
| 30 | Ninoy Aquino International Airport |  | PH | 1109 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1099 |
| 32 | Barcelona International Airport |  | ES | 1064 |
| 33 | Daniel K Inouye International Airport |  | US | 1030 |
| 34 | Viracopos International Airport |  | BR | 1030 |
| 35 | Seattle-Tacoma International Airport |  | US | 1030 |
| 36 | Reno/Tahoe International Airport |  | US | 1019 |
| 37 | Calgary International Airport |  | CA | 1017 |
| 38 | Oslo Gardermoen Airport |  | NO | 996 |
| 39 | Tenerife Norte Airport |  | ES | 981 |
| 40 | Amsterdam Airport Schiphol |  | NL | 972 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 912 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 660 | 21m | 244 km | 2,779.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 420 | 1h 8m | 770 km | 5,579.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 420 | 24m | 225 km | 1,629.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 417 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 300 | 27m | 275 km | 1,421.6 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 294 | 1h 7m | 706 km | 3,579.5 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 270 | 44m | 241 km | 1,121.5 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 252 | 1h 48m | 1,423 km | 6,184.5 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 235 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 232 | 20m | 250 km | 1,002.1 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 227 | 26m | 215 km | 840.7 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 221 | 19m | 99 km | 378.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 219 | 31m | 49 km | 185.1 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 216 | 51m | 556 km | 2,070.5 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 215 | 1h 15m | 961 km | 3,563.7 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 213 | 19m | 144 km | 529.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 209 | 1h 38m | 1,156 km | 4,169.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 208 | 12m | - | - |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 206 | 31m | 369 km | 1,311.2 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 204 | 24m | 218 km | 768.5 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 202 | 28m | 152 km | 527.9 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 195 | 1h 2m | 695 km | 2,337.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N53PE |  | Aurora State Airport (KUAO) | Mcnary Field (KSLE) | 2026-08-08 18:22 UTC | 2026-08-08 18:54 UTC | 32m |
| RAM983 | Royal Air Maroc | Lisbon Portela Airport (LPPT) | Mohammed V International Airport (GMMN) | 2026-08-08 18:03 UTC | 2026-08-08 18:53 UTC | 49m |
| N608PT |  | Bob Paul Airport (FL88) | Immokalee Regional Airport (KIMM) | 2026-08-08 18:30 UTC | 2026-08-08 18:40 UTC | 10m |
| CAP499 | CAP | Gillespie Field (KSEE) | Camp Pendleton Mcas (Munn Field) Airport (KNFG) | 2026-08-08 17:59 UTC | 2026-08-08 18:35 UTC | 36m |
| N738ZA |  | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-08-08 17:12 UTC | 2026-08-08 18:35 UTC | 1h 23m |
| N7269T |  | Albuquerque International Sunport Airport (KABQ) | Sandia Airpark Estates East Airport (K1N1) | 2026-08-08 13:43 UTC | 2026-08-08 18:30 UTC | 4h 46m |
| ASI934 | ASI | Phoenix Deer Valley Airport (KDVT) | Phoenix Deer Valley Airport (KDVT) | 2026-08-08 18:03 UTC | 2026-08-08 18:30 UTC | 27m |
| N36GV |  | Iron Mountain Ranch Airport (5TE5) | Maravillas Gap Ranch Airport (48XS) | 2026-08-08 16:04 UTC | 2026-08-08 18:20 UTC | 2h 16m |
| N76KA |  | Nanaimo Airport (CYCD) | Campbell River Airport (CYBL) | 2026-08-08 17:14 UTC | 2026-08-08 18:19 UTC | 1h 5m |
| XBMLF | XBM | Tizayuca Airport (MM28) | Atizapan De Zaragoza Airport (MMJC) | 2026-08-08 17:56 UTC | 2026-08-08 18:18 UTC | 22m |
| N3563Q |  | 26LL (26LL) | IS63 (IS63) | 2026-08-08 18:17 UTC | 2026-08-08 18:18 UTC | 0m |
| AWH98B | AWH | Leipzig Halle Airport (EDDP) | Hamburg Airport (EDDH) | 2026-08-08 17:23 UTC | 2026-08-08 18:18 UTC | 55m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-08 17:33 UTC | 2026-08-08 18:16 UTC | 43m |
| LYM4210 | LYM | Denver International Airport (KDEN) | NE19 (NE19) | 2026-08-08 17:43 UTC | 2026-08-08 18:16 UTC | 32m |
| N452DD |  | Livermore Municipal Airport (KLVK) | 6CL4 (6CL4) | 2026-08-08 17:13 UTC | 2026-08-08 18:16 UTC | 1h 2m |
| THY3PC | Turkish Airlines | Istanbul Airport (LTFM) | HE42 (HE42) | 2026-08-08 16:42 UTC | 2026-08-08 18:13 UTC | 1h 30m |
| BNO91J | BNO | Oslo Gardermoen Airport (ENGM) | Trondheim Airport Vaernes (ENVA) | 2026-08-08 17:33 UTC | 2026-08-08 18:12 UTC | 39m |
| MSR758 | EgyptAir | Amsterdam Airport Schiphol (EHAM) | HE12 (HE12) | 2026-08-08 14:27 UTC | 2026-08-08 18:12 UTC | 3h 45m |
| N744DA |  | Fairbanks International Airport (PAFA) | Ruby Airport (PARY) | 2026-08-08 17:15 UTC | 2026-08-08 18:12 UTC | 57m |
| N930MG |  | Boeing Field/King County International Airport (KBFI) | Buchanan Field (KCCR) | 2026-08-08 16:40 UTC | 2026-08-08 18:11 UTC | 1h 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
