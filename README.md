# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_22:42:53_UTC-green)

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

**Latest saved flight:** 2026-08-23 22:42:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 22:42:53 UTC

- **230,400** saved flights
- **71,109** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **230,400** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,778,614.5 tonnes** estimated CO2 emissions
- **161,079,102 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9252 |
| 2 | SkyWest Airlines | 8189 |
| 3 | EJA | 4462 |
| 4 | IndiGo | 3882 |
| 5 | American Airlines | 3780 |
| 6 | Southwest Airlines | 3561 |
| 7 | Delta Air Lines | 2948 |
| 8 | ENY | 2813 |
| 9 | LATAM Airlines | 2218 |
| 10 | AZU | 2143 |
| 11 | Vueling | 1958 |
| 12 | Lufthansa | 1874 |
| 13 | LXJ | 1820 |
| 14 | WIF | 1813 |
| 15 | easyJet | 1608 |
| 16 | Swiss International | 1538 |
| 17 | AXM | 1520 |
| 18 | EJU | 1470 |
| 19 | United Airlines | 1464 |
| 20 | QLK | 1451 |
| 21 | Alaska Airlines | 1388 |
| 22 | All Nippon Airways | 1372 |
| 23 | GLO | 1287 |
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
| 1 | 🇺🇸 US | 192406 |
| 2 | 🇪🇸 ES | 14784 |
| 3 | 🇧🇷 BR | 13488 |
| 4 | 🇦🇺 AU | 12973 |
| 5 | 🇨🇦 CA | 12720 |
| 6 | 🇮🇹 IT | 12476 |
| 7 | 🇮🇳 IN | 12101 |
| 8 | 🇩🇪 DE | 11329 |
| 9 | 🇬🇧 GB | 10844 |
| 10 | 🇨🇴 CO | 9573 |
| 11 | 🇯🇵 JP | 9316 |
| 12 | 🇫🇷 FR | 9219 |
| 13 | 🇹🇷 TR | 6802 |
| 14 | 🇬🇷 GR | 6771 |
| 15 | 🇲🇽 MX | 6407 |
| 16 | 🇨🇭 CH | 6116 |
| 17 | 🇳🇴 NO | 5659 |
| 18 | 🇲🇾 MY | 4063 |
| 19 | 🇿🇦 ZA | 4015 |
| 20 | 🇹🇭 TH | 3997 |
| 21 | 🇵🇱 PL | 3827 |
| 22 | 🇳🇿 NZ | 3183 |
| 23 | 🇵🇭 PH | 3148 |
| 24 | 🇬🇹 GT | 2903 |
| 25 | 🇰🇷 KR | 2706 |
| 26 | 🇭🇷 HR | 2638 |
| 27 | 🇲🇦 MA | 2337 |
| 28 | 🇲🇪 ME | 2111 |
| 29 | 🇳🇱 NL | 2059 |
| 30 | 🇮🇩 ID | 1978 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4812 |
| 2 | Denver International Airport |  | US | 3754 |
| 3 | Indira Gandhi International Airport |  | IN | 2800 |
| 4 | Tokyo International Airport |  | JP | 2782 |
| 5 | Guaymaral Airport |  | CO | 2654 |
| 6 | Harry Reid International Airport |  | US | 2488 |
| 7 | Zurich Airport |  | CH | 2403 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2358 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2318 |
| 10 | La Aurora Airport |  | GT | 2212 |
| 11 | El Dorado International Airport |  | CO | 2134 |
| 12 | Chicago O'Hare International Airport |  | US | 2091 |
| 13 | Salt Lake City International Airport |  | US | 2030 |
| 14 | Congonhas Airport |  | BR | 1968 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1950 |
| 16 | Frankfurt am Main International Airport |  | DE | 1843 |
| 17 | Madrid Barajas International Airport |  | ES | 1808 |
| 18 | Capua Airport |  | IT | 1806 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1731 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1715 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1653 |
| 22 | Malpensa International Airport |  | IT | 1648 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1612 |
| 24 | Charles de Gaulle International Airport |  | FR | 1598 |
| 25 | Macau International Airport |  | MO | 1597 |
| 26 | Ninoy Aquino International Airport |  | PH | 1512 |
| 27 | Charlotte/Douglas International Airport |  | US | 1506 |
| 28 | Kuala Lumpur International Airport |  | MY | 1472 |
| 29 | Barcelona International Airport |  | ES | 1442 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1398 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1388 |
| 32 | Viracopos International Airport |  | BR | 1370 |
| 33 | Seattle-Tacoma International Airport |  | US | 1358 |
| 34 | Bengaluru International Airport |  | IN | 1358 |
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
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 576 | 1h 6m | 770 km | 7,651.7 t |
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
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 245 | 28m | 152 km | 640.3 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 241 | 15m | 154 km | 638.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N256J |  | Montgomery-Gibbs Executive Airport (KMYF) | Ramona Airport (KRNM) | 2026-08-23 21:27 UTC | 2026-08-23 22:42 UTC | 1h 15m |
| ZKLTH | ZKL | Hood Airport (NZMS) | Hood Airport (NZMS) | 2026-08-23 21:44 UTC | 2026-08-23 22:39 UTC | 55m |
| N53494 |  | Ed Carlson Memorial Field/South Lewis County Airport (KTDO) | Ed Carlson Memorial Field/South Lewis County Airport (KTDO) | 2026-08-23 22:12 UTC | 2026-08-23 22:31 UTC | 18m |
| N190AE |  | Houston County Airport (KM93) | John C Tune Airport (KJWN) | 2026-08-23 21:53 UTC | 2026-08-23 22:19 UTC | 26m |
| N32169 |  | Santa Monica Municipal Airport (KSMO) | Santa Barbara Municipal Airport (KSBA) | 2026-08-23 21:28 UTC | 2026-08-23 22:15 UTC | 47m |
| N353KM |  | San Luis Obispo County Regional Airport (KSBP) | Truckee-Tahoe Airport (KTRK) | 2026-08-23 21:20 UTC | 2026-08-23 22:14 UTC | 54m |
| N539JM |  | Flying K Airport (7TX8) | 81NM (81NM) | 2026-08-23 21:40 UTC | 2026-08-23 22:13 UTC | 32m |
| VKIN16 | VKI | Calgary International Airport (CYYC) | Swift Current Airport (CYYN) | 2026-08-23 21:17 UTC | 2026-08-23 22:11 UTC | 54m |
| N5399K |  | Bolingbrook's Clow International Airport (K1C5) | Morris Municipal/James R Washburn Field (KC09) | 2026-08-23 21:29 UTC | 2026-08-23 22:10 UTC | 40m |
| TGCYE | TGC | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-08-23 21:41 UTC | 2026-08-23 22:10 UTC | 29m |
| N565TA |  | Talkeetna Village Strip (AK44) | Nugget Bench Airport (33AK) | 2026-08-23 21:17 UTC | 2026-08-23 22:08 UTC | 50m |
| CAP424 | CAP | Buchanan Field (KCCR) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-23 21:01 UTC | 2026-08-23 22:06 UTC | 1h 4m |
| QLK571D | QLK | Adelaide International Airport (YPAD) | Whyalla Airport (YWHA) | 2026-08-23 21:23 UTC | 2026-08-23 22:01 UTC | 38m |
| N7757Z |  | Minden-Tahoe Airport (KMEV) | Desert Creek Airport (NV97) | 2026-08-23 21:42 UTC | 2026-08-23 22:01 UTC | 19m |
| CFMCN | CFM | Vancouver International Airport (CYVR) | Big Andy Airport (7WA0) | 2026-08-23 21:37 UTC | 2026-08-23 22:00 UTC | 23m |
| N797MM |  | Boeing Field/King County International Airport (KBFI) | Eureka Municipal Airport (K3W8) | 2026-08-23 19:41 UTC | 2026-08-23 21:57 UTC | 2h 16m |
| AAL2320 | American Airlines | Charlotte/Douglas International Airport (KCLT) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-08-23 20:37 UTC | 2026-08-23 21:57 UTC | 1h 19m |
| N510PR |  | Talkeetna Village Strip (AK44) | Nugget Bench Airport (33AK) | 2026-08-23 21:25 UTC | 2026-08-23 21:55 UTC | 30m |
| EJA974 | EJA | City Of Colorado Springs Municipal Airport (KCOS) | True Grit South Airport (CO95) | 2026-08-23 21:06 UTC | 2026-08-23 21:55 UTC | 49m |
| EJU87YT | EJU | Malpensa International Airport (LIMC) | Santorini Airport (LGSR) | 2026-08-23 19:50 UTC | 2026-08-23 21:54 UTC | 2h 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
