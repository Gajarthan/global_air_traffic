# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_06:56:17_UTC-green)

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

**Latest saved flight:** 2026-08-09 06:56:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 06:56:17 UTC

- **180,360** saved flights
- **57,749** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **180,360** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,167,461.2 tonnes** estimated CO2 emissions
- **125,649,924 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7134 |
| 2 | SkyWest Airlines | 6582 |
| 3 | EJA | 3555 |
| 4 | IndiGo | 3160 |
| 5 | Southwest Airlines | 2840 |
| 6 | American Airlines | 2817 |
| 7 | ENY | 2250 |
| 8 | Delta Air Lines | 2142 |
| 9 | LATAM Airlines | 1680 |
| 10 | AZU | 1613 |
| 11 | Lufthansa | 1600 |
| 12 | WIF | 1493 |
| 13 | Vueling | 1488 |
| 14 | LXJ | 1407 |
| 15 | easyJet | 1229 |
| 16 | Swiss International | 1227 |
| 17 | AXM | 1219 |
| 18 | QLK | 1111 |
| 19 | Alaska Airlines | 1097 |
| 20 | All Nippon Airways | 1096 |
| 21 | EJU | 1096 |
| 22 | VIV | 996 |
| 23 | GLO | 965 |
| 24 | Cathay Pacific | 946 |
| 25 | CXK | 946 |
| 26 | AEE | 939 |
| 27 | United Airlines | 929 |
| 28 | Air France | 924 |
| 29 | MXY | 905 |
| 30 | PGT | 900 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 154718 |
| 2 | 🇪🇸 ES | 11561 |
| 3 | 🇧🇷 BR | 10344 |
| 4 | 🇦🇺 AU | 10163 |
| 5 | 🇮🇳 IN | 9906 |
| 6 | 🇨🇦 CA | 9850 |
| 7 | 🇮🇹 IT | 9299 |
| 8 | 🇩🇪 DE | 8900 |
| 9 | 🇬🇧 GB | 8309 |
| 10 | 🇯🇵 JP | 7288 |
| 11 | 🇫🇷 FR | 7154 |
| 12 | 🇨🇴 CO | 6707 |
| 13 | 🇬🇷 GR | 5258 |
| 14 | 🇲🇽 MX | 5163 |
| 15 | 🇨🇭 CH | 4795 |
| 16 | 🇳🇴 NO | 4646 |
| 17 | 🇹🇷 TR | 4599 |
| 18 | 🇲🇾 MY | 3181 |
| 19 | 🇵🇱 PL | 3002 |
| 20 | 🇿🇦 ZA | 2926 |
| 21 | 🇹🇭 TH | 2749 |
| 22 | 🇳🇿 NZ | 2608 |
| 23 | 🇵🇭 PH | 2386 |
| 24 | 🇬🇹 GT | 2294 |
| 25 | 🇰🇷 KR | 2254 |
| 26 | 🇲🇦 MA | 1817 |
| 27 | 🇭🇷 HR | 1794 |
| 28 | 🇲🇪 ME | 1635 |
| 29 | 🇳🇱 NL | 1618 |
| 30 | 🇲🇴 MO | 1512 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3732 |
| 2 | Denver International Airport |  | US | 2987 |
| 3 | Tokyo International Airport |  | JP | 2263 |
| 4 | Guaymaral Airport |  | CO | 2223 |
| 5 | Indira Gandhi International Airport |  | IN | 2210 |
| 6 | Harry Reid International Airport |  | US | 2126 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1939 |
| 8 | Zurich Airport |  | CH | 1912 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1878 |
| 10 | La Aurora Airport |  | GT | 1762 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1648 |
| 12 | Chicago O'Hare International Airport |  | US | 1626 |
| 13 | Salt Lake City International Airport |  | US | 1615 |
| 14 | El Dorado International Airport |  | CO | 1611 |
| 15 | Frankfurt am Main International Airport |  | DE | 1565 |
| 16 | Macau International Airport |  | MO | 1512 |
| 17 | Congonhas Airport |  | BR | 1500 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1436 |
| 19 | Madrid Barajas International Airport |  | ES | 1410 |
| 20 | Capua Airport |  | IT | 1406 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1351 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1284 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1267 |
| 24 | Malpensa International Airport |  | IT | 1242 |
| 25 | Charlotte/Douglas International Airport |  | US | 1224 |
| 26 | Charles de Gaulle International Airport |  | FR | 1216 |
| 27 | Kuala Lumpur International Airport |  | MY | 1196 |
| 28 | Bengaluru International Airport |  | IN | 1178 |
| 29 | Ninoy Aquino International Airport |  | PH | 1123 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1121 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1109 |
| 32 | Barcelona International Airport |  | ES | 1073 |
| 33 | Seattle-Tacoma International Airport |  | US | 1041 |
| 34 | Daniel K Inouye International Airport |  | US | 1040 |
| 35 | Viracopos International Airport |  | BR | 1036 |
| 36 | Reno/Tahoe International Airport |  | US | 1032 |
| 37 | Calgary International Airport |  | CA | 1029 |
| 38 | Oslo Gardermoen Airport |  | NO | 998 |
| 39 | Tenerife Norte Airport |  | ES | 983 |
| 40 | Amsterdam Airport Schiphol |  | NL | 975 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 918 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 669 | 21m | 244 km | 2,817.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 425 | 1h 8m | 770 km | 5,645.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 425 | 24m | 225 km | 1,648.8 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 417 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 302 | 27m | 275 km | 1,431.0 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 297 | 1h 7m | 706 km | 3,616.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 270 | 44m | 241 km | 1,121.5 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 253 | 1h 48m | 1,423 km | 6,209.0 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 241 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 233 | 20m | 250 km | 1,006.4 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 227 | 26m | 215 km | 840.7 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 221 | 19m | 99 km | 378.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 219 | 31m | 49 km | 185.1 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 219 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 218 | 1h 15m | 961 km | 3,613.5 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 218 | 50m | 556 km | 2,089.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 215 | 19m | 144 km | 534.8 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 211 | 1h 38m | 1,156 km | 4,209.4 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 209 | 31m | 369 km | 1,330.3 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 205 | 24m | 218 km | 772.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 203 | 28m | 152 km | 530.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 197 | 1h 1m | 695 km | 2,361.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-09 06:46 UTC | 2026-08-09 06:56 UTC | 10m |
| THY1BX | Turkish Airlines | Istanbul Airport (LTFM) | Smolensk North Airport (XUBS) | 2026-08-09 04:33 UTC | 2026-08-09 06:48 UTC | 2h 14m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-09 06:01 UTC | 2026-08-09 06:32 UTC | 31m |
| CRK676D | CRK | Chek Lap Kok International Airport (VHHH) | Kerama Airport (ROKR) | 2026-08-09 04:26 UTC | 2026-08-09 06:27 UTC | 2h 0m |
| QLK6D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Tamworth Airport (YSTW) | 2026-08-09 05:36 UTC | 2026-08-09 06:17 UTC | 40m |
| N898MT |  | Caldwell Municipal Airport (KRWV) | Coulter Field (KCFD) | 2026-08-09 06:03 UTC | 2026-08-09 06:14 UTC | 10m |
| N979AZ |  | Akron-Canton Regional Airport (KCAK) | Scottsdale Airport (KSDL) | 2026-08-09 02:11 UTC | 2026-08-09 06:07 UTC | 3h 56m |
| 9HFAE |  | Luqa Airport (LMML) | Luqa Airport (LMML) | 2026-08-09 04:46 UTC | 2026-08-09 06:05 UTC | 1h 19m |
| TGW420 | TGW | Changi Air Base (WSAC) | Malacca Airport (WMKM) | 2026-08-09 05:34 UTC | 2026-08-09 06:02 UTC | 28m |
| CFH21 | CFH | Newcastle Airport (YWLM) | Walcha Airport (YWCH) | 2026-08-09 05:28 UTC | 2026-08-09 06:00 UTC | 31m |
| IBX59 | IBX | Matsumoto Airport (RJAF) | Ozuki Airport (RJOZ) | 2026-08-09 05:19 UTC | 2026-08-09 05:59 UTC | 39m |
| CRK658 | CRK | Chek Lap Kok International Airport (VHHH) | Kerama Airport (ROKR) | 2026-08-09 03:55 UTC | 2026-08-09 05:58 UTC | 2h 3m |
| AIQ3552 | AIQ | Don Mueang International Airport (VTBD) | Nan Airport (VTCN) | 2026-08-09 05:10 UTC | 2026-08-09 05:57 UTC | 47m |
| QLK324D | QLK | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-08-09 05:30 UTC | 2026-08-09 05:57 UTC | 26m |
| AIZ803 | AIZ | Ben Gurion International Airport (LLBG) | Ein Yahav Airfield (LLEY) | 2026-08-09 05:31 UTC | 2026-08-09 05:56 UTC | 24m |
| AWG120R | AWG | Henri Coanda International Airport (LROP) | Caransebes Airport (LRCS) | 2026-08-09 05:25 UTC | 2026-08-09 05:54 UTC | 28m |
| SWR4DX | Swiss International | Geneva Cointrin International Airport (LSGG) | Zurich Airport (LSZH) | 2026-08-09 05:23 UTC | 2026-08-09 05:54 UTC | 30m |
| LNI172 | LNI | Soekarno-Hatta International Airport (WIII) | Batujajar Airport (WI1B) | 2026-08-09 05:37 UTC | 2026-08-09 05:52 UTC | 14m |
| QLK225D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Tumut Airport (YTMU) | 2026-08-09 05:16 UTC | 2026-08-09 05:50 UTC | 33m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-09 05:39 UTC | 2026-08-09 05:49 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
