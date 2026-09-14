# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--14_13:47:27_UTC-green)

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

**Latest saved flight:** 2026-09-14 13:47:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-14 13:47:27 UTC

- **258,349** saved flights
- **76,817** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **258,349** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,127,577.2 tonnes** estimated CO2 emissions
- **181,308,826 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10256 |
| 2 | SkyWest Airlines | 8996 |
| 3 | EJA | 5006 |
| 4 | IndiGo | 4340 |
| 5 | American Airlines | 4080 |
| 6 | Southwest Airlines | 3801 |
| 7 | Delta Air Lines | 3232 |
| 8 | ENY | 3061 |
| 9 | LATAM Airlines | 2487 |
| 10 | AZU | 2420 |
| 11 | Vueling | 2187 |
| 12 | WIF | 2074 |
| 13 | LXJ | 2019 |
| 14 | Lufthansa | 2018 |
| 15 | easyJet | 1761 |
| 16 | Swiss International | 1726 |
| 17 | QLK | 1666 |
| 18 | AXM | 1647 |
| 19 | EJU | 1640 |
| 20 | United Airlines | 1596 |
| 21 | Alaska Airlines | 1533 |
| 22 | All Nippon Airways | 1498 |
| 23 | WMT | 1460 |
| 24 | GLO | 1439 |
| 25 | PGT | 1436 |
| 26 | Air France | 1413 |
| 27 | VIV | 1411 |
| 28 | Wizz Air | 1408 |
| 29 | AEE | 1249 |
| 30 | JetBlue | 1249 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 214413 |
| 2 | 🇪🇸 ES | 16385 |
| 3 | 🇧🇷 BR | 15102 |
| 4 | 🇦🇺 AU | 14732 |
| 5 | 🇨🇦 CA | 14377 |
| 6 | 🇮🇹 IT | 14079 |
| 7 | 🇮🇳 IN | 13638 |
| 8 | 🇩🇪 DE | 12574 |
| 9 | 🇬🇧 GB | 12044 |
| 10 | 🇨🇴 CO | 11593 |
| 11 | 🇫🇷 FR | 10381 |
| 12 | 🇯🇵 JP | 10067 |
| 13 | 🇹🇷 TR | 7778 |
| 14 | 🇬🇷 GR | 7525 |
| 15 | 🇲🇽 MX | 7118 |
| 16 | 🇨🇭 CH | 6935 |
| 17 | 🇳🇴 NO | 6386 |
| 18 | 🇹🇭 TH | 4647 |
| 19 | 🇲🇾 MY | 4432 |
| 20 | 🇿🇦 ZA | 4392 |
| 21 | 🇵🇱 PL | 4281 |
| 22 | 🇳🇿 NZ | 3571 |
| 23 | 🇵🇭 PH | 3474 |
| 24 | 🇬🇹 GT | 3265 |
| 25 | 🇭🇷 HR | 2964 |
| 26 | 🇰🇷 KR | 2955 |
| 27 | 🇲🇦 MA | 2593 |
| 28 | 🇲🇪 ME | 2432 |
| 29 | 🇳🇱 NL | 2322 |
| 30 | 🇮🇩 ID | 2193 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5296 |
| 2 | Denver International Airport |  | US | 4176 |
| 3 | Indira Gandhi International Airport |  | IN | 3122 |
| 4 | Tokyo International Airport |  | JP | 3003 |
| 5 | Guaymaral Airport |  | CO | 2766 |
| 6 | Harry Reid International Airport |  | US | 2740 |
| 7 | Zurich Airport |  | CH | 2710 |
| 8 | El Dorado International Airport |  | CO | 2699 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2603 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2521 |
| 11 | La Aurora Airport |  | GT | 2480 |
| 12 | Salt Lake City International Airport |  | US | 2276 |
| 13 | Chicago O'Hare International Airport |  | US | 2246 |
| 14 | Congonhas Airport |  | BR | 2213 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2112 |
| 16 | Capua Airport |  | IT | 2024 |
| 17 | Madrid Barajas International Airport |  | ES | 2013 |
| 18 | Frankfurt am Main International Airport |  | DE | 1990 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1942 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1863 |
| 21 | Malpensa International Airport |  | IT | 1859 |
| 22 | Charles de Gaulle International Airport |  | FR | 1821 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1819 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1786 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1753 |
| 26 | Macau International Airport |  | MO | 1712 |
| 27 | Ninoy Aquino International Airport |  | PH | 1702 |
| 28 | Barcelona International Airport |  | ES | 1623 |
| 29 | Charlotte/Douglas International Airport |  | US | 1616 |
| 30 | Kuala Lumpur International Airport |  | MY | 1594 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1583 |
| 32 | Viracopos International Airport |  | BR | 1558 |
| 33 | Seattle-Tacoma International Airport |  | US | 1516 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1507 |
| 35 | Don Mueang International Airport |  | TH | 1486 |
| 36 | Calgary International Airport |  | CA | 1477 |
| 37 | Bengaluru International Airport |  | IN | 1469 |
| 38 | Oslo Gardermoen Airport |  | NO | 1457 |
| 39 | Vancouver International Airport |  | CA | 1448 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1391 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 963 | 21m | 244 km | 4,054.9 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 696 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 648 | 1h 6m | 770 km | 8,608.2 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 646 | 24m | 225 km | 2,506.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 577 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 419 | 27m | 275 km | 1,985.5 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 419 | 44m | 555 km | 4,012.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 411 | 1h 50m | 1,423 km | 10,086.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 391 | 44m | 241 km | 1,624.1 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 363 | 24m | 218 km | 1,367.6 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 356 | 21m | 250 km | 1,537.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 343 | 23m | 55 km | 326.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 326 | 1h 6m | 706 km | 3,969.1 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 321 | 26m | 215 km | 1,188.8 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 321 | 19m | 99 km | 549.8 t |
| 19 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 315 | 12m | - | - |
| 20 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 309 | 13m | - | - |
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
| SYS104 | SYS | RAF Shawbury (EGOS) | RAF Shawbury (EGOS) | 2026-09-14 12:19 UTC | 2026-09-14 13:47 UTC | 1h 27m |
| ARG1226 | ARG | Jorge Newbery Airpark (SABE) | Ely Rego Airport (SIJR) | 2026-09-14 12:11 UTC | 2026-09-14 13:45 UTC | 1h 34m |
| CLOVE1 | CLO | Randolph Afb Airport (KRND) | Haass Field (TE57) | 2026-09-14 13:33 UTC | 2026-09-14 13:45 UTC | 12m |
| PAT712A | PAT | Fernando Luis Ribas Dominicci Airport (TJIG) | Antonio/Nery/Juarbe Pol Airport (TJAB) | 2026-09-14 13:30 UTC | 2026-09-14 13:44 UTC | 13m |
| GOLEM41 | GOL | 75OK (75OK) | Ramey 1 Airport (0OK8) | 2026-09-14 12:36 UTC | 2026-09-14 13:41 UTC | 1h 4m |
| OST48 | OST | Stillwater Regional Airport (KSWO) | Haskell Airport (K2K9) | 2026-09-14 13:04 UTC | 2026-09-14 13:37 UTC | 33m |
| HBZYW | HBZ | Wangen-Lachen Airport (LSPV) | Hausen am Albis Airport (LSZN) | 2026-09-14 13:13 UTC | 2026-09-14 13:34 UTC | 21m |
| FIRE01 | FIR | Lousa Private Airport (LPLZ) | Braga Municipal Aerodrome (LPBR) | 2026-09-14 12:35 UTC | 2026-09-14 13:33 UTC | 58m |
| N4640E |  | K36U (K36U) | K36U (K36U) | 2026-09-14 13:09 UTC | 2026-09-14 13:33 UTC | 24m |
| N8024Q |  | Trenton Mercer Airport (KTTN) | Lehigh Valley International Airport (KABE) | 2026-09-14 12:43 UTC | 2026-09-14 13:27 UTC | 44m |
| SYS670 | SYS | RAF Shawbury (EGOS) | RAF Shawbury (EGOS) | 2026-09-14 11:57 UTC | 2026-09-14 13:23 UTC | 1h 26m |
| CXK149 | CXK | Mckinney Ntl Airport (KTKI) | Square Air Airport (TS63) | 2026-09-14 13:02 UTC | 2026-09-14 13:23 UTC | 21m |
| ERU909 | ERU | Daytona Beach International Airport (KDAB) | New Smyrna Beach Municipal (Jack Bolt Field) Airport (KEVB) | 2026-09-14 12:59 UTC | 2026-09-14 13:22 UTC | 23m |
| N998CT |  | Fort Lauderdale Executive Airport (KFXE) | Duda Airstrip (FA69) | 2026-09-14 12:49 UTC | 2026-09-14 13:19 UTC | 30m |
| IGO746L | IndiGo | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 2026-09-14 12:09 UTC | 2026-09-14 13:18 UTC | 1h 9m |
| WIF850 | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-09-14 13:03 UTC | 2026-09-14 13:16 UTC | 13m |
| OOGEE | OOG | La Mole Airport (LFTZ) | Brussels Airport (EBBR) | 2026-09-14 10:53 UTC | 2026-09-14 13:13 UTC | 2h 20m |
| AIC6NR | Air India | Chennai International Airport (VOMM) | Pune Airport (VAPO) | 2026-09-14 11:50 UTC | 2026-09-14 13:11 UTC | 1h 20m |
| N85NG |  | Boise Air Trml/Gowen Field (KBOI) | Hanson Airport (0MT6) | 2026-09-14 12:03 UTC | 2026-09-14 13:11 UTC | 1h 8m |
| N225SF |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-09-14 12:55 UTC | 2026-09-14 13:11 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
