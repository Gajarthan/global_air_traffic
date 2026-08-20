# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_07:41:38_UTC-green)

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

**Latest saved flight:** 2026-08-20 07:41:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 07:41:38 UTC

- **218,477** saved flights
- **68,748** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **218,477** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,629,256.9 tonnes** estimated CO2 emissions
- **152,420,691 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8746 |
| 2 | SkyWest Airlines | 7813 |
| 3 | EJA | 4247 |
| 4 | IndiGo | 3707 |
| 5 | American Airlines | 3636 |
| 6 | Southwest Airlines | 3470 |
| 7 | Delta Air Lines | 2822 |
| 8 | ENY | 2698 |
| 9 | LATAM Airlines | 2069 |
| 10 | AZU | 2002 |
| 11 | Vueling | 1832 |
| 12 | Lufthansa | 1814 |
| 13 | WIF | 1745 |
| 14 | LXJ | 1728 |
| 15 | easyJet | 1511 |
| 16 | Swiss International | 1451 |
| 17 | AXM | 1429 |
| 18 | United Airlines | 1382 |
| 19 | QLK | 1372 |
| 20 | EJU | 1360 |
| 21 | Alaska Airlines | 1339 |
| 22 | All Nippon Airways | 1316 |
| 23 | VIV | 1196 |
| 24 | GLO | 1187 |
| 25 | PGT | 1182 |
| 26 | Air France | 1178 |
| 27 | WMT | 1146 |
| 28 | JetBlue | 1112 |
| 29 | Wizz Air | 1109 |
| 30 | AEE | 1093 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 184164 |
| 2 | 🇪🇸 ES | 13971 |
| 3 | 🇧🇷 BR | 12597 |
| 4 | 🇦🇺 AU | 12376 |
| 5 | 🇨🇦 CA | 12065 |
| 6 | 🇮🇹 IT | 11609 |
| 7 | 🇮🇳 IN | 11543 |
| 8 | 🇩🇪 DE | 10778 |
| 9 | 🇬🇧 GB | 10224 |
| 10 | 🇨🇴 CO | 8981 |
| 11 | 🇯🇵 JP | 8931 |
| 12 | 🇫🇷 FR | 8683 |
| 13 | 🇬🇷 GR | 6363 |
| 14 | 🇹🇷 TR | 6282 |
| 15 | 🇲🇽 MX | 6095 |
| 16 | 🇨🇭 CH | 5784 |
| 17 | 🇳🇴 NO | 5421 |
| 18 | 🇲🇾 MY | 3778 |
| 19 | 🇿🇦 ZA | 3699 |
| 20 | 🇵🇱 PL | 3610 |
| 21 | 🇹🇭 TH | 3592 |
| 22 | 🇳🇿 NZ | 3041 |
| 23 | 🇵🇭 PH | 2941 |
| 24 | 🇬🇹 GT | 2767 |
| 25 | 🇰🇷 KR | 2626 |
| 26 | 🇭🇷 HR | 2394 |
| 27 | 🇲🇦 MA | 2191 |
| 28 | 🇳🇱 NL | 1941 |
| 29 | 🇲🇪 ME | 1917 |
| 30 | 🇮🇩 ID | 1850 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4591 |
| 2 | Denver International Airport |  | US | 3576 |
| 3 | Tokyo International Airport |  | JP | 2682 |
| 4 | Indira Gandhi International Airport |  | IN | 2647 |
| 5 | Guaymaral Airport |  | CO | 2595 |
| 6 | Harry Reid International Airport |  | US | 2416 |
| 7 | Zurich Airport |  | CH | 2263 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2245 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2217 |
| 10 | La Aurora Airport |  | GT | 2106 |
| 11 | El Dorado International Airport |  | CO | 2053 |
| 12 | Chicago O'Hare International Airport |  | US | 2007 |
| 13 | Salt Lake City International Airport |  | US | 1931 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1900 |
| 15 | Congonhas Airport |  | BR | 1840 |
| 16 | Frankfurt am Main International Airport |  | DE | 1780 |
| 17 | Madrid Barajas International Airport |  | ES | 1708 |
| 18 | Capua Airport |  | IT | 1662 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1643 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1618 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1604 |
| 22 | Macau International Airport |  | MO | 1566 |
| 23 | Malpensa International Airport |  | IT | 1540 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1538 |
| 25 | Charles de Gaulle International Airport |  | FR | 1494 |
| 26 | Charlotte/Douglas International Airport |  | US | 1462 |
| 27 | Ninoy Aquino International Airport |  | PH | 1397 |
| 28 | Kuala Lumpur International Airport |  | MY | 1389 |
| 29 | Barcelona International Airport |  | ES | 1336 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1331 |
| 31 | Bengaluru International Airport |  | IN | 1317 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1306 |
| 33 | Seattle-Tacoma International Airport |  | US | 1299 |
| 34 | Viracopos International Airport |  | BR | 1278 |
| 35 | Calgary International Airport |  | CA | 1234 |
| 36 | Oslo Gardermoen Airport |  | NO | 1209 |
| 37 | Vitoria/Foronda Airport |  | ES | 1208 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1201 |
| 39 | Don Mueang International Airport |  | TH | 1186 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1174 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 785 | 21m | 244 km | 3,305.4 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 541 | 1h 7m | 770 km | 7,186.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 518 | 24m | 225 km | 2,009.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 493 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 485 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 365 | 27m | 275 km | 1,729.6 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 321 | 1h 50m | 1,423 km | 7,877.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 319 | 44m | 241 km | 1,325.1 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 311 | 1h 7m | 706 km | 3,786.4 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 294 | 22m | 55 km | 279.4 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 286 | 21m | 250 km | 1,235.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 273 | 1h 38m | 1,156 km | 5,446.2 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 268 | 27m | 215 km | 992.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 268 | 24m | 218 km | 1,009.7 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 260 | 13m | - | - |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 258 | 1h 14m | 961 km | 4,276.5 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 247 | 19m | 144 km | 614.4 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 246 | 12m | - | - |
| 27 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 240 | 44m | 555 km | 2,298.1 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 236 | 1h 49m | 1,304 km | 5,309.4 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FNY55D5 | FNY | Landivisiau Air Base (LFRJ) | La Roche-sur-Yon Airport (LFRI) | 2026-08-20 07:17 UTC | 2026-08-20 07:41 UTC | 24m |
| PR24 |  | Karup Airport (EKKA) | Billund Airport (EKBI) | 2026-08-20 07:18 UTC | 2026-08-20 07:41 UTC | 22m |
| SWR138 | Swiss International | Zurich Airport (LSZH) | Zhuhai Airport (ZGSD) | 2026-08-19 20:49 UTC | 2026-08-20 07:27 UTC | 10h 37m |
| SJX841 | SJX | Fukuoka Airport (RJFF) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-20 05:37 UTC | 2026-08-20 07:25 UTC | 1h 48m |
| WLT | WLT | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-08-20 06:49 UTC | 2026-08-20 07:17 UTC | 27m |
| ECODU | ECO | Valencia Airport (LEVC) | Altarejos-Guadalcanal Airport (LEGC) | 2026-08-20 06:33 UTC | 2026-08-20 07:16 UTC | 42m |
| TTW201 | TTW | Narita International Airport (RJAA) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-20 04:23 UTC | 2026-08-20 07:14 UTC | 2h 51m |
| ANE30KP | ANE | Madrid Barajas International Airport (LEMD) | Federico Garcia Lorca Airport (LEGR) | 2026-08-20 06:31 UTC | 2026-08-20 07:12 UTC | 40m |
| QLK11D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-08-20 06:45 UTC | 2026-08-20 07:07 UTC | 22m |
| RYR53BM | Ryanair | Grazzanise Airport (LIRM) | Wethersfield Airport (EGVT) | 2026-08-20 04:41 UTC | 2026-08-20 07:04 UTC | 2h 22m |
| IOR50310 | IOR | Reus Air Base (LERS) | Castellon-Costa Azahar Airport (LEDS) | 2026-08-20 06:40 UTC | 2026-08-20 07:02 UTC | 22m |
| FD264 |  | Sydney Bankstown Airport (YSBK) | Bathurst Airport (YBTH) | 2026-08-20 06:40 UTC | 2026-08-20 07:02 UTC | 22m |
| SAS48V | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Aarhus Airport (EKAH) | 2026-08-20 06:38 UTC | 2026-08-20 07:02 UTC | 24m |
| IGO7HC | IndiGo | Bengaluru International Airport (VOBL) | Kovilpatti Airport (VO26) | 2026-08-20 05:53 UTC | 2026-08-20 07:01 UTC | 1h 7m |
| BAW31 | British Airways | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-08-19 19:49 UTC | 2026-08-20 07:00 UTC | 11h 11m |
| AIQ3358 | AIQ | Don Mueang International Airport (VTBD) | Khon Kaen Airport (VTUK) | 2026-08-20 06:19 UTC | 2026-08-20 06:59 UTC | 39m |
| WIF4X | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-20 06:25 UTC | 2026-08-20 06:57 UTC | 32m |
| R20653 |  | Lakloey Air Park (AK22) | Ladd Army Air Field (PAFB) | 2026-08-20 05:52 UTC | 2026-08-20 06:55 UTC | 1h 2m |
| JAL2737 | Japan Airlines | Okadama Airport (RJCO) | Nakashibetsu Airport (RJCN) | 2026-08-20 06:15 UTC | 2026-08-20 06:54 UTC | 38m |
| SDG234 | SDG | Hindon Airport (VIDX) | Shimla Airport (VISM) | 2026-08-20 06:24 UTC | 2026-08-20 06:52 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
