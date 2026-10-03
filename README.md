# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_17:25:29_UTC-green)

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

**Latest saved flight:** 2026-10-03 17:25:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-10-03 17:25:29 UTC

- **275,470** saved flights
- **80,238** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **275,470** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,333,168.0 tonnes** estimated CO2 emissions
- **193,227,132 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10801 |
| 2 | SkyWest Airlines | 9579 |
| 3 | EJA | 5397 |
| 4 | IndiGo | 4594 |
| 5 | American Airlines | 4260 |
| 6 | Southwest Airlines | 4048 |
| 7 | Delta Air Lines | 3420 |
| 8 | ENY | 3222 |
| 9 | LATAM Airlines | 2668 |
| 10 | AZU | 2592 |
| 11 | Vueling | 2285 |
| 12 | WIF | 2242 |
| 13 | LXJ | 2178 |
| 14 | Lufthansa | 2073 |
| 15 | easyJet | 1830 |
| 16 | Swiss International | 1804 |
| 17 | QLK | 1775 |
| 18 | EJU | 1711 |
| 19 | AXM | 1689 |
| 20 | United Airlines | 1679 |
| 21 | Alaska Airlines | 1623 |
| 22 | All Nippon Airways | 1572 |
| 23 | PGT | 1550 |
| 24 | GLO | 1539 |
| 25 | WMT | 1533 |
| 26 | Air France | 1511 |
| 27 | VIV | 1511 |
| 28 | Wizz Air | 1489 |
| 29 | CXK | 1360 |
| 30 | AEE | 1310 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 229806 |
| 2 | 🇪🇸 ES | 17227 |
| 3 | 🇧🇷 BR | 16182 |
| 4 | 🇦🇺 AU | 15882 |
| 5 | 🇨🇦 CA | 15353 |
| 6 | 🇮🇹 IT | 14849 |
| 7 | 🇮🇳 IN | 14535 |
| 8 | 🇩🇪 DE | 13173 |
| 9 | 🇨🇴 CO | 12781 |
| 10 | 🇬🇧 GB | 12682 |
| 11 | 🇫🇷 FR | 10892 |
| 12 | 🇯🇵 JP | 10502 |
| 13 | 🇹🇷 TR | 8324 |
| 14 | 🇬🇷 GR | 7903 |
| 15 | 🇲🇽 MX | 7613 |
| 16 | 🇨🇭 CH | 7319 |
| 17 | 🇳🇴 NO | 6798 |
| 18 | 🇹🇭 TH | 4936 |
| 19 | 🇲🇾 MY | 4575 |
| 20 | 🇿🇦 ZA | 4562 |
| 21 | 🇵🇱 PL | 4501 |
| 22 | 🇳🇿 NZ | 3905 |
| 23 | 🇵🇭 PH | 3638 |
| 24 | 🇬🇹 GT | 3456 |
| 25 | 🇭🇷 HR | 3132 |
| 26 | 🇰🇷 KR | 3101 |
| 27 | 🇲🇦 MA | 2719 |
| 28 | 🇲🇪 ME | 2585 |
| 29 | 🇳🇱 NL | 2461 |
| 30 | 🇮🇩 ID | 2279 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5589 |
| 2 | Denver International Airport |  | US | 4494 |
| 3 | Indira Gandhi International Airport |  | IN | 3284 |
| 4 | Tokyo International Airport |  | JP | 3149 |
| 5 | El Dorado International Airport |  | CO | 3051 |
| 6 | Harry Reid International Airport |  | US | 2966 |
| 7 | Zurich Airport |  | CH | 2862 |
| 8 | Guaymaral Airport |  | CO | 2853 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2749 |
| 10 | La Aurora Airport |  | GT | 2628 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2628 |
| 12 | Salt Lake City International Airport |  | US | 2447 |
| 13 | Congonhas Airport |  | BR | 2355 |
| 14 | Chicago O'Hare International Airport |  | US | 2326 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2252 |
| 16 | Capua Airport |  | IT | 2139 |
| 17 | Madrid Barajas International Airport |  | ES | 2119 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2101 |
| 19 | Frankfurt am Main International Airport |  | DE | 2071 |
| 20 | Enrique Olaya Herrera Airport |  | CO | 1959 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1952 |
| 22 | Malpensa International Airport |  | IT | 1947 |
| 23 | Charles de Gaulle International Airport |  | FR | 1947 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1929 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1839 |
| 26 | Macau International Airport |  | MO | 1792 |
| 27 | Ninoy Aquino International Airport |  | PH | 1789 |
| 28 | Charlotte/Douglas International Airport |  | US | 1719 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1713 |
| 30 | Barcelona International Airport |  | ES | 1701 |
| 31 | Viracopos International Airport |  | BR | 1651 |
| 32 | Kuala Lumpur International Airport |  | MY | 1639 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1618 |
| 34 | Seattle-Tacoma International Airport |  | US | 1615 |
| 35 | Calgary International Airport |  | CA | 1564 |
| 36 | Don Mueang International Airport |  | TH | 1557 |
| 37 | Oslo Gardermoen Airport |  | NO | 1544 |
| 38 | Vancouver International Airport |  | CA | 1544 |
| 39 | Bengaluru International Airport |  | IN | 1541 |
| 40 | Reno/Tahoe International Airport |  | US | 1494 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1134 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1039 | 21m | 244 km | 4,374.9 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 767 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 696 | 1h 6m | 770 km | 9,245.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 694 | 24m | 225 km | 2,692.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 611 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 459 | 44m | 555 km | 4,395.1 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 443 | 27m | 275 km | 2,099.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 435 | 1h 50m | 1,423 km | 10,675.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 423 | 44m | 241 km | 1,757.1 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 393 | 24m | 218 km | 1,480.6 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 382 | 35m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 374 | 23m | 55 km | 355.5 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 370 | 21m | 250 km | 1,598.2 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 353 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 349 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 347 | 1h 6m | 706 km | 4,224.7 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 344 | 19m | 99 km | 589.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 342 | 26m | 215 km | 1,266.6 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 320 | 19m | 144 km | 796.0 t |
| 22 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 316 | 18m | 14 km | 79.0 t |
| 23 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 312 | 1h 14m | 961 km | 5,171.6 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 310 | 42m | 535 km | 2,863.1 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 298 | 1h 50m | 1,304 km | 6,704.2 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 274 | 51m | 556 km | 2,626.5 t |
| 30 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 273 | 44m | 431 km | 2,031.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N66717 |  | Essex County Airport (KCDW) | Somerset Airport (KSMQ) | 2026-10-03 16:42 UTC | 2026-10-03 17:25 UTC | 43m |
| N862PA |  | Manchester Boston Regional Airport (KMHT) | Bangor International Airport (KBGR) | 2026-10-03 16:22 UTC | 2026-10-03 17:22 UTC | 59m |
| N303RH |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Tracy Municipal Airport (KTCY) | 2026-10-03 16:44 UTC | 2026-10-03 17:18 UTC | 34m |
| LXJ446 | LXJ | Austin-Bergstrom International Airport (KAUS) | Austin-Bergstrom International Airport (KAUS) | 2026-10-03 16:50 UTC | 2026-10-03 17:17 UTC | 26m |
| AIC9DK | Air India | Trivandrum International Airport (VOTV) | Pune Airport (VAPO) | 2026-10-03 15:23 UTC | 2026-10-03 17:14 UTC | 1h 51m |
| SCU38 | SCU | Tulsa Riverside Airport (KRVS) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-10-03 16:40 UTC | 2026-10-03 17:08 UTC | 28m |
| LXJ428 | LXJ | Los Angeles International Airport (KLAX) | Van Nuys Airport (KVNY) | 2026-10-03 16:46 UTC | 2026-10-03 17:08 UTC | 21m |
| RCR7790 | RCR | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2026-10-03 06:01 UTC | 2026-10-03 16:59 UTC | 10h 58m |
| BYF31 | BYF | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-10-03 16:51 UTC | 2026-10-03 16:55 UTC | 4m |
| THY576 | Turkish Airlines | Istanbul Airport (LTFM) | Queen Alia International Airport (OJAI) | 2026-10-03 15:29 UTC | 2026-10-03 16:54 UTC | 1h 24m |
| N220CS |  | City Of Colorado Springs Municipal Airport (KCOS) | Telluride Regional Airport (KTEX) | 2026-10-03 13:56 UTC | 2026-10-03 16:53 UTC | 2h 57m |
| N403TD |  | Linden Airport (KLDJ) | Newark Liberty International Airport (KEWR) | 2026-10-03 13:46 UTC | 2026-10-03 16:53 UTC | 3h 7m |
| N8318Q |  | Quakertown Airport (KUKT) | Quakertown Airport (KUKT) | 2026-10-03 16:23 UTC | 2026-10-03 16:53 UTC | 29m |
| N5726B |  | Minden-Tahoe Airport (KMEV) | Minden-Tahoe Airport (KMEV) | 2026-10-03 16:41 UTC | 2026-10-03 16:53 UTC | 11m |
| N74CW |  | Skypark Airport (KBTF) | UT99 (UT99) | 2026-10-03 16:23 UTC | 2026-10-03 16:50 UTC | 26m |
| BZAZ0909 | BZA | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 2026-10-03 16:37 UTC | 2026-10-03 16:50 UTC | 12m |
| SAMU38 | SAM | Grenoble Le Versoud Airport (LFLG) | Grenoble Le Versoud Airport (LFLG) | 2026-10-03 16:48 UTC | 2026-10-03 16:50 UTC | 1m |
| N3558Y |  | San Luis Obispo County Regional Airport (KSBP) | Lompoc Airport (KLPC) | 2026-10-03 16:25 UTC | 2026-10-03 16:50 UTC | 24m |
| MAS127 | Malaysia Airlines | Kuala Lumpur International Airport (WMKK) | Perth International Airport (YPPH) | 2026-10-03 11:50 UTC | 2026-10-03 16:48 UTC | 4h 57m |
| N421RN |  | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-10-03 16:25 UTC | 2026-10-03 16:47 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
