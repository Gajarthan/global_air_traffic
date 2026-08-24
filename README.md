# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_22:32:34_UTC-green)

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

**Latest saved flight:** 2026-08-24 22:32:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 22:32:34 UTC

- **233,635** saved flights
- **71,735** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **233,635** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,815,503.2 tonnes** estimated CO2 emissions
- **163,217,575 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9382 |
| 2 | SkyWest Airlines | 8277 |
| 3 | EJA | 4544 |
| 4 | IndiGo | 3943 |
| 5 | American Airlines | 3812 |
| 6 | Southwest Airlines | 3591 |
| 7 | Delta Air Lines | 2983 |
| 8 | ENY | 2848 |
| 9 | LATAM Airlines | 2245 |
| 10 | AZU | 2177 |
| 11 | Vueling | 1998 |
| 12 | Lufthansa | 1901 |
| 13 | WIF | 1856 |
| 14 | LXJ | 1842 |
| 15 | easyJet | 1632 |
| 16 | Swiss International | 1565 |
| 17 | AXM | 1551 |
| 18 | EJU | 1495 |
| 19 | United Airlines | 1481 |
| 20 | QLK | 1477 |
| 21 | Alaska Airlines | 1406 |
| 22 | All Nippon Airways | 1386 |
| 23 | GLO | 1304 |
| 24 | WMT | 1297 |
| 25 | VIV | 1285 |
| 26 | PGT | 1274 |
| 27 | Air France | 1268 |
| 28 | Wizz Air | 1234 |
| 29 | AEE | 1161 |
| 30 | JetBlue | 1161 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 194611 |
| 2 | 🇪🇸 ES | 15005 |
| 3 | 🇧🇷 BR | 13654 |
| 4 | 🇦🇺 AU | 13176 |
| 5 | 🇨🇦 CA | 12912 |
| 6 | 🇮🇹 IT | 12704 |
| 7 | 🇮🇳 IN | 12281 |
| 8 | 🇩🇪 DE | 11507 |
| 9 | 🇬🇧 GB | 11011 |
| 10 | 🇨🇴 CO | 9810 |
| 11 | 🇯🇵 JP | 9448 |
| 12 | 🇫🇷 FR | 9344 |
| 13 | 🇹🇷 TR | 6921 |
| 14 | 🇬🇷 GR | 6872 |
| 15 | 🇲🇽 MX | 6491 |
| 16 | 🇨🇭 CH | 6225 |
| 17 | 🇳🇴 NO | 5770 |
| 18 | 🇲🇾 MY | 4144 |
| 19 | 🇹🇭 TH | 4108 |
| 20 | 🇿🇦 ZA | 4071 |
| 21 | 🇵🇱 PL | 3891 |
| 22 | 🇳🇿 NZ | 3214 |
| 23 | 🇵🇭 PH | 3188 |
| 24 | 🇬🇹 GT | 2929 |
| 25 | 🇰🇷 KR | 2726 |
| 26 | 🇭🇷 HR | 2686 |
| 27 | 🇲🇦 MA | 2372 |
| 28 | 🇲🇪 ME | 2155 |
| 29 | 🇳🇱 NL | 2092 |
| 30 | 🇮🇩 ID | 2015 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4863 |
| 2 | Denver International Airport |  | US | 3791 |
| 3 | Indira Gandhi International Airport |  | IN | 2844 |
| 4 | Tokyo International Airport |  | JP | 2818 |
| 5 | Guaymaral Airport |  | CO | 2677 |
| 6 | Harry Reid International Airport |  | US | 2507 |
| 7 | Zurich Airport |  | CH | 2442 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2390 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2343 |
| 10 | La Aurora Airport |  | GT | 2232 |
| 11 | El Dorado International Airport |  | CO | 2185 |
| 12 | Chicago O'Hare International Airport |  | US | 2114 |
| 13 | Salt Lake City International Airport |  | US | 2060 |
| 14 | Congonhas Airport |  | BR | 1994 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1968 |
| 16 | Frankfurt am Main International Airport |  | DE | 1863 |
| 17 | Capua Airport |  | IT | 1840 |
| 18 | Madrid Barajas International Airport |  | ES | 1835 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1757 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1730 |
| 21 | Malpensa International Airport |  | IT | 1674 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1663 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1636 |
| 24 | Charles de Gaulle International Airport |  | FR | 1621 |
| 25 | Macau International Airport |  | MO | 1605 |
| 26 | Ninoy Aquino International Airport |  | PH | 1537 |
| 27 | Charlotte/Douglas International Airport |  | US | 1514 |
| 28 | Kuala Lumpur International Airport |  | MY | 1498 |
| 29 | Barcelona International Airport |  | ES | 1475 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1439 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1412 |
| 32 | Viracopos International Airport |  | BR | 1391 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1373 |
| 34 | Bengaluru International Airport |  | IN | 1372 |
| 35 | Seattle-Tacoma International Airport |  | US | 1369 |
| 36 | Don Mueang International Airport |  | TH | 1339 |
| 37 | Calgary International Airport |  | CA | 1335 |
| 38 | Oslo Gardermoen Airport |  | NO | 1307 |
| 39 | Vancouver International Airport |  | CA | 1271 |
| 40 | Vitoria/Foronda Airport |  | ES | 1266 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1085 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 852 | 21m | 244 km | 3,587.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 586 | 1h 6m | 770 km | 7,784.6 t |
| 4 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 582 | 8m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 581 | 24m | 225 km | 2,254.0 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 522 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 385 | 27m | 275 km | 1,824.4 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 361 | 1h 50m | 1,423 km | 8,859.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 359 | 35m | - | - |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 339 | 44m | 241 km | 1,408.1 t |
| 11 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 327 | 44m | 555 km | 3,131.2 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 327 | 21m | 250 km | 1,412.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 310 | 24m | 218 km | 1,167.9 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 306 | 1h 38m | 1,156 km | 6,104.6 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 289 | 19m | 99 km | 495.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 285 | 27m | 215 km | 1,055.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 272 | 1h 14m | 961 km | 4,508.5 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 271 | 13m | - | - |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 266 | 29m | 304 km | 1,394.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 266 | 19m | 144 km | 661.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 251 | 15m | 154 km | 665.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 250 | 1h 50m | 1,304 km | 5,624.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1885M |  | Wasilla Airport (PAWS) | Ted Stevens Anchorage International Airport (PANC) | 2026-08-24 22:13 UTC | 2026-08-24 22:32 UTC | 18m |
| N541GP |  | William P Hobby Airport (KHOU) | Easterwood Field (KCLL) | 2026-08-24 21:51 UTC | 2026-08-24 22:23 UTC | 32m |
| YGN | YGN | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-08-24 21:40 UTC | 2026-08-24 22:19 UTC | 39m |
| TVF972N | TVF | Paris-Orly Airport (LFPO) | DAAX (DAAX) | 2026-08-24 20:27 UTC | 2026-08-24 22:15 UTC | 1h 47m |
| N54466 |  | Somerset Airport (KSMQ) | Sky Manor Airport (KN40) | 2026-08-24 21:48 UTC | 2026-08-24 22:11 UTC | 23m |
| N7354X |  | Chorman Airport (KD74) | Dover Afb Airport (KDOV) | 2026-08-24 21:14 UTC | 2026-08-24 22:09 UTC | 55m |
| GIZMO31 | GIZ | Enid Woodring Regional Airport (KWDG) | Ramey 1 Airport (0OK8) | 2026-08-24 21:49 UTC | 2026-08-24 22:06 UTC | 16m |
| N684TH |  | Jonesboro Municipal Airport (KJBR) | OVER (OVER) | 2026-08-24 21:45 UTC | 2026-08-24 22:05 UTC | 20m |
| TAUNT21 | TAU | Cottonwood Airport (OK66) | Miller Brothers Airport (OK47) | 2026-08-24 21:47 UTC | 2026-08-24 22:02 UTC | 15m |
| N18JA |  | Aurora Municipal Airport (KARR) | De Kalb Taylor Municipal Airport (KDKB) | 2026-08-24 21:51 UTC | 2026-08-24 22:00 UTC | 9m |
| N3921Q |  | Fletcher Field (2MO0) | Miami County Airport (KK81) | 2026-08-24 21:29 UTC | 2026-08-24 21:59 UTC | 29m |
| AMMO84 | AMM | Edwards Af Aux North Base Airport (K9L2) | Edwards Af Aux North Base Airport (K9L2) | 2026-08-24 21:43 UTC | 2026-08-24 21:57 UTC | 14m |
| N8026N |  | Bloomsburg Municipal Airport (KN13) | Wings Field (KLOM) | 2026-08-24 21:10 UTC | 2026-08-24 21:57 UTC | 47m |
| N858AU |  | Dupage Airport (KDPA) | IS80 (IS80) | 2026-08-24 21:37 UTC | 2026-08-24 21:53 UTC | 16m |
| EJA833 | EJA | Burke Lakefront Airport (KBKL) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-24 21:17 UTC | 2026-08-24 21:52 UTC | 35m |
| TOGO21 | TOG | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-08-24 21:15 UTC | 2026-08-24 21:51 UTC | 35m |
| N945RF |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-24 21:38 UTC | 2026-08-24 21:50 UTC | 12m |
| GRYDR17 | GRY | Frederick Douglass/Greater Rochester International Airport (KROC) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-08-24 21:26 UTC | 2026-08-24 21:48 UTC | 21m |
| N850CS |  | College Park Airport (KCGS) | Roscoe Turner Airport (KCRX) | 2026-08-24 19:21 UTC | 2026-08-24 21:47 UTC | 2h 26m |
| 1881 |  | Cildir Airport (LTBD) | Cildir Airport (LTBD) | 2026-08-24 20:43 UTC | 2026-08-24 21:43 UTC | 1h 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
