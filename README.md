# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--02_04:47:37_UTC-green)

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

**Latest saved flight:** 2026-09-02 04:47:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-02 04:47:37 UTC

- **244,419** saved flights
- **73,975** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **244,419** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,945,819.9 tonnes** estimated CO2 emissions
- **170,772,168 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9801 |
| 2 | SkyWest Airlines | 8566 |
| 3 | EJA | 4721 |
| 4 | IndiGo | 4096 |
| 5 | American Airlines | 3930 |
| 6 | Southwest Airlines | 3665 |
| 7 | Delta Air Lines | 3112 |
| 8 | ENY | 2939 |
| 9 | LATAM Airlines | 2344 |
| 10 | AZU | 2273 |
| 11 | Vueling | 2092 |
| 12 | Lufthansa | 1956 |
| 13 | WIF | 1947 |
| 14 | LXJ | 1887 |
| 15 | easyJet | 1698 |
| 16 | Swiss International | 1646 |
| 17 | AXM | 1610 |
| 18 | EJU | 1570 |
| 19 | QLK | 1563 |
| 20 | United Airlines | 1538 |
| 21 | Alaska Airlines | 1462 |
| 22 | All Nippon Airways | 1441 |
| 23 | WMT | 1371 |
| 24 | GLO | 1366 |
| 25 | PGT | 1337 |
| 26 | VIV | 1337 |
| 27 | Air France | 1333 |
| 28 | Wizz Air | 1326 |
| 29 | AEE | 1207 |
| 30 | JetBlue | 1205 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 202549 |
| 2 | 🇪🇸 ES | 15688 |
| 3 | 🇧🇷 BR | 14247 |
| 4 | 🇦🇺 AU | 13900 |
| 5 | 🇨🇦 CA | 13605 |
| 6 | 🇮🇹 IT | 13375 |
| 7 | 🇮🇳 IN | 12771 |
| 8 | 🇩🇪 DE | 12048 |
| 9 | 🇬🇧 GB | 11529 |
| 10 | 🇨🇴 CO | 10586 |
| 11 | 🇫🇷 FR | 9853 |
| 12 | 🇯🇵 JP | 9746 |
| 13 | 🇹🇷 TR | 7271 |
| 14 | 🇬🇷 GR | 7208 |
| 15 | 🇲🇽 MX | 6734 |
| 16 | 🇨🇭 CH | 6566 |
| 17 | 🇳🇴 NO | 6053 |
| 18 | 🇹🇭 TH | 4416 |
| 19 | 🇲🇾 MY | 4320 |
| 20 | 🇿🇦 ZA | 4247 |
| 21 | 🇵🇱 PL | 4104 |
| 22 | 🇳🇿 NZ | 3359 |
| 23 | 🇵🇭 PH | 3350 |
| 24 | 🇬🇹 GT | 3070 |
| 25 | 🇰🇷 KR | 2869 |
| 26 | 🇭🇷 HR | 2814 |
| 27 | 🇲🇦 MA | 2470 |
| 28 | 🇲🇪 ME | 2282 |
| 29 | 🇳🇱 NL | 2212 |
| 30 | 🇮🇩 ID | 2128 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5038 |
| 2 | Denver International Airport |  | US | 3939 |
| 3 | Indira Gandhi International Airport |  | IN | 2981 |
| 4 | Tokyo International Airport |  | JP | 2904 |
| 5 | Guaymaral Airport |  | CO | 2713 |
| 6 | Harry Reid International Airport |  | US | 2601 |
| 7 | Zurich Airport |  | CH | 2566 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2490 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2435 |
| 10 | El Dorado International Airport |  | CO | 2406 |
| 11 | La Aurora Airport |  | GT | 2335 |
| 12 | Salt Lake City International Airport |  | US | 2165 |
| 13 | Chicago O'Hare International Airport |  | US | 2161 |
| 14 | Congonhas Airport |  | BR | 2087 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2024 |
| 16 | Frankfurt am Main International Airport |  | DE | 1927 |
| 17 | Capua Airport |  | IT | 1922 |
| 18 | Madrid Barajas International Airport |  | ES | 1921 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1836 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1799 |
| 21 | Malpensa International Airport |  | IT | 1747 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1721 |
| 23 | Charles de Gaulle International Airport |  | FR | 1717 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1713 |
| 25 | Macau International Airport |  | MO | 1632 |
| 26 | Ninoy Aquino International Airport |  | PH | 1630 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1572 |
| 28 | Charlotte/Douglas International Airport |  | US | 1560 |
| 29 | Kuala Lumpur International Airport |  | MY | 1556 |
| 30 | Barcelona International Airport |  | ES | 1548 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1477 |
| 32 | Viracopos International Airport |  | BR | 1453 |
| 33 | Seattle-Tacoma International Airport |  | US | 1432 |
| 34 | Don Mueang International Airport |  | TH | 1421 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1418 |
| 36 | Bengaluru International Airport |  | IN | 1414 |
| 37 | Calgary International Airport |  | CA | 1406 |
| 38 | Oslo Gardermoen Airport |  | NO | 1377 |
| 39 | Vancouver International Airport |  | CA | 1364 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1337 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1099 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 903 | 21m | 244 km | 3,802.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 633 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 623 | 24m | 225 km | 2,416.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 615 | 1h 6m | 770 km | 8,169.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 549 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 403 | 27m | 275 km | 1,909.6 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 386 | 1h 50m | 1,423 km | 9,473.0 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 374 | 44m | 555 km | 3,581.2 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 360 | 44m | 241 km | 1,495.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 347 | 21m | 250 km | 1,498.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 335 | 24m | 218 km | 1,262.1 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 327 | 1h 39m | 1,156 km | 6,523.5 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 325 | 22m | 55 km | 308.9 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 322 | 1h 6m | 706 km | 3,920.4 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 303 | 19m | 99 km | 519.0 t |
| 19 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 297 | 26m | 215 km | 1,100.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 289 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 283 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 281 | 1h 14m | 961 km | 4,657.7 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 276 | 19m | 144 km | 686.5 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 262 | 1h 50m | 1,304 km | 5,894.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 251 | 28m | 152 km | 656.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TTW211 | TTW | Kansai International Airport (RJBB) | Taiwan Taoyuan International Airport (RCTP) | 2026-09-02 02:41 UTC | 2026-09-02 04:47 UTC | 2h 6m |
| N4401L |  | Tolovana Hot Springs Airport (83AK) | Fairbanks International Airport (PAFA) | 2026-09-02 04:23 UTC | 2026-09-02 04:44 UTC | 21m |
| ETH3618 | Ethiopian Airlines | Incheon International Airport (RKSI) | Macau International Airport (VMMC) | 2026-09-02 01:47 UTC | 2026-09-02 04:39 UTC | 2h 51m |
| CKS550 | CKS | Narita International Airport (RJAA) | Macau International Airport (VMMC) | 2026-09-02 00:48 UTC | 2026-09-02 04:36 UTC | 3h 48m |
| WJA135 | WJA | Calgary International Airport (CYYC) | Vancouver International Airport (CYVR) | 2026-09-02 03:27 UTC | 2026-09-02 04:34 UTC | 1h 7m |
| N749DS |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-09-02 03:21 UTC | 2026-09-02 04:26 UTC | 1h 5m |
| WIF150 | WIF | Ørsta-Volda Airport Hovden (ENOV) | Sogndal Airport (ENSG) | 2026-09-02 04:06 UTC | 2026-09-02 04:22 UTC | 15m |
| N108UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-09-02 03:06 UTC | 2026-09-02 04:19 UTC | 1h 13m |
| JAV280 | JAV | Queen Alia International Airport (OJAI) | Queen Alia International Airport (OJAI) | 2026-09-02 04:04 UTC | 2026-09-02 04:17 UTC | 12m |
| ZKTTL | ZKT | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-09-02 03:52 UTC | 2026-09-02 04:14 UTC | 22m |
| N503LP |  | K00V (K00V) | Metrogro Farm Airport (CO25) | 2026-09-02 03:45 UTC | 2026-09-02 04:13 UTC | 27m |
| N36BM |  | Charles M Schulz/Sonoma County Airport (KSTS) | Boeing Field/King County International Airport (KBFI) | 2026-09-02 02:52 UTC | 2026-09-02 04:11 UTC | 1h 19m |
| N641EC |  | Lebanon Municipal Airport (KM54) | John C Tune Airport (KJWN) | 2026-09-02 03:55 UTC | 2026-09-02 04:09 UTC | 13m |
| WGW | WGW | Holbrook Airport (YHBK) | Albury Airport (YMAY) | 2026-09-02 03:54 UTC | 2026-09-02 04:09 UTC | 15m |
| LNE216 | LNE | Ascazubi Airport (SEAS) | Miami International Airport (KMIA) | 2026-09-02 00:29 UTC | 2026-09-02 04:08 UTC | 3h 39m |
| FIRE5 | FIR | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-09-02 03:35 UTC | 2026-09-02 04:03 UTC | 28m |
| N116UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-09-02 02:59 UTC | 2026-09-02 04:01 UTC | 1h 2m |
| N830CA |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-09-02 03:55 UTC | 2026-09-02 03:59 UTC | 4m |
| SKQ51 | SKQ | Burlington/Alamance Regional Airport (KBUY) | Morristown Municipal Airport (KMMU) | 2026-09-02 02:14 UTC | 2026-09-02 03:58 UTC | 1h 43m |
| YHX | YHX | Warrnambool Airport (YWBL) | Warrnambool Airport (YWBL) | 2026-09-02 03:31 UTC | 2026-09-02 03:58 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
