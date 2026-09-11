# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--11_10:15:03_UTC-green)

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

**Latest saved flight:** 2026-09-11 10:15:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-11 10:15:03 UTC

- **254,710** saved flights
- **76,084** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **254,710** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,074,160.9 tonnes** estimated CO2 emissions
- **178,212,228 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10159 |
| 2 | SkyWest Airlines | 8882 |
| 3 | EJA | 4919 |
| 4 | IndiGo | 4266 |
| 5 | American Airlines | 4040 |
| 6 | Southwest Airlines | 3755 |
| 7 | Delta Air Lines | 3198 |
| 8 | ENY | 3032 |
| 9 | LATAM Airlines | 2454 |
| 10 | AZU | 2370 |
| 11 | Vueling | 2163 |
| 12 | WIF | 2042 |
| 13 | Lufthansa | 1996 |
| 14 | LXJ | 1991 |
| 15 | easyJet | 1738 |
| 16 | Swiss International | 1707 |
| 17 | QLK | 1646 |
| 18 | AXM | 1638 |
| 19 | EJU | 1628 |
| 20 | United Airlines | 1583 |
| 21 | Alaska Airlines | 1515 |
| 22 | All Nippon Airways | 1489 |
| 23 | WMT | 1440 |
| 24 | GLO | 1418 |
| 25 | PGT | 1399 |
| 26 | VIV | 1391 |
| 27 | Air France | 1388 |
| 28 | Wizz Air | 1386 |
| 29 | JetBlue | 1239 |
| 30 | AEE | 1237 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 211436 |
| 2 | 🇪🇸 ES | 16220 |
| 3 | 🇧🇷 BR | 14867 |
| 4 | 🇦🇺 AU | 14555 |
| 5 | 🇨🇦 CA | 14170 |
| 6 | 🇮🇹 IT | 13936 |
| 7 | 🇮🇳 IN | 13362 |
| 8 | 🇩🇪 DE | 12451 |
| 9 | 🇬🇧 GB | 11901 |
| 10 | 🇨🇴 CO | 11288 |
| 11 | 🇫🇷 FR | 10233 |
| 12 | 🇯🇵 JP | 9979 |
| 13 | 🇹🇷 TR | 7624 |
| 14 | 🇬🇷 GR | 7445 |
| 15 | 🇲🇽 MX | 7018 |
| 16 | 🇨🇭 CH | 6837 |
| 17 | 🇳🇴 NO | 6314 |
| 18 | 🇹🇭 TH | 4583 |
| 19 | 🇲🇾 MY | 4405 |
| 20 | 🇿🇦 ZA | 4345 |
| 21 | 🇵🇱 PL | 4224 |
| 22 | 🇳🇿 NZ | 3511 |
| 23 | 🇵🇭 PH | 3439 |
| 24 | 🇬🇹 GT | 3164 |
| 25 | 🇰🇷 KR | 2929 |
| 26 | 🇭🇷 HR | 2919 |
| 27 | 🇲🇦 MA | 2567 |
| 28 | 🇲🇪 ME | 2394 |
| 29 | 🇳🇱 NL | 2292 |
| 30 | 🇮🇩 ID | 2173 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5231 |
| 2 | Denver International Airport |  | US | 4115 |
| 3 | Indira Gandhi International Airport |  | IN | 3085 |
| 4 | Tokyo International Airport |  | JP | 2978 |
| 5 | Guaymaral Airport |  | CO | 2755 |
| 6 | Harry Reid International Airport |  | US | 2699 |
| 7 | Zurich Airport |  | CH | 2664 |
| 8 | El Dorado International Airport |  | CO | 2611 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2574 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2499 |
| 11 | La Aurora Airport |  | GT | 2413 |
| 12 | Salt Lake City International Airport |  | US | 2247 |
| 13 | Chicago O'Hare International Airport |  | US | 2219 |
| 14 | Congonhas Airport |  | BR | 2183 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2083 |
| 16 | Capua Airport |  | IT | 2007 |
| 17 | Madrid Barajas International Airport |  | ES | 1990 |
| 18 | Frankfurt am Main International Airport |  | DE | 1967 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1909 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1845 |
| 21 | Malpensa International Airport |  | IT | 1829 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1791 |
| 23 | Charles de Gaulle International Airport |  | FR | 1790 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1770 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1704 |
| 26 | Macau International Airport |  | MO | 1685 |
| 27 | Ninoy Aquino International Airport |  | PH | 1681 |
| 28 | Barcelona International Airport |  | ES | 1603 |
| 29 | Charlotte/Douglas International Airport |  | US | 1600 |
| 30 | Kuala Lumpur International Airport |  | MY | 1586 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1562 |
| 32 | Viracopos International Airport |  | BR | 1522 |
| 33 | Seattle-Tacoma International Airport |  | US | 1496 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1481 |
| 35 | Don Mueang International Airport |  | TH | 1467 |
| 36 | Calgary International Airport |  | CA | 1467 |
| 37 | Bengaluru International Airport |  | IN | 1448 |
| 38 | Oslo Gardermoen Airport |  | NO | 1439 |
| 39 | Vancouver International Airport |  | CA | 1428 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1375 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1108 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 946 | 21m | 244 km | 3,983.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 679 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 639 | 1h 6m | 770 km | 8,488.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 638 | 24m | 225 km | 2,475.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 569 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 416 | 27m | 275 km | 1,971.2 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 406 | 44m | 555 km | 3,887.6 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 405 | 1h 50m | 1,423 km | 9,939.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 383 | 44m | 241 km | 1,590.9 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 355 | 24m | 218 km | 1,337.4 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 354 | 21m | 250 km | 1,529.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 339 | 23m | 55 km | 322.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 313 | 26m | 215 km | 1,159.2 t |
| 18 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 309 | 19m | 99 km | 529.3 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 307 | 12m | - | - |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 300 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 292 | 1h 14m | 961 km | 4,840.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 290 | 19m | 144 km | 721.4 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 274 | 1h 50m | 1,304 km | 6,164.3 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 266 | 41m | 535 km | 2,456.7 t |
| 29 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 258 | 28m | 152 km | 674.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA451 | Cathay Pacific | Narita International Airport (RJAA) | Hsinchu Air Base (RCPO) | 2026-09-11 07:12 UTC | 2026-09-11 10:15 UTC | 3h 2m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-09-11 09:25 UTC | 2026-09-11 10:10 UTC | 45m |
| DLH1KK | Lufthansa | Munich International Airport (EDDM) | Capua Airport (LIAU) | 2026-09-11 09:03 UTC | 2026-09-11 10:07 UTC | 1h 4m |
| PTN37G | PTN | Gloucestershire Airport (EGBJ) | Rotterdam Airport (EHRD) | 2026-09-11 08:59 UTC | 2026-09-11 09:50 UTC | 50m |
| PHHVB | PHH | Bonn-Hangelar Airport (EDKB) | Bonn-Hangelar Airport (EDKB) | 2026-09-11 09:36 UTC | 2026-09-11 09:50 UTC | 14m |
| CSR506U | CSR | Montpellier-Mediterranee Airport (LFMT) | Nimes-Arles-Camargue Airport (LFTW) | 2026-09-11 09:30 UTC | 2026-09-11 09:48 UTC | 17m |
| SYS111 | SYS | RAF Shawbury (EGOS) | RAF Shawbury (EGOS) | 2026-09-11 07:50 UTC | 2026-09-11 09:47 UTC | 1h 56m |
| JME633C | JME | Liverpool John Lennon Airport (EGGP) | Ibiza Airport (LEIB) | 2026-09-11 06:31 UTC | 2026-09-11 09:43 UTC | 3h 11m |
| SWR3TE | Swiss International | Berlin Brandenburg Airport (EDDB) | Zurich Airport (LSZH) | 2026-09-11 08:32 UTC | 2026-09-11 09:42 UTC | 1h 9m |
| SHA123 | SHA | Tribhuvan International Airport (VNKT) | Tulsipur Airport (VNDG) | 2026-09-11 09:04 UTC | 2026-09-11 09:37 UTC | 32m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Sandane Airport Anda (ENSD) | 2026-09-11 09:16 UTC | 2026-09-11 09:36 UTC | 19m |
| N856LF |  | Boise Air Trml/Gowen Field (KBOI) | Rugg Ranches Airport (45OG) | 2026-09-11 08:51 UTC | 2026-09-11 09:36 UTC | 44m |
| 8QTBB |  | Dharavandhoo Airport (VRMD) | Dharavandhoo Airport (VRMD) | 2026-09-11 09:28 UTC | 2026-09-11 09:32 UTC | 3m |
| HFA742 | HFA | Mikonos Airport (LGMK) | Haifa International Airport (LLHA) | 2026-09-11 07:22 UTC | 2026-09-11 09:31 UTC | 2h 8m |
| APG713 | APG | Ninoy Aquino International Airport (RPLL) | Romblon Airport (RPVU) | 2026-09-11 09:00 UTC | 2026-09-11 09:26 UTC | 26m |
|  |  | Osan Air Base (RKSO) | Osan Air Base (RKSO) | 2026-09-11 09:14 UTC | 2026-09-11 09:24 UTC | 9m |
| ANA297 | All Nippon Airways | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 2026-09-11 08:41 UTC | 2026-09-11 09:22 UTC | 40m |
| IGO082 | IndiGo | Ras Tanura Airport (OERT) | Pune Airport (VAPO) | 2026-09-11 06:07 UTC | 2026-09-11 09:21 UTC | 3h 14m |
| IGO7454 | IndiGo | Dabolim Airport (VOGO) | Coimbatore International Airport (VOCB) | 2026-09-11 07:52 UTC | 2026-09-11 09:19 UTC | 1h 26m |
| SWR2GE | Swiss International | Charles de Gaulle International Airport (LFPG) | Zurich Airport (LSZH) | 2026-09-11 08:26 UTC | 2026-09-11 09:19 UTC | 52m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
