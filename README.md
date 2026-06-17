# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--17_11:19:09_UTC-green)

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

**Latest saved flight:** 2026-06-17 11:19:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-17 11:19:09 UTC

- **112,857** saved flights
- **39,240** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **112,857** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,376,800.3 tonnes** estimated CO2 emissions
- **79,814,509 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4649 |
| 2 | SkyWest Airlines | 4204 |
| 3 | IndiGo | 2192 |
| 4 | EJA | 2189 |
| 5 | American Airlines | 1782 |
| 6 | Southwest Airlines | 1682 |
| 7 | ENY | 1409 |
| 8 | Delta Air Lines | 1335 |
| 9 | Lufthansa | 1266 |
| 10 | Vueling | 1030 |
| 11 | WIF | 995 |
| 12 | LATAM Airlines | 994 |
| 13 | AXM | 945 |
| 14 | AZU | 939 |
| 15 | LXJ | 861 |
| 16 | Swiss International | 807 |
| 17 | All Nippon Airways | 786 |
| 18 | Alaska Airlines | 764 |
| 19 | QLK | 739 |
| 20 | easyJet | 728 |
| 21 | EJU | 714 |
| 22 | Cathay Pacific | 665 |
| 23 | AEE | 632 |
| 24 | Air France | 627 |
| 25 | United Airlines | 626 |
| 26 | VIV | 626 |
| 27 | MXY | 598 |
| 28 | CXK | 595 |
| 29 | GLO | 555 |
| 30 | AXB | 554 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 95090 |
| 2 | 🇪🇸 ES | 7728 |
| 3 | 🇮🇳 IN | 6922 |
| 4 | 🇦🇺 AU | 6722 |
| 5 | 🇧🇷 BR | 6242 |
| 6 | 🇮🇹 IT | 6061 |
| 7 | 🇩🇪 DE | 6027 |
| 8 | 🇨🇦 CA | 5927 |
| 9 | 🇯🇵 JP | 5111 |
| 10 | 🇬🇧 GB | 4869 |
| 11 | 🇫🇷 FR | 4494 |
| 12 | 🇨🇴 CO | 3812 |
| 13 | 🇲🇽 MX | 3331 |
| 14 | 🇬🇷 GR | 3203 |
| 15 | 🇳🇴 NO | 3111 |
| 16 | 🇨🇭 CH | 2887 |
| 17 | 🇲🇾 MY | 2443 |
| 18 | 🇹🇷 TR | 2260 |
| 19 | 🇿🇦 ZA | 1919 |
| 20 | 🇰🇷 KR | 1868 |
| 21 | 🇳🇿 NZ | 1856 |
| 22 | 🇹🇭 TH | 1843 |
| 23 | 🇵🇱 PL | 1840 |
| 24 | 🇵🇭 PH | 1649 |
| 25 | 🇬🇹 GT | 1610 |
| 26 | 🇲🇦 MA | 1240 |
| 27 | 🇲🇴 MO | 1161 |
| 28 | 🇲🇪 ME | 1106 |
| 29 | 🇳🇱 NL | 1098 |
| 30 | 🇭🇷 HR | 980 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2407 |
| 2 | Denver International Airport |  | US | 1909 |
| 3 | Tokyo International Airport |  | JP | 1696 |
| 4 | Indira Gandhi International Airport |  | IN | 1508 |
| 5 | Harry Reid International Airport |  | US | 1416 |
| 6 | Guaymaral Airport |  | CO | 1413 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1390 |
| 8 | Zurich Airport |  | CH | 1268 |
| 9 | La Aurora Airport |  | GT | 1240 |
| 10 | Frankfurt am Main International Airport |  | DE | 1236 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1213 |
| 12 | Macau International Airport |  | MO | 1161 |
| 13 | El Dorado International Airport |  | CO | 1144 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1132 |
| 15 | Chicago O'Hare International Airport |  | US | 1122 |
| 16 | Capua Airport |  | IT | 981 |
| 17 | Madrid Barajas International Airport |  | ES | 977 |
| 18 | Salt Lake City International Airport |  | US | 954 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 947 |
| 20 | Kuala Lumpur International Airport |  | MY | 947 |
| 21 | Charlotte/Douglas International Airport |  | US | 874 |
| 22 | Congonhas Airport |  | BR | 868 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 845 |
| 24 | Charles de Gaulle International Airport |  | FR | 839 |
| 25 | Bengaluru International Airport |  | IN | 838 |
| 26 | Malpensa International Airport |  | IT | 817 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 785 |
| 28 | Ninoy Aquino International Airport |  | PH | 760 |
| 29 | Daniel K Inouye International Airport |  | US | 745 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 740 |
| 31 | Tenerife Norte Airport |  | ES | 739 |
| 32 | Barcelona International Airport |  | ES | 732 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 713 |
| 34 | Don Mueang International Airport |  | TH | 672 |
| 35 | Amsterdam Airport Schiphol |  | NL | 672 |
| 36 | Vitoria/Foronda Airport |  | ES | 669 |
| 37 | Calgary International Airport |  | CA | 666 |
| 38 | Seattle-Tacoma International Airport |  | US | 651 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 648 |
| 40 | Viracopos International Airport |  | BR | 642 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 586 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 411 | 21m | 244 km | 1,730.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 301 | 24m | 225 km | 1,167.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 293 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 284 | 1h 7m | 706 km | 3,457.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 277 | 1h 25m | 910 km | 4,346.8 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 275 | 14m | 114 km | 539.4 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 270 | 1h 10m | 770 km | 3,586.7 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 227 | 26m | 275 km | 1,075.7 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 225 | 19m | 165 km | 640.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 210 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 167 | 20m | 99 km | 286.1 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 164 | 26m | 215 km | 607.4 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 164 | 22m | 55 km | 155.9 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 162 | 13m | - | - |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 154 | 27m | 152 km | 402.5 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 153 | 31m | 369 km | 973.9 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 150 | 44m | 452 km | 1,169.0 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 146 | 18m | 144 km | 363.2 t |
| 22 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 144 | 44m | 241 km | 598.1 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 144 | 20m | 250 km | 622.0 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 135 | 1h 1m | 695 km | 1,618.2 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 133 | 1h 43m | 1,423 km | 3,264.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 133 | 1h 39m | 1,156 km | 2,653.3 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 127 | 12m | - | - |
| 29 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 126 | 24m | 223 km | 484.7 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 126 | 1h 17m | 961 km | 2,088.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ANA36 | All Nippon Airways | Osaka International Airport (RJOO) | Tokyo International Airport (RJTT) | 2026-06-17 10:27 UTC | 2026-06-17 11:19 UTC | 51m |
| CHX62 | CHX | Pirna-Pratzschwitz Airport (EDAR) | Dresden Airport (EDDC) | 2026-06-17 11:06 UTC | 2026-06-17 11:17 UTC | 11m |
| PHJVZ | PHJ | Seppe Airport (EHSE) | Rotterdam Airport (EHRD) | 2026-06-17 10:18 UTC | 2026-06-17 11:17 UTC | 58m |
| N80393 |  | 1AR0 (1AR0) | 1AR0 (1AR0) | 2026-06-17 10:43 UTC | 2026-06-17 11:11 UTC | 27m |
| YOX | YOX | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-06-17 10:30 UTC | 2026-06-17 10:59 UTC | 29m |
| N9236K |  | Decatur Municipal Airport (KLUD) | Decatur Municipal Airport (KLUD) | 2026-06-17 10:56 UTC | 2026-06-17 10:58 UTC | 2m |
| WIF77P | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-06-17 10:11 UTC | 2026-06-17 10:57 UTC | 46m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | NV11 (NV11) | 2026-06-17 10:40 UTC | 2026-06-17 10:53 UTC | 12m |
| LLR513 | LLR | Bengaluru International Airport (VOBL) | Hosur Airport (VO95) | 2026-06-17 10:29 UTC | 2026-06-17 10:49 UTC | 19m |
| ZEF | ZEF | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-06-17 10:11 UTC | 2026-06-17 10:47 UTC | 35m |
| HLE06 | HLE | Bristol International Airport (EGGD) | Gloucestershire Airport (EGBJ) | 2026-06-17 10:28 UTC | 2026-06-17 10:45 UTC | 16m |
| HNL24A | HNL | De Kooy Airport (EHKD) | Rotterdam Airport (EHRD) | 2026-06-17 10:04 UTC | 2026-06-17 10:43 UTC | 38m |
| RYR3TY | Ryanair | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Santorini Airport (LGSR) | 2026-06-17 09:03 UTC | 2026-06-17 10:40 UTC | 1h 36m |
| RYR6GM | Ryanair | Memmingen Allgau Airport (EDJA) | Visoko Sport Airfield (LQVI) | 2026-06-17 09:44 UTC | 2026-06-17 10:38 UTC | 54m |
| IBB28TX | IBB | Tenerife Norte Airport (GCXO) | Santander Airport (LEXJ) | 2026-06-17 08:08 UTC | 2026-06-17 10:37 UTC | 2h 29m |
| YOJ | YOJ | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-06-17 09:59 UTC | 2026-06-17 10:37 UTC | 38m |
| JAL613M | Japan Airlines | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 2026-06-17 09:17 UTC | 2026-06-17 10:35 UTC | 1h 17m |
| AUR202 | AUR | Guernsey Airport (EGJB) | Guernsey Airport (EGJB) | 2026-06-17 10:34 UTC | 2026-06-17 10:34 UTC | 0m |
| EWG49C | EWG | Malaga Airport (LEMG) | Hannover Airport (EDDV) | 2026-06-17 07:46 UTC | 2026-06-17 10:33 UTC | 2h 47m |
| FD629 |  | Perth Jandakot Airport (YPJT) | Wagin Airport (YWGN) | 2026-06-17 09:58 UTC | 2026-06-17 10:30 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
