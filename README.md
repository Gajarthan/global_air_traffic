# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_08:26:17_UTC-green)

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

**Latest saved flight:** 2026-08-23 08:26:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 08:26:17 UTC

- **227,898** saved flights
- **70,608** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **227,898** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,747,560.4 tonnes** estimated CO2 emissions
- **159,278,862 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9143 |
| 2 | SkyWest Airlines | 8104 |
| 3 | EJA | 4393 |
| 4 | IndiGo | 3856 |
| 5 | American Airlines | 3740 |
| 6 | Southwest Airlines | 3549 |
| 7 | Delta Air Lines | 2919 |
| 8 | ENY | 2791 |
| 9 | LATAM Airlines | 2184 |
| 10 | AZU | 2112 |
| 11 | Vueling | 1932 |
| 12 | Lufthansa | 1863 |
| 13 | WIF | 1797 |
| 14 | LXJ | 1790 |
| 15 | easyJet | 1583 |
| 16 | Swiss International | 1519 |
| 17 | AXM | 1511 |
| 18 | QLK | 1445 |
| 19 | United Airlines | 1444 |
| 20 | EJU | 1440 |
| 21 | Alaska Airlines | 1385 |
| 22 | All Nippon Airways | 1367 |
| 23 | GLO | 1264 |
| 24 | VIV | 1253 |
| 25 | PGT | 1251 |
| 26 | Air France | 1235 |
| 27 | WMT | 1232 |
| 28 | Wizz Air | 1181 |
| 29 | JetBlue | 1142 |
| 30 | AEE | 1133 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 190643 |
| 2 | 🇪🇸 ES | 14602 |
| 3 | 🇧🇷 BR | 13293 |
| 4 | 🇦🇺 AU | 12931 |
| 5 | 🇨🇦 CA | 12616 |
| 6 | 🇮🇹 IT | 12249 |
| 7 | 🇮🇳 IN | 12011 |
| 8 | 🇩🇪 DE | 11203 |
| 9 | 🇬🇧 GB | 10696 |
| 10 | 🇨🇴 CO | 9384 |
| 11 | 🇯🇵 JP | 9268 |
| 12 | 🇫🇷 FR | 9107 |
| 13 | 🇹🇷 TR | 6693 |
| 14 | 🇬🇷 GR | 6673 |
| 15 | 🇲🇽 MX | 6358 |
| 16 | 🇨🇭 CH | 6010 |
| 17 | 🇳🇴 NO | 5601 |
| 18 | 🇲🇾 MY | 4031 |
| 19 | 🇹🇭 TH | 3942 |
| 20 | 🇿🇦 ZA | 3935 |
| 21 | 🇵🇱 PL | 3786 |
| 22 | 🇳🇿 NZ | 3165 |
| 23 | 🇵🇭 PH | 3121 |
| 24 | 🇬🇹 GT | 2873 |
| 25 | 🇰🇷 KR | 2699 |
| 26 | 🇭🇷 HR | 2581 |
| 27 | 🇲🇦 MA | 2298 |
| 28 | 🇲🇪 ME | 2059 |
| 29 | 🇳🇱 NL | 2029 |
| 30 | 🇮🇩 ID | 1970 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4771 |
| 2 | Denver International Airport |  | US | 3714 |
| 3 | Indira Gandhi International Airport |  | IN | 2772 |
| 4 | Tokyo International Airport |  | JP | 2771 |
| 5 | Guaymaral Airport |  | CO | 2647 |
| 6 | Harry Reid International Airport |  | US | 2473 |
| 7 | Zurich Airport |  | CH | 2369 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2332 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2298 |
| 10 | La Aurora Airport |  | GT | 2189 |
| 11 | El Dorado International Airport |  | CO | 2084 |
| 12 | Chicago O'Hare International Airport |  | US | 2071 |
| 13 | Salt Lake City International Airport |  | US | 2009 |
| 14 | Congonhas Airport |  | BR | 1939 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1938 |
| 16 | Frankfurt am Main International Airport |  | DE | 1827 |
| 17 | Madrid Barajas International Airport |  | ES | 1776 |
| 18 | Capua Airport |  | IT | 1771 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1703 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1698 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1648 |
| 22 | Malpensa International Airport |  | IT | 1620 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1607 |
| 24 | Macau International Airport |  | MO | 1594 |
| 25 | Charles de Gaulle International Airport |  | FR | 1573 |
| 26 | Ninoy Aquino International Airport |  | PH | 1495 |
| 27 | Charlotte/Douglas International Airport |  | US | 1492 |
| 28 | Kuala Lumpur International Airport |  | MY | 1461 |
| 29 | Barcelona International Airport |  | ES | 1418 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1384 |
| 31 | Bengaluru International Airport |  | IN | 1351 |
| 32 | Enrique Olaya Herrera Airport |  | CO | 1350 |
| 33 | Viracopos International Airport |  | BR | 1348 |
| 34 | Seattle-Tacoma International Airport |  | US | 1347 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1345 |
| 36 | Calgary International Airport |  | CA | 1299 |
| 37 | Don Mueang International Airport |  | TH | 1293 |
| 38 | Oslo Gardermoen Airport |  | NO | 1264 |
| 39 | Vitoria/Foronda Airport |  | ES | 1247 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1229 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1075 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 832 | 21m | 244 km | 3,503.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 571 | 1h 6m | 770 km | 7,585.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 565 | 24m | 225 km | 2,191.9 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 547 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 514 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 356 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 346 | 1h 50m | 1,423 km | 8,491.4 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 314 | 1h 7m | 706 km | 3,823.0 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 310 | 21m | 250 km | 1,339.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 305 | 22m | 55 km | 289.9 t |
| 15 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 301 | 44m | 555 km | 2,882.2 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
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
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 238 | 15m | 154 km | 630.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LOT6669 | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Palermo / Punta Raisi Airport (LICJ) | 2026-08-23 06:11 UTC | 2026-08-23 08:26 UTC | 2h 15m |
| N857GA |  | Ted Stevens Anchorage International Airport (PANC) | Tianjin Binhai International Airport (ZBTJ) | 2026-08-22 23:06 UTC | 2026-08-23 08:20 UTC | 9h 14m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-23 08:09 UTC | 2026-08-23 08:19 UTC | 10m |
| MMA361 | MMA | Don Mueang International Airport (VTBD) | Anisakan Airport (VYAS) | 2026-08-23 06:52 UTC | 2026-08-23 08:00 UTC | 1h 8m |
| BNI47 | BNI | Łódź Władysław Reymont Airport (EPLL) | Łódź Władysław Reymont Airport (EPLL) | 2026-08-23 07:25 UTC | 2026-08-23 08:00 UTC | 34m |
| 8AX |  | Hillman Farm Airport (YHLM) | Hillman Farm Airport (YHLM) | 2026-08-23 07:44 UTC | 2026-08-23 07:58 UTC | 14m |
| VOE3DL | VOE | Menorca Airport (LEMH) | Bilbao Airport (LEBB) | 2026-08-23 06:28 UTC | 2026-08-23 07:39 UTC | 1h 11m |
| OKBUR37 | OKB | Holic Airport (LZHL) | Kyjov Airport (LKKY) | 2026-08-23 07:02 UTC | 2026-08-23 07:38 UTC | 36m |
| NJE355M | NJE | Geneva Cointrin International Airport (LSGG) | Aosta Airport (LIMW) | 2026-08-23 07:01 UTC | 2026-08-23 07:37 UTC | 35m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-23 07:06 UTC | 2026-08-23 07:35 UTC | 29m |
| AXM6073 | AXM | Kota Kinabalu International Airport (WBKK) | Anduki Airport (WBAK) | 2026-08-23 07:10 UTC | 2026-08-23 07:32 UTC | 21m |
| EAI7S | EAI | Dublin Airport (EIDW) | Southampton Airport (EGHI) | 2026-08-23 06:17 UTC | 2026-08-23 07:31 UTC | 1h 14m |
| TLM556 | TLM | Don Mueang International Airport (VTBD) | Takhli Airport (VTPI) | 2026-08-23 07:11 UTC | 2026-08-23 07:27 UTC | 15m |
| NV151 |  | Sydney Bankstown Airport (YSBK) | Albury Airport (YMAY) | 2026-08-23 06:32 UTC | 2026-08-23 07:25 UTC | 52m |
| AIQ3142 | AIQ | Don Mueang International Airport (VTBD) | Kawthoung Airport (VYKT) | 2026-08-23 06:42 UTC | 2026-08-23 07:23 UTC | 40m |
| EAF9786 | EAF | Chania International Airport (LGSA) | Brno-Turany Airport (LKTB) | 2026-08-23 05:11 UTC | 2026-08-23 07:23 UTC | 2h 11m |
| UTY3240 | UTY | Adelaide International Airport (YPAD) | Roxby Downs Station Airport (YRXB) | 2026-08-23 06:38 UTC | 2026-08-23 07:23 UTC | 45m |
| MNE101 | MNE | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 2026-08-23 07:01 UTC | 2026-08-23 07:23 UTC | 21m |
| FRG119 | FRG | General Mitchell International Airport (KMKE) | Phoenix Sky Harbor International Airport (KPHX) | 2026-08-23 03:14 UTC | 2026-08-23 07:22 UTC | 4h 8m |
| EJU31CM | EJU | Paris-Orly Airport (LFPO) | Capua Airport (LIAU) | 2026-08-23 05:38 UTC | 2026-08-23 07:19 UTC | 1h 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
