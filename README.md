# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_07:02:55_UTC-green)

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

**Latest saved flight:** 2026-08-20 07:02:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 07:02:55 UTC

- **218,399** saved flights
- **68,733** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **218,399** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,628,222.7 tonnes** estimated CO2 emissions
- **152,360,737 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8737 |
| 2 | SkyWest Airlines | 7813 |
| 3 | EJA | 4247 |
| 4 | IndiGo | 3704 |
| 5 | American Airlines | 3636 |
| 6 | Southwest Airlines | 3470 |
| 7 | Delta Air Lines | 2822 |
| 8 | ENY | 2698 |
| 9 | LATAM Airlines | 2069 |
| 10 | AZU | 2002 |
| 11 | Vueling | 1832 |
| 12 | Lufthansa | 1814 |
| 13 | WIF | 1744 |
| 14 | LXJ | 1728 |
| 15 | easyJet | 1511 |
| 16 | Swiss International | 1450 |
| 17 | AXM | 1427 |
| 18 | United Airlines | 1382 |
| 19 | QLK | 1369 |
| 20 | EJU | 1359 |
| 21 | Alaska Airlines | 1339 |
| 22 | All Nippon Airways | 1316 |
| 23 | VIV | 1196 |
| 24 | GLO | 1187 |
| 25 | PGT | 1181 |
| 26 | Air France | 1178 |
| 27 | WMT | 1146 |
| 28 | JetBlue | 1112 |
| 29 | Wizz Air | 1107 |
| 30 | AEE | 1093 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 184164 |
| 2 | 🇪🇸 ES | 13963 |
| 3 | 🇧🇷 BR | 12597 |
| 4 | 🇦🇺 AU | 12356 |
| 5 | 🇨🇦 CA | 12061 |
| 6 | 🇮🇹 IT | 11603 |
| 7 | 🇮🇳 IN | 11535 |
| 8 | 🇩🇪 DE | 10776 |
| 9 | 🇬🇧 GB | 10219 |
| 10 | 🇨🇴 CO | 8981 |
| 11 | 🇯🇵 JP | 8925 |
| 12 | 🇫🇷 FR | 8675 |
| 13 | 🇬🇷 GR | 6362 |
| 14 | 🇹🇷 TR | 6276 |
| 15 | 🇲🇽 MX | 6095 |
| 16 | 🇨🇭 CH | 5779 |
| 17 | 🇳🇴 NO | 5417 |
| 18 | 🇲🇾 MY | 3772 |
| 19 | 🇿🇦 ZA | 3695 |
| 20 | 🇵🇱 PL | 3605 |
| 21 | 🇹🇭 TH | 3586 |
| 22 | 🇳🇿 NZ | 3041 |
| 23 | 🇵🇭 PH | 2931 |
| 24 | 🇬🇹 GT | 2767 |
| 25 | 🇰🇷 KR | 2626 |
| 26 | 🇭🇷 HR | 2393 |
| 27 | 🇲🇦 MA | 2189 |
| 28 | 🇳🇱 NL | 1941 |
| 29 | 🇲🇪 ME | 1915 |
| 30 | 🇮🇩 ID | 1847 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4591 |
| 2 | Denver International Airport |  | US | 3576 |
| 3 | Tokyo International Airport |  | JP | 2681 |
| 4 | Indira Gandhi International Airport |  | IN | 2645 |
| 5 | Guaymaral Airport |  | CO | 2595 |
| 6 | Harry Reid International Airport |  | US | 2416 |
| 7 | Zurich Airport |  | CH | 2261 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2245 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2217 |
| 10 | La Aurora Airport |  | GT | 2106 |
| 11 | El Dorado International Airport |  | CO | 2053 |
| 12 | Chicago O'Hare International Airport |  | US | 2007 |
| 13 | Salt Lake City International Airport |  | US | 1931 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1900 |
| 15 | Congonhas Airport |  | BR | 1840 |
| 16 | Frankfurt am Main International Airport |  | DE | 1780 |
| 17 | Madrid Barajas International Airport |  | ES | 1705 |
| 18 | Capua Airport |  | IT | 1662 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1643 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1618 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1604 |
| 22 | Macau International Airport |  | MO | 1566 |
| 23 | Malpensa International Airport |  | IT | 1540 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1536 |
| 25 | Charles de Gaulle International Airport |  | FR | 1494 |
| 26 | Charlotte/Douglas International Airport |  | US | 1462 |
| 27 | Ninoy Aquino International Airport |  | PH | 1392 |
| 28 | Kuala Lumpur International Airport |  | MY | 1388 |
| 29 | Barcelona International Airport |  | ES | 1336 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1331 |
| 31 | Bengaluru International Airport |  | IN | 1316 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1306 |
| 33 | Seattle-Tacoma International Airport |  | US | 1299 |
| 34 | Viracopos International Airport |  | BR | 1278 |
| 35 | Calgary International Airport |  | CA | 1234 |
| 36 | Oslo Gardermoen Airport |  | NO | 1208 |
| 37 | Vitoria/Foronda Airport |  | ES | 1207 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1201 |
| 39 | Don Mueang International Airport |  | TH | 1184 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1174 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 785 | 21m | 244 km | 3,305.4 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 540 | 1h 7m | 770 km | 7,173.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 516 | 24m | 225 km | 2,001.8 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 493 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 485 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 364 | 27m | 275 km | 1,724.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 321 | 1h 50m | 1,423 km | 7,877.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 318 | 44m | 241 km | 1,320.9 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 311 | 1h 7m | 706 km | 3,786.4 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 294 | 22m | 55 km | 279.4 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 285 | 21m | 250 km | 1,231.0 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 272 | 1h 38m | 1,156 km | 5,426.3 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 268 | 27m | 215 km | 992.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 268 | 24m | 218 km | 1,009.7 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 260 | 13m | - | - |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 258 | 31m | 369 km | 1,642.2 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 258 | 1h 14m | 961 km | 4,276.5 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 247 | 19m | 144 km | 614.4 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 246 | 12m | - | - |
| 27 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 239 | 44m | 555 km | 2,288.5 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 236 | 1h 49m | 1,304 km | 5,309.4 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IOR50310 | IOR | Reus Air Base (LERS) | Castellon-Costa Azahar Airport (LEDS) | 2026-08-20 06:40 UTC | 2026-08-20 07:02 UTC | 22m |
| BAW31 | British Airways | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-08-19 19:49 UTC | 2026-08-20 07:00 UTC | 11h 11m |
| R20653 |  | Lakloey Air Park (AK22) | Ladd Army Air Field (PAFB) | 2026-08-20 05:52 UTC | 2026-08-20 06:55 UTC | 1h 2m |
| ICY52 | ICY | Highland Airport (47AK) | Elmendorf Afb Airport (PAED) | 2026-08-20 05:58 UTC | 2026-08-20 06:50 UTC | 52m |
| N191TX |  | Mckinney Ntl Airport (KTKI) | Mckinney Ntl Airport (KTKI) | 2026-08-20 04:53 UTC | 2026-08-20 06:45 UTC | 1h 52m |
| CARD51 | CAR | A 511 Airport (RKSG) | Incheon International Airport (RKSI) | 2026-08-20 06:14 UTC | 2026-08-20 06:40 UTC | 26m |
| ETD925 | Etihad Airways | Abu Dhabi International Airport (OMAA) | Zhuhai Airport (ZGSD) | 2026-08-19 23:13 UTC | 2026-08-20 06:40 UTC | 7h 27m |
| WIF64M | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-20 05:46 UTC | 2026-08-20 06:36 UTC | 49m |
| CPA256 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-08-19 19:38 UTC | 2026-08-20 06:35 UTC | 10h 56m |
| LNI | LNI | Cervantes Airport (YCVS) | Jurien Bay Airport (YJNB) | 2026-08-20 06:19 UTC | 2026-08-20 06:34 UTC | 14m |
| WIF8C | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-08-20 06:17 UTC | 2026-08-20 06:32 UTC | 14m |
| JUST72 | JUS | Holsworthy (Military) Airport (YSHW) | Holsworthy (Military) Airport (YSHW) | 2026-08-20 06:11 UTC | 2026-08-20 06:30 UTC | 18m |
| WIF3LP | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-20 05:43 UTC | 2026-08-20 06:25 UTC | 41m |
| QLK207D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Albury Airport (YMAY) | 2026-08-20 05:23 UTC | 2026-08-20 06:22 UTC | 59m |
| VOE1580 | VOE | Palermo / Punta Raisi Airport (LICJ) | Mikonos Airport (LGMK) | 2026-08-20 04:56 UTC | 2026-08-20 06:22 UTC | 1h 25m |
| QLK24D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-08-20 05:41 UTC | 2026-08-20 06:22 UTC | 40m |
| HBZNH | HBZ | St Stephan Airport (LSTS) | St Stephan Airport (LSTS) | 2026-08-20 06:18 UTC | 2026-08-20 06:20 UTC | 2m |
| RYR3GD | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Capua Airport (LIAU) | 2026-08-20 05:23 UTC | 2026-08-20 06:13 UTC | 50m |
| WIF3BR | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-08-20 05:43 UTC | 2026-08-20 06:10 UTC | 27m |
| EJU56NB | EJU | Malpensa International Airport (LIMC) | Vitoria/Foronda Airport (LEVT) | 2026-08-20 04:42 UTC | 2026-08-20 06:08 UTC | 1h 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
