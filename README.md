# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_17:19:58_UTC-green)

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

**Latest saved flight:** 2026-08-21 17:19:58 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 17:19:58 UTC

- **222,933** saved flights
- **69,671** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **222,933** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,683,577.7 tonnes** estimated CO2 emissions
- **155,569,722 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8935 |
| 2 | SkyWest Airlines | 7907 |
| 3 | EJA | 4309 |
| 4 | IndiGo | 3778 |
| 5 | American Airlines | 3682 |
| 6 | Southwest Airlines | 3497 |
| 7 | Delta Air Lines | 2857 |
| 8 | ENY | 2734 |
| 9 | LATAM Airlines | 2122 |
| 10 | AZU | 2048 |
| 11 | Vueling | 1883 |
| 12 | Lufthansa | 1841 |
| 13 | WIF | 1784 |
| 14 | LXJ | 1758 |
| 15 | easyJet | 1542 |
| 16 | Swiss International | 1483 |
| 17 | AXM | 1466 |
| 18 | QLK | 1405 |
| 19 | EJU | 1396 |
| 20 | United Airlines | 1395 |
| 21 | Alaska Airlines | 1353 |
| 22 | All Nippon Airways | 1333 |
| 23 | GLO | 1222 |
| 24 | PGT | 1222 |
| 25 | VIV | 1211 |
| 26 | Air France | 1210 |
| 27 | WMT | 1187 |
| 28 | Wizz Air | 1148 |
| 29 | JetBlue | 1119 |
| 30 | AEE | 1112 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 187090 |
| 2 | 🇪🇸 ES | 14298 |
| 3 | 🇧🇷 BR | 12905 |
| 4 | 🇦🇺 AU | 12653 |
| 5 | 🇨🇦 CA | 12311 |
| 6 | 🇮🇹 IT | 11885 |
| 7 | 🇮🇳 IN | 11786 |
| 8 | 🇩🇪 DE | 11008 |
| 9 | 🇬🇧 GB | 10459 |
| 10 | 🇨🇴 CO | 9193 |
| 11 | 🇯🇵 JP | 9054 |
| 12 | 🇫🇷 FR | 8892 |
| 13 | 🇬🇷 GR | 6504 |
| 14 | 🇹🇷 TR | 6469 |
| 15 | 🇲🇽 MX | 6176 |
| 16 | 🇨🇭 CH | 5869 |
| 17 | 🇳🇴 NO | 5550 |
| 18 | 🇲🇾 MY | 3886 |
| 19 | 🇿🇦 ZA | 3851 |
| 20 | 🇹🇭 TH | 3774 |
| 21 | 🇵🇱 PL | 3703 |
| 22 | 🇳🇿 NZ | 3089 |
| 23 | 🇵🇭 PH | 3020 |
| 24 | 🇬🇹 GT | 2814 |
| 25 | 🇰🇷 KR | 2657 |
| 26 | 🇭🇷 HR | 2488 |
| 27 | 🇲🇦 MA | 2243 |
| 28 | 🇳🇱 NL | 1981 |
| 29 | 🇲🇪 ME | 1981 |
| 30 | 🇮🇩 ID | 1909 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4666 |
| 2 | Denver International Airport |  | US | 3628 |
| 3 | Tokyo International Airport |  | JP | 2714 |
| 4 | Indira Gandhi International Airport |  | IN | 2708 |
| 5 | Guaymaral Airport |  | CO | 2622 |
| 6 | Harry Reid International Airport |  | US | 2447 |
| 7 | Zurich Airport |  | CH | 2309 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2283 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2261 |
| 10 | La Aurora Airport |  | GT | 2145 |
| 11 | El Dorado International Airport |  | CO | 2079 |
| 12 | Chicago O'Hare International Airport |  | US | 2029 |
| 13 | Salt Lake City International Airport |  | US | 1949 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1914 |
| 15 | Congonhas Airport |  | BR | 1889 |
| 16 | Frankfurt am Main International Airport |  | DE | 1809 |
| 17 | Madrid Barajas International Airport |  | ES | 1744 |
| 18 | Capua Airport |  | IT | 1704 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1665 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1645 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1627 |
| 22 | Macau International Airport |  | MO | 1589 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1571 |
| 24 | Malpensa International Airport |  | IT | 1564 |
| 25 | Charles de Gaulle International Airport |  | FR | 1539 |
| 26 | Charlotte/Douglas International Airport |  | US | 1475 |
| 27 | Ninoy Aquino International Airport |  | PH | 1438 |
| 28 | Kuala Lumpur International Airport |  | MY | 1419 |
| 29 | Barcelona International Airport |  | ES | 1374 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1349 |
| 31 | Bengaluru International Airport |  | IN | 1334 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1316 |
| 33 | Seattle-Tacoma International Airport |  | US | 1315 |
| 34 | Viracopos International Airport |  | BR | 1308 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1272 |
| 36 | Calgary International Airport |  | CA | 1258 |
| 37 | Oslo Gardermoen Airport |  | NO | 1245 |
| 38 | Don Mueang International Airport |  | TH | 1239 |
| 39 | Vitoria/Foronda Airport |  | ES | 1238 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1201 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1070 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 802 | 21m | 244 km | 3,377.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 556 | 1h 7m | 770 km | 7,386.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 538 | 24m | 225 km | 2,087.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 513 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 503 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 376 | 27m | 275 km | 1,781.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 353 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 331 | 1h 50m | 1,423 km | 8,123.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 326 | 44m | 241 km | 1,354.1 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 298 | 22m | 55 km | 283.2 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 298 | 21m | 250 km | 1,287.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 282 | 1h 39m | 1,156 km | 5,625.8 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 278 | 24m | 218 km | 1,047.3 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 275 | 27m | 215 km | 1,018.5 t |
| 19 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 274 | 44m | 555 km | 2,623.7 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 274 | 19m | 99 km | 469.3 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 263 | 1h 14m | 961 km | 4,359.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 254 | 19m | 144 km | 631.8 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 252 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 241 | 1h 50m | 1,304 km | 5,421.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 236 | 28m | 152 km | 616.8 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N426LM |  | Albuquerque International Sunport Airport (KABQ) | NM74 (NM74) | 2026-08-21 17:02 UTC | 2026-08-21 17:19 UTC | 17m |
| GRYDR18 | GRY | Westchester County Airport (KHPN) | Laguardia Airport (KLGA) | 2026-08-21 15:43 UTC | 2026-08-21 17:19 UTC | 1h 36m |
| N580ET |  | Rocky Mountain Metro Airport (KBJC) | Fort Morgan Municipal Airport (KFMM) | 2026-08-21 16:33 UTC | 2026-08-21 17:19 UTC | 46m |
| SCU35 | SCU | Tulsa Riverside Airport (KRVS) | Tulsa Riverside Airport (KRVS) | 2026-08-21 16:33 UTC | 2026-08-21 17:18 UTC | 45m |
| PTA271 | PTA | Incheon International Airport (RKSI) | Noi Bai International Airport (VVNB) | 2026-08-21 11:12 UTC | 2026-08-21 17:18 UTC | 6h 5m |
| DHX721 | DHX | Bahrain International Airport (OBBI) | Macau International Airport (VMMC) | 2026-08-21 09:23 UTC | 2026-08-21 17:15 UTC | 7h 52m |
| N801JA |  | Pru Field (K33S) | Pru Field (K33S) | 2026-08-21 17:00 UTC | 2026-08-21 17:15 UTC | 15m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-08-21 16:54 UTC | 2026-08-21 17:13 UTC | 18m |
| N443FC |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-08-21 16:41 UTC | 2026-08-21 17:12 UTC | 30m |
| N26ND |  | Las Cruces International Airport (KLRU) | Las Cruces International Airport (KLRU) | 2026-08-21 16:26 UTC | 2026-08-21 17:11 UTC | 45m |
| N6025E |  | Boeing Field/King County International Airport (KBFI) | Seattle Paine Field International Airport (KPAE) | 2026-08-21 16:57 UTC | 2026-08-21 17:10 UTC | 13m |
| N739WR |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-08-21 16:37 UTC | 2026-08-21 17:10 UTC | 32m |
| CGYAF | CGY | CPJ6 (CPJ6) | CPJ6 (CPJ6) | 2026-08-21 16:21 UTC | 2026-08-21 17:09 UTC | 47m |
| DOG1 | DOG | North Island Nas (Halsey Field) Airport (KNZY) | Catalina Airport (KAVX) | 2026-08-21 16:40 UTC | 2026-08-21 17:07 UTC | 26m |
| N4381L |  | Blairstown Airport (K1N7) | Blairstown Airport (K1N7) | 2026-08-21 16:30 UTC | 2026-08-21 17:06 UTC | 36m |
| N257MM |  | Adirondack Regional Airport (KSLK) | Lancaster Airport (KLNS) | 2026-08-21 15:59 UTC | 2026-08-21 17:06 UTC | 1h 6m |
| SH235 |  | Skypark Estates Owners Assoc Airport (18FD) | South Alabama Regional At Bill Benton Field (K79J) | 2026-08-21 16:40 UTC | 2026-08-21 17:05 UTC | 24m |
| BALL28 | BAL | Flysooner Field (OK50) | Cottonwood Airport (OK66) | 2026-08-21 16:53 UTC | 2026-08-21 17:01 UTC | 8m |
| N591SS |  | Reno/Tahoe International Airport (KRNO) | Silver Springs Airport (KSPZ) | 2026-08-21 16:53 UTC | 2026-08-21 17:00 UTC | 7m |
| WMU60 | WMU | Battle Creek Executive At Kellogg Field (KBTL) | MI56 (MI56) | 2026-08-21 16:42 UTC | 2026-08-21 16:57 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
