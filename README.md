# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30_22:17:26_UTC-green)

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

**Latest saved flight:** 2026-07-30 22:17:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-30 22:17:26 UTC

- **161,510** saved flights
- **53,323** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **161,510** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,936,720.5 tonnes** estimated CO2 emissions
- **112,273,652 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6463 |
| 2 | SkyWest Airlines | 5894 |
| 3 | EJA | 3204 |
| 4 | IndiGo | 2832 |
| 5 | American Airlines | 2555 |
| 6 | Southwest Airlines | 2533 |
| 7 | ENY | 2009 |
| 8 | Delta Air Lines | 1921 |
| 9 | Lufthansa | 1520 |
| 10 | LATAM Airlines | 1518 |
| 11 | AZU | 1419 |
| 12 | WIF | 1366 |
| 13 | Vueling | 1339 |
| 14 | LXJ | 1254 |
| 15 | AXM | 1120 |
| 16 | Swiss International | 1112 |
| 17 | easyJet | 1057 |
| 18 | Alaska Airlines | 1005 |
| 19 | EJU | 994 |
| 20 | QLK | 992 |
| 21 | All Nippon Airways | 990 |
| 22 | VIV | 889 |
| 23 | CXK | 863 |
| 24 | United Airlines | 854 |
| 25 | Cathay Pacific | 848 |
| 26 | GLO | 848 |
| 27 | AEE | 846 |
| 28 | Air France | 837 |
| 29 | MXY | 837 |
| 30 | JetBlue | 826 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 139590 |
| 2 | 🇪🇸 ES | 10346 |
| 3 | 🇧🇷 BR | 9230 |
| 4 | 🇦🇺 AU | 9090 |
| 5 | 🇮🇳 IN | 8911 |
| 6 | 🇨🇦 CA | 8771 |
| 7 | 🇮🇹 IT | 8323 |
| 8 | 🇩🇪 DE | 8140 |
| 9 | 🇬🇧 GB | 7411 |
| 10 | 🇯🇵 JP | 6531 |
| 11 | 🇫🇷 FR | 6391 |
| 12 | 🇨🇴 CO | 5745 |
| 13 | 🇲🇽 MX | 4638 |
| 14 | 🇬🇷 GR | 4634 |
| 15 | 🇳🇴 NO | 4267 |
| 16 | 🇨🇭 CH | 4231 |
| 17 | 🇹🇷 TR | 3851 |
| 18 | 🇲🇾 MY | 2909 |
| 19 | 🇵🇱 PL | 2741 |
| 20 | 🇿🇦 ZA | 2601 |
| 21 | 🇳🇿 NZ | 2370 |
| 22 | 🇹🇭 TH | 2292 |
| 23 | 🇵🇭 PH | 2119 |
| 24 | 🇰🇷 KR | 2108 |
| 25 | 🇬🇹 GT | 2075 |
| 26 | 🇲🇦 MA | 1629 |
| 27 | 🇲🇪 ME | 1527 |
| 28 | 🇭🇷 HR | 1508 |
| 29 | 🇳🇱 NL | 1479 |
| 30 | 🇲🇴 MO | 1339 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3298 |
| 2 | Denver International Airport |  | US | 2688 |
| 3 | Tokyo International Airport |  | JP | 2063 |
| 4 | Guaymaral Airport |  | CO | 2035 |
| 5 | Indira Gandhi International Airport |  | IN | 1982 |
| 6 | Harry Reid International Airport |  | US | 1962 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1785 |
| 8 | Zurich Airport |  | CH | 1721 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1698 |
| 10 | La Aurora Airport |  | GT | 1611 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1503 |
| 12 | El Dorado International Airport |  | CO | 1480 |
| 13 | Frankfurt am Main International Airport |  | DE | 1471 |
| 14 | Chicago O'Hare International Airport |  | US | 1468 |
| 15 | Salt Lake City International Airport |  | US | 1454 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1351 |
| 17 | Congonhas Airport |  | BR | 1340 |
| 18 | Macau International Airport |  | MO | 1339 |
| 19 | Madrid Barajas International Airport |  | ES | 1277 |
| 20 | Capua Airport |  | IT | 1271 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1236 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1147 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1146 |
| 24 | Charlotte/Douglas International Airport |  | US | 1136 |
| 25 | Kuala Lumpur International Airport |  | MY | 1111 |
| 26 | Charles de Gaulle International Airport |  | FR | 1103 |
| 27 | Malpensa International Airport |  | IT | 1068 |
| 28 | Bengaluru International Airport |  | IN | 1059 |
| 29 | Ninoy Aquino International Airport |  | PH | 994 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 988 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 981 |
| 32 | Barcelona International Airport |  | ES | 958 |
| 33 | Daniel K Inouye International Airport |  | US | 950 |
| 34 | Seattle-Tacoma International Airport |  | US | 936 |
| 35 | Calgary International Airport |  | CA | 924 |
| 36 | Viracopos International Airport |  | BR | 920 |
| 37 | Scottsdale Airport |  | US | 907 |
| 38 | Tenerife Norte Airport |  | ES | 906 |
| 39 | Oslo Gardermoen Airport |  | NO | 897 |
| 40 | Reno/Tahoe International Airport |  | US | 889 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 853 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 589 | 21m | 244 km | 2,480.1 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 387 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 383 | 24m | 225 km | 1,485.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 369 | 1h 9m | 770 km | 4,901.9 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 296 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 283 | 27m | 275 km | 1,341.0 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 238 | 22m | 55 km | 226.2 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 237 | 19m | 165 km | 674.2 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 231 | 44m | 241 km | 959.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 222 | 1h 47m | 1,423 km | 5,448.2 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 212 | 26m | 215 km | 785.2 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 206 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 204 | 20m | 99 km | 349.4 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 203 | 20m | 250 km | 876.8 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 194 | 30m | 49 km | 164.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 192 | 1h 15m | 961 km | 3,182.5 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 192 | 28m | 152 km | 501.8 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 191 | 18m | 144 km | 475.1 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 189 | 31m | 369 km | 1,203.0 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 187 | 50m | 556 km | 1,792.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 181 | 1h 39m | 1,156 km | 3,610.9 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 179 | 1h 1m | 695 km | 2,145.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 177 | 44m | 452 km | 1,379.5 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 172 | 23m | 218 km | 648.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RFS710 | RFS | Seattle Paine Field International Airport (KPAE) | Arlington Municipal Airport (KAWO) | 2026-07-30 21:40 UTC | 2026-07-30 22:17 UTC | 36m |
| EZY68NC | easyJet | Glasgow International Airport (EGPF) | Glasgow International Airport (EGPF) | 2026-07-30 15:34 UTC | 2026-07-30 22:10 UTC | 6h 35m |
| N351DD |  | Brooksville-Tampa Bay Regional Airport (KBKV) | Savannah/Hilton Head International Airport (KSAV) | 2026-07-30 20:58 UTC | 2026-07-30 22:06 UTC | 1h 7m |
| TKR137 | TKR | Coeur D'Alene/Pappy Boyington Field (KCOE) | Libby Airport (KS59) | 2026-07-30 21:51 UTC | 2026-07-30 22:03 UTC | 12m |
| N18JA |  | Aurora Municipal Airport (KARR) | Humm Airport (06IL) | 2026-07-30 21:45 UTC | 2026-07-30 22:03 UTC | 18m |
| N555NL |  | Bridgeport/Sikorsky Airport (KBDR) | Laguardia Airport (KLGA) | 2026-07-30 21:39 UTC | 2026-07-30 22:02 UTC | 22m |
| N393DS |  | Bowman Field (KLOU) | Bowman Field (KLOU) | 2026-07-30 21:25 UTC | 2026-07-30 22:02 UTC | 36m |
| N319SB |  | K3C8 (K3C8) | Laguardia Airport (KLGA) | 2026-07-30 21:36 UTC | 2026-07-30 22:00 UTC | 24m |
| N89539 |  | Murfreesboro Municipal Airport (KMBT) | Murfreesboro Municipal Airport (KMBT) | 2026-07-30 21:38 UTC | 2026-07-30 21:58 UTC | 20m |
| N88765 |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-07-30 21:25 UTC | 2026-07-30 21:57 UTC | 31m |
| BT11 |  | Camp Pendleton Mcas (Munn Field) Airport (KNFG) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-07-30 20:47 UTC | 2026-07-30 21:53 UTC | 1h 5m |
| TKR184 | TKR | Grant County International Airport (KMWH) | 0WN9 (0WN9) | 2026-07-30 21:39 UTC | 2026-07-30 21:53 UTC | 13m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-07-30 21:51 UTC | 2026-07-30 21:52 UTC | 0m |
| N97VS |  | Allegheny County Airport (KAGC) | Black Airport (9IL7) | 2026-07-30 20:31 UTC | 2026-07-30 21:50 UTC | 1h 18m |
| TKR102 | TKR | Libby Airport (KS59) | Coeur D'Alene/Pappy Boyington Field (KCOE) | 2026-07-30 21:35 UTC | 2026-07-30 21:50 UTC | 14m |
| N900BA |  | Joe Foss Field (KFSD) | Hintzman Airport (4MN1) | 2026-07-30 21:06 UTC | 2026-07-30 21:47 UTC | 40m |
| TKR186 | TKR | Grant County International Airport (KMWH) | 0WN9 (0WN9) | 2026-07-30 21:33 UTC | 2026-07-30 21:46 UTC | 12m |
| TGBER | TGB | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-07-30 21:35 UTC | 2026-07-30 21:45 UTC | 10m |
| HK5489 |  | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 2026-07-30 21:31 UTC | 2026-07-30 21:43 UTC | 11m |
| N247WD |  | Centennial Airport (KAPA) | Artesia Municipal Airport (KATS) | 2026-07-30 20:42 UTC | 2026-07-30 21:42 UTC | 59m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
