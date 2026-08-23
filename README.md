# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_16:01:42_UTC-green)

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

**Latest saved flight:** 2026-08-23 16:01:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 16:01:42 UTC

- **229,004** saved flights
- **70,799** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **229,004** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,761,783.5 tonnes** estimated CO2 emissions
- **160,103,389 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9200 |
| 2 | SkyWest Airlines | 8113 |
| 3 | EJA | 4404 |
| 4 | IndiGo | 3876 |
| 5 | American Airlines | 3746 |
| 6 | Southwest Airlines | 3550 |
| 7 | Delta Air Lines | 2930 |
| 8 | ENY | 2794 |
| 9 | LATAM Airlines | 2200 |
| 10 | AZU | 2127 |
| 11 | Vueling | 1946 |
| 12 | Lufthansa | 1873 |
| 13 | WIF | 1804 |
| 14 | LXJ | 1792 |
| 15 | easyJet | 1599 |
| 16 | Swiss International | 1531 |
| 17 | AXM | 1520 |
| 18 | EJU | 1459 |
| 19 | United Airlines | 1450 |
| 20 | QLK | 1448 |
| 21 | Alaska Airlines | 1385 |
| 22 | All Nippon Airways | 1372 |
| 23 | GLO | 1272 |
| 24 | VIV | 1255 |
| 25 | PGT | 1252 |
| 26 | WMT | 1252 |
| 27 | Air France | 1244 |
| 28 | Wizz Air | 1197 |
| 29 | JetBlue | 1143 |
| 30 | AEE | 1141 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 191030 |
| 2 | 🇪🇸 ES | 14711 |
| 3 | 🇧🇷 BR | 13375 |
| 4 | 🇦🇺 AU | 12963 |
| 5 | 🇨🇦 CA | 12637 |
| 6 | 🇮🇹 IT | 12391 |
| 7 | 🇮🇳 IN | 12082 |
| 8 | 🇩🇪 DE | 11283 |
| 9 | 🇬🇧 GB | 10783 |
| 10 | 🇨🇴 CO | 9437 |
| 11 | 🇯🇵 JP | 9312 |
| 12 | 🇫🇷 FR | 9182 |
| 13 | 🇹🇷 TR | 6747 |
| 14 | 🇬🇷 GR | 6734 |
| 15 | 🇲🇽 MX | 6364 |
| 16 | 🇨🇭 CH | 6090 |
| 17 | 🇳🇴 NO | 5631 |
| 18 | 🇲🇾 MY | 4062 |
| 19 | 🇹🇭 TH | 3997 |
| 20 | 🇿🇦 ZA | 3993 |
| 21 | 🇵🇱 PL | 3815 |
| 22 | 🇳🇿 NZ | 3169 |
| 23 | 🇵🇭 PH | 3144 |
| 24 | 🇬🇹 GT | 2878 |
| 25 | 🇰🇷 KR | 2705 |
| 26 | 🇭🇷 HR | 2617 |
| 27 | 🇲🇦 MA | 2323 |
| 28 | 🇲🇪 ME | 2090 |
| 29 | 🇳🇱 NL | 2054 |
| 30 | 🇮🇩 ID | 1978 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4776 |
| 2 | Denver International Airport |  | US | 3718 |
| 3 | Indira Gandhi International Airport |  | IN | 2793 |
| 4 | Tokyo International Airport |  | JP | 2781 |
| 5 | Guaymaral Airport |  | CO | 2648 |
| 6 | Harry Reid International Airport |  | US | 2475 |
| 7 | Zurich Airport |  | CH | 2387 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2341 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2310 |
| 10 | La Aurora Airport |  | GT | 2192 |
| 11 | El Dorado International Airport |  | CO | 2093 |
| 12 | Chicago O'Hare International Airport |  | US | 2072 |
| 13 | Salt Lake City International Airport |  | US | 2011 |
| 14 | Congonhas Airport |  | BR | 1951 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1940 |
| 16 | Frankfurt am Main International Airport |  | DE | 1837 |
| 17 | Madrid Barajas International Airport |  | ES | 1794 |
| 18 | Capua Airport |  | IT | 1788 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1715 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1703 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1650 |
| 22 | Malpensa International Airport |  | IT | 1638 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1612 |
| 24 | Macau International Airport |  | MO | 1596 |
| 25 | Charles de Gaulle International Airport |  | FR | 1587 |
| 26 | Ninoy Aquino International Airport |  | PH | 1509 |
| 27 | Charlotte/Douglas International Airport |  | US | 1495 |
| 28 | Kuala Lumpur International Airport |  | MY | 1471 |
| 29 | Barcelona International Airport |  | ES | 1435 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1385 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1364 |
| 32 | Viracopos International Airport |  | BR | 1361 |
| 33 | Bengaluru International Airport |  | IN | 1357 |
| 34 | Seattle-Tacoma International Airport |  | US | 1348 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1345 |
| 36 | Don Mueang International Airport |  | TH | 1307 |
| 37 | Calgary International Airport |  | CA | 1299 |
| 38 | Oslo Gardermoen Airport |  | NO | 1272 |
| 39 | Vitoria/Foronda Airport |  | ES | 1249 |
| 40 | O. R. Tambo International Airport |  | ZA | 1240 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1075 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 834 | 21m | 244 km | 3,511.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 575 | 1h 6m | 770 km | 7,638.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 567 | 24m | 225 km | 2,199.7 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 553 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 514 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 380 | 27m | 275 km | 1,800.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 351 | 1h 50m | 1,423 km | 8,614.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 317 | 21m | 250 km | 1,369.2 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 315 | 1h 7m | 706 km | 3,835.1 t |
| 13 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 14 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 310 | 44m | 555 km | 2,968.4 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 306 | 22m | 55 km | 290.8 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 297 | 24m | 218 km | 1,118.9 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 294 | 1h 38m | 1,156 km | 5,865.2 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 285 | 19m | 99 km | 488.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 278 | 27m | 215 km | 1,029.6 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 268 | 1h 14m | 961 km | 4,442.2 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 266 | 12m | - | - |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 261 | 19m | 144 km | 649.2 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 245 | 1h 50m | 1,304 km | 5,511.9 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 241 | 15m | 154 km | 638.6 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 240 | 28m | 152 km | 627.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N583CA |  | Dallas Executive Airport (KRBD) | Lancaster Regional Airport (KLNC) | 2026-08-23 14:44 UTC | 2026-08-23 16:01 UTC | 1h 17m |
| N93EP |  | Martha's Vineyard Airport (KMVY) | Wings Field (KLOM) | 2026-08-23 15:05 UTC | 2026-08-23 16:01 UTC | 55m |
| N601MB |  | Gooden Airpark (KRJD) | 5MD0 (5MD0) | 2026-08-23 14:37 UTC | 2026-08-23 16:00 UTC | 1h 23m |
| HAWK238 | HAW | Corpus Christi International Airport (KCRP) | Cage Ranch Airport (7TE2) | 2026-08-23 15:38 UTC | 2026-08-23 16:00 UTC | 21m |
| N627RG |  | Harford County Airport (K0W3) | Ocean City Municipal Airport (KOXB) | 2026-08-23 15:16 UTC | 2026-08-23 15:58 UTC | 41m |
| FTO383 | FTO | KHTO (KHTO) | Laguardia Airport (KLGA) | 2026-08-23 15:15 UTC | 2026-08-23 15:58 UTC | 42m |
| N6428S |  | Watts-Woodland Airport (KO41) | Angwin-Parrett Field (K2O3) | 2026-08-23 15:44 UTC | 2026-08-23 15:58 UTC | 13m |
| N5217G |  | King Salmon Airport (PAKN) | Tibbetts Airport (4AK9) | 2026-08-23 15:39 UTC | 2026-08-23 15:56 UTC | 16m |
| FFL626 | FFL | Reid-Hillview Of Santa Clara County Airport (KRHV) | Meadows Field (KBFL) | 2026-08-23 15:03 UTC | 2026-08-23 15:55 UTC | 52m |
| N165EA |  | Reno/Tahoe International Airport (KRNO) | Reno/Tahoe International Airport (KRNO) | 2026-08-23 15:38 UTC | 2026-08-23 15:54 UTC | 15m |
| TRP7 | TRP | Robinson Airport (MD14) | Joint Base Andrews Airport (KADW) | 2026-08-23 15:41 UTC | 2026-08-23 15:53 UTC | 12m |
| N436CA |  | Meadows Field (KBFL) | Bakersfield Municipal Airport (KL45) | 2026-08-23 15:12 UTC | 2026-08-23 15:49 UTC | 37m |
| SPHSA | SPH | Tomaszów Mazowiecki Military Air Base (EPTM) | Tomaszów Mazowiecki Military Air Base (EPTM) | 2026-08-23 15:21 UTC | 2026-08-23 15:49 UTC | 27m |
| N999VP |  | IS95 (IS95) | 2LL1 (2LL1) | 2026-08-23 15:33 UTC | 2026-08-23 15:43 UTC | 10m |
| NDU679 | NDU | Pinal Airpark (KMZJ) | Sarita Airport (37AZ) | 2026-08-23 15:18 UTC | 2026-08-23 15:41 UTC | 23m |
| N424T |  | Phoenix Deer Valley Airport (KDVT) | Montezuma Airport (19AZ) | 2026-08-23 15:01 UTC | 2026-08-23 15:38 UTC | 37m |
| N843FF |  | Perugia / San Egidio Airport (LIRZ) | Bangor International Airport (KBGR) | 2026-08-23 07:40 UTC | 2026-08-23 15:38 UTC | 7h 58m |
| SFY114 | SFY | Broocke Air Patch Airport (FL95) | Fellsmere Airport (4FL3) | 2026-08-23 15:11 UTC | 2026-08-23 15:37 UTC | 25m |
| SIO007 | SIO | Milas Bodrum International Airport (LTFE) | Samedan Airport (LSZS) | 2026-08-23 13:21 UTC | 2026-08-23 15:36 UTC | 2h 14m |
| N541S |  | John C Tune Airport (KJWN) | Savannah-Hardin County Airport (KSNH) | 2026-08-23 15:17 UTC | 2026-08-23 15:35 UTC | 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
