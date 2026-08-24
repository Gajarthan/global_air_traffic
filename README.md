# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_23:18:47_UTC-green)

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

**Latest saved flight:** 2026-08-24 23:18:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 23:18:47 UTC

- **233,732** saved flights
- **71,747** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **233,732** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,816,581.1 tonnes** estimated CO2 emissions
- **163,280,065 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9382 |
| 2 | SkyWest Airlines | 8283 |
| 3 | EJA | 4546 |
| 4 | IndiGo | 3943 |
| 5 | American Airlines | 3813 |
| 6 | Southwest Airlines | 3593 |
| 7 | Delta Air Lines | 2986 |
| 8 | ENY | 2850 |
| 9 | LATAM Airlines | 2249 |
| 10 | AZU | 2182 |
| 11 | Vueling | 1998 |
| 12 | Lufthansa | 1901 |
| 13 | WIF | 1856 |
| 14 | LXJ | 1842 |
| 15 | easyJet | 1632 |
| 16 | Swiss International | 1565 |
| 17 | AXM | 1551 |
| 18 | EJU | 1495 |
| 19 | United Airlines | 1482 |
| 20 | QLK | 1477 |
| 21 | Alaska Airlines | 1408 |
| 22 | All Nippon Airways | 1386 |
| 23 | GLO | 1306 |
| 24 | WMT | 1297 |
| 25 | VIV | 1286 |
| 26 | PGT | 1274 |
| 27 | Air France | 1268 |
| 28 | Wizz Air | 1234 |
| 29 | AEE | 1161 |
| 30 | JetBlue | 1161 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 194721 |
| 2 | 🇪🇸 ES | 15005 |
| 3 | 🇧🇷 BR | 13676 |
| 4 | 🇦🇺 AU | 13182 |
| 5 | 🇨🇦 CA | 12926 |
| 6 | 🇮🇹 IT | 12704 |
| 7 | 🇮🇳 IN | 12281 |
| 8 | 🇩🇪 DE | 11507 |
| 9 | 🇬🇧 GB | 11011 |
| 10 | 🇨🇴 CO | 9820 |
| 11 | 🇯🇵 JP | 9448 |
| 12 | 🇫🇷 FR | 9346 |
| 13 | 🇹🇷 TR | 6921 |
| 14 | 🇬🇷 GR | 6872 |
| 15 | 🇲🇽 MX | 6495 |
| 16 | 🇨🇭 CH | 6225 |
| 17 | 🇳🇴 NO | 5770 |
| 18 | 🇲🇾 MY | 4144 |
| 19 | 🇹🇭 TH | 4108 |
| 20 | 🇿🇦 ZA | 4071 |
| 21 | 🇵🇱 PL | 3891 |
| 22 | 🇳🇿 NZ | 3218 |
| 23 | 🇵🇭 PH | 3188 |
| 24 | 🇬🇹 GT | 2931 |
| 25 | 🇰🇷 KR | 2726 |
| 26 | 🇭🇷 HR | 2686 |
| 27 | 🇲🇦 MA | 2372 |
| 28 | 🇲🇪 ME | 2155 |
| 29 | 🇳🇱 NL | 2092 |
| 30 | 🇮🇩 ID | 2015 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4867 |
| 2 | Denver International Airport |  | US | 3791 |
| 3 | Indira Gandhi International Airport |  | IN | 2844 |
| 4 | Tokyo International Airport |  | JP | 2818 |
| 5 | Guaymaral Airport |  | CO | 2677 |
| 6 | Harry Reid International Airport |  | US | 2509 |
| 7 | Zurich Airport |  | CH | 2442 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2392 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2343 |
| 10 | La Aurora Airport |  | GT | 2234 |
| 11 | El Dorado International Airport |  | CO | 2188 |
| 12 | Chicago O'Hare International Airport |  | US | 2115 |
| 13 | Salt Lake City International Airport |  | US | 2061 |
| 14 | Congonhas Airport |  | BR | 1996 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1969 |
| 16 | Frankfurt am Main International Airport |  | DE | 1863 |
| 17 | Capua Airport |  | IT | 1840 |
| 18 | Madrid Barajas International Airport |  | ES | 1835 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1762 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1732 |
| 21 | Malpensa International Airport |  | IT | 1674 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1664 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1637 |
| 24 | Charles de Gaulle International Airport |  | FR | 1622 |
| 25 | Macau International Airport |  | MO | 1605 |
| 26 | Ninoy Aquino International Airport |  | PH | 1537 |
| 27 | Charlotte/Douglas International Airport |  | US | 1515 |
| 28 | Kuala Lumpur International Airport |  | MY | 1498 |
| 29 | Barcelona International Airport |  | ES | 1475 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1443 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1412 |
| 32 | Viracopos International Airport |  | BR | 1395 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1373 |
| 34 | Seattle-Tacoma International Airport |  | US | 1373 |
| 35 | Bengaluru International Airport |  | IN | 1372 |
| 36 | Don Mueang International Airport |  | TH | 1339 |
| 37 | Calgary International Airport |  | CA | 1338 |
| 38 | Oslo Gardermoen Airport |  | NO | 1307 |
| 39 | Vancouver International Airport |  | CA | 1274 |
| 40 | Vitoria/Foronda Airport |  | ES | 1266 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1085 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 853 | 21m | 244 km | 3,591.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 586 | 1h 6m | 770 km | 7,784.6 t |
| 4 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 584 | 8m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 581 | 24m | 225 km | 2,254.0 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 523 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 385 | 27m | 275 km | 1,824.4 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 361 | 1h 50m | 1,423 km | 8,859.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 359 | 35m | - | - |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 339 | 44m | 241 km | 1,408.1 t |
| 11 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 327 | 44m | 555 km | 3,131.2 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 327 | 21m | 250 km | 1,412.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 310 | 24m | 218 km | 1,167.9 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 306 | 1h 38m | 1,156 km | 6,104.6 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 289 | 19m | 99 km | 495.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 285 | 27m | 215 km | 1,055.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 272 | 1h 14m | 961 km | 4,508.5 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 271 | 13m | - | - |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 266 | 29m | 304 km | 1,394.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 266 | 19m | 144 km | 661.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 251 | 15m | 154 km | 665.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 250 | 1h 50m | 1,304 km | 5,624.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BT614 |  | Ensenada Airport (MMES) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-24 22:42 UTC | 2026-08-24 23:18 UTC | 36m |
| N6094E |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-24 22:48 UTC | 2026-08-24 23:10 UTC | 22m |
| N92353 |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | San Martin Airport (KE16) | 2026-08-24 22:39 UTC | 2026-08-24 23:07 UTC | 28m |
| N9342T |  | Atlanta Regional Falcon Field (KFFC) | Atlanta Regional Falcon Field (KFFC) | 2026-08-24 21:53 UTC | 2026-08-24 23:05 UTC | 1h 11m |
| AAL3328 | American Airlines | Austin-Bergstrom International Airport (KAUS) | Phoenix Sky Harbor International Airport (KPHX) | 2026-08-24 21:11 UTC | 2026-08-24 23:04 UTC | 1h 52m |
| BT615 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-24 22:44 UTC | 2026-08-24 23:02 UTC | 17m |
| TKR855 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-08-24 22:29 UTC | 2026-08-24 23:01 UTC | 31m |
| N875PJ |  | Harford County Airport (K0W3) | Ocean City Municipal Airport (KOXB) | 2026-08-24 22:06 UTC | 2026-08-24 22:59 UTC | 53m |
| CAL5381 | CAL | Seattle-Tacoma International Airport (KSEA) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-24 11:17 UTC | 2026-08-24 22:58 UTC | 11h 41m |
| JUMP16 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-08-24 21:37 UTC | 2026-08-24 22:55 UTC | 1h 17m |
| N3779T |  | Dupage Airport (KDPA) | Wade Airport (56LL) | 2026-08-24 22:14 UTC | 2026-08-24 22:52 UTC | 38m |
| N458MM |  | San Carlos Airport (KSQL) | Buchanan Field (KCCR) | 2026-08-24 21:51 UTC | 2026-08-24 22:45 UTC | 54m |
| SPSTR9 | SPS | Oakland San Francisco Bay Airport (KOAK) | Riverside Airport (KRAL) | 2026-08-24 21:09 UTC | 2026-08-24 22:43 UTC | 1h 34m |
| TKR873 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-08-24 22:29 UTC | 2026-08-24 22:38 UTC | 9m |
| N343BM |  | Renton Municipal Airport (KRNT) | Portland-Hillsboro Airport (KHIO) | 2026-08-24 21:30 UTC | 2026-08-24 22:34 UTC | 1h 4m |
| FTO383 | FTO | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-08-24 21:47 UTC | 2026-08-24 22:34 UTC | 47m |
| N161EA |  | Perkins Airport (5OK8) | University Of Oklahoma Westheimer Airport (KOUN) | 2026-08-24 22:03 UTC | 2026-08-24 22:33 UTC | 30m |
| N1885M |  | Wasilla Airport (PAWS) | Ted Stevens Anchorage International Airport (PANC) | 2026-08-24 22:13 UTC | 2026-08-24 22:32 UTC | 18m |
| N717FH |  | Albany Municipal Airport (KT23) | Marion County Regional Airport (KFLP) | 2026-08-24 21:40 UTC | 2026-08-24 22:32 UTC | 51m |
| DAH1543 | DAH | Charles de Gaulle International Airport (LFPG) | Ain Oussera Airport (DAAQ) | 2026-08-24 20:36 UTC | 2026-08-24 22:28 UTC | 1h 52m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
