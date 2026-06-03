# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--03_20:17:57_UTC-green)

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

**Latest saved flight:** 2026-06-03 20:17:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-03 20:17:57 UTC

- **101,637** saved flights
- **36,029** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **101,637** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,243,666.9 tonnes** estimated CO2 emissions
- **72,096,630 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4196 |
| 2 | SkyWest Airlines | 3817 |
| 3 | IndiGo | 2038 |
| 4 | EJA | 1940 |
| 5 | American Airlines | 1643 |
| 6 | Southwest Airlines | 1541 |
| 7 | ENY | 1262 |
| 8 | Delta Air Lines | 1196 |
| 9 | Lufthansa | 1188 |
| 10 | Vueling | 947 |
| 11 | LATAM Airlines | 900 |
| 12 | WIF | 891 |
| 13 | AXM | 878 |
| 14 | AZU | 820 |
| 15 | LXJ | 763 |
| 16 | Swiss International | 738 |
| 17 | All Nippon Airways | 718 |
| 18 | Alaska Airlines | 713 |
| 19 | QLK | 682 |
| 20 | easyJet | 660 |
| 21 | EJU | 638 |
| 22 | Cathay Pacific | 615 |
| 23 | AEE | 590 |
| 24 | VIV | 587 |
| 25 | Air France | 586 |
| 26 | United Airlines | 568 |
| 27 | MXY | 548 |
| 28 | CXK | 545 |
| 29 | Japan Airlines | 509 |
| 30 | AXB | 501 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 85297 |
| 2 | 🇪🇸 ES | 7022 |
| 3 | 🇮🇳 IN | 6449 |
| 4 | 🇦🇺 AU | 6161 |
| 5 | 🇧🇷 BR | 5557 |
| 6 | 🇩🇪 DE | 5490 |
| 7 | 🇮🇹 IT | 5412 |
| 8 | 🇨🇦 CA | 5264 |
| 9 | 🇯🇵 JP | 4699 |
| 10 | 🇬🇧 GB | 4311 |
| 11 | 🇫🇷 FR | 4048 |
| 12 | 🇨🇴 CO | 3505 |
| 13 | 🇲🇽 MX | 3077 |
| 14 | 🇬🇷 GR | 2894 |
| 15 | 🇳🇴 NO | 2819 |
| 16 | 🇨🇭 CH | 2615 |
| 17 | 🇲🇾 MY | 2240 |
| 18 | 🇹🇷 TR | 1925 |
| 19 | 🇿🇦 ZA | 1769 |
| 20 | 🇳🇿 NZ | 1711 |
| 21 | 🇹🇭 TH | 1690 |
| 22 | 🇰🇷 KR | 1645 |
| 23 | 🇵🇱 PL | 1631 |
| 24 | 🇬🇹 GT | 1501 |
| 25 | 🇵🇭 PH | 1485 |
| 26 | 🇲🇦 MA | 1134 |
| 27 | 🇲🇴 MO | 1074 |
| 28 | 🇳🇱 NL | 1009 |
| 29 | 🇲🇪 ME | 961 |
| 30 | 🇭🇷 HR | 899 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2208 |
| 2 | Denver International Airport |  | US | 1742 |
| 3 | Tokyo International Airport |  | JP | 1557 |
| 4 | Indira Gandhi International Airport |  | IN | 1403 |
| 5 | Harry Reid International Airport |  | US | 1304 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1301 |
| 7 | Guaymaral Airport |  | CO | 1267 |
| 8 | Frankfurt am Main International Airport |  | DE | 1188 |
| 9 | Zurich Airport |  | CH | 1165 |
| 10 | La Aurora Airport |  | GT | 1154 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1098 |
| 12 | El Dorado International Airport |  | CO | 1075 |
| 13 | Macau International Airport |  | MO | 1074 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1033 |
| 15 | Chicago O'Hare International Airport |  | US | 1016 |
| 16 | Madrid Barajas International Airport |  | ES | 887 |
| 17 | Kuala Lumpur International Airport |  | MY | 885 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 874 |
| 19 | Salt Lake City International Airport |  | US | 859 |
| 20 | Capua Airport |  | IT | 844 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 792 |
| 22 | Charlotte/Douglas International Airport |  | US | 787 |
| 23 | Charles de Gaulle International Airport |  | FR | 780 |
| 24 | Malpensa International Airport |  | IT | 771 |
| 25 | Bengaluru International Airport |  | IN | 770 |
| 26 | Congonhas Airport |  | BR | 770 |
| 27 | Daniel K Inouye International Airport |  | US | 704 |
| 28 | Tenerife Norte Airport |  | ES | 698 |
| 29 | Ninoy Aquino International Airport |  | PH | 679 |
| 30 | Barcelona International Airport |  | ES | 671 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 663 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 660 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 648 |
| 34 | Amsterdam Airport Schiphol |  | NL | 623 |
| 35 | Don Mueang International Airport |  | TH | 618 |
| 36 | Vitoria/Foronda Airport |  | ES | 616 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 38 | Calgary International Airport |  | CA | 596 |
| 39 | Seattle-Tacoma International Airport |  | US | 586 |
| 40 | John Paul II International Airport Kraków-Balice Airport |  | PL | 575 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 522 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 373 | 21m | 244 km | 1,570.6 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 271 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 268 | 24m | 225 km | 1,039.7 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 256 | 14m | 114 km | 502.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 249 | 1h 26m | 910 km | 3,907.4 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 246 | 28m | 304 km | 1,289.6 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 233 | 1h 10m | 770 km | 3,095.2 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 214 | 19m | 165 km | 608.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 201 | 26m | 275 km | 952.5 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 159 | 20m | 99 km | 272.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 151 | 22m | 55 km | 143.5 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 150 | 27m | 215 km | 555.5 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 142 | 31m | 369 km | 903.9 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 141 | 27m | 152 km | 368.5 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 136 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 131 | 20m | 147 km | 331.5 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 131 | 18m | 144 km | 325.9 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 128 | 1h 39m | 1,156 km | 2,553.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 127 | 1h 1m | 695 km | 1,522.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 120 | 1h 43m | 1,423 km | 2,945.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 117 | 1h 18m | 961 km | 1,939.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 117 | 12m | - | - |
| 30 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N129FR |  | Sky Acres Airport (K44N) | Hartford-Brainard Airport (KHFD) | 2026-06-03 19:40 UTC | 2026-06-03 20:17 UTC | 37m |
| N52654 |  | Merrill Field (PAMR) | Homer Airport (PAHO) | 2026-06-03 18:51 UTC | 2026-06-03 20:13 UTC | 1h 21m |
| STEEL21 | STE | OK79 (OK79) | OK79 (OK79) | 2026-06-03 19:48 UTC | 2026-06-03 20:09 UTC | 20m |
| ZPBJL | ZPB | Obera Airport (SATO) | Encarnacion Airport (SGEN) | 2026-06-03 19:43 UTC | 2026-06-03 20:06 UTC | 22m |
| DUKE51 | DUK | Wiesbaden Army Airfield (ETOU) | Stuttgart Airport (EDDS) | 2026-06-03 18:53 UTC | 2026-06-03 20:06 UTC | 1h 12m |
| SPADE20 | SPA | Wiesbaden Army Airfield (ETOU) | Wiesbaden Army Airfield (ETOU) | 2026-06-03 19:22 UTC | 2026-06-03 20:05 UTC | 43m |
| N746TW |  | KU42 (KU42) | KU42 (KU42) | 2026-06-03 19:46 UTC | 2026-06-03 19:58 UTC | 11m |
| LXJ600 | LXJ | Hopewell Airpark (90NY) | Rocky Mountain Metro Airport (KBJC) | 2026-06-03 16:38 UTC | 2026-06-03 19:56 UTC | 3h 18m |
| BRU945 | BRU | Minsk International Airport (UMMS) | Kasimovo Airfield (XLLN) | 2026-06-03 17:25 UTC | 2026-06-03 19:53 UTC | 2h 28m |
| PRCBJ | PRC | Congonhas Airport (SBSP) | Parati Airport (SDTK) | 2026-06-03 19:24 UTC | 2026-06-03 19:51 UTC | 27m |
| N101PG |  | French Valley Airport (KF70) | Reno/Tahoe International Airport (KRNO) | 2026-06-03 18:44 UTC | 2026-06-03 19:47 UTC | 1h 2m |
| N44668 |  | Westfield-Barnes Regional Airport (KBAF) | Concord Municipal Airport (KCON) | 2026-06-03 18:47 UTC | 2026-06-03 19:47 UTC | 59m |
| N12791 |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-06-03 19:19 UTC | 2026-06-03 19:46 UTC | 26m |
| GFY164 | GFY | 52OR (52OR) | Grabhorn's Airport (8OR6) | 2026-06-03 19:30 UTC | 2026-06-03 19:46 UTC | 16m |
| KAPT76 | KAP | Cape Cod Gateway Airport (KHYA) | Provincetown Municipal Airport (KPVC) | 2026-06-03 18:38 UTC | 2026-06-03 19:44 UTC | 1h 5m |
| N100BW |  | Talkeetna Airport (PATK) | Mc Kinley Country Airport (81AK) | 2026-06-03 19:13 UTC | 2026-06-03 19:44 UTC | 30m |
| N556HD |  | Salt Lake City International Airport (KSLC) | Cokeville Municipal Airport (KU06) | 2026-06-03 19:28 UTC | 2026-06-03 19:42 UTC | 13m |
| FRG491 | FRG | San Luis Obispo County Regional Airport (KSBP) | Pueblo Memorial Airport (KPUB) | 2026-06-03 17:08 UTC | 2026-06-03 19:39 UTC | 2h 30m |
| N885US |  | Lincoln Regional/Karl Harder Field (KLHM) | San Carlos Airport (KSQL) | 2026-06-03 18:52 UTC | 2026-06-03 19:37 UTC | 45m |
| WIF149 | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-06-03 19:06 UTC | 2026-06-03 19:37 UTC | 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
