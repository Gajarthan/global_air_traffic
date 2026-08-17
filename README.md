# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_11:39:49_UTC-green)

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

**Latest saved flight:** 2026-08-17 11:39:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 11:39:49 UTC

- **207,758** saved flights
- **66,058** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **207,758** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,499,155.9 tonnes** estimated CO2 emissions
- **144,878,602 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8201 |
| 2 | SkyWest Airlines | 7461 |
| 3 | EJA | 4038 |
| 4 | IndiGo | 3558 |
| 5 | American Airlines | 3456 |
| 6 | Southwest Airlines | 3330 |
| 7 | Delta Air Lines | 2667 |
| 8 | ENY | 2586 |
| 9 | LATAM Airlines | 1952 |
| 10 | AZU | 1877 |
| 11 | Lufthansa | 1759 |
| 12 | Vueling | 1725 |
| 13 | WIF | 1672 |
| 14 | LXJ | 1643 |
| 15 | easyJet | 1435 |
| 16 | Swiss International | 1385 |
| 17 | AXM | 1360 |
| 18 | United Airlines | 1306 |
| 19 | QLK | 1293 |
| 20 | Alaska Airlines | 1287 |
| 21 | EJU | 1267 |
| 22 | All Nippon Airways | 1265 |
| 23 | VIV | 1144 |
| 24 | GLO | 1121 |
| 25 | Air France | 1114 |
| 26 | PGT | 1112 |
| 27 | JetBlue | 1063 |
| 28 | AEE | 1060 |
| 29 | WMT | 1051 |
| 30 | Wizz Air | 1024 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 176083 |
| 2 | 🇪🇸 ES | 13271 |
| 3 | 🇧🇷 BR | 11887 |
| 4 | 🇦🇺 AU | 11737 |
| 5 | 🇨🇦 CA | 11467 |
| 6 | 🇮🇳 IN | 11090 |
| 7 | 🇮🇹 IT | 10853 |
| 8 | 🇩🇪 DE | 10273 |
| 9 | 🇬🇧 GB | 9675 |
| 10 | 🇯🇵 JP | 8632 |
| 11 | 🇨🇴 CO | 8246 |
| 12 | 🇫🇷 FR | 8226 |
| 13 | 🇬🇷 GR | 6116 |
| 14 | 🇹🇷 TR | 5903 |
| 15 | 🇲🇽 MX | 5842 |
| 16 | 🇨🇭 CH | 5541 |
| 17 | 🇳🇴 NO | 5178 |
| 18 | 🇲🇾 MY | 3587 |
| 19 | 🇿🇦 ZA | 3492 |
| 20 | 🇵🇱 PL | 3421 |
| 21 | 🇹🇭 TH | 3330 |
| 22 | 🇳🇿 NZ | 2893 |
| 23 | 🇵🇭 PH | 2765 |
| 24 | 🇬🇹 GT | 2652 |
| 25 | 🇰🇷 KR | 2543 |
| 26 | 🇭🇷 HR | 2228 |
| 27 | 🇲🇦 MA | 2094 |
| 28 | 🇳🇱 NL | 1848 |
| 29 | 🇲🇪 ME | 1761 |
| 30 | 🇮🇩 ID | 1721 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4365 |
| 2 | Denver International Airport |  | US | 3394 |
| 3 | Tokyo International Airport |  | JP | 2596 |
| 4 | Indira Gandhi International Airport |  | IN | 2522 |
| 5 | Guaymaral Airport |  | CO | 2496 |
| 6 | Harry Reid International Airport |  | US | 2342 |
| 7 | Zurich Airport |  | CH | 2169 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2164 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2150 |
| 10 | La Aurora Airport |  | GT | 2019 |
| 11 | Chicago O'Hare International Airport |  | US | 1922 |
| 12 | El Dorado International Airport |  | CO | 1892 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1857 |
| 14 | Salt Lake City International Airport |  | US | 1838 |
| 15 | Congonhas Airport |  | BR | 1730 |
| 16 | Frankfurt am Main International Airport |  | DE | 1712 |
| 17 | Madrid Barajas International Airport |  | ES | 1628 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1578 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1575 |
| 20 | Capua Airport |  | IT | 1572 |
| 21 | Macau International Airport |  | MO | 1544 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1506 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1467 |
| 24 | Malpensa International Airport |  | IT | 1439 |
| 25 | Charles de Gaulle International Airport |  | FR | 1427 |
| 26 | Charlotte/Douglas International Airport |  | US | 1413 |
| 27 | Kuala Lumpur International Airport |  | MY | 1325 |
| 28 | Ninoy Aquino International Airport |  | PH | 1310 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1284 |
| 30 | Bengaluru International Airport |  | IN | 1283 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1259 |
| 32 | Barcelona International Airport |  | ES | 1240 |
| 33 | Seattle-Tacoma International Airport |  | US | 1238 |
| 34 | Viracopos International Airport |  | BR | 1203 |
| 35 | Calgary International Airport |  | CA | 1174 |
| 36 | Oslo Gardermoen Airport |  | NO | 1149 |
| 37 | Vitoria/Foronda Airport |  | ES | 1146 |
| 38 | Reno/Tahoe International Airport |  | US | 1143 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1114 |
| 40 | Daniel K Inouye International Airport |  | US | 1110 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1026 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 736 | 21m | 244 km | 3,099.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 512 | 1h 7m | 770 km | 6,801.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 486 | 24m | 225 km | 1,885.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 471 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 403 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 347 | 27m | 275 km | 1,644.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 344 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 305 | 44m | 241 km | 1,266.9 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 302 | 1h 49m | 1,423 km | 7,411.6 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 270 | 21m | 250 km | 1,166.2 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 261 | 24m | 218 km | 983.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 257 | 19m | 99 km | 440.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 253 | 27m | 215 km | 937.0 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 247 | 1h 37m | 1,156 km | 4,927.6 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 246 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 238 | 31m | 369 km | 1,514.9 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 238 | 19m | 144 km | 592.0 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 225 | 28m | 152 km | 588.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 223 | 1h 49m | 1,304 km | 5,016.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N4012J |  | HOPA (HOPA) | HOPA (HOPA) | 2026-08-17 11:21 UTC | 2026-08-17 11:39 UTC | 17m |
| SRG387 | SRG | Land's End Airport (EGHC) | Newquay Cornwall Airport (EGHQ) | 2026-08-17 11:20 UTC | 2026-08-17 11:36 UTC | 15m |
| N710HF |  | Ruder Airport (59IL) | Chicago Midway International Airport (KMDW) | 2026-08-17 10:45 UTC | 2026-08-17 11:34 UTC | 48m |
| THY6 | Turkish Airlines | Chicago O'Hare International Airport (KORD) | Tekirdag Corlu Airport (LTBU) | 2026-08-17 02:09 UTC | 2026-08-17 11:29 UTC | 9h 19m |
| N838C |  | Mid-Carolina Regional Airport (KRUQ) | Capital City Airport (KCXY) | 2026-08-17 10:27 UTC | 2026-08-17 11:28 UTC | 1h 0m |
| SXS5DW | SXS | Berlin Brandenburg Airport (EDDB) | Karain Airport (LTXE) | 2026-08-17 08:32 UTC | 2026-08-17 11:15 UTC | 2h 42m |
| HM1 |  | Melbourne Essendon Airport (YMEN) | Melbourne Moorabbin Airport (YMMB) | 2026-08-17 10:59 UTC | 2026-08-17 11:14 UTC | 15m |
| CHX55 | CHX | EDVT (EDVT) | Bremen Airport (EDDW) | 2026-08-17 10:24 UTC | 2026-08-17 11:09 UTC | 45m |
| LINCE01 | LIN | Torrejon Airport (LETO) | Valladolid Airport (LEVD) | 2026-08-17 10:47 UTC | 2026-08-17 11:07 UTC | 19m |
| SPGAA | SPG | Jastarnia Airport (EPJA) | Jastarnia Airport (EPJA) | 2026-08-17 11:02 UTC | 2026-08-17 11:03 UTC | 1m |
| WIF808 | WIF | Bodø Airport (ENBO) | Mo i Rana Airport Rossvoll (ENRA) | 2026-08-17 10:47 UTC | 2026-08-17 11:00 UTC | 12m |
| WIF5WP | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-08-17 10:44 UTC | 2026-08-17 10:55 UTC | 11m |
| TMN1 | TMN | Auckland International Airport (NZAA) | Sydney Kingsford Smith International Airport (YSSY) | 2026-08-17 08:02 UTC | 2026-08-17 10:55 UTC | 2h 53m |
| TTN148 | TTN | Lanseria Airport (FALA) | Harrismith Airport (FAHR) | 2026-08-17 10:29 UTC | 2026-08-17 10:54 UTC | 25m |
|  |  | Nairobi Wilson Airport (HKNW) | Narok Airport (HKNO) | 2026-08-17 10:36 UTC | 2026-08-17 10:53 UTC | 16m |
| RYR28SK | Ryanair | Bologna / Borgo Panigale Airport (LIPE) | Gioia Del Colle Airport (LIBV) | 2026-08-17 10:03 UTC | 2026-08-17 10:48 UTC | 45m |
| GRVGO | GRV | Leicester Airport (EGBG) | Bembridge Airport (EGHJ) | 2026-08-17 09:55 UTC | 2026-08-17 10:47 UTC | 51m |
| EIN952 | Aer Lingus | Seattle-Tacoma International Airport (KSEA) | Dublin Airport (EIDW) | 2026-08-17 02:21 UTC | 2026-08-17 10:46 UTC | 8h 25m |
| N126TS |  | Portland-Hillsboro Airport (KHIO) | Collins Landing Strip (04OR) | 2026-08-17 10:11 UTC | 2026-08-17 10:45 UTC | 34m |
| JON10 | JON | Lulea Airport (ESPA) | Andøya Airport (ENAN) | 2026-08-17 10:10 UTC | 2026-08-17 10:45 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
