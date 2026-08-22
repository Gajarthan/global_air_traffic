# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_06:28:37_UTC-green)

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

**Latest saved flight:** 2026-08-22 06:28:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-22 06:28:37 UTC

- **224,729** saved flights
- **70,039** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **224,729** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,706,689.8 tonnes** estimated CO2 emissions
- **156,909,550 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8997 |
| 2 | SkyWest Airlines | 7997 |
| 3 | EJA | 4353 |
| 4 | IndiGo | 3797 |
| 5 | American Airlines | 3705 |
| 6 | Southwest Airlines | 3524 |
| 7 | Delta Air Lines | 2878 |
| 8 | ENY | 2759 |
| 9 | LATAM Airlines | 2140 |
| 10 | AZU | 2072 |
| 11 | Vueling | 1890 |
| 12 | Lufthansa | 1845 |
| 13 | WIF | 1788 |
| 14 | LXJ | 1776 |
| 15 | easyJet | 1551 |
| 16 | Swiss International | 1492 |
| 17 | AXM | 1479 |
| 18 | QLK | 1417 |
| 19 | United Airlines | 1417 |
| 20 | EJU | 1406 |
| 21 | Alaska Airlines | 1369 |
| 22 | All Nippon Airways | 1348 |
| 23 | GLO | 1244 |
| 24 | PGT | 1232 |
| 25 | VIV | 1231 |
| 26 | Air France | 1215 |
| 27 | WMT | 1195 |
| 28 | Wizz Air | 1155 |
| 29 | JetBlue | 1129 |
| 30 | AEE | 1119 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 188709 |
| 2 | 🇪🇸 ES | 14368 |
| 3 | 🇧🇷 BR | 13049 |
| 4 | 🇦🇺 AU | 12748 |
| 5 | 🇨🇦 CA | 12478 |
| 6 | 🇮🇹 IT | 11993 |
| 7 | 🇮🇳 IN | 11836 |
| 8 | 🇩🇪 DE | 11045 |
| 9 | 🇬🇧 GB | 10515 |
| 10 | 🇨🇴 CO | 9256 |
| 11 | 🇯🇵 JP | 9134 |
| 12 | 🇫🇷 FR | 8938 |
| 13 | 🇹🇷 TR | 6552 |
| 14 | 🇬🇷 GR | 6538 |
| 15 | 🇲🇽 MX | 6259 |
| 16 | 🇨🇭 CH | 5891 |
| 17 | 🇳🇴 NO | 5563 |
| 18 | 🇲🇾 MY | 3933 |
| 19 | 🇿🇦 ZA | 3863 |
| 20 | 🇹🇭 TH | 3826 |
| 21 | 🇵🇱 PL | 3719 |
| 22 | 🇳🇿 NZ | 3136 |
| 23 | 🇵🇭 PH | 3060 |
| 24 | 🇬🇹 GT | 2850 |
| 25 | 🇰🇷 KR | 2668 |
| 26 | 🇭🇷 HR | 2507 |
| 27 | 🇲🇦 MA | 2256 |
| 28 | 🇳🇱 NL | 1992 |
| 29 | 🇲🇪 ME | 1991 |
| 30 | 🇮🇩 ID | 1933 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4706 |
| 2 | Denver International Airport |  | US | 3670 |
| 3 | Tokyo International Airport |  | JP | 2734 |
| 4 | Indira Gandhi International Airport |  | IN | 2727 |
| 5 | Guaymaral Airport |  | CO | 2630 |
| 6 | Harry Reid International Airport |  | US | 2465 |
| 7 | Zurich Airport |  | CH | 2322 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2301 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2271 |
| 10 | La Aurora Airport |  | GT | 2172 |
| 11 | El Dorado International Airport |  | CO | 2080 |
| 12 | Chicago O'Hare International Airport |  | US | 2048 |
| 13 | Salt Lake City International Airport |  | US | 1979 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1926 |
| 15 | Congonhas Airport |  | BR | 1909 |
| 16 | Frankfurt am Main International Airport |  | DE | 1814 |
| 17 | Madrid Barajas International Airport |  | ES | 1755 |
| 18 | Capua Airport |  | IT | 1721 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1677 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1667 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1634 |
| 22 | Macau International Airport |  | MO | 1591 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1585 |
| 24 | Malpensa International Airport |  | IT | 1573 |
| 25 | Charles de Gaulle International Airport |  | FR | 1548 |
| 26 | Charlotte/Douglas International Airport |  | US | 1483 |
| 27 | Ninoy Aquino International Airport |  | PH | 1461 |
| 28 | Kuala Lumpur International Airport |  | MY | 1435 |
| 29 | Barcelona International Airport |  | ES | 1385 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1368 |
| 31 | Bengaluru International Airport |  | IN | 1337 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1333 |
| 33 | Seattle-Tacoma International Airport |  | US | 1328 |
| 34 | Viracopos International Airport |  | BR | 1322 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1303 |
| 36 | Calgary International Airport |  | CA | 1279 |
| 37 | Don Mueang International Airport |  | TH | 1256 |
| 38 | Oslo Gardermoen Airport |  | NO | 1251 |
| 39 | Vitoria/Foronda Airport |  | ES | 1240 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1208 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1072 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 815 | 21m | 244 km | 3,431.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 559 | 1h 7m | 770 km | 7,425.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 551 | 24m | 225 km | 2,137.6 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 527 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 510 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 377 | 27m | 275 km | 1,786.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 354 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 337 | 1h 50m | 1,423 km | 8,270.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 326 | 44m | 241 km | 1,354.1 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 299 | 21m | 250 km | 1,291.5 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 298 | 22m | 55 km | 283.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 286 | 1h 38m | 1,156 km | 5,705.6 t |
| 17 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 283 | 44m | 555 km | 2,709.9 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 281 | 24m | 218 km | 1,058.6 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 280 | 19m | 99 km | 479.6 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 275 | 27m | 215 km | 1,018.5 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 264 | 1h 14m | 961 km | 4,375.9 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 258 | 12m | - | - |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 256 | 19m | 144 km | 636.8 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 244 | 1h 50m | 1,304 km | 5,489.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 238 | 28m | 152 km | 622.0 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AE930 |  | Sydney Bankstown Airport (YSBK) | Bathurst Airport (YBTH) | 2026-08-22 06:08 UTC | 2026-08-22 06:28 UTC | 20m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-22 05:55 UTC | 2026-08-22 06:25 UTC | 29m |
| WIF152 | WIF | Ørsta-Volda Airport Hovden (ENOV) | Sogndal Airport (ENSG) | 2026-08-22 06:09 UTC | 2026-08-22 06:24 UTC | 15m |
| FJIRZ | FJI | Toulouse-Lasbordes Airport (LFCL) | Toulouse-Lasbordes Airport (LFCL) | 2026-08-22 05:41 UTC | 2026-08-22 06:13 UTC | 31m |
| N909CS |  | Lanai Airport (PHNY) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-08-22 05:03 UTC | 2026-08-22 06:05 UTC | 1h 1m |
| DLH6VV | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hannover Airport (EDDV) | 2026-08-22 05:22 UTC | 2026-08-22 05:57 UTC | 35m |
| AIQ1040 | AIQ | Don Mueang International Airport (VTBD) | Xieng Khouang Airport (VLXK) | 2026-08-22 05:12 UTC | 2026-08-22 05:55 UTC | 42m |
| IGO7339 | IndiGo | Tambaram Air Force Station (VOTX) | Kovilpatti Airport (VO26) | 2026-08-22 04:46 UTC | 2026-08-22 05:54 UTC | 1h 8m |
| ASA1122 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-08-22 05:24 UTC | 2026-08-22 05:48 UTC | 23m |
| N717PA |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-08-22 05:22 UTC | 2026-08-22 05:47 UTC | 25m |
| ACA838 | Air Canada | Vancouver International Airport (CYVR) | Frankfurt am Main International Airport (EDDF) | 2026-08-21 20:43 UTC | 2026-08-22 05:47 UTC | 9h 3m |
| AEE348 | AEE | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-08-22 05:25 UTC | 2026-08-22 05:45 UTC | 19m |
| DLH9TT | Lufthansa | Munich International Airport (EDDM) | Hannover Airport (EDDV) | 2026-08-22 04:56 UTC | 2026-08-22 05:45 UTC | 48m |
| SWR9PW | Swiss International | Geneva Cointrin International Airport (LSGG) | Palma De Mallorca Airport (LEPA) | 2026-08-22 04:29 UTC | 2026-08-22 05:44 UTC | 1h 14m |
| LNI | LNI | Cervantes Airport (YCVS) | Jurien Bay Airport (YJNB) | 2026-08-22 05:30 UTC | 2026-08-22 05:43 UTC | 13m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-22 05:30 UTC | 2026-08-22 05:40 UTC | 10m |
| AIQ3225 | AIQ | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 2026-08-22 04:54 UTC | 2026-08-22 05:40 UTC | 46m |
| IGO7626 | IndiGo | Safdarjung Airport (VIDD) | Jaipur International Airport (VIJP) | 2026-08-22 05:03 UTC | 2026-08-22 05:38 UTC | 34m |
| RYR5GE | Ryanair | Karlsruhe Baden-Baden Airport (EDSB) | Otocac Airport (LDRO) | 2026-08-22 04:42 UTC | 2026-08-22 05:37 UTC | 55m |
| AIQ3003 | AIQ | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 2026-08-22 04:51 UTC | 2026-08-22 05:35 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
