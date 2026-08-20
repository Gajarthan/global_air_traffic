# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_00:10:14_UTC-green)

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

**Latest saved flight:** 2026-08-20 00:10:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 00:10:14 UTC

- **217,849** saved flights
- **68,651** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **217,849** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,621,155.9 tonnes** estimated CO2 emissions
- **151,951,065 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8713 |
| 2 | SkyWest Airlines | 7809 |
| 3 | EJA | 4245 |
| 4 | IndiGo | 3693 |
| 5 | American Airlines | 3634 |
| 6 | Southwest Airlines | 3463 |
| 7 | Delta Air Lines | 2820 |
| 8 | ENY | 2698 |
| 9 | LATAM Airlines | 2068 |
| 10 | AZU | 2000 |
| 11 | Vueling | 1827 |
| 12 | Lufthansa | 1813 |
| 13 | WIF | 1738 |
| 14 | LXJ | 1726 |
| 15 | easyJet | 1511 |
| 16 | Swiss International | 1448 |
| 17 | AXM | 1418 |
| 18 | United Airlines | 1382 |
| 19 | EJU | 1355 |
| 20 | QLK | 1351 |
| 21 | Alaska Airlines | 1332 |
| 22 | All Nippon Airways | 1306 |
| 23 | VIV | 1193 |
| 24 | GLO | 1187 |
| 25 | PGT | 1178 |
| 26 | Air France | 1177 |
| 27 | WMT | 1142 |
| 28 | JetBlue | 1109 |
| 29 | Wizz Air | 1105 |
| 30 | AEE | 1089 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 183897 |
| 2 | 🇪🇸 ES | 13942 |
| 3 | 🇧🇷 BR | 12591 |
| 4 | 🇦🇺 AU | 12205 |
| 5 | 🇨🇦 CA | 12024 |
| 6 | 🇮🇹 IT | 11560 |
| 7 | 🇮🇳 IN | 11502 |
| 8 | 🇩🇪 DE | 10765 |
| 9 | 🇬🇧 GB | 10214 |
| 10 | 🇨🇴 CO | 8957 |
| 11 | 🇯🇵 JP | 8876 |
| 12 | 🇫🇷 FR | 8666 |
| 13 | 🇬🇷 GR | 6347 |
| 14 | 🇹🇷 TR | 6258 |
| 15 | 🇲🇽 MX | 6083 |
| 16 | 🇨🇭 CH | 5768 |
| 17 | 🇳🇴 NO | 5405 |
| 18 | 🇲🇾 MY | 3746 |
| 19 | 🇿🇦 ZA | 3685 |
| 20 | 🇵🇱 PL | 3596 |
| 21 | 🇹🇭 TH | 3539 |
| 22 | 🇳🇿 NZ | 3016 |
| 23 | 🇵🇭 PH | 2908 |
| 24 | 🇬🇹 GT | 2763 |
| 25 | 🇰🇷 KR | 2612 |
| 26 | 🇭🇷 HR | 2390 |
| 27 | 🇲🇦 MA | 2189 |
| 28 | 🇳🇱 NL | 1940 |
| 29 | 🇲🇪 ME | 1909 |
| 30 | 🇮🇩 ID | 1818 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4590 |
| 2 | Denver International Airport |  | US | 3569 |
| 3 | Tokyo International Airport |  | JP | 2665 |
| 4 | Indira Gandhi International Airport |  | IN | 2632 |
| 5 | Guaymaral Airport |  | CO | 2595 |
| 6 | Harry Reid International Airport |  | US | 2414 |
| 7 | Zurich Airport |  | CH | 2258 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2244 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2213 |
| 10 | La Aurora Airport |  | GT | 2103 |
| 11 | El Dorado International Airport |  | CO | 2042 |
| 12 | Chicago O'Hare International Airport |  | US | 2007 |
| 13 | Salt Lake City International Airport |  | US | 1926 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1899 |
| 15 | Congonhas Airport |  | BR | 1840 |
| 16 | Frankfurt am Main International Airport |  | DE | 1779 |
| 17 | Madrid Barajas International Airport |  | ES | 1703 |
| 18 | Capua Airport |  | IT | 1655 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1643 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1615 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1603 |
| 22 | Macau International Airport |  | MO | 1563 |
| 23 | Malpensa International Airport |  | IT | 1534 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1519 |
| 25 | Charles de Gaulle International Airport |  | FR | 1493 |
| 26 | Charlotte/Douglas International Airport |  | US | 1462 |
| 27 | Ninoy Aquino International Airport |  | PH | 1381 |
| 28 | Kuala Lumpur International Airport |  | MY | 1379 |
| 29 | Barcelona International Airport |  | ES | 1333 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1330 |
| 31 | Bengaluru International Airport |  | IN | 1316 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1302 |
| 33 | Seattle-Tacoma International Airport |  | US | 1296 |
| 34 | Viracopos International Airport |  | BR | 1277 |
| 35 | Calgary International Airport |  | CA | 1230 |
| 36 | Oslo Gardermoen Airport |  | NO | 1205 |
| 37 | Vitoria/Foronda Airport |  | ES | 1204 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1201 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1173 |
| 40 | Reno/Tahoe International Airport |  | US | 1169 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 777 | 21m | 244 km | 3,271.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 535 | 1h 7m | 770 km | 7,107.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 509 | 24m | 225 km | 1,974.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 492 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 485 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 363 | 27m | 275 km | 1,720.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 318 | 1h 49m | 1,423 km | 7,804.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 316 | 44m | 241 km | 1,312.6 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 294 | 22m | 55 km | 279.4 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 285 | 21m | 250 km | 1,231.0 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 271 | 19m | 99 km | 464.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 269 | 1h 38m | 1,156 km | 5,366.4 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 267 | 27m | 215 km | 988.9 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 258 | 1h 14m | 961 km | 4,276.5 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 258 | 13m | - | - |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 256 | 31m | 369 km | 1,629.5 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 247 | 19m | 144 km | 614.4 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 246 | 12m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 236 | 1h 49m | 1,304 km | 5,309.4 t |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 29 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 233 | 44m | 555 km | 2,231.1 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1590V |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-08-19 23:47 UTC | 2026-08-20 00:10 UTC | 22m |
| TKR104 | TKR | Sandpoint Airport (KSZT) | Coeur D'Alene Airport (KCOE) | 2026-08-19 23:54 UTC | 2026-08-20 00:07 UTC | 13m |
| RBG545 | RBG | Bergamo / Orio Al Serio Airport (LIME) | Cairo International Airport (HECA) | 2026-08-19 20:37 UTC | 2026-08-20 00:01 UTC | 3h 23m |
| TKR167 | TKR | Boise Air Trml/Gowen Field (KBOI) | Harrington Airport (20ID) | 2026-08-19 23:52 UTC | 2026-08-19 23:59 UTC | 6m |
| GRIT79 | GRI | Cheyenne Regional/Jerry Olson Field (KCYS) | Laramie Regional Airport (KLAR) | 2026-08-19 23:00 UTC | 2026-08-19 23:48 UTC | 48m |
| TKR137 | TKR | Boise Air Trml/Gowen Field (KBOI) | Harrington Airport (20ID) | 2026-08-19 23:39 UTC | 2026-08-19 23:44 UTC | 5m |
| OFT3 | OFT | Henderson/Oxford Airport (KHNZ) | Richard Arthur Field (KM95) | 2026-08-19 21:51 UTC | 2026-08-19 23:43 UTC | 1h 51m |
| ASP827 | ASP | Calgary International Airport (CYYC) | Vancouver International Airport (CYVR) | 2026-08-19 22:09 UTC | 2026-08-19 23:43 UTC | 1h 33m |
| N73KG |  | Mason City Municipal Airport (KMCW) | Mason City Municipal Airport (KMCW) | 2026-08-19 23:40 UTC | 2026-08-19 23:43 UTC | 2m |
| N5399K |  | Bolingbrook's Clow International Airport (K1C5) | 95LL (95LL) | 2026-08-19 23:23 UTC | 2026-08-19 23:42 UTC | 18m |
| N250LC |  | Addison Airport (KADS) | Bangor International Airport (KBGR) | 2026-08-19 20:18 UTC | 2026-08-19 23:37 UTC | 3h 18m |
| OXV | OXV | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-19 23:25 UTC | 2026-08-19 23:36 UTC | 11m |
| N922ST |  | Wallom Field (8CA8) | Truckee-Tahoe Airport (KTRK) | 2026-08-19 22:48 UTC | 2026-08-19 23:35 UTC | 47m |
| LS16 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-19 20:54 UTC | 2026-08-19 23:33 UTC | 2h 39m |
| BOE123 | BOE | Seattle Paine Field International Airport (KPAE) | Franz Ranch Airport (33WA) | 2026-08-19 20:09 UTC | 2026-08-19 23:32 UTC | 3h 22m |
| DAL1342 | Delta Air Lines | Salt Lake City International Airport (KSLC) | Sacramento International Airport (KSMF) | 2026-08-19 22:12 UTC | 2026-08-19 23:32 UTC | 1h 19m |
| MB25F |  | Perth International Airport (YPPH) | Rothsay Mine Airport (YROT) | 2026-08-19 22:51 UTC | 2026-08-19 23:32 UTC | 40m |
| CFWZK | CFW | Vancouver International Airport (CYVR) | Princeton Airport (CYDC) | 2026-08-19 22:51 UTC | 2026-08-19 23:31 UTC | 40m |
| GBA713 | GBA | Auckland International Airport (NZAA) | Kaikohe Airport (NZKO) | 2026-08-19 22:52 UTC | 2026-08-19 23:31 UTC | 39m |
| N337RH |  | Rickenbacker International Airport (KLCK) | Black River Ranch Airport (1MI3) | 2026-08-19 21:46 UTC | 2026-08-19 23:31 UTC | 1h 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
