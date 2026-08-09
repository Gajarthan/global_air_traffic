# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_15:01:02_UTC-green)

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

**Latest saved flight:** 2026-08-09 15:01:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 15:01:02 UTC

- **181,300** saved flights
- **57,921** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **181,300** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,179,248.2 tonnes** estimated CO2 emissions
- **126,333,230 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7192 |
| 2 | SkyWest Airlines | 6583 |
| 3 | EJA | 3556 |
| 4 | IndiGo | 3182 |
| 5 | Southwest Airlines | 2843 |
| 6 | American Airlines | 2819 |
| 7 | ENY | 2251 |
| 8 | Delta Air Lines | 2144 |
| 9 | LATAM Airlines | 1694 |
| 10 | AZU | 1626 |
| 11 | Lufthansa | 1613 |
| 12 | Vueling | 1502 |
| 13 | WIF | 1501 |
| 14 | LXJ | 1407 |
| 15 | easyJet | 1241 |
| 16 | Swiss International | 1240 |
| 17 | AXM | 1226 |
| 18 | QLK | 1116 |
| 19 | EJU | 1110 |
| 20 | All Nippon Airways | 1107 |
| 21 | Alaska Airlines | 1097 |
| 22 | VIV | 998 |
| 23 | GLO | 968 |
| 24 | CXK | 949 |
| 25 | AEE | 947 |
| 26 | Cathay Pacific | 947 |
| 27 | Air France | 938 |
| 28 | United Airlines | 930 |
| 29 | PGT | 911 |
| 30 | MXY | 909 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 154934 |
| 2 | 🇪🇸 ES | 11681 |
| 3 | 🇧🇷 BR | 10410 |
| 4 | 🇦🇺 AU | 10202 |
| 5 | 🇮🇳 IN | 9978 |
| 6 | 🇨🇦 CA | 9862 |
| 7 | 🇮🇹 IT | 9383 |
| 8 | 🇩🇪 DE | 8993 |
| 9 | 🇬🇧 GB | 8393 |
| 10 | 🇯🇵 JP | 7379 |
| 11 | 🇫🇷 FR | 7227 |
| 12 | 🇨🇴 CO | 6728 |
| 13 | 🇬🇷 GR | 5313 |
| 14 | 🇲🇽 MX | 5172 |
| 15 | 🇨🇭 CH | 4847 |
| 16 | 🇹🇷 TR | 4680 |
| 17 | 🇳🇴 NO | 4670 |
| 18 | 🇲🇾 MY | 3195 |
| 19 | 🇵🇱 PL | 3046 |
| 20 | 🇿🇦 ZA | 2998 |
| 21 | 🇹🇭 TH | 2802 |
| 22 | 🇳🇿 NZ | 2608 |
| 23 | 🇵🇭 PH | 2410 |
| 24 | 🇬🇹 GT | 2301 |
| 25 | 🇰🇷 KR | 2263 |
| 26 | 🇲🇦 MA | 1831 |
| 27 | 🇭🇷 HR | 1808 |
| 28 | 🇲🇪 ME | 1644 |
| 29 | 🇳🇱 NL | 1632 |
| 30 | 🇲🇴 MO | 1518 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3735 |
| 2 | Denver International Airport |  | US | 2988 |
| 3 | Tokyo International Airport |  | JP | 2287 |
| 4 | Indira Gandhi International Airport |  | IN | 2228 |
| 5 | Guaymaral Airport |  | CO | 2224 |
| 6 | Harry Reid International Airport |  | US | 2127 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1951 |
| 8 | Zurich Airport |  | CH | 1935 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1878 |
| 10 | La Aurora Airport |  | GT | 1767 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1648 |
| 12 | Chicago O'Hare International Airport |  | US | 1626 |
| 13 | Salt Lake City International Airport |  | US | 1617 |
| 14 | El Dorado International Airport |  | CO | 1616 |
| 15 | Frankfurt am Main International Airport |  | DE | 1575 |
| 16 | Macau International Airport |  | MO | 1518 |
| 17 | Congonhas Airport |  | BR | 1508 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1439 |
| 19 | Madrid Barajas International Airport |  | ES | 1428 |
| 20 | Capua Airport |  | IT | 1418 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1352 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1296 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1270 |
| 24 | Malpensa International Airport |  | IT | 1251 |
| 25 | Charles de Gaulle International Airport |  | FR | 1233 |
| 26 | Charlotte/Douglas International Airport |  | US | 1226 |
| 27 | Kuala Lumpur International Airport |  | MY | 1201 |
| 28 | Bengaluru International Airport |  | IN | 1185 |
| 29 | Ninoy Aquino International Airport |  | PH | 1135 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1125 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1110 |
| 32 | Barcelona International Airport |  | ES | 1080 |
| 33 | Viracopos International Airport |  | BR | 1045 |
| 34 | Daniel K Inouye International Airport |  | US | 1041 |
| 35 | Seattle-Tacoma International Airport |  | US | 1041 |
| 36 | Reno/Tahoe International Airport |  | US | 1032 |
| 37 | Calgary International Airport |  | CA | 1030 |
| 38 | Oslo Gardermoen Airport |  | NO | 1004 |
| 39 | Tenerife Norte Airport |  | ES | 992 |
| 40 | Vitoria/Foronda Airport |  | ES | 984 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 918 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 670 | 21m | 244 km | 2,821.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 434 | 1h 8m | 770 km | 5,765.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 428 | 24m | 225 km | 1,660.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 418 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 327 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 306 | 27m | 275 km | 1,450.0 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 298 | 1h 7m | 706 km | 3,628.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 271 | 44m | 241 km | 1,125.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 255 | 1h 48m | 1,423 km | 6,258.1 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 244 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 240 | 20m | 250 km | 1,036.7 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 228 | 26m | 215 km | 844.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 223 | 19m | 99 km | 382.0 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 219 | 31m | 49 km | 185.1 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 219 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 218 | 1h 15m | 961 km | 3,613.5 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 218 | 50m | 556 km | 2,089.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 217 | 19m | 144 km | 539.8 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 214 | 1h 38m | 1,156 km | 4,269.2 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 211 | 31m | 369 km | 1,343.1 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 210 | 24m | 218 km | 791.2 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 203 | 28m | 152 km | 530.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 197 | 1h 1m | 695 km | 2,361.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| Y44 |  | Wethersfield Airport (EGVT) | Wethersfield Airport (EGVT) | 2026-08-09 14:39 UTC | 2026-08-09 15:01 UTC | 21m |
| N12772 |  | Rocky Mountain Metro Airport (KBJC) | Laramie Regional Airport (KLAR) | 2026-08-09 14:00 UTC | 2026-08-09 14:58 UTC | 58m |
| N10RP |  | Centennial Airport (KAPA) | Cuchara Ranch Airport (CD48) | 2026-08-09 14:06 UTC | 2026-08-09 14:57 UTC | 51m |
| CXK268 | CXK | Raleigh Executive Jetport At Sanford-Lee County Airport (KTTA) | Moore County Airport (KSOP) | 2026-08-09 14:34 UTC | 2026-08-09 14:55 UTC | 20m |
| SCU34 | SCU | 2OL2 (2OL2) | Haskell Airport (K2K9) | 2026-08-09 14:40 UTC | 2026-08-09 14:51 UTC | 10m |
| N759ZH |  | Martha's Vineyard Airport (KMVY) | Pheasant Field (MA64) | 2026-08-09 14:29 UTC | 2026-08-09 14:51 UTC | 21m |
| N484CW |  | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | Singleton Airport (97VA) | 2026-08-09 14:28 UTC | 2026-08-09 14:48 UTC | 19m |
| RAM802L | Royal Air Maroc | Mohammed V International Airport (GMMN) | London Gatwick Airport (EGKK) | 2026-08-09 12:02 UTC | 2026-08-09 14:44 UTC | 2h 42m |
| C6058 |  | Point Mugu Nas (Naval Base Ventura Co) Airport (KNTD) | Oxnard Airport (KOXR) | 2026-08-09 12:58 UTC | 2026-08-09 14:42 UTC | 1h 44m |
| CXK111 | CXK | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-08-09 14:24 UTC | 2026-08-09 14:39 UTC | 15m |
| XBVNY | XBV | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-08-09 13:49 UTC | 2026-08-09 14:34 UTC | 45m |
| NJE393P | NJE | Gothenburg-Landvetter Airport (ESGG) | Samedan Airport (LSZS) | 2026-08-09 12:47 UTC | 2026-08-09 14:34 UTC | 1h 46m |
| CHX42 | CHX | Pellworm Airport (EDHP) | Husum-Schwesing Airport (EDXJ) | 2026-08-09 14:25 UTC | 2026-08-09 14:33 UTC | 7m |
| RYR164G | Ryanair | Pisa / San Giusto - Galileo Galilei International Airport (LIRP) | Chania International Airport (LGSA) | 2026-08-09 12:36 UTC | 2026-08-09 14:33 UTC | 1h 56m |
| N999VP |  | Vogen Airport (IS41) | IS95 (IS95) | 2026-08-09 13:40 UTC | 2026-08-09 14:32 UTC | 52m |
| N469TS |  | Hen & Bacon Airport (90VA) | Orange County Airport (KOMH) | 2026-08-09 14:12 UTC | 2026-08-09 14:27 UTC | 15m |
| SWR15Y | Swiss International | Brussels Airport (EBBR) | Zurich Airport (LSZH) | 2026-08-09 13:31 UTC | 2026-08-09 14:27 UTC | 56m |
| RYR4LW | Ryanair | Sofia Airport (LBSF) | Chania International Airport (LGSA) | 2026-08-09 13:17 UTC | 2026-08-09 14:26 UTC | 1h 9m |
| N224JA |  | KU77 (KU77) | K36U (K36U) | 2026-08-09 14:09 UTC | 2026-08-09 14:23 UTC | 14m |
| WING37 | WIN | St Pete-Clearwater International Airport (KPIE) | WV11 (WV11) | 2026-08-09 12:45 UTC | 2026-08-09 14:23 UTC | 1h 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
