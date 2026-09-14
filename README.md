# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--14_06:52:48_UTC-green)

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

**Latest saved flight:** 2026-09-14 06:52:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-14 06:52:48 UTC

- **258,208** saved flights
- **76,790** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **258,208** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,126,390.5 tonnes** estimated CO2 emissions
- **181,240,030 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10253 |
| 2 | SkyWest Airlines | 8996 |
| 3 | EJA | 5005 |
| 4 | IndiGo | 4336 |
| 5 | American Airlines | 4080 |
| 6 | Southwest Airlines | 3801 |
| 7 | Delta Air Lines | 3232 |
| 8 | ENY | 3061 |
| 9 | LATAM Airlines | 2484 |
| 10 | AZU | 2415 |
| 11 | Vueling | 2185 |
| 12 | WIF | 2071 |
| 13 | Lufthansa | 2018 |
| 14 | LXJ | 2018 |
| 15 | easyJet | 1761 |
| 16 | Swiss International | 1726 |
| 17 | QLK | 1666 |
| 18 | AXM | 1647 |
| 19 | EJU | 1639 |
| 20 | United Airlines | 1596 |
| 21 | Alaska Airlines | 1533 |
| 22 | All Nippon Airways | 1498 |
| 23 | WMT | 1458 |
| 24 | GLO | 1439 |
| 25 | PGT | 1435 |
| 26 | VIV | 1411 |
| 27 | Air France | 1410 |
| 28 | Wizz Air | 1405 |
| 29 | JetBlue | 1249 |
| 30 | AEE | 1248 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 214346 |
| 2 | 🇪🇸 ES | 16378 |
| 3 | 🇧🇷 BR | 15085 |
| 4 | 🇦🇺 AU | 14730 |
| 5 | 🇨🇦 CA | 14373 |
| 6 | 🇮🇹 IT | 14075 |
| 7 | 🇮🇳 IN | 13619 |
| 8 | 🇩🇪 DE | 12569 |
| 9 | 🇬🇧 GB | 12032 |
| 10 | 🇨🇴 CO | 11583 |
| 11 | 🇫🇷 FR | 10371 |
| 12 | 🇯🇵 JP | 10067 |
| 13 | 🇹🇷 TR | 7772 |
| 14 | 🇬🇷 GR | 7522 |
| 15 | 🇲🇽 MX | 7118 |
| 16 | 🇨🇭 CH | 6925 |
| 17 | 🇳🇴 NO | 6377 |
| 18 | 🇹🇭 TH | 4645 |
| 19 | 🇲🇾 MY | 4432 |
| 20 | 🇿🇦 ZA | 4390 |
| 21 | 🇵🇱 PL | 4276 |
| 22 | 🇳🇿 NZ | 3571 |
| 23 | 🇵🇭 PH | 3473 |
| 24 | 🇬🇹 GT | 3263 |
| 25 | 🇭🇷 HR | 2963 |
| 26 | 🇰🇷 KR | 2955 |
| 27 | 🇲🇦 MA | 2592 |
| 28 | 🇲🇪 ME | 2428 |
| 29 | 🇳🇱 NL | 2322 |
| 30 | 🇮🇩 ID | 2193 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5296 |
| 2 | Denver International Airport |  | US | 4176 |
| 3 | Indira Gandhi International Airport |  | IN | 3119 |
| 4 | Tokyo International Airport |  | JP | 3003 |
| 5 | Guaymaral Airport |  | CO | 2764 |
| 6 | Harry Reid International Airport |  | US | 2739 |
| 7 | Zurich Airport |  | CH | 2707 |
| 8 | El Dorado International Airport |  | CO | 2696 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2603 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2520 |
| 11 | La Aurora Airport |  | GT | 2479 |
| 12 | Salt Lake City International Airport |  | US | 2276 |
| 13 | Chicago O'Hare International Airport |  | US | 2246 |
| 14 | Congonhas Airport |  | BR | 2212 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2112 |
| 16 | Capua Airport |  | IT | 2024 |
| 17 | Madrid Barajas International Airport |  | ES | 2013 |
| 18 | Frankfurt am Main International Airport |  | DE | 1990 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1939 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1863 |
| 21 | Malpensa International Airport |  | IT | 1858 |
| 22 | Charles de Gaulle International Airport |  | FR | 1819 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1818 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1786 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1751 |
| 26 | Macau International Airport |  | MO | 1712 |
| 27 | Ninoy Aquino International Airport |  | PH | 1701 |
| 28 | Barcelona International Airport |  | ES | 1623 |
| 29 | Charlotte/Douglas International Airport |  | US | 1616 |
| 30 | Kuala Lumpur International Airport |  | MY | 1594 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1583 |
| 32 | Viracopos International Airport |  | BR | 1554 |
| 33 | Seattle-Tacoma International Airport |  | US | 1516 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1507 |
| 35 | Don Mueang International Airport |  | TH | 1485 |
| 36 | Calgary International Airport |  | CA | 1477 |
| 37 | Bengaluru International Airport |  | IN | 1468 |
| 38 | Oslo Gardermoen Airport |  | NO | 1455 |
| 39 | Vancouver International Airport |  | CA | 1448 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1391 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 962 | 21m | 244 km | 4,050.7 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 695 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 648 | 1h 6m | 770 km | 8,608.2 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 646 | 24m | 225 km | 2,506.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 577 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 419 | 27m | 275 km | 1,985.5 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 419 | 44m | 555 km | 4,012.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 411 | 1h 50m | 1,423 km | 10,086.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 390 | 44m | 241 km | 1,620.0 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 362 | 24m | 218 km | 1,363.8 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 356 | 21m | 250 km | 1,537.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 343 | 23m | 55 km | 326.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 326 | 1h 6m | 706 km | 3,969.1 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 320 | 26m | 215 km | 1,185.1 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 320 | 19m | 99 km | 548.1 t |
| 19 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 315 | 12m | - | - |
| 20 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 308 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 299 | 19m | 144 km | 743.7 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 297 | 1h 14m | 961 km | 4,922.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 276 | 1h 50m | 1,304 km | 6,209.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 274 | 42m | 535 km | 2,530.6 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 270 | 28m | 152 km | 705.6 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BAW31 | British Airways | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-09-13 19:00 UTC | 2026-09-14 06:52 UTC | 11h 52m |
| GNS06 | GNS | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-09-14 06:33 UTC | 2026-09-14 06:51 UTC | 17m |
| CIL | CIL | Sunshine Coast Airport (YBMC) | Toowoomba Airport (YTWB) | 2026-09-14 06:04 UTC | 2026-09-14 06:46 UTC | 41m |
| N911FK |  | Miami Homestead General Aviation Airport (KX51) | Miami Executive Airport (KTMB) | 2026-09-14 06:32 UTC | 2026-09-14 06:45 UTC | 12m |
| JUST71 | JUS | Holsworthy (Military) Airport (YSHW) | Holsworthy (Military) Airport (YSHW) | 2026-09-14 04:55 UTC | 2026-09-14 06:31 UTC | 1h 35m |
| AIC44K | Air India | Newark Liberty International Airport (KEWR) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-13 15:55 UTC | 2026-09-14 06:30 UTC | 14h 35m |
| CWA935 | CWA | Edmonton International Airport (CYEG) | Glendon Airport (CFP5) | 2026-09-14 05:55 UTC | 2026-09-14 06:19 UTC | 24m |
| N1065B |  | Anderson Regional Airport (KAND) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-09-14 05:43 UTC | 2026-09-14 06:19 UTC | 35m |
| CDG | CDG | Brisbane Archerfield Airport (YBAF) | Mudgee Airport (YMDG) | 2026-09-14 04:43 UTC | 2026-09-14 06:18 UTC | 1h 35m |
| IGO5151 | IndiGo | Jamnagar Airport (VAJM) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-14 05:34 UTC | 2026-09-14 06:17 UTC | 42m |
| VQBQV | VQB | Seletar Airport (WSSL) | Jendarata Airport (WMAJ) | 2026-09-14 05:32 UTC | 2026-09-14 06:13 UTC | 40m |
| WIF5DB | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-09-14 05:46 UTC | 2026-09-14 06:10 UTC | 24m |
| GNS110 | GNS | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-09-14 05:32 UTC | 2026-09-14 06:07 UTC | 35m |
| VAA010 | VAA | Mukhrani Airport (UGMM) | UGMS (UGMS) | 2026-09-14 05:33 UTC | 2026-09-14 06:06 UTC | 33m |
| DLH8HW | Lufthansa | Munich International Airport (EDDM) | Munster Osnabruck Airport (EDDG) | 2026-09-14 05:08 UTC | 2026-09-14 06:03 UTC | 55m |
| SLNG | SLN | RAAF Base Pearce (YPEA) | RAAF Gingin (YGIG) | 2026-09-14 05:34 UTC | 2026-09-14 06:02 UTC | 27m |
| SHA943 | SHA | Tribhuvan International Airport (VNKT) | Bhojpur Airport (VNBJ) | 2026-09-14 05:45 UTC | 2026-09-14 06:02 UTC | 16m |
| IGO491 | IndiGo | Agartala Airport (VEAT) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-09-14 05:25 UTC | 2026-09-14 06:01 UTC | 35m |
| N917SH |  | Joe Foss Field (KFSD) | Drake Farm Airport (1SD5) | 2026-09-14 05:32 UTC | 2026-09-14 05:56 UTC | 24m |
| IGO17FP | IndiGo | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 2026-09-14 04:48 UTC | 2026-09-14 05:56 UTC | 1h 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
