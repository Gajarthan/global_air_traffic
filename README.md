# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_10:54:05_UTC-green)

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

**Latest saved flight:** 2026-08-20 10:54:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 10:54:05 UTC

- **218,857** saved flights
- **68,810** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **218,857** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,635,931.0 tonnes** estimated CO2 emissions
- **152,807,595 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8772 |
| 2 | SkyWest Airlines | 7813 |
| 3 | EJA | 4247 |
| 4 | IndiGo | 3717 |
| 5 | American Airlines | 3637 |
| 6 | Southwest Airlines | 3470 |
| 7 | Delta Air Lines | 2823 |
| 8 | ENY | 2698 |
| 9 | LATAM Airlines | 2070 |
| 10 | AZU | 2004 |
| 11 | Vueling | 1840 |
| 12 | Lufthansa | 1818 |
| 13 | WIF | 1749 |
| 14 | LXJ | 1728 |
| 15 | easyJet | 1516 |
| 16 | Swiss International | 1457 |
| 17 | AXM | 1436 |
| 18 | United Airlines | 1382 |
| 19 | QLK | 1375 |
| 20 | EJU | 1367 |
| 21 | Alaska Airlines | 1339 |
| 22 | All Nippon Airways | 1318 |
| 23 | VIV | 1196 |
| 24 | Air France | 1190 |
| 25 | GLO | 1188 |
| 26 | PGT | 1185 |
| 27 | WMT | 1151 |
| 28 | Wizz Air | 1115 |
| 29 | JetBlue | 1112 |
| 30 | AEE | 1097 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 184200 |
| 2 | 🇪🇸 ES | 14012 |
| 3 | 🇧🇷 BR | 12607 |
| 4 | 🇦🇺 AU | 12404 |
| 5 | 🇨🇦 CA | 12074 |
| 6 | 🇮🇹 IT | 11656 |
| 7 | 🇮🇳 IN | 11586 |
| 8 | 🇩🇪 DE | 10815 |
| 9 | 🇬🇧 GB | 10266 |
| 10 | 🇨🇴 CO | 8981 |
| 11 | 🇯🇵 JP | 8954 |
| 12 | 🇫🇷 FR | 8725 |
| 13 | 🇬🇷 GR | 6381 |
| 14 | 🇹🇷 TR | 6299 |
| 15 | 🇲🇽 MX | 6095 |
| 16 | 🇨🇭 CH | 5800 |
| 17 | 🇳🇴 NO | 5432 |
| 18 | 🇲🇾 MY | 3797 |
| 19 | 🇿🇦 ZA | 3715 |
| 20 | 🇵🇱 PL | 3621 |
| 21 | 🇹🇭 TH | 3618 |
| 22 | 🇳🇿 NZ | 3041 |
| 23 | 🇵🇭 PH | 2955 |
| 24 | 🇬🇹 GT | 2767 |
| 25 | 🇰🇷 KR | 2629 |
| 26 | 🇭🇷 HR | 2409 |
| 27 | 🇲🇦 MA | 2202 |
| 28 | 🇳🇱 NL | 1944 |
| 29 | 🇲🇪 ME | 1926 |
| 30 | 🇮🇩 ID | 1857 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4591 |
| 2 | Denver International Airport |  | US | 3578 |
| 3 | Tokyo International Airport |  | JP | 2687 |
| 4 | Indira Gandhi International Airport |  | IN | 2656 |
| 5 | Guaymaral Airport |  | CO | 2595 |
| 6 | Harry Reid International Airport |  | US | 2416 |
| 7 | Zurich Airport |  | CH | 2271 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2245 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2225 |
| 10 | La Aurora Airport |  | GT | 2106 |
| 11 | El Dorado International Airport |  | CO | 2053 |
| 12 | Chicago O'Hare International Airport |  | US | 2007 |
| 13 | Salt Lake City International Airport |  | US | 1931 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1900 |
| 15 | Congonhas Airport |  | BR | 1842 |
| 16 | Frankfurt am Main International Airport |  | DE | 1782 |
| 17 | Madrid Barajas International Airport |  | ES | 1713 |
| 18 | Capua Airport |  | IT | 1668 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1643 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1619 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1605 |
| 22 | Macau International Airport |  | MO | 1573 |
| 23 | Malpensa International Airport |  | IT | 1544 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1541 |
| 25 | Charles de Gaulle International Airport |  | FR | 1508 |
| 26 | Charlotte/Douglas International Airport |  | US | 1462 |
| 27 | Ninoy Aquino International Airport |  | PH | 1404 |
| 28 | Kuala Lumpur International Airport |  | MY | 1394 |
| 29 | Barcelona International Airport |  | ES | 1343 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1331 |
| 31 | Bengaluru International Airport |  | IN | 1321 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1306 |
| 33 | Seattle-Tacoma International Airport |  | US | 1299 |
| 34 | Viracopos International Airport |  | BR | 1279 |
| 35 | Calgary International Airport |  | CA | 1235 |
| 36 | Vitoria/Foronda Airport |  | ES | 1212 |
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
| CAN11 | CAN | Pescara International Airport (LIBP) | Pescara International Airport (LIBP) | 2026-08-20 10:22 UTC | 2026-08-20 10:54 UTC | 31m |
| DHK238 | DHK | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-08-20 00:35 UTC | 2026-08-20 10:52 UTC | 10h 17m |
| AZU2713 | AZU | Viracopos International Airport (SBKP) | Fazenda Cachoeira do Lontra Airport (SINS) | 2026-08-20 09:14 UTC | 2026-08-20 10:50 UTC | 1h 36m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-08-19 20:00 UTC | 2026-08-20 10:50 UTC | 14h 49m |
| CHRI33 | CHR | Spitzerberg Airport (LOAS) | Altlichtenwarth Airport (LOAR) | 2026-08-20 10:27 UTC | 2026-08-20 10:41 UTC | 13m |
| UPS806 | UPS | Ontario International Airport (KONT) | Denver International Airport (KDEN) | 2026-08-20 08:56 UTC | 2026-08-20 10:39 UTC | 1h 43m |
| CAN18 | CAN | Pescara International Airport (LIBP) | Pescara International Airport (LIBP) | 2026-08-20 10:22 UTC | 2026-08-20 10:33 UTC | 10m |
| JZR532 | JZR | VGZR (VGZR) | UKFB (UKFB) | 2026-08-19 23:03 UTC | 2026-08-20 10:28 UTC | 11h 24m |
| FGOBR | FGO | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | 2026-08-20 09:46 UTC | 2026-08-20 10:18 UTC | 31m |
| BO11 |  | Futenma Marine Corps Air Station (ROTM) | Kadena Air Base (RODN) | 2026-08-20 09:22 UTC | 2026-08-20 10:16 UTC | 54m |
| RYR8FV | Ryanair | Girona Airport (LEGE) | Grefrath-Niershorst Airport (EDLF) | 2026-08-20 08:32 UTC | 2026-08-20 10:13 UTC | 1h 41m |
| BOX732 | BOX | Dubai International Airport (OMDB) | Macau International Airport (VMMC) | 2026-08-20 03:23 UTC | 2026-08-20 10:13 UTC | 6h 49m |
| TUTOR64 | TUT | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-20 09:45 UTC | 2026-08-20 10:10 UTC | 24m |
| CCM83H | CCM | Ajaccio-Napoleon Bonaparte Airport (LFKJ) | Ambert Le Poyet Airport (LFHT) | 2026-08-20 08:37 UTC | 2026-08-20 10:10 UTC | 1h 32m |
| EAI17W | EAI | Manchester Airport (EGCC) | Dublin Airport (EIDW) | 2026-08-20 08:45 UTC | 2026-08-20 10:09 UTC | 1h 24m |
| SWBLD1 | SWB | Middle Wallop Airfield (EGVP) | Upavon Aerodrome (EGDJ) | 2026-08-20 09:43 UTC | 2026-08-20 10:07 UTC | 23m |
| UAE382 | Emirates | Dubai International Airport (OMDB) | Macau International Airport (VMMC) | 2026-08-20 03:18 UTC | 2026-08-20 10:05 UTC | 6h 46m |
| LOT3FG | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Václav Havel Airport (LKPR) | 2026-08-20 09:04 UTC | 2026-08-20 10:01 UTC | 57m |
| DHK362 | DHK | Leipzig Halle Airport (EDDP) | John F Kennedy International Airport (KJFK) | 2026-08-20 01:49 UTC | 2026-08-20 10:00 UTC | 8h 11m |
| UPS802 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Denver International Airport (KDEN) | 2026-08-20 07:41 UTC | 2026-08-20 09:58 UTC | 2h 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
