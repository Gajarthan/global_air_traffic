# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_10:28:55_UTC-green)

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

**Latest saved flight:** 2026-08-20 10:28:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 10:28:55 UTC

- **218,791** saved flights
- **68,800** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **218,791** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,634,516.7 tonnes** estimated CO2 emissions
- **152,725,604 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8765 |
| 2 | SkyWest Airlines | 7813 |
| 3 | EJA | 4247 |
| 4 | IndiGo | 3716 |
| 5 | American Airlines | 3637 |
| 6 | Southwest Airlines | 3470 |
| 7 | Delta Air Lines | 2823 |
| 8 | ENY | 2698 |
| 9 | LATAM Airlines | 2069 |
| 10 | AZU | 2002 |
| 11 | Vueling | 1840 |
| 12 | Lufthansa | 1818 |
| 13 | WIF | 1749 |
| 14 | LXJ | 1728 |
| 15 | easyJet | 1516 |
| 16 | Swiss International | 1456 |
| 17 | AXM | 1435 |
| 18 | United Airlines | 1382 |
| 19 | QLK | 1375 |
| 20 | EJU | 1366 |
| 21 | Alaska Airlines | 1339 |
| 22 | All Nippon Airways | 1318 |
| 23 | VIV | 1196 |
| 24 | GLO | 1188 |
| 25 | Air France | 1187 |
| 26 | PGT | 1185 |
| 27 | WMT | 1149 |
| 28 | JetBlue | 1112 |
| 29 | Wizz Air | 1111 |
| 30 | AEE | 1096 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 184195 |
| 2 | 🇪🇸 ES | 14003 |
| 3 | 🇧🇷 BR | 12601 |
| 4 | 🇦🇺 AU | 12400 |
| 5 | 🇨🇦 CA | 12074 |
| 6 | 🇮🇹 IT | 11646 |
| 7 | 🇮🇳 IN | 11581 |
| 8 | 🇩🇪 DE | 10807 |
| 9 | 🇬🇧 GB | 10255 |
| 10 | 🇨🇴 CO | 8981 |
| 11 | 🇯🇵 JP | 8951 |
| 12 | 🇫🇷 FR | 8717 |
| 13 | 🇬🇷 GR | 6378 |
| 14 | 🇹🇷 TR | 6295 |
| 15 | 🇲🇽 MX | 6095 |
| 16 | 🇨🇭 CH | 5798 |
| 17 | 🇳🇴 NO | 5432 |
| 18 | 🇲🇾 MY | 3794 |
| 19 | 🇿🇦 ZA | 3713 |
| 20 | 🇵🇱 PL | 3619 |
| 21 | 🇹🇭 TH | 3614 |
| 22 | 🇳🇿 NZ | 3041 |
| 23 | 🇵🇭 PH | 2954 |
| 24 | 🇬🇹 GT | 2767 |
| 25 | 🇰🇷 KR | 2629 |
| 26 | 🇭🇷 HR | 2406 |
| 27 | 🇲🇦 MA | 2199 |
| 28 | 🇳🇱 NL | 1944 |
| 29 | 🇲🇪 ME | 1923 |
| 30 | 🇮🇩 ID | 1856 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4591 |
| 2 | Denver International Airport |  | US | 3577 |
| 3 | Tokyo International Airport |  | JP | 2686 |
| 4 | Indira Gandhi International Airport |  | IN | 2654 |
| 5 | Guaymaral Airport |  | CO | 2595 |
| 6 | Harry Reid International Airport |  | US | 2416 |
| 7 | Zurich Airport |  | CH | 2270 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2245 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2224 |
| 10 | La Aurora Airport |  | GT | 2106 |
| 11 | El Dorado International Airport |  | CO | 2053 |
| 12 | Chicago O'Hare International Airport |  | US | 2007 |
| 13 | Salt Lake City International Airport |  | US | 1931 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1900 |
| 15 | Congonhas Airport |  | BR | 1840 |
| 16 | Frankfurt am Main International Airport |  | DE | 1782 |
| 17 | Madrid Barajas International Airport |  | ES | 1712 |
| 18 | Capua Airport |  | IT | 1666 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1643 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1619 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1605 |
| 22 | Macau International Airport |  | MO | 1570 |
| 23 | Malpensa International Airport |  | IT | 1544 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1541 |
| 25 | Charles de Gaulle International Airport |  | FR | 1504 |
| 26 | Charlotte/Douglas International Airport |  | US | 1462 |
| 27 | Ninoy Aquino International Airport |  | PH | 1403 |
| 28 | Kuala Lumpur International Airport |  | MY | 1393 |
| 29 | Barcelona International Airport |  | ES | 1341 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1331 |
| 31 | Bengaluru International Airport |  | IN | 1320 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1306 |
| 33 | Seattle-Tacoma International Airport |  | US | 1299 |
| 34 | Viracopos International Airport |  | BR | 1278 |
| 35 | Calgary International Airport |  | CA | 1235 |
| 36 | Oslo Gardermoen Airport |  | NO | 1211 |
| 37 | Vitoria/Foronda Airport |  | ES | 1210 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1201 |
| 39 | Don Mueang International Airport |  | TH | 1192 |
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
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 366 | 27m | 275 km | 1,734.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 321 | 1h 50m | 1,423 km | 7,877.8 t |
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
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 246 | 12m | - | - |
| 27 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 244 | 44m | 555 km | 2,336.4 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 236 | 1h 49m | 1,304 km | 5,309.4 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JZR532 | JZR | VGZR (VGZR) | UKFB (UKFB) | 2026-08-19 23:03 UTC | 2026-08-20 10:28 UTC | 11h 24m |
| FGOBR | FGO | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | 2026-08-20 09:46 UTC | 2026-08-20 10:18 UTC | 31m |
| BO11 |  | Futenma Marine Corps Air Station (ROTM) | Kadena Air Base (RODN) | 2026-08-20 09:22 UTC | 2026-08-20 10:16 UTC | 54m |
| BOX732 | BOX | Dubai International Airport (OMDB) | Macau International Airport (VMMC) | 2026-08-20 03:23 UTC | 2026-08-20 10:13 UTC | 6h 49m |
| TUTOR64 | TUT | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-20 09:45 UTC | 2026-08-20 10:10 UTC | 24m |
| SWBLD1 | SWB | Middle Wallop Airfield (EGVP) | Upavon Aerodrome (EGDJ) | 2026-08-20 09:43 UTC | 2026-08-20 10:07 UTC | 23m |
| UAE382 | Emirates | Dubai International Airport (OMDB) | Macau International Airport (VMMC) | 2026-08-20 03:18 UTC | 2026-08-20 10:05 UTC | 6h 46m |
| DHK362 | DHK | Leipzig Halle Airport (EDDP) | John F Kennedy International Airport (KJFK) | 2026-08-20 01:49 UTC | 2026-08-20 10:00 UTC | 8h 11m |
| UPS802 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Denver International Airport (KDEN) | 2026-08-20 07:41 UTC | 2026-08-20 09:58 UTC | 2h 17m |
| AP95 |  | Campo Fontenelle Airport (SBYS) | Casa Branca Airport (SDKB) | 2026-08-20 09:53 UTC | 2026-08-20 09:56 UTC | 3m |
| OEELA | OEE | Salzburg Airport (LOWS) | Voslau Airport (LOAV) | 2026-08-20 09:13 UTC | 2026-08-20 09:49 UTC | 36m |
| CWA922 | CWA | Calgary International Airport (CYYC) | Bawlf (Blackwells) Airport (CFR2) | 2026-08-20 09:19 UTC | 2026-08-20 09:47 UTC | 27m |
| UPS474 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Montréal (Mirabel) Airport (CYMX) | 2026-08-20 08:13 UTC | 2026-08-20 09:46 UTC | 1h 32m |
| MKELY | MKE | Jersey Airport (EGJJ) | Ireland West Knock Airport (EIKN) | 2026-08-20 08:37 UTC | 2026-08-20 09:45 UTC | 1h 7m |
| JFA24E | JFA | Bern Belp Airport (LSZB) | Sion Airport (LSGS) | 2026-08-20 09:27 UTC | 2026-08-20 09:44 UTC | 16m |
| EJU95LQ | EJU | Madeira Airport (LPMA) | Alijo Airport (LPJO) | 2026-08-20 07:48 UTC | 2026-08-20 09:43 UTC | 1h 55m |
| URSA01 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-20 08:09 UTC | 2026-08-20 09:42 UTC | 1h 33m |
| SUBUO | SUB | El Alamein International Airport (HEAL) | El Alamein International Airport (HEAL) | 2026-08-20 09:36 UTC | 2026-08-20 09:41 UTC | 4m |
| TSU831 | TSU | Lincoln Airport (KLNK) | Branhams Airport (K6J7) | 2026-08-20 07:33 UTC | 2026-08-20 09:40 UTC | 2h 6m |
| DAL154 | Delta Air Lines | General Edward Lawrence Logan International Airport (KBOS) | Dublin Airport (EIDW) | 2026-08-20 03:51 UTC | 2026-08-20 09:39 UTC | 5h 48m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
