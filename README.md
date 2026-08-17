# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_07:10:07_UTC-green)

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

**Latest saved flight:** 2026-08-17 07:10:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 07:10:07 UTC

- **207,246** saved flights
- **65,971** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **207,246** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,492,238.0 tonnes** estimated CO2 emissions
- **144,477,567 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8164 |
| 2 | SkyWest Airlines | 7461 |
| 3 | EJA | 4038 |
| 4 | IndiGo | 3541 |
| 5 | American Airlines | 3455 |
| 6 | Southwest Airlines | 3330 |
| 7 | Delta Air Lines | 2666 |
| 8 | ENY | 2586 |
| 9 | LATAM Airlines | 1951 |
| 10 | AZU | 1875 |
| 11 | Lufthansa | 1755 |
| 12 | Vueling | 1713 |
| 13 | WIF | 1664 |
| 14 | LXJ | 1643 |
| 15 | easyJet | 1428 |
| 16 | Swiss International | 1378 |
| 17 | AXM | 1354 |
| 18 | United Airlines | 1304 |
| 19 | QLK | 1288 |
| 20 | Alaska Airlines | 1287 |
| 21 | EJU | 1261 |
| 22 | All Nippon Airways | 1257 |
| 23 | VIV | 1144 |
| 24 | GLO | 1121 |
| 25 | PGT | 1106 |
| 26 | Air France | 1103 |
| 27 | JetBlue | 1063 |
| 28 | AEE | 1055 |
| 29 | WMT | 1044 |
| 30 | Wizz Air | 1020 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 176051 |
| 2 | 🇪🇸 ES | 13205 |
| 3 | 🇧🇷 BR | 11877 |
| 4 | 🇦🇺 AU | 11680 |
| 5 | 🇨🇦 CA | 11459 |
| 6 | 🇮🇳 IN | 11039 |
| 7 | 🇮🇹 IT | 10794 |
| 8 | 🇩🇪 DE | 10226 |
| 9 | 🇬🇧 GB | 9629 |
| 10 | 🇯🇵 JP | 8567 |
| 11 | 🇨🇴 CO | 8246 |
| 12 | 🇫🇷 FR | 8174 |
| 13 | 🇬🇷 GR | 6086 |
| 14 | 🇹🇷 TR | 5871 |
| 15 | 🇲🇽 MX | 5842 |
| 16 | 🇨🇭 CH | 5522 |
| 17 | 🇳🇴 NO | 5152 |
| 18 | 🇲🇾 MY | 3564 |
| 19 | 🇿🇦 ZA | 3456 |
| 20 | 🇵🇱 PL | 3410 |
| 21 | 🇹🇭 TH | 3293 |
| 22 | 🇳🇿 NZ | 2886 |
| 23 | 🇵🇭 PH | 2757 |
| 24 | 🇬🇹 GT | 2652 |
| 25 | 🇰🇷 KR | 2527 |
| 26 | 🇭🇷 HR | 2213 |
| 27 | 🇲🇦 MA | 2083 |
| 28 | 🇳🇱 NL | 1839 |
| 29 | 🇲🇪 ME | 1747 |
| 30 | 🇮🇩 ID | 1714 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4365 |
| 2 | Denver International Airport |  | US | 3394 |
| 3 | Tokyo International Airport |  | JP | 2577 |
| 4 | Indira Gandhi International Airport |  | IN | 2507 |
| 5 | Guaymaral Airport |  | CO | 2496 |
| 6 | Harry Reid International Airport |  | US | 2342 |
| 7 | Zurich Airport |  | CH | 2159 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2156 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2150 |
| 10 | La Aurora Airport |  | GT | 2019 |
| 11 | Chicago O'Hare International Airport |  | US | 1920 |
| 12 | El Dorado International Airport |  | CO | 1892 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1854 |
| 14 | Salt Lake City International Airport |  | US | 1838 |
| 15 | Congonhas Airport |  | BR | 1729 |
| 16 | Frankfurt am Main International Airport |  | DE | 1710 |
| 17 | Madrid Barajas International Airport |  | ES | 1622 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1578 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1575 |
| 20 | Capua Airport |  | IT | 1570 |
| 21 | Macau International Airport |  | MO | 1543 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1505 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1462 |
| 24 | Malpensa International Airport |  | IT | 1431 |
| 25 | Charlotte/Douglas International Airport |  | US | 1413 |
| 26 | Charles de Gaulle International Airport |  | FR | 1413 |
| 27 | Kuala Lumpur International Airport |  | MY | 1317 |
| 28 | Ninoy Aquino International Airport |  | PH | 1306 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1284 |
| 30 | Bengaluru International Airport |  | IN | 1280 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1259 |
| 32 | Seattle-Tacoma International Airport |  | US | 1236 |
| 33 | Barcelona International Airport |  | ES | 1233 |
| 34 | Viracopos International Airport |  | BR | 1202 |
| 35 | Calgary International Airport |  | CA | 1174 |
| 36 | Reno/Tahoe International Airport |  | US | 1143 |
| 37 | Oslo Gardermoen Airport |  | NO | 1141 |
| 38 | Vitoria/Foronda Airport |  | ES | 1137 |
| 39 | Daniel K Inouye International Airport |  | US | 1110 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1107 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1026 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 736 | 21m | 244 km | 3,099.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 508 | 1h 7m | 770 km | 6,748.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 483 | 24m | 225 km | 1,873.8 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 471 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 403 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 346 | 27m | 275 km | 1,639.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 343 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 304 | 44m | 241 km | 1,262.8 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 300 | 1h 49m | 1,423 km | 7,362.5 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 268 | 21m | 250 km | 1,157.6 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 257 | 24m | 218 km | 968.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 257 | 19m | 99 km | 440.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 252 | 27m | 215 km | 933.3 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 245 | 1h 37m | 1,156 km | 4,887.7 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 238 | 31m | 369 km | 1,514.9 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 237 | 19m | 144 km | 589.5 t |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 225 | 28m | 152 km | 588.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 223 | 1h 49m | 1,304 km | 5,016.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| A6FHE |  | Das Island Airport (OMAS) | Das Island Airport (OMAS) | 2026-08-17 06:42 UTC | 2026-08-17 07:10 UTC | 27m |
| MJO | MJO | Tangalooma Resort Airport (YXTA) | Tangalooma Resort Airport (YXTA) | 2026-08-17 06:40 UTC | 2026-08-17 07:07 UTC | 27m |
| WIF4X | WIF | Oslo Gardermoen Airport (ENGM) | Gol Airport (ENKL) | 2026-08-17 06:20 UTC | 2026-08-17 06:54 UTC | 34m |
| DLH1WN | Lufthansa | Frankfurt am Main International Airport (EDDF) | Zurich Airport (LSZH) | 2026-08-17 06:09 UTC | 2026-08-17 06:53 UTC | 44m |
| TTW725 | TTW | Izumo Airport (RJOC) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-17 04:36 UTC | 2026-08-17 06:38 UTC | 2h 1m |
| WIF64M | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-17 05:48 UTC | 2026-08-17 06:36 UTC | 48m |
| OAL099 | OAL | Ikaria Airport (LGIK) | Limnos Airport (LGLM) | 2026-08-17 05:54 UTC | 2026-08-17 06:33 UTC | 38m |
| DLH796 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Zhuhai Airport (ZGSD) | 2026-08-16 20:03 UTC | 2026-08-17 06:30 UTC | 10h 26m |
| QLK87D | QLK | Melbourne International Airport (YMML) | Queenstown Airport (YQNS) | 2026-08-17 05:54 UTC | 2026-08-17 06:29 UTC | 35m |
| TJT31DR | TJT | Toulouse-Blagnac Airport (LFBO) | Rennes-Saint-Jacques Airport (LFRN) | 2026-08-17 05:02 UTC | 2026-08-17 06:22 UTC | 1h 19m |
| WZZ247 | Wizz Air | Kopitnari Airport (UGKO) | Malpensa International Airport (LIMC) | 2026-08-17 02:31 UTC | 2026-08-17 06:22 UTC | 3h 50m |
| BH102 |  | Tejgaon Airport (VGTJ) | Tejgaon Airport (VGTJ) | 2026-08-17 05:19 UTC | 2026-08-17 06:19 UTC | 1h 0m |
| ANE87CJ | ANE | Madrid Barajas International Airport (LEMD) | La Morgal Airport (LEMR) | 2026-08-17 05:43 UTC | 2026-08-17 06:17 UTC | 34m |
| BTK7531 | BTK | Soekarno-Hatta International Airport (WIII) | Achmad Yani Airport (WARS) | 2026-08-17 05:41 UTC | 2026-08-17 06:17 UTC | 36m |
| WIF3YC | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-08-17 05:46 UTC | 2026-08-17 06:16 UTC | 29m |
| VLG2KV | Vueling | Paris-Orly Airport (LFPO) | Santiago de Compostela Airport (LEST) | 2026-08-17 04:43 UTC | 2026-08-17 06:15 UTC | 1h 31m |
| AIQ1040 | AIQ | Don Mueang International Airport (VTBD) | Wattay International Airport (VLVT) | 2026-08-17 05:26 UTC | 2026-08-17 06:12 UTC | 46m |
| WIF8HM | WIF | Bergen Airport Flesland (ENBR) | Molde Airport (ENML) | 2026-08-17 05:38 UTC | 2026-08-17 06:11 UTC | 32m |
| SWR2MC | Swiss International | Zurich Airport (LSZH) | Munich International Airport (EDDM) | 2026-08-17 05:34 UTC | 2026-08-17 06:11 UTC | 36m |
| IBE04RD | Iberia | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 2026-08-17 05:41 UTC | 2026-08-17 06:09 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
