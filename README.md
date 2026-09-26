# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_19:06:10_UTC-green)

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

**Latest saved flight:** 2026-09-26 19:06:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-26 19:06:10 UTC

- **270,347** saved flights
- **79,198** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **270,347** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,279,201.8 tonnes** estimated CO2 emissions
- **190,098,656 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10640 |
| 2 | SkyWest Airlines | 9406 |
| 3 | EJA | 5279 |
| 4 | IndiGo | 4525 |
| 5 | American Airlines | 4199 |
| 6 | Southwest Airlines | 3975 |
| 7 | Delta Air Lines | 3359 |
| 8 | ENY | 3176 |
| 9 | LATAM Airlines | 2602 |
| 10 | AZU | 2536 |
| 11 | Vueling | 2253 |
| 12 | WIF | 2198 |
| 13 | LXJ | 2123 |
| 14 | Lufthansa | 2053 |
| 15 | easyJet | 1812 |
| 16 | Swiss International | 1772 |
| 17 | QLK | 1738 |
| 18 | EJU | 1695 |
| 19 | AXM | 1674 |
| 20 | United Airlines | 1653 |
| 21 | Alaska Airlines | 1595 |
| 22 | All Nippon Airways | 1553 |
| 23 | PGT | 1523 |
| 24 | WMT | 1512 |
| 25 | GLO | 1507 |
| 26 | Air France | 1485 |
| 27 | VIV | 1475 |
| 28 | Wizz Air | 1470 |
| 29 | CXK | 1328 |
| 30 | AEE | 1296 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 225156 |
| 2 | 🇪🇸 ES | 16940 |
| 3 | 🇧🇷 BR | 15811 |
| 4 | 🇦🇺 AU | 15527 |
| 5 | 🇨🇦 CA | 15070 |
| 6 | 🇮🇹 IT | 14624 |
| 7 | 🇮🇳 IN | 14323 |
| 8 | 🇩🇪 DE | 12981 |
| 9 | 🇬🇧 GB | 12512 |
| 10 | 🇨🇴 CO | 12401 |
| 11 | 🇫🇷 FR | 10744 |
| 12 | 🇯🇵 JP | 10372 |
| 13 | 🇹🇷 TR | 8186 |
| 14 | 🇬🇷 GR | 7805 |
| 15 | 🇲🇽 MX | 7464 |
| 16 | 🇨🇭 CH | 7191 |
| 17 | 🇳🇴 NO | 6682 |
| 18 | 🇹🇭 TH | 4831 |
| 19 | 🇲🇾 MY | 4532 |
| 20 | 🇿🇦 ZA | 4516 |
| 21 | 🇵🇱 PL | 4429 |
| 22 | 🇳🇿 NZ | 3785 |
| 23 | 🇵🇭 PH | 3582 |
| 24 | 🇬🇹 GT | 3418 |
| 25 | 🇭🇷 HR | 3085 |
| 26 | 🇰🇷 KR | 3051 |
| 27 | 🇲🇦 MA | 2686 |
| 28 | 🇲🇪 ME | 2536 |
| 29 | 🇳🇱 NL | 2417 |
| 30 | 🇮🇩 ID | 2251 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5501 |
| 2 | Denver International Airport |  | US | 4398 |
| 3 | Indira Gandhi International Airport |  | IN | 3238 |
| 4 | Tokyo International Airport |  | JP | 3105 |
| 5 | El Dorado International Airport |  | CO | 2937 |
| 6 | Harry Reid International Airport |  | US | 2899 |
| 7 | Guaymaral Airport |  | CO | 2820 |
| 8 | Zurich Airport |  | CH | 2804 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2715 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2599 |
| 11 | La Aurora Airport |  | GT | 2598 |
| 12 | Salt Lake City International Airport |  | US | 2385 |
| 13 | Chicago O'Hare International Airport |  | US | 2307 |
| 14 | Congonhas Airport |  | BR | 2305 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2212 |
| 16 | Capua Airport |  | IT | 2094 |
| 17 | Madrid Barajas International Airport |  | ES | 2083 |
| 18 | Frankfurt am Main International Airport |  | DE | 2048 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2043 |
| 20 | Malpensa International Airport |  | IT | 1931 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1925 |
| 22 | Charles de Gaulle International Airport |  | FR | 1919 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1898 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1888 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1823 |
| 26 | Macau International Airport |  | MO | 1788 |
| 27 | Ninoy Aquino International Airport |  | PH | 1758 |
| 28 | Charlotte/Douglas International Airport |  | US | 1692 |
| 29 | Barcelona International Airport |  | ES | 1681 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1680 |
| 31 | Viracopos International Airport |  | BR | 1631 |
| 32 | Kuala Lumpur International Airport |  | MY | 1624 |
| 33 | Seattle-Tacoma International Airport |  | US | 1583 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1581 |
| 35 | Calgary International Airport |  | CA | 1540 |
| 36 | Don Mueang International Airport |  | TH | 1528 |
| 37 | Bengaluru International Airport |  | IN | 1523 |
| 38 | Oslo Gardermoen Airport |  | NO | 1515 |
| 39 | Vancouver International Airport |  | CA | 1511 |
| 40 | Antalya International Airport |  | TR | 1444 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1123 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1012 | 21m | 244 km | 4,261.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 747 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 682 | 1h 6m | 770 km | 9,059.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 676 | 24m | 225 km | 2,622.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 601 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 446 | 44m | 555 km | 4,270.7 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 435 | 27m | 275 km | 2,061.3 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 427 | 1h 50m | 1,423 km | 10,479.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 412 | 44m | 241 km | 1,711.4 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 387 | 24m | 218 km | 1,458.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 378 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 366 | 21m | 250 km | 1,580.9 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 364 | 23m | 55 km | 346.0 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 345 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 343 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 341 | 1h 6m | 706 km | 4,151.7 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 340 | 19m | 99 km | 582.4 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 336 | 26m | 215 km | 1,244.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 314 | 19m | 144 km | 781.1 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 305 | 1h 14m | 961 km | 5,055.5 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 298 | 42m | 535 km | 2,752.2 t |
| 26 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 294 | 18m | 14 km | 73.5 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 291 | 1h 50m | 1,304 km | 6,546.8 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 272 | 15m | 154 km | 720.7 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N26BQ |  | Dupage Airport (KDPA) | Morris Municipal/James R Washburn Field (KC09) | 2026-09-26 18:47 UTC | 2026-09-26 19:06 UTC | 18m |
| THY8CD | Turkish Airlines | Antalya International Airport (LTAI) | LZSY (LZSY) | 2026-09-26 16:51 UTC | 2026-09-26 19:03 UTC | 2h 11m |
| N92DV |  | Vance Brand Airport (KLMO) | Vance Brand Airport (KLMO) | 2026-09-26 17:18 UTC | 2026-09-26 19:03 UTC | 1h 44m |
| N10BB |  | Chester Catawba Regional Airport (KDCM) | Chester Catawba Regional Airport (KDCM) | 2026-09-26 18:34 UTC | 2026-09-26 18:59 UTC | 25m |
| N351SA |  | Ted Stevens Anchorage International Airport (PANC) | Merle K (Mudhole) Smith Airport (PACV) | 2026-09-26 17:13 UTC | 2026-09-26 18:58 UTC | 1h 44m |
| UPS104 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Ted Stevens Anchorage International Airport (PANC) | 2026-09-26 12:46 UTC | 2026-09-26 18:55 UTC | 6h 8m |
| N172FK |  | Whiteman Airport (KWHP) | Whiteman Airport (KWHP) | 2026-09-26 18:34 UTC | 2026-09-26 18:54 UTC | 20m |
| CXK416 | CXK | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-09-26 17:33 UTC | 2026-09-26 18:54 UTC | 1h 21m |
| N39AS |  | KA09 (KA09) | Lake Havasu City Airport (KHII) | 2026-09-26 18:36 UTC | 2026-09-26 18:51 UTC | 15m |
| N739MR |  | Aurora State Airport (KUAO) | Aurora State Airport (KUAO) | 2026-09-26 17:48 UTC | 2026-09-26 18:48 UTC | 1h 0m |
| WNG7HB | WNG | Denton Enterprise Airport (KDTO) | Felton Field (4XS2) | 2026-09-26 18:27 UTC | 2026-09-26 18:48 UTC | 20m |
| N7163G |  | Southwest Washington Regional Airport (KKLS) | Michair Airport (WT44) | 2026-09-26 18:37 UTC | 2026-09-26 18:47 UTC | 10m |
| N9411T |  | Georgetown Executive Airport (KGTU) | Georgetown Executive Airport (KGTU) | 2026-09-26 18:27 UTC | 2026-09-26 18:46 UTC | 19m |
| N811BL |  | Winter Haven Regional Airport (KGIF) | Winter Haven Regional Airport (KGIF) | 2026-09-26 17:58 UTC | 2026-09-26 18:46 UTC | 48m |
| N911LK |  | Miami Homestead General Aviation Airport (KX51) | Miami Executive Airport (KTMB) | 2026-09-26 18:31 UTC | 2026-09-26 18:43 UTC | 11m |
| N13HN |  | Dubuque Regional Airport (KDBQ) | Dubuque Regional Airport (KDBQ) | 2026-09-26 18:17 UTC | 2026-09-26 18:42 UTC | 24m |
| N555BG |  | Centennial Airport (KAPA) | Telluride Regional Airport (KTEX) | 2026-09-26 18:00 UTC | 2026-09-26 18:41 UTC | 40m |
| N843FF |  | Farnborough Airport (EGLF) | Perugia / San Egidio Airport (LIRZ) | 2026-09-26 16:52 UTC | 2026-09-26 18:41 UTC | 1h 49m |
| AAL2122 | American Airlines | Phoenix Sky Harbor International Airport (KPHX) | San Diego International Airport (KSAN) | 2026-09-26 17:51 UTC | 2026-09-26 18:41 UTC | 49m |
| N452DD |  | Portland-Troutdale Airport (KTTD) | Quincy Flying Service Airport (WA74) | 2026-09-26 16:57 UTC | 2026-09-26 18:40 UTC | 1h 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
