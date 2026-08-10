# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_10:32:32_UTC-green)

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

**Latest saved flight:** 2026-08-10 10:32:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-10 10:32:32 UTC

- **183,655** saved flights
- **58,534** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **183,655** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,207,754.8 tonnes** estimated CO2 emissions
- **127,985,782 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7283 |
| 2 | SkyWest Airlines | 6684 |
| 3 | EJA | 3629 |
| 4 | IndiGo | 3217 |
| 5 | Southwest Airlines | 2882 |
| 6 | American Airlines | 2868 |
| 7 | ENY | 2290 |
| 8 | Delta Air Lines | 2172 |
| 9 | LATAM Airlines | 1716 |
| 10 | AZU | 1646 |
| 11 | Lufthansa | 1621 |
| 12 | WIF | 1520 |
| 13 | Vueling | 1513 |
| 14 | LXJ | 1451 |
| 15 | Swiss International | 1259 |
| 16 | easyJet | 1258 |
| 17 | AXM | 1232 |
| 18 | QLK | 1134 |
| 19 | EJU | 1127 |
| 20 | All Nippon Airways | 1122 |
| 21 | Alaska Airlines | 1104 |
| 22 | VIV | 1012 |
| 23 | GLO | 984 |
| 24 | AEE | 957 |
| 25 | Air France | 953 |
| 26 | CXK | 953 |
| 27 | Cathay Pacific | 947 |
| 28 | United Airlines | 940 |
| 29 | PGT | 934 |
| 30 | MXY | 915 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 156986 |
| 2 | 🇪🇸 ES | 11792 |
| 3 | 🇧🇷 BR | 10535 |
| 4 | 🇦🇺 AU | 10294 |
| 5 | 🇮🇳 IN | 10075 |
| 6 | 🇨🇦 CA | 9995 |
| 7 | 🇮🇹 IT | 9494 |
| 8 | 🇩🇪 DE | 9087 |
| 9 | 🇬🇧 GB | 8517 |
| 10 | 🇯🇵 JP | 7486 |
| 11 | 🇫🇷 FR | 7318 |
| 12 | 🇨🇴 CO | 6865 |
| 13 | 🇬🇷 GR | 5382 |
| 14 | 🇲🇽 MX | 5248 |
| 15 | 🇨🇭 CH | 4902 |
| 16 | 🇹🇷 TR | 4787 |
| 17 | 🇳🇴 NO | 4726 |
| 18 | 🇲🇾 MY | 3208 |
| 19 | 🇵🇱 PL | 3073 |
| 20 | 🇿🇦 ZA | 3059 |
| 21 | 🇹🇭 TH | 2835 |
| 22 | 🇳🇿 NZ | 2629 |
| 23 | 🇵🇭 PH | 2433 |
| 24 | 🇬🇹 GT | 2351 |
| 25 | 🇰🇷 KR | 2283 |
| 26 | 🇲🇦 MA | 1853 |
| 27 | 🇭🇷 HR | 1836 |
| 28 | 🇲🇪 ME | 1659 |
| 29 | 🇳🇱 NL | 1647 |
| 30 | 🇲🇴 MO | 1520 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3808 |
| 2 | Denver International Airport |  | US | 3036 |
| 3 | Tokyo International Airport |  | JP | 2320 |
| 4 | Indira Gandhi International Airport |  | IN | 2257 |
| 5 | Guaymaral Airport |  | CO | 2236 |
| 6 | Harry Reid International Airport |  | US | 2149 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1968 |
| 8 | Zurich Airport |  | CH | 1962 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1908 |
| 10 | La Aurora Airport |  | GT | 1804 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1673 |
| 12 | El Dorado International Airport |  | CO | 1646 |
| 13 | Salt Lake City International Airport |  | US | 1638 |
| 14 | Chicago O'Hare International Airport |  | US | 1637 |
| 15 | Frankfurt am Main International Airport |  | DE | 1586 |
| 16 | Congonhas Airport |  | BR | 1528 |
| 17 | Macau International Airport |  | MO | 1520 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1450 |
| 19 | Madrid Barajas International Airport |  | ES | 1442 |
| 20 | Capua Airport |  | IT | 1435 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1373 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1314 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1288 |
| 24 | Malpensa International Airport |  | IT | 1272 |
| 25 | Charles de Gaulle International Airport |  | FR | 1253 |
| 26 | Charlotte/Douglas International Airport |  | US | 1245 |
| 27 | Kuala Lumpur International Airport |  | MY | 1204 |
| 28 | Bengaluru International Airport |  | IN | 1193 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1148 |
| 30 | Ninoy Aquino International Airport |  | PH | 1147 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1129 |
| 32 | Barcelona International Airport |  | ES | 1086 |
| 33 | Seattle-Tacoma International Airport |  | US | 1057 |
| 34 | Viracopos International Airport |  | BR | 1054 |
| 35 | Reno/Tahoe International Airport |  | US | 1049 |
| 36 | Daniel K Inouye International Airport |  | US | 1046 |
| 37 | Calgary International Airport |  | CA | 1046 |
| 38 | Oslo Gardermoen Airport |  | NO | 1019 |
| 39 | Tenerife Norte Airport |  | ES | 1001 |
| 40 | Amsterdam Airport Schiphol |  | NL | 994 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 922 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 674 | 21m | 244 km | 2,838.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 440 | 1h 8m | 770 km | 5,845.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 430 | 24m | 225 km | 1,668.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 427 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 327 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 308 | 27m | 275 km | 1,459.5 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 299 | 1h 7m | 706 km | 3,640.3 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 272 | 44m | 241 km | 1,129.8 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 267 | 22m | 55 km | 253.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 259 | 1h 48m | 1,423 km | 6,356.3 t |
| 15 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 255 | 8m | - | - |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 248 | 20m | 250 km | 1,071.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 231 | 26m | 215 km | 855.5 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 231 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 226 | 19m | 99 km | 387.1 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 224 | 1h 15m | 961 km | 3,712.9 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 224 | 12m | - | - |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 221 | 31m | 49 km | 186.8 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 220 | 50m | 556 km | 2,108.9 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 220 | 19m | 144 km | 547.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 217 | 1h 38m | 1,156 km | 4,329.1 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 215 | 24m | 218 km | 810.0 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 213 | 31m | 369 km | 1,355.8 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 201 | 1h 1m | 695 km | 2,409.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HASJF | HAS | Budaors Glider Airport (LHBS) | Farkashegy Airport (LHFH) | 2026-08-10 10:17 UTC | 2026-08-10 10:32 UTC | 14m |
| THA619 | Thai Airways | Simao Airport (ZPSM) | VTBH (VTBH) | 2026-08-10 09:28 UTC | 2026-08-10 10:28 UTC | 1h 0m |
| CFZMK | CFZ | Tejgaon Airport (VGTJ) | Tejgaon Airport (VGTJ) | 2026-08-10 09:48 UTC | 2026-08-10 10:14 UTC | 25m |
| AWG720F | AWG | Henri Coanda International Airport (LROP) | Istanbul Hezarfen Airfield (LTBW) | 2026-08-10 09:25 UTC | 2026-08-10 10:01 UTC | 36m |
| FHGYO | FHG | Annecy-Haute-Savoie-Mont Blanc Airport (LFLP) | Bourg-Ceyzeriat Airport (LFHS) | 2026-08-10 09:23 UTC | 2026-08-10 09:55 UTC | 32m |
| ZSORP | ZSO | O. R. Tambo International Airport (FAOR) | Rooiberg Airport (FARO) | 2026-08-10 09:16 UTC | 2026-08-10 09:50 UTC | 33m |
| SWR2TM | Swiss International | Malpensa International Airport (LIMC) | Zurich Airport (LSZH) | 2026-08-10 09:06 UTC | 2026-08-10 09:43 UTC | 36m |
| CFE91C | CFE | London City Airport (EGLC) | Dublin Airport (EIDW) | 2026-08-10 08:38 UTC | 2026-08-10 09:40 UTC | 1h 1m |
| AIC6LX | Air India | Indira Gandhi International Airport (VIDP) | Ambala Air Force Station (VIAM) | 2026-08-10 09:08 UTC | 2026-08-10 09:37 UTC | 28m |
| ITY066 | ITY | Linate Airport (LIML) | Ibiza Airport (LEIB) | 2026-08-10 08:01 UTC | 2026-08-10 09:36 UTC | 1h 35m |
| RYR674 | Ryanair | Vienna International Airport (LOWW) | Trstenik Airport (LYTR) | 2026-08-10 08:44 UTC | 2026-08-10 09:32 UTC | 47m |
| EWG3GJ | EWG | Palma De Mallorca Airport (LEPA) | Munich International Airport (EDDM) | 2026-08-10 07:47 UTC | 2026-08-10 09:31 UTC | 1h 44m |
| TVF37NP | TVF | Paris-Orly Airport (LFPO) | Kasteli Airport (LGTL) | 2026-08-10 06:40 UTC | 2026-08-10 09:31 UTC | 2h 50m |
| VUAVT | VUA | Indira Gandhi International Airport (VIDP) | Chandigarh Airport (VICG) | 2026-08-10 08:59 UTC | 2026-08-10 09:30 UTC | 31m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Sandane Airport Anda (ENSD) | 2026-08-10 09:08 UTC | 2026-08-10 09:30 UTC | 21m |
| NOZ7TE | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Bardufoss Airport (ENDU) | 2026-08-10 08:10 UTC | 2026-08-10 09:26 UTC | 1h 15m |
| SFR259 | SFR | Kroonstad Airport (FAKS) | Rand Airport (FAGM) | 2026-08-10 09:09 UTC | 2026-08-10 09:26 UTC | 17m |
| SXS8RG | SXS | Antalya International Airport (LTAI) | Berlin Brandenburg Airport (EDDB) | 2026-08-10 06:22 UTC | 2026-08-10 09:25 UTC | 3h 2m |
| QLK1581 | QLK | Sunshine Coast Airport (YBMC) | Sydney Kingsford Smith International Airport (YSSY) | 2026-08-10 07:54 UTC | 2026-08-10 09:23 UTC | 1h 28m |
| FDB869 | flydubai | Dubai International Airport (OMDB) | Ras Tanura Airport (OERT) | 2026-08-10 08:30 UTC | 2026-08-10 09:21 UTC | 50m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
