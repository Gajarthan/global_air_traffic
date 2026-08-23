# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_05:56:26_UTC-green)

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

**Latest saved flight:** 2026-08-23 05:56:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 05:56:26 UTC

- **227,687** saved flights
- **70,582** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **227,687** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,744,805.5 tonnes** estimated CO2 emissions
- **159,119,162 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9125 |
| 2 | SkyWest Airlines | 8104 |
| 3 | EJA | 4392 |
| 4 | IndiGo | 3847 |
| 5 | American Airlines | 3740 |
| 6 | Southwest Airlines | 3549 |
| 7 | Delta Air Lines | 2919 |
| 8 | ENY | 2791 |
| 9 | LATAM Airlines | 2184 |
| 10 | AZU | 2112 |
| 11 | Vueling | 1926 |
| 12 | Lufthansa | 1860 |
| 13 | WIF | 1797 |
| 14 | LXJ | 1790 |
| 15 | easyJet | 1579 |
| 16 | Swiss International | 1515 |
| 17 | AXM | 1503 |
| 18 | United Airlines | 1444 |
| 19 | QLK | 1438 |
| 20 | EJU | 1435 |
| 21 | Alaska Airlines | 1384 |
| 22 | All Nippon Airways | 1365 |
| 23 | GLO | 1264 |
| 24 | VIV | 1253 |
| 25 | PGT | 1251 |
| 26 | Air France | 1235 |
| 27 | WMT | 1230 |
| 28 | Wizz Air | 1179 |
| 29 | JetBlue | 1141 |
| 30 | AEE | 1131 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 190630 |
| 2 | 🇪🇸 ES | 14571 |
| 3 | 🇧🇷 BR | 13293 |
| 4 | 🇦🇺 AU | 12897 |
| 5 | 🇨🇦 CA | 12612 |
| 6 | 🇮🇹 IT | 12218 |
| 7 | 🇮🇳 IN | 11979 |
| 8 | 🇩🇪 DE | 11189 |
| 9 | 🇬🇧 GB | 10688 |
| 10 | 🇨🇴 CO | 9384 |
| 11 | 🇯🇵 JP | 9253 |
| 12 | 🇫🇷 FR | 9094 |
| 13 | 🇹🇷 TR | 6686 |
| 14 | 🇬🇷 GR | 6654 |
| 15 | 🇲🇽 MX | 6358 |
| 16 | 🇨🇭 CH | 5997 |
| 17 | 🇳🇴 NO | 5601 |
| 18 | 🇲🇾 MY | 4012 |
| 19 | 🇿🇦 ZA | 3925 |
| 20 | 🇹🇭 TH | 3921 |
| 21 | 🇵🇱 PL | 3782 |
| 22 | 🇳🇿 NZ | 3163 |
| 23 | 🇵🇭 PH | 3112 |
| 24 | 🇬🇹 GT | 2873 |
| 25 | 🇰🇷 KR | 2696 |
| 26 | 🇭🇷 HR | 2571 |
| 27 | 🇲🇦 MA | 2297 |
| 28 | 🇲🇪 ME | 2053 |
| 29 | 🇳🇱 NL | 2027 |
| 30 | 🇮🇩 ID | 1966 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4771 |
| 2 | Denver International Airport |  | US | 3714 |
| 3 | Tokyo International Airport |  | JP | 2765 |
| 4 | Indira Gandhi International Airport |  | IN | 2763 |
| 5 | Guaymaral Airport |  | CO | 2647 |
| 6 | Harry Reid International Airport |  | US | 2473 |
| 7 | Zurich Airport |  | CH | 2362 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2332 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2295 |
| 10 | La Aurora Airport |  | GT | 2189 |
| 11 | El Dorado International Airport |  | CO | 2084 |
| 12 | Chicago O'Hare International Airport |  | US | 2071 |
| 13 | Salt Lake City International Airport |  | US | 2008 |
| 14 | Congonhas Airport |  | BR | 1939 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1937 |
| 16 | Frankfurt am Main International Airport |  | DE | 1824 |
| 17 | Madrid Barajas International Airport |  | ES | 1771 |
| 18 | Capua Airport |  | IT | 1763 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1703 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1698 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1647 |
| 22 | Malpensa International Airport |  | IT | 1615 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1603 |
| 24 | Macau International Airport |  | MO | 1594 |
| 25 | Charles de Gaulle International Airport |  | FR | 1573 |
| 26 | Charlotte/Douglas International Airport |  | US | 1492 |
| 27 | Ninoy Aquino International Airport |  | PH | 1490 |
| 28 | Kuala Lumpur International Airport |  | MY | 1456 |
| 29 | Barcelona International Airport |  | ES | 1414 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1384 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1350 |
| 32 | Viracopos International Airport |  | BR | 1348 |
| 33 | Bengaluru International Airport |  | IN | 1347 |
| 34 | Seattle-Tacoma International Airport |  | US | 1346 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1345 |
| 36 | Calgary International Airport |  | CA | 1299 |
| 37 | Don Mueang International Airport |  | TH | 1285 |
| 38 | Oslo Gardermoen Airport |  | NO | 1264 |
| 39 | Vitoria/Foronda Airport |  | ES | 1247 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1228 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1075 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 831 | 21m | 244 km | 3,499.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 568 | 1h 6m | 770 km | 7,545.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 562 | 24m | 225 km | 2,180.3 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 547 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 514 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 356 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 346 | 1h 50m | 1,423 km | 8,491.4 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 313 | 1h 7m | 706 km | 3,810.8 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 307 | 21m | 250 km | 1,326.1 t |
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
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 236 | 15m | 154 km | 625.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N558LM |  | Ted Stevens Anchorage International Airport (PANC) | Ted Stevens Anchorage International Airport (PANC) | 2026-08-23 04:36 UTC | 2026-08-23 05:56 UTC | 1h 20m |
| SPMEU | SPM | Kamien Slaski Airport (EPKN) | Hradec Kralove Airport (LKHK) | 2026-08-23 05:17 UTC | 2026-08-23 05:49 UTC | 32m |
| VLG3505 | Vueling | Ibiza Airport (LEIB) | Barcelona International Airport (LEBL) | 2026-08-23 05:09 UTC | 2026-08-23 05:43 UTC | 33m |
| ZKICU | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-08-23 05:25 UTC | 2026-08-23 05:38 UTC | 12m |
| ACA123 | Air Canada | Toronto Pearson International Airport (CYYZ) | Vancouver International Airport (CYVR) | 2026-08-23 00:57 UTC | 2026-08-23 05:37 UTC | 4h 39m |
| AEE968 | AEE | Eleftherios Venizelos International Airport (LGAV) | Stryama Airport (LBST) | 2026-08-23 04:51 UTC | 2026-08-23 05:36 UTC | 45m |
| DTCHMN42 | DTC | Bob Maxwell Memorial Airfield (KOKB) | Camp Pendleton Mcas (Munn Field) Airport (KNFG) | 2026-08-23 04:45 UTC | 2026-08-23 05:24 UTC | 38m |
| FSCN200 | FSC | RAAF Base Richmond (YSRI) | Mudgee Airport (YMDG) | 2026-08-23 05:03 UTC | 2026-08-23 05:22 UTC | 19m |
| TCVRG | TCV | Mikonos Airport (LGMK) | Adnan Menderes International Airport (LTBJ) | 2026-08-23 05:02 UTC | 2026-08-23 05:19 UTC | 16m |
| N917SH |  | Joe Foss Field (KFSD) | Clark County Airport (K8D7) | 2026-08-23 04:52 UTC | 2026-08-23 05:17 UTC | 25m |
| RXA6133 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-08-23 04:37 UTC | 2026-08-23 05:17 UTC | 40m |
| CTN3T | CTN | Zemunik Airport (LDZD) | Otocac Airport (LDRO) | 2026-08-23 04:53 UTC | 2026-08-23 05:14 UTC | 21m |
| SJX847 | SJX | Taiwan Taoyuan International Airport (RCTP) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-22 23:45 UTC | 2026-08-23 05:13 UTC | 5h 27m |
| N443LF |  | Cline Falls Air Park (3OR8) | Pilot Butte Airport (8OR5) | 2026-08-23 04:58 UTC | 2026-08-23 05:09 UTC | 11m |
| RYR95YC | Ryanair | Memmingen Allgau Airport (EDJA) | Capua Airport (LIAU) | 2026-08-23 04:05 UTC | 2026-08-23 05:09 UTC | 1h 3m |
| FIN8PN | Finnair | Helsinki Vantaa Airport (EFHK) | EFML (EFML) | 2026-08-23 04:22 UTC | 2026-08-23 05:09 UTC | 46m |
| SEH1TK | SEH | Eleftherios Venizelos International Airport (LGAV) | Olimboi Airport (LG56) | 2026-08-23 04:42 UTC | 2026-08-23 05:08 UTC | 26m |
| FJO68N | FJO | Valencia Airport (LEVC) | Ibiza Airport (LEIB) | 2026-08-23 04:43 UTC | 2026-08-23 05:07 UTC | 24m |
| RXA2125 | RXA | Perth International Airport (YPPH) | Frankland Airport (YFRK) | 2026-08-23 04:25 UTC | 2026-08-23 05:05 UTC | 39m |
| RYR824 | Ryanair | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Capua Airport (LIAU) | 2026-08-23 04:20 UTC | 2026-08-23 05:04 UTC | 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
