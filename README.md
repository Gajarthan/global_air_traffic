# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--06_08:57:57_UTC-green)

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

**Latest saved flight:** 2026-08-06 08:57:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-06 08:57:57 UTC

- **173,799** saved flights
- **56,316** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **173,799** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,093,098.6 tonnes** estimated CO2 emissions
- **121,339,047 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6892 |
| 2 | SkyWest Airlines | 6370 |
| 3 | EJA | 3451 |
| 4 | IndiGo | 3040 |
| 5 | Southwest Airlines | 2742 |
| 6 | American Airlines | 2732 |
| 7 | ENY | 2166 |
| 8 | Delta Air Lines | 2062 |
| 9 | LATAM Airlines | 1605 |
| 10 | Lufthansa | 1575 |
| 11 | AZU | 1535 |
| 12 | WIF | 1453 |
| 13 | Vueling | 1429 |
| 14 | LXJ | 1362 |
| 15 | AXM | 1190 |
| 16 | Swiss International | 1180 |
| 17 | easyJet | 1178 |
| 18 | QLK | 1063 |
| 19 | EJU | 1062 |
| 20 | Alaska Airlines | 1058 |
| 21 | All Nippon Airways | 1053 |
| 22 | VIV | 956 |
| 23 | Cathay Pacific | 939 |
| 24 | CXK | 924 |
| 25 | GLO | 915 |
| 26 | AEE | 905 |
| 27 | United Airlines | 904 |
| 28 | Air France | 889 |
| 29 | MXY | 880 |
| 30 | JetBlue | 868 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 149801 |
| 2 | 🇪🇸 ES | 11109 |
| 3 | 🇧🇷 BR | 9889 |
| 4 | 🇦🇺 AU | 9757 |
| 5 | 🇮🇳 IN | 9535 |
| 6 | 🇨🇦 CA | 9512 |
| 7 | 🇮🇹 IT | 8965 |
| 8 | 🇩🇪 DE | 8596 |
| 9 | 🇬🇧 GB | 8035 |
| 10 | 🇯🇵 JP | 6977 |
| 11 | 🇫🇷 FR | 6885 |
| 12 | 🇨🇴 CO | 6403 |
| 13 | 🇬🇷 GR | 5039 |
| 14 | 🇲🇽 MX | 4976 |
| 15 | 🇨🇭 CH | 4576 |
| 16 | 🇳🇴 NO | 4518 |
| 17 | 🇹🇷 TR | 4261 |
| 18 | 🇲🇾 MY | 3090 |
| 19 | 🇵🇱 PL | 2900 |
| 20 | 🇿🇦 ZA | 2786 |
| 21 | 🇹🇭 TH | 2553 |
| 22 | 🇳🇿 NZ | 2523 |
| 23 | 🇵🇭 PH | 2294 |
| 24 | 🇬🇹 GT | 2213 |
| 25 | 🇰🇷 KR | 2178 |
| 26 | 🇲🇦 MA | 1744 |
| 27 | 🇭🇷 HR | 1678 |
| 28 | 🇲🇪 ME | 1589 |
| 29 | 🇳🇱 NL | 1565 |
| 30 | 🇲🇴 MO | 1501 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3595 |
| 2 | Denver International Airport |  | US | 2882 |
| 3 | Tokyo International Airport |  | JP | 2180 |
| 4 | Guaymaral Airport |  | CO | 2163 |
| 5 | Indira Gandhi International Airport |  | IN | 2123 |
| 6 | Harry Reid International Airport |  | US | 2081 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1885 |
| 8 | Zurich Airport |  | CH | 1836 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1824 |
| 10 | La Aurora Airport |  | GT | 1707 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1602 |
| 12 | El Dorado International Airport |  | CO | 1581 |
| 13 | Chicago O'Hare International Airport |  | US | 1572 |
| 14 | Salt Lake City International Airport |  | US | 1562 |
| 15 | Frankfurt am Main International Airport |  | DE | 1537 |
| 16 | Macau International Airport |  | MO | 1501 |
| 17 | Congonhas Airport |  | BR | 1431 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1420 |
| 19 | Capua Airport |  | IT | 1354 |
| 20 | Madrid Barajas International Airport |  | ES | 1353 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1305 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1221 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1214 |
| 24 | Charlotte/Douglas International Airport |  | US | 1200 |
| 25 | Malpensa International Airport |  | IT | 1178 |
| 26 | Charles de Gaulle International Airport |  | FR | 1176 |
| 27 | Kuala Lumpur International Airport |  | MY | 1165 |
| 28 | Bengaluru International Airport |  | IN | 1131 |
| 29 | Norman Y Mineta San Jose International Airport |  | US | 1080 |
| 30 | Ninoy Aquino International Airport |  | PH | 1079 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1072 |
| 32 | Barcelona International Airport |  | ES | 1025 |
| 33 | Daniel K Inouye International Airport |  | US | 1003 |
| 34 | Seattle-Tacoma International Airport |  | US | 1003 |
| 35 | Calgary International Airport |  | CA | 989 |
| 36 | Reno/Tahoe International Airport |  | US | 987 |
| 37 | Viracopos International Airport |  | BR | 986 |
| 38 | Oslo Gardermoen Airport |  | NO | 965 |
| 39 | Tenerife Norte Airport |  | ES | 961 |
| 40 | Scottsdale Airport |  | US | 946 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 635 | 21m | 244 km | 2,673.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 410 | 24m | 225 km | 1,590.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 407 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 393 | 1h 8m | 770 km | 5,220.7 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 321 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 294 | 27m | 275 km | 1,393.1 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 262 | 22m | 55 km | 249.0 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 260 | 44m | 241 km | 1,080.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 238 | 1h 48m | 1,423 km | 5,840.9 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 224 | 20m | 250 km | 967.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 223 | 26m | 215 km | 825.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 222 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 212 | 20m | 99 km | 363.1 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 209 | 50m | 556 km | 2,003.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 207 | 1h 15m | 961 km | 3,431.1 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 206 | 19m | 144 km | 512.4 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 202 | 31m | 369 km | 1,285.8 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 202 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 201 | 1h 38m | 1,156 km | 4,009.9 t |
| 27 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 200 | 8m | - | - |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 193 | 24m | 218 km | 727.1 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 189 | 43m | 452 km | 1,473.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EOX | EOX | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-08-06 08:17 UTC | 2026-08-06 08:57 UTC | 40m |
| ZFP | ZFP | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-08-06 08:06 UTC | 2026-08-06 08:54 UTC | 48m |
| HBZWE | HBZ | St Stephan Airport (LSTS) | Raron Airport (LSTA) | 2026-08-06 08:30 UTC | 2026-08-06 08:54 UTC | 24m |
| 3AMTT |  | Nice-Cote d'Azur Airport (LFMN) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-06 07:38 UTC | 2026-08-06 08:53 UTC | 1h 15m |
| IVW | IVW | Redcliffe Airport (YRED) | Redcliffe Airport (YRED) | 2026-08-06 08:07 UTC | 2026-08-06 08:48 UTC | 40m |
| CAL1806 | CAL | Taiwan Taoyuan International Airport (RCTP) | Kaohsiung International Airport (RCKH) | 2026-08-06 06:37 UTC | 2026-08-06 08:41 UTC | 2h 3m |
| STING82 | STI | RAF Akrotiri (LCRA) | RAF Akrotiri (LCRA) | 2026-08-06 07:26 UTC | 2026-08-06 08:40 UTC | 1h 14m |
| TVF64SY | TVF | Paris-Orly Airport (LFPO) | Kalamata Airport (LGKL) | 2026-08-06 06:04 UTC | 2026-08-06 08:39 UTC | 2h 35m |
| DHK368 | DHK | East Midlands Airport (EGNX) | John F Kennedy International Airport (KJFK) | 2026-08-06 01:33 UTC | 2026-08-06 08:25 UTC | 6h 51m |
| FHAFG | FHA | Annemasse Airport (LFLI) | Annemasse Airport (LFLI) | 2026-08-06 08:16 UTC | 2026-08-06 08:22 UTC | 5m |
| HBZWE | HBZ | Bern Belp Airport (LSZB) | Raron Airport (LSTA) | 2026-08-06 07:18 UTC | 2026-08-06 08:19 UTC | 1h 1m |
| RYR5CN | Ryanair | Bari / Palese International Airport (LIBD) | Malpensa International Airport (LIMC) | 2026-08-06 06:57 UTC | 2026-08-06 08:13 UTC | 1h 16m |
| MYM | MYM | Wondai Airport (YWND) | Toowoomba Airport (YTWB) | 2026-08-06 07:45 UTC | 2026-08-06 08:13 UTC | 27m |
| DIFLE | DIF | Wangerooge Airport (EDWG) | Wangerooge Airport (EDWG) | 2026-08-06 07:57 UTC | 2026-08-06 08:11 UTC | 14m |
| FHZSL | FHZ | Nice-Cote d'Azur Airport (LFMN) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-06 08:02 UTC | 2026-08-06 08:08 UTC | 6m |
| DUFFY01 | DUF | Gioia Del Colle Airport (LIBV) | Gioia Del Colle Airport (LIBV) | 2026-08-06 08:03 UTC | 2026-08-06 08:07 UTC | 4m |
| EJU49QM | EJU | Malpensa International Airport (LIMC) | Santorini Airport (LGSR) | 2026-08-06 05:53 UTC | 2026-08-06 08:05 UTC | 2h 12m |
| QLK11D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-08-06 07:42 UTC | 2026-08-06 08:05 UTC | 23m |
| RSC59LK | RSC | Gran Canaria Airport (GCLP) | Tenerife Norte Airport (GCXO) | 2026-08-06 07:42 UTC | 2026-08-06 08:04 UTC | 21m |
| VOE3359 | VOE | Malaga Airport (LEMG) | Vitoria/Foronda Airport (LEVT) | 2026-08-06 06:59 UTC | 2026-08-06 08:03 UTC | 1h 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
