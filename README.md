# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_03:12:47_UTC-green)

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

**Latest saved flight:** 2026-08-25 03:12:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 03:12:47 UTC

- **234,055** saved flights
- **71,813** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **234,055** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,819,461.5 tonnes** estimated CO2 emissions
- **163,447,043 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9382 |
| 2 | SkyWest Airlines | 8296 |
| 3 | EJA | 4551 |
| 4 | IndiGo | 3946 |
| 5 | American Airlines | 3815 |
| 6 | Southwest Airlines | 3598 |
| 7 | Delta Air Lines | 2991 |
| 8 | ENY | 2854 |
| 9 | LATAM Airlines | 2251 |
| 10 | AZU | 2183 |
| 11 | Vueling | 1998 |
| 12 | Lufthansa | 1901 |
| 13 | WIF | 1856 |
| 14 | LXJ | 1843 |
| 15 | easyJet | 1632 |
| 16 | Swiss International | 1565 |
| 17 | AXM | 1554 |
| 18 | EJU | 1495 |
| 19 | QLK | 1488 |
| 20 | United Airlines | 1484 |
| 21 | Alaska Airlines | 1411 |
| 22 | All Nippon Airways | 1393 |
| 23 | GLO | 1306 |
| 24 | WMT | 1297 |
| 25 | VIV | 1292 |
| 26 | PGT | 1274 |
| 27 | Air France | 1268 |
| 28 | Wizz Air | 1234 |
| 29 | AEE | 1162 |
| 30 | JetBlue | 1162 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 195018 |
| 2 | 🇪🇸 ES | 15005 |
| 3 | 🇧🇷 BR | 13681 |
| 4 | 🇦🇺 AU | 13239 |
| 5 | 🇨🇦 CA | 12965 |
| 6 | 🇮🇹 IT | 12705 |
| 7 | 🇮🇳 IN | 12291 |
| 8 | 🇩🇪 DE | 11511 |
| 9 | 🇬🇧 GB | 11013 |
| 10 | 🇨🇴 CO | 9842 |
| 11 | 🇯🇵 JP | 9481 |
| 12 | 🇫🇷 FR | 9347 |
| 13 | 🇹🇷 TR | 6929 |
| 14 | 🇬🇷 GR | 6873 |
| 15 | 🇲🇽 MX | 6520 |
| 16 | 🇨🇭 CH | 6225 |
| 17 | 🇳🇴 NO | 5770 |
| 18 | 🇲🇾 MY | 4153 |
| 19 | 🇹🇭 TH | 4123 |
| 20 | 🇿🇦 ZA | 4071 |
| 21 | 🇵🇱 PL | 3894 |
| 22 | 🇳🇿 NZ | 3232 |
| 23 | 🇵🇭 PH | 3199 |
| 24 | 🇬🇹 GT | 2931 |
| 25 | 🇰🇷 KR | 2734 |
| 26 | 🇭🇷 HR | 2686 |
| 27 | 🇲🇦 MA | 2372 |
| 28 | 🇲🇪 ME | 2155 |
| 29 | 🇳🇱 NL | 2092 |
| 30 | 🇮🇩 ID | 2023 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4873 |
| 2 | Denver International Airport |  | US | 3797 |
| 3 | Indira Gandhi International Airport |  | IN | 2846 |
| 4 | Tokyo International Airport |  | JP | 2825 |
| 5 | Guaymaral Airport |  | CO | 2677 |
| 6 | Harry Reid International Airport |  | US | 2515 |
| 7 | Zurich Airport |  | CH | 2442 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2396 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2343 |
| 10 | La Aurora Airport |  | GT | 2234 |
| 11 | El Dorado International Airport |  | CO | 2192 |
| 12 | Chicago O'Hare International Airport |  | US | 2117 |
| 13 | Salt Lake City International Airport |  | US | 2068 |
| 14 | Congonhas Airport |  | BR | 1997 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1971 |
| 16 | Frankfurt am Main International Airport |  | DE | 1863 |
| 17 | Capua Airport |  | IT | 1840 |
| 18 | Madrid Barajas International Airport |  | ES | 1835 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1763 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1732 |
| 21 | Malpensa International Airport |  | IT | 1674 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1664 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1644 |
| 24 | Charles de Gaulle International Airport |  | FR | 1623 |
| 25 | Macau International Airport |  | MO | 1606 |
| 26 | Ninoy Aquino International Airport |  | PH | 1543 |
| 27 | Charlotte/Douglas International Airport |  | US | 1515 |
| 28 | Kuala Lumpur International Airport |  | MY | 1502 |
| 29 | Barcelona International Airport |  | ES | 1475 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1443 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1419 |
| 32 | Viracopos International Airport |  | BR | 1396 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1377 |
| 34 | Seattle-Tacoma International Airport |  | US | 1376 |
| 35 | Bengaluru International Airport |  | IN | 1372 |
| 36 | Calgary International Airport |  | CA | 1343 |
| 37 | Don Mueang International Airport |  | TH | 1342 |
| 38 | Oslo Gardermoen Airport |  | NO | 1307 |
| 39 | Vancouver International Airport |  | CA | 1280 |
| 40 | Vitoria/Foronda Airport |  | ES | 1266 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1085 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 856 | 21m | 244 km | 3,604.4 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 588 | 1h 6m | 770 km | 7,811.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 585 | 24m | 225 km | 2,269.5 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 584 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 523 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 385 | 27m | 275 km | 1,824.4 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 361 | 1h 50m | 1,423 km | 8,859.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 360 | 35m | - | - |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 339 | 44m | 241 km | 1,408.1 t |
| 11 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 328 | 44m | 555 km | 3,140.8 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 327 | 21m | 250 km | 1,412.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 310 | 24m | 218 km | 1,167.9 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 307 | 1h 40m | 1,156 km | 6,124.5 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 289 | 19m | 99 km | 495.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 285 | 27m | 215 km | 1,055.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 272 | 1h 14m | 961 km | 4,508.5 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 271 | 13m | - | - |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 267 | 29m | 304 km | 1,399.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 266 | 19m | 144 km | 661.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 252 | 15m | 154 km | 667.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 251 | 1h 50m | 1,304 km | 5,646.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TRP7 | TRP | St Mary's County Regional Airport (K2W6) | Joint Base Andrews Airport (KADW) | 2026-08-25 02:54 UTC | 2026-08-25 03:12 UTC | 18m |
| N232LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Van Nuys Airport (KVNY) | 2026-08-25 01:20 UTC | 2026-08-25 03:02 UTC | 1h 42m |
| OXF6398 | OXF | Falcon Field (KFFZ) | Falcon Field (KFFZ) | 2026-08-25 02:41 UTC | 2026-08-25 03:01 UTC | 20m |
| CFR91 | CFR | Redding Regional Airport (KRDD) | California Pines Airport (KA24) | 2026-08-25 02:41 UTC | 2026-08-25 03:00 UTC | 19m |
| N919CM |  | Colonel James Jabara Airport (KAAO) | Cessna Acft Field (KCEA) | 2026-08-25 02:33 UTC | 2026-08-25 02:59 UTC | 25m |
| CPA466 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-25 01:09 UTC | 2026-08-25 02:54 UTC | 1h 45m |
| JA012G |  | Fukuoka Airport (RJFF) | Tsuiki Airport (RJFZ) | 2026-08-25 02:40 UTC | 2026-08-25 02:52 UTC | 11m |
| CFR95 | CFR | Tulelake Municipal Airport (KO81) | California Pines Airport (KA24) | 2026-08-25 01:28 UTC | 2026-08-25 02:51 UTC | 1h 22m |
| ZKWJH | ZKW | Hamilton International Airport (NZHN) | Hamilton International Airport (NZHN) | 2026-08-25 01:54 UTC | 2026-08-25 02:48 UTC | 53m |
| BURNY10 | BUR | Danaher Airport (7TX0) | Smiley Johnson Municipal/Bass Field (KE34) | 2026-08-25 02:26 UTC | 2026-08-25 02:43 UTC | 17m |
| HOOK63 | HOO | Flying E Ranch Airport (OK16) | 75OK (75OK) | 2026-08-25 02:08 UTC | 2026-08-25 02:40 UTC | 32m |
| TTW231 | TTW | Taiwan Taoyuan International Airport (RCTP) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-24 23:04 UTC | 2026-08-25 02:37 UTC | 3h 33m |
| CPA015 | Cathay Pacific | Narita International Airport (RJAA) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-24 23:48 UTC | 2026-08-25 02:35 UTC | 2h 46m |
| TKR136 | TKR | Boise Air Trml/Gowen Field (KBOI) | Mountain Home Municipal Airport (KU76) | 2026-08-25 02:22 UTC | 2026-08-25 02:32 UTC | 10m |
| IY22 |  | Seoul Air Base (RKSM) | G 419 Airport (RK48) | 2026-08-25 02:11 UTC | 2026-08-25 02:28 UTC | 16m |
| N272SF |  | St George Regional Airport (KSGU) | Four Pillars Airport (AZ21) | 2026-08-25 01:21 UTC | 2026-08-25 02:27 UTC | 1h 5m |
| FFT2457 | FFT | Los Angeles International Airport (KLAX) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-25 01:40 UTC | 2026-08-25 02:27 UTC | 46m |
| A6GBA |  | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-25 02:17 UTC | 2026-08-25 02:27 UTC | 9m |
| ARCAS06 | ARC | Danaher Airport (7TX0) | 5TA4 (5TA4) | 2026-08-25 02:00 UTC | 2026-08-25 02:20 UTC | 19m |
| 8AX |  | Hillman Farm Airport (YHLM) | Hillman Farm Airport (YHLM) | 2026-08-25 02:08 UTC | 2026-08-25 02:18 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
