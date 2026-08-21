# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_20:44:51_UTC-green)

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

**Latest saved flight:** 2026-08-21 20:44:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 20:44:51 UTC

- **223,741** saved flights
- **69,857** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **223,741** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,695,117.4 tonnes** estimated CO2 emissions
- **156,238,691 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8970 |
| 2 | SkyWest Airlines | 7951 |
| 3 | EJA | 4332 |
| 4 | IndiGo | 3781 |
| 5 | American Airlines | 3695 |
| 6 | Southwest Airlines | 3505 |
| 7 | Delta Air Lines | 2870 |
| 8 | ENY | 2749 |
| 9 | LATAM Airlines | 2125 |
| 10 | AZU | 2061 |
| 11 | Vueling | 1885 |
| 12 | Lufthansa | 1842 |
| 13 | WIF | 1787 |
| 14 | LXJ | 1764 |
| 15 | easyJet | 1547 |
| 16 | Swiss International | 1489 |
| 17 | AXM | 1467 |
| 18 | United Airlines | 1407 |
| 19 | QLK | 1405 |
| 20 | EJU | 1401 |
| 21 | Alaska Airlines | 1357 |
| 22 | All Nippon Airways | 1333 |
| 23 | GLO | 1231 |
| 24 | PGT | 1228 |
| 25 | VIV | 1217 |
| 26 | Air France | 1213 |
| 27 | WMT | 1193 |
| 28 | Wizz Air | 1152 |
| 29 | JetBlue | 1122 |
| 30 | AEE | 1115 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 187897 |
| 2 | 🇪🇸 ES | 14347 |
| 3 | 🇧🇷 BR | 12970 |
| 4 | 🇦🇺 AU | 12655 |
| 5 | 🇨🇦 CA | 12374 |
| 6 | 🇮🇹 IT | 11947 |
| 7 | 🇮🇳 IN | 11793 |
| 8 | 🇩🇪 DE | 11025 |
| 9 | 🇬🇧 GB | 10500 |
| 10 | 🇨🇴 CO | 9225 |
| 11 | 🇯🇵 JP | 9054 |
| 12 | 🇫🇷 FR | 8925 |
| 13 | 🇬🇷 GR | 6522 |
| 14 | 🇹🇷 TR | 6519 |
| 15 | 🇲🇽 MX | 6208 |
| 16 | 🇨🇭 CH | 5887 |
| 17 | 🇳🇴 NO | 5560 |
| 18 | 🇲🇾 MY | 3887 |
| 19 | 🇿🇦 ZA | 3861 |
| 20 | 🇹🇭 TH | 3774 |
| 21 | 🇵🇱 PL | 3713 |
| 22 | 🇳🇿 NZ | 3090 |
| 23 | 🇵🇭 PH | 3020 |
| 24 | 🇬🇹 GT | 2836 |
| 25 | 🇰🇷 KR | 2657 |
| 26 | 🇭🇷 HR | 2497 |
| 27 | 🇲🇦 MA | 2253 |
| 28 | 🇳🇱 NL | 1989 |
| 29 | 🇲🇪 ME | 1989 |
| 30 | 🇮🇩 ID | 1909 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4687 |
| 2 | Denver International Airport |  | US | 3649 |
| 3 | Tokyo International Airport |  | JP | 2714 |
| 4 | Indira Gandhi International Airport |  | IN | 2713 |
| 5 | Guaymaral Airport |  | CO | 2625 |
| 6 | Harry Reid International Airport |  | US | 2454 |
| 7 | Zurich Airport |  | CH | 2319 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2293 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2266 |
| 10 | La Aurora Airport |  | GT | 2162 |
| 11 | El Dorado International Airport |  | CO | 2080 |
| 12 | Chicago O'Hare International Airport |  | US | 2043 |
| 13 | Salt Lake City International Airport |  | US | 1963 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1922 |
| 15 | Congonhas Airport |  | BR | 1898 |
| 16 | Frankfurt am Main International Airport |  | DE | 1809 |
| 17 | Madrid Barajas International Airport |  | ES | 1754 |
| 18 | Capua Airport |  | IT | 1712 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1671 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1652 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1629 |
| 22 | Macau International Airport |  | MO | 1589 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1571 |
| 24 | Malpensa International Airport |  | IT | 1566 |
| 25 | Charles de Gaulle International Airport |  | FR | 1546 |
| 26 | Charlotte/Douglas International Airport |  | US | 1478 |
| 27 | Ninoy Aquino International Airport |  | PH | 1438 |
| 28 | Kuala Lumpur International Airport |  | MY | 1420 |
| 29 | Barcelona International Airport |  | ES | 1379 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1357 |
| 31 | Bengaluru International Airport |  | IN | 1334 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1320 |
| 33 | Seattle-Tacoma International Airport |  | US | 1318 |
| 34 | Viracopos International Airport |  | BR | 1314 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1295 |
| 36 | Calgary International Airport |  | CA | 1267 |
| 37 | Oslo Gardermoen Airport |  | NO | 1251 |
| 38 | Vitoria/Foronda Airport |  | ES | 1240 |
| 39 | Don Mueang International Airport |  | TH | 1239 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1205 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1071 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 805 | 21m | 244 km | 3,389.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 556 | 1h 7m | 770 km | 7,386.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 538 | 24m | 225 km | 2,087.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 524 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 507 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 377 | 27m | 275 km | 1,786.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 353 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 333 | 1h 50m | 1,423 km | 8,172.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 326 | 44m | 241 km | 1,354.1 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 299 | 21m | 250 km | 1,291.5 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 298 | 22m | 55 km | 283.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 283 | 1h 39m | 1,156 km | 5,645.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 278 | 24m | 218 km | 1,047.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 277 | 19m | 99 km | 474.5 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 275 | 27m | 215 km | 1,018.5 t |
| 20 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 274 | 44m | 555 km | 2,623.7 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 263 | 1h 14m | 961 km | 4,359.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 256 | 19m | 144 km | 636.8 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 252 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 242 | 1h 50m | 1,304 km | 5,444.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 238 | 28m | 152 km | 622.0 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N64RU |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-21 19:01 UTC | 2026-08-21 20:44 UTC | 1h 42m |
| TKR910 | TKR | Hanson Airport (0MT6) | Boundary County Airport (K65S) | 2026-08-21 20:31 UTC | 2026-08-21 20:41 UTC | 10m |
| N74FF |  | Falcon Field (KFFZ) | Falcon Field (KFFZ) | 2026-08-21 19:55 UTC | 2026-08-21 20:38 UTC | 43m |
| ASI985 | ASI | Sugar Land Regional Airport (KSGR) | Easterwood Field (KCLL) | 2026-08-21 19:28 UTC | 2026-08-21 20:32 UTC | 1h 3m |
| N727FW |  | Chester County G O Carlson Airport (KMQS) | Chester County G O Carlson Airport (KMQS) | 2026-08-21 20:12 UTC | 2026-08-21 20:31 UTC | 19m |
| N57FT |  | Colonel James Jabara Airport (KAAO) | Johnson County Executive Airport (KOJC) | 2026-08-21 19:49 UTC | 2026-08-21 20:28 UTC | 38m |
| N190DC |  | Roberts Field/Redmond Municipal Airport (KRDM) | Dry Creek Airpark (OG21) | 2026-08-21 20:09 UTC | 2026-08-21 20:25 UTC | 16m |
| N24NY |  | Linden Airport (KLDJ) | Linden Airport (KLDJ) | 2026-08-21 18:38 UTC | 2026-08-21 20:21 UTC | 1h 43m |
| N15DP |  | Rogers Executive - Carter Field (KROG) | Reno/Tahoe International Airport (KRNO) | 2026-08-21 17:12 UTC | 2026-08-21 20:19 UTC | 3h 6m |
| N265TG |  | Bangor International Airport (KBGR) | Bangor International Airport (KBGR) | 2026-08-21 19:18 UTC | 2026-08-21 20:18 UTC | 59m |
| N42JA |  | Lakewood Airport (KN12) | Lakewood Airport (KN12) | 2026-08-21 20:01 UTC | 2026-08-21 20:17 UTC | 15m |
| CPA811 | Cathay Pacific | General Edward Lawrence Logan International Airport (KBOS) | Zhuhai Airport (ZGSD) | 2026-08-21 05:54 UTC | 2026-08-21 20:15 UTC | 14h 20m |
| N8120M |  | Carroll County Regional/Jack B Poage Field (KDMW) | Lancaster Airport (KLNS) | 2026-08-21 19:45 UTC | 2026-08-21 20:14 UTC | 28m |
| FLAT68 | FLA | Houston Municipal Airport (KM44) | Mccharen Field (KM83) | 2026-08-21 19:50 UTC | 2026-08-21 20:11 UTC | 21m |
| CWA927 | CWA | Bow Island Airport (CEF3) | Taber Airport (CED5) | 2026-08-21 19:59 UTC | 2026-08-21 20:10 UTC | 10m |
| PSSVG | PSS | Tres Marias Airport (SDWL) | Fazenda Morro Vermelho Airport (SDMV) | 2026-08-21 19:42 UTC | 2026-08-21 20:10 UTC | 27m |
| N750U |  | Highland County Airport (KHOC) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-21 19:46 UTC | 2026-08-21 20:06 UTC | 20m |
| TORA21 | TOR | 75OK (75OK) | Farney Field (42KS) | 2026-08-21 19:44 UTC | 2026-08-21 20:06 UTC | 22m |
| N1990H |  | AL79 (AL79) | Geneva Municipal Airport (K33J) | 2026-08-21 19:04 UTC | 2026-08-21 20:05 UTC | 1h 0m |
| TAUNT21 | TAU | 75OK (75OK) | Sopwith Ldg Airport (OK56) | 2026-08-21 19:50 UTC | 2026-08-21 20:03 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
