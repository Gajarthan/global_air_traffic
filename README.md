# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--04_14:11:07_UTC-green)

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

**Latest saved flight:** 2026-10-04 14:11:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-10-04 14:11:07 UTC

- **276,096** saved flights
- **80,345** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **276,096** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,342,221.5 tonnes** estimated CO2 emissions
- **193,751,974 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10826 |
| 2 | SkyWest Airlines | 9604 |
| 3 | EJA | 5405 |
| 4 | IndiGo | 4604 |
| 5 | American Airlines | 4271 |
| 6 | Southwest Airlines | 4054 |
| 7 | Delta Air Lines | 3429 |
| 8 | ENY | 3225 |
| 9 | LATAM Airlines | 2676 |
| 10 | AZU | 2599 |
| 11 | Vueling | 2287 |
| 12 | WIF | 2247 |
| 13 | LXJ | 2182 |
| 14 | Lufthansa | 2074 |
| 15 | easyJet | 1833 |
| 16 | Swiss International | 1805 |
| 17 | QLK | 1778 |
| 18 | EJU | 1717 |
| 19 | AXM | 1694 |
| 20 | United Airlines | 1682 |
| 21 | Alaska Airlines | 1629 |
| 22 | All Nippon Airways | 1577 |
| 23 | PGT | 1552 |
| 24 | GLO | 1540 |
| 25 | WMT | 1535 |
| 26 | Air France | 1518 |
| 27 | VIV | 1514 |
| 28 | Wizz Air | 1489 |
| 29 | CXK | 1363 |
| 30 | AEE | 1313 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 230321 |
| 2 | 🇪🇸 ES | 17260 |
| 3 | 🇧🇷 BR | 16222 |
| 4 | 🇦🇺 AU | 15919 |
| 5 | 🇨🇦 CA | 15378 |
| 6 | 🇮🇹 IT | 14880 |
| 7 | 🇮🇳 IN | 14572 |
| 8 | 🇩🇪 DE | 13188 |
| 9 | 🇨🇴 CO | 12829 |
| 10 | 🇬🇧 GB | 12712 |
| 11 | 🇫🇷 FR | 10916 |
| 12 | 🇯🇵 JP | 10523 |
| 13 | 🇹🇷 TR | 8338 |
| 14 | 🇬🇷 GR | 7917 |
| 15 | 🇲🇽 MX | 7625 |
| 16 | 🇨🇭 CH | 7332 |
| 17 | 🇳🇴 NO | 6813 |
| 18 | 🇹🇭 TH | 4958 |
| 19 | 🇲🇾 MY | 4587 |
| 20 | 🇿🇦 ZA | 4572 |
| 21 | 🇵🇱 PL | 4515 |
| 22 | 🇳🇿 NZ | 3922 |
| 23 | 🇵🇭 PH | 3649 |
| 24 | 🇬🇹 GT | 3464 |
| 25 | 🇭🇷 HR | 3138 |
| 26 | 🇰🇷 KR | 3105 |
| 27 | 🇲🇦 MA | 2725 |
| 28 | 🇲🇪 ME | 2593 |
| 29 | 🇳🇱 NL | 2463 |
| 30 | 🇮🇩 ID | 2281 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5597 |
| 2 | Denver International Airport |  | US | 4505 |
| 3 | Indira Gandhi International Airport |  | IN | 3291 |
| 4 | Tokyo International Airport |  | JP | 3156 |
| 5 | El Dorado International Airport |  | CO | 3070 |
| 6 | Harry Reid International Airport |  | US | 2973 |
| 7 | Zurich Airport |  | CH | 2867 |
| 8 | Guaymaral Airport |  | CO | 2853 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2757 |
| 10 | La Aurora Airport |  | GT | 2635 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2633 |
| 12 | Salt Lake City International Airport |  | US | 2455 |
| 13 | Congonhas Airport |  | BR | 2357 |
| 14 | Chicago O'Hare International Airport |  | US | 2328 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2260 |
| 16 | Capua Airport |  | IT | 2144 |
| 17 | Madrid Barajas International Airport |  | ES | 2125 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2110 |
| 19 | Frankfurt am Main International Airport |  | DE | 2073 |
| 20 | Enrique Olaya Herrera Airport |  | CO | 1959 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1958 |
| 22 | Charles de Gaulle International Airport |  | FR | 1956 |
| 23 | Malpensa International Airport |  | IT | 1949 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1929 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1840 |
| 26 | Macau International Airport |  | MO | 1797 |
| 27 | Ninoy Aquino International Airport |  | PH | 1795 |
| 28 | Charlotte/Douglas International Airport |  | US | 1723 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1716 |
| 30 | Barcelona International Airport |  | ES | 1701 |
| 31 | Viracopos International Airport |  | BR | 1656 |
| 32 | Kuala Lumpur International Airport |  | MY | 1644 |
| 33 | Seattle-Tacoma International Airport |  | US | 1624 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1622 |
| 35 | Calgary International Airport |  | CA | 1568 |
| 36 | Don Mueang International Airport |  | TH | 1562 |
| 37 | Oslo Gardermoen Airport |  | NO | 1549 |
| 38 | Vancouver International Airport |  | CA | 1547 |
| 39 | Bengaluru International Airport |  | IN | 1542 |
| 40 | Reno/Tahoe International Airport |  | US | 1497 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1134 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1042 | 21m | 244 km | 4,387.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 767 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 698 | 24m | 225 km | 2,707.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 698 | 1h 6m | 770 km | 9,272.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 614 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 461 | 44m | 555 km | 4,414.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 444 | 27m | 275 km | 2,103.9 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 436 | 1h 50m | 1,423 km | 10,700.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 424 | 44m | 241 km | 1,761.2 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 395 | 24m | 218 km | 1,488.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 382 | 35m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 375 | 23m | 55 km | 356.4 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 371 | 21m | 250 km | 1,602.5 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 354 | 12m | - | - |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 353 | 13m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 348 | 1h 6m | 706 km | 4,236.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 344 | 19m | 99 km | 589.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 343 | 26m | 215 km | 1,270.3 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 337 | 1h 40m | 1,156 km | 6,723.0 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 322 | 19m | 144 km | 801.0 t |
| 22 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 321 | 18m | 14 km | 80.3 t |
| 23 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 312 | 42m | 535 km | 2,881.5 t |
| 24 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 312 | 1h 14m | 961 km | 5,171.6 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 298 | 1h 50m | 1,304 km | 6,704.2 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 274 | 44m | 431 km | 2,039.0 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 274 | 51m | 556 km | 2,626.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BAW771C | British Airways | Stockholm-Arlanda Airport (ESSA) | London Heathrow Airport (EGLL) | 2026-10-04 11:44 UTC | 2026-10-04 14:11 UTC | 2h 26m |
| N567FL |  | Trenton Mercer Airport (KTTN) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-10-04 13:26 UTC | 2026-10-04 13:58 UTC | 32m |
| N270GX |  | Sky Manor Airport (KN40) | Lehigh Valley International Airport (KABE) | 2026-10-04 13:23 UTC | 2026-10-04 13:56 UTC | 32m |
| OKBUI74 | OKB | Mlada Boleslav Airport (LKMB) | Mlada Boleslav Airport (LKMB) | 2026-10-04 13:43 UTC | 2026-10-04 13:54 UTC | 10m |
| GRDWN | GRD | Coventry Airport (EGBE) | Caernarfon Airport (EGCK) | 2026-10-04 12:53 UTC | 2026-10-04 13:50 UTC | 57m |
| N247LT |  | Nashville International Airport (KBNA) | Dane County Regional/Truax Field (KMSN) | 2026-10-04 12:42 UTC | 2026-10-04 13:50 UTC | 1h 8m |
| OEDTA | OED | Stockerau Airport (LOAU) | Stockerau Airport (LOAU) | 2026-10-04 13:23 UTC | 2026-10-04 13:47 UTC | 23m |
| HK5214 |  | Tunja Airport (SKTJ) | Tunja Airport (SKTJ) | 2026-10-04 13:06 UTC | 2026-10-04 13:42 UTC | 35m |
| N52CP |  | Phoenix Sky Harbor International Airport (KPHX) | Rocky Mountain Metro Airport (KBJC) | 2026-10-04 12:11 UTC | 2026-10-04 13:39 UTC | 1h 27m |
| NUS531 | NUS | Chicago Executive Airport (KPWK) | Ball Airport (5MS8) | 2026-10-04 12:18 UTC | 2026-10-04 13:39 UTC | 1h 20m |
| DEEKY | DEE | Vogtareuth Airport (EDNV) | Vogtareuth Airport (EDNV) | 2026-10-04 13:26 UTC | 2026-10-04 13:37 UTC | 11m |
| SPGTS | SPG | Pila Airport (EPPI) | Pila Airport (EPPI) | 2026-10-04 13:31 UTC | 2026-10-04 13:34 UTC | 3m |
| N90JF |  | Antonio/Nery/Juarbe Pol Airport (TJAB) | Antonio/Nery/Juarbe Pol Airport (TJAB) | 2026-10-04 13:16 UTC | 2026-10-04 13:32 UTC | 16m |
| N350PD |  | Long Island Mac Arthur Airport (KISP) | Teterboro Airport (KTEB) | 2026-10-04 12:59 UTC | 2026-10-04 13:32 UTC | 32m |
| CTN344 | CTN | LDZI (LDZI) | Visoko Sport Airfield (LQVI) | 2026-10-04 13:02 UTC | 2026-10-04 13:29 UTC | 26m |
| QTR816 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-10-04 06:17 UTC | 2026-10-04 13:25 UTC | 7h 7m |
| SPMOC | SPM | Pobiednik Wielki Airport (EPKP) | Pobiednik Wielki Airport (EPKP) | 2026-10-04 12:29 UTC | 2026-10-04 13:23 UTC | 54m |
| OKDUI87 | OKD | Mlada Boleslav Airport (LKMB) | Mlada Boleslav Airport (LKMB) | 2026-10-04 13:05 UTC | 2026-10-04 13:21 UTC | 16m |
| RYR2428 | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Visoko Sport Airfield (LQVI) | 2026-10-04 12:23 UTC | 2026-10-04 13:19 UTC | 56m |
| N8760C |  | Lake In The Hills Airport (K3CK) | Campbell Airport (KC81) | 2026-10-04 13:07 UTC | 2026-10-04 13:18 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
