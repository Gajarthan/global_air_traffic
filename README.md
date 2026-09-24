# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_06:11:21_UTC-green)

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

**Latest saved flight:** 2026-09-24 06:11:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-24 06:11:21 UTC

- **267,986** saved flights
- **78,684** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **267,986** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,250,448.4 tonnes** estimated CO2 emissions
- **188,431,793 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10576 |
| 2 | SkyWest Airlines | 9323 |
| 3 | EJA | 5209 |
| 4 | IndiGo | 4489 |
| 5 | American Airlines | 4172 |
| 6 | Southwest Airlines | 3938 |
| 7 | Delta Air Lines | 3333 |
| 8 | ENY | 3149 |
| 9 | LATAM Airlines | 2582 |
| 10 | AZU | 2512 |
| 11 | Vueling | 2240 |
| 12 | WIF | 2174 |
| 13 | LXJ | 2104 |
| 14 | Lufthansa | 2045 |
| 15 | easyJet | 1798 |
| 16 | Swiss International | 1760 |
| 17 | QLK | 1731 |
| 18 | EJU | 1685 |
| 19 | AXM | 1673 |
| 20 | United Airlines | 1643 |
| 21 | Alaska Airlines | 1585 |
| 22 | All Nippon Airways | 1545 |
| 23 | PGT | 1508 |
| 24 | WMT | 1501 |
| 25 | GLO | 1494 |
| 26 | Air France | 1470 |
| 27 | VIV | 1463 |
| 28 | Wizz Air | 1454 |
| 29 | CXK | 1310 |
| 30 | AEE | 1289 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 222883 |
| 2 | 🇪🇸 ES | 16808 |
| 3 | 🇧🇷 BR | 15664 |
| 4 | 🇦🇺 AU | 15435 |
| 5 | 🇨🇦 CA | 14951 |
| 6 | 🇮🇹 IT | 14532 |
| 7 | 🇮🇳 IN | 14203 |
| 8 | 🇩🇪 DE | 12883 |
| 9 | 🇬🇧 GB | 12418 |
| 10 | 🇨🇴 CO | 12257 |
| 11 | 🇫🇷 FR | 10665 |
| 12 | 🇯🇵 JP | 10322 |
| 13 | 🇹🇷 TR | 8121 |
| 14 | 🇬🇷 GR | 7749 |
| 15 | 🇲🇽 MX | 7387 |
| 16 | 🇨🇭 CH | 7135 |
| 17 | 🇳🇴 NO | 6628 |
| 18 | 🇹🇭 TH | 4805 |
| 19 | 🇲🇾 MY | 4518 |
| 20 | 🇿🇦 ZA | 4482 |
| 21 | 🇵🇱 PL | 4395 |
| 22 | 🇳🇿 NZ | 3749 |
| 23 | 🇵🇭 PH | 3556 |
| 24 | 🇬🇹 GT | 3392 |
| 25 | 🇭🇷 HR | 3056 |
| 26 | 🇰🇷 KR | 3037 |
| 27 | 🇲🇦 MA | 2672 |
| 28 | 🇲🇪 ME | 2512 |
| 29 | 🇳🇱 NL | 2399 |
| 30 | 🇮🇩 ID | 2238 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5459 |
| 2 | Denver International Airport |  | US | 4350 |
| 3 | Indira Gandhi International Airport |  | IN | 3215 |
| 4 | Tokyo International Airport |  | JP | 3087 |
| 5 | El Dorado International Airport |  | CO | 2894 |
| 6 | Harry Reid International Airport |  | US | 2865 |
| 7 | Guaymaral Airport |  | CO | 2805 |
| 8 | Zurich Airport |  | CH | 2781 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2690 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2581 |
| 11 | La Aurora Airport |  | GT | 2578 |
| 12 | Salt Lake City International Airport |  | US | 2361 |
| 13 | Chicago O'Hare International Airport |  | US | 2296 |
| 14 | Congonhas Airport |  | BR | 2282 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2193 |
| 16 | Capua Airport |  | IT | 2086 |
| 17 | Madrid Barajas International Airport |  | ES | 2061 |
| 18 | Frankfurt am Main International Airport |  | DE | 2037 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2028 |
| 20 | Malpensa International Airport |  | IT | 1925 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1913 |
| 22 | Charles de Gaulle International Airport |  | FR | 1898 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1882 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1878 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1816 |
| 26 | Macau International Airport |  | MO | 1783 |
| 27 | Ninoy Aquino International Airport |  | PH | 1745 |
| 28 | Charlotte/Douglas International Airport |  | US | 1672 |
| 29 | Barcelona International Airport |  | ES | 1666 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1656 |
| 31 | Viracopos International Airport |  | BR | 1621 |
| 32 | Kuala Lumpur International Airport |  | MY | 1617 |
| 33 | Seattle-Tacoma International Airport |  | US | 1571 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1566 |
| 35 | Calgary International Airport |  | CA | 1528 |
| 36 | Don Mueang International Airport |  | TH | 1522 |
| 37 | Bengaluru International Airport |  | IN | 1511 |
| 38 | Oslo Gardermoen Airport |  | NO | 1506 |
| 39 | Vancouver International Airport |  | CA | 1502 |
| 40 | Antalya International Airport |  | TR | 1431 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1119 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1005 | 21m | 244 km | 4,231.8 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 741 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 675 | 1h 6m | 770 km | 8,966.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 669 | 24m | 225 km | 2,595.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 596 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 442 | 44m | 555 km | 4,232.4 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 428 | 27m | 275 km | 2,028.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 425 | 1h 50m | 1,423 km | 10,430.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 409 | 44m | 241 km | 1,698.9 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 383 | 24m | 218 km | 1,442.9 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 363 | 21m | 250 km | 1,567.9 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 358 | 23m | 55 km | 340.3 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 342 | 12m | - | - |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 340 | 13m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 338 | 1h 6m | 706 km | 4,115.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 336 | 19m | 99 km | 575.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 333 | 26m | 215 km | 1,233.3 t |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 312 | 19m | 144 km | 776.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 304 | 1h 14m | 961 km | 5,039.0 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 293 | 42m | 535 km | 2,706.0 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 27 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 285 | 18m | 14 km | 71.3 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 284 | 28m | 152 km | 742.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 272 | 15m | 154 km | 720.7 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| THY2YM | Turkish Airlines | Istanbul Airport (LTFM) | Istanbul Airport (LTFM) | 2026-09-23 13:55 UTC | 2026-09-24 06:11 UTC | 16h 15m |
| MAS366 | Malaysia Airlines | Kuala Lumpur International Airport (WMKK) | Hsinchu Air Base (RCPO) | 2026-09-24 01:48 UTC | 2026-09-24 06:04 UTC | 4h 15m |
| SHWK414 | SHW | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-24 04:01 UTC | 2026-09-24 05:55 UTC | 1h 54m |
| KR21 |  | Atsugi Naval Air Facility (RJTA) | Kisarazu Airport (RJTK) | 2026-09-24 05:29 UTC | 2026-09-24 05:41 UTC | 12m |
| N76BH |  | Bob Maxwell Memorial Airfield (KOKB) | Hemet-Ryan Airport (KHMT) | 2026-09-24 05:19 UTC | 2026-09-24 05:41 UTC | 21m |
| FGTFB | FGT | Lyon-Bron Airport (LFLY) | Langogne - Lesperon Airport (LFHL) | 2026-09-24 05:08 UTC | 2026-09-24 05:31 UTC | 22m |
| SWR12K | Swiss International | Václav Havel Airport (LKPR) | Zurich Airport (LSZH) | 2026-09-24 04:27 UTC | 2026-09-24 05:24 UTC | 57m |
| QLK171D | QLK | Brisbane International Airport (YBBN) | Port Macquarie Airport (YPMQ) | 2026-09-24 04:26 UTC | 2026-09-24 05:24 UTC | 57m |
| FIN311 | Finnair | Helsinki Vantaa Airport (EFHK) | Vaasa Airport (EFVA) | 2026-09-24 04:37 UTC | 2026-09-24 05:23 UTC | 46m |
| QLK324D | QLK | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-09-24 04:57 UTC | 2026-09-24 05:21 UTC | 24m |
| ZMP | ZMP | Perth Jandakot Airport (YPJT) | Perenjori Airport (YPJI) | 2026-09-24 04:25 UTC | 2026-09-24 05:21 UTC | 56m |
| LLR643 | LLR | Indira Gandhi International Airport (VIDP) | Jaipur International Airport (VIJP) | 2026-09-24 04:48 UTC | 2026-09-24 05:21 UTC | 32m |
| LKF | LKF | Perth Jandakot Airport (YPJT) | Perenjori Airport (YPJI) | 2026-09-24 04:23 UTC | 2026-09-24 05:16 UTC | 53m |
| JTE244 | JTE | Adelaide International Airport (YPAD) | Mount Vivian Airport (YVIV) | 2026-09-24 04:13 UTC | 2026-09-24 05:12 UTC | 59m |
| AAL3010 | American Airlines | Miami International Airport (KMIA) | San Diego International Airport (KSAN) | 2026-09-24 00:34 UTC | 2026-09-24 05:07 UTC | 4h 32m |
| RYR221H | Ryanair | Copernicus Wrocław Airport (EPWR) | Brac Airport (LDSB) | 2026-09-24 03:56 UTC | 2026-09-24 05:05 UTC | 1h 8m |
| IGO479 | IndiGo | Chennai International Airport (VOMM) | Coimbatore Air Force Station (VOSX) | 2026-09-24 04:32 UTC | 2026-09-24 05:04 UTC | 32m |
| CPA821 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Zhuhai Airport (ZGSD) | 2026-09-23 14:56 UTC | 2026-09-24 05:03 UTC | 14h 7m |
| CPA250 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-09-23 17:39 UTC | 2026-09-24 05:00 UTC | 11h 21m |
| VHJKM | VHJ | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-09-24 04:33 UTC | 2026-09-24 05:00 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
