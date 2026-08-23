# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_11:09:10_UTC-green)

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

**Latest saved flight:** 2026-08-23 11:09:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 11:09:10 UTC

- **228,212** saved flights
- **70,652** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **228,212** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,752,433.9 tonnes** estimated CO2 emissions
- **159,561,384 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9160 |
| 2 | SkyWest Airlines | 8104 |
| 3 | EJA | 4393 |
| 4 | IndiGo | 3863 |
| 5 | American Airlines | 3740 |
| 6 | Southwest Airlines | 3549 |
| 7 | Delta Air Lines | 2919 |
| 8 | ENY | 2791 |
| 9 | LATAM Airlines | 2185 |
| 10 | AZU | 2112 |
| 11 | Vueling | 1935 |
| 12 | Lufthansa | 1868 |
| 13 | WIF | 1799 |
| 14 | LXJ | 1790 |
| 15 | easyJet | 1590 |
| 16 | Swiss International | 1522 |
| 17 | AXM | 1517 |
| 18 | QLK | 1448 |
| 19 | EJU | 1445 |
| 20 | United Airlines | 1444 |
| 21 | Alaska Airlines | 1385 |
| 22 | All Nippon Airways | 1371 |
| 23 | GLO | 1265 |
| 24 | VIV | 1253 |
| 25 | PGT | 1251 |
| 26 | WMT | 1244 |
| 27 | Air France | 1241 |
| 28 | Wizz Air | 1185 |
| 29 | JetBlue | 1142 |
| 30 | AEE | 1138 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 190656 |
| 2 | 🇪🇸 ES | 14637 |
| 3 | 🇧🇷 BR | 13296 |
| 4 | 🇦🇺 AU | 12953 |
| 5 | 🇨🇦 CA | 12620 |
| 6 | 🇮🇹 IT | 12293 |
| 7 | 🇮🇳 IN | 12041 |
| 8 | 🇩🇪 DE | 11228 |
| 9 | 🇬🇧 GB | 10728 |
| 10 | 🇨🇴 CO | 9384 |
| 11 | 🇯🇵 JP | 9304 |
| 12 | 🇫🇷 FR | 9128 |
| 13 | 🇹🇷 TR | 6714 |
| 14 | 🇬🇷 GR | 6700 |
| 15 | 🇲🇽 MX | 6358 |
| 16 | 🇨🇭 CH | 6035 |
| 17 | 🇳🇴 NO | 5606 |
| 18 | 🇲🇾 MY | 4049 |
| 19 | 🇿🇦 ZA | 3965 |
| 20 | 🇹🇭 TH | 3962 |
| 21 | 🇵🇱 PL | 3792 |
| 22 | 🇳🇿 NZ | 3169 |
| 23 | 🇵🇭 PH | 3134 |
| 24 | 🇬🇹 GT | 2873 |
| 25 | 🇰🇷 KR | 2703 |
| 26 | 🇭🇷 HR | 2596 |
| 27 | 🇲🇦 MA | 2305 |
| 28 | 🇲🇪 ME | 2068 |
| 29 | 🇳🇱 NL | 2037 |
| 30 | 🇮🇩 ID | 1972 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4771 |
| 2 | Denver International Airport |  | US | 3714 |
| 3 | Indira Gandhi International Airport |  | IN | 2784 |
| 4 | Tokyo International Airport |  | JP | 2778 |
| 5 | Guaymaral Airport |  | CO | 2647 |
| 6 | Harry Reid International Airport |  | US | 2473 |
| 7 | Zurich Airport |  | CH | 2373 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2332 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2303 |
| 10 | La Aurora Airport |  | GT | 2189 |
| 11 | El Dorado International Airport |  | CO | 2084 |
| 12 | Chicago O'Hare International Airport |  | US | 2071 |
| 13 | Salt Lake City International Airport |  | US | 2009 |
| 14 | Congonhas Airport |  | BR | 1940 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1938 |
| 16 | Frankfurt am Main International Airport |  | DE | 1830 |
| 17 | Madrid Barajas International Airport |  | ES | 1780 |
| 18 | Capua Airport |  | IT | 1774 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1703 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1698 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1649 |
| 22 | Malpensa International Airport |  | IT | 1625 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1611 |
| 24 | Macau International Airport |  | MO | 1594 |
| 25 | Charles de Gaulle International Airport |  | FR | 1579 |
| 26 | Ninoy Aquino International Airport |  | PH | 1502 |
| 27 | Charlotte/Douglas International Airport |  | US | 1492 |
| 28 | Kuala Lumpur International Airport |  | MY | 1467 |
| 29 | Barcelona International Airport |  | ES | 1424 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1384 |
| 31 | Bengaluru International Airport |  | IN | 1353 |
| 32 | Enrique Olaya Herrera Airport |  | CO | 1350 |
| 33 | Viracopos International Airport |  | BR | 1348 |
| 34 | Seattle-Tacoma International Airport |  | US | 1347 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1345 |
| 36 | Don Mueang International Airport |  | TH | 1299 |
| 37 | Calgary International Airport |  | CA | 1299 |
| 38 | Oslo Gardermoen Airport |  | NO | 1264 |
| 39 | Vitoria/Foronda Airport |  | ES | 1247 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1232 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1075 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 832 | 21m | 244 km | 3,503.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 573 | 1h 6m | 770 km | 7,611.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 567 | 24m | 225 km | 2,199.7 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 547 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 514 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 348 | 1h 50m | 1,423 km | 8,540.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 315 | 1h 7m | 706 km | 3,835.1 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 313 | 21m | 250 km | 1,352.0 t |
| 13 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 305 | 22m | 55 km | 289.9 t |
| 15 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 304 | 44m | 555 km | 2,910.9 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 293 | 1h 38m | 1,156 km | 5,845.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 291 | 24m | 218 km | 1,096.3 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 284 | 19m | 99 km | 486.5 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 277 | 27m | 215 km | 1,025.9 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 267 | 1h 14m | 961 km | 4,425.7 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 266 | 12m | - | - |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 260 | 19m | 144 km | 646.7 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 245 | 1h 50m | 1,304 km | 5,511.9 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 240 | 15m | 154 km | 635.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 239 | 28m | 152 km | 624.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FHBBZ | FHB | Saint-Cyr-l'Ecole Airport (LFPZ) | Etampes Mondesir Airport (LFOX) | 2026-08-23 10:17 UTC | 2026-08-23 11:09 UTC | 51m |
| GCJKO | GCJ | Colerne Airport (EGUO) | Colerne Airport (EGUO) | 2026-08-23 10:37 UTC | 2026-08-23 11:00 UTC | 22m |
| EJU3629 | EJU | Malpensa International Airport (LIMC) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-23 09:45 UTC | 2026-08-23 10:42 UTC | 57m |
| HBKNE | HBK | Locarno Airport (LSZL) | Ambri Airport (LSPM) | 2026-08-23 10:23 UTC | 2026-08-23 10:40 UTC | 17m |
| VOZ878 | Virgin Australia | Sydney Kingsford Smith International Airport (YSSY) | Melbourne International Airport (YMML) | 2026-08-23 09:02 UTC | 2026-08-23 10:39 UTC | 1h 37m |
| CRK260 | CRK | Chek Lap Kok International Airport (VHHH) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-23 09:04 UTC | 2026-08-23 10:38 UTC | 1h 33m |
| AM345 |  | Melbourne Essendon Airport (YMEN) | Sale Airport (YSLT) | 2026-08-23 10:11 UTC | 2026-08-23 10:37 UTC | 25m |
| N799LG |  | John C Tune Airport (KJWN) | Bangor International Airport (KBGR) | 2026-08-23 08:26 UTC | 2026-08-23 10:33 UTC | 2h 6m |
| CHX32 | CHX | ETT1 (ETT1) | ETT1 (ETT1) | 2026-08-23 10:26 UTC | 2026-08-23 10:29 UTC | 3m |
| PH876 |  | Teuge Airport (EHTE) | Teuge Airport (EHTE) | 2026-08-23 08:51 UTC | 2026-08-23 10:24 UTC | 1h 33m |
| TLJ813R | TLJ | Paris-Le Bourget Airport (LFPB) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-23 08:55 UTC | 2026-08-23 10:23 UTC | 1h 27m |
| EWG15HR | EWG | Alexander the Great International Airport (LGKV) | Stuttgart Airport (EDDS) | 2026-08-23 07:55 UTC | 2026-08-23 10:21 UTC | 2h 26m |
| UBG537 | UBG | VGZR (VGZR) | Shillong Airport (VEBI) | 2026-08-23 09:55 UTC | 2026-08-23 10:21 UTC | 25m |
| EWG54J | EWG | Palma De Mallorca Airport (LEPA) | Dusseldorf International Airport (EDDL) | 2026-08-23 08:29 UTC | 2026-08-23 10:20 UTC | 1h 50m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-23 10:02 UTC | 2026-08-23 10:18 UTC | 16m |
| SAMU05 | SAM | Gap - Tallard Airport (LFNA) | Barcelonnette - Saint-Pons Airport (LFMR) | 2026-08-23 09:54 UTC | 2026-08-23 10:14 UTC | 20m |
| EAI31F | EAI | Edinburgh Airport (EGPH) | Dublin Airport (EIDW) | 2026-08-23 09:10 UTC | 2026-08-23 10:12 UTC | 1h 1m |
| FIN2MF | Finnair | Helsinki Vantaa Airport (EFHK) | EFML (EFML) | 2026-08-23 09:23 UTC | 2026-08-23 10:10 UTC | 47m |
| UBG149 | UBG | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-08-23 09:31 UTC | 2026-08-23 10:09 UTC | 37m |
| TVL5302 | TVL | Budapest Ferenc Liszt International Airport (LHBP) | Antalya International Airport (LTAI) | 2026-08-23 08:06 UTC | 2026-08-23 10:09 UTC | 2h 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
