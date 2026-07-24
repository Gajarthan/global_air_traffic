# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--24_03:25:52_UTC-green)

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

**Latest saved flight:** 2026-07-24 03:25:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-24 03:25:52 UTC

- **147,118** saved flights
- **49,179** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **147,118** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,762,366.9 tonnes** estimated CO2 emissions
- **102,166,195 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5944 |
| 2 | SkyWest Airlines | 5402 |
| 3 | EJA | 2914 |
| 4 | IndiGo | 2648 |
| 5 | American Airlines | 2348 |
| 6 | Southwest Airlines | 2228 |
| 7 | ENY | 1833 |
| 8 | Delta Air Lines | 1746 |
| 9 | Lufthansa | 1450 |
| 10 | LATAM Airlines | 1354 |
| 11 | AZU | 1268 |
| 12 | Vueling | 1245 |
| 13 | WIF | 1245 |
| 14 | LXJ | 1134 |
| 15 | AXM | 1068 |
| 16 | Swiss International | 1037 |
| 17 | easyJet | 947 |
| 18 | All Nippon Airways | 934 |
| 19 | Alaska Airlines | 923 |
| 20 | QLK | 917 |
| 21 | EJU | 900 |
| 22 | VIV | 819 |
| 23 | CXK | 788 |
| 24 | AEE | 777 |
| 25 | JetBlue | 773 |
| 26 | Cathay Pacific | 772 |
| 27 | Air France | 770 |
| 28 | MXY | 770 |
| 29 | United Airlines | 765 |
| 30 | GLO | 762 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 127078 |
| 2 | 🇪🇸 ES | 9501 |
| 3 | 🇦🇺 AU | 8398 |
| 4 | 🇧🇷 BR | 8306 |
| 5 | 🇮🇳 IN | 8296 |
| 6 | 🇨🇦 CA | 7884 |
| 7 | 🇮🇹 IT | 7620 |
| 8 | 🇩🇪 DE | 7537 |
| 9 | 🇬🇧 GB | 6687 |
| 10 | 🇯🇵 JP | 6119 |
| 11 | 🇫🇷 FR | 5817 |
| 12 | 🇨🇴 CO | 4879 |
| 13 | 🇲🇽 MX | 4281 |
| 14 | 🇬🇷 GR | 4158 |
| 15 | 🇳🇴 NO | 3908 |
| 16 | 🇨🇭 CH | 3818 |
| 17 | 🇹🇷 TR | 3441 |
| 18 | 🇲🇾 MY | 2784 |
| 19 | 🇵🇱 PL | 2470 |
| 20 | 🇿🇦 ZA | 2372 |
| 21 | 🇳🇿 NZ | 2238 |
| 22 | 🇹🇭 TH | 2141 |
| 23 | 🇰🇷 KR | 2049 |
| 24 | 🇵🇭 PH | 1952 |
| 25 | 🇬🇹 GT | 1908 |
| 26 | 🇲🇦 MA | 1514 |
| 27 | 🇲🇪 ME | 1454 |
| 28 | 🇳🇱 NL | 1364 |
| 29 | 🇭🇷 HR | 1337 |
| 30 | 🇲🇴 MO | 1230 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3035 |
| 2 | Denver International Airport |  | US | 2470 |
| 3 | Tokyo International Airport |  | JP | 1965 |
| 4 | Indira Gandhi International Airport |  | IN | 1843 |
| 5 | Harry Reid International Airport |  | US | 1837 |
| 6 | Guaymaral Airport |  | CO | 1812 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1659 |
| 8 | Zurich Airport |  | CH | 1614 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1551 |
| 10 | La Aurora Airport |  | GT | 1479 |
| 11 | Frankfurt am Main International Airport |  | DE | 1401 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1387 |
| 13 | Chicago O'Hare International Airport |  | US | 1367 |
| 14 | Salt Lake City International Airport |  | US | 1329 |
| 15 | El Dorado International Airport |  | CO | 1320 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1274 |
| 17 | Macau International Airport |  | MO | 1230 |
| 18 | Capua Airport |  | IT | 1190 |
| 19 | Congonhas Airport |  | BR | 1185 |
| 20 | Madrid Barajas International Airport |  | ES | 1169 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1153 |
| 22 | Kuala Lumpur International Airport |  | MY | 1075 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1061 |
| 24 | Charlotte/Douglas International Airport |  | US | 1050 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1030 |
| 26 | Charles de Gaulle International Airport |  | FR | 1016 |
| 27 | Bengaluru International Airport |  | IN | 992 |
| 28 | Malpensa International Airport |  | IT | 946 |
| 29 | Ninoy Aquino International Airport |  | PH | 912 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 901 |
| 31 | Barcelona International Airport |  | ES | 889 |
| 32 | Daniel K Inouye International Airport |  | US | 885 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 884 |
| 34 | Seattle-Tacoma International Airport |  | US | 846 |
| 35 | Tenerife Norte Airport |  | ES | 844 |
| 36 | Calgary International Airport |  | CA | 844 |
| 37 | Scottsdale Airport |  | US | 833 |
| 38 | Viracopos International Airport |  | BR | 832 |
| 39 | Amsterdam Airport Schiphol |  | NL | 824 |
| 40 | Oslo Gardermoen Airport |  | NO | 809 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 764 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 534 | 21m | 244 km | 2,248.5 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 356 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 355 | 24m | 225 km | 1,377.2 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 345 | 1h 9m | 770 km | 4,583.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 264 | 27m | 275 km | 1,251.0 t |
| 10 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 262 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 222 | 22m | 55 km | 211.0 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 197 | 44m | 241 km | 818.3 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 196 | 1h 46m | 1,423 km | 4,810.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 194 | 26m | 215 km | 718.5 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 193 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 180 | 20m | 250 km | 777.5 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 180 | 28m | 152 km | 470.4 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 174 | 18m | 144 km | 432.8 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 172 | 1h 16m | 961 km | 2,851.0 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 171 | 12m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 170 | 44m | 452 km | 1,324.9 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 168 | 1h 1m | 695 km | 2,013.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 166 | 1h 39m | 1,156 km | 3,311.6 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 160 | 55m | 136 km | 375.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N89312 |  | Portland-Hillsboro Airport (KHIO) | Corvallis Municipal Airport (KCVO) | 2026-07-24 02:29 UTC | 2026-07-24 03:25 UTC | 56m |
| N515MV |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-07-24 02:56 UTC | 2026-07-24 03:20 UTC | 23m |
| ROLR9 | ROL | Sale Airport (YSLT) | Yarram Airport (YYRM) | 2026-07-24 02:50 UTC | 2026-07-24 03:14 UTC | 23m |
| KING32 | KIN | Stronghold Airport (09AZ) | Benson Municipal/Paul Kerchum Field (KE95) | 2026-07-24 02:26 UTC | 2026-07-24 03:11 UTC | 45m |
| N193SR |  | Lawrence Smith Memorial Airport (KLRY) | Kansas City Downtown/Wheeler Field (KMKC) | 2026-07-24 02:56 UTC | 2026-07-24 03:09 UTC | 13m |
| CPA660 | Cathay Pacific | Juhu Aerodrome (VAJJ) | Macau International Airport (VMMC) | 2026-07-23 21:48 UTC | 2026-07-24 03:00 UTC | 5h 12m |
| R20722 |  | Campbell Army Air Field (Fort Campbell) Airport (KHOP) | Parr Field (TN53) | 2026-07-24 02:29 UTC | 2026-07-24 02:59 UTC | 30m |
| MII | MII | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-07-24 02:40 UTC | 2026-07-24 02:57 UTC | 17m |
| QLK22D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-07-24 02:18 UTC | 2026-07-24 02:53 UTC | 35m |
| LIFELN1 | LIF | Northern Colorado Regional Airport (KFNL) | Northern Colorado Regional Airport (KFNL) | 2026-07-24 02:51 UTC | 2026-07-24 02:53 UTC | 1m |
| DYNO91 | DYN | Carl Folsom Airport (K14J) | Carl Folsom Airport (K14J) | 2026-07-24 02:40 UTC | 2026-07-24 02:52 UTC | 11m |
| VAR408 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-07-24 01:27 UTC | 2026-07-24 02:50 UTC | 1h 23m |
| SFJ45 | SFJ | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-07-24 01:39 UTC | 2026-07-24 02:50 UTC | 1h 11m |
| N5094L |  | Portland-Troutdale Airport (KTTD) | Ed Carlson Memorial Field/South Lewis County Airport (KTDO) | 2026-07-24 02:03 UTC | 2026-07-24 02:49 UTC | 46m |
| N1163F |  | Rachel's Landing Airport (8TN6) | Murfreesboro Municipal Airport (KMBT) | 2026-07-24 02:00 UTC | 2026-07-24 02:47 UTC | 47m |
| WIS500 | WIS | Anoka County/Blaine (Janes Field) Airport (KANE) | Eugene F Kranz Toledo Express Airport (KTOL) | 2026-07-24 00:05 UTC | 2026-07-24 02:45 UTC | 2h 39m |
| SABLE6 | SAB | Castle Airport (KMER) | Hunt Farms Airport (15CL) | 2026-07-24 02:32 UTC | 2026-07-24 02:44 UTC | 12m |
| RXA6528 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Cudal Airport (YCUA) | 2026-07-24 02:07 UTC | 2026-07-24 02:40 UTC | 32m |
| N326ME |  | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-07-24 02:29 UTC | 2026-07-24 02:40 UTC | 11m |
| EVA106 | EVA Air | Taiwan Taoyuan International Airport (RCTP) | Iki Airport (RJDB) | 2026-07-24 01:05 UTC | 2026-07-24 02:39 UTC | 1h 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
