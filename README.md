# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_11:51:08_UTC-green)

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

**Latest saved flight:** 2026-08-23 11:51:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 11:51:08 UTC

- **228,306** saved flights
- **70,669** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **228,306** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,753,807.8 tonnes** estimated CO2 emissions
- **159,641,030 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9164 |
| 2 | SkyWest Airlines | 8104 |
| 3 | EJA | 4393 |
| 4 | IndiGo | 3867 |
| 5 | American Airlines | 3740 |
| 6 | Southwest Airlines | 3549 |
| 7 | Delta Air Lines | 2919 |
| 8 | ENY | 2791 |
| 9 | LATAM Airlines | 2185 |
| 10 | AZU | 2113 |
| 11 | Vueling | 1938 |
| 12 | Lufthansa | 1868 |
| 13 | WIF | 1800 |
| 14 | LXJ | 1790 |
| 15 | easyJet | 1593 |
| 16 | Swiss International | 1522 |
| 17 | AXM | 1518 |
| 18 | QLK | 1448 |
| 19 | EJU | 1445 |
| 20 | United Airlines | 1445 |
| 21 | Alaska Airlines | 1385 |
| 22 | All Nippon Airways | 1371 |
| 23 | GLO | 1265 |
| 24 | VIV | 1253 |
| 25 | PGT | 1252 |
| 26 | WMT | 1247 |
| 27 | Air France | 1241 |
| 28 | Wizz Air | 1187 |
| 29 | JetBlue | 1142 |
| 30 | AEE | 1138 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 190665 |
| 2 | 🇪🇸 ES | 14650 |
| 3 | 🇧🇷 BR | 13298 |
| 4 | 🇦🇺 AU | 12957 |
| 5 | 🇨🇦 CA | 12622 |
| 6 | 🇮🇹 IT | 12309 |
| 7 | 🇮🇳 IN | 12054 |
| 8 | 🇩🇪 DE | 11232 |
| 9 | 🇬🇧 GB | 10744 |
| 10 | 🇨🇴 CO | 9384 |
| 11 | 🇯🇵 JP | 9308 |
| 12 | 🇫🇷 FR | 9136 |
| 13 | 🇹🇷 TR | 6720 |
| 14 | 🇬🇷 GR | 6703 |
| 15 | 🇲🇽 MX | 6358 |
| 16 | 🇨🇭 CH | 6045 |
| 17 | 🇳🇴 NO | 5610 |
| 18 | 🇲🇾 MY | 4051 |
| 19 | 🇿🇦 ZA | 3969 |
| 20 | 🇹🇭 TH | 3969 |
| 21 | 🇵🇱 PL | 3797 |
| 22 | 🇳🇿 NZ | 3169 |
| 23 | 🇵🇭 PH | 3136 |
| 24 | 🇬🇹 GT | 2873 |
| 25 | 🇰🇷 KR | 2705 |
| 26 | 🇭🇷 HR | 2600 |
| 27 | 🇲🇦 MA | 2308 |
| 28 | 🇲🇪 ME | 2072 |
| 29 | 🇳🇱 NL | 2039 |
| 30 | 🇮🇩 ID | 1974 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4771 |
| 2 | Denver International Airport |  | US | 3714 |
| 3 | Indira Gandhi International Airport |  | IN | 2787 |
| 4 | Tokyo International Airport |  | JP | 2779 |
| 5 | Guaymaral Airport |  | CO | 2647 |
| 6 | Harry Reid International Airport |  | US | 2473 |
| 7 | Zurich Airport |  | CH | 2374 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2332 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2303 |
| 10 | La Aurora Airport |  | GT | 2189 |
| 11 | El Dorado International Airport |  | CO | 2084 |
| 12 | Chicago O'Hare International Airport |  | US | 2071 |
| 13 | Salt Lake City International Airport |  | US | 2009 |
| 14 | Congonhas Airport |  | BR | 1940 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1938 |
| 16 | Frankfurt am Main International Airport |  | DE | 1830 |
| 17 | Madrid Barajas International Airport |  | ES | 1784 |
| 18 | Capua Airport |  | IT | 1775 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1703 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1698 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1649 |
| 22 | Malpensa International Airport |  | IT | 1628 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1611 |
| 24 | Macau International Airport |  | MO | 1596 |
| 25 | Charles de Gaulle International Airport |  | FR | 1579 |
| 26 | Ninoy Aquino International Airport |  | PH | 1503 |
| 27 | Charlotte/Douglas International Airport |  | US | 1492 |
| 28 | Kuala Lumpur International Airport |  | MY | 1468 |
| 29 | Barcelona International Airport |  | ES | 1426 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1384 |
| 31 | Bengaluru International Airport |  | IN | 1355 |
| 32 | Enrique Olaya Herrera Airport |  | CO | 1350 |
| 33 | Viracopos International Airport |  | BR | 1349 |
| 34 | Seattle-Tacoma International Airport |  | US | 1347 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1345 |
| 36 | Don Mueang International Airport |  | TH | 1302 |
| 37 | Calgary International Airport |  | CA | 1299 |
| 38 | Oslo Gardermoen Airport |  | NO | 1264 |
| 39 | Vitoria/Foronda Airport |  | ES | 1247 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1233 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1075 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 832 | 21m | 244 km | 3,503.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 574 | 1h 6m | 770 km | 7,625.1 t |
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
| 14 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 306 | 44m | 555 km | 2,930.1 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 305 | 22m | 55 km | 289.9 t |
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
| PH1312 |  | EHDB (EHDB) | EHDB (EHDB) | 2026-08-23 10:52 UTC | 2026-08-23 11:51 UTC | 58m |
| N947KC |  | Poplar Grove Airport (KC77) | De Kalb Taylor Municipal Airport (KDKB) | 2026-08-23 11:25 UTC | 2026-08-23 11:48 UTC | 22m |
| N90AR |  | Miami Executive Airport (KTMB) | Mjd Airport (FL31) | 2026-08-23 11:39 UTC | 2026-08-23 11:45 UTC | 5m |
| EIN5WG | Aer Lingus | Barcelona International Airport (LEBL) | Dublin Airport (EIDW) | 2026-08-23 09:34 UTC | 2026-08-23 11:44 UTC | 2h 10m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-08-23 11:16 UTC | 2026-08-23 11:34 UTC | 18m |
| N534NT |  | East Texas Regional Airport (KGGG) | Z M Jack Stell Field (KCRT) | 2026-08-23 11:12 UTC | 2026-08-23 11:33 UTC | 20m |
| OKPON | OKP | LZRY (LZRY) | LZRY (LZRY) | 2026-08-23 11:05 UTC | 2026-08-23 11:25 UTC | 20m |
| DMPAF | DMP | Bonn-Hangelar Airport (EDKB) | Bad Neuenahr-Ahrweiler Airport (EDRA) | 2026-08-23 11:13 UTC | 2026-08-23 11:24 UTC | 11m |
| EZY79EZ | easyJet | Malpensa International Airport (LIMC) | Wycombe Air Park (EGTB) | 2026-08-23 09:28 UTC | 2026-08-23 11:24 UTC | 1h 55m |
| DICMD | DIC | Nice-Cote d'Azur Airport (LFMN) | Samedan Airport (LSZS) | 2026-08-23 10:30 UTC | 2026-08-23 11:19 UTC | 49m |
| CSZ9074 | CSZ | Taiwan Taoyuan International Airport (RCTP) | Zhuhai Airport (ZGSD) | 2026-08-23 09:47 UTC | 2026-08-23 11:11 UTC | 1h 24m |
| RYR2PQ | Ryanair | Brussels South Charleroi Airport (EBCI) | Kenitra Airport (GMMY) | 2026-08-23 08:23 UTC | 2026-08-23 11:10 UTC | 2h 47m |
| FHBBZ | FHB | Saint-Cyr-l'Ecole Airport (LFPZ) | Etampes Mondesir Airport (LFOX) | 2026-08-23 10:17 UTC | 2026-08-23 11:09 UTC | 51m |
| FLJ61H | FLJ | Inverness Airport (EGPE) | Southampton Airport (EGHI) | 2026-08-23 09:59 UTC | 2026-08-23 11:08 UTC | 1h 9m |
| AIC8GW | Air India | Juhu Aerodrome (VAJJ) | Patiala Airport (VIPL) | 2026-08-23 09:21 UTC | 2026-08-23 11:01 UTC | 1h 40m |
| IGO7142 | IndiGo | Bengaluru International Airport (VOBL) | Vellore Airport (VOVR) | 2026-08-23 10:37 UTC | 2026-08-23 11:00 UTC | 22m |
| GCJKO | GCJ | Colerne Airport (EGUO) | Colerne Airport (EGUO) | 2026-08-23 10:37 UTC | 2026-08-23 11:00 UTC | 22m |
| MXD816 | MXD | Sultan Abdul Aziz Shah International Airport (WMSA) | Hang Nadim Airport (WIDD) | 2026-08-23 10:15 UTC | 2026-08-23 10:59 UTC | 43m |
| WZZ7WD | Wizz Air | Warsaw Chopin Airport (EPWA) | Otocac Airport (LDRO) | 2026-08-23 09:38 UTC | 2026-08-23 10:59 UTC | 1h 20m |
| GENTW | GEN | Elstree Airfield (EGTR) | Elstree Airfield (EGTR) | 2026-08-23 10:10 UTC | 2026-08-23 10:58 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
