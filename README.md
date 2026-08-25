# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_12:51:16_UTC-green)

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

**Latest saved flight:** 2026-08-25 12:51:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 12:51:16 UTC

- **234,999** saved flights
- **71,939** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **234,999** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,832,144.0 tonnes** estimated CO2 emissions
- **164,182,258 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9426 |
| 2 | SkyWest Airlines | 8299 |
| 3 | EJA | 4555 |
| 4 | IndiGo | 3977 |
| 5 | American Airlines | 3815 |
| 6 | Southwest Airlines | 3599 |
| 7 | Delta Air Lines | 2991 |
| 8 | ENY | 2854 |
| 9 | LATAM Airlines | 2256 |
| 10 | AZU | 2190 |
| 11 | Vueling | 2013 |
| 12 | Lufthansa | 1913 |
| 13 | WIF | 1869 |
| 14 | LXJ | 1844 |
| 15 | easyJet | 1641 |
| 16 | Swiss International | 1577 |
| 17 | AXM | 1574 |
| 18 | EJU | 1503 |
| 19 | QLK | 1497 |
| 20 | United Airlines | 1485 |
| 21 | Alaska Airlines | 1417 |
| 22 | All Nippon Airways | 1401 |
| 23 | GLO | 1308 |
| 24 | WMT | 1307 |
| 25 | VIV | 1295 |
| 26 | PGT | 1280 |
| 27 | Air France | 1278 |
| 28 | Wizz Air | 1248 |
| 29 | AEE | 1167 |
| 30 | JetBlue | 1162 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 195174 |
| 2 | 🇪🇸 ES | 15105 |
| 3 | 🇧🇷 BR | 13711 |
| 4 | 🇦🇺 AU | 13332 |
| 5 | 🇨🇦 CA | 12983 |
| 6 | 🇮🇹 IT | 12786 |
| 7 | 🇮🇳 IN | 12386 |
| 8 | 🇩🇪 DE | 11589 |
| 9 | 🇬🇧 GB | 11081 |
| 10 | 🇨🇴 CO | 9884 |
| 11 | 🇯🇵 JP | 9545 |
| 12 | 🇫🇷 FR | 9421 |
| 13 | 🇹🇷 TR | 6973 |
| 14 | 🇬🇷 GR | 6926 |
| 15 | 🇲🇽 MX | 6529 |
| 16 | 🇨🇭 CH | 6277 |
| 17 | 🇳🇴 NO | 5812 |
| 18 | 🇲🇾 MY | 4219 |
| 19 | 🇹🇭 TH | 4205 |
| 20 | 🇿🇦 ZA | 4115 |
| 21 | 🇵🇱 PL | 3920 |
| 22 | 🇳🇿 NZ | 3247 |
| 23 | 🇵🇭 PH | 3238 |
| 24 | 🇬🇹 GT | 2935 |
| 25 | 🇰🇷 KR | 2757 |
| 26 | 🇭🇷 HR | 2702 |
| 27 | 🇲🇦 MA | 2384 |
| 28 | 🇲🇪 ME | 2177 |
| 29 | 🇳🇱 NL | 2107 |
| 30 | 🇮🇩 ID | 2054 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4874 |
| 2 | Denver International Airport |  | US | 3799 |
| 3 | Indira Gandhi International Airport |  | IN | 2873 |
| 4 | Tokyo International Airport |  | JP | 2842 |
| 5 | Guaymaral Airport |  | CO | 2677 |
| 6 | Harry Reid International Airport |  | US | 2520 |
| 7 | Zurich Airport |  | CH | 2462 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2398 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2356 |
| 10 | La Aurora Airport |  | GT | 2236 |
| 11 | El Dorado International Airport |  | CO | 2207 |
| 12 | Chicago O'Hare International Airport |  | US | 2118 |
| 13 | Salt Lake City International Airport |  | US | 2069 |
| 14 | Congonhas Airport |  | BR | 2001 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1973 |
| 16 | Frankfurt am Main International Airport |  | DE | 1874 |
| 17 | Madrid Barajas International Airport |  | ES | 1849 |
| 18 | Capua Airport |  | IT | 1848 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1767 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1732 |
| 21 | Malpensa International Airport |  | IT | 1683 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1664 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1649 |
| 24 | Charles de Gaulle International Airport |  | FR | 1634 |
| 25 | Macau International Airport |  | MO | 1609 |
| 26 | Ninoy Aquino International Airport |  | PH | 1564 |
| 27 | Kuala Lumpur International Airport |  | MY | 1525 |
| 28 | Charlotte/Douglas International Airport |  | US | 1515 |
| 29 | Barcelona International Airport |  | ES | 1484 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1450 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1421 |
| 32 | Viracopos International Airport |  | BR | 1400 |
| 33 | Bengaluru International Airport |  | IN | 1380 |
| 34 | Seattle-Tacoma International Airport |  | US | 1378 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1377 |
| 36 | Don Mueang International Airport |  | TH | 1365 |
| 37 | Calgary International Airport |  | CA | 1345 |
| 38 | Oslo Gardermoen Airport |  | NO | 1319 |
| 39 | Vancouver International Airport |  | CA | 1283 |
| 40 | O. R. Tambo International Airport |  | ZA | 1280 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1085 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 863 | 21m | 244 km | 3,633.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 598 | 1h 6m | 770 km | 7,944.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 595 | 24m | 225 km | 2,308.3 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 587 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 523 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 387 | 27m | 275 km | 1,833.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 364 | 1h 50m | 1,423 km | 8,933.1 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 361 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 341 | 44m | 555 km | 3,265.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 340 | 44m | 241 km | 1,412.3 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 330 | 21m | 250 km | 1,425.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 317 | 1h 7m | 706 km | 3,859.5 t |
| 14 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 315 | 24m | 218 km | 1,186.7 t |
| 15 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 310 | 1h 40m | 1,156 km | 6,184.4 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 290 | 19m | 99 km | 496.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 288 | 27m | 215 km | 1,066.6 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 273 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 272 | 1h 14m | 961 km | 4,508.5 t |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 267 | 29m | 304 km | 1,399.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 267 | 19m | 144 km | 664.1 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 262 | 15m | 154 km | 694.2 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 251 | 1h 50m | 1,304 km | 5,646.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N475BL |  | Pensacola International Airport (KPNS) | AL97 (AL97) | 2026-08-25 11:24 UTC | 2026-08-25 12:51 UTC | 1h 26m |
| QTR8420 | Qatar Airways | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-08-24 14:19 UTC | 2026-08-25 12:43 UTC | 22h 24m |
| DRAG169 | DRA | Torino / Caselle International Airport (LIMF) | Aosta Airport (LIMW) | 2026-08-25 12:30 UTC | 2026-08-25 12:41 UTC | 11m |
| RNA218 | RNA | Indira Gandhi International Airport (VIDP) | Tribhuvan International Airport (VNKT) | 2026-08-25 11:23 UTC | 2026-08-25 12:41 UTC | 1h 17m |
| HBZVU | HBZ | Reichenbach Air Base (LSGR) | Raron Airport (LSTA) | 2026-08-25 12:15 UTC | 2026-08-25 12:40 UTC | 25m |
| SWR188 | Swiss International | Zurich Airport (LSZH) | UG27 (UG27) | 2026-08-24 11:17 UTC | 2026-08-25 12:39 UTC | 25h 21m |
| SCU17 | SCU | Tulsa Riverside Airport (KRVS) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-08-25 12:15 UTC | 2026-08-25 12:39 UTC | 23m |
| N40HC |  | Birmingham-Shuttlesworth International Airport (KBHM) | Butler Municipal Airport (K6A1) | 2026-08-25 12:09 UTC | 2026-08-25 12:39 UTC | 29m |
| OKDPH | OKD | Letnany Airport (LKLT) | Mnichovo Hradiste Airport (LKMH) | 2026-08-25 12:10 UTC | 2026-08-25 12:37 UTC | 26m |
| HBKTW | HBK | La Mole Airport (LFTZ) | Milano / Bresso Airport (LIMB) | 2026-08-25 11:00 UTC | 2026-08-25 12:36 UTC | 1h 36m |
| LAN056 | LAN | La Puerta Airport (SCPT) | Chicureo Airport (SCHC) | 2026-08-25 12:17 UTC | 2026-08-25 12:34 UTC | 17m |
|  |  | Stoney's Airport (OI32) | Portage County Airport (KPOV) | 2026-08-25 12:31 UTC | 2026-08-25 12:32 UTC | 0m |
| N421PH |  | 5TA2 (5TA2) | Bud Dryden Airport (TX05) | 2026-08-25 11:41 UTC | 2026-08-25 12:28 UTC | 47m |
|  |  | Cairns Army Air Field (Fort Rucker) Airport (KOZR) | Freedom Field (AL41) | 2026-08-25 12:25 UTC | 2026-08-25 12:28 UTC | 3m |
| FSF302A | FSF | La Mole Airport (LFTZ) | Cannes-Mandelieu Airport (LFMD) | 2026-08-25 12:07 UTC | 2026-08-25 12:23 UTC | 15m |
| C10 |  | Linz-Ost Airport (LOLO) | Linz-Ost Airport (LOLO) | 2026-08-25 12:18 UTC | 2026-08-25 12:22 UTC | 3m |
| N534NT |  | East Texas Regional Airport (KGGG) | Snell - North Laramie River Airport (WY25) | 2026-08-25 10:27 UTC | 2026-08-25 12:20 UTC | 1h 52m |
| WIF170 | WIF | Bergen Airport Flesland (ENBR) | Bringeland Airport (ENBL) | 2026-08-25 11:51 UTC | 2026-08-25 12:14 UTC | 23m |
| 8QMBF |  | Dharavandhoo Airport (VRMD) | Dharavandhoo Airport (VRMD) | 2026-08-25 12:00 UTC | 2026-08-25 12:13 UTC | 13m |
| N821TN |  | Kansas City Downtown/Wheeler Field (KMKC) | Marshall Memorial Municipal Airport (KMHL) | 2026-08-25 12:00 UTC | 2026-08-25 12:11 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
