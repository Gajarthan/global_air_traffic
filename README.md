# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_07:28:15_UTC-green)

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

**Latest saved flight:** 2026-08-22 07:28:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-22 07:28:15 UTC

- **224,808** saved flights
- **70,056** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **224,808** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,707,680.6 tonnes** estimated CO2 emissions
- **156,966,991 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9006 |
| 2 | SkyWest Airlines | 7997 |
| 3 | EJA | 4353 |
| 4 | IndiGo | 3800 |
| 5 | American Airlines | 3705 |
| 6 | Southwest Airlines | 3524 |
| 7 | Delta Air Lines | 2878 |
| 8 | ENY | 2759 |
| 9 | LATAM Airlines | 2140 |
| 10 | AZU | 2073 |
| 11 | Vueling | 1896 |
| 12 | Lufthansa | 1847 |
| 13 | WIF | 1788 |
| 14 | LXJ | 1776 |
| 15 | easyJet | 1551 |
| 16 | Swiss International | 1492 |
| 17 | AXM | 1481 |
| 18 | QLK | 1417 |
| 19 | United Airlines | 1417 |
| 20 | EJU | 1409 |
| 21 | Alaska Airlines | 1369 |
| 22 | All Nippon Airways | 1349 |
| 23 | GLO | 1244 |
| 24 | PGT | 1233 |
| 25 | VIV | 1231 |
| 26 | Air France | 1215 |
| 27 | WMT | 1195 |
| 28 | Wizz Air | 1156 |
| 29 | JetBlue | 1129 |
| 30 | AEE | 1119 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 188713 |
| 2 | 🇪🇸 ES | 14386 |
| 3 | 🇧🇷 BR | 13051 |
| 4 | 🇦🇺 AU | 12752 |
| 5 | 🇨🇦 CA | 12478 |
| 6 | 🇮🇹 IT | 12009 |
| 7 | 🇮🇳 IN | 11844 |
| 8 | 🇩🇪 DE | 11053 |
| 9 | 🇬🇧 GB | 10518 |
| 10 | 🇨🇴 CO | 9256 |
| 11 | 🇯🇵 JP | 9144 |
| 12 | 🇫🇷 FR | 8942 |
| 13 | 🇹🇷 TR | 6558 |
| 14 | 🇬🇷 GR | 6545 |
| 15 | 🇲🇽 MX | 6259 |
| 16 | 🇨🇭 CH | 5895 |
| 17 | 🇳🇴 NO | 5563 |
| 18 | 🇲🇾 MY | 3943 |
| 19 | 🇿🇦 ZA | 3871 |
| 20 | 🇹🇭 TH | 3827 |
| 21 | 🇵🇱 PL | 3721 |
| 22 | 🇳🇿 NZ | 3136 |
| 23 | 🇵🇭 PH | 3062 |
| 24 | 🇬🇹 GT | 2850 |
| 25 | 🇰🇷 KR | 2669 |
| 26 | 🇭🇷 HR | 2509 |
| 27 | 🇲🇦 MA | 2256 |
| 28 | 🇲🇪 ME | 1995 |
| 29 | 🇳🇱 NL | 1992 |
| 30 | 🇮🇩 ID | 1934 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4706 |
| 2 | Denver International Airport |  | US | 3670 |
| 3 | Tokyo International Airport |  | JP | 2736 |
| 4 | Indira Gandhi International Airport |  | IN | 2728 |
| 5 | Guaymaral Airport |  | CO | 2630 |
| 6 | Harry Reid International Airport |  | US | 2465 |
| 7 | Zurich Airport |  | CH | 2323 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2301 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2271 |
| 10 | La Aurora Airport |  | GT | 2172 |
| 11 | El Dorado International Airport |  | CO | 2080 |
| 12 | Chicago O'Hare International Airport |  | US | 2048 |
| 13 | Salt Lake City International Airport |  | US | 1979 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1926 |
| 15 | Congonhas Airport |  | BR | 1909 |
| 16 | Frankfurt am Main International Airport |  | DE | 1814 |
| 17 | Madrid Barajas International Airport |  | ES | 1757 |
| 18 | Capua Airport |  | IT | 1723 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1677 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1667 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1634 |
| 22 | Macau International Airport |  | MO | 1591 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1586 |
| 24 | Malpensa International Airport |  | IT | 1576 |
| 25 | Charles de Gaulle International Airport |  | FR | 1548 |
| 26 | Charlotte/Douglas International Airport |  | US | 1483 |
| 27 | Ninoy Aquino International Airport |  | PH | 1462 |
| 28 | Kuala Lumpur International Airport |  | MY | 1437 |
| 29 | Barcelona International Airport |  | ES | 1388 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1368 |
| 31 | Bengaluru International Airport |  | IN | 1338 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1333 |
| 33 | Seattle-Tacoma International Airport |  | US | 1328 |
| 34 | Viracopos International Airport |  | BR | 1323 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1303 |
| 36 | Calgary International Airport |  | CA | 1279 |
| 37 | Don Mueang International Airport |  | TH | 1257 |
| 38 | Oslo Gardermoen Airport |  | NO | 1251 |
| 39 | Vitoria/Foronda Airport |  | ES | 1241 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1208 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1072 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 815 | 21m | 244 km | 3,431.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 560 | 1h 7m | 770 km | 7,439.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 552 | 24m | 225 km | 2,141.5 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 527 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 510 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
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
| VHRIO | VHR | VGZR (VGZR) | Naypyidaw Airport (VYEL) | 2026-08-22 05:57 UTC | 2026-08-22 07:28 UTC | 1h 30m |
| LBQ791 | LBQ | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | Teterboro Airport (KTEB) | 2026-08-22 06:40 UTC | 2026-08-22 07:19 UTC | 38m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-22 06:39 UTC | 2026-08-22 07:07 UTC | 28m |
| N400DP |  | Pheasant Wings Airport (26OK) | Addison Airport (KADS) | 2026-08-22 06:06 UTC | 2026-08-22 07:07 UTC | 1h 0m |
| SJX821 | SJX | Kansai International Airport (RJBB) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-22 04:42 UTC | 2026-08-22 06:54 UTC | 2h 12m |
| JA123F |  | Gifu Airport (RJNG) | Okadama Airport (RJCO) | 2026-08-22 05:07 UTC | 2026-08-22 06:53 UTC | 1h 45m |
| SEJYV | SEJ | Muenster Aero Airport (LSPU) | Biella / Cerrione Airport (LILE) | 2026-08-22 06:12 UTC | 2026-08-22 06:44 UTC | 32m |
| UZB274 | UZB | Erzurum International Airport (LTCE) | Ukhta Airport (UUYH) | 2026-08-21 22:01 UTC | 2026-08-22 06:43 UTC | 8h 42m |
| RYR9081 | Ryanair | Pescara International Airport (LIBP) | Malpensa International Airport (LIMC) | 2026-08-22 05:32 UTC | 2026-08-22 06:42 UTC | 1h 10m |
| GPJCD | GPJ | Norwich International Airport (EGSH) | Norwich International Airport (EGSH) | 2026-08-22 06:39 UTC | 2026-08-22 06:40 UTC | 0m |
| RYR77GB | Ryanair | Manchester Airport (EGCC) | Dublin Airport (EIDW) | 2026-08-22 05:56 UTC | 2026-08-22 06:37 UTC | 40m |
| AUA871 | Austrian Airlines | Vienna International Airport (LOWW) | Diagoras Airport (LGRP) | 2026-08-22 04:14 UTC | 2026-08-22 06:31 UTC | 2h 17m |
| DLH3FF | Lufthansa | Munich International Airport (EDDM) | Stuttgart Airport (EDDS) | 2026-08-22 06:05 UTC | 2026-08-22 06:30 UTC | 25m |
| RYR526B | Ryanair | Francisco de Sá Carneiro Airport (LPPR) | Toulouse-Blagnac Airport (LFBO) | 2026-08-22 05:14 UTC | 2026-08-22 06:30 UTC | 1h 15m |
| AE930 |  | Sydney Bankstown Airport (YSBK) | Bathurst Airport (YBTH) | 2026-08-22 06:08 UTC | 2026-08-22 06:28 UTC | 20m |
| VOE60UK | VOE | Torino / Caselle International Airport (LIMF) | Ghisonaccia Alzitone Airport (LFKG) | 2026-08-22 05:39 UTC | 2026-08-22 06:28 UTC | 48m |
| ANE87CJ | ANE | Madrid Barajas International Airport (LEMD) | La Morgal Airport (LEMR) | 2026-08-22 05:54 UTC | 2026-08-22 06:28 UTC | 33m |
| VLG1DP | Vueling | Barcelona International Airport (LEBL) | Pamplona Airport (LEPP) | 2026-08-22 05:47 UTC | 2026-08-22 06:26 UTC | 39m |
| MNE157 | MNE | Belgrade Nikola Tesla Airport (LYBE) | Niksic Airport (LYNK) | 2026-08-22 06:04 UTC | 2026-08-22 06:26 UTC | 22m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-22 05:55 UTC | 2026-08-22 06:25 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
