# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_08:10:44_UTC-green)

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

**Latest saved flight:** 2026-08-15 08:10:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-15 08:10:44 UTC

- **197,859** saved flights
- **61,960** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **197,859** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,362,746.5 tonnes** estimated CO2 emissions
- **136,970,814 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7855 |
| 2 | SkyWest Airlines | 7115 |
| 3 | EJA | 3897 |
| 4 | IndiGo | 3415 |
| 5 | Southwest Airlines | 3070 |
| 6 | American Airlines | 3054 |
| 7 | ENY | 2445 |
| 8 | Delta Air Lines | 2344 |
| 9 | LATAM Airlines | 1857 |
| 10 | AZU | 1791 |
| 11 | Lufthansa | 1697 |
| 12 | Vueling | 1654 |
| 13 | WIF | 1628 |
| 14 | LXJ | 1570 |
| 15 | easyJet | 1355 |
| 16 | Swiss International | 1333 |
| 17 | AXM | 1295 |
| 18 | EJU | 1227 |
| 19 | QLK | 1224 |
| 20 | All Nippon Airways | 1198 |
| 21 | Alaska Airlines | 1174 |
| 22 | VIV | 1093 |
| 23 | GLO | 1070 |
| 24 | PGT | 1036 |
| 25 | Air France | 1035 |
| 26 | AEE | 1017 |
| 27 | United Airlines | 1009 |
| 28 | CXK | 1005 |
| 29 | WMT | 990 |
| 30 | Wizz Air | 978 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 168179 |
| 2 | 🇪🇸 ES | 12756 |
| 3 | 🇧🇷 BR | 11383 |
| 4 | 🇦🇺 AU | 11137 |
| 5 | 🇨🇦 CA | 10841 |
| 6 | 🇮🇳 IN | 10667 |
| 7 | 🇮🇹 IT | 10311 |
| 8 | 🇩🇪 DE | 9804 |
| 9 | 🇬🇧 GB | 9256 |
| 10 | 🇯🇵 JP | 8082 |
| 11 | 🇫🇷 FR | 7858 |
| 12 | 🇨🇴 CO | 7806 |
| 13 | 🇬🇷 GR | 5810 |
| 14 | 🇲🇽 MX | 5605 |
| 15 | 🇹🇷 TR | 5413 |
| 16 | 🇨🇭 CH | 5332 |
| 17 | 🇳🇴 NO | 5045 |
| 18 | 🇲🇾 MY | 3386 |
| 19 | 🇿🇦 ZA | 3328 |
| 20 | 🇵🇱 PL | 3270 |
| 21 | 🇹🇭 TH | 3086 |
| 22 | 🇳🇿 NZ | 2772 |
| 23 | 🇵🇭 PH | 2627 |
| 24 | 🇬🇹 GT | 2530 |
| 25 | 🇰🇷 KR | 2402 |
| 26 | 🇭🇷 HR | 2073 |
| 27 | 🇲🇦 MA | 1998 |
| 28 | 🇳🇱 NL | 1773 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1623 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4117 |
| 2 | Denver International Airport |  | US | 3220 |
| 3 | Tokyo International Airport |  | JP | 2474 |
| 4 | Guaymaral Airport |  | CO | 2443 |
| 5 | Indira Gandhi International Airport |  | IN | 2416 |
| 6 | Harry Reid International Airport |  | US | 2269 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2087 |
| 8 | Zurich Airport |  | CH | 2085 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2049 |
| 10 | La Aurora Airport |  | GT | 1938 |
| 11 | El Dorado International Airport |  | CO | 1816 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1764 |
| 13 | Salt Lake City International Airport |  | US | 1760 |
| 14 | Chicago O'Hare International Airport |  | US | 1737 |
| 15 | Congonhas Airport |  | BR | 1666 |
| 16 | Frankfurt am Main International Airport |  | DE | 1664 |
| 17 | Madrid Barajas International Airport |  | ES | 1556 |
| 18 | Macau International Airport |  | MO | 1533 |
| 19 | Capua Airport |  | IT | 1512 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1509 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1458 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1424 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1378 |
| 24 | Malpensa International Airport |  | IT | 1374 |
| 25 | Charles de Gaulle International Airport |  | FR | 1351 |
| 26 | Charlotte/Douglas International Airport |  | US | 1308 |
| 27 | Kuala Lumpur International Airport |  | MY | 1264 |
| 28 | Bengaluru International Airport |  | IN | 1249 |
| 29 | Ninoy Aquino International Airport |  | PH | 1242 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1236 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1212 |
| 32 | Barcelona International Airport |  | ES | 1189 |
| 33 | Viracopos International Airport |  | BR | 1151 |
| 34 | Seattle-Tacoma International Airport |  | US | 1139 |
| 35 | Calgary International Airport |  | CA | 1127 |
| 36 | Reno/Tahoe International Airport |  | US | 1116 |
| 37 | Oslo Gardermoen Airport |  | NO | 1113 |
| 38 | Daniel K Inouye International Airport |  | US | 1102 |
| 39 | Vitoria/Foronda Airport |  | ES | 1086 |
| 40 | Tenerife Norte Airport |  | ES | 1079 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1006 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 481 | 1h 7m | 770 km | 6,389.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 464 | 24m | 225 km | 1,800.1 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 462 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 354 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 338 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 332 | 27m | 275 km | 1,573.2 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 305 | 1h 7m | 706 km | 3,713.4 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 297 | 44m | 241 km | 1,233.7 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 286 | 1h 49m | 1,423 km | 7,018.9 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 282 | 22m | 55 km | 268.0 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 261 | 21m | 250 km | 1,127.4 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 245 | 26m | 215 km | 907.4 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 244 | 24m | 218 km | 919.2 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 242 | 19m | 99 km | 414.5 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 241 | 1h 15m | 961 km | 3,994.7 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 235 | 1h 38m | 1,156 km | 4,688.2 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 231 | 19m | 144 km | 574.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 225 | 31m | 369 km | 1,432.2 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 215 | 28m | 152 km | 561.9 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 214 | 1h 3m | 695 km | 2,565.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| WZZ8DM | Wizz Air | Aberdeen Dyce Airport (EGPD) | Oksywie Military Air Base (EPOK) | 2026-08-15 06:35 UTC | 2026-08-15 08:10 UTC | 1h 35m |
| N741SM |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-15 07:07 UTC | 2026-08-15 08:08 UTC | 1h 0m |
| HBKTN | HBK | LSMF (LSMF) | Bad Ragaz Airport (LSZE) | 2026-08-15 07:34 UTC | 2026-08-15 07:54 UTC | 19m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-15 07:22 UTC | 2026-08-15 07:53 UTC | 30m |
| OKLCZ | OKL | Hradec Kralove Airport (LKHK) | Prerov Air Base (LKPO) | 2026-08-15 07:19 UTC | 2026-08-15 07:45 UTC | 26m |
| N253EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-08-15 04:30 UTC | 2026-08-15 07:27 UTC | 2h 57m |
| VOE3567 | VOE | Castellon-Costa Azahar Airport (LEDS) | La Morgal Airport (LEMR) | 2026-08-15 06:26 UTC | 2026-08-15 07:22 UTC | 55m |
| N486LP |  | 99AZ (99AZ) | Glendale Regional Airport (KGEU) | 2026-08-15 06:25 UTC | 2026-08-15 07:21 UTC | 55m |
| HBZZX | HBZ | Reichenbach Air Base (LSGR) | Raron Airport (LSTA) | 2026-08-15 06:43 UTC | 2026-08-15 07:18 UTC | 35m |
| AGV01 | AGV | St Stephan Airport (LSTS) | Sion Airport (LSGS) | 2026-08-15 07:15 UTC | 2026-08-15 07:16 UTC | 0m |
| HBZUO | HBZ | Locarno Airport (LSZL) | Muenster Aero Airport (LSPU) | 2026-08-15 06:44 UTC | 2026-08-15 07:14 UTC | 29m |
| OC99 |  | Fukuoka Airport (RJFF) | Kamigoto Airport (RJDK) | 2026-08-15 06:50 UTC | 2026-08-15 07:10 UTC | 19m |
| AUR202 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-08-15 06:55 UTC | 2026-08-15 07:09 UTC | 13m |
| ZKIUY | ZKI | La Mole Airport (LFTZ) | La Mole Airport (LFTZ) | 2026-08-15 06:53 UTC | 2026-08-15 07:08 UTC | 14m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-15 06:57 UTC | 2026-08-15 07:07 UTC | 10m |
| HSEFS | HSE | Pattaya Airpark (YTBF) | Bang Pra Airport (VTBT) | 2026-08-15 06:39 UTC | 2026-08-15 07:06 UTC | 26m |
| HBCFY | HBC | St Gallen Altenrhein Airport (LSZR) | Friedrichshafen Airport (EDNY) | 2026-08-15 06:48 UTC | 2026-08-15 07:06 UTC | 17m |
| VLG3QU | Vueling | Barcelona International Airport (LEBL) | La Morgal Airport (LEMR) | 2026-08-15 06:03 UTC | 2026-08-15 07:05 UTC | 1h 2m |
| EJU73AR | EJU | Barcelona International Airport (LEBL) | Malpensa International Airport (LIMC) | 2026-08-15 05:50 UTC | 2026-08-15 07:03 UTC | 1h 12m |
| CNF412S | CNF | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 2026-08-15 06:52 UTC | 2026-08-15 07:03 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
