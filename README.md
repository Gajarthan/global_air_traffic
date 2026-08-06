# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--06_05:41:45_UTC-green)

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

**Latest saved flight:** 2026-08-06 05:41:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-06 05:41:45 UTC

- **173,681** saved flights
- **56,298** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **173,681** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,091,620.5 tonnes** estimated CO2 emissions
- **121,253,364 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6889 |
| 2 | SkyWest Airlines | 6370 |
| 3 | EJA | 3451 |
| 4 | IndiGo | 3038 |
| 5 | Southwest Airlines | 2742 |
| 6 | American Airlines | 2732 |
| 7 | ENY | 2166 |
| 8 | Delta Air Lines | 2062 |
| 9 | LATAM Airlines | 1605 |
| 10 | Lufthansa | 1575 |
| 11 | AZU | 1535 |
| 12 | WIF | 1450 |
| 13 | Vueling | 1428 |
| 14 | LXJ | 1362 |
| 15 | AXM | 1186 |
| 16 | Swiss International | 1179 |
| 17 | easyJet | 1175 |
| 18 | QLK | 1061 |
| 19 | EJU | 1059 |
| 20 | Alaska Airlines | 1058 |
| 21 | All Nippon Airways | 1050 |
| 22 | VIV | 956 |
| 23 | Cathay Pacific | 939 |
| 24 | CXK | 924 |
| 25 | GLO | 915 |
| 26 | United Airlines | 904 |
| 27 | AEE | 903 |
| 28 | Air France | 888 |
| 29 | MXY | 880 |
| 30 | JetBlue | 868 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 149792 |
| 2 | 🇪🇸 ES | 11095 |
| 3 | 🇧🇷 BR | 9889 |
| 4 | 🇦🇺 AU | 9734 |
| 5 | 🇮🇳 IN | 9526 |
| 6 | 🇨🇦 CA | 9512 |
| 7 | 🇮🇹 IT | 8951 |
| 8 | 🇩🇪 DE | 8587 |
| 9 | 🇬🇧 GB | 8029 |
| 10 | 🇯🇵 JP | 6964 |
| 11 | 🇫🇷 FR | 6870 |
| 12 | 🇨🇴 CO | 6403 |
| 13 | 🇬🇷 GR | 5031 |
| 14 | 🇲🇽 MX | 4976 |
| 15 | 🇨🇭 CH | 4567 |
| 16 | 🇳🇴 NO | 4510 |
| 17 | 🇹🇷 TR | 4256 |
| 18 | 🇲🇾 MY | 3085 |
| 19 | 🇵🇱 PL | 2899 |
| 20 | 🇿🇦 ZA | 2782 |
| 21 | 🇹🇭 TH | 2548 |
| 22 | 🇳🇿 NZ | 2523 |
| 23 | 🇵🇭 PH | 2290 |
| 24 | 🇬🇹 GT | 2213 |
| 25 | 🇰🇷 KR | 2177 |
| 26 | 🇲🇦 MA | 1742 |
| 27 | 🇭🇷 HR | 1676 |
| 28 | 🇲🇪 ME | 1586 |
| 29 | 🇳🇱 NL | 1564 |
| 30 | 🇲🇴 MO | 1501 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3595 |
| 2 | Denver International Airport |  | US | 2882 |
| 3 | Tokyo International Airport |  | JP | 2178 |
| 4 | Guaymaral Airport |  | CO | 2163 |
| 5 | Indira Gandhi International Airport |  | IN | 2122 |
| 6 | Harry Reid International Airport |  | US | 2081 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1883 |
| 8 | Zurich Airport |  | CH | 1833 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1824 |
| 10 | La Aurora Airport |  | GT | 1707 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1602 |
| 12 | El Dorado International Airport |  | CO | 1581 |
| 13 | Chicago O'Hare International Airport |  | US | 1572 |
| 14 | Salt Lake City International Airport |  | US | 1562 |
| 15 | Frankfurt am Main International Airport |  | DE | 1536 |
| 16 | Macau International Airport |  | MO | 1501 |
| 17 | Congonhas Airport |  | BR | 1431 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1420 |
| 19 | Capua Airport |  | IT | 1352 |
| 20 | Madrid Barajas International Airport |  | ES | 1350 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1305 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1221 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1211 |
| 24 | Charlotte/Douglas International Airport |  | US | 1200 |
| 25 | Charles de Gaulle International Airport |  | FR | 1175 |
| 26 | Malpensa International Airport |  | IT | 1174 |
| 27 | Kuala Lumpur International Airport |  | MY | 1163 |
| 28 | Bengaluru International Airport |  | IN | 1130 |
| 29 | Norman Y Mineta San Jose International Airport |  | US | 1080 |
| 30 | Ninoy Aquino International Airport |  | PH | 1078 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1072 |
| 32 | Barcelona International Airport |  | ES | 1025 |
| 33 | Daniel K Inouye International Airport |  | US | 1003 |
| 34 | Seattle-Tacoma International Airport |  | US | 1003 |
| 35 | Calgary International Airport |  | CA | 989 |
| 36 | Reno/Tahoe International Airport |  | US | 987 |
| 37 | Viracopos International Airport |  | BR | 986 |
| 38 | Oslo Gardermoen Airport |  | NO | 963 |
| 39 | Tenerife Norte Airport |  | ES | 960 |
| 40 | Scottsdale Airport |  | US | 946 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 635 | 21m | 244 km | 2,673.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 409 | 24m | 225 km | 1,586.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 407 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 393 | 1h 8m | 770 km | 5,220.7 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 321 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 293 | 27m | 275 km | 1,388.4 t |
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
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 205 | 19m | 144 km | 509.9 t |
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
| N900SE |  | Ted Stevens Anchorage International Airport (PANC) | Wood Strip (1MT3) | 2026-08-06 02:25 UTC | 2026-08-06 05:41 UTC | 3h 16m |
| IOORS | IOO | Bolzano Airport (LIPB) | LIVD (LIVD) | 2026-08-06 05:06 UTC | 2026-08-06 05:40 UTC | 34m |
| YTW | YTW | Toowoomba Wellcamp Airport (YBWW) | Sunshine Coast Airport (YBMC) | 2026-08-06 04:44 UTC | 2026-08-06 05:37 UTC | 52m |
| 85H |  | Brisbane Archerfield Airport (YBAF) | Dalby Airport (YDAY) | 2026-08-06 05:01 UTC | 2026-08-06 05:30 UTC | 29m |
| VT512 |  | Faa'a International Airport (NTAA) | Niau Airport (NTKN) | 2026-08-06 04:31 UTC | 2026-08-06 05:21 UTC | 49m |
| RXA6133 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-08-06 04:34 UTC | 2026-08-06 05:17 UTC | 42m |
| SERCE44 | SER | Yalova Airport (LTBP) | Yalova Airport (LTBP) | 2026-08-06 05:03 UTC | 2026-08-06 05:13 UTC | 9m |
| SPNTG | SPN | Deblin Military Air Base (EPDE) | Deblin Military Air Base (EPDE) | 2026-08-06 04:08 UTC | 2026-08-06 05:13 UTC | 1h 4m |
| FD548 |  | Adelaide International Airport (YPAD) | Blinman Airport (YBLM) | 2026-08-06 04:39 UTC | 2026-08-06 05:13 UTC | 33m |
| SWR12K | Swiss International | Václav Havel Airport (LKPR) | Zurich Airport (LSZH) | 2026-08-06 04:16 UTC | 2026-08-06 05:11 UTC | 54m |
| RYR39PG | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Otocac Airport (LDRO) | 2026-08-06 04:33 UTC | 2026-08-06 05:09 UTC | 36m |
| SPRN02 | SPR | Halim Perdanakusuma International Airport (WIHH) | Halim Perdanakusuma International Airport (WIHH) | 2026-08-06 05:02 UTC | 2026-08-06 05:09 UTC | 6m |
| VOE79TQ | VOE | L'Aquila / Preturo Airport (LIAP) | Kastoria National Airport (LGKA) | 2026-08-06 04:19 UTC | 2026-08-06 05:08 UTC | 48m |
| IGO5268 | IndiGo | Juhu Aerodrome (VAJJ) | Chandigarh Airport (VICG) | 2026-08-06 03:17 UTC | 2026-08-06 05:04 UTC | 1h 46m |
| DLH1MA | Lufthansa | Budapest Ferenc Liszt International Airport (LHBP) | Munich International Airport (EDDM) | 2026-08-06 04:08 UTC | 2026-08-06 05:04 UTC | 55m |
| CFH21 | CFH | Coffs Harbour Airport (YSCH) | Wollomombi Airport (YWMM) | 2026-08-06 04:48 UTC | 2026-08-06 05:04 UTC | 15m |
| SERCE28 | SER | Yalova Airport (LTBP) | Yalova Airport (LTBP) | 2026-08-06 04:53 UTC | 2026-08-06 05:03 UTC | 10m |
| FPP | FPP | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-06 04:42 UTC | 2026-08-06 04:58 UTC | 16m |
| JST223 | JST | Sydney Kingsford Smith International Airport (YSSY) | Queenstown International Airport (NZQN) | 2026-08-06 02:36 UTC | 2026-08-06 04:55 UTC | 2h 19m |
| ASA1102 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-08-06 04:33 UTC | 2026-08-06 04:55 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
