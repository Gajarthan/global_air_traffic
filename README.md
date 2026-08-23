# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_09:07:38_UTC-green)

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

**Latest saved flight:** 2026-08-23 09:07:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 09:07:38 UTC

- **228,004** saved flights
- **70,625** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **228,004** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,749,225.1 tonnes** estimated CO2 emissions
- **159,375,368 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9150 |
| 2 | SkyWest Airlines | 8104 |
| 3 | EJA | 4393 |
| 4 | IndiGo | 3856 |
| 5 | American Airlines | 3740 |
| 6 | Southwest Airlines | 3549 |
| 7 | Delta Air Lines | 2919 |
| 8 | ENY | 2791 |
| 9 | LATAM Airlines | 2184 |
| 10 | AZU | 2112 |
| 11 | Vueling | 1934 |
| 12 | Lufthansa | 1863 |
| 13 | WIF | 1797 |
| 14 | LXJ | 1790 |
| 15 | easyJet | 1585 |
| 16 | Swiss International | 1519 |
| 17 | AXM | 1514 |
| 18 | QLK | 1446 |
| 19 | United Airlines | 1444 |
| 20 | EJU | 1442 |
| 21 | Alaska Airlines | 1385 |
| 22 | All Nippon Airways | 1368 |
| 23 | GLO | 1264 |
| 24 | VIV | 1253 |
| 25 | PGT | 1251 |
| 26 | WMT | 1237 |
| 27 | Air France | 1236 |
| 28 | Wizz Air | 1182 |
| 29 | JetBlue | 1142 |
| 30 | AEE | 1136 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 190647 |
| 2 | 🇪🇸 ES | 14614 |
| 3 | 🇧🇷 BR | 13293 |
| 4 | 🇦🇺 AU | 12937 |
| 5 | 🇨🇦 CA | 12618 |
| 6 | 🇮🇹 IT | 12268 |
| 7 | 🇮🇳 IN | 12019 |
| 8 | 🇩🇪 DE | 11212 |
| 9 | 🇬🇧 GB | 10704 |
| 10 | 🇨🇴 CO | 9384 |
| 11 | 🇯🇵 JP | 9284 |
| 12 | 🇫🇷 FR | 9112 |
| 13 | 🇹🇷 TR | 6697 |
| 14 | 🇬🇷 GR | 6691 |
| 15 | 🇲🇽 MX | 6358 |
| 16 | 🇨🇭 CH | 6018 |
| 17 | 🇳🇴 NO | 5601 |
| 18 | 🇲🇾 MY | 4038 |
| 19 | 🇹🇭 TH | 3946 |
| 20 | 🇿🇦 ZA | 3943 |
| 21 | 🇵🇱 PL | 3788 |
| 22 | 🇳🇿 NZ | 3167 |
| 23 | 🇵🇭 PH | 3126 |
| 24 | 🇬🇹 GT | 2873 |
| 25 | 🇰🇷 KR | 2702 |
| 26 | 🇭🇷 HR | 2589 |
| 27 | 🇲🇦 MA | 2302 |
| 28 | 🇲🇪 ME | 2062 |
| 29 | 🇳🇱 NL | 2034 |
| 30 | 🇮🇩 ID | 1970 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4771 |
| 2 | Denver International Airport |  | US | 3714 |
| 3 | Indira Gandhi International Airport |  | IN | 2776 |
| 4 | Tokyo International Airport |  | JP | 2773 |
| 5 | Guaymaral Airport |  | CO | 2647 |
| 6 | Harry Reid International Airport |  | US | 2473 |
| 7 | Zurich Airport |  | CH | 2369 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2332 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2302 |
| 10 | La Aurora Airport |  | GT | 2189 |
| 11 | El Dorado International Airport |  | CO | 2084 |
| 12 | Chicago O'Hare International Airport |  | US | 2071 |
| 13 | Salt Lake City International Airport |  | US | 2009 |
| 14 | Congonhas Airport |  | BR | 1939 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1938 |
| 16 | Frankfurt am Main International Airport |  | DE | 1827 |
| 17 | Madrid Barajas International Airport |  | ES | 1778 |
| 18 | Capua Airport |  | IT | 1771 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1703 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1698 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1648 |
| 22 | Malpensa International Airport |  | IT | 1622 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1608 |
| 24 | Macau International Airport |  | MO | 1594 |
| 25 | Charles de Gaulle International Airport |  | FR | 1574 |
| 26 | Ninoy Aquino International Airport |  | PH | 1498 |
| 27 | Charlotte/Douglas International Airport |  | US | 1492 |
| 28 | Kuala Lumpur International Airport |  | MY | 1463 |
| 29 | Barcelona International Airport |  | ES | 1421 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1384 |
| 31 | Bengaluru International Airport |  | IN | 1352 |
| 32 | Enrique Olaya Herrera Airport |  | CO | 1350 |
| 33 | Viracopos International Airport |  | BR | 1348 |
| 34 | Seattle-Tacoma International Airport |  | US | 1347 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1345 |
| 36 | Calgary International Airport |  | CA | 1299 |
| 37 | Don Mueang International Airport |  | TH | 1294 |
| 38 | Oslo Gardermoen Airport |  | NO | 1264 |
| 39 | Vitoria/Foronda Airport |  | ES | 1247 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1231 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1075 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 832 | 21m | 244 km | 3,503.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 572 | 1h 6m | 770 km | 7,598.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 566 | 24m | 225 km | 2,195.8 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 547 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 514 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 356 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 347 | 1h 50m | 1,423 km | 8,515.9 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 314 | 1h 7m | 706 km | 3,823.0 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 311 | 21m | 250 km | 1,343.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 305 | 22m | 55 km | 289.9 t |
| 15 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 302 | 44m | 555 km | 2,891.8 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 292 | 1h 38m | 1,156 km | 5,825.3 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 291 | 24m | 218 km | 1,096.3 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 284 | 19m | 99 km | 486.5 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 276 | 27m | 215 km | 1,022.2 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 267 | 1h 14m | 961 km | 4,425.7 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 266 | 12m | - | - |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 260 | 19m | 144 km | 646.7 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 245 | 1h 50m | 1,304 km | 5,511.9 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 240 | 15m | 154 km | 635.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 239 | 28m | 152 km | 624.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HBYJF | HBY | Langenthal Airport (LSPL) | Ambri Airport (LSPM) | 2026-08-23 08:22 UTC | 2026-08-23 09:07 UTC | 45m |
| BEL7NL | Brussels Airlines | Geneva Cointrin International Airport (LSGG) | Brussels Airport (EBBR) | 2026-08-23 07:16 UTC | 2026-08-23 09:06 UTC | 1h 50m |
| FPTUN | FPT | Ambri Airport (LSPM) | Ambri Airport (LSPM) | 2026-08-23 08:32 UTC | 2026-08-23 08:52 UTC | 20m |
| RYR866B | Ryanair | Eindhoven Airport (EHEH) | Bergamo / Orio Al Serio Airport (LIME) | 2026-08-23 07:45 UTC | 2026-08-23 08:49 UTC | 1h 3m |
| CWA921 | CWA | Edmonton International Airport (CYEG) | Mayerthorpe Airport (CEV5) | 2026-08-23 08:28 UTC | 2026-08-23 08:45 UTC | 17m |
| RYR9MP | Ryanair | Birmingham International Airport (EGBB) | Dublin Airport (EIDW) | 2026-08-23 08:00 UTC | 2026-08-23 08:42 UTC | 41m |
| FDR304 | FDR | O. R. Tambo International Airport (FAOR) | Pilanesberg International Airport (FAPN) | 2026-08-23 08:08 UTC | 2026-08-23 08:40 UTC | 32m |
| HBKPJ | HBK | Mollis Airport (LSZM) | Donaueschingen-Villingen Airport (EDTD) | 2026-08-23 07:44 UTC | 2026-08-23 08:39 UTC | 55m |
| CHX80 | CHX | Weiden in der Oberpfalz Airport (EDQW) | Weiden in der Oberpfalz Airport (EDQW) | 2026-08-23 08:35 UTC | 2026-08-23 08:38 UTC | 2m |
| AEE5C | AEE | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-08-23 08:14 UTC | 2026-08-23 08:36 UTC | 21m |
| ANA297 | All Nippon Airways | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 2026-08-23 07:53 UTC | 2026-08-23 08:34 UTC | 41m |
| JL2325 |  | Osaka International Airport (RJOO) | Tajima Airport (RJBT) | 2026-08-23 08:13 UTC | 2026-08-23 08:32 UTC | 19m |
| PJZ600 | PJZ | Nea Anchialos Airport (LGBL) | Santorini Airport (LGSR) | 2026-08-23 08:04 UTC | 2026-08-23 08:32 UTC | 27m |
| ZSOHK | ZSO | Grand Central Airport (FAGC) | Morningside Farm Airport (FAMS) | 2026-08-23 07:24 UTC | 2026-08-23 08:31 UTC | 1h 6m |
| RYR4EY | Ryanair | Brussels South Charleroi Airport (EBCI) | Angads Airport (GMFO) | 2026-08-23 06:02 UTC | 2026-08-23 08:29 UTC | 2h 26m |
| TRA5371 | TRA | Rotterdam Airport (EHRD) | Taza Airport (GMFZ) | 2026-08-23 05:35 UTC | 2026-08-23 08:27 UTC | 2h 52m |
| ICE30R | ICE | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 2026-08-23 08:07 UTC | 2026-08-23 08:26 UTC | 18m |
| LOT6669 | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Palermo / Punta Raisi Airport (LICJ) | 2026-08-23 06:11 UTC | 2026-08-23 08:26 UTC | 2h 15m |
| EZY64KL | easyJet | London Luton Airport (EGGW) | Barcelona International Airport (LEBL) | 2026-08-23 06:32 UTC | 2026-08-23 08:24 UTC | 1h 52m |
| AAR8735 | AAR | Gimpo International Airport (RKSS) | G 710 Airport (RK6D) | 2026-08-23 07:54 UTC | 2026-08-23 08:23 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
