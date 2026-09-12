# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--12_15:58:41_UTC-green)

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

**Latest saved flight:** 2026-09-12 15:58:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-12 15:58:41 UTC

- **256,192** saved flights
- **76,380** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **256,192** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,095,248.8 tonnes** estimated CO2 emissions
- **179,434,715 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10197 |
| 2 | SkyWest Airlines | 8923 |
| 3 | EJA | 4944 |
| 4 | IndiGo | 4298 |
| 5 | American Airlines | 4056 |
| 6 | Southwest Airlines | 3768 |
| 7 | Delta Air Lines | 3204 |
| 8 | ENY | 3041 |
| 9 | LATAM Airlines | 2467 |
| 10 | AZU | 2386 |
| 11 | Vueling | 2167 |
| 12 | WIF | 2055 |
| 13 | Lufthansa | 2007 |
| 14 | LXJ | 1998 |
| 15 | easyJet | 1746 |
| 16 | Swiss International | 1718 |
| 17 | QLK | 1653 |
| 18 | AXM | 1642 |
| 19 | EJU | 1634 |
| 20 | United Airlines | 1587 |
| 21 | Alaska Airlines | 1522 |
| 22 | All Nippon Airways | 1493 |
| 23 | WMT | 1450 |
| 24 | GLO | 1430 |
| 25 | PGT | 1411 |
| 26 | VIV | 1402 |
| 27 | Air France | 1397 |
| 28 | Wizz Air | 1392 |
| 29 | TKR | 1247 |
| 30 | JetBlue | 1244 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 212631 |
| 2 | 🇪🇸 ES | 16281 |
| 3 | 🇧🇷 BR | 14956 |
| 4 | 🇦🇺 AU | 14613 |
| 5 | 🇨🇦 CA | 14265 |
| 6 | 🇮🇹 IT | 14000 |
| 7 | 🇮🇳 IN | 13467 |
| 8 | 🇩🇪 DE | 12502 |
| 9 | 🇬🇧 GB | 11955 |
| 10 | 🇨🇴 CO | 11423 |
| 11 | 🇫🇷 FR | 10296 |
| 12 | 🇯🇵 JP | 10017 |
| 13 | 🇹🇷 TR | 7687 |
| 14 | 🇬🇷 GR | 7473 |
| 15 | 🇲🇽 MX | 7071 |
| 16 | 🇨🇭 CH | 6885 |
| 17 | 🇳🇴 NO | 6347 |
| 18 | 🇹🇭 TH | 4613 |
| 19 | 🇲🇾 MY | 4415 |
| 20 | 🇿🇦 ZA | 4362 |
| 21 | 🇵🇱 PL | 4251 |
| 22 | 🇳🇿 NZ | 3537 |
| 23 | 🇵🇭 PH | 3446 |
| 24 | 🇬🇹 GT | 3227 |
| 25 | 🇰🇷 KR | 2938 |
| 26 | 🇭🇷 HR | 2938 |
| 27 | 🇲🇦 MA | 2580 |
| 28 | 🇲🇪 ME | 2410 |
| 29 | 🇳🇱 NL | 2311 |
| 30 | 🇮🇩 ID | 2178 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5251 |
| 2 | Denver International Airport |  | US | 4137 |
| 3 | Indira Gandhi International Airport |  | IN | 3100 |
| 4 | Tokyo International Airport |  | JP | 2991 |
| 5 | Guaymaral Airport |  | CO | 2759 |
| 6 | Harry Reid International Airport |  | US | 2713 |
| 7 | Zurich Airport |  | CH | 2684 |
| 8 | El Dorado International Airport |  | CO | 2647 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2581 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2507 |
| 11 | La Aurora Airport |  | GT | 2453 |
| 12 | Salt Lake City International Airport |  | US | 2258 |
| 13 | Chicago O'Hare International Airport |  | US | 2228 |
| 14 | Congonhas Airport |  | BR | 2197 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2092 |
| 16 | Capua Airport |  | IT | 2016 |
| 17 | Madrid Barajas International Airport |  | ES | 2000 |
| 18 | Frankfurt am Main International Airport |  | DE | 1979 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1924 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1852 |
| 21 | Malpensa International Airport |  | IT | 1845 |
| 22 | Charles de Gaulle International Airport |  | FR | 1802 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1799 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1779 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1727 |
| 26 | Macau International Airport |  | MO | 1698 |
| 27 | Ninoy Aquino International Airport |  | PH | 1685 |
| 28 | Barcelona International Airport |  | ES | 1611 |
| 29 | Charlotte/Douglas International Airport |  | US | 1603 |
| 30 | Kuala Lumpur International Airport |  | MY | 1588 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1571 |
| 32 | Viracopos International Airport |  | BR | 1530 |
| 33 | Seattle-Tacoma International Airport |  | US | 1501 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1488 |
| 35 | Don Mueang International Airport |  | TH | 1475 |
| 36 | Calgary International Airport |  | CA | 1470 |
| 37 | Bengaluru International Airport |  | IN | 1456 |
| 38 | Oslo Gardermoen Airport |  | NO | 1449 |
| 39 | Vancouver International Airport |  | CA | 1438 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1385 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 954 | 21m | 244 km | 4,017.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 686 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 643 | 1h 6m | 770 km | 8,541.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 640 | 24m | 225 km | 2,482.9 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 573 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 418 | 27m | 275 km | 1,980.7 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 412 | 44m | 555 km | 3,945.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 407 | 1h 50m | 1,423 km | 9,988.4 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 387 | 44m | 241 km | 1,607.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 358 | 24m | 218 km | 1,348.7 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 355 | 21m | 250 km | 1,533.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 343 | 23m | 55 km | 326.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 325 | 1h 6m | 706 km | 3,956.9 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 317 | 19m | 99 km | 543.0 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 316 | 26m | 215 km | 1,170.3 t |
| 19 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 309 | 12m | - | - |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 304 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 294 | 1h 14m | 961 km | 4,873.2 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 293 | 19m | 144 km | 728.8 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 275 | 1h 50m | 1,304 km | 6,186.8 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 27 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 269 | 41m | 535 km | 2,484.4 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 266 | 28m | 152 km | 695.2 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CGOEB | CGO | Weyburn Airport (CJE3) | Regina International Airport (CYQR) | 2026-09-12 15:43 UTC | 2026-09-12 15:58 UTC | 14m |
| N1910R |  | MHLE (MHLE) | La Aurora Airport (MGGT) | 2026-09-12 15:21 UTC | 2026-09-12 15:56 UTC | 35m |
| N16SE |  | FA44 (FA44) | Pompano Beach Airpark (KPMP) | 2026-09-12 15:40 UTC | 2026-09-12 15:54 UTC | 13m |
| PAT767 | PAT | Fort Worth Nas Jrb (Carswell Field) Airport (KNFW) | Grant Besley Airport (NM03) | 2026-09-12 14:52 UTC | 2026-09-12 15:51 UTC | 58m |
| N251ME |  | KFTG (KFTG) | Central Colorado Regional Airport (KAEJ) | 2026-09-12 14:49 UTC | 2026-09-12 15:50 UTC | 1h 1m |
| CKS221 | CKS | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-09-12 04:57 UTC | 2026-09-12 15:48 UTC | 10h 51m |
| N543TH |  | Trenton Mercer Airport (KTTN) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-09-12 15:09 UTC | 2026-09-12 15:48 UTC | 38m |
| THY6650 | Turkish Airlines | Queen Alia International Airport (OJAI) | Zhuhai Airport (ZGSD) | 2026-09-12 05:29 UTC | 2026-09-12 15:47 UTC | 10h 17m |
| N682AC |  | Hidden Valley Ranch Airport (TS90) | Bb Airpark (TE88) | 2026-09-12 14:53 UTC | 2026-09-12 15:46 UTC | 53m |
| N611SG |  | KU77 (KU77) | Nephi Municipal Airport (KU14) | 2026-09-12 15:13 UTC | 2026-09-12 15:43 UTC | 29m |
| VPCPM | VPC | Al Bateen Executive Airport (OMAD) | Zhuhai Airport (ZGSD) | 2026-09-12 07:50 UTC | 2026-09-12 15:43 UTC | 7h 52m |
| N404TD |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-09-12 14:05 UTC | 2026-09-12 15:40 UTC | 1h 34m |
| N165AR |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-09-12 14:09 UTC | 2026-09-12 15:38 UTC | 1h 29m |
| N972FB |  | Scottsdale Airport (KSDL) | True Grit South Airport (CO95) | 2026-09-12 14:45 UTC | 2026-09-12 15:37 UTC | 52m |
| N842EB |  | Sebastian Municipal Airport (KX26) | Sebastian Municipal Airport (KX26) | 2026-09-12 15:17 UTC | 2026-09-12 15:36 UTC | 19m |
| N701HS |  | Shady Cove Airpark (OG31) | Beagle Sky Ranch Airport (OR96) | 2026-09-12 15:22 UTC | 2026-09-12 15:35 UTC | 12m |
| N40798 |  | Van Nuys Airport (KVNY) | Meadows Field (KBFL) | 2026-09-12 14:38 UTC | 2026-09-12 15:32 UTC | 54m |
| CAP1931 | CAP | Claremont Municipal Airport (KCNH) | Lebanon Municipal Airport (KLEB) | 2026-09-12 15:23 UTC | 2026-09-12 15:31 UTC | 7m |
| N415AM |  | Downey/Hyde Memorial/ Airport (KU58) | Simko Field (1ID9) | 2026-09-12 15:13 UTC | 2026-09-12 15:31 UTC | 17m |
| N777ZA |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-09-12 14:08 UTC | 2026-09-12 15:31 UTC | 1h 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
