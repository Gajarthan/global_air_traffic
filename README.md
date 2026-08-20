# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_11:45:53_UTC-green)

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

**Latest saved flight:** 2026-08-20 11:45:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 11:45:53 UTC

- **218,992** saved flights
- **68,833** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **218,992** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,637,656.0 tonnes** estimated CO2 emissions
- **152,907,593 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8785 |
| 2 | SkyWest Airlines | 7813 |
| 3 | EJA | 4247 |
| 4 | IndiGo | 3721 |
| 5 | American Airlines | 3637 |
| 6 | Southwest Airlines | 3470 |
| 7 | Delta Air Lines | 2823 |
| 8 | ENY | 2698 |
| 9 | LATAM Airlines | 2071 |
| 10 | AZU | 2005 |
| 11 | Vueling | 1842 |
| 12 | Lufthansa | 1818 |
| 13 | WIF | 1750 |
| 14 | LXJ | 1728 |
| 15 | easyJet | 1519 |
| 16 | Swiss International | 1458 |
| 17 | AXM | 1440 |
| 18 | United Airlines | 1382 |
| 19 | QLK | 1375 |
| 20 | EJU | 1367 |
| 21 | Alaska Airlines | 1339 |
| 22 | All Nippon Airways | 1319 |
| 23 | VIV | 1196 |
| 24 | Air France | 1190 |
| 25 | GLO | 1190 |
| 26 | PGT | 1186 |
| 27 | WMT | 1152 |
| 28 | Wizz Air | 1116 |
| 29 | JetBlue | 1112 |
| 30 | AEE | 1097 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 184221 |
| 2 | 🇪🇸 ES | 14031 |
| 3 | 🇧🇷 BR | 12619 |
| 4 | 🇦🇺 AU | 12410 |
| 5 | 🇨🇦 CA | 12079 |
| 6 | 🇮🇹 IT | 11668 |
| 7 | 🇮🇳 IN | 11596 |
| 8 | 🇩🇪 DE | 10823 |
| 9 | 🇬🇧 GB | 10280 |
| 10 | 🇨🇴 CO | 8983 |
| 11 | 🇯🇵 JP | 8956 |
| 12 | 🇫🇷 FR | 8732 |
| 13 | 🇬🇷 GR | 6383 |
| 14 | 🇹🇷 TR | 6303 |
| 15 | 🇲🇽 MX | 6096 |
| 16 | 🇨🇭 CH | 5803 |
| 17 | 🇳🇴 NO | 5434 |
| 18 | 🇲🇾 MY | 3805 |
| 19 | 🇿🇦 ZA | 3731 |
| 20 | 🇵🇱 PL | 3629 |
| 21 | 🇹🇭 TH | 3624 |
| 22 | 🇳🇿 NZ | 3041 |
| 23 | 🇵🇭 PH | 2956 |
| 24 | 🇬🇹 GT | 2767 |
| 25 | 🇰🇷 KR | 2635 |
| 26 | 🇭🇷 HR | 2413 |
| 27 | 🇲🇦 MA | 2206 |
| 28 | 🇳🇱 NL | 1948 |
| 29 | 🇲🇪 ME | 1931 |
| 30 | 🇮🇩 ID | 1862 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4591 |
| 2 | Denver International Airport |  | US | 3578 |
| 3 | Tokyo International Airport |  | JP | 2688 |
| 4 | Indira Gandhi International Airport |  | IN | 2658 |
| 5 | Guaymaral Airport |  | CO | 2595 |
| 6 | Harry Reid International Airport |  | US | 2418 |
| 7 | Zurich Airport |  | CH | 2273 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2245 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2225 |
| 10 | La Aurora Airport |  | GT | 2106 |
| 11 | El Dorado International Airport |  | CO | 2053 |
| 12 | Chicago O'Hare International Airport |  | US | 2007 |
| 13 | Salt Lake City International Airport |  | US | 1931 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1900 |
| 15 | Congonhas Airport |  | BR | 1845 |
| 16 | Frankfurt am Main International Airport |  | DE | 1783 |
| 17 | Madrid Barajas International Airport |  | ES | 1716 |
| 18 | Capua Airport |  | IT | 1669 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1643 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1619 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1605 |
| 22 | Macau International Airport |  | MO | 1574 |
| 23 | Malpensa International Airport |  | IT | 1546 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1541 |
| 25 | Charles de Gaulle International Airport |  | FR | 1508 |
| 26 | Charlotte/Douglas International Airport |  | US | 1462 |
| 27 | Ninoy Aquino International Airport |  | PH | 1405 |
| 28 | Kuala Lumpur International Airport |  | MY | 1397 |
| 29 | Barcelona International Airport |  | ES | 1344 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1331 |
| 31 | Bengaluru International Airport |  | IN | 1321 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1306 |
| 33 | Seattle-Tacoma International Airport |  | US | 1299 |
| 34 | Viracopos International Airport |  | BR | 1280 |
| 35 | Calgary International Airport |  | CA | 1235 |
| 36 | Vitoria/Foronda Airport |  | ES | 1214 |
| 37 | Oslo Gardermoen Airport |  | NO | 1212 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1202 |
| 39 | Don Mueang International Airport |  | TH | 1196 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1177 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 785 | 21m | 244 km | 3,305.4 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 542 | 1h 7m | 770 km | 7,200.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 521 | 24m | 225 km | 2,021.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 493 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 485 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 367 | 27m | 275 km | 1,739.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 322 | 1h 50m | 1,423 km | 7,902.4 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 320 | 44m | 241 km | 1,329.2 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 294 | 22m | 55 km | 279.4 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 287 | 21m | 250 km | 1,239.7 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 273 | 1h 38m | 1,156 km | 5,446.2 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 270 | 24m | 218 km | 1,017.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 269 | 27m | 215 km | 996.3 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 260 | 13m | - | - |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 258 | 1h 14m | 961 km | 4,276.5 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 249 | 19m | 144 km | 619.4 t |
| 26 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 247 | 44m | 555 km | 2,365.1 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 246 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 236 | 1h 49m | 1,304 km | 5,309.4 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SPSKD | SPS | Zamość-Mokre Airport (EPZA) | Zamość-Mokre Airport (EPZA) | 2026-08-20 10:44 UTC | 2026-08-20 11:45 UTC | 1h 1m |
| ACA1066 | Air Canada | Vancouver International Airport (CYVR) | Austin-Bergstrom International Airport (KAUS) | 2026-08-20 07:54 UTC | 2026-08-20 11:41 UTC | 3h 46m |
| LOT4KK | LOT Polish Airlines | Riga International Airport (EVRA) | Kedainiai Air Base (EYKD) | 2026-08-20 11:18 UTC | 2026-08-20 11:39 UTC | 20m |
| CGCOM | CGC | Victoriaville Airport (CSR3) | Montréal / St-Hubert Airport (CYHU) | 2026-08-20 11:19 UTC | 2026-08-20 11:37 UTC | 18m |
| R20653 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-20 09:29 UTC | 2026-08-20 11:31 UTC | 2h 2m |
| EIN205 | Aer Lingus | Manchester Airport (EGCC) | Dublin Airport (EIDW) | 2026-08-20 10:51 UTC | 2026-08-20 11:26 UTC | 35m |
| JANET33 | JAN | Harry Reid International Airport (KLAS) | KXTA (KXTA) | 2026-08-20 11:12 UTC | 2026-08-20 11:24 UTC | 12m |
| BRU912 | BRU | Sheremetyevo International Airport (UUEE) | Smolensk North Airport (XUBS) | 2026-08-20 11:01 UTC | 2026-08-20 11:24 UTC | 22m |
| EMC8T | EMC | London Biggin Hill Airport (EGKB) | Lydd Airport (EGMD) | 2026-08-20 10:14 UTC | 2026-08-20 11:22 UTC | 1h 8m |
| ICE5438 | ICE | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 2026-08-20 10:57 UTC | 2026-08-20 11:20 UTC | 23m |
| DFSWW | DFS | Herning Airport (EKHG) | Herning Airport (EKHG) | 2026-08-20 10:38 UTC | 2026-08-20 11:19 UTC | 40m |
| HNL24B | HNL | De Kooy Airport (EHKD) | Rotterdam Airport (EHRD) | 2026-08-20 10:44 UTC | 2026-08-20 11:17 UTC | 33m |
| N652WE |  | London Luton Airport (EGGW) | Visoko Sport Airfield (LQVI) | 2026-08-20 09:29 UTC | 2026-08-20 11:16 UTC | 1h 47m |
| 5YFDF |  | Nairobi Wilson Airport (HKNW) | Narok Airport (HKNO) | 2026-08-20 10:59 UTC | 2026-08-20 11:16 UTC | 16m |
| MRA603 | MRA | Owosso Community Airport (KRNP) | Mbs International Airport (KMBS) | 2026-08-20 10:59 UTC | 2026-08-20 11:10 UTC | 11m |
| N1227Q |  | Trenton Mercer Airport (KTTN) | Atlantic City International Airport (KACY) | 2026-08-20 10:56 UTC | 2026-08-20 11:08 UTC | 12m |
| HK4854 |  | Enrique Olaya Herrera Airport (SKMD) | Amalfi Airport (SKAM) | 2026-08-20 10:57 UTC | 2026-08-20 11:08 UTC | 11m |
| RYR1ST | Ryanair | Brussels South Charleroi Airport (EBCI) | Santander Airport (LEXJ) | 2026-08-20 09:40 UTC | 2026-08-20 11:06 UTC | 1h 26m |
| N |  | Eurico de Aguiar Salles Airport (SBVT) | Marica Airport (SDMC) | 2026-08-20 10:07 UTC | 2026-08-20 11:06 UTC | 58m |
| RYR15RK | Ryanair | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Pantelleria Airport (LICG) | 2026-08-20 10:32 UTC | 2026-08-20 11:02 UTC | 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
