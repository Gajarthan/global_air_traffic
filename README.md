# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_03:29:34_UTC-green)

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

**Latest saved flight:** 2026-08-02 03:29:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-02 03:29:34 UTC

- **165,945** saved flights
- **54,416** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **165,945** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,996,669.6 tonnes** estimated CO2 emissions
- **115,748,963 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6616 |
| 2 | SkyWest Airlines | 6059 |
| 3 | EJA | 3293 |
| 4 | IndiGo | 2917 |
| 5 | American Airlines | 2622 |
| 6 | Southwest Airlines | 2614 |
| 7 | ENY | 2068 |
| 8 | Delta Air Lines | 1983 |
| 9 | LATAM Airlines | 1547 |
| 10 | Lufthansa | 1537 |
| 11 | AZU | 1455 |
| 12 | WIF | 1388 |
| 13 | Vueling | 1368 |
| 14 | LXJ | 1289 |
| 15 | AXM | 1144 |
| 16 | Swiss International | 1134 |
| 17 | easyJet | 1093 |
| 18 | Alaska Airlines | 1025 |
| 19 | EJU | 1016 |
| 20 | QLK | 1014 |
| 21 | All Nippon Airways | 1011 |
| 22 | VIV | 914 |
| 23 | CXK | 886 |
| 24 | Cathay Pacific | 883 |
| 25 | United Airlines | 876 |
| 26 | AEE | 872 |
| 27 | GLO | 869 |
| 28 | MXY | 857 |
| 29 | Air France | 855 |
| 30 | JetBlue | 840 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 143390 |
| 2 | 🇪🇸 ES | 10597 |
| 3 | 🇧🇷 BR | 9450 |
| 4 | 🇦🇺 AU | 9290 |
| 5 | 🇮🇳 IN | 9155 |
| 6 | 🇨🇦 CA | 9019 |
| 7 | 🇮🇹 IT | 8560 |
| 8 | 🇩🇪 DE | 8288 |
| 9 | 🇬🇧 GB | 7632 |
| 10 | 🇯🇵 JP | 6690 |
| 11 | 🇫🇷 FR | 6566 |
| 12 | 🇨🇴 CO | 5975 |
| 13 | 🇬🇷 GR | 4788 |
| 14 | 🇲🇽 MX | 4754 |
| 15 | 🇨🇭 CH | 4355 |
| 16 | 🇳🇴 NO | 4343 |
| 17 | 🇹🇷 TR | 3987 |
| 18 | 🇲🇾 MY | 2979 |
| 19 | 🇵🇱 PL | 2806 |
| 20 | 🇿🇦 ZA | 2695 |
| 21 | 🇳🇿 NZ | 2420 |
| 22 | 🇹🇭 TH | 2376 |
| 23 | 🇵🇭 PH | 2190 |
| 24 | 🇬🇹 GT | 2141 |
| 25 | 🇰🇷 KR | 2139 |
| 26 | 🇲🇦 MA | 1671 |
| 27 | 🇭🇷 HR | 1574 |
| 28 | 🇲🇪 ME | 1544 |
| 29 | 🇳🇱 NL | 1502 |
| 30 | 🇲🇴 MO | 1414 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3398 |
| 2 | Denver International Airport |  | US | 2766 |
| 3 | Tokyo International Airport |  | JP | 2102 |
| 4 | Guaymaral Airport |  | CO | 2082 |
| 5 | Indira Gandhi International Airport |  | IN | 2029 |
| 6 | Harry Reid International Airport |  | US | 2005 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1820 |
| 8 | Zurich Airport |  | CH | 1760 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1743 |
| 10 | La Aurora Airport |  | GT | 1658 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1539 |
| 12 | El Dorado International Airport |  | CO | 1521 |
| 13 | Chicago O'Hare International Airport |  | US | 1500 |
| 14 | Frankfurt am Main International Airport |  | DE | 1500 |
| 15 | Salt Lake City International Airport |  | US | 1490 |
| 16 | Macau International Airport |  | MO | 1414 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1385 |
| 18 | Congonhas Airport |  | BR | 1370 |
| 19 | Madrid Barajas International Airport |  | ES | 1306 |
| 20 | Capua Airport |  | IT | 1296 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1263 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1173 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1169 |
| 24 | Charlotte/Douglas International Airport |  | US | 1162 |
| 25 | Charles de Gaulle International Airport |  | FR | 1131 |
| 26 | Kuala Lumpur International Airport |  | MY | 1129 |
| 27 | Malpensa International Airport |  | IT | 1108 |
| 28 | Bengaluru International Airport |  | IN | 1083 |
| 29 | Ninoy Aquino International Airport |  | PH | 1029 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1024 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1016 |
| 32 | Barcelona International Airport |  | ES | 979 |
| 33 | Daniel K Inouye International Airport |  | US | 967 |
| 34 | Seattle-Tacoma International Airport |  | US | 965 |
| 35 | Calgary International Airport |  | CA | 944 |
| 36 | Viracopos International Airport |  | BR | 941 |
| 37 | Scottsdale Airport |  | US | 926 |
| 38 | Tenerife Norte Airport |  | ES | 923 |
| 39 | Oslo Gardermoen Airport |  | NO | 920 |
| 40 | Reno/Tahoe International Airport |  | US | 917 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 868 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 605 | 21m | 244 km | 2,547.5 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 399 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 398 | 24m | 225 km | 1,544.1 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 378 | 1h 9m | 770 km | 5,021.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 310 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 285 | 27m | 275 km | 1,350.5 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 244 | 19m | 165 km | 694.1 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 239 | 44m | 241 km | 992.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 228 | 1h 47m | 1,423 km | 5,595.5 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 217 | 20m | 250 km | 937.3 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 215 | 26m | 215 km | 796.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 210 | 20m | 99 km | 359.7 t |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 210 | 31m | 49 km | 177.5 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 209 | 13m | - | - |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 198 | 1h 15m | 961 km | 3,282.0 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 195 | 19m | 144 km | 485.1 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 192 | 31m | 369 km | 1,222.1 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 189 | 50m | 556 km | 1,811.7 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 189 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 186 | 1h 38m | 1,156 km | 3,710.6 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 182 | 1h 1m | 695 km | 2,181.6 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 181 | 44m | 452 km | 1,410.6 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 178 | 24m | 218 km | 670.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N343AP |  | Ted Stevens Anchorage International Airport (PANC) | Homer Airport (PAHO) | 2026-08-02 03:06 UTC | 2026-08-02 03:29 UTC | 23m |
| TTW241 | TTW | Fukuoka Airport (RJFF) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-02 01:42 UTC | 2026-08-02 03:28 UTC | 1h 46m |
| MANLY51 | MAN | Wiley Post Airport (KPWA) | 84OL (84OL) | 2026-08-02 02:46 UTC | 2026-08-02 03:24 UTC | 37m |
| CAL5165 | CAL | Kansai International Airport (RJBB) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-02 01:16 UTC | 2026-08-02 03:21 UTC | 2h 4m |
| JJP13 | JJP | Narita International Airport (RJAA) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-02 00:29 UTC | 2026-08-02 03:17 UTC | 2h 48m |
| ELY082 | ELY | Suvarnabhumi Airport (VTBS) | Ben Gurion International Airport (LLBG) | 2026-08-01 17:16 UTC | 2026-08-02 03:12 UTC | 9h 56m |
| N2235V |  | Long Beach (Daugherty Field) Airport (KLGB) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-08-02 01:51 UTC | 2026-08-02 03:12 UTC | 1h 20m |
| WPF | WPF | Perth Jandakot Airport (YPJT) | Kalgoorlie-Boulder Airport (YPKG) | 2026-08-02 01:43 UTC | 2026-08-02 03:10 UTC | 1h 26m |
| CCA101 | Air China | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-08-02 00:33 UTC | 2026-08-02 03:07 UTC | 2h 34m |
| KAL791 | Korean Air | Incheon International Airport (RKSI) | Iki Airport (RJDB) | 2026-08-02 02:27 UTC | 2026-08-02 03:07 UTC | 39m |
| ANA249 | All Nippon Airways | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-08-02 01:57 UTC | 2026-08-02 03:05 UTC | 1h 7m |
| N510PR |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-08-02 02:18 UTC | 2026-08-02 03:03 UTC | 44m |
| XCN70 | XCN | Spokane International Airport (KGEG) | Fowler Field (02WN) | 2026-08-02 02:29 UTC | 2026-08-02 02:59 UTC | 29m |
| LIFELN1 | LIF | Northern Colorado Regional Airport (KFNL) | Northern Colorado Regional Airport (KFNL) | 2026-08-02 02:46 UTC | 2026-08-02 02:57 UTC | 10m |
| TNV54 | TNV | Igiugig Airport (PAIG) | Ted Stevens Anchorage International Airport (PANC) | 2026-08-02 02:00 UTC | 2026-08-02 02:56 UTC | 56m |
| JAL313 | Japan Airlines | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-08-02 01:50 UTC | 2026-08-02 02:56 UTC | 1h 6m |
| N80866 |  | Albuquerque International Sunport Airport (KABQ) | NM74 (NM74) | 2026-08-02 02:31 UTC | 2026-08-02 02:54 UTC | 23m |
| RXA6123 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-08-02 02:13 UTC | 2026-08-02 02:54 UTC | 40m |
| LNI | LNI | Jurien Bay Airport (YJNB) | Jurien Bay Airport (YJNB) | 2026-08-02 02:46 UTC | 2026-08-02 02:53 UTC | 7m |
| N138HN |  | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-08-02 02:49 UTC | 2026-08-02 02:53 UTC | 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
