# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_23:39:08_UTC-green)

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

**Latest saved flight:** 2026-08-23 23:39:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 23:39:08 UTC

- **230,537** saved flights
- **71,134** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **230,537** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,779,998.5 tonnes** estimated CO2 emissions
- **161,159,335 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9252 |
| 2 | SkyWest Airlines | 8195 |
| 3 | EJA | 4467 |
| 4 | IndiGo | 3883 |
| 5 | American Airlines | 3782 |
| 6 | Southwest Airlines | 3568 |
| 7 | Delta Air Lines | 2951 |
| 8 | ENY | 2817 |
| 9 | LATAM Airlines | 2223 |
| 10 | AZU | 2148 |
| 11 | Vueling | 1958 |
| 12 | Lufthansa | 1874 |
| 13 | LXJ | 1822 |
| 14 | WIF | 1813 |
| 15 | easyJet | 1608 |
| 16 | Swiss International | 1538 |
| 17 | AXM | 1520 |
| 18 | EJU | 1470 |
| 19 | United Airlines | 1467 |
| 20 | QLK | 1453 |
| 21 | Alaska Airlines | 1389 |
| 22 | All Nippon Airways | 1372 |
| 23 | GLO | 1289 |
| 24 | VIV | 1267 |
| 25 | WMT | 1262 |
| 26 | PGT | 1259 |
| 27 | Air France | 1253 |
| 28 | Wizz Air | 1212 |
| 29 | JetBlue | 1149 |
| 30 | AEE | 1147 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 192555 |
| 2 | 🇪🇸 ES | 14784 |
| 3 | 🇧🇷 BR | 13512 |
| 4 | 🇦🇺 AU | 12993 |
| 5 | 🇨🇦 CA | 12729 |
| 6 | 🇮🇹 IT | 12477 |
| 7 | 🇮🇳 IN | 12103 |
| 8 | 🇩🇪 DE | 11329 |
| 9 | 🇬🇧 GB | 10845 |
| 10 | 🇨🇴 CO | 9590 |
| 11 | 🇯🇵 JP | 9321 |
| 12 | 🇫🇷 FR | 9219 |
| 13 | 🇹🇷 TR | 6802 |
| 14 | 🇬🇷 GR | 6771 |
| 15 | 🇲🇽 MX | 6416 |
| 16 | 🇨🇭 CH | 6116 |
| 17 | 🇳🇴 NO | 5659 |
| 18 | 🇲🇾 MY | 4063 |
| 19 | 🇿🇦 ZA | 4015 |
| 20 | 🇹🇭 TH | 3997 |
| 21 | 🇵🇱 PL | 3827 |
| 22 | 🇳🇿 NZ | 3189 |
| 23 | 🇵🇭 PH | 3152 |
| 24 | 🇬🇹 GT | 2903 |
| 25 | 🇰🇷 KR | 2708 |
| 26 | 🇭🇷 HR | 2638 |
| 27 | 🇲🇦 MA | 2337 |
| 28 | 🇲🇪 ME | 2112 |
| 29 | 🇳🇱 NL | 2059 |
| 30 | 🇮🇩 ID | 1978 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4819 |
| 2 | Denver International Airport |  | US | 3754 |
| 3 | Indira Gandhi International Airport |  | IN | 2801 |
| 4 | Tokyo International Airport |  | JP | 2783 |
| 5 | Guaymaral Airport |  | CO | 2654 |
| 6 | Harry Reid International Airport |  | US | 2489 |
| 7 | Zurich Airport |  | CH | 2403 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2360 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2318 |
| 10 | La Aurora Airport |  | GT | 2212 |
| 11 | El Dorado International Airport |  | CO | 2139 |
| 12 | Chicago O'Hare International Airport |  | US | 2094 |
| 13 | Salt Lake City International Airport |  | US | 2030 |
| 14 | Congonhas Airport |  | BR | 1970 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1953 |
| 16 | Frankfurt am Main International Airport |  | DE | 1843 |
| 17 | Madrid Barajas International Airport |  | ES | 1808 |
| 18 | Capua Airport |  | IT | 1806 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1736 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1717 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1653 |
| 22 | Malpensa International Airport |  | IT | 1649 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1614 |
| 24 | Charles de Gaulle International Airport |  | FR | 1598 |
| 25 | Macau International Airport |  | MO | 1597 |
| 26 | Ninoy Aquino International Airport |  | PH | 1514 |
| 27 | Charlotte/Douglas International Airport |  | US | 1507 |
| 28 | Kuala Lumpur International Airport |  | MY | 1472 |
| 29 | Barcelona International Airport |  | ES | 1442 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1399 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1388 |
| 32 | Viracopos International Airport |  | BR | 1374 |
| 33 | Seattle-Tacoma International Airport |  | US | 1360 |
| 34 | Bengaluru International Airport |  | IN | 1358 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1354 |
| 36 | Calgary International Airport |  | CA | 1313 |
| 37 | Don Mueang International Airport |  | TH | 1307 |
| 38 | Oslo Gardermoen Airport |  | NO | 1283 |
| 39 | Vitoria/Foronda Airport |  | ES | 1252 |
| 40 | O. R. Tambo International Airport |  | ZA | 1250 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1076 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 838 | 21m | 244 km | 3,528.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 576 | 1h 6m | 770 km | 7,651.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 569 | 24m | 225 km | 2,207.4 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 563 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 517 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 380 | 27m | 275 km | 1,800.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 353 | 1h 50m | 1,423 km | 8,663.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 334 | 44m | 241 km | 1,387.4 t |
| 11 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 325 | 21m | 250 km | 1,403.8 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 315 | 1h 7m | 706 km | 3,835.1 t |
| 13 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 14 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 310 | 44m | 555 km | 2,968.4 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 307 | 22m | 55 km | 291.8 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 298 | 24m | 218 km | 1,122.7 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 298 | 1h 38m | 1,156 km | 5,945.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 285 | 19m | 99 km | 488.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 280 | 27m | 215 km | 1,037.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 272 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 270 | 1h 14m | 961 km | 4,475.4 t |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 265 | 13m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 262 | 19m | 144 km | 651.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 247 | 1h 50m | 1,304 km | 5,556.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 245 | 28m | 152 km | 640.3 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 241 | 15m | 154 km | 638.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TTW217 | TTW | Tokyo International Airport (RJTT) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-23 20:53 UTC | 2026-08-23 23:39 UTC | 2h 45m |
| N2158S |  | Gilbert Airport (73PA) | Millville Municipal Airport (KMIV) | 2026-08-23 22:51 UTC | 2026-08-23 23:38 UTC | 47m |
| N626LM |  | Sussex Airport (KFWN) | Sussex Airport (KFWN) | 2026-08-23 23:25 UTC | 2026-08-23 23:38 UTC | 12m |
| N841PA |  | Skypark Airport (KBTF) | KU77 (KU77) | 2026-08-23 22:50 UTC | 2026-08-23 23:31 UTC | 41m |
| RFS734 | RFS | Seattle Paine Field International Airport (KPAE) | Arlington Municipal Airport (KAWO) | 2026-08-23 23:16 UTC | 2026-08-23 23:29 UTC | 12m |
| N551MA |  | Montgomery-Gibbs Executive Airport (KMYF) | Borrego Valley Airport (KL08) | 2026-08-23 23:10 UTC | 2026-08-23 23:28 UTC | 17m |
| ZFH | ZFH | Bacchus Marsh Airport (YBSS) | Bacchus Marsh Airport (YBSS) | 2026-08-23 23:00 UTC | 2026-08-23 23:27 UTC | 26m |
| SWA2500 | Southwest Airlines | Noahs Ark Airport (06MO) | Hock Airport (13NE) | 2026-08-23 22:26 UTC | 2026-08-23 23:26 UTC | 1h 0m |
| N15VX |  | Indianapolis Executive Airport (KTYQ) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-08-23 22:05 UTC | 2026-08-23 23:22 UTC | 1h 16m |
| N334VG |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-08-23 22:58 UTC | 2026-08-23 23:20 UTC | 21m |
| N166WC |  | Campbell River Airport (CYBL) | Boeing Field/King County International Airport (KBFI) | 2026-08-23 22:44 UTC | 2026-08-23 23:17 UTC | 33m |
| N115SE |  | Harry Reid International Airport (KLAS) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-23 22:13 UTC | 2026-08-23 23:16 UTC | 1h 3m |
| N955TG |  | Villa Char Mar Airport (1FA9) | Market World Airport (FL16) | 2026-08-23 22:56 UTC | 2026-08-23 23:16 UTC | 19m |
| MSC804 | MSC | Malpensa International Airport (LIMC) | HE12 (HE12) | 2026-08-23 20:04 UTC | 2026-08-23 23:14 UTC | 3h 9m |
| N713SQ |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-08-23 23:07 UTC | 2026-08-23 23:13 UTC | 5m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-23 23:01 UTC | 2026-08-23 23:12 UTC | 10m |
|  |  | Peterborough Airport (YPBH) | Peterborough Airport (YPBH) | 2026-08-23 23:00 UTC | 2026-08-23 23:11 UTC | 11m |
| N365AV |  | Manchester Boston Regional Airport (KMHT) | Moffett Federal Airfield (KNUQ) | 2026-08-23 17:27 UTC | 2026-08-23 23:08 UTC | 5h 41m |
| JA6940 |  | Kisarazu Airport (RJTK) | Kisarazu Airport (RJTK) | 2026-08-23 23:08 UTC | 2026-08-23 23:08 UTC | 0m |
| N74GG |  | Teterboro Airport (KTEB) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-23 17:32 UTC | 2026-08-23 23:07 UTC | 5h 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
