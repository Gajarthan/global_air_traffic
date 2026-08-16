# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_05:42:54_UTC-green)

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

**Latest saved flight:** 2026-08-16 05:42:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 05:42:54 UTC

- **203,580** saved flights
- **65,186** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **203,580** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,446,880.6 tonnes** estimated CO2 emissions
- **141,848,153 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7992 |
| 2 | SkyWest Airlines | 7350 |
| 3 | EJA | 3954 |
| 4 | IndiGo | 3466 |
| 5 | American Airlines | 3400 |
| 6 | Southwest Airlines | 3304 |
| 7 | Delta Air Lines | 2610 |
| 8 | ENY | 2548 |
| 9 | LATAM Airlines | 1907 |
| 10 | AZU | 1836 |
| 11 | Lufthansa | 1722 |
| 12 | Vueling | 1682 |
| 13 | WIF | 1640 |
| 14 | LXJ | 1606 |
| 15 | easyJet | 1397 |
| 16 | Swiss International | 1352 |
| 17 | AXM | 1317 |
| 18 | United Airlines | 1292 |
| 19 | Alaska Airlines | 1275 |
| 20 | QLK | 1251 |
| 21 | EJU | 1242 |
| 22 | All Nippon Airways | 1235 |
| 23 | VIV | 1119 |
| 24 | GLO | 1094 |
| 25 | PGT | 1080 |
| 26 | Air France | 1077 |
| 27 | JetBlue | 1051 |
| 28 | AEE | 1034 |
| 29 | CXK | 1011 |
| 30 | WMT | 1011 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 173756 |
| 2 | 🇪🇸 ES | 12992 |
| 3 | 🇧🇷 BR | 11644 |
| 4 | 🇦🇺 AU | 11411 |
| 5 | 🇨🇦 CA | 11270 |
| 6 | 🇮🇳 IN | 10826 |
| 7 | 🇮🇹 IT | 10526 |
| 8 | 🇩🇪 DE | 10013 |
| 9 | 🇬🇧 GB | 9462 |
| 10 | 🇯🇵 JP | 8341 |
| 11 | 🇨🇴 CO | 8044 |
| 12 | 🇫🇷 FR | 8033 |
| 13 | 🇬🇷 GR | 5960 |
| 14 | 🇲🇽 MX | 5741 |
| 15 | 🇹🇷 TR | 5680 |
| 16 | 🇨🇭 CH | 5419 |
| 17 | 🇳🇴 NO | 5077 |
| 18 | 🇲🇾 MY | 3461 |
| 19 | 🇿🇦 ZA | 3378 |
| 20 | 🇵🇱 PL | 3334 |
| 21 | 🇹🇭 TH | 3182 |
| 22 | 🇳🇿 NZ | 2829 |
| 23 | 🇵🇭 PH | 2689 |
| 24 | 🇬🇹 GT | 2556 |
| 25 | 🇰🇷 KR | 2485 |
| 26 | 🇭🇷 HR | 2140 |
| 27 | 🇲🇦 MA | 2037 |
| 28 | 🇳🇱 NL | 1801 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1663 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4287 |
| 2 | Denver International Airport |  | US | 3338 |
| 3 | Tokyo International Airport |  | JP | 2524 |
| 4 | Guaymaral Airport |  | CO | 2476 |
| 5 | Indira Gandhi International Airport |  | IN | 2460 |
| 6 | Harry Reid International Airport |  | US | 2321 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2123 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2118 |
| 9 | Zurich Airport |  | CH | 2110 |
| 10 | La Aurora Airport |  | GT | 1958 |
| 11 | Chicago O'Hare International Airport |  | US | 1903 |
| 12 | El Dorado International Airport |  | CO | 1860 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1826 |
| 14 | Salt Lake City International Airport |  | US | 1808 |
| 15 | Congonhas Airport |  | BR | 1694 |
| 16 | Frankfurt am Main International Airport |  | DE | 1685 |
| 17 | Madrid Barajas International Airport |  | ES | 1585 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1564 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1555 |
| 20 | Macau International Airport |  | MO | 1540 |
| 21 | Capua Airport |  | IT | 1539 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1471 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1430 |
| 24 | Malpensa International Airport |  | IT | 1399 |
| 25 | Charlotte/Douglas International Airport |  | US | 1391 |
| 26 | Charles de Gaulle International Airport |  | FR | 1387 |
| 27 | Kuala Lumpur International Airport |  | MY | 1287 |
| 28 | Ninoy Aquino International Airport |  | PH | 1272 |
| 29 | Bengaluru International Airport |  | IN | 1264 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1257 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1231 |
| 32 | Barcelona International Airport |  | ES | 1214 |
| 33 | Seattle-Tacoma International Airport |  | US | 1212 |
| 34 | Viracopos International Airport |  | BR | 1177 |
| 35 | Calgary International Airport |  | CA | 1157 |
| 36 | Reno/Tahoe International Airport |  | US | 1133 |
| 37 | Oslo Gardermoen Airport |  | NO | 1120 |
| 38 | Vitoria/Foronda Airport |  | ES | 1117 |
| 39 | Daniel K Inouye International Airport |  | US | 1103 |
| 40 | Tenerife Norte Airport |  | ES | 1096 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1019 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 492 | 1h 7m | 770 km | 6,535.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 471 | 24m | 225 km | 1,827.3 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 466 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 383 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 340 | 27m | 275 km | 1,611.1 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 307 | 1h 7m | 706 km | 3,737.7 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 299 | 44m | 241 km | 1,242.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 293 | 1h 49m | 1,423 km | 7,190.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 262 | 21m | 250 km | 1,131.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 251 | 24m | 218 km | 945.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 248 | 26m | 215 km | 918.5 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 20 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 245 | 1h 14m | 961 km | 4,061.0 t |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 245 | 19m | 99 km | 419.7 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 244 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 239 | 1h 37m | 1,156 km | 4,768.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 234 | 19m | 144 km | 582.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 229 | 31m | 369 km | 1,457.6 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 220 | 1h 49m | 1,304 km | 4,949.4 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 216 | 1h 3m | 695 km | 2,589.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ASA661 | Alaska Airlines | WA69 (WA69) | Ted Stevens Anchorage International Airport (PANC) | 2026-08-16 02:49 UTC | 2026-08-16 05:42 UTC | 2h 53m |
| ZAM17 | ZAM | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-08-16 05:02 UTC | 2026-08-16 05:40 UTC | 38m |
| UAE9616 | Emirates | Singapore Changi International Airport (WSSS) | Sydney Kingsford Smith International Airport (YSSY) | 2026-08-15 22:34 UTC | 2026-08-16 05:38 UTC | 7h 3m |
| DAL848 | Delta Air Lines | Baker City Municipal Airport (KBKE) | Austin-Bergstrom International Airport (KAUS) | 2026-08-16 02:49 UTC | 2026-08-16 05:34 UTC | 2h 45m |
| CSZ8966 | CSZ | Shenzhen Bao'an International Airport (ZGSZ) | Shenzhen Bao'an International Airport (ZGSZ) | 2026-08-16 01:02 UTC | 2026-08-16 05:32 UTC | 4h 30m |
| JBU993 | JetBlue | Owosso Community Airport (KRNP) | Denver International Airport (KDEN) | 2026-08-16 02:48 UTC | 2026-08-16 05:29 UTC | 2h 40m |
| DLH7EK | Lufthansa | Hamburg Airport (EDDH) | Frankfurt am Main International Airport (EDDF) | 2026-08-16 04:35 UTC | 2026-08-16 05:26 UTC | 50m |
| BRU738 | BRU | Minsk International Airport (UMMS) | Smolensk North Airport (XUBS) | 2026-08-15 14:56 UTC | 2026-08-16 05:26 UTC | 14h 29m |
| CXA8681 | CXA | Beijing Nanyuan Airport (ZBNY) | Macau International Airport (VMMC) | 2026-08-15 23:31 UTC | 2026-08-16 05:22 UTC | 5h 51m |
| SXS303 | SXS | Tbilisi International Airport (UGTB) | Antalya International Airport (LTAI) | 2026-08-16 03:15 UTC | 2026-08-16 05:22 UTC | 2h 7m |
| CFNZT | CFN | Calgary / Springbank Airport (CYBW) | Turner Valley Bar N Ranch Airport (CFY6) | 2026-08-16 04:48 UTC | 2026-08-16 05:21 UTC | 33m |
| DLH2TN | Lufthansa | Zagreb Airport (LDZA) | Frankfurt am Main International Airport (EDDF) | 2026-08-16 04:07 UTC | 2026-08-16 05:19 UTC | 1h 12m |
| KAL273 | Korean Air | Ted Stevens Anchorage International Airport (PANC) | Atlin Airport (CYSQ) | 2026-08-16 04:17 UTC | 2026-08-16 05:19 UTC | 1h 2m |
| ASA66 | Alaska Airlines | Juneau International Airport (PAJN) | Seattle-Tacoma International Airport (KSEA) | 2026-08-16 03:22 UTC | 2026-08-16 05:19 UTC | 1h 56m |
| SYE | SYE | Tyabb Airport (YTYA) | Melbourne Essendon Airport (YMEN) | 2026-08-16 04:48 UTC | 2026-08-16 05:18 UTC | 30m |
| R7217 |  | Wedderburn Airport (YWBN) | The Oaks Airport (YOAS) | 2026-08-16 05:08 UTC | 2026-08-16 05:16 UTC | 8m |
| PAL336 | Philippine Airlines | Ninoy Aquino International Airport (RPLL) | Matsu Nangan Airport (RCFG) | 2026-08-16 03:20 UTC | 2026-08-16 05:15 UTC | 1h 54m |
| ENY3725 | ENY | Chicago O'Hare International Airport (KORD) | Converse Farm Airport (SN47) | 2026-08-16 04:02 UTC | 2026-08-16 05:15 UTC | 1h 12m |
| ROT6471 | ROT | Henri Coanda International Airport (LROP) | Antalya International Airport (LTAI) | 2026-08-16 03:42 UTC | 2026-08-16 05:14 UTC | 1h 31m |
| CHH7925 | CHH | General Abelardo L. Rodriguez International Airport (MMTJ) | Puerto Libertad North Airport (MM32) | 2026-08-16 04:27 UTC | 2026-08-16 05:07 UTC | 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
