# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_22:15:08_UTC-green)

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

**Latest saved flight:** 2026-08-23 22:15:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 22:15:08 UTC

- **230,350** saved flights
- **71,098** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **230,350** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,778,024.4 tonnes** estimated CO2 emissions
- **161,044,891 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9252 |
| 2 | SkyWest Airlines | 8187 |
| 3 | EJA | 4462 |
| 4 | IndiGo | 3882 |
| 5 | American Airlines | 3778 |
| 6 | Southwest Airlines | 3561 |
| 7 | Delta Air Lines | 2946 |
| 8 | ENY | 2813 |
| 9 | LATAM Airlines | 2216 |
| 10 | AZU | 2141 |
| 11 | Vueling | 1958 |
| 12 | Lufthansa | 1874 |
| 13 | LXJ | 1820 |
| 14 | WIF | 1813 |
| 15 | easyJet | 1608 |
| 16 | Swiss International | 1538 |
| 17 | AXM | 1520 |
| 18 | EJU | 1468 |
| 19 | United Airlines | 1464 |
| 20 | QLK | 1451 |
| 21 | Alaska Airlines | 1388 |
| 22 | All Nippon Airways | 1372 |
| 23 | GLO | 1286 |
| 24 | VIV | 1264 |
| 25 | WMT | 1262 |
| 26 | PGT | 1259 |
| 27 | Air France | 1253 |
| 28 | Wizz Air | 1212 |
| 29 | JetBlue | 1149 |
| 30 | AEE | 1147 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 192351 |
| 2 | 🇪🇸 ES | 14782 |
| 3 | 🇧🇷 BR | 13478 |
| 4 | 🇦🇺 AU | 12972 |
| 5 | 🇨🇦 CA | 12719 |
| 6 | 🇮🇹 IT | 12473 |
| 7 | 🇮🇳 IN | 12101 |
| 8 | 🇩🇪 DE | 11329 |
| 9 | 🇬🇧 GB | 10842 |
| 10 | 🇨🇴 CO | 9569 |
| 11 | 🇯🇵 JP | 9314 |
| 12 | 🇫🇷 FR | 9219 |
| 13 | 🇹🇷 TR | 6802 |
| 14 | 🇬🇷 GR | 6770 |
| 15 | 🇲🇽 MX | 6407 |
| 16 | 🇨🇭 CH | 6116 |
| 17 | 🇳🇴 NO | 5659 |
| 18 | 🇲🇾 MY | 4063 |
| 19 | 🇿🇦 ZA | 4015 |
| 20 | 🇹🇭 TH | 3997 |
| 21 | 🇵🇱 PL | 3827 |
| 22 | 🇳🇿 NZ | 3181 |
| 23 | 🇵🇭 PH | 3147 |
| 24 | 🇬🇹 GT | 2902 |
| 25 | 🇰🇷 KR | 2706 |
| 26 | 🇭🇷 HR | 2638 |
| 27 | 🇲🇦 MA | 2335 |
| 28 | 🇲🇪 ME | 2111 |
| 29 | 🇳🇱 NL | 2059 |
| 30 | 🇮🇩 ID | 1978 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4812 |
| 2 | Denver International Airport |  | US | 3752 |
| 3 | Indira Gandhi International Airport |  | IN | 2800 |
| 4 | Tokyo International Airport |  | JP | 2781 |
| 5 | Guaymaral Airport |  | CO | 2654 |
| 6 | Harry Reid International Airport |  | US | 2487 |
| 7 | Zurich Airport |  | CH | 2403 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2356 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2318 |
| 10 | La Aurora Airport |  | GT | 2211 |
| 11 | El Dorado International Airport |  | CO | 2132 |
| 12 | Chicago O'Hare International Airport |  | US | 2091 |
| 13 | Salt Lake City International Airport |  | US | 2030 |
| 14 | Congonhas Airport |  | BR | 1968 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1950 |
| 16 | Frankfurt am Main International Airport |  | DE | 1843 |
| 17 | Madrid Barajas International Airport |  | ES | 1807 |
| 18 | Capua Airport |  | IT | 1806 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1728 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1714 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1653 |
| 22 | Malpensa International Airport |  | IT | 1646 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1612 |
| 24 | Charles de Gaulle International Airport |  | FR | 1598 |
| 25 | Macau International Airport |  | MO | 1597 |
| 26 | Ninoy Aquino International Airport |  | PH | 1511 |
| 27 | Charlotte/Douglas International Airport |  | US | 1505 |
| 28 | Kuala Lumpur International Airport |  | MY | 1472 |
| 29 | Barcelona International Airport |  | ES | 1442 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1398 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1388 |
| 32 | Viracopos International Airport |  | BR | 1370 |
| 33 | Bengaluru International Airport |  | IN | 1358 |
| 34 | Seattle-Tacoma International Airport |  | US | 1357 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1352 |
| 36 | Calgary International Airport |  | CA | 1310 |
| 37 | Don Mueang International Airport |  | TH | 1307 |
| 38 | Oslo Gardermoen Airport |  | NO | 1283 |
| 39 | Vitoria/Foronda Airport |  | ES | 1252 |
| 40 | O. R. Tambo International Airport |  | ZA | 1250 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1076 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 837 | 21m | 244 km | 3,524.4 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 575 | 1h 6m | 770 km | 7,638.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 567 | 24m | 225 km | 2,199.7 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 563 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 517 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 380 | 27m | 275 km | 1,800.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 353 | 1h 50m | 1,423 km | 8,663.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 334 | 44m | 241 km | 1,387.4 t |
| 11 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 325 | 21m | 250 km | 1,403.8 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 315 | 1h 7m | 706 km | 3,835.1 t |
| 13 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 14 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 310 | 44m | 555 km | 2,968.4 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 307 | 22m | 55 km | 291.8 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 298 | 24m | 218 km | 1,122.7 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 297 | 1h 38m | 1,156 km | 5,925.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 285 | 19m | 99 km | 488.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 280 | 27m | 215 km | 1,037.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 271 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 270 | 1h 14m | 961 km | 4,475.4 t |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 265 | 13m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 262 | 19m | 144 km | 651.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 247 | 1h 50m | 1,304 km | 5,556.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 244 | 28m | 152 km | 637.7 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 241 | 15m | 154 km | 638.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N32169 |  | Santa Monica Municipal Airport (KSMO) | Santa Barbara Municipal Airport (KSBA) | 2026-08-23 21:28 UTC | 2026-08-23 22:15 UTC | 47m |
| VKIN16 | VKI | Calgary International Airport (CYYC) | Swift Current Airport (CYYN) | 2026-08-23 21:17 UTC | 2026-08-23 22:11 UTC | 54m |
| N5399K |  | Bolingbrook's Clow International Airport (K1C5) | Morris Municipal/James R Washburn Field (KC09) | 2026-08-23 21:29 UTC | 2026-08-23 22:10 UTC | 40m |
| CAP424 | CAP | Buchanan Field (KCCR) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-23 21:01 UTC | 2026-08-23 22:06 UTC | 1h 4m |
| QLK571D | QLK | Adelaide International Airport (YPAD) | Whyalla Airport (YWHA) | 2026-08-23 21:23 UTC | 2026-08-23 22:01 UTC | 38m |
| EJA974 | EJA | City Of Colorado Springs Municipal Airport (KCOS) | True Grit South Airport (CO95) | 2026-08-23 21:06 UTC | 2026-08-23 21:55 UTC | 49m |
| N100BW |  | Talkeetna Village Strip (AK44) | Mc Kinley Country Airport (81AK) | 2026-08-23 21:23 UTC | 2026-08-23 21:51 UTC | 28m |
| MAFFS2 | MAF | Boise Air Trml/Gowen Field (KBOI) | Bald Mountain Airport (OG45) | 2026-08-23 21:33 UTC | 2026-08-23 21:51 UTC | 17m |
| N626LM |  | Sussex Airport (KFWN) | Sussex Airport (KFWN) | 2026-08-23 21:39 UTC | 2026-08-23 21:50 UTC | 11m |
| N707KA |  | Boeing Field/King County International Airport (KBFI) | Victoria International Airport (CYYJ) | 2026-08-23 21:07 UTC | 2026-08-23 21:50 UTC | 42m |
| BAW398 | British Airways | London Heathrow Airport (EGLL) | HE42 (HE42) | 2026-08-23 17:43 UTC | 2026-08-23 21:49 UTC | 4h 6m |
| CFG4105 | CFG | Frankfurt am Main International Airport (EDDF) | HE12 (HE12) | 2026-08-23 18:12 UTC | 2026-08-23 21:45 UTC | 3h 33m |
| N185YY |  | Tidewater Airport (77AK) | Ted Stevens Anchorage International Airport (PANC) | 2026-08-23 21:32 UTC | 2026-08-23 21:45 UTC | 13m |
| CCDAL | CCD | Municipal de Vitacura Airport (SCLC) | Eulogio Sanchez Airport (SCTB) | 2026-08-23 21:31 UTC | 2026-08-23 21:44 UTC | 13m |
| EJA843 | EJA | John Wayne/Orange County Airport (KSNA) | Henderson Executive Airport (KHND) | 2026-08-23 20:58 UTC | 2026-08-23 21:44 UTC | 45m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-23 21:32 UTC | 2026-08-23 21:44 UTC | 11m |
| N628SR |  | San Carlos Airport (KSQL) | Truckee-Tahoe Airport (KTRK) | 2026-08-23 21:05 UTC | 2026-08-23 21:40 UTC | 34m |
| N412TB |  | Minden-Tahoe Airport (KMEV) | Sweetwater (Usmc) Airport (NV72) | 2026-08-23 20:06 UTC | 2026-08-23 21:38 UTC | 1h 31m |
| EZY34JP | easyJet | London Luton Airport (EGGW) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-23 19:57 UTC | 2026-08-23 21:36 UTC | 1h 39m |
| EJA322 | EJA | Mc Clellan-Palomar Airport (KCRQ) | Truckee-Tahoe Airport (KTRK) | 2026-08-23 20:35 UTC | 2026-08-23 21:36 UTC | 1h 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
