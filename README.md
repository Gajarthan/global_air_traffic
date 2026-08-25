# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_06:48:57_UTC-green)

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

**Latest saved flight:** 2026-08-25 06:48:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 06:48:57 UTC

- **234,316** saved flights
- **71,841** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **234,316** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,822,528.7 tonnes** estimated CO2 emissions
- **163,624,850 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9388 |
| 2 | SkyWest Airlines | 8299 |
| 3 | EJA | 4553 |
| 4 | IndiGo | 3958 |
| 5 | American Airlines | 3815 |
| 6 | Southwest Airlines | 3599 |
| 7 | Delta Air Lines | 2991 |
| 8 | ENY | 2854 |
| 9 | LATAM Airlines | 2252 |
| 10 | AZU | 2183 |
| 11 | Vueling | 1999 |
| 12 | Lufthansa | 1902 |
| 13 | WIF | 1859 |
| 14 | LXJ | 1844 |
| 15 | easyJet | 1632 |
| 16 | Swiss International | 1565 |
| 17 | AXM | 1563 |
| 18 | EJU | 1495 |
| 19 | QLK | 1493 |
| 20 | United Airlines | 1484 |
| 21 | Alaska Airlines | 1417 |
| 22 | All Nippon Airways | 1395 |
| 23 | GLO | 1306 |
| 24 | WMT | 1299 |
| 25 | VIV | 1293 |
| 26 | PGT | 1278 |
| 27 | Air France | 1268 |
| 28 | Wizz Air | 1236 |
| 29 | AEE | 1164 |
| 30 | JetBlue | 1162 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 195085 |
| 2 | 🇪🇸 ES | 15014 |
| 3 | 🇧🇷 BR | 13683 |
| 4 | 🇦🇺 AU | 13292 |
| 5 | 🇨🇦 CA | 12973 |
| 6 | 🇮🇹 IT | 12716 |
| 7 | 🇮🇳 IN | 12322 |
| 8 | 🇩🇪 DE | 11521 |
| 9 | 🇬🇧 GB | 11014 |
| 10 | 🇨🇴 CO | 9853 |
| 11 | 🇯🇵 JP | 9503 |
| 12 | 🇫🇷 FR | 9350 |
| 13 | 🇹🇷 TR | 6940 |
| 14 | 🇬🇷 GR | 6885 |
| 15 | 🇲🇽 MX | 6526 |
| 16 | 🇨🇭 CH | 6230 |
| 17 | 🇳🇴 NO | 5774 |
| 18 | 🇲🇾 MY | 4177 |
| 19 | 🇹🇭 TH | 4158 |
| 20 | 🇿🇦 ZA | 4081 |
| 21 | 🇵🇱 PL | 3900 |
| 22 | 🇳🇿 NZ | 3247 |
| 23 | 🇵🇭 PH | 3219 |
| 24 | 🇬🇹 GT | 2935 |
| 25 | 🇰🇷 KR | 2746 |
| 26 | 🇭🇷 HR | 2687 |
| 27 | 🇲🇦 MA | 2373 |
| 28 | 🇲🇪 ME | 2159 |
| 29 | 🇳🇱 NL | 2093 |
| 30 | 🇮🇩 ID | 2037 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4874 |
| 2 | Denver International Airport |  | US | 3799 |
| 3 | Indira Gandhi International Airport |  | IN | 2854 |
| 4 | Tokyo International Airport |  | JP | 2828 |
| 5 | Guaymaral Airport |  | CO | 2677 |
| 6 | Harry Reid International Airport |  | US | 2517 |
| 7 | Zurich Airport |  | CH | 2443 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2396 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2347 |
| 10 | La Aurora Airport |  | GT | 2236 |
| 11 | El Dorado International Airport |  | CO | 2197 |
| 12 | Chicago O'Hare International Airport |  | US | 2117 |
| 13 | Salt Lake City International Airport |  | US | 2069 |
| 14 | Congonhas Airport |  | BR | 1997 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1973 |
| 16 | Frankfurt am Main International Airport |  | DE | 1864 |
| 17 | Capua Airport |  | IT | 1842 |
| 18 | Madrid Barajas International Airport |  | ES | 1837 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1764 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1732 |
| 21 | Malpensa International Airport |  | IT | 1676 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1664 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1648 |
| 24 | Charles de Gaulle International Airport |  | FR | 1624 |
| 25 | Macau International Airport |  | MO | 1607 |
| 26 | Ninoy Aquino International Airport |  | PH | 1554 |
| 27 | Charlotte/Douglas International Airport |  | US | 1515 |
| 28 | Kuala Lumpur International Airport |  | MY | 1512 |
| 29 | Barcelona International Airport |  | ES | 1476 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1443 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1420 |
| 32 | Viracopos International Airport |  | BR | 1396 |
| 33 | Seattle-Tacoma International Airport |  | US | 1378 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1377 |
| 35 | Bengaluru International Airport |  | IN | 1375 |
| 36 | Don Mueang International Airport |  | TH | 1352 |
| 37 | Calgary International Airport |  | CA | 1345 |
| 38 | Oslo Gardermoen Airport |  | NO | 1307 |
| 39 | Vancouver International Airport |  | CA | 1282 |
| 40 | Vitoria/Foronda Airport |  | ES | 1269 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1085 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 862 | 21m | 244 km | 3,629.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 591 | 24m | 225 km | 2,292.8 t |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 590 | 1h 6m | 770 km | 7,837.7 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 584 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 523 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 386 | 27m | 275 km | 1,829.1 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 362 | 1h 50m | 1,423 km | 8,884.1 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 360 | 35m | - | - |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 339 | 44m | 241 km | 1,408.1 t |
| 11 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 335 | 44m | 555 km | 3,207.8 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 327 | 21m | 250 km | 1,412.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 311 | 24m | 218 km | 1,171.7 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 307 | 1h 40m | 1,156 km | 6,124.5 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 290 | 19m | 99 km | 496.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 286 | 27m | 215 km | 1,059.2 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 273 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 272 | 1h 14m | 961 km | 4,508.5 t |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 267 | 29m | 304 km | 1,399.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 266 | 19m | 144 km | 661.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 257 | 15m | 154 km | 680.9 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 251 | 1h 50m | 1,304 km | 5,646.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JJA1393 | JJA | Incheon International Airport (RKSI) | Kansai International Airport (RJBB) | 2026-08-25 05:23 UTC | 2026-08-25 06:48 UTC | 1h 25m |
| NHD421 | NHD | Esbjerg Airport (EKEB) | Stauning Airport (EKVJ) | 2026-08-25 06:06 UTC | 2026-08-25 06:25 UTC | 19m |
| AE980 |  | Sydney Bankstown Airport (YSBK) | Federation Hsd Airport (YFDN) | 2026-08-25 05:26 UTC | 2026-08-25 06:14 UTC | 47m |
| LR455 |  | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-08-25 05:42 UTC | 2026-08-25 06:12 UTC | 30m |
| N302TP |  | Tulsa International Airport (KTUL) | Tulsa International Airport (KTUL) | 2026-08-25 05:43 UTC | 2026-08-25 06:09 UTC | 25m |
| WIF5DB | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-08-25 05:33 UTC | 2026-08-25 05:57 UTC | 24m |
| AYT101 | AYT | Hatzor Air Base (LLHS) | Ovda International Airport (LLOV) | 2026-08-25 05:36 UTC | 2026-08-25 05:57 UTC | 21m |
| RYR4UR | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Triodhon Airport (LG55) | 2026-08-25 04:14 UTC | 2026-08-25 05:53 UTC | 1h 38m |
| KAL199T | Korean Air | Gimpo International Airport (RKSS) | Daegu Airport (RKTN) | 2026-08-25 05:23 UTC | 2026-08-25 05:51 UTC | 27m |
| RPB7278 | RPB | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 2026-08-25 05:33 UTC | 2026-08-25 05:49 UTC | 15m |
| ASA1122 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-08-25 05:26 UTC | 2026-08-25 05:47 UTC | 21m |
| AUA89E | Austrian Airlines | Vienna International Airport (LOWW) | Karpathos Airport (LGKP) | 2026-08-25 03:41 UTC | 2026-08-25 05:45 UTC | 2h 4m |
| RYR9489 | Ryanair | Reggio Calabria Airport (LICR) | Malpensa International Airport (LIMC) | 2026-08-25 04:14 UTC | 2026-08-25 05:44 UTC | 1h 29m |
| RTP186 | RTP | Don Mueang International Airport (VTBD) | Takhli Airport (VTPI) | 2026-08-25 05:17 UTC | 2026-08-25 05:40 UTC | 23m |
| YTX | YTX | Toowoomba Wellcamp Airport (YBWW) | Brisbane Archerfield Airport (YBAF) | 2026-08-25 04:55 UTC | 2026-08-25 05:40 UTC | 44m |
| WZZ5372 | Wizz Air | Kopitnari Airport (UGKO) | Poznań-Ławica Airport (EPPO) | 2026-08-25 02:01 UTC | 2026-08-25 05:39 UTC | 3h 37m |
| DLH172 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Berlin Brandenburg Airport (EDDB) | 2026-08-25 04:52 UTC | 2026-08-25 05:38 UTC | 45m |
| ELW103 | ELW | Nairobi Wilson Airport (HKNW) | Jomo Kenyatta International Airport (HKJK) | 2026-08-25 05:21 UTC | 2026-08-25 05:36 UTC | 15m |
| RYR2TY | Ryanair | Pescara International Airport (LIBP) | Malpensa International Airport (LIMC) | 2026-08-25 04:34 UTC | 2026-08-25 05:36 UTC | 1h 1m |
| SJX847 | SJX | Taiwan Taoyuan International Airport (RCTP) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-24 23:32 UTC | 2026-08-25 05:34 UTC | 6h 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
