# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_10:39:57_UTC-green)

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

**Latest saved flight:** 2026-08-08 10:39:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 10:39:57 UTC

- **177,906** saved flights
- **57,199** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **177,906** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,138,160.8 tonnes** estimated CO2 emissions
- **123,951,350 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7050 |
| 2 | SkyWest Airlines | 6496 |
| 3 | EJA | 3507 |
| 4 | IndiGo | 3125 |
| 5 | Southwest Airlines | 2804 |
| 6 | American Airlines | 2772 |
| 7 | ENY | 2213 |
| 8 | Delta Air Lines | 2100 |
| 9 | LATAM Airlines | 1646 |
| 10 | Lufthansa | 1592 |
| 11 | AZU | 1581 |
| 12 | WIF | 1485 |
| 13 | Vueling | 1467 |
| 14 | LXJ | 1395 |
| 15 | Swiss International | 1212 |
| 16 | AXM | 1207 |
| 17 | easyJet | 1206 |
| 18 | QLK | 1093 |
| 19 | All Nippon Airways | 1087 |
| 20 | EJU | 1084 |
| 21 | Alaska Airlines | 1081 |
| 22 | VIV | 979 |
| 23 | Cathay Pacific | 946 |
| 24 | CXK | 942 |
| 25 | GLO | 939 |
| 26 | AEE | 927 |
| 27 | United Airlines | 918 |
| 28 | Air France | 916 |
| 29 | MXY | 896 |
| 30 | PGT | 881 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 152732 |
| 2 | 🇪🇸 ES | 11393 |
| 3 | 🇧🇷 BR | 10138 |
| 4 | 🇦🇺 AU | 10066 |
| 5 | 🇮🇳 IN | 9794 |
| 6 | 🇨🇦 CA | 9727 |
| 7 | 🇮🇹 IT | 9199 |
| 8 | 🇩🇪 DE | 8794 |
| 9 | 🇬🇧 GB | 8201 |
| 10 | 🇯🇵 JP | 7210 |
| 11 | 🇫🇷 FR | 7066 |
| 12 | 🇨🇴 CO | 6526 |
| 13 | 🇬🇷 GR | 5187 |
| 14 | 🇲🇽 MX | 5097 |
| 15 | 🇨🇭 CH | 4720 |
| 16 | 🇳🇴 NO | 4618 |
| 17 | 🇹🇷 TR | 4453 |
| 18 | 🇲🇾 MY | 3150 |
| 19 | 🇵🇱 PL | 2959 |
| 20 | 🇿🇦 ZA | 2894 |
| 21 | 🇹🇭 TH | 2682 |
| 22 | 🇳🇿 NZ | 2582 |
| 23 | 🇵🇭 PH | 2358 |
| 24 | 🇬🇹 GT | 2270 |
| 25 | 🇰🇷 KR | 2229 |
| 26 | 🇲🇦 MA | 1796 |
| 27 | 🇭🇷 HR | 1756 |
| 28 | 🇲🇪 ME | 1619 |
| 29 | 🇳🇱 NL | 1603 |
| 30 | 🇲🇴 MO | 1509 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3673 |
| 2 | Denver International Airport |  | US | 2948 |
| 3 | Tokyo International Airport |  | JP | 2240 |
| 4 | Indira Gandhi International Airport |  | IN | 2179 |
| 5 | Guaymaral Airport |  | CO | 2177 |
| 6 | Harry Reid International Airport |  | US | 2113 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1922 |
| 8 | Zurich Airport |  | CH | 1887 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1854 |
| 10 | La Aurora Airport |  | GT | 1745 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1627 |
| 12 | Chicago O'Hare International Airport |  | US | 1599 |
| 13 | Salt Lake City International Airport |  | US | 1591 |
| 14 | El Dorado International Airport |  | CO | 1584 |
| 15 | Frankfurt am Main International Airport |  | DE | 1555 |
| 16 | Macau International Airport |  | MO | 1509 |
| 17 | Congonhas Airport |  | BR | 1471 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1428 |
| 19 | Capua Airport |  | IT | 1393 |
| 20 | Madrid Barajas International Airport |  | ES | 1388 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1322 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1255 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1248 |
| 24 | Malpensa International Airport |  | IT | 1219 |
| 25 | Charlotte/Douglas International Airport |  | US | 1212 |
| 26 | Charles de Gaulle International Airport |  | FR | 1207 |
| 27 | Kuala Lumpur International Airport |  | MY | 1186 |
| 28 | Bengaluru International Airport |  | IN | 1166 |
| 29 | Ninoy Aquino International Airport |  | PH | 1109 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1103 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1098 |
| 32 | Barcelona International Airport |  | ES | 1057 |
| 33 | Daniel K Inouye International Airport |  | US | 1025 |
| 34 | Seattle-Tacoma International Airport |  | US | 1025 |
| 35 | Viracopos International Airport |  | BR | 1016 |
| 36 | Reno/Tahoe International Airport |  | US | 1014 |
| 37 | Calgary International Airport |  | CA | 1012 |
| 38 | Oslo Gardermoen Airport |  | NO | 991 |
| 39 | Tenerife Norte Airport |  | ES | 974 |
| 40 | Amsterdam Airport Schiphol |  | NL | 962 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 899 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 655 | 21m | 244 km | 2,758.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 420 | 24m | 225 km | 1,629.4 t |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 417 | 1h 8m | 770 km | 5,539.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 414 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 299 | 27m | 275 km | 1,416.8 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 294 | 1h 7m | 706 km | 3,579.5 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 270 | 44m | 241 km | 1,121.5 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 246 | 1h 48m | 1,423 km | 6,037.2 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 231 | 20m | 250 km | 997.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 225 | 26m | 215 km | 833.3 t |
| 19 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 223 | 8m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 220 | 20m | 99 km | 376.8 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 215 | 51m | 556 km | 2,061.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 212 | 1h 15m | 961 km | 3,514.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 212 | 19m | 144 km | 527.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 208 | 1h 38m | 1,156 km | 4,149.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 208 | 12m | - | - |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 206 | 31m | 369 km | 1,311.2 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 203 | 24m | 218 km | 764.8 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 201 | 28m | 152 km | 525.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 194 | 1h 2m | 695 km | 2,325.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-08 10:28 UTC | 2026-08-08 10:39 UTC | 11m |
| GCKTE | GCK | Warton Airport (EGNO) | Warton Airport (EGNO) | 2026-08-08 09:56 UTC | 2026-08-08 10:39 UTC | 42m |
| ABF8 | ABF | Nice-Cote d'Azur Airport (LFMN) | Helsinki Vantaa Airport (EFHK) | 2026-08-08 07:29 UTC | 2026-08-08 10:25 UTC | 2h 56m |
| N208PC |  | Hohenems-Dornbirn Airport (LOIH) | Hohenems-Dornbirn Airport (LOIH) | 2026-08-08 07:56 UTC | 2026-08-08 10:19 UTC | 2h 23m |
| DESSC | DES | Friedrichshafen Airport (EDNY) | Friedrichshafen Airport (EDNY) | 2026-08-08 09:46 UTC | 2026-08-08 10:18 UTC | 32m |
| HB3246 |  | Zweisimmen Airport (LSTZ) | Saanen Airport (LSGK) | 2026-08-08 09:23 UTC | 2026-08-08 10:10 UTC | 47m |
| N520EM |  | London Luton Airport (EGGW) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-08 08:17 UTC | 2026-08-08 10:06 UTC | 1h 48m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-08 09:49 UTC | 2026-08-08 10:04 UTC | 14m |
| CHX1 | CHX | Oberschleisheim Airfield (EDNX) | Oberschleisheim Airfield (EDNX) | 2026-08-08 09:40 UTC | 2026-08-08 10:02 UTC | 21m |
| UBG310 | UBG | VGZR (VGZR) | Naypyidaw Airport (VYEL) | 2026-08-08 02:30 UTC | 2026-08-08 10:02 UTC | 7h 31m |
| RGA17 | RGA | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-08-08 09:53 UTC | 2026-08-08 10:01 UTC | 8m |
| CAN1O | CAN | Ciampino Airport (LIRA) | L'Aquila / Preturo Airport (LIAP) | 2026-08-08 07:39 UTC | 2026-08-08 09:59 UTC | 2h 20m |
| MOONL | MOO | Ben Gurion International Airport (LLBG) | Corte Airport (LFKT) | 2026-08-08 06:53 UTC | 2026-08-08 09:55 UTC | 3h 1m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-08-08 09:43 UTC | 2026-08-08 09:51 UTC | 7m |
| IBX65 | IBX | Matsumoto Airport (RJAF) | Iwami Airport (RJOW) | 2026-08-08 09:14 UTC | 2026-08-08 09:50 UTC | 35m |
| A6FTT |  | Al Minhad Air Base (OMDM) | Al Maktoum International Airport (OMDW) | 2026-08-08 08:48 UTC | 2026-08-08 09:49 UTC | 1h 0m |
| DMBIY | DMB | Saulgau Airport (EDTU) | Mengen-Hohentengen Airport (EDTM) | 2026-08-08 08:57 UTC | 2026-08-08 09:48 UTC | 51m |
| LDX12C | LDX | Vienna International Airport (LOWW) | Samedan Airport (LSZS) | 2026-08-08 09:00 UTC | 2026-08-08 09:46 UTC | 45m |
| HUE40H | HUE | Nice-Cote d'Azur Airport (LFMN) | Sion Airport (LSGS) | 2026-08-08 08:55 UTC | 2026-08-08 09:44 UTC | 49m |
| FGOBR | FGO | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | 2026-08-08 09:35 UTC | 2026-08-08 09:43 UTC | 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
