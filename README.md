# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--05_05:14:47_UTC-green)

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

**Latest saved flight:** 2026-10-05 05:14:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-10-05 05:14:47 UTC

- **276,709** saved flights
- **80,490** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **276,709** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,351,244.4 tonnes** estimated CO2 emissions
- **194,275,037 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10847 |
| 2 | SkyWest Airlines | 9618 |
| 3 | EJA | 5428 |
| 4 | IndiGo | 4616 |
| 5 | American Airlines | 4280 |
| 6 | Southwest Airlines | 4063 |
| 7 | Delta Air Lines | 3441 |
| 8 | ENY | 3229 |
| 9 | LATAM Airlines | 2681 |
| 10 | AZU | 2603 |
| 11 | Vueling | 2290 |
| 12 | WIF | 2252 |
| 13 | LXJ | 2191 |
| 14 | Lufthansa | 2077 |
| 15 | easyJet | 1834 |
| 16 | Swiss International | 1806 |
| 17 | QLK | 1785 |
| 18 | EJU | 1720 |
| 19 | AXM | 1695 |
| 20 | United Airlines | 1684 |
| 21 | Alaska Airlines | 1632 |
| 22 | All Nippon Airways | 1581 |
| 23 | PGT | 1557 |
| 24 | GLO | 1544 |
| 25 | WMT | 1536 |
| 26 | Air France | 1522 |
| 27 | VIV | 1517 |
| 28 | Wizz Air | 1498 |
| 29 | CXK | 1366 |
| 30 | AEE | 1315 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 230911 |
| 2 | 🇪🇸 ES | 17294 |
| 3 | 🇧🇷 BR | 16253 |
| 4 | 🇦🇺 AU | 15975 |
| 5 | 🇨🇦 CA | 15410 |
| 6 | 🇮🇹 IT | 14922 |
| 7 | 🇮🇳 IN | 14603 |
| 8 | 🇩🇪 DE | 13204 |
| 9 | 🇨🇴 CO | 12852 |
| 10 | 🇬🇧 GB | 12736 |
| 11 | 🇫🇷 FR | 10930 |
| 12 | 🇯🇵 JP | 10538 |
| 13 | 🇹🇷 TR | 8353 |
| 14 | 🇬🇷 GR | 7928 |
| 15 | 🇲🇽 MX | 7645 |
| 16 | 🇨🇭 CH | 7338 |
| 17 | 🇳🇴 NO | 6822 |
| 18 | 🇹🇭 TH | 4967 |
| 19 | 🇲🇾 MY | 4591 |
| 20 | 🇿🇦 ZA | 4576 |
| 21 | 🇵🇱 PL | 4521 |
| 22 | 🇳🇿 NZ | 3944 |
| 23 | 🇵🇭 PH | 3666 |
| 24 | 🇬🇹 GT | 3467 |
| 25 | 🇭🇷 HR | 3143 |
| 26 | 🇰🇷 KR | 3110 |
| 27 | 🇲🇦 MA | 2730 |
| 28 | 🇲🇪 ME | 2594 |
| 29 | 🇳🇱 NL | 2466 |
| 30 | 🇮🇩 ID | 2286 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5607 |
| 2 | Denver International Airport |  | US | 4513 |
| 3 | Indira Gandhi International Airport |  | IN | 3297 |
| 4 | Tokyo International Airport |  | JP | 3160 |
| 5 | El Dorado International Airport |  | CO | 3080 |
| 6 | Harry Reid International Airport |  | US | 2982 |
| 7 | Zurich Airport |  | CH | 2869 |
| 8 | Guaymaral Airport |  | CO | 2855 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2765 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2639 |
| 11 | La Aurora Airport |  | GT | 2637 |
| 12 | Salt Lake City International Airport |  | US | 2463 |
| 13 | Congonhas Airport |  | BR | 2365 |
| 14 | Chicago O'Hare International Airport |  | US | 2330 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2270 |
| 16 | Capua Airport |  | IT | 2152 |
| 17 | Madrid Barajas International Airport |  | ES | 2132 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2112 |
| 19 | Frankfurt am Main International Airport |  | DE | 2078 |
| 20 | Charles de Gaulle International Airport |  | FR | 1962 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1961 |
| 22 | Enrique Olaya Herrera Airport |  | CO | 1959 |
| 23 | Malpensa International Airport |  | IT | 1953 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1937 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1844 |
| 26 | Macau International Airport |  | MO | 1806 |
| 27 | Ninoy Aquino International Airport |  | PH | 1804 |
| 28 | Charlotte/Douglas International Airport |  | US | 1725 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1721 |
| 30 | Barcelona International Airport |  | ES | 1704 |
| 31 | Viracopos International Airport |  | BR | 1658 |
| 32 | Kuala Lumpur International Airport |  | MY | 1647 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1630 |
| 34 | Seattle-Tacoma International Airport |  | US | 1627 |
| 35 | Calgary International Airport |  | CA | 1572 |
| 36 | Don Mueang International Airport |  | TH | 1565 |
| 37 | Oslo Gardermoen Airport |  | NO | 1550 |
| 38 | Vancouver International Airport |  | CA | 1549 |
| 39 | Bengaluru International Airport |  | IN | 1543 |
| 40 | Reno/Tahoe International Airport |  | US | 1505 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1134 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1044 | 21m | 244 km | 4,396.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 767 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 703 | 24m | 225 km | 2,727.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 699 | 1h 6m | 770 km | 9,285.7 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 614 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 464 | 44m | 555 km | 4,443.0 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 444 | 27m | 275 km | 2,103.9 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 439 | 1h 50m | 1,423 km | 10,773.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 425 | 44m | 241 km | 1,765.4 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 395 | 24m | 218 km | 1,488.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 382 | 35m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 375 | 23m | 55 km | 356.4 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 371 | 21m | 250 km | 1,602.5 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 357 | 12m | - | - |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 354 | 13m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 348 | 1h 6m | 706 km | 4,236.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 344 | 19m | 99 km | 589.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 343 | 26m | 215 km | 1,270.3 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 338 | 1h 39m | 1,156 km | 6,743.0 t |
| 21 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 324 | 19m | 14 km | 81.0 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 322 | 19m | 144 km | 801.0 t |
| 23 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 312 | 42m | 535 km | 2,881.5 t |
| 24 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 312 | 1h 14m | 961 km | 5,171.6 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 298 | 1h 50m | 1,304 km | 6,704.2 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 287 | 28m | 152 km | 750.0 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 276 | 44m | 431 km | 2,053.9 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 275 | 51m | 556 km | 2,636.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BAW199 | British Airways | London Heathrow Airport (EGLL) | Chhatrapati Shivaji International Airport (VABB) | 2026-10-04 20:45 UTC | 2026-10-05 05:14 UTC | 8h 29m |
| AXB2KM | AXB | Aurangabad Airport (VAAU) | Chhatrapati Shivaji International Airport (VABB) | 2026-10-05 04:46 UTC | 2026-10-05 05:12 UTC | 25m |
| SD1 |  | Napa County Airport (KAPC) | Palo Alto Airport (KPAO) | 2026-10-05 04:33 UTC | 2026-10-05 05:01 UTC | 27m |
| A7GAA |  | Doha International Airport (OTBD) | Das Island Airport (OMAS) | 2026-10-05 04:34 UTC | 2026-10-05 05:00 UTC | 25m |
| EVA062 | EVA Air | Suvarnabhumi Airport (VTBS) | Hsinchu Air Base (RCPO) | 2026-10-05 01:47 UTC | 2026-10-05 05:00 UTC | 3h 12m |
| TWB687 | TWB | Daegu Airport (RKTN) | Taiwan Taoyuan International Airport (RCTP) | 2026-10-05 01:22 UTC | 2026-10-05 04:57 UTC | 3h 34m |
| IGO675 | IndiGo | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 2026-10-05 03:23 UTC | 2026-10-05 04:50 UTC | 1h 27m |
| ANE002 | ANE | Madrid Barajas International Airport (LEMD) | La Morgal Airport (LEMR) | 2026-10-05 04:15 UTC | 2026-10-05 04:46 UTC | 31m |
| WSK153 | WSK | Perth International Airport (YPPH) | Kondinin Airport (YKDN) | 2026-10-05 04:05 UTC | 2026-10-05 04:42 UTC | 37m |
| AM322 |  | Melbourne Essendon Airport (YMEN) | Albury Airport (YMAY) | 2026-10-05 03:57 UTC | 2026-10-05 04:41 UTC | 43m |
| AM261 |  | Sydney Kingsford Smith International Airport (YSSY) | Tumut Airport (YTMU) | 2026-10-05 04:06 UTC | 2026-10-05 04:40 UTC | 34m |
| RYR824 | Ryanair | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Capua Airport (LIAU) | 2026-10-05 03:53 UTC | 2026-10-05 04:35 UTC | 42m |
| SWA2389 | Southwest Airlines | Harry Reid International Airport (KLAS) | NV13 (NV13) | 2026-10-05 03:45 UTC | 2026-10-05 04:34 UTC | 48m |
| ANE001 | ANE | Madrid Barajas International Airport (LEMD) | Federico Garcia Lorca Airport (LEGR) | 2026-10-05 03:52 UTC | 2026-10-05 04:33 UTC | 41m |
| ZKNYZ | ZKN | Tekapo Aerodrome (NZTL) | Pudding Hill Aerodrome (NZPH) | 2026-10-05 04:01 UTC | 2026-10-05 04:32 UTC | 31m |
| 5YSLQ |  | Nairobi Wilson Airport (HKNW) | Amboseli Airport (HKAM) | 2026-10-05 04:12 UTC | 2026-10-05 04:30 UTC | 18m |
| RYR11EX | Ryanair | Eleftherios Venizelos International Airport (LGAV) | Kasteli Airport (LGTL) | 2026-10-05 04:09 UTC | 2026-10-05 04:29 UTC | 19m |
| WIF7GT | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-10-05 04:14 UTC | 2026-10-05 04:26 UTC | 12m |
| RYR3074 | Ryanair | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Bari / Palese International Airport (LIBD) | 2026-10-05 03:51 UTC | 2026-10-05 04:23 UTC | 32m |
| RYR8QW | Ryanair | Catania / Fontanarossa Airport (LICC) | Salerno / Pontecagnano Airport (LIRI) | 2026-10-05 03:50 UTC | 2026-10-05 04:21 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
