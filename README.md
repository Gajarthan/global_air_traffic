# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_20:21:52_UTC-green)

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

**Latest saved flight:** 2026-08-21 20:21:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 20:21:52 UTC

- **223,667** saved flights
- **69,838** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **223,667** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,694,085.5 tonnes** estimated CO2 emissions
- **156,178,871 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8967 |
| 2 | SkyWest Airlines | 7945 |
| 3 | EJA | 4332 |
| 4 | IndiGo | 3780 |
| 5 | American Airlines | 3694 |
| 6 | Southwest Airlines | 3505 |
| 7 | Delta Air Lines | 2870 |
| 8 | ENY | 2749 |
| 9 | LATAM Airlines | 2124 |
| 10 | AZU | 2058 |
| 11 | Vueling | 1885 |
| 12 | Lufthansa | 1842 |
| 13 | WIF | 1787 |
| 14 | LXJ | 1762 |
| 15 | easyJet | 1547 |
| 16 | Swiss International | 1488 |
| 17 | AXM | 1467 |
| 18 | QLK | 1405 |
| 19 | United Airlines | 1405 |
| 20 | EJU | 1401 |
| 21 | Alaska Airlines | 1357 |
| 22 | All Nippon Airways | 1333 |
| 23 | GLO | 1230 |
| 24 | PGT | 1226 |
| 25 | VIV | 1216 |
| 26 | Air France | 1213 |
| 27 | WMT | 1191 |
| 28 | Wizz Air | 1152 |
| 29 | JetBlue | 1122 |
| 30 | AEE | 1115 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 187826 |
| 2 | 🇪🇸 ES | 14342 |
| 3 | 🇧🇷 BR | 12958 |
| 4 | 🇦🇺 AU | 12655 |
| 5 | 🇨🇦 CA | 12365 |
| 6 | 🇮🇹 IT | 11940 |
| 7 | 🇮🇳 IN | 11791 |
| 8 | 🇩🇪 DE | 11024 |
| 9 | 🇬🇧 GB | 10499 |
| 10 | 🇨🇴 CO | 9223 |
| 11 | 🇯🇵 JP | 9054 |
| 12 | 🇫🇷 FR | 8925 |
| 13 | 🇬🇷 GR | 6522 |
| 14 | 🇹🇷 TR | 6513 |
| 15 | 🇲🇽 MX | 6204 |
| 16 | 🇨🇭 CH | 5885 |
| 17 | 🇳🇴 NO | 5560 |
| 18 | 🇲🇾 MY | 3887 |
| 19 | 🇿🇦 ZA | 3861 |
| 20 | 🇹🇭 TH | 3774 |
| 21 | 🇵🇱 PL | 3713 |
| 22 | 🇳🇿 NZ | 3090 |
| 23 | 🇵🇭 PH | 3020 |
| 24 | 🇬🇹 GT | 2834 |
| 25 | 🇰🇷 KR | 2657 |
| 26 | 🇭🇷 HR | 2497 |
| 27 | 🇲🇦 MA | 2253 |
| 28 | 🇳🇱 NL | 1989 |
| 29 | 🇲🇪 ME | 1987 |
| 30 | 🇮🇩 ID | 1909 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4686 |
| 2 | Denver International Airport |  | US | 3644 |
| 3 | Tokyo International Airport |  | JP | 2714 |
| 4 | Indira Gandhi International Airport |  | IN | 2712 |
| 5 | Guaymaral Airport |  | CO | 2625 |
| 6 | Harry Reid International Airport |  | US | 2454 |
| 7 | Zurich Airport |  | CH | 2317 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2292 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2266 |
| 10 | La Aurora Airport |  | GT | 2161 |
| 11 | El Dorado International Airport |  | CO | 2080 |
| 12 | Chicago O'Hare International Airport |  | US | 2043 |
| 13 | Salt Lake City International Airport |  | US | 1963 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1921 |
| 15 | Congonhas Airport |  | BR | 1898 |
| 16 | Frankfurt am Main International Airport |  | DE | 1809 |
| 17 | Madrid Barajas International Airport |  | ES | 1753 |
| 18 | Capua Airport |  | IT | 1712 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1670 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1649 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1629 |
| 22 | Macau International Airport |  | MO | 1589 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1571 |
| 24 | Malpensa International Airport |  | IT | 1566 |
| 25 | Charles de Gaulle International Airport |  | FR | 1546 |
| 26 | Charlotte/Douglas International Airport |  | US | 1478 |
| 27 | Ninoy Aquino International Airport |  | PH | 1438 |
| 28 | Kuala Lumpur International Airport |  | MY | 1420 |
| 29 | Barcelona International Airport |  | ES | 1379 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1356 |
| 31 | Bengaluru International Airport |  | IN | 1334 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1320 |
| 33 | Seattle-Tacoma International Airport |  | US | 1318 |
| 34 | Viracopos International Airport |  | BR | 1312 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1293 |
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
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 523 | 8m | - | - |
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
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 282 | 1h 39m | 1,156 km | 5,625.8 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 278 | 24m | 218 km | 1,047.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 276 | 19m | 99 km | 472.8 t |
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
| N24NY |  | Linden Airport (KLDJ) | Linden Airport (KLDJ) | 2026-08-21 18:38 UTC | 2026-08-21 20:21 UTC | 1h 43m |
| CPA811 | Cathay Pacific | General Edward Lawrence Logan International Airport (KBOS) | Zhuhai Airport (ZGSD) | 2026-08-21 05:54 UTC | 2026-08-21 20:15 UTC | 14h 20m |
| N8120M |  | Carroll County Regional/Jack B Poage Field (KDMW) | Lancaster Airport (KLNS) | 2026-08-21 19:45 UTC | 2026-08-21 20:14 UTC | 28m |
| N750U |  | Highland County Airport (KHOC) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-21 19:46 UTC | 2026-08-21 20:06 UTC | 20m |
| TORA21 | TOR | 75OK (75OK) | Farney Field (42KS) | 2026-08-21 19:44 UTC | 2026-08-21 20:06 UTC | 22m |
| N1990H |  | AL79 (AL79) | Geneva Municipal Airport (K33J) | 2026-08-21 19:04 UTC | 2026-08-21 20:05 UTC | 1h 0m |
| TAUNT21 | TAU | 75OK (75OK) | Sopwith Ldg Airport (OK56) | 2026-08-21 19:50 UTC | 2026-08-21 20:03 UTC | 13m |
|  |  | AL37 (AL37) | AL37 (AL37) | 2026-08-21 20:00 UTC | 2026-08-21 20:01 UTC | 1m |
| ANZ8 | ANZ | Auckland International Airport (NZAA) | San Francisco International Airport (KSFO) | 2026-08-21 08:14 UTC | 2026-08-21 20:01 UTC | 11h 46m |
| N9421F |  | Elephant Path Airport (PS03) | Pennridge Airport (KCKZ) | 2026-08-21 19:43 UTC | 2026-08-21 19:58 UTC | 15m |
| N6538F |  | Bartow Executive Airport (KBOW) | Lakeland Linder International Airport (KLAL) | 2026-08-21 19:49 UTC | 2026-08-21 19:58 UTC | 8m |
| N493LG |  | CO54 (CO54) | Usaf Academy Davis Airfield (KAFF) | 2026-08-21 19:42 UTC | 2026-08-21 19:57 UTC | 14m |
| UPS4 | UPS | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-08-21 09:10 UTC | 2026-08-21 19:56 UTC | 10h 45m |
| TKR15 | TKR | Boise Air Trml/Gowen Field (KBOI) | Harrington Airport (20ID) | 2026-08-21 19:47 UTC | 2026-08-21 19:54 UTC | 6m |
| C2014 |  | Kodiak Airport (PADQ) | Ralph Wien Memorial Airport (PAOT) | 2026-08-21 17:35 UTC | 2026-08-21 19:52 UTC | 2h 16m |
| XBPNU | XBP | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-08-21 19:33 UTC | 2026-08-21 19:52 UTC | 19m |
| N622TP |  | Tweed/New Haven Airport (KHVN) | Laguardia Airport (KLGA) | 2026-08-21 19:24 UTC | 2026-08-21 19:49 UTC | 25m |
| EJA894 | EJA | Boeing Field/King County International Airport (KBFI) | 74WT (74WT) | 2026-08-21 19:30 UTC | 2026-08-21 19:47 UTC | 17m |
| CXK651 | CXK | 95CA (95CA) | Meadows Field (KBFL) | 2026-08-21 18:45 UTC | 2026-08-21 19:44 UTC | 58m |
| N17WG |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-08-21 19:16 UTC | 2026-08-21 19:42 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
