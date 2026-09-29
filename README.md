# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_12:15:13_UTC-green)

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

**Latest saved flight:** 2026-09-29 12:15:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-29 12:15:13 UTC

- **272,232** saved flights
- **79,594** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **272,232** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,299,316.0 tonnes** estimated CO2 emissions
- **191,264,696 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10703 |
| 2 | SkyWest Airlines | 9484 |
| 3 | EJA | 5331 |
| 4 | IndiGo | 4548 |
| 5 | American Airlines | 4226 |
| 6 | Southwest Airlines | 4007 |
| 7 | Delta Air Lines | 3385 |
| 8 | ENY | 3195 |
| 9 | LATAM Airlines | 2626 |
| 10 | AZU | 2558 |
| 11 | Vueling | 2265 |
| 12 | WIF | 2217 |
| 13 | LXJ | 2145 |
| 14 | Lufthansa | 2060 |
| 15 | easyJet | 1818 |
| 16 | Swiss International | 1781 |
| 17 | QLK | 1755 |
| 18 | EJU | 1700 |
| 19 | AXM | 1679 |
| 20 | United Airlines | 1664 |
| 21 | Alaska Airlines | 1605 |
| 22 | All Nippon Airways | 1561 |
| 23 | PGT | 1538 |
| 24 | GLO | 1520 |
| 25 | WMT | 1516 |
| 26 | Air France | 1495 |
| 27 | VIV | 1493 |
| 28 | Wizz Air | 1478 |
| 29 | CXK | 1343 |
| 30 | AEE | 1304 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 226858 |
| 2 | 🇪🇸 ES | 17042 |
| 3 | 🇧🇷 BR | 15973 |
| 4 | 🇦🇺 AU | 15686 |
| 5 | 🇨🇦 CA | 15167 |
| 6 | 🇮🇹 IT | 14699 |
| 7 | 🇮🇳 IN | 14393 |
| 8 | 🇩🇪 DE | 13045 |
| 9 | 🇬🇧 GB | 12577 |
| 10 | 🇨🇴 CO | 12528 |
| 11 | 🇫🇷 FR | 10808 |
| 12 | 🇯🇵 JP | 10420 |
| 13 | 🇹🇷 TR | 8254 |
| 14 | 🇬🇷 GR | 7849 |
| 15 | 🇲🇽 MX | 7522 |
| 16 | 🇨🇭 CH | 7235 |
| 17 | 🇳🇴 NO | 6725 |
| 18 | 🇹🇭 TH | 4879 |
| 19 | 🇲🇾 MY | 4549 |
| 20 | 🇿🇦 ZA | 4530 |
| 21 | 🇵🇱 PL | 4461 |
| 22 | 🇳🇿 NZ | 3833 |
| 23 | 🇵🇭 PH | 3597 |
| 24 | 🇬🇹 GT | 3426 |
| 25 | 🇭🇷 HR | 3099 |
| 26 | 🇰🇷 KR | 3074 |
| 27 | 🇲🇦 MA | 2699 |
| 28 | 🇲🇪 ME | 2550 |
| 29 | 🇳🇱 NL | 2443 |
| 30 | 🇮🇩 ID | 2264 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5541 |
| 2 | Denver International Airport |  | US | 4438 |
| 3 | Indira Gandhi International Airport |  | IN | 3251 |
| 4 | Tokyo International Airport |  | JP | 3121 |
| 5 | El Dorado International Airport |  | CO | 2983 |
| 6 | Harry Reid International Airport |  | US | 2925 |
| 7 | Guaymaral Airport |  | CO | 2828 |
| 8 | Zurich Airport |  | CH | 2821 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2729 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2613 |
| 11 | La Aurora Airport |  | GT | 2604 |
| 12 | Salt Lake City International Airport |  | US | 2414 |
| 13 | Congonhas Airport |  | BR | 2324 |
| 14 | Chicago O'Hare International Airport |  | US | 2315 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2230 |
| 16 | Capua Airport |  | IT | 2102 |
| 17 | Madrid Barajas International Airport |  | ES | 2097 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2063 |
| 19 | Frankfurt am Main International Airport |  | DE | 2054 |
| 20 | Malpensa International Airport |  | IT | 1934 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1933 |
| 22 | Charles de Gaulle International Airport |  | FR | 1931 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1917 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1906 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1828 |
| 26 | Macau International Airport |  | MO | 1789 |
| 27 | Ninoy Aquino International Airport |  | PH | 1767 |
| 28 | Charlotte/Douglas International Airport |  | US | 1699 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1695 |
| 30 | Barcelona International Airport |  | ES | 1685 |
| 31 | Viracopos International Airport |  | BR | 1637 |
| 32 | Kuala Lumpur International Airport |  | MY | 1630 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1599 |
| 34 | Seattle-Tacoma International Airport |  | US | 1594 |
| 35 | Calgary International Airport |  | CA | 1548 |
| 36 | Don Mueang International Airport |  | TH | 1543 |
| 37 | Bengaluru International Airport |  | IN | 1530 |
| 38 | Oslo Gardermoen Airport |  | NO | 1525 |
| 39 | Vancouver International Airport |  | CA | 1522 |
| 40 | Reno/Tahoe International Airport |  | US | 1458 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1125 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1021 | 21m | 244 km | 4,299.2 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 753 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 686 | 1h 6m | 770 km | 9,113.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 682 | 24m | 225 km | 2,645.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 602 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 456 | 44m | 555 km | 4,366.4 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 438 | 27m | 275 km | 2,075.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 430 | 1h 50m | 1,423 km | 10,552.9 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 418 | 44m | 241 km | 1,736.3 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 391 | 24m | 218 km | 1,473.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 379 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 367 | 21m | 250 km | 1,585.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 364 | 23m | 55 km | 346.0 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 349 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 345 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 342 | 1h 6m | 706 km | 4,163.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 341 | 19m | 99 km | 584.1 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 337 | 26m | 215 km | 1,248.1 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 317 | 19m | 144 km | 788.5 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 308 | 1h 14m | 961 km | 5,105.3 t |
| 24 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 303 | 18m | 14 km | 75.8 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 302 | 42m | 535 km | 2,789.2 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 295 | 1h 50m | 1,304 km | 6,636.7 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| THY3032 | Turkish Airlines | Antalya International Airport (LTAI) | Bezymyanka Airfield (UWWG) | 2026-09-29 08:53 UTC | 2026-09-29 12:15 UTC | 3h 21m |
| ERU835 | ERU | Daytona Beach International Airport (KDAB) | Skinners Wholesale Nursery Airport (16FD) | 2026-09-29 11:12 UTC | 2026-09-29 12:11 UTC | 59m |
| N98EG |  | Linden Airport (KLDJ) | Monmouth Executive Airport (KBLM) | 2026-09-29 12:00 UTC | 2026-09-29 12:11 UTC | 10m |
| N422JC |  | Chorman Airport (KD74) | Huey Airport (DE14) | 2026-09-29 11:36 UTC | 2026-09-29 12:08 UTC | 32m |
| N709PT |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-09-29 11:35 UTC | 2026-09-29 12:06 UTC | 31m |
| DMDIS | DMD | Augsburg Airport (EDMA) | Tannheim Airport (EDMT) | 2026-09-29 11:32 UTC | 2026-09-29 12:05 UTC | 33m |
| EFY7812 | EFY | El Dorado International Airport (SKBO) | La Nubia Airport (SKMZ) | 2026-09-29 11:26 UTC | 2026-09-29 11:55 UTC | 29m |
| RHINO26 | RHI | Toulouse-Francazal (BA 101) Air Base (LFBF) | Toulouse-Francazal (BA 101) Air Base (LFBF) | 2026-09-29 11:01 UTC | 2026-09-29 11:52 UTC | 50m |
| UPS946 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Oakland San Francisco Bay Airport (KOAK) | 2026-09-29 07:46 UTC | 2026-09-29 11:51 UTC | 4h 4m |
| ERU852 | ERU | Daytona Beach International Airport (KDAB) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-09-29 11:29 UTC | 2026-09-29 11:47 UTC | 17m |
| ERU476 | ERU | Daytona Beach International Airport (KDAB) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-09-29 11:07 UTC | 2026-09-29 11:43 UTC | 36m |
| N73929 |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-09-29 11:17 UTC | 2026-09-29 11:39 UTC | 21m |
| N4325R |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-09-29 11:14 UTC | 2026-09-29 11:38 UTC | 23m |
| TAM3514 | LATAM Airlines | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | Caçador Airport (SBCD) | 2026-09-29 10:43 UTC | 2026-09-29 11:37 UTC | 53m |
| SWR1DT | Swiss International | Zurich Airport (LSZH) | Stuttgart Airport (EDDS) | 2026-09-29 11:10 UTC | 2026-09-29 11:34 UTC | 23m |
| JAL377 | Japan Airlines | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-09-29 10:23 UTC | 2026-09-29 11:32 UTC | 1h 8m |
| N1653F |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-09-29 11:16 UTC | 2026-09-29 11:31 UTC | 15m |
| NOK604 | NOK | Don Mueang International Airport (VTBD) | Bokpyinn Airport (VYBP) | 2026-09-29 11:01 UTC | 2026-09-29 11:31 UTC | 29m |
| SXHGG | SXH | Eleftherios Venizelos International Airport (LGAV) | Syros Airport (LGSO) | 2026-09-29 10:39 UTC | 2026-09-29 11:30 UTC | 50m |
| LLR513 | LLR | Bengaluru International Airport (VOBL) | Salem Airport (VOSM) | 2026-09-29 11:04 UTC | 2026-09-29 11:26 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
