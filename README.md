# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_07:10:54_UTC-green)

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

**Latest saved flight:** 2026-08-21 07:10:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 07:10:54 UTC

- **221,373** saved flights
- **69,373** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **221,373** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,664,184.0 tonnes** estimated CO2 emissions
- **154,445,450 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8862 |
| 2 | SkyWest Airlines | 7891 |
| 3 | EJA | 4289 |
| 4 | IndiGo | 3749 |
| 5 | American Airlines | 3670 |
| 6 | Southwest Airlines | 3491 |
| 7 | Delta Air Lines | 2850 |
| 8 | ENY | 2724 |
| 9 | LATAM Airlines | 2103 |
| 10 | AZU | 2032 |
| 11 | Vueling | 1859 |
| 12 | Lufthansa | 1831 |
| 13 | WIF | 1766 |
| 14 | LXJ | 1746 |
| 15 | easyJet | 1530 |
| 16 | Swiss International | 1469 |
| 17 | AXM | 1456 |
| 18 | QLK | 1394 |
| 19 | United Airlines | 1390 |
| 20 | EJU | 1376 |
| 21 | Alaska Airlines | 1351 |
| 22 | All Nippon Airways | 1327 |
| 23 | GLO | 1211 |
| 24 | PGT | 1206 |
| 25 | VIV | 1206 |
| 26 | Air France | 1197 |
| 27 | WMT | 1169 |
| 28 | Wizz Air | 1126 |
| 29 | JetBlue | 1119 |
| 30 | AEE | 1107 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 186281 |
| 2 | 🇪🇸 ES | 14161 |
| 3 | 🇧🇷 BR | 12790 |
| 4 | 🇦🇺 AU | 12592 |
| 5 | 🇨🇦 CA | 12240 |
| 6 | 🇮🇹 IT | 11758 |
| 7 | 🇮🇳 IN | 11688 |
| 8 | 🇩🇪 DE | 10909 |
| 9 | 🇬🇧 GB | 10367 |
| 10 | 🇨🇴 CO | 9102 |
| 11 | 🇯🇵 JP | 9003 |
| 12 | 🇫🇷 FR | 8793 |
| 13 | 🇬🇷 GR | 6454 |
| 14 | 🇹🇷 TR | 6376 |
| 15 | 🇲🇽 MX | 6157 |
| 16 | 🇨🇭 CH | 5836 |
| 17 | 🇳🇴 NO | 5487 |
| 18 | 🇲🇾 MY | 3855 |
| 19 | 🇿🇦 ZA | 3775 |
| 20 | 🇹🇭 TH | 3707 |
| 21 | 🇵🇱 PL | 3668 |
| 22 | 🇳🇿 NZ | 3088 |
| 23 | 🇵🇭 PH | 2999 |
| 24 | 🇬🇹 GT | 2793 |
| 25 | 🇰🇷 KR | 2641 |
| 26 | 🇭🇷 HR | 2450 |
| 27 | 🇲🇦 MA | 2220 |
| 28 | 🇳🇱 NL | 1964 |
| 29 | 🇲🇪 ME | 1955 |
| 30 | 🇮🇩 ID | 1888 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4649 |
| 2 | Denver International Airport |  | US | 3615 |
| 3 | Tokyo International Airport |  | JP | 2703 |
| 4 | Indira Gandhi International Airport |  | IN | 2686 |
| 5 | Guaymaral Airport |  | CO | 2606 |
| 6 | Harry Reid International Airport |  | US | 2443 |
| 7 | Zurich Airport |  | CH | 2291 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2276 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2246 |
| 10 | La Aurora Airport |  | GT | 2128 |
| 11 | El Dorado International Airport |  | CO | 2073 |
| 12 | Chicago O'Hare International Airport |  | US | 2024 |
| 13 | Salt Lake City International Airport |  | US | 1948 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1909 |
| 15 | Congonhas Airport |  | BR | 1869 |
| 16 | Frankfurt am Main International Airport |  | DE | 1798 |
| 17 | Madrid Barajas International Airport |  | ES | 1732 |
| 18 | Capua Airport |  | IT | 1688 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1661 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1630 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1625 |
| 22 | Macau International Airport |  | MO | 1586 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1566 |
| 24 | Malpensa International Airport |  | IT | 1550 |
| 25 | Charles de Gaulle International Airport |  | FR | 1520 |
| 26 | Charlotte/Douglas International Airport |  | US | 1471 |
| 27 | Ninoy Aquino International Airport |  | PH | 1428 |
| 28 | Kuala Lumpur International Airport |  | MY | 1412 |
| 29 | Barcelona International Airport |  | ES | 1358 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1346 |
| 31 | Bengaluru International Airport |  | IN | 1326 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1315 |
| 33 | Seattle-Tacoma International Airport |  | US | 1312 |
| 34 | Viracopos International Airport |  | BR | 1299 |
| 35 | Calgary International Airport |  | CA | 1256 |
| 36 | Enrique Olaya Herrera Airport |  | CO | 1235 |
| 37 | Vitoria/Foronda Airport |  | ES | 1226 |
| 38 | Oslo Gardermoen Airport |  | NO | 1224 |
| 39 | Don Mueang International Airport |  | TH | 1219 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1188 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1064 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 798 | 21m | 244 km | 3,360.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 549 | 1h 7m | 770 km | 7,293.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 534 | 24m | 225 km | 2,071.7 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 499 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 499 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 372 | 27m | 275 km | 1,762.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 351 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 328 | 1h 50m | 1,423 km | 8,049.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 324 | 44m | 241 km | 1,345.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 292 | 21m | 250 km | 1,261.3 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 276 | 24m | 218 km | 1,039.8 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 276 | 1h 38m | 1,156 km | 5,506.1 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 273 | 19m | 99 km | 467.6 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 272 | 27m | 215 km | 1,007.4 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 22 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 261 | 44m | 555 km | 2,499.2 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 261 | 1h 14m | 961 km | 4,326.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 252 | 12m | - | - |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 251 | 19m | 144 km | 624.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 239 | 1h 49m | 1,304 km | 5,376.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N359DG |  | Los Angeles International Airport (KLAX) | Madera Municipal Airport (KMAE) | 2026-08-21 06:24 UTC | 2026-08-21 07:10 UTC | 46m |
| MRL11 | MRL | San Javier Airport (LELC) | Alhama De Murcia Airport (LELH) | 2026-08-21 06:49 UTC | 2026-08-21 07:04 UTC | 15m |
| UPS18 | UPS | Cologne Bonn Airport (EDDK) | Zhuhai Airport (ZGSD) | 2026-08-20 20:45 UTC | 2026-08-21 07:03 UTC | 10h 18m |
| RYR41YE | Ryanair | Vienna International Airport (LOWW) | Palma De Mallorca Airport (LEPA) | 2026-08-21 04:40 UTC | 2026-08-21 06:49 UTC | 2h 8m |
| WIF8C | WIF | Bodø Airport (ENBO) | Svolvær Helle Airport (ENSH) | 2026-08-21 06:18 UTC | 2026-08-21 06:36 UTC | 17m |
| RYR280W | Ryanair | Gdańsk Lech Wałęsa Airport (EPGD) | Dublin Airport (EIDW) | 2026-08-21 04:11 UTC | 2026-08-21 06:33 UTC | 2h 21m |
| QLK1908 | QLK | Adelaide International Airport (YPAD) | Newcastle Airport (YWLM) | 2026-08-21 04:48 UTC | 2026-08-21 06:32 UTC | 1h 44m |
| ZSTKH | ZST | Mafeking Airport (FAMK) | Rooiberg Airport (FARO) | 2026-08-21 06:04 UTC | 2026-08-21 06:32 UTC | 28m |
| EJU31EQ | EJU | Palma De Mallorca Airport (LEPA) | Bordeaux-Merignac (BA 106) Airport (LFBD) | 2026-08-21 05:22 UTC | 2026-08-21 06:31 UTC | 1h 8m |
| WIF7HY | WIF | Bergen Airport Flesland (ENBR) | Bringeland Airport (ENBL) | 2026-08-21 06:07 UTC | 2026-08-21 06:28 UTC | 20m |
| BLINR87 | BLI | Travis Afb Airport (KSUU) | Travis Afb Airport (KSUU) | 2026-08-21 05:57 UTC | 2026-08-21 06:25 UTC | 28m |
| AZU4112 | AZU | Val de Cans/Julio Cezar Ribeiro International Airport (SBBE) | Maraba Airport (SBMA) | 2026-08-21 05:46 UTC | 2026-08-21 06:25 UTC | 38m |
| QLK24D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Woodville Airport (YWVL) | 2026-08-21 05:36 UTC | 2026-08-21 06:22 UTC | 46m |
| SWR47W | Swiss International | Amsterdam Airport Schiphol (EHAM) | Zurich Airport (LSZH) | 2026-08-21 05:16 UTC | 2026-08-21 06:20 UTC | 1h 3m |
| MMD2848 | MMD | Stockholm-Bromma Airport (ESSB) | Gothenburg-Landvetter Airport (ESGG) | 2026-08-21 05:39 UTC | 2026-08-21 06:16 UTC | 37m |
| WMT8LX | WMT | Sigonella Airport (LICZ) | Malpensa International Airport (LIMC) | 2026-08-21 04:27 UTC | 2026-08-21 06:11 UTC | 1h 43m |
| AEE348 | AEE | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-08-21 05:49 UTC | 2026-08-21 06:11 UTC | 21m |
| CJT626 | CJT | Montréal (Mirabel) Airport (CYMX) | Chipman Airport (CCS4) | 2026-08-21 05:24 UTC | 2026-08-21 06:09 UTC | 45m |
| FJJJY | FJJ | Saint-Nazaire-Montoir Airport (LFRZ) | Saint-Nazaire-Montoir Airport (LFRZ) | 2026-08-21 05:42 UTC | 2026-08-21 06:09 UTC | 26m |
| JAL375 | Japan Airlines | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-08-21 05:05 UTC | 2026-08-21 06:08 UTC | 1h 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
