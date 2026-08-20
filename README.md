# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_11:31:08_UTC-green)

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

**Latest saved flight:** 2026-08-20 11:31:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 11:31:08 UTC

- **218,933** saved flights
- **68,822** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **218,933** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,636,838.1 tonnes** estimated CO2 emissions
- **152,860,181 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8779 |
| 2 | SkyWest Airlines | 7813 |
| 3 | EJA | 4247 |
| 4 | IndiGo | 3721 |
| 5 | American Airlines | 3637 |
| 6 | Southwest Airlines | 3470 |
| 7 | Delta Air Lines | 2823 |
| 8 | ENY | 2698 |
| 9 | LATAM Airlines | 2071 |
| 10 | AZU | 2004 |
| 11 | Vueling | 1842 |
| 12 | Lufthansa | 1818 |
| 13 | WIF | 1749 |
| 14 | LXJ | 1728 |
| 15 | easyJet | 1517 |
| 16 | Swiss International | 1458 |
| 17 | AXM | 1440 |
| 18 | United Airlines | 1382 |
| 19 | QLK | 1375 |
| 20 | EJU | 1367 |
| 21 | Alaska Airlines | 1339 |
| 22 | All Nippon Airways | 1318 |
| 23 | VIV | 1196 |
| 24 | Air France | 1190 |
| 25 | GLO | 1189 |
| 26 | PGT | 1186 |
| 27 | WMT | 1151 |
| 28 | Wizz Air | 1116 |
| 29 | JetBlue | 1112 |
| 30 | AEE | 1097 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 184213 |
| 2 | 🇪🇸 ES | 14020 |
| 3 | 🇧🇷 BR | 12613 |
| 4 | 🇦🇺 AU | 12408 |
| 5 | 🇨🇦 CA | 12076 |
| 6 | 🇮🇹 IT | 11660 |
| 7 | 🇮🇳 IN | 11593 |
| 8 | 🇩🇪 DE | 10821 |
| 9 | 🇬🇧 GB | 10276 |
| 10 | 🇨🇴 CO | 8981 |
| 11 | 🇯🇵 JP | 8954 |
| 12 | 🇫🇷 FR | 8730 |
| 13 | 🇬🇷 GR | 6383 |
| 14 | 🇹🇷 TR | 6303 |
| 15 | 🇲🇽 MX | 6096 |
| 16 | 🇨🇭 CH | 5803 |
| 17 | 🇳🇴 NO | 5432 |
| 18 | 🇲🇾 MY | 3805 |
| 19 | 🇿🇦 ZA | 3721 |
| 20 | 🇵🇱 PL | 3625 |
| 21 | 🇹🇭 TH | 3620 |
| 22 | 🇳🇿 NZ | 3041 |
| 23 | 🇵🇭 PH | 2956 |
| 24 | 🇬🇹 GT | 2767 |
| 25 | 🇰🇷 KR | 2631 |
| 26 | 🇭🇷 HR | 2411 |
| 27 | 🇲🇦 MA | 2205 |
| 28 | 🇳🇱 NL | 1947 |
| 29 | 🇲🇪 ME | 1929 |
| 30 | 🇮🇩 ID | 1861 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4591 |
| 2 | Denver International Airport |  | US | 3578 |
| 3 | Tokyo International Airport |  | JP | 2687 |
| 4 | Indira Gandhi International Airport |  | IN | 2657 |
| 5 | Guaymaral Airport |  | CO | 2595 |
| 6 | Harry Reid International Airport |  | US | 2417 |
| 7 | Zurich Airport |  | CH | 2273 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2245 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2225 |
| 10 | La Aurora Airport |  | GT | 2106 |
| 11 | El Dorado International Airport |  | CO | 2053 |
| 12 | Chicago O'Hare International Airport |  | US | 2007 |
| 13 | Salt Lake City International Airport |  | US | 1931 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1900 |
| 15 | Congonhas Airport |  | BR | 1844 |
| 16 | Frankfurt am Main International Airport |  | DE | 1783 |
| 17 | Madrid Barajas International Airport |  | ES | 1713 |
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
| 34 | Viracopos International Airport |  | BR | 1279 |
| 35 | Calgary International Airport |  | CA | 1235 |
| 36 | Vitoria/Foronda Airport |  | ES | 1214 |
| 37 | Oslo Gardermoen Airport |  | NO | 1211 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1201 |
| 39 | Don Mueang International Airport |  | TH | 1194 |
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
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 319 | 44m | 241 km | 1,325.1 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 294 | 22m | 55 km | 279.4 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 286 | 21m | 250 km | 1,235.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 273 | 1h 38m | 1,156 km | 5,446.2 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 270 | 24m | 218 km | 1,017.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 269 | 27m | 215 km | 996.3 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 260 | 13m | - | - |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 258 | 1h 14m | 961 km | 4,276.5 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 248 | 19m | 144 km | 616.9 t |
| 26 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 246 | 44m | 555 km | 2,355.6 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 246 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 236 | 1h 49m | 1,304 km | 5,309.4 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| R20653 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-20 09:29 UTC | 2026-08-20 11:31 UTC | 2h 2m |
| EIN205 | Aer Lingus | Manchester Airport (EGCC) | Dublin Airport (EIDW) | 2026-08-20 10:51 UTC | 2026-08-20 11:26 UTC | 35m |
| BRU912 | BRU | Sheremetyevo International Airport (UUEE) | Smolensk North Airport (XUBS) | 2026-08-20 11:01 UTC | 2026-08-20 11:24 UTC | 22m |
| EMC8T | EMC | London Biggin Hill Airport (EGKB) | Lydd Airport (EGMD) | 2026-08-20 10:14 UTC | 2026-08-20 11:22 UTC | 1h 8m |
| DFSWW | DFS | Herning Airport (EKHG) | Herning Airport (EKHG) | 2026-08-20 10:38 UTC | 2026-08-20 11:19 UTC | 40m |
| HNL24B | HNL | De Kooy Airport (EHKD) | Rotterdam Airport (EHRD) | 2026-08-20 10:44 UTC | 2026-08-20 11:17 UTC | 33m |
| MRA603 | MRA | Owosso Community Airport (KRNP) | Mbs International Airport (KMBS) | 2026-08-20 10:59 UTC | 2026-08-20 11:10 UTC | 11m |
| N1227Q |  | Trenton Mercer Airport (KTTN) | Atlantic City International Airport (KACY) | 2026-08-20 10:56 UTC | 2026-08-20 11:08 UTC | 12m |
| N8326D |  | Easton/Newnam Field (KESN) | Ocean City Municipal Airport (KOXB) | 2026-08-20 10:39 UTC | 2026-08-20 11:02 UTC | 22m |
| ATLAS12 | ATL | Wunstorf Airport (ETNW) | Siegerland Airport (EDGS) | 2026-08-20 10:30 UTC | 2026-08-20 11:02 UTC | 31m |
| N8891V |  | Heritage Field (KPTW) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-08-20 10:49 UTC | 2026-08-20 11:01 UTC | 12m |
| PSMYM | PSM | Sao Joaquim Airport (SSSQ) | Fazenda Bonanza Airport (SDBN) | 2026-08-20 10:08 UTC | 2026-08-20 10:55 UTC | 46m |
| CAN11 | CAN | Pescara International Airport (LIBP) | Pescara International Airport (LIBP) | 2026-08-20 10:22 UTC | 2026-08-20 10:54 UTC | 31m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | KXTA (KXTA) | 2026-08-20 10:40 UTC | 2026-08-20 10:53 UTC | 12m |
| DHK238 | DHK | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-08-20 00:35 UTC | 2026-08-20 10:52 UTC | 10h 17m |
| AZU2713 | AZU | Viracopos International Airport (SBKP) | Fazenda Cachoeira do Lontra Airport (SINS) | 2026-08-20 09:14 UTC | 2026-08-20 10:50 UTC | 1h 36m |
| TCKIP | TCK | Milas Bodrum International Airport (LTFE) | HE42 (HE42) | 2026-08-20 09:32 UTC | 2026-08-20 10:50 UTC | 1h 17m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-08-19 20:00 UTC | 2026-08-20 10:50 UTC | 14h 49m |
| N2475L |  | Miami Executive Airport (KTMB) | Mjd Airport (FL31) | 2026-08-20 10:39 UTC | 2026-08-20 10:47 UTC | 7m |
| RYR30UJ | Ryanair | Barcelona International Airport (LEBL) | Vila Real Airport (LPVR) | 2026-08-20 09:10 UTC | 2026-08-20 10:44 UTC | 1h 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
