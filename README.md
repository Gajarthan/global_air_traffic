# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--07_05:34:09_UTC-green)

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

**Latest saved flight:** 2026-09-07 05:34:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-07 05:34:09 UTC

- **250,258** saved flights
- **75,159** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **250,258** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,013,218.2 tonnes** estimated CO2 emissions
- **174,679,318 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10019 |
| 2 | SkyWest Airlines | 8737 |
| 3 | EJA | 4832 |
| 4 | IndiGo | 4182 |
| 5 | American Airlines | 4004 |
| 6 | Southwest Airlines | 3718 |
| 7 | Delta Air Lines | 3171 |
| 8 | ENY | 2995 |
| 9 | LATAM Airlines | 2416 |
| 10 | AZU | 2329 |
| 11 | Vueling | 2135 |
| 12 | WIF | 1999 |
| 13 | Lufthansa | 1983 |
| 14 | LXJ | 1940 |
| 15 | easyJet | 1724 |
| 16 | Swiss International | 1680 |
| 17 | AXM | 1628 |
| 18 | EJU | 1609 |
| 19 | QLK | 1609 |
| 20 | United Airlines | 1568 |
| 21 | Alaska Airlines | 1496 |
| 22 | All Nippon Airways | 1467 |
| 23 | WMT | 1420 |
| 24 | GLO | 1392 |
| 25 | PGT | 1375 |
| 26 | VIV | 1372 |
| 27 | Wizz Air | 1362 |
| 28 | Air France | 1361 |
| 29 | AEE | 1229 |
| 30 | JetBlue | 1227 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 207520 |
| 2 | 🇪🇸 ES | 16001 |
| 3 | 🇧🇷 BR | 14612 |
| 4 | 🇦🇺 AU | 14230 |
| 5 | 🇨🇦 CA | 13906 |
| 6 | 🇮🇹 IT | 13709 |
| 7 | 🇮🇳 IN | 13052 |
| 8 | 🇩🇪 DE | 12300 |
| 9 | 🇬🇧 GB | 11736 |
| 10 | 🇨🇴 CO | 10990 |
| 11 | 🇫🇷 FR | 10079 |
| 12 | 🇯🇵 JP | 9872 |
| 13 | 🇹🇷 TR | 7470 |
| 14 | 🇬🇷 GR | 7363 |
| 15 | 🇲🇽 MX | 6915 |
| 16 | 🇨🇭 CH | 6744 |
| 17 | 🇳🇴 NO | 6191 |
| 18 | 🇹🇭 TH | 4508 |
| 19 | 🇲🇾 MY | 4370 |
| 20 | 🇿🇦 ZA | 4307 |
| 21 | 🇵🇱 PL | 4180 |
| 22 | 🇳🇿 NZ | 3423 |
| 23 | 🇵🇭 PH | 3403 |
| 24 | 🇬🇹 GT | 3133 |
| 25 | 🇰🇷 KR | 2898 |
| 26 | 🇭🇷 HR | 2875 |
| 27 | 🇲🇦 MA | 2531 |
| 28 | 🇲🇪 ME | 2352 |
| 29 | 🇳🇱 NL | 2261 |
| 30 | 🇮🇩 ID | 2147 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5168 |
| 2 | Denver International Airport |  | US | 4045 |
| 3 | Indira Gandhi International Airport |  | IN | 3042 |
| 4 | Tokyo International Airport |  | JP | 2946 |
| 5 | Guaymaral Airport |  | CO | 2737 |
| 6 | Harry Reid International Airport |  | US | 2662 |
| 7 | Zurich Airport |  | CH | 2618 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2540 |
| 9 | El Dorado International Airport |  | CO | 2534 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2480 |
| 11 | La Aurora Airport |  | GT | 2389 |
| 12 | Salt Lake City International Airport |  | US | 2213 |
| 13 | Chicago O'Hare International Airport |  | US | 2185 |
| 14 | Congonhas Airport |  | BR | 2146 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2058 |
| 16 | Capua Airport |  | IT | 1972 |
| 17 | Madrid Barajas International Airport |  | ES | 1966 |
| 18 | Frankfurt am Main International Airport |  | DE | 1952 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1880 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1823 |
| 21 | Malpensa International Airport |  | IT | 1802 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1759 |
| 23 | Charles de Gaulle International Airport |  | FR | 1752 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1745 |
| 25 | Ninoy Aquino International Airport |  | PH | 1660 |
| 26 | Macau International Airport |  | MO | 1648 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1639 |
| 28 | Charlotte/Douglas International Airport |  | US | 1585 |
| 29 | Barcelona International Airport |  | ES | 1583 |
| 30 | Kuala Lumpur International Airport |  | MY | 1573 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1533 |
| 32 | Viracopos International Airport |  | BR | 1496 |
| 33 | Seattle-Tacoma International Airport |  | US | 1474 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1452 |
| 35 | Don Mueang International Airport |  | TH | 1444 |
| 36 | Calgary International Airport |  | CA | 1440 |
| 37 | Bengaluru International Airport |  | IN | 1433 |
| 38 | Oslo Gardermoen Airport |  | NO | 1409 |
| 39 | Vancouver International Airport |  | CA | 1400 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1358 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 930 | 21m | 244 km | 3,916.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 657 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 635 | 24m | 225 km | 2,463.5 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 629 | 1h 6m | 770 km | 8,355.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 563 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 410 | 27m | 275 km | 1,942.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 399 | 1h 50m | 1,423 km | 9,792.1 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 390 | 44m | 555 km | 3,734.4 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 371 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 371 | 44m | 241 km | 1,541.1 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 352 | 21m | 250 km | 1,520.4 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 349 | 24m | 218 km | 1,314.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 334 | 23m | 55 km | 317.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 309 | 26m | 215 km | 1,144.4 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 300 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 290 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 289 | 1h 14m | 961 km | 4,790.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 287 | 19m | 144 km | 713.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 270 | 1h 50m | 1,304 km | 6,074.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 257 | 41m | 535 km | 2,373.6 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 257 | 28m | 152 km | 671.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LAE1525 | LAE | Miami International Airport (KMIA) | El Dorado International Airport (SKBO) | 2026-09-07 02:27 UTC | 2026-09-07 05:34 UTC | 3h 6m |
| SXAQU | SXA | Dimokritos Airport (LGAL) | Limnos Airport (LGLM) | 2026-09-07 04:17 UTC | 2026-09-07 05:31 UTC | 1h 13m |
| N447DB |  | Daniel K Inouye International Airport (PHNL) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-09-07 04:44 UTC | 2026-09-07 05:28 UTC | 43m |
| N1115M |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-09-07 05:00 UTC | 2026-09-07 05:23 UTC | 23m |
| AIC9TT | Air India | Chennai International Airport (VOMM) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-07 03:56 UTC | 2026-09-07 05:19 UTC | 1h 23m |
| N929TG |  | Beluga Airport (PABG) | Ted Stevens Anchorage International Airport (PANC) | 2026-09-07 04:52 UTC | 2026-09-07 05:11 UTC | 19m |
| WZZ3860 | Wizz Air | Heydar Aliyev International Airport (UBBB) | UKFB (UKFB) | 2026-09-07 02:31 UTC | 2026-09-07 05:00 UTC | 2h 29m |
| IGO627 | IndiGo | Trivandrum International Airport (VOTV) | Pune Airport (VAPO) | 2026-09-07 03:15 UTC | 2026-09-07 04:56 UTC | 1h 40m |
| HUF865 | HUF | Kecskemet Airport (LHKE) | Hamburg Airport (EDDH) | 2026-09-07 02:59 UTC | 2026-09-07 04:54 UTC | 1h 55m |
| BAW199 | British Airways | London Heathrow Airport (EGLL) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-06 20:43 UTC | 2026-09-07 04:53 UTC | 8h 10m |
| WZZ37KJ | Wizz Air | Gdańsk Lech Wałęsa Airport (EPGD) | Stockholm-Arlanda Airport (ESSA) | 2026-09-07 03:51 UTC | 2026-09-07 04:52 UTC | 1h 0m |
| RYR4FL | Ryanair | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Bari / Palese International Airport (LIBD) | 2026-09-07 04:14 UTC | 2026-09-07 04:48 UTC | 34m |
| WMT5843 | WMT | Henri Coanda International Airport (LROP) | Mikonos Airport (LGMK) | 2026-09-07 03:29 UTC | 2026-09-07 04:46 UTC | 1h 17m |
| TRP2 | TRP | Finagin Airfield (MD05) | Joint Base Andrews Airport (KADW) | 2026-09-07 04:29 UTC | 2026-09-07 04:43 UTC | 13m |
| RYR824 | Ryanair | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Capua Airport (LIAU) | 2026-09-07 04:00 UTC | 2026-09-07 04:42 UTC | 42m |
| WI7GT |  | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-09-07 04:25 UTC | 2026-09-07 04:40 UTC | 14m |
| NMU | NMU | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-09-07 04:22 UTC | 2026-09-07 04:38 UTC | 15m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-09-07 04:28 UTC | 2026-09-07 04:38 UTC | 10m |
| IGO5215 | IndiGo | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 2026-09-07 02:40 UTC | 2026-09-07 04:32 UTC | 1h 51m |
| THY2TF | Turkish Airlines | Istanbul Airport (LTFM) | Antalya International Airport (LTAI) | 2026-09-07 03:41 UTC | 2026-09-07 04:32 UTC | 51m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
