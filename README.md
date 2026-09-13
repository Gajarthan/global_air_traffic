# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_10:04:23_UTC-green)

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

**Latest saved flight:** 2026-09-13 10:04:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-13 10:04:23 UTC

- **257,079** saved flights
- **76,558** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **257,079** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,109,851.7 tonnes** estimated CO2 emissions
- **180,281,259 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10218 |
| 2 | SkyWest Airlines | 8957 |
| 3 | EJA | 4965 |
| 4 | IndiGo | 4311 |
| 5 | American Airlines | 4064 |
| 6 | Southwest Airlines | 3783 |
| 7 | Delta Air Lines | 3220 |
| 8 | ENY | 3048 |
| 9 | LATAM Airlines | 2470 |
| 10 | AZU | 2394 |
| 11 | Vueling | 2174 |
| 12 | WIF | 2056 |
| 13 | Lufthansa | 2014 |
| 14 | LXJ | 2004 |
| 15 | easyJet | 1758 |
| 16 | Swiss International | 1721 |
| 17 | QLK | 1660 |
| 18 | AXM | 1645 |
| 19 | EJU | 1638 |
| 20 | United Airlines | 1592 |
| 21 | Alaska Airlines | 1527 |
| 22 | All Nippon Airways | 1496 |
| 23 | WMT | 1452 |
| 24 | GLO | 1431 |
| 25 | PGT | 1426 |
| 26 | VIV | 1406 |
| 27 | Air France | 1402 |
| 28 | Wizz Air | 1398 |
| 29 | TKR | 1247 |
| 30 | JetBlue | 1246 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 213353 |
| 2 | 🇪🇸 ES | 16323 |
| 3 | 🇧🇷 BR | 14986 |
| 4 | 🇦🇺 AU | 14658 |
| 5 | 🇨🇦 CA | 14322 |
| 6 | 🇮🇹 IT | 14036 |
| 7 | 🇮🇳 IN | 13522 |
| 8 | 🇩🇪 DE | 12533 |
| 9 | 🇬🇧 GB | 11999 |
| 10 | 🇨🇴 CO | 11504 |
| 11 | 🇫🇷 FR | 10326 |
| 12 | 🇯🇵 JP | 10038 |
| 13 | 🇹🇷 TR | 7734 |
| 14 | 🇬🇷 GR | 7492 |
| 15 | 🇲🇽 MX | 7094 |
| 16 | 🇨🇭 CH | 6903 |
| 17 | 🇳🇴 NO | 6349 |
| 18 | 🇹🇭 TH | 4631 |
| 19 | 🇲🇾 MY | 4423 |
| 20 | 🇿🇦 ZA | 4376 |
| 21 | 🇵🇱 PL | 4263 |
| 22 | 🇳🇿 NZ | 3556 |
| 23 | 🇵🇭 PH | 3460 |
| 24 | 🇬🇹 GT | 3257 |
| 25 | 🇭🇷 HR | 2950 |
| 26 | 🇰🇷 KR | 2945 |
| 27 | 🇲🇦 MA | 2585 |
| 28 | 🇲🇪 ME | 2420 |
| 29 | 🇳🇱 NL | 2316 |
| 30 | 🇮🇩 ID | 2185 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5267 |
| 2 | Denver International Airport |  | US | 4156 |
| 3 | Indira Gandhi International Airport |  | IN | 3111 |
| 4 | Tokyo International Airport |  | JP | 2996 |
| 5 | Guaymaral Airport |  | CO | 2761 |
| 6 | Harry Reid International Airport |  | US | 2723 |
| 7 | Zurich Airport |  | CH | 2694 |
| 8 | El Dorado International Airport |  | CO | 2671 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2593 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2510 |
| 11 | La Aurora Airport |  | GT | 2474 |
| 12 | Salt Lake City International Airport |  | US | 2265 |
| 13 | Chicago O'Hare International Airport |  | US | 2239 |
| 14 | Congonhas Airport |  | BR | 2199 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2098 |
| 16 | Capua Airport |  | IT | 2023 |
| 17 | Madrid Barajas International Airport |  | ES | 2006 |
| 18 | Frankfurt am Main International Airport |  | DE | 1985 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1927 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1857 |
| 21 | Malpensa International Airport |  | IT | 1850 |
| 22 | Charles de Gaulle International Airport |  | FR | 1809 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1808 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1782 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1740 |
| 26 | Macau International Airport |  | MO | 1705 |
| 27 | Ninoy Aquino International Airport |  | PH | 1694 |
| 28 | Barcelona International Airport |  | ES | 1617 |
| 29 | Charlotte/Douglas International Airport |  | US | 1608 |
| 30 | Kuala Lumpur International Airport |  | MY | 1591 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1575 |
| 32 | Viracopos International Airport |  | BR | 1536 |
| 33 | Seattle-Tacoma International Airport |  | US | 1506 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1493 |
| 35 | Don Mueang International Airport |  | TH | 1481 |
| 36 | Calgary International Airport |  | CA | 1471 |
| 37 | Bengaluru International Airport |  | IN | 1461 |
| 38 | Oslo Gardermoen Airport |  | NO | 1450 |
| 39 | Vancouver International Airport |  | CA | 1447 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1389 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 960 | 21m | 244 km | 4,042.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 691 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 644 | 1h 6m | 770 km | 8,555.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 644 | 24m | 225 km | 2,498.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 576 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 418 | 27m | 275 km | 1,980.7 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 416 | 44m | 555 km | 3,983.4 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 410 | 1h 50m | 1,423 km | 10,062.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 387 | 44m | 241 km | 1,607.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 359 | 24m | 218 km | 1,352.5 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 355 | 21m | 250 km | 1,533.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 343 | 23m | 55 km | 326.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 325 | 1h 6m | 706 km | 3,956.9 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 320 | 19m | 99 km | 548.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 316 | 26m | 215 km | 1,170.3 t |
| 19 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 311 | 12m | - | - |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 305 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 297 | 19m | 144 km | 738.8 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 295 | 1h 14m | 961 km | 4,889.8 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 275 | 1h 50m | 1,304 km | 6,186.8 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 271 | 41m | 535 km | 2,502.9 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 270 | 28m | 152 km | 705.6 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AIQ243 | AIQ | New Chitose Airport (RJCC) | Hsinchu Air Base (RCPO) | 2026-09-13 06:12 UTC | 2026-09-13 10:04 UTC | 3h 51m |
| DMDMP | DMD | Vilsbiburg Airport (EDMP) | Innsbruck Airport (LOWI) | 2026-09-13 08:49 UTC | 2026-09-13 09:48 UTC | 58m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Zhuhai Airport (ZGSD) | 2026-09-12 19:09 UTC | 2026-09-13 09:38 UTC | 14h 28m |
| VPCCQ | VPC | Shenzhen Bao'an International Airport (ZGSZ) | Macau International Airport (VMMC) | 2026-09-13 09:29 UTC | 2026-09-13 09:38 UTC | 8m |
| GLEAM | GLE | Lausanne-la Blecherette Airport (LSGL) | Bex Airport (LSGB) | 2026-09-13 09:06 UTC | 2026-09-13 09:36 UTC | 30m |
| THY24 | Turkish Airlines | Istanbul Airport (LTFM) | Hsinchu Air Base (RCPO) | 2026-09-12 22:44 UTC | 2026-09-13 09:30 UTC | 10h 46m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-09-12 21:39 UTC | 2026-09-13 09:25 UTC | 11h 46m |
| SPMOC | SPM | Pobiednik Wielki Airport (EPKP) | Pobiednik Wielki Airport (EPKP) | 2026-09-13 08:24 UTC | 2026-09-13 09:24 UTC | 59m |
| SHA123 | SHA | Tribhuvan International Airport (VNKT) | Tulsipur Airport (VNDG) | 2026-09-13 08:47 UTC | 2026-09-13 09:21 UTC | 33m |
| HKE114 | HKE | Chek Lap Kok International Airport (VHHH) | Hsinchu Air Base (RCPO) | 2026-09-13 08:06 UTC | 2026-09-13 09:18 UTC | 1h 11m |
| ZSDBY | ZSD | O. R. Tambo International Airport (FAOR) | Hartebeespoortdam Airport (FAHB) | 2026-09-13 08:37 UTC | 2026-09-13 09:16 UTC | 38m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Macau International Airport (VMMC) | 2026-09-12 22:01 UTC | 2026-09-13 09:15 UTC | 11h 14m |
| DEEWY | DEE | Tannheim Airport (EDMT) | Tannheim Airport (EDMT) | 2026-09-13 08:05 UTC | 2026-09-13 09:13 UTC | 1h 8m |
| THA634 | Thai Airways | Suvarnabhumi Airport (VTBS) | Hsinchu Air Base (RCPO) | 2026-09-13 06:00 UTC | 2026-09-13 09:12 UTC | 3h 11m |
| QLK1537 | QLK | Canberra International Airport (YSCB) | Melbourne International Airport (YMML) | 2026-09-13 08:09 UTC | 2026-09-13 09:09 UTC | 1h 0m |
| CPA472 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Hsinchu Air Base (RCPO) | 2026-09-13 07:53 UTC | 2026-09-13 09:09 UTC | 1h 15m |
| JME605R | JME | Oxford (Kidlington) Airport (EGTK) | Nice-Cote d'Azur Airport (LFMN) | 2026-09-13 07:30 UTC | 2026-09-13 09:06 UTC | 1h 35m |
| LNK655A | LNK | Cape Town International Airport (FACT) | Lydenburg Airport (FALL) | 2026-09-13 07:13 UTC | 2026-09-13 09:04 UTC | 1h 51m |
| KLM1523 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Bilbao Airport (LEBB) | 2026-09-13 07:27 UTC | 2026-09-13 09:03 UTC | 1h 35m |
| ZSMLE | ZSM | Malmesbury Airport (FAMY) | Malmesbury Airport (FAMY) | 2026-09-13 08:55 UTC | 2026-09-13 09:02 UTC | 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
