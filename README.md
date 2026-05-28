# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--28_21:07:00_UTC-green)

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

**Latest saved flight:** 2026-05-28 21:07:00 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-28 21:07:00 UTC

- **96,183** saved flights
- **33,839** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **96,183** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,179,167.9 tonnes** estimated CO2 emissions
- **68,357,562 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4040 |
| 2 | SkyWest Airlines | 3580 |
| 3 | IndiGo | 1988 |
| 4 | EJA | 1821 |
| 5 | American Airlines | 1457 |
| 6 | Southwest Airlines | 1400 |
| 7 | ENY | 1185 |
| 8 | Lufthansa | 1150 |
| 9 | Delta Air Lines | 1053 |
| 10 | Vueling | 910 |
| 11 | LATAM Airlines | 864 |
| 12 | AXM | 848 |
| 13 | WIF | 847 |
| 14 | AZU | 772 |
| 15 | LXJ | 734 |
| 16 | Swiss International | 716 |
| 17 | All Nippon Airways | 709 |
| 18 | Alaska Airlines | 668 |
| 19 | QLK | 663 |
| 20 | easyJet | 632 |
| 21 | EJU | 613 |
| 22 | Cathay Pacific | 582 |
| 23 | AEE | 579 |
| 24 | Air France | 566 |
| 25 | VIV | 566 |
| 26 | CXK | 514 |
| 27 | MXY | 510 |
| 28 | Japan Airlines | 493 |
| 29 | AXB | 486 |
| 30 | AIQ | 462 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 79582 |
| 2 | 🇪🇸 ES | 6724 |
| 3 | 🇮🇳 IN | 6276 |
| 4 | 🇦🇺 AU | 5880 |
| 5 | 🇧🇷 BR | 5286 |
| 6 | 🇩🇪 DE | 5268 |
| 7 | 🇮🇹 IT | 5202 |
| 8 | 🇨🇦 CA | 4884 |
| 9 | 🇯🇵 JP | 4584 |
| 10 | 🇬🇧 GB | 4122 |
| 11 | 🇫🇷 FR | 3900 |
| 12 | 🇨🇴 CO | 3343 |
| 13 | 🇲🇽 MX | 2954 |
| 14 | 🇬🇷 GR | 2773 |
| 15 | 🇳🇴 NO | 2694 |
| 16 | 🇨🇭 CH | 2527 |
| 17 | 🇲🇾 MY | 2152 |
| 18 | 🇹🇷 TR | 1784 |
| 19 | 🇿🇦 ZA | 1723 |
| 20 | 🇳🇿 NZ | 1636 |
| 21 | 🇹🇭 TH | 1625 |
| 22 | 🇰🇷 KR | 1580 |
| 23 | 🇵🇱 PL | 1569 |
| 24 | 🇵🇭 PH | 1444 |
| 25 | 🇬🇹 GT | 1439 |
| 26 | 🇲🇦 MA | 1091 |
| 27 | 🇲🇴 MO | 1038 |
| 28 | 🇳🇱 NL | 968 |
| 29 | 🇲🇪 ME | 946 |
| 30 | 🇭🇷 HR | 871 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2084 |
| 2 | Denver International Airport |  | US | 1629 |
| 3 | Tokyo International Airport |  | JP | 1521 |
| 4 | Indira Gandhi International Airport |  | IN | 1359 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1271 |
| 6 | Harry Reid International Airport |  | US | 1239 |
| 7 | Guaymaral Airport |  | CO | 1184 |
| 8 | Frankfurt am Main International Airport |  | DE | 1160 |
| 9 | Zurich Airport |  | CH | 1122 |
| 10 | La Aurora Airport |  | GT | 1103 |
| 11 | El Dorado International Airport |  | CO | 1041 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1039 |
| 13 | Macau International Airport |  | MO | 1038 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 966 |
| 15 | Chicago O'Hare International Airport |  | US | 925 |
| 16 | Madrid Barajas International Airport |  | ES | 853 |
| 17 | Kuala Lumpur International Airport |  | MY | 853 |
| 18 | Salt Lake City International Airport |  | US | 811 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 809 |
| 20 | Capua Airport |  | IT | 799 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 763 |
| 22 | Malpensa International Airport |  | IT | 753 |
| 23 | Bengaluru International Airport |  | IN | 752 |
| 24 | Charles de Gaulle International Airport |  | FR | 748 |
| 25 | Congonhas Airport |  | BR | 733 |
| 26 | Charlotte/Douglas International Airport |  | US | 730 |
| 27 | Daniel K Inouye International Airport |  | US | 684 |
| 28 | Tenerife Norte Airport |  | ES | 682 |
| 29 | Ninoy Aquino International Airport |  | PH | 659 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 644 |
| 31 | Barcelona International Airport |  | ES | 643 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 622 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 616 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 601 |
| 35 | Amsterdam Airport Schiphol |  | NL | 596 |
| 36 | Vitoria/Foronda Airport |  | ES | 594 |
| 37 | Don Mueang International Airport |  | TH | 593 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 570 |
| 39 | Calgary International Airport |  | CA | 566 |
| 40 | O. R. Tambo International Airport |  | ZA | 548 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 487 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 354 | 21m | 244 km | 1,490.6 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 260 | 24m | 225 km | 1,008.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 256 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 245 | 14m | 114 km | 480.5 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 242 | 1h 26m | 910 km | 3,797.5 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 240 | 28m | 304 km | 1,258.1 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 221 | 1h 10m | 770 km | 2,935.8 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 208 | 19m | 165 km | 591.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 192 | 26m | 275 km | 909.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 154 | 21m | 99 km | 263.8 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 144 | 27m | 215 km | 533.3 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 142 | 44m | 452 km | 1,106.7 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 138 | 22m | 55 km | 131.2 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 138 | 27m | 152 km | 360.6 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 130 | 20m | 250 km | 561.5 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 129 | 20m | 147 km | 326.4 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 125 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 123 | 1h 1m | 695 km | 1,474.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 123 | 18m | 144 km | 306.0 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 122 | 1h 39m | 1,156 km | 2,433.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 52m | 1,304 km | 2,609.7 t |
| 27 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 114 | 1h 18m | 961 km | 1,889.6 t |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N402WD |  | Rabb Dusting Inc Airport (XS66) | Cabaniss Field Nolf Airport (KNGW) | 2026-05-28 20:31 UTC | 2026-05-28 21:07 UTC | 35m |
| N419AM |  | Waukegan Ntl Airport (KUGN) | Waukegan Ntl Airport (KUGN) | 2026-05-28 20:22 UTC | 2026-05-28 21:04 UTC | 41m |
| N447BL |  | Johnston Regional Airport (KJNX) | Rocky Mount/Wilson Regional Airport (KRWI) | 2026-05-28 20:02 UTC | 2026-05-28 21:00 UTC | 57m |
| N |  | Saskatoon John G. Diefenbaker International Airport (CYXE) | Saskatoon John G. Diefenbaker International Airport (CYXE) | 2026-05-28 19:56 UTC | 2026-05-28 20:58 UTC | 1h 1m |
| ICE5000 | ICE | Keflavik International Airport (BIKF) | Keflavik International Airport (BIKF) | 2026-05-28 20:08 UTC | 2026-05-28 20:55 UTC | 47m |
| CRN101T | CRN | Kelowna Airport (CYLW) | Penticton Airport (CYYF) | 2026-05-28 20:38 UTC | 2026-05-28 20:53 UTC | 14m |
| N78US |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-05-28 19:59 UTC | 2026-05-28 20:51 UTC | 52m |
| FFAB123 | FFA | Hoffman Airport (0CA5) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-05-28 19:25 UTC | 2026-05-28 20:47 UTC | 1h 22m |
| URSA01 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-05-28 19:25 UTC | 2026-05-28 20:44 UTC | 1h 18m |
| N36116 |  | Meriden Markham Municipal Airport (KMMK) | Windham Airport (KIJD) | 2026-05-28 20:18 UTC | 2026-05-28 20:43 UTC | 24m |
| FFL1617 | FFL | Teterboro Airport (KTEB) | Tweed/New Haven Airport (KHVN) | 2026-05-28 20:17 UTC | 2026-05-28 20:42 UTC | 24m |
| BOE101 | BOE | Zwainz Farms Airport (WA08) | WA15 (WA15) | 2026-05-28 20:22 UTC | 2026-05-28 20:40 UTC | 18m |
| N721KP |  | Atlin Airport (CYSQ) | Kake Airport (PAFE) | 2026-05-28 20:25 UTC | 2026-05-28 20:40 UTC | 14m |
| N698VJ |  | Lawrence County Airpark (KHTW) | Ashland Regional Airport (KDWU) | 2026-05-28 20:29 UTC | 2026-05-28 20:40 UTC | 10m |
| N348BA |  | Joe Foss Field (KFSD) | Wadena Municipal Airport (KADC) | 2026-05-28 20:06 UTC | 2026-05-28 20:35 UTC | 29m |
| RPA5707 | Republic Airways | Cincinnati/Northern Kentucky International Airport (KCVG) | General Edward Lawrence Logan International Airport (KBOS) | 2026-05-28 18:48 UTC | 2026-05-28 20:33 UTC | 1h 44m |
| N138BL |  | Johnston Regional Airport (KJNX) | Wayne Executive Jetport Airport (KGWW) | 2026-05-28 19:33 UTC | 2026-05-28 20:33 UTC | 59m |
| N7DW |  | Lee Airport (KANP) | MD09 (MD09) | 2026-05-28 20:20 UTC | 2026-05-28 20:33 UTC | 12m |
| N991AL |  | Zamperini Field (KTOA) | Zamperini Field (KTOA) | 2026-05-28 20:17 UTC | 2026-05-28 20:32 UTC | 15m |
| HK1479G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-05-28 20:13 UTC | 2026-05-28 20:31 UTC | 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
