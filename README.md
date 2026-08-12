# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_11:04:06_UTC-green)

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

**Latest saved flight:** 2026-08-12 11:04:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-12 11:04:06 UTC

- **189,094** saved flights
- **59,801** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **189,094** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,265,989.8 tonnes** estimated CO2 emissions
- **131,361,725 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7502 |
| 2 | SkyWest Airlines | 6863 |
| 3 | EJA | 3722 |
| 4 | IndiGo | 3291 |
| 5 | Southwest Airlines | 2956 |
| 6 | American Airlines | 2934 |
| 7 | ENY | 2344 |
| 8 | Delta Air Lines | 2220 |
| 9 | LATAM Airlines | 1762 |
| 10 | AZU | 1700 |
| 11 | Lufthansa | 1653 |
| 12 | Vueling | 1571 |
| 13 | WIF | 1568 |
| 14 | LXJ | 1478 |
| 15 | easyJet | 1302 |
| 16 | Swiss International | 1290 |
| 17 | AXM | 1251 |
| 18 | QLK | 1168 |
| 19 | EJU | 1166 |
| 20 | All Nippon Airways | 1154 |
| 21 | Alaska Airlines | 1132 |
| 22 | VIV | 1045 |
| 23 | GLO | 1017 |
| 24 | Air France | 987 |
| 25 | PGT | 975 |
| 26 | AEE | 971 |
| 27 | United Airlines | 971 |
| 28 | CXK | 966 |
| 29 | Cathay Pacific | 947 |
| 30 | Wizz Air | 939 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 161182 |
| 2 | 🇪🇸 ES | 12183 |
| 3 | 🇧🇷 BR | 10837 |
| 4 | 🇦🇺 AU | 10648 |
| 5 | 🇨🇦 CA | 10343 |
| 6 | 🇮🇳 IN | 10319 |
| 7 | 🇮🇹 IT | 9802 |
| 8 | 🇩🇪 DE | 9341 |
| 9 | 🇬🇧 GB | 8792 |
| 10 | 🇯🇵 JP | 7753 |
| 11 | 🇫🇷 FR | 7559 |
| 12 | 🇨🇴 CO | 7181 |
| 13 | 🇬🇷 GR | 5538 |
| 14 | 🇲🇽 MX | 5383 |
| 15 | 🇨🇭 CH | 5070 |
| 16 | 🇹🇷 TR | 5018 |
| 17 | 🇳🇴 NO | 4862 |
| 18 | 🇲🇾 MY | 3272 |
| 19 | 🇿🇦 ZA | 3172 |
| 20 | 🇵🇱 PL | 3131 |
| 21 | 🇹🇭 TH | 2932 |
| 22 | 🇳🇿 NZ | 2682 |
| 23 | 🇵🇭 PH | 2503 |
| 24 | 🇬🇹 GT | 2399 |
| 25 | 🇰🇷 KR | 2333 |
| 26 | 🇭🇷 HR | 1920 |
| 27 | 🇲🇦 MA | 1919 |
| 28 | 🇳🇱 NL | 1687 |
| 29 | 🇲🇪 ME | 1685 |
| 30 | 🇲🇴 MO | 1525 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3924 |
| 2 | Denver International Airport |  | US | 3116 |
| 3 | Tokyo International Airport |  | JP | 2392 |
| 4 | Indira Gandhi International Airport |  | IN | 2326 |
| 5 | Guaymaral Airport |  | CO | 2312 |
| 6 | Harry Reid International Airport |  | US | 2210 |
| 7 | Zurich Airport |  | CH | 2012 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2004 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1956 |
| 10 | La Aurora Airport |  | GT | 1843 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1714 |
| 12 | El Dorado International Airport |  | CO | 1699 |
| 13 | Salt Lake City International Airport |  | US | 1681 |
| 14 | Chicago O'Hare International Airport |  | US | 1661 |
| 15 | Frankfurt am Main International Airport |  | DE | 1621 |
| 16 | Congonhas Airport |  | BR | 1575 |
| 17 | Macau International Airport |  | MO | 1525 |
| 18 | Madrid Barajas International Airport |  | ES | 1489 |
| 19 | Capua Airport |  | IT | 1471 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1466 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1398 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1350 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1323 |
| 24 | Malpensa International Airport |  | IT | 1304 |
| 25 | Charles de Gaulle International Airport |  | FR | 1295 |
| 26 | Charlotte/Douglas International Airport |  | US | 1264 |
| 27 | Kuala Lumpur International Airport |  | MY | 1224 |
| 28 | Bengaluru International Airport |  | IN | 1216 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1184 |
| 30 | Ninoy Aquino International Airport |  | PH | 1182 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1161 |
| 32 | Barcelona International Airport |  | ES | 1135 |
| 33 | Reno/Tahoe International Airport |  | US | 1094 |
| 34 | Viracopos International Airport |  | BR | 1091 |
| 35 | Seattle-Tacoma International Airport |  | US | 1090 |
| 36 | Calgary International Airport |  | CA | 1077 |
| 37 | Daniel K Inouye International Airport |  | US | 1064 |
| 38 | Oslo Gardermoen Airport |  | NO | 1054 |
| 39 | Tenerife Norte Airport |  | ES | 1040 |
| 40 | Vitoria/Foronda Airport |  | ES | 1023 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 953 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 692 | 21m | 244 km | 2,913.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 459 | 1h 7m | 770 km | 6,097.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 442 | 24m | 225 km | 1,714.8 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 439 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 333 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 317 | 27m | 275 km | 1,502.1 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 307 | 14m | 114 km | 602.1 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 284 | 8m | - | - |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 282 | 44m | 241 km | 1,171.4 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 271 | 1h 49m | 1,423 km | 6,650.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 271 | 22m | 55 km | 257.6 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 251 | 20m | 250 km | 1,084.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 236 | 27m | 215 km | 874.0 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 236 | 13m | - | - |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 232 | 12m | - | - |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 231 | 19m | 99 km | 395.7 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 230 | 1h 15m | 961 km | 3,812.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 225 | 1h 38m | 1,156 km | 4,488.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 225 | 19m | 144 km | 559.7 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 223 | 24m | 218 km | 840.1 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 218 | 31m | 369 km | 1,387.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 206 | 1h 48m | 1,304 km | 4,634.5 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 206 | 28m | 152 km | 538.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FCA4VO | FCA | Bergamo / Orio Al Serio Airport (LIME) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-12 10:08 UTC | 2026-08-12 11:04 UTC | 55m |
| ALIFE2 | ALI | Athanasiou Valley Airport (CO07) | Buckley Space Force Base Airport (KBKF) | 2026-08-12 10:32 UTC | 2026-08-12 10:50 UTC | 18m |
| N520MD |  | Savannah/Hilton Head International Airport (KSAV) | Hunter Army Air Field (KSVN) | 2026-08-12 10:41 UTC | 2026-08-12 10:45 UTC | 3m |
|  |  | Calcinate Del Pesce Airport (LILC) | Calcinate Del Pesce Airport (LILC) | 2026-08-12 10:35 UTC | 2026-08-12 10:38 UTC | 3m |
| WWIND229 | WWI | Anglesey Airport (EGOV) | Caernarfon Airport (EGCK) | 2026-08-12 10:13 UTC | 2026-08-12 10:38 UTC | 25m |
| SUCCE | SUC | Port Said Airport (HEPS) | Port Said Airport (HEPS) | 2026-08-12 10:14 UTC | 2026-08-12 10:33 UTC | 18m |
| HNL24A | HNL | De Kooy Airport (EHKD) | Rotterdam Airport (EHRD) | 2026-08-12 10:02 UTC | 2026-08-12 10:30 UTC | 27m |
| BBC437 | BBC | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-08-12 09:55 UTC | 2026-08-12 10:26 UTC | 31m |
| TRP7 | TRP | St Mary's County Regional Airport (K2W6) | Joint Base Andrews Airport (KADW) | 2026-08-12 10:05 UTC | 2026-08-12 10:24 UTC | 18m |
| N941SP |  | Clark Regional Airport (KJVY) | Teterboro Airport (KTEB) | 2026-08-12 08:44 UTC | 2026-08-12 10:16 UTC | 1h 32m |
| GBIHO | GBI | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-12 09:50 UTC | 2026-08-12 10:14 UTC | 24m |
| IBB97FU | IBB | Tenerife Norte Airport (GCXO) | La Morgal Airport (LEMR) | 2026-08-12 07:47 UTC | 2026-08-12 10:11 UTC | 2h 24m |
| JST779 | JST | Adelaide International Airport (YPAD) | Melbourne International Airport (YMML) | 2026-08-12 09:01 UTC | 2026-08-12 10:10 UTC | 1h 9m |
| DTA231 | DTA | Quatro De Fevereiro Airport (FNLU) | Tshimpi Airport (FZAM) | 2026-08-12 09:42 UTC | 2026-08-12 10:09 UTC | 27m |
| UAL966 | United Airlines | Newark Liberty International Airport (KEWR) | Napoli / Capodichino International Airport (LIRN) | 2026-08-12 02:21 UTC | 2026-08-12 10:07 UTC | 7h 45m |
| FDA207 | FDA | Matsumoto Airport (RJAF) | Ashiya Airport (RJFA) | 2026-08-12 09:04 UTC | 2026-08-12 10:06 UTC | 1h 1m |
| N727DL |  | Zurich Airport (LSZH) | Mauterndorf Airport (LOSM) | 2026-08-12 09:03 UTC | 2026-08-12 10:04 UTC | 1h 0m |
| RTV2M | RTV | Viseu Airport (LPVZ) | Viseu Airport (LPVZ) | 2026-08-12 09:45 UTC | 2026-08-12 10:02 UTC | 16m |
| BNOR | BNO | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-08-12 09:46 UTC | 2026-08-12 10:01 UTC | 14m |
| ZSTKH | ZST | O. R. Tambo International Airport (FAOR) | Pilanesberg International Airport (FAPN) | 2026-08-12 09:33 UTC | 2026-08-12 10:01 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
