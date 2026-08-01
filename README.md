# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_10:01:53_UTC-green)

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

**Latest saved flight:** 2026-08-01 10:01:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-01 10:01:53 UTC

- **164,136** saved flights
- **53,990** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **164,136** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,972,530.3 tonnes** estimated CO2 emissions
- **114,349,584 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6551 |
| 2 | SkyWest Airlines | 5982 |
| 3 | EJA | 3255 |
| 4 | IndiGo | 2885 |
| 5 | American Airlines | 2590 |
| 6 | Southwest Airlines | 2578 |
| 7 | ENY | 2041 |
| 8 | Delta Air Lines | 1959 |
| 9 | LATAM Airlines | 1533 |
| 10 | Lufthansa | 1532 |
| 11 | AZU | 1439 |
| 12 | WIF | 1381 |
| 13 | Vueling | 1357 |
| 14 | LXJ | 1274 |
| 15 | AXM | 1136 |
| 16 | Swiss International | 1128 |
| 17 | easyJet | 1075 |
| 18 | Alaska Airlines | 1017 |
| 19 | QLK | 1011 |
| 20 | All Nippon Airways | 1004 |
| 21 | EJU | 1003 |
| 22 | VIV | 906 |
| 23 | CXK | 879 |
| 24 | Cathay Pacific | 873 |
| 25 | United Airlines | 864 |
| 26 | AEE | 861 |
| 27 | GLO | 858 |
| 28 | Air France | 847 |
| 29 | MXY | 846 |
| 30 | JetBlue | 836 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 141805 |
| 2 | 🇪🇸 ES | 10491 |
| 3 | 🇧🇷 BR | 9355 |
| 4 | 🇦🇺 AU | 9253 |
| 5 | 🇮🇳 IN | 9058 |
| 6 | 🇨🇦 CA | 8938 |
| 7 | 🇮🇹 IT | 8456 |
| 8 | 🇩🇪 DE | 8218 |
| 9 | 🇬🇧 GB | 7535 |
| 10 | 🇯🇵 JP | 6630 |
| 11 | 🇫🇷 FR | 6487 |
| 12 | 🇨🇴 CO | 5866 |
| 13 | 🇬🇷 GR | 4727 |
| 14 | 🇲🇽 MX | 4704 |
| 15 | 🇳🇴 NO | 4322 |
| 16 | 🇨🇭 CH | 4314 |
| 17 | 🇹🇷 TR | 3921 |
| 18 | 🇲🇾 MY | 2956 |
| 19 | 🇵🇱 PL | 2780 |
| 20 | 🇿🇦 ZA | 2671 |
| 21 | 🇳🇿 NZ | 2410 |
| 22 | 🇹🇭 TH | 2344 |
| 23 | 🇵🇭 PH | 2158 |
| 24 | 🇰🇷 KR | 2127 |
| 25 | 🇬🇹 GT | 2115 |
| 26 | 🇲🇦 MA | 1655 |
| 27 | 🇭🇷 HR | 1546 |
| 28 | 🇲🇪 ME | 1538 |
| 29 | 🇳🇱 NL | 1489 |
| 30 | 🇲🇴 MO | 1388 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3351 |
| 2 | Denver International Airport |  | US | 2730 |
| 3 | Tokyo International Airport |  | JP | 2086 |
| 4 | Guaymaral Airport |  | CO | 2063 |
| 5 | Indira Gandhi International Airport |  | IN | 2009 |
| 6 | Harry Reid International Airport |  | US | 1990 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1810 |
| 8 | Zurich Airport |  | CH | 1748 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1726 |
| 10 | La Aurora Airport |  | GT | 1638 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1523 |
| 12 | El Dorado International Airport |  | CO | 1504 |
| 13 | Frankfurt am Main International Airport |  | DE | 1488 |
| 14 | Chicago O'Hare International Airport |  | US | 1482 |
| 15 | Salt Lake City International Airport |  | US | 1477 |
| 16 | Macau International Airport |  | MO | 1388 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1378 |
| 18 | Congonhas Airport |  | BR | 1355 |
| 19 | Madrid Barajas International Airport |  | ES | 1294 |
| 20 | Capua Airport |  | IT | 1286 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1252 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1163 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1161 |
| 24 | Charlotte/Douglas International Airport |  | US | 1153 |
| 25 | Charles de Gaulle International Airport |  | FR | 1120 |
| 26 | Kuala Lumpur International Airport |  | MY | 1120 |
| 27 | Malpensa International Airport |  | IT | 1085 |
| 28 | Bengaluru International Airport |  | IN | 1076 |
| 29 | Ninoy Aquino International Airport |  | PH | 1014 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1007 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1005 |
| 32 | Barcelona International Airport |  | ES | 970 |
| 33 | Daniel K Inouye International Airport |  | US | 959 |
| 34 | Seattle-Tacoma International Airport |  | US | 952 |
| 35 | Calgary International Airport |  | CA | 937 |
| 36 | Viracopos International Airport |  | BR | 930 |
| 37 | Scottsdale Airport |  | US | 917 |
| 38 | Oslo Gardermoen Airport |  | NO | 916 |
| 39 | Tenerife Norte Airport |  | ES | 914 |
| 40 | Reno/Tahoe International Airport |  | US | 902 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 862 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 597 | 21m | 244 km | 2,513.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 395 | 24m | 225 km | 1,532.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 391 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 374 | 1h 9m | 770 km | 4,968.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 306 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 284 | 27m | 275 km | 1,345.8 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 244 | 22m | 55 km | 231.9 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 240 | 19m | 165 km | 682.7 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 238 | 44m | 241 km | 988.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 225 | 1h 47m | 1,423 km | 5,521.9 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 213 | 26m | 215 km | 788.9 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 210 | 20m | 250 km | 907.1 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 209 | 20m | 99 km | 358.0 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 208 | 13m | - | - |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 202 | 31m | 49 km | 170.7 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 195 | 1h 15m | 961 km | 3,232.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 193 | 18m | 144 km | 480.1 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 190 | 31m | 369 km | 1,209.4 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 187 | 50m | 556 km | 1,792.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 183 | 1h 39m | 1,156 km | 3,650.8 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 181 | 1h 1m | 695 km | 2,169.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 180 | 44m | 452 km | 1,402.8 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 176 | 24m | 218 km | 663.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N33VC |  | Dubrovnik Airport (LDDU) | Stanke Dimitrov Highway Strip (LB37) | 2026-08-01 09:14 UTC | 2026-08-01 10:01 UTC | 47m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-07-31 19:13 UTC | 2026-08-01 09:50 UTC | 14h 37m |
| N456LF |  | Easton State Airport (KESW) | Boeing Field/King County International Airport (KBFI) | 2026-08-01 09:30 UTC | 2026-08-01 09:48 UTC | 17m |
| HBZUZ | HBZ | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-08-01 07:25 UTC | 2026-08-01 09:48 UTC | 2h 22m |
| GCICK | GCI | Compton Abbas Aerodrome (EGHA) | Compton Abbas Aerodrome (EGHA) | 2026-08-01 09:35 UTC | 2026-08-01 09:40 UTC | 5m |
| UAL149 | United Airlines | Newark Liberty International Airport (KEWR) | Fazenda Avanhandava Airport (SDWH) | 2026-08-01 01:21 UTC | 2026-08-01 09:37 UTC | 8h 15m |
| AMX014 | Aeromexico | Licenciado Benito Juarez International Airport (MMMX) | Rosana Camargo Airport (SIBX) | 2026-08-01 01:46 UTC | 2026-08-01 09:35 UTC | 7h 49m |
| GBMSB | GBM | Newquay Cornwall Airport (EGHQ) | Truro Airport (EGHY) | 2026-08-01 09:28 UTC | 2026-08-01 09:34 UTC | 6m |
| SWR8HG | Swiss International | London Heathrow Airport (EGLL) | Zurich Airport (LSZH) | 2026-08-01 08:19 UTC | 2026-08-01 09:34 UTC | 1h 14m |
| RRR1258 | RRR | Rzeszow-Jasionka Airport (EPRZ) | RAF Northolt (EGWU) | 2026-08-01 06:48 UTC | 2026-08-01 09:28 UTC | 2h 40m |
| RNA409 | RNA | Tribhuvan International Airport (VNKT) | Macau International Airport (VMMC) | 2026-08-01 05:34 UTC | 2026-08-01 09:28 UTC | 3h 53m |
| ZSNHX | ZSN | Lanseria Airport (FALA) | Hartebeespoortdam Airport (FAHB) | 2026-08-01 09:04 UTC | 2026-08-01 09:27 UTC | 23m |
| VJH373 | VJH | Eleftherios Venizelos International Airport (LGAV) | Radomir Dolni Rakovets Airfield (LB13) | 2026-08-01 08:44 UTC | 2026-08-01 09:26 UTC | 42m |
| LOG21XA | LOG | Glasgow International Airport (EGPF) | Kirkwall Airport (EGPA) | 2026-08-01 08:37 UTC | 2026-08-01 09:23 UTC | 46m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-07-31 22:07 UTC | 2026-08-01 09:22 UTC | 11h 14m |
| BNO93J | BNO | Stavanger Airport Sola (ENZV) | Kristiansand Airport (ENCN) | 2026-08-01 08:59 UTC | 2026-08-01 09:22 UTC | 22m |
| ICE16Y | ICE | Reykjavik Airport (BIRK) | Stykkishólmur Airport (BIST) | 2026-08-01 09:01 UTC | 2026-08-01 09:21 UTC | 19m |
| RYR3HP | Ryanair | Filippos Airport (LGKZ) | M. R. Stefanik Airport (LZIB) | 2026-08-01 07:53 UTC | 2026-08-01 09:19 UTC | 1h 25m |
| AOJ53L | AOJ | Thessaloniki Macedonia International Airport (LGTS) | Tsalapita Airport (LB11) | 2026-08-01 08:43 UTC | 2026-08-01 09:18 UTC | 34m |
| JCO3 | JCO | Paris-Le Bourget Airport (LFPB) | Samedan Airport (LSZS) | 2026-08-01 08:20 UTC | 2026-08-01 09:17 UTC | 56m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
