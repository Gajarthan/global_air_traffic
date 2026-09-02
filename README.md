# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--02_09:17:33_UTC-green)

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

**Latest saved flight:** 2026-09-02 09:17:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-02 09:17:33 UTC

- **244,540** saved flights
- **73,996** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **244,540** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,947,569.9 tonnes** estimated CO2 emissions
- **170,873,614 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9810 |
| 2 | SkyWest Airlines | 8566 |
| 3 | EJA | 4721 |
| 4 | IndiGo | 4098 |
| 5 | American Airlines | 3930 |
| 6 | Southwest Airlines | 3665 |
| 7 | Delta Air Lines | 3112 |
| 8 | ENY | 2939 |
| 9 | LATAM Airlines | 2344 |
| 10 | AZU | 2273 |
| 11 | Vueling | 2093 |
| 12 | Lufthansa | 1958 |
| 13 | WIF | 1950 |
| 14 | LXJ | 1887 |
| 15 | easyJet | 1701 |
| 16 | Swiss International | 1647 |
| 17 | AXM | 1612 |
| 18 | EJU | 1573 |
| 19 | QLK | 1566 |
| 20 | United Airlines | 1539 |
| 21 | Alaska Airlines | 1462 |
| 22 | All Nippon Airways | 1442 |
| 23 | WMT | 1379 |
| 24 | GLO | 1366 |
| 25 | PGT | 1337 |
| 26 | VIV | 1337 |
| 27 | Air France | 1335 |
| 28 | Wizz Air | 1327 |
| 29 | AEE | 1207 |
| 30 | JetBlue | 1205 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 202559 |
| 2 | 🇪🇸 ES | 15706 |
| 3 | 🇧🇷 BR | 14247 |
| 4 | 🇦🇺 AU | 13915 |
| 5 | 🇨🇦 CA | 13607 |
| 6 | 🇮🇹 IT | 13396 |
| 7 | 🇮🇳 IN | 12776 |
| 8 | 🇩🇪 DE | 12060 |
| 9 | 🇬🇧 GB | 11542 |
| 10 | 🇨🇴 CO | 10588 |
| 11 | 🇫🇷 FR | 9876 |
| 12 | 🇯🇵 JP | 9750 |
| 13 | 🇹🇷 TR | 7275 |
| 14 | 🇬🇷 GR | 7212 |
| 15 | 🇲🇽 MX | 6734 |
| 16 | 🇨🇭 CH | 6570 |
| 17 | 🇳🇴 NO | 6061 |
| 18 | 🇹🇭 TH | 4425 |
| 19 | 🇲🇾 MY | 4323 |
| 20 | 🇿🇦 ZA | 4247 |
| 21 | 🇵🇱 PL | 4109 |
| 22 | 🇳🇿 NZ | 3360 |
| 23 | 🇵🇭 PH | 3351 |
| 24 | 🇬🇹 GT | 3070 |
| 25 | 🇰🇷 KR | 2869 |
| 26 | 🇭🇷 HR | 2818 |
| 27 | 🇲🇦 MA | 2473 |
| 28 | 🇲🇪 ME | 2284 |
| 29 | 🇳🇱 NL | 2214 |
| 30 | 🇮🇩 ID | 2133 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5038 |
| 2 | Denver International Airport |  | US | 3939 |
| 3 | Indira Gandhi International Airport |  | IN | 2981 |
| 4 | Tokyo International Airport |  | JP | 2905 |
| 5 | Guaymaral Airport |  | CO | 2713 |
| 6 | Harry Reid International Airport |  | US | 2602 |
| 7 | Zurich Airport |  | CH | 2567 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2490 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2436 |
| 10 | El Dorado International Airport |  | CO | 2407 |
| 11 | La Aurora Airport |  | GT | 2335 |
| 12 | Salt Lake City International Airport |  | US | 2165 |
| 13 | Chicago O'Hare International Airport |  | US | 2161 |
| 14 | Congonhas Airport |  | BR | 2087 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2024 |
| 16 | Frankfurt am Main International Airport |  | DE | 1929 |
| 17 | Madrid Barajas International Airport |  | ES | 1923 |
| 18 | Capua Airport |  | IT | 1923 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1836 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1799 |
| 21 | Malpensa International Airport |  | IT | 1750 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1721 |
| 23 | Charles de Gaulle International Airport |  | FR | 1719 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1714 |
| 25 | Macau International Airport |  | MO | 1632 |
| 26 | Ninoy Aquino International Airport |  | PH | 1631 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1572 |
| 28 | Charlotte/Douglas International Airport |  | US | 1560 |
| 29 | Kuala Lumpur International Airport |  | MY | 1557 |
| 30 | Barcelona International Airport |  | ES | 1549 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1477 |
| 32 | Viracopos International Airport |  | BR | 1453 |
| 33 | Seattle-Tacoma International Airport |  | US | 1432 |
| 34 | Don Mueang International Airport |  | TH | 1423 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1418 |
| 36 | Bengaluru International Airport |  | IN | 1415 |
| 37 | Calgary International Airport |  | CA | 1406 |
| 38 | Oslo Gardermoen Airport |  | NO | 1380 |
| 39 | Vancouver International Airport |  | CA | 1364 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1338 |

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
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 375 | 44m | 555 km | 3,590.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 361 | 44m | 241 km | 1,499.5 t |
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
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 277 | 19m | 144 km | 689.0 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 262 | 1h 50m | 1,304 km | 5,894.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 251 | 28m | 152 km | 656.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FJJJY | FJJ | Saint-Nazaire-Montoir Airport (LFRZ) | Saint-Nazaire-Montoir Airport (LFRZ) | 2026-09-02 09:07 UTC | 2026-09-02 09:17 UTC | 10m |
| NAK67N | NAK | La Roche-sur-Yon Airport (LFRI) | Rennes-Saint-Jacques Airport (LFRN) | 2026-09-02 08:25 UTC | 2026-09-02 09:10 UTC | 45m |
| XHE | XHE | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-09-02 08:16 UTC | 2026-09-02 09:05 UTC | 48m |
| FJCGD | FJC | Les Mureaux Airport (LFXU) | Etrepagny Airport (LFFY) | 2026-09-02 08:45 UTC | 2026-09-02 09:00 UTC | 14m |
| EZY68JH | easyJet | London Luton Airport (EGGW) | Chania International Airport (LGSA) | 2026-09-02 05:41 UTC | 2026-09-02 08:58 UTC | 3h 17m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-09-02 08:35 UTC | 2026-09-02 08:54 UTC | 18m |
| ASL4010 | ASL | Belgrade Nikola Tesla Airport (LYBE) | Belgrade Nikola Tesla Airport (LYBE) | 2026-09-02 07:37 UTC | 2026-09-02 08:50 UTC | 1h 13m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Zhuhai Airport (ZGSD) | 2026-09-01 21:56 UTC | 2026-09-02 08:41 UTC | 10h 45m |
| VAA017 | VAA | Kopitnari Airport (UGKO) | UGMS (UGMS) | 2026-09-02 08:18 UTC | 2026-09-02 08:37 UTC | 19m |
| BAW88LP | British Airways | London Heathrow Airport (EGLL) | Hannover Airport (EDDV) | 2026-09-02 07:30 UTC | 2026-09-02 08:35 UTC | 1h 5m |
| NOZ30BF | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Kiruna Airport (ESNQ) | 2026-09-02 07:04 UTC | 2026-09-02 08:27 UTC | 1h 23m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-09-02 08:15 UTC | 2026-09-02 08:27 UTC | 11m |
| OEKOE | OEK | Wiener Neustadt East Airport (LOAN) | Graz Airport (LOWG) | 2026-09-02 07:15 UTC | 2026-09-02 08:24 UTC | 1h 9m |
| AM315 |  | Horsham Airport (YHSM) | Prairie Airport (YPRA) | 2026-09-02 08:03 UTC | 2026-09-02 08:24 UTC | 21m |
| 3AMAX |  | Nice-Cote d'Azur Airport (LFMN) | Nice-Cote d'Azur Airport (LFMN) | 2026-09-02 07:52 UTC | 2026-09-02 08:23 UTC | 31m |
| AFR188 | Air France | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-09-01 21:39 UTC | 2026-09-02 08:22 UTC | 10h 43m |
| RYR8976 | Ryanair | Sofia Airport (LBSF) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-09-02 07:09 UTC | 2026-09-02 08:22 UTC | 1h 12m |
| EWG86C | EWG | Palma De Mallorca Airport (LEPA) | Saarbrucken Airport (EDDR) | 2026-09-02 06:36 UTC | 2026-09-02 08:21 UTC | 1h 44m |
| AXM6082 | AXM | Senai International Airport (WMKJ) | Sitiawan Airport (WMBA) | 2026-09-02 07:45 UTC | 2026-09-02 08:21 UTC | 35m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-09-02 07:32 UTC | 2026-09-02 08:20 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
