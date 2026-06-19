# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--19_17:59:06_UTC-green)

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

**Latest saved flight:** 2026-06-19 17:59:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-19 17:59:06 UTC

- **114,868** saved flights
- **39,830** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **114,868** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,397,462.1 tonnes** estimated CO2 emissions
- **81,012,295 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4734 |
| 2 | SkyWest Airlines | 4273 |
| 3 | EJA | 2222 |
| 4 | IndiGo | 2216 |
| 5 | American Airlines | 1802 |
| 6 | Southwest Airlines | 1707 |
| 7 | ENY | 1428 |
| 8 | Delta Air Lines | 1357 |
| 9 | Lufthansa | 1278 |
| 10 | Vueling | 1039 |
| 11 | WIF | 1021 |
| 12 | LATAM Airlines | 1011 |
| 13 | AZU | 961 |
| 14 | AXM | 950 |
| 15 | LXJ | 871 |
| 16 | Swiss International | 813 |
| 17 | All Nippon Airways | 792 |
| 18 | Alaska Airlines | 772 |
| 19 | QLK | 748 |
| 20 | easyJet | 737 |
| 21 | EJU | 721 |
| 22 | Cathay Pacific | 671 |
| 23 | AEE | 646 |
| 24 | United Airlines | 635 |
| 25 | VIV | 634 |
| 26 | Air France | 633 |
| 27 | CXK | 609 |
| 28 | MXY | 608 |
| 29 | AXB | 563 |
| 30 | GLO | 562 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 96891 |
| 2 | 🇪🇸 ES | 7843 |
| 3 | 🇮🇳 IN | 6994 |
| 4 | 🇦🇺 AU | 6817 |
| 5 | 🇧🇷 BR | 6340 |
| 6 | 🇮🇹 IT | 6156 |
| 7 | 🇩🇪 DE | 6144 |
| 8 | 🇨🇦 CA | 6034 |
| 9 | 🇯🇵 JP | 5159 |
| 10 | 🇬🇧 GB | 4984 |
| 11 | 🇫🇷 FR | 4569 |
| 12 | 🇨🇴 CO | 3958 |
| 13 | 🇲🇽 MX | 3389 |
| 14 | 🇬🇷 GR | 3274 |
| 15 | 🇳🇴 NO | 3175 |
| 16 | 🇨🇭 CH | 2927 |
| 17 | 🇲🇾 MY | 2458 |
| 18 | 🇹🇷 TR | 2318 |
| 19 | 🇿🇦 ZA | 1945 |
| 20 | 🇳🇿 NZ | 1888 |
| 21 | 🇵🇱 PL | 1881 |
| 22 | 🇰🇷 KR | 1878 |
| 23 | 🇹🇭 TH | 1871 |
| 24 | 🇵🇭 PH | 1667 |
| 25 | 🇬🇹 GT | 1633 |
| 26 | 🇲🇦 MA | 1250 |
| 27 | 🇲🇴 MO | 1168 |
| 28 | 🇲🇪 ME | 1130 |
| 29 | 🇳🇱 NL | 1114 |
| 30 | 🇭🇷 HR | 1000 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2431 |
| 2 | Denver International Airport |  | US | 1940 |
| 3 | Tokyo International Airport |  | JP | 1712 |
| 4 | Indira Gandhi International Airport |  | IN | 1528 |
| 5 | Guaymaral Airport |  | CO | 1465 |
| 6 | Harry Reid International Airport |  | US | 1446 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1411 |
| 8 | Zurich Airport |  | CH | 1282 |
| 9 | La Aurora Airport |  | GT | 1260 |
| 10 | Frankfurt am Main International Airport |  | DE | 1248 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1233 |
| 12 | Macau International Airport |  | MO | 1168 |
| 13 | El Dorado International Airport |  | CO | 1167 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1145 |
| 15 | Chicago O'Hare International Airport |  | US | 1130 |
| 16 | Capua Airport |  | IT | 1000 |
| 17 | Madrid Barajas International Airport |  | ES | 983 |
| 18 | Salt Lake City International Airport |  | US | 979 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 964 |
| 20 | Kuala Lumpur International Airport |  | MY | 952 |
| 21 | Charlotte/Douglas International Airport |  | US | 883 |
| 22 | Congonhas Airport |  | BR | 880 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 856 |
| 24 | Bengaluru International Airport |  | IN | 847 |
| 25 | Charles de Gaulle International Airport |  | FR | 846 |
| 26 | General Edward Lawrence Logan International Airport |  | US | 830 |
| 27 | Malpensa International Airport |  | IT | 822 |
| 28 | Ninoy Aquino International Airport |  | PH | 768 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 754 |
| 30 | Daniel K Inouye International Airport |  | US | 749 |
| 31 | Tenerife Norte Airport |  | ES | 746 |
| 32 | Barcelona International Airport |  | ES | 735 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 722 |
| 34 | Don Mueang International Airport |  | TH | 678 |
| 35 | Amsterdam Airport Schiphol |  | NL | 678 |
| 36 | Vitoria/Foronda Airport |  | ES | 677 |
| 37 | Calgary International Airport |  | CA | 675 |
| 38 | Seattle-Tacoma International Airport |  | US | 663 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 657 |
| 40 | Viracopos International Airport |  | BR | 655 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 608 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 415 | 21m | 244 km | 1,747.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 306 | 24m | 225 km | 1,187.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 298 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 285 | 1h 7m | 706 km | 3,469.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 282 | 1h 25m | 910 km | 4,425.2 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 274 | 1h 10m | 770 km | 3,639.9 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 229 | 26m | 275 km | 1,085.1 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 227 | 19m | 165 km | 645.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 213 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 170 | 22m | 55 km | 161.6 t |
| 14 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 168 | 20m | 99 km | 287.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 167 | 26m | 215 km | 618.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 157 | 27m | 152 km | 410.3 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 153 | 31m | 369 km | 973.9 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 152 | 44m | 452 km | 1,184.6 t |
| 21 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 150 | 44m | 241 km | 623.1 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 147 | 20m | 250 km | 635.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 137 | 1h 1m | 695 km | 1,642.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 135 | 1h 43m | 1,423 km | 3,313.1 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 134 | 1h 38m | 1,156 km | 2,673.2 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 130 | 13m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 129 | 1h 17m | 961 km | 2,138.2 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 128 | 12m | 99 km | 219.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N5897V |  | OI34 (OI34) | OI34 (OI34) | 2026-06-19 17:29 UTC | 2026-06-19 17:59 UTC | 29m |
| N4347G |  | Purdue University Airport (KLAF) | Frankfort Clinton County Regional Airport (KFKR) | 2026-06-19 17:31 UTC | 2026-06-19 17:55 UTC | 24m |
| N821SS |  | Newark Liberty International Airport (KEWR) | Francis S Gabreski Airport (KFOK) | 2026-06-19 17:09 UTC | 2026-06-19 17:53 UTC | 43m |
| LYBRI | LYB | Paluknys Airport (EYVP) | Paluknys Airport (EYVP) | 2026-06-19 17:26 UTC | 2026-06-19 17:52 UTC | 25m |
| N121GX |  | Aurora Municipal Airport (KARR) | 0IL8 (0IL8) | 2026-06-19 17:39 UTC | 2026-06-19 17:49 UTC | 10m |
| N169BA |  | Songbird Ranch Airport (91TS) | TE77 (TE77) | 2026-06-19 17:37 UTC | 2026-06-19 17:48 UTC | 10m |
| N5419F |  | Aurora Municipal Airport (KARR) | Ruder Airport (59IL) | 2026-06-19 16:55 UTC | 2026-06-19 17:47 UTC | 51m |
| N64WG |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-06-19 16:27 UTC | 2026-06-19 17:47 UTC | 1h 19m |
| AEE808 | AEE | Eleftherios Venizelos International Airport (LGAV) | Stuttgart Airport (EDDS) | 2026-06-19 15:15 UTC | 2026-06-19 17:47 UTC | 2h 31m |
| N625MC |  | Boeing Field/King County International Airport (KBFI) | 9WA3 (9WA3) | 2026-06-19 16:53 UTC | 2026-06-19 17:46 UTC | 52m |
| N52620 |  | Bob Maxwell Memorial Airfield (KOKB) | Imperial Beach Nolf (Ream Field) Airport (KNRS) | 2026-06-19 16:51 UTC | 2026-06-19 17:46 UTC | 54m |
| IDPCY | IDP | Lamezia Terme Airport (LICA) | Lamezia Terme Airport (LICA) | 2026-06-19 16:42 UTC | 2026-06-19 17:46 UTC | 1h 3m |
| CAN24 | CAN | Lamezia Terme Airport (LICA) | Lamezia Terme Airport (LICA) | 2026-06-19 16:26 UTC | 2026-06-19 17:45 UTC | 1h 19m |
| N842EB |  | Sebastian Municipal Airport (KX26) | Sebastian Municipal Airport (KX26) | 2026-06-19 17:18 UTC | 2026-06-19 17:36 UTC | 18m |
| N650MC |  | Monterey Bay Academy Airport (CA66) | Truckee-Tahoe Airport (KTRK) | 2026-06-19 16:59 UTC | 2026-06-19 17:36 UTC | 37m |
| N27M |  | Newark Liberty International Airport (KEWR) | Teterboro Airport (KTEB) | 2026-06-19 17:00 UTC | 2026-06-19 17:33 UTC | 33m |
| N264FA |  | Wings Field (KLOM) | Lancaster Airport (KLNS) | 2026-06-19 17:02 UTC | 2026-06-19 17:32 UTC | 30m |
| N737CV |  | K1J6 (K1J6) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-06-19 17:06 UTC | 2026-06-19 17:31 UTC | 24m |
| GCJMP | GCJ | London Biggin Hill Airport (EGKB) | London Biggin Hill Airport (EGKB) | 2026-06-19 17:26 UTC | 2026-06-19 17:30 UTC | 4m |
| N5719V |  | Los Alamos Airport (KLAM) | Ohkay Owingeh Airport (KE14) | 2026-06-19 17:26 UTC | 2026-06-19 17:29 UTC | 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
