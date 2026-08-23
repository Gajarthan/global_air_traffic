# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_19:32:36_UTC-green)

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

**Latest saved flight:** 2026-08-23 19:32:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 19:32:36 UTC

- **229,836** saved flights
- **70,980** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **229,836** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,771,858.9 tonnes** estimated CO2 emissions
- **160,687,472 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9230 |
| 2 | SkyWest Airlines | 8151 |
| 3 | EJA | 4439 |
| 4 | IndiGo | 3881 |
| 5 | American Airlines | 3763 |
| 6 | Southwest Airlines | 3556 |
| 7 | Delta Air Lines | 2941 |
| 8 | ENY | 2805 |
| 9 | LATAM Airlines | 2208 |
| 10 | AZU | 2135 |
| 11 | Vueling | 1953 |
| 12 | Lufthansa | 1874 |
| 13 | LXJ | 1811 |
| 14 | WIF | 1809 |
| 15 | easyJet | 1604 |
| 16 | Swiss International | 1537 |
| 17 | AXM | 1520 |
| 18 | EJU | 1466 |
| 19 | United Airlines | 1455 |
| 20 | QLK | 1448 |
| 21 | Alaska Airlines | 1385 |
| 22 | All Nippon Airways | 1372 |
| 23 | GLO | 1280 |
| 24 | VIV | 1263 |
| 25 | WMT | 1259 |
| 26 | PGT | 1255 |
| 27 | Air France | 1253 |
| 28 | Wizz Air | 1207 |
| 29 | AEE | 1147 |
| 30 | JetBlue | 1147 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 191807 |
| 2 | 🇪🇸 ES | 14755 |
| 3 | 🇧🇷 BR | 13434 |
| 4 | 🇦🇺 AU | 12964 |
| 5 | 🇨🇦 CA | 12680 |
| 6 | 🇮🇹 IT | 12449 |
| 7 | 🇮🇳 IN | 12097 |
| 8 | 🇩🇪 DE | 11322 |
| 9 | 🇬🇧 GB | 10822 |
| 10 | 🇨🇴 CO | 9505 |
| 11 | 🇯🇵 JP | 9314 |
| 12 | 🇫🇷 FR | 9209 |
| 13 | 🇹🇷 TR | 6779 |
| 14 | 🇬🇷 GR | 6765 |
| 15 | 🇲🇽 MX | 6400 |
| 16 | 🇨🇭 CH | 6112 |
| 17 | 🇳🇴 NO | 5650 |
| 18 | 🇲🇾 MY | 4063 |
| 19 | 🇿🇦 ZA | 4013 |
| 20 | 🇹🇭 TH | 3997 |
| 21 | 🇵🇱 PL | 3825 |
| 22 | 🇳🇿 NZ | 3171 |
| 23 | 🇵🇭 PH | 3144 |
| 24 | 🇬🇹 GT | 2892 |
| 25 | 🇰🇷 KR | 2706 |
| 26 | 🇭🇷 HR | 2631 |
| 27 | 🇲🇦 MA | 2332 |
| 28 | 🇲🇪 ME | 2104 |
| 29 | 🇳🇱 NL | 2058 |
| 30 | 🇮🇩 ID | 1978 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4800 |
| 2 | Denver International Airport |  | US | 3734 |
| 3 | Indira Gandhi International Airport |  | IN | 2798 |
| 4 | Tokyo International Airport |  | JP | 2781 |
| 5 | Guaymaral Airport |  | CO | 2653 |
| 6 | Harry Reid International Airport |  | US | 2482 |
| 7 | Zurich Airport |  | CH | 2400 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2348 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2318 |
| 10 | La Aurora Airport |  | GT | 2203 |
| 11 | El Dorado International Airport |  | CO | 2112 |
| 12 | Chicago O'Hare International Airport |  | US | 2080 |
| 13 | Salt Lake City International Airport |  | US | 2023 |
| 14 | Congonhas Airport |  | BR | 1961 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1947 |
| 16 | Frankfurt am Main International Airport |  | DE | 1842 |
| 17 | Madrid Barajas International Airport |  | ES | 1805 |
| 18 | Capua Airport |  | IT | 1804 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1721 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1710 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1653 |
| 22 | Malpensa International Airport |  | IT | 1643 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1612 |
| 24 | Charles de Gaulle International Airport |  | FR | 1598 |
| 25 | Macau International Airport |  | MO | 1597 |
| 26 | Ninoy Aquino International Airport |  | PH | 1509 |
| 27 | Charlotte/Douglas International Airport |  | US | 1502 |
| 28 | Kuala Lumpur International Airport |  | MY | 1472 |
| 29 | Barcelona International Airport |  | ES | 1438 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1397 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1376 |
| 32 | Viracopos International Airport |  | BR | 1367 |
| 33 | Bengaluru International Airport |  | IN | 1358 |
| 34 | Seattle-Tacoma International Airport |  | US | 1354 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1348 |
| 36 | Don Mueang International Airport |  | TH | 1307 |
| 37 | Calgary International Airport |  | CA | 1303 |
| 38 | Oslo Gardermoen Airport |  | NO | 1280 |
| 39 | Vitoria/Foronda Airport |  | ES | 1251 |
| 40 | O. R. Tambo International Airport |  | ZA | 1249 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1076 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 834 | 21m | 244 km | 3,511.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 575 | 1h 6m | 770 km | 7,638.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 567 | 24m | 225 km | 2,199.7 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 558 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 515 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 380 | 27m | 275 km | 1,800.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 353 | 1h 50m | 1,423 km | 8,663.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 333 | 44m | 241 km | 1,383.2 t |
| 11 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 324 | 21m | 250 km | 1,399.5 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 315 | 1h 7m | 706 km | 3,835.1 t |
| 13 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 14 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 310 | 44m | 555 km | 2,968.4 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 306 | 22m | 55 km | 290.8 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 298 | 24m | 218 km | 1,122.7 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 295 | 1h 38m | 1,156 km | 5,885.1 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 285 | 19m | 99 km | 488.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 280 | 27m | 215 km | 1,037.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 269 | 1h 14m | 961 km | 4,458.8 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 267 | 12m | - | - |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 261 | 19m | 144 km | 649.2 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 247 | 1h 50m | 1,304 km | 5,556.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 242 | 28m | 152 km | 632.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 241 | 15m | 154 km | 638.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-23 18:49 UTC | 2026-08-23 19:32 UTC | 43m |
| N9027C |  | Elizabeth City Cg Air Station/Regional Airport (KECG) | Pine Island Airport (7NC2) | 2026-08-23 19:19 UTC | 2026-08-23 19:30 UTC | 10m |
| AFL2147 | AFL | Antalya International Airport (LTAI) | Sheremetyevo International Airport (UUEE) | 2026-08-23 15:10 UTC | 2026-08-23 19:28 UTC | 4h 17m |
| SWR105W | Swiss International | Hamburg Airport (EDDH) | Zurich Airport (LSZH) | 2026-08-23 18:20 UTC | 2026-08-23 19:27 UTC | 1h 6m |
| N2224W |  | Lake Elmo Airport (K21D) | St Paul Downtown Holman Field (KSTP) | 2026-08-23 18:38 UTC | 2026-08-23 19:26 UTC | 48m |
| N1314T |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-23 18:15 UTC | 2026-08-23 19:21 UTC | 1h 6m |
| N1507X |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-08-23 18:54 UTC | 2026-08-23 19:16 UTC | 22m |
| N556C |  | Johnson Airport (3AK4) | Drift River Airport (3AK5) | 2026-08-23 18:44 UTC | 2026-08-23 19:16 UTC | 31m |
| MSR712 | EgyptAir | Beirut Rafic Hariri International Airport (OLBA) | HE12 (HE12) | 2026-08-23 18:03 UTC | 2026-08-23 19:14 UTC | 1h 10m |
| N432ER |  | Lake In The Hills Airport (K3CK) | Funny Farm Airport (5LL7) | 2026-08-23 18:49 UTC | 2026-08-23 19:14 UTC | 24m |
| N4841Y |  | Kelly Air Park (CO15) | Ambrosich Field (4CO7) | 2026-08-23 18:59 UTC | 2026-08-23 19:09 UTC | 10m |
| TGNGT | TGN | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 2026-08-23 18:33 UTC | 2026-08-23 19:09 UTC | 35m |
| N3028E |  | Linden Airport (KLDJ) | Central Jersey Regional Airport (K47N) | 2026-08-23 17:53 UTC | 2026-08-23 19:08 UTC | 1h 15m |
| N993AK |  | Merrill Field (PAMR) | Big Creek Airport (AK51) | 2026-08-23 18:22 UTC | 2026-08-23 19:05 UTC | 43m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-08-23 18:46 UTC | 2026-08-23 19:05 UTC | 18m |
| TWY85 | TWY | Centennial Airport (KAPA) | NV13 (NV13) | 2026-08-23 17:19 UTC | 2026-08-23 19:03 UTC | 1h 43m |
| N914LD |  | Oakland San Francisco Bay Airport (KOAK) | Scottsdale Airport (KSDL) | 2026-08-23 17:24 UTC | 2026-08-23 19:03 UTC | 1h 38m |
| N362DS |  | Washington Manassas/Harry P Davis Field (KHEF) | Lancaster Airport (KLNS) | 2026-08-23 17:59 UTC | 2026-08-23 19:00 UTC | 1h 1m |
| N242DP |  | Smyrna Airport (KMQY) | Lebanon Municipal Airport (KM54) | 2026-08-23 17:47 UTC | 2026-08-23 19:00 UTC | 1h 13m |
| CCA866 | Air China | Madrid Barajas International Airport (LEMD) | Smolensk North Airport (XUBS) | 2026-08-23 16:06 UTC | 2026-08-23 18:59 UTC | 2h 53m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
