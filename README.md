# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--19_16:09:35_UTC-green)

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

**Latest saved flight:** 2026-06-19 16:09:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-19 16:09:35 UTC

- **114,569** saved flights
- **39,734** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **114,569** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,394,581.4 tonnes** estimated CO2 emissions
- **80,845,301 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4724 |
| 2 | SkyWest Airlines | 4263 |
| 3 | EJA | 2217 |
| 4 | IndiGo | 2215 |
| 5 | American Airlines | 1798 |
| 6 | Southwest Airlines | 1700 |
| 7 | ENY | 1424 |
| 8 | Delta Air Lines | 1352 |
| 9 | Lufthansa | 1278 |
| 10 | Vueling | 1038 |
| 11 | WIF | 1020 |
| 12 | LATAM Airlines | 1010 |
| 13 | AZU | 959 |
| 14 | AXM | 950 |
| 15 | LXJ | 871 |
| 16 | Swiss International | 813 |
| 17 | All Nippon Airways | 792 |
| 18 | Alaska Airlines | 771 |
| 19 | QLK | 748 |
| 20 | easyJet | 735 |
| 21 | EJU | 718 |
| 22 | Cathay Pacific | 671 |
| 23 | AEE | 644 |
| 24 | United Airlines | 633 |
| 25 | VIV | 633 |
| 26 | Air France | 632 |
| 27 | CXK | 607 |
| 28 | MXY | 605 |
| 29 | AXB | 562 |
| 30 | GLO | 560 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 96569 |
| 2 | 🇪🇸 ES | 7827 |
| 3 | 🇮🇳 IN | 6991 |
| 4 | 🇦🇺 AU | 6817 |
| 5 | 🇧🇷 BR | 6330 |
| 6 | 🇮🇹 IT | 6142 |
| 7 | 🇩🇪 DE | 6134 |
| 8 | 🇨🇦 CA | 6000 |
| 9 | 🇯🇵 JP | 5158 |
| 10 | 🇬🇧 GB | 4964 |
| 11 | 🇫🇷 FR | 4555 |
| 12 | 🇨🇴 CO | 3938 |
| 13 | 🇲🇽 MX | 3377 |
| 14 | 🇬🇷 GR | 3266 |
| 15 | 🇳🇴 NO | 3169 |
| 16 | 🇨🇭 CH | 2927 |
| 17 | 🇲🇾 MY | 2458 |
| 18 | 🇹🇷 TR | 2310 |
| 19 | 🇿🇦 ZA | 1941 |
| 20 | 🇳🇿 NZ | 1888 |
| 21 | 🇰🇷 KR | 1878 |
| 22 | 🇵🇱 PL | 1875 |
| 23 | 🇹🇭 TH | 1871 |
| 24 | 🇵🇭 PH | 1667 |
| 25 | 🇬🇹 GT | 1630 |
| 26 | 🇲🇦 MA | 1249 |
| 27 | 🇲🇴 MO | 1168 |
| 28 | 🇲🇪 ME | 1128 |
| 29 | 🇳🇱 NL | 1112 |
| 30 | 🇭🇷 HR | 999 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2426 |
| 2 | Denver International Airport |  | US | 1939 |
| 3 | Tokyo International Airport |  | JP | 1712 |
| 4 | Indira Gandhi International Airport |  | IN | 1526 |
| 5 | Guaymaral Airport |  | CO | 1455 |
| 6 | Harry Reid International Airport |  | US | 1438 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1409 |
| 8 | Zurich Airport |  | CH | 1282 |
| 9 | La Aurora Airport |  | GT | 1257 |
| 10 | Frankfurt am Main International Airport |  | DE | 1247 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1229 |
| 12 | Macau International Airport |  | MO | 1168 |
| 13 | El Dorado International Airport |  | CO | 1164 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1141 |
| 15 | Chicago O'Hare International Airport |  | US | 1128 |
| 16 | Capua Airport |  | IT | 998 |
| 17 | Madrid Barajas International Airport |  | ES | 983 |
| 18 | Salt Lake City International Airport |  | US | 970 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 961 |
| 20 | Kuala Lumpur International Airport |  | MY | 952 |
| 21 | Charlotte/Douglas International Airport |  | US | 883 |
| 22 | Congonhas Airport |  | BR | 878 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 856 |
| 24 | Bengaluru International Airport |  | IN | 847 |
| 25 | Charles de Gaulle International Airport |  | FR | 845 |
| 26 | General Edward Lawrence Logan International Airport |  | US | 826 |
| 27 | Malpensa International Airport |  | IT | 822 |
| 28 | Ninoy Aquino International Airport |  | PH | 768 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 753 |
| 30 | Daniel K Inouye International Airport |  | US | 748 |
| 31 | Tenerife Norte Airport |  | ES | 744 |
| 32 | Barcelona International Airport |  | ES | 735 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 720 |
| 34 | Don Mueang International Airport |  | TH | 678 |
| 35 | Vitoria/Foronda Airport |  | ES | 677 |
| 36 | Amsterdam Airport Schiphol |  | NL | 677 |
| 37 | Calgary International Airport |  | CA | 672 |
| 38 | Seattle-Tacoma International Airport |  | US | 661 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 655 |
| 40 | Viracopos International Airport |  | BR | 655 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 604 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 414 | 21m | 244 km | 1,743.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 306 | 24m | 225 km | 1,187.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 297 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 285 | 1h 7m | 706 km | 3,469.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 282 | 1h 25m | 910 km | 4,425.2 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 279 | 14m | 114 km | 547.2 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 274 | 1h 10m | 770 km | 3,639.9 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 229 | 26m | 275 km | 1,085.1 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 227 | 19m | 165 km | 645.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 213 | 31m | - | - |
| 13 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 168 | 22m | 55 km | 159.7 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 168 | 20m | 99 km | 287.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 167 | 26m | 215 km | 618.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 156 | 27m | 152 km | 407.7 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 153 | 31m | 369 km | 973.9 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 152 | 44m | 452 km | 1,184.6 t |
| 21 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 150 | 44m | 241 km | 623.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 146 | 20m | 250 km | 630.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 137 | 1h 1m | 695 km | 1,642.2 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 134 | 1h 43m | 1,423 km | 3,288.6 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 134 | 1h 38m | 1,156 km | 2,673.2 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 130 | 13m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 129 | 1h 17m | 961 km | 2,138.2 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 128 | 12m | 99 km | 219.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N681MA |  | Sky Manor Airport (KN40) | Sky Manor Airport (KN40) | 2026-06-19 15:53 UTC | 2026-06-19 16:09 UTC | 16m |
| CXK1042 | CXK | Mesa Gateway Airport (KIWA) | Coolidge Municipal Airport (KP08) | 2026-06-19 14:58 UTC | 2026-06-19 16:03 UTC | 1h 4m |
| N360FA |  | Lehigh Valley International Airport (KABE) | Lancaster Airport (KLNS) | 2026-06-19 15:30 UTC | 2026-06-19 16:02 UTC | 32m |
| WDK45 | WDK | Fairoaks Airport (EGTF) | RAF Woodvale (EGOW) | 2026-06-19 14:48 UTC | 2026-06-19 16:02 UTC | 1h 14m |
| XBPBH | XBP | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-06-19 15:36 UTC | 2026-06-19 16:01 UTC | 25m |
| N366EA |  | Glendale Regional Airport (KGEU) | Indian Hills Airpark (2AZ1) | 2026-06-19 14:52 UTC | 2026-06-19 16:01 UTC | 1h 9m |
| N121GX |  | Aurora Municipal Airport (KARR) | 2LL9 (2LL9) | 2026-06-19 15:14 UTC | 2026-06-19 15:55 UTC | 41m |
| NDU19 | NDU | 7NA0 (7NA0) | Christianson Field (26MN) | 2026-06-19 15:32 UTC | 2026-06-19 15:55 UTC | 22m |
| N4347R |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-06-19 15:37 UTC | 2026-06-19 15:52 UTC | 14m |
| SPVAN | SPV | Słupsk-Krępa Airport (EPSR) | Słupsk-Krępa Airport (EPSR) | 2026-06-19 15:14 UTC | 2026-06-19 15:51 UTC | 36m |
| OEASE | OEA | EDJG (EDJG) | Nuremberg Airport (EDDN) | 2026-06-19 14:33 UTC | 2026-06-19 15:49 UTC | 1h 16m |
| N54858 |  | Frederick Municipal Airport (KFDK) | Hagerstown Regional/Richard A Henson Field (KHGR) | 2026-06-19 15:03 UTC | 2026-06-19 15:48 UTC | 44m |
| RPA5745 | Republic Airways | Laguardia Airport (KLGA) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-19 15:09 UTC | 2026-06-19 15:46 UTC | 37m |
| N24144 |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-06-19 15:21 UTC | 2026-06-19 15:46 UTC | 24m |
| EJA314 | EJA | Toronto Pearson International Airport (CYYZ) | Toronto Pearson International Airport (CYYZ) | 2026-06-19 15:31 UTC | 2026-06-19 15:46 UTC | 14m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-06-19 15:20 UTC | 2026-06-19 15:45 UTC | 25m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-06-19 15:28 UTC | 2026-06-19 15:45 UTC | 16m |
| ERU22 | ERU | Massey Farm Airport (AZ34) | Lake Havasu City Airport (KHII) | 2026-06-19 15:30 UTC | 2026-06-19 15:44 UTC | 14m |
| JBU1151 | JetBlue | Nantucket Memorial Airport (KACK) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-19 15:20 UTC | 2026-06-19 15:42 UTC | 22m |
| N690JK |  | Truckee-Tahoe Airport (KTRK) | Truckee-Tahoe Airport (KTRK) | 2026-06-19 15:27 UTC | 2026-06-19 15:42 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
