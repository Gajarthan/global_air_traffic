# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_05:24:27_UTC-green)

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

**Latest saved flight:** 2026-08-23 05:24:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 05:24:27 UTC

- **227,639** saved flights
- **70,577** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **227,639** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,744,136.1 tonnes** estimated CO2 emissions
- **159,080,356 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9123 |
| 2 | SkyWest Airlines | 8104 |
| 3 | EJA | 4392 |
| 4 | IndiGo | 3847 |
| 5 | American Airlines | 3739 |
| 6 | Southwest Airlines | 3549 |
| 7 | Delta Air Lines | 2919 |
| 8 | ENY | 2791 |
| 9 | LATAM Airlines | 2183 |
| 10 | AZU | 2111 |
| 11 | Vueling | 1925 |
| 12 | Lufthansa | 1860 |
| 13 | WIF | 1797 |
| 14 | LXJ | 1790 |
| 15 | easyJet | 1579 |
| 16 | Swiss International | 1515 |
| 17 | AXM | 1503 |
| 18 | United Airlines | 1444 |
| 19 | EJU | 1435 |
| 20 | QLK | 1435 |
| 21 | Alaska Airlines | 1384 |
| 22 | All Nippon Airways | 1364 |
| 23 | GLO | 1264 |
| 24 | VIV | 1253 |
| 25 | PGT | 1251 |
| 26 | Air France | 1235 |
| 27 | WMT | 1229 |
| 28 | Wizz Air | 1178 |
| 29 | JetBlue | 1141 |
| 30 | AEE | 1130 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 190624 |
| 2 | 🇪🇸 ES | 14567 |
| 3 | 🇧🇷 BR | 13290 |
| 4 | 🇦🇺 AU | 12881 |
| 5 | 🇨🇦 CA | 12608 |
| 6 | 🇮🇹 IT | 12214 |
| 7 | 🇮🇳 IN | 11978 |
| 8 | 🇩🇪 DE | 11184 |
| 9 | 🇬🇧 GB | 10688 |
| 10 | 🇨🇴 CO | 9384 |
| 11 | 🇯🇵 JP | 9249 |
| 12 | 🇫🇷 FR | 9094 |
| 13 | 🇹🇷 TR | 6681 |
| 14 | 🇬🇷 GR | 6648 |
| 15 | 🇲🇽 MX | 6358 |
| 16 | 🇨🇭 CH | 5997 |
| 17 | 🇳🇴 NO | 5601 |
| 18 | 🇲🇾 MY | 4010 |
| 19 | 🇿🇦 ZA | 3923 |
| 20 | 🇹🇭 TH | 3915 |
| 21 | 🇵🇱 PL | 3780 |
| 22 | 🇳🇿 NZ | 3161 |
| 23 | 🇵🇭 PH | 3108 |
| 24 | 🇬🇹 GT | 2873 |
| 25 | 🇰🇷 KR | 2694 |
| 26 | 🇭🇷 HR | 2569 |
| 27 | 🇲🇦 MA | 2297 |
| 28 | 🇲🇪 ME | 2053 |
| 29 | 🇳🇱 NL | 2027 |
| 30 | 🇮🇩 ID | 1964 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4771 |
| 2 | Denver International Airport |  | US | 3713 |
| 3 | Tokyo International Airport |  | JP | 2764 |
| 4 | Indira Gandhi International Airport |  | IN | 2762 |
| 5 | Guaymaral Airport |  | CO | 2647 |
| 6 | Harry Reid International Airport |  | US | 2473 |
| 7 | Zurich Airport |  | CH | 2362 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2332 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2293 |
| 10 | La Aurora Airport |  | GT | 2189 |
| 11 | El Dorado International Airport |  | CO | 2084 |
| 12 | Chicago O'Hare International Airport |  | US | 2071 |
| 13 | Salt Lake City International Airport |  | US | 2008 |
| 14 | Congonhas Airport |  | BR | 1939 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1937 |
| 16 | Frankfurt am Main International Airport |  | DE | 1824 |
| 17 | Madrid Barajas International Airport |  | ES | 1771 |
| 18 | Capua Airport |  | IT | 1761 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1702 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1698 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1647 |
| 22 | Malpensa International Airport |  | IT | 1614 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1601 |
| 24 | Macau International Airport |  | MO | 1594 |
| 25 | Charles de Gaulle International Airport |  | FR | 1573 |
| 26 | Charlotte/Douglas International Airport |  | US | 1491 |
| 27 | Ninoy Aquino International Airport |  | PH | 1488 |
| 28 | Kuala Lumpur International Airport |  | MY | 1455 |
| 29 | Barcelona International Airport |  | ES | 1413 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1384 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1350 |
| 32 | Viracopos International Airport |  | BR | 1348 |
| 33 | Bengaluru International Airport |  | IN | 1347 |
| 34 | Seattle-Tacoma International Airport |  | US | 1346 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1345 |
| 36 | Calgary International Airport |  | CA | 1298 |
| 37 | Don Mueang International Airport |  | TH | 1284 |
| 38 | Oslo Gardermoen Airport |  | NO | 1264 |
| 39 | Vitoria/Foronda Airport |  | ES | 1247 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1228 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1075 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 831 | 21m | 244 km | 3,499.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 568 | 1h 6m | 770 km | 7,545.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 560 | 24m | 225 km | 2,172.5 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 547 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 514 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 356 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 345 | 1h 50m | 1,423 km | 8,466.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 313 | 1h 7m | 706 km | 3,810.8 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 306 | 21m | 250 km | 1,321.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 305 | 22m | 55 km | 289.9 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 16 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 298 | 44m | 555 km | 2,853.5 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 292 | 1h 38m | 1,156 km | 5,825.3 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 289 | 24m | 218 km | 1,088.8 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 284 | 19m | 99 km | 486.5 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 276 | 27m | 215 km | 1,022.2 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 267 | 1h 14m | 961 km | 4,425.7 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 266 | 12m | - | - |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 259 | 19m | 144 km | 644.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 245 | 1h 50m | 1,304 km | 5,511.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 239 | 28m | 152 km | 624.6 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 235 | 15m | 154 km | 622.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DTCHMN42 | DTC | Bob Maxwell Memorial Airfield (KOKB) | Camp Pendleton Mcas (Munn Field) Airport (KNFG) | 2026-08-23 04:45 UTC | 2026-08-23 05:24 UTC | 38m |
| SJX847 | SJX | Taiwan Taoyuan International Airport (RCTP) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-22 23:45 UTC | 2026-08-23 05:13 UTC | 5h 27m |
| N443LF |  | Cline Falls Air Park (3OR8) | Pilot Butte Airport (8OR5) | 2026-08-23 04:58 UTC | 2026-08-23 05:09 UTC | 11m |
| A7GAC |  | Al Khawr Airport (OTBK) | Al Khawr Airport (OTBK) | 2026-08-23 04:58 UTC | 2026-08-23 05:03 UTC | 5m |
| YR5564 |  | Baneasa International Airport (LRBS) | Baneasa International Airport (LRBS) | 2026-08-23 04:50 UTC | 2026-08-23 05:01 UTC | 10m |
| TWB843 | TWB | Cheongju International Airport (RKTU) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-22 23:52 UTC | 2026-08-23 04:59 UTC | 5h 6m |
| A7GQC |  | Al Khawr Airport (OTBK) | Persian Gulf International Airport (OIBP) | 2026-08-23 04:07 UTC | 2026-08-23 04:53 UTC | 45m |
| A7GAC |  | Doha International Airport (OTBD) | Al Khawr Airport (OTBK) | 2026-08-23 04:08 UTC | 2026-08-23 04:48 UTC | 39m |
| N737BC |  | San Luis Obispo County Regional Airport (KSBP) | Santa Barbara Municipal Airport (KSBA) | 2026-08-23 04:03 UTC | 2026-08-23 04:47 UTC | 44m |
| TGW474 | TGW | Changi Air Base (WSAC) | Sultan Abdul Aziz Shah International Airport (WMSA) | 2026-08-23 04:14 UTC | 2026-08-23 04:47 UTC | 33m |
| RYR1VM | Ryanair | Gdańsk Lech Wałęsa Airport (EPGD) | Aarhus Airport (EKAH) | 2026-08-23 03:46 UTC | 2026-08-23 04:36 UTC | 49m |
| XIH | XIH | Caloundra Airport (YCDR) | Sunshine Coast Airport (YBMC) | 2026-08-23 04:28 UTC | 2026-08-23 04:33 UTC | 5m |
| RYR11EX | Ryanair | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-08-23 04:08 UTC | 2026-08-23 04:31 UTC | 23m |
| SWR2069 | Swiss International | Francisco de Sá Carneiro Airport (LPPR) | Zurich Airport (LSZH) | 2026-08-23 02:11 UTC | 2026-08-23 04:28 UTC | 2h 17m |
| IGO5215 | IndiGo | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 2026-08-23 02:31 UTC | 2026-08-23 04:26 UTC | 1h 54m |
| JAL981 | Japan Airlines | Tokyo International Airport (RJTT) | Kerama Airport (ROKR) | 2026-08-23 02:21 UTC | 2026-08-23 04:25 UTC | 2h 4m |
| CSI502 | CSI | Albuquerque International Sunport Airport (KABQ) | Castle Lakes Airport (CD32) | 2026-08-23 03:52 UTC | 2026-08-23 04:22 UTC | 29m |
| OCN2B | OCN | Frankfurt am Main International Airport (EDDF) | Brac Airport (LDSB) | 2026-08-23 03:08 UTC | 2026-08-23 04:21 UTC | 1h 13m |
| CEB911 | CEB | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-08-23 03:57 UTC | 2026-08-23 04:19 UTC | 21m |
| VOZ1117 | Virgin Australia | Brisbane International Airport (YBBN) | Lakeside Airpark (YLAK) | 2026-08-23 03:00 UTC | 2026-08-23 04:18 UTC | 1h 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
