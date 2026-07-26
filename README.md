# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--26_23:00:02_UTC-green)

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

**Latest saved flight:** 2026-07-26 23:00:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-26 23:00:02 UTC

- **153,457** saved flights
- **50,892** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **153,457** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,835,677.2 tonnes** estimated CO2 emissions
- **106,416,070 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6196 |
| 2 | SkyWest Airlines | 5620 |
| 3 | EJA | 3045 |
| 4 | IndiGo | 2729 |
| 5 | American Airlines | 2435 |
| 6 | Southwest Airlines | 2334 |
| 7 | ENY | 1921 |
| 8 | Delta Air Lines | 1799 |
| 9 | Lufthansa | 1488 |
| 10 | LATAM Airlines | 1427 |
| 11 | AZU | 1339 |
| 12 | WIF | 1290 |
| 13 | Vueling | 1281 |
| 14 | LXJ | 1184 |
| 15 | AXM | 1090 |
| 16 | Swiss International | 1072 |
| 17 | easyJet | 1003 |
| 18 | All Nippon Airways | 960 |
| 19 | Alaska Airlines | 955 |
| 20 | EJU | 943 |
| 21 | QLK | 943 |
| 22 | VIV | 847 |
| 23 | CXK | 820 |
| 24 | MXY | 809 |
| 25 | AEE | 807 |
| 26 | GLO | 801 |
| 27 | Air France | 798 |
| 28 | JetBlue | 794 |
| 29 | United Airlines | 787 |
| 30 | Cathay Pacific | 784 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 132419 |
| 2 | 🇪🇸 ES | 9913 |
| 3 | 🇧🇷 BR | 8735 |
| 4 | 🇦🇺 AU | 8615 |
| 5 | 🇮🇳 IN | 8579 |
| 6 | 🇨🇦 CA | 8220 |
| 7 | 🇮🇹 IT | 7942 |
| 8 | 🇩🇪 DE | 7828 |
| 9 | 🇬🇧 GB | 7035 |
| 10 | 🇯🇵 JP | 6314 |
| 11 | 🇫🇷 FR | 6072 |
| 12 | 🇨🇴 CO | 5266 |
| 13 | 🇲🇽 MX | 4430 |
| 14 | 🇬🇷 GR | 4376 |
| 15 | 🇳🇴 NO | 4051 |
| 16 | 🇨🇭 CH | 4024 |
| 17 | 🇹🇷 TR | 3670 |
| 18 | 🇲🇾 MY | 2838 |
| 19 | 🇵🇱 PL | 2625 |
| 20 | 🇿🇦 ZA | 2483 |
| 21 | 🇳🇿 NZ | 2297 |
| 22 | 🇹🇭 TH | 2221 |
| 23 | 🇰🇷 KR | 2079 |
| 24 | 🇵🇭 PH | 2027 |
| 25 | 🇬🇹 GT | 1999 |
| 26 | 🇲🇦 MA | 1569 |
| 27 | 🇲🇪 ME | 1496 |
| 28 | 🇭🇷 HR | 1409 |
| 29 | 🇳🇱 NL | 1405 |
| 30 | 🇲🇴 MO | 1255 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3166 |
| 2 | Denver International Airport |  | US | 2576 |
| 3 | Tokyo International Airport |  | JP | 2006 |
| 4 | Guaymaral Airport |  | CO | 1927 |
| 5 | Indira Gandhi International Airport |  | IN | 1904 |
| 6 | Harry Reid International Airport |  | US | 1881 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1717 |
| 8 | Zurich Airport |  | CH | 1668 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1607 |
| 10 | La Aurora Airport |  | GT | 1550 |
| 11 | Frankfurt am Main International Airport |  | DE | 1438 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1435 |
| 13 | Chicago O'Hare International Airport |  | US | 1409 |
| 14 | Salt Lake City International Airport |  | US | 1386 |
| 15 | El Dorado International Airport |  | CO | 1384 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1304 |
| 17 | Macau International Airport |  | MO | 1255 |
| 18 | Congonhas Airport |  | BR | 1248 |
| 19 | Madrid Barajas International Airport |  | ES | 1225 |
| 20 | Capua Airport |  | IT | 1215 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1186 |
| 22 | Kuala Lumpur International Airport |  | MY | 1091 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1089 |
| 24 | Charlotte/Douglas International Airport |  | US | 1089 |
| 25 | Sydney Kingsford Smith International Airport |  | AU | 1087 |
| 26 | Charles de Gaulle International Airport |  | FR | 1052 |
| 27 | Bengaluru International Airport |  | IN | 1025 |
| 28 | Malpensa International Airport |  | IT | 1004 |
| 29 | Ninoy Aquino International Airport |  | PH | 949 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 930 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 925 |
| 32 | Barcelona International Airport |  | ES | 915 |
| 33 | Daniel K Inouye International Airport |  | US | 911 |
| 34 | Tenerife Norte Airport |  | ES | 883 |
| 35 | Seattle-Tacoma International Airport |  | US | 883 |
| 36 | Calgary International Airport |  | CA | 874 |
| 37 | Viracopos International Airport |  | BR | 872 |
| 38 | Scottsdale Airport |  | US | 871 |
| 39 | Amsterdam Airport Schiphol |  | NL | 846 |
| 40 | Oslo Gardermoen Airport |  | NO | 841 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 810 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 555 | 21m | 244 km | 2,337.0 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 373 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 368 | 24m | 225 km | 1,427.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 356 | 1h 9m | 770 km | 4,729.2 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 280 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 275 | 27m | 275 km | 1,303.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 226 | 22m | 55 km | 214.8 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 208 | 44m | 241 km | 864.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 207 | 1h 47m | 1,423 km | 5,080.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 202 | 26m | 215 km | 748.1 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 200 | 20m | 99 km | 342.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 198 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 191 | 20m | 250 km | 825.0 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 187 | 30m | 49 km | 158.1 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 187 | 27m | 152 km | 488.7 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 182 | 1h 15m | 961 km | 3,016.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 180 | 18m | 144 km | 447.7 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 180 | 13m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 179 | 31m | 369 km | 1,139.4 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 174 | 44m | 452 km | 1,356.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 172 | 1h 39m | 1,156 km | 3,431.3 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 172 | 1h 1m | 695 km | 2,061.8 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 172 | 51m | 556 km | 1,648.8 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SWA1202 | Southwest Airlines | John Glenn Columbus International Airport (KCMH) | NM15 (NM15) | 2026-07-26 20:40 UTC | 2026-07-26 23:00 UTC | 2h 19m |
| PFT144 | PFT | Smith Reynolds Airport (KINT) | Tierra De Dios Airport (NM92) | 2026-07-26 20:24 UTC | 2026-07-26 22:59 UTC | 2h 34m |
| YGW | YGW | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-07-26 22:10 UTC | 2026-07-26 22:55 UTC | 44m |
| N442HB |  | Springdale Municipal Airport (KASG) | Springdale Municipal Airport (KASG) | 2026-07-26 21:44 UTC | 2026-07-26 22:55 UTC | 1h 10m |
| PSNYC | PSN | Amarais Airport (SDAM) | Santa Cruz Airport (SBSC) | 2026-07-26 22:13 UTC | 2026-07-26 22:53 UTC | 40m |
| CFRT71 | CFR | Ramona Airport (KRNM) | Hemet-Ryan Airport (KHMT) | 2026-07-26 22:28 UTC | 2026-07-26 22:52 UTC | 24m |
| N69AY |  | KU77 (KU77) | Lee Vining Airport (KO24) | 2026-07-26 21:23 UTC | 2026-07-26 22:48 UTC | 1h 25m |
| USI | USI | Adelaide Parafield Airport (YPPF) | Adelaide Parafield Airport (YPPF) | 2026-07-26 22:30 UTC | 2026-07-26 22:48 UTC | 17m |
| CXK419 | CXK | Bradley Field (NC29) | Schneider Haven Airstrip (NC75) | 2026-07-26 22:24 UTC | 2026-07-26 22:47 UTC | 22m |
| GPD433 | GPD | KHTO (KHTO) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-07-26 22:03 UTC | 2026-07-26 22:47 UTC | 43m |
| N7668K |  | 67LL (67LL) | 0LL2 (0LL2) | 2026-07-26 22:00 UTC | 2026-07-26 22:47 UTC | 46m |
| AAL1160 | American Airlines | Chicago O'Hare International Airport (KORD) | Beaver Municipal Airport (KK44) | 2026-07-26 21:16 UTC | 2026-07-26 22:46 UTC | 1h 30m |
| VHRGF | VHR | Kingaroy Airport (YKRY) | Gympie Airport (YGYM) | 2026-07-26 22:32 UTC | 2026-07-26 22:46 UTC | 14m |
| UCA4256 | UCA | George Bush Intcntl/Houston Airport (KIAH) | AL02 (AL02) | 2026-07-26 21:34 UTC | 2026-07-26 22:45 UTC | 1h 10m |
| UPS5952 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Sacramento Mather Airport (KMHR) | 2026-07-26 18:51 UTC | 2026-07-26 22:44 UTC | 3h 53m |
| T73 |  | Hemet-Ryan Airport (KHMT) | Hemet-Ryan Airport (KHMT) | 2026-07-26 22:04 UTC | 2026-07-26 22:44 UTC | 39m |
| N185YY |  | Chenega Bay Airport (PFCB) | Ted Stevens Anchorage International Airport (PANC) | 2026-07-26 21:44 UTC | 2026-07-26 22:43 UTC | 59m |
| EWG9ZT | EWG | Dusseldorf International Airport (EDDL) | Ben Slimane Airport (GMMB) | 2026-07-26 19:56 UTC | 2026-07-26 22:41 UTC | 2h 45m |
| N35CV |  | Wings Field (KLOM) | Lehigh Valley International Airport (KABE) | 2026-07-26 21:59 UTC | 2026-07-26 22:33 UTC | 33m |
| VOZ306 | Virgin Australia | Brisbane International Airport (YBBN) | Melbourne International Airport (YMML) | 2026-07-26 20:21 UTC | 2026-07-26 22:29 UTC | 2h 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
