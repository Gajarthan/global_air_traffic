# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_11:46:46_UTC-green)

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

**Latest saved flight:** 2026-08-19 11:46:46 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 11:46:46 UTC

- **215,161** saved flights
- **67,890** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **215,161** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,589,037.0 tonnes** estimated CO2 emissions
- **150,089,104 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8568 |
| 2 | SkyWest Airlines | 7696 |
| 3 | EJA | 4184 |
| 4 | IndiGo | 3677 |
| 5 | American Airlines | 3579 |
| 6 | Southwest Airlines | 3430 |
| 7 | Delta Air Lines | 2767 |
| 8 | ENY | 2660 |
| 9 | LATAM Airlines | 2029 |
| 10 | AZU | 1965 |
| 11 | Vueling | 1808 |
| 12 | Lufthansa | 1800 |
| 13 | WIF | 1725 |
| 14 | LXJ | 1694 |
| 15 | easyJet | 1490 |
| 16 | Swiss International | 1434 |
| 17 | AXM | 1415 |
| 18 | United Airlines | 1362 |
| 19 | QLK | 1346 |
| 20 | EJU | 1332 |
| 21 | Alaska Airlines | 1324 |
| 22 | All Nippon Airways | 1304 |
| 23 | VIV | 1183 |
| 24 | PGT | 1165 |
| 25 | GLO | 1164 |
| 26 | Air France | 1160 |
| 27 | WMT | 1118 |
| 28 | JetBlue | 1091 |
| 29 | Wizz Air | 1088 |
| 30 | AEE | 1082 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 181436 |
| 2 | 🇪🇸 ES | 13774 |
| 3 | 🇧🇷 BR | 12362 |
| 4 | 🇦🇺 AU | 12157 |
| 5 | 🇨🇦 CA | 11862 |
| 6 | 🇮🇳 IN | 11448 |
| 7 | 🇮🇹 IT | 11377 |
| 8 | 🇩🇪 DE | 10643 |
| 9 | 🇬🇧 GB | 10047 |
| 10 | 🇯🇵 JP | 8864 |
| 11 | 🇨🇴 CO | 8745 |
| 12 | 🇫🇷 FR | 8568 |
| 13 | 🇬🇷 GR | 6305 |
| 14 | 🇹🇷 TR | 6172 |
| 15 | 🇲🇽 MX | 6023 |
| 16 | 🇨🇭 CH | 5708 |
| 17 | 🇳🇴 NO | 5346 |
| 18 | 🇲🇾 MY | 3738 |
| 19 | 🇿🇦 ZA | 3650 |
| 20 | 🇵🇱 PL | 3545 |
| 21 | 🇹🇭 TH | 3513 |
| 22 | 🇳🇿 NZ | 2998 |
| 23 | 🇵🇭 PH | 2892 |
| 24 | 🇬🇹 GT | 2732 |
| 25 | 🇰🇷 KR | 2607 |
| 26 | 🇭🇷 HR | 2353 |
| 27 | 🇲🇦 MA | 2166 |
| 28 | 🇳🇱 NL | 1914 |
| 29 | 🇲🇪 ME | 1871 |
| 30 | 🇮🇩 ID | 1810 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4516 |
| 2 | Denver International Airport |  | US | 3508 |
| 3 | Tokyo International Airport |  | JP | 2661 |
| 4 | Indira Gandhi International Airport |  | IN | 2615 |
| 5 | Guaymaral Airport |  | CO | 2561 |
| 6 | Harry Reid International Airport |  | US | 2397 |
| 7 | Zurich Airport |  | CH | 2235 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2212 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2207 |
| 10 | La Aurora Airport |  | GT | 2077 |
| 11 | El Dorado International Airport |  | CO | 1998 |
| 12 | Chicago O'Hare International Airport |  | US | 1979 |
| 13 | Salt Lake City International Airport |  | US | 1900 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1889 |
| 15 | Congonhas Airport |  | BR | 1800 |
| 16 | Frankfurt am Main International Airport |  | DE | 1757 |
| 17 | Madrid Barajas International Airport |  | ES | 1678 |
| 18 | Capua Airport |  | IT | 1636 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1617 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1605 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1575 |
| 22 | Macau International Airport |  | MO | 1562 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1516 |
| 24 | Malpensa International Airport |  | IT | 1507 |
| 25 | Charles de Gaulle International Airport |  | FR | 1479 |
| 26 | Charlotte/Douglas International Airport |  | US | 1443 |
| 27 | Kuala Lumpur International Airport |  | MY | 1376 |
| 28 | Ninoy Aquino International Airport |  | PH | 1373 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1319 |
| 30 | Barcelona International Airport |  | ES | 1317 |
| 31 | Bengaluru International Airport |  | IN | 1313 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1288 |
| 33 | Seattle-Tacoma International Airport |  | US | 1281 |
| 34 | Viracopos International Airport |  | BR | 1256 |
| 35 | Calgary International Airport |  | CA | 1217 |
| 36 | Oslo Gardermoen Airport |  | NO | 1193 |
| 37 | Vitoria/Foronda Airport |  | ES | 1191 |
| 38 | Reno/Tahoe International Airport |  | US | 1164 |
| 39 | Don Mueang International Airport |  | TH | 1161 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1159 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1047 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 769 | 21m | 244 km | 3,238.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 533 | 1h 7m | 770 km | 7,080.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 507 | 24m | 225 km | 1,966.9 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 483 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 458 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 358 | 27m | 275 km | 1,696.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 349 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 316 | 1h 49m | 1,423 km | 7,755.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 315 | 44m | 241 km | 1,308.4 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 282 | 21m | 250 km | 1,218.1 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 268 | 1h 38m | 1,156 km | 5,346.5 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 267 | 19m | 99 km | 457.4 t |
| 19 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 263 | 27m | 215 km | 974.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 254 | 1h 14m | 961 km | 4,210.2 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 254 | 13m | - | - |
| 23 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 251 | 31m | 369 km | 1,597.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 245 | 19m | 144 km | 609.4 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 243 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 231 | 1h 49m | 1,304 km | 5,196.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 30 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 230 | 44m | 555 km | 2,202.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N5128D |  | Lakeland Linder International Airport (KLAL) | Lakeland Linder International Airport (KLAL) | 2026-08-19 11:12 UTC | 2026-08-19 11:46 UTC | 34m |
| N |  | Fazenda Santa Fe Airport (SIWK) | Municipal Bom Futuro Airport (SILC) | 2026-08-19 11:06 UTC | 2026-08-19 11:37 UTC | 30m |
| SXS6EV | SXS | Mollis Airport (LSZM) | Isparta Airport (LTBM) | 2026-08-19 08:45 UTC | 2026-08-19 11:29 UTC | 2h 44m |
| GKCIN | GKC | Denham Aerodrome (EGLD) | Turweston Airport (EGBT) | 2026-08-19 10:55 UTC | 2026-08-19 11:27 UTC | 31m |
| N1545E |  | West Georgia Regional/O V Gray Field (KCTJ) | West Georgia Regional/O V Gray Field (KCTJ) | 2026-08-19 10:37 UTC | 2026-08-19 11:27 UTC | 49m |
| GFOXP | GFO | EG32 (EG32) | EG32 (EG32) | 2026-08-19 11:04 UTC | 2026-08-19 11:24 UTC | 19m |
| RWL4631 | RWL | Monchengladbach Airport (EDLN) | Dortmund Airport (EDLW) | 2026-08-19 09:52 UTC | 2026-08-19 11:17 UTC | 1h 24m |
| AIC2029 | Air India | Indira Gandhi International Airport (VIDP) | Das Island Airport (OMAS) | 2026-08-19 08:16 UTC | 2026-08-19 11:15 UTC | 2h 59m |
| PSVTT | PSV | Campo de Marte Airport (SBMT) | Catanduva Airport (SDCD) | 2026-08-19 10:21 UTC | 2026-08-19 11:14 UTC | 53m |
| N4CH |  | Wiley Post Airport (KPWA) | 0AR1 (0AR1) | 2026-08-19 10:41 UTC | 2026-08-19 11:14 UTC | 32m |
| VOZ236 | Virgin Australia | Adelaide International Airport (YPAD) | Melbourne International Airport (YMML) | 2026-08-19 09:38 UTC | 2026-08-19 11:14 UTC | 1h 35m |
| PSNFC | PSN | Joao Moteiro Airport (SIVU) | Fazenda Ideal Airport (SJWU) | 2026-08-19 10:40 UTC | 2026-08-19 11:11 UTC | 31m |
| GCLEV | GCL | Wroughton Airfield (EGDT) | Wroughton Airfield (EGDT) | 2026-08-19 10:47 UTC | 2026-08-19 11:11 UTC | 24m |
| AIC157 | Air India | Indira Gandhi International Airport (VIDP) | Das Island Airport (OMAS) | 2026-08-19 08:10 UTC | 2026-08-19 11:11 UTC | 3h 0m |
| JZR262 | JZR | Beirut Rafic Hariri International Airport (OLBA) | Das Island Airport (OMAS) | 2026-08-19 06:32 UTC | 2026-08-19 11:10 UTC | 4h 38m |
| PPCOD | PPC | Eurico de Aguiar Salles Airport (SBVT) | Bartolomeu Lisandro Airport (SBCP) | 2026-08-19 10:43 UTC | 2026-08-19 11:07 UTC | 23m |
| CPA805 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Zhuhai Airport (ZGSD) | 2026-08-18 20:54 UTC | 2026-08-19 11:05 UTC | 14h 10m |
| RYR8XK | Ryanair | Bologna / Borgo Panigale Airport (LIPE) | Crotone Airport (LIBC) | 2026-08-19 09:57 UTC | 2026-08-19 11:03 UTC | 1h 6m |
| WIF5WP | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-08-19 10:51 UTC | 2026-08-19 11:03 UTC | 11m |
| UFX31 | UFX | RAF Woodvale (EGOW) | Blackpool International Airport (EGNH) | 2026-08-19 10:33 UTC | 2026-08-19 11:02 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
